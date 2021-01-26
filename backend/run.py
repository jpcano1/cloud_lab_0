from src import app
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

if __name__ == "__main__":
    app.run(
        port=os.getenv("PORT", 3000),
        host=os.getenv("HOST", "localhost")
    )