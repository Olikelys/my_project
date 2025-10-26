import os
from dotenv import load_dotenv

load_dotenv()


class GreetingService:
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY")

    def greet(self):
        return f"Hello! Secret Key: {self.secret_key[:5]}..."


if __name__ == "__main__":
    service = GreetingService()
    print(service.greet())
