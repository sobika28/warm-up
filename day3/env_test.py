
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

api_key = os.getenv("API_KEY")
app_env = os.getenv("APP_ENV")

print("API key loaded:", bool(api_key))
print("Environment:", app_env)
