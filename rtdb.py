from firebase import firebase

menu = """
Make a change to the RTDB!
[0] Get data
[1] Post data
"""

class RTDB():
    app = firebase.FirebaseApplication('https://test-12ddf-default-rtdb.firebaseio.com/', None)

    def run(self):
        print("Welcome to Realtime Database!")
        while True:
            print(menu)
            num = input("What will it be: ")

            if num == "0":
                print("Getting data...")
                print(self.app.get("/", None))

            elif num == "1":
                print("Posting data...")
                key = input("Enter key:   ")
                value = input("Enter value: ")
                self.app.put("/", key, value)

