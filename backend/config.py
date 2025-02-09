import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API keys
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
