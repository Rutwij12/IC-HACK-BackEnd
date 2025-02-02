from dotenv import load_dotenv
import os

load_dotenv()

TEST_ENV = os.getenv("TEST_ENV") == "TEST"
