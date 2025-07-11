# SNS Dashboard

SNS Dashboard는 **YouTube · TikTok · Instagram** 채널의 일일 조회수를 수집해
예상 수익을 계산하고, GUI로 API 자격 증명을 손쉽게 저장할 수 있는 파이썬 애플리케이션입니다.  
설정 값과 채널 정보는 `config.json`에 보관되며, 다른 모듈에서 재사용할 수 있습니다.

---

## Usage

### 1. 의존성 설치

```bash
pip install -r requirements.txt


# 방법 1
python -m sns_dashboard setup

# 방법 2
python -m sns_dashboard.main setup

# 방법 3 (스크립트 직접 실행)
python sns_dashboard/main.py setup

sns-dashboard.exe setup

python -m sns_dashboard run

python -m sns_dashboard plot


필요한 게 README 외 다른 충돌 파일(`config.json`, `sns_dashboard/gui.py`, `sns_dashboard/main.py`)도 있으면 알려 주세요!
