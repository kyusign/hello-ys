import json
import os
from typing import Any, Dict

# config.json 경로
CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")

# 기본 값
DEFAULT_CONFIG = {
    "youtube_url": "",
    "tiktok_url": "",
    "instagram_url": "",
    "rates": {
        "youtube": 0.0,
        "tiktok": 0.0,
        "instagram": 0.0,
    },
}

# ──────────────────────────────────────────────────────────────
# 헬퍼 함수
# ──────────────────────────────────────────────────────────────
def config_exists() -> bool:
    """config.json 파일 존재 여부"""
    return os.path.exists(CONFIG_PATH)


def is_config_complete(cfg: Dict[str, Any]) -> bool:
    """필수 URL 3개가 모두 채워졌는지 확인"""
    required = ["youtube_url", "tiktok_url", "instagram_url"]
    return all(cfg.get(k) for k in required)


def load_config() -> Dict[str, Any]:
    """config.json 로드 (없으면 기본 값 반환)"""
    if not config_exists():
        return DEFAULT_CONFIG.copy()
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(cfg: Dict[str, Any]) -> None:
    """config.json 저장"""
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)
