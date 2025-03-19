import os
from dotenv import load_dotenv, find_dotenv

# Detect the environment from an ENV variable

def load_env():
    ENV = os.getenv("APP_ENV", "dev")  # Default to "dev" if not set

    # Map environments to corresponding .env files
    ENV_FILES = {
        "dev": "dev.env",
        "staging": ".env.staging",
        "prod": ".env.prod",
    }

    # Load the correct .env file
    env_file = find_dotenv(ENV_FILES.get(ENV, ".env"))
    load_dotenv(env_file)

    # print(f"Loaded environment file: {env_file}")
    # print(f"AWS Region: {os.getenv('AWS_REGION')}")

load_env()