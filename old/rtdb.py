from firebase import firebase
from dotenv import load_dotenv
import os

load_dotenv(".env")
database_url = os.environ.get("DATABASE_URL")

menu = """
Make a change to the RTDB!
[1] Get data
[2] Post data
[0] Quit
"""

class RTDB():
    app = firebase.FirebaseApplication(database_url, None)

    def run(self):
        print("Welcome to Realtime Database!")
        while True:
            print(menu)
            num = input("What will it be: ")

            if num == "1":
                print("Getting data...")
                print(self.app.get("/", None))

            elif num == "2":
                print("Posting data...")
                key = input("Enter key:   ")
                value = input("Enter value: ")
                self.app.put("/", key, value)
            elif num == "0":
                break

