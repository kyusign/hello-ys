from .config import load_config


def get_token() -> None:
    """Simulate initial authentication using saved credentials."""
    cfg = load_config()
    print("Performing initial authentication...")
    creds = [
        cfg.get("google_client_id"),
        cfg.get("instagram_client_id"),
        cfg.get("tiktok_client_key"),
    ]
    if all(creds):
        print("Credentials loaded. (authentication stub)")
    else:
        print("Missing credentials; authentication skipped")
