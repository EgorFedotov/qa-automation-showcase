"""Central configuration read from environment variables (with sane defaults).

Copy .env.example to .env to override locally.
"""
import os

from dotenv import load_dotenv

load_dotenv()

# --- UI (SauceDemo) ---
UI_BASE_URL = os.getenv("UI_BASE_URL", "https://www.saucedemo.com")
UI_USERNAME = os.getenv("UI_USERNAME", "standard_user")
UI_PASSWORD = os.getenv("UI_PASSWORD", "secret_sauce")

# --- API (restful-booker) ---
API_BASE_URL = os.getenv("API_BASE_URL", "https://restful-booker.herokuapp.com")
API_ADMIN_USER = os.getenv("API_ADMIN_USER", "admin")
API_ADMIN_PASSWORD = os.getenv("API_ADMIN_PASSWORD", "password123")
