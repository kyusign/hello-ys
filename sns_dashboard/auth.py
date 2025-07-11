"""
auth.py

Minimal placeholder for future authentication.

현재 SNS Dashboard는 공개 채널 조회수만 가져오기 때문에
별도의 API 인증이 필요하지 않습니다. 나중에 OAuth 키 등을
추가하게 되면 이 모듈에서 처리하도록 남겨 둡니다.
"""


def get_token() -> None:
    """No-op authentication stub."""
    print("Authentication not required for minimal configuration.")
