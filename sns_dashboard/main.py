import os
import sys
import time
import typer

# ──────────────────────────────────────────────────────────────
# 패키지 경로 보정 (스크립트 직접 실행 시 절대 임포트 가능하도록)
# ──────────────────────────────────────────────────────────────
if __package__ is None or __package__ == "":
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# 필수 GUI 모듈
from sns_dashboard.gui import run as run_gui

# 선택(존재 여부에 따라) 모듈들
try:
    from sns_dashboard.scheduler import start as start_scheduler
    from sns_dashboard.viz import plot_views
    from sns_dashboard.db import init_db
    from sns_dashboard.config import load_config, config_exists, is_config_complete
except ImportError:
    # 일부 파일이 아직 없다면 안전하게 무시하고 CLI는 제한 기능으로 동작
    start_scheduler = None
    plot_views = None
    init_db = None
    load_config = None
    config_exists = lambda: False
    is_config_complete = lambda _: False

# ──────────────────────────────────────────────────────────────
# Typer CLI 정의
# ──────────────────────────────────────────────────────────────
app = typer.Typer(help="SNS Dashboard Command Line Interface")


@app.callback()
def main() -> None:
    """SNS Dashboard CLI 루트 커맨드(도움말용)."""
    pass


@app.command()
def setup() -> None:
    """설정 GUI 창을 실행합니다."""
    run_gui()


@app.command()
def run() -> None:
    """
    매일 00시에 조회수·수익 데이터를 수집하는 스케줄러를 실행합니다.
    (필요 모듈이 없으면 오류 메시지 후 종료)
    """
    if init_db is None or start_scheduler is None:
        typer.secho("⚠️  스케줄러 관련 모듈이 없어 실행할 수 없습니다.", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)

    init_db()
    start_scheduler()
    try:
        while True:
            time.sleep(1)  # 메인 스레드 유지
    except KeyboardInterrupt:
        typer.echo("\n⏹️  스케줄러가 중단되었습니다.")


@app.command()
def plot() -> None:
    """수집된 조회수 데이터를 그래프로 시각화합니다."""
    if plot_views is None:
        typer.secho("⚠️  시각화 모듈이 없어 실행할 수 없습니다.", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)

    plot_views()


# ──────────────────────────────────────────────────────────────
# 인자 없이 실행했을 때의 자동 동작 결정
#   - config.json 미존재/미완성 ⇒ setup
#   - 완성되어 있으면              ⇒ run
# ──────────────────────────────────────────────────────────────
def _auto_mode() -> None:
    if load_config is None:
        # config 관리 모듈이 없으면 무조건 설정 GUI
        sys.argv.append("setup")
        return

    cfg = load_config() if config_exists() else None
    if cfg is None or not is_config_complete(cfg):
        sys.argv.append("setup")
    else:
        sys.argv.append("run")


# ──────────────────────────────────────────────────────────────
# 진입점
# ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) == 1:
        _auto_mode()
    app()
