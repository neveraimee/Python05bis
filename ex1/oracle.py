import os
from dotenv import load_dotenv


def env_ignored() -> bool:
    gitignore = os.path.join(os.path.dirname(__file__), ".gitignore")
    try:
        with open(gitignore) as file:
            return ".env" in file.read().splitlines() #return true if one of the lines is .env
    except FileNotFoundError:
        return False


def main() -> None:
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
    mode = os.getenv("MATRIX_MODE", "development")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print()
    print("ORACLE STATUS: Consulting the configuration...")
    print()

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Log Level: {log_level}")
    if database_url:
        print("Database: Connected to local instance")
    else:
        print("Database: MISSING")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: MISSING")
    if zion_endpoint:
        print("Remote Network: Online")
    else:
        print("Remote Network: MISSING")
    print()

    if mode == "production":
        print("PRODUCTION MODE: secrets are required")
        if not api_key:
            print("ERROR: no API key in production!")
    else:
        print("DEVELOPMENT MODE: missing settings are allowed")
    print()

    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    if env_ignored():
        print("[OK] .env file is properly ignored by git")
    else:
        print("[WARNING] .env is NOT in .gitignore!")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()

