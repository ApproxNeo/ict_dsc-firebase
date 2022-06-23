import pyrebase
import dotenv
import os
from getpass import *


dotenv.load_dotenv()

config = {
  "apiKey": os.environ.get("API_KEY"),
  "authDomain": os.environ.get("AUTH_DOMAIN"),
  "databaseURL": os.environ.get("DATABASE_URL"),
  "storageBucket": os.environ.get("STORAGE_BUCKET")
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

menuMain = """
[1] Login
[2] Register
[3] RealTime DB
[0] Quit
"""

menuDatabase = """
[1] Get all data
[2] Post data
[0] Back to main menu
"""

def login():
  print("Logging on...")
  email = input("Enter email: ")
  password = getpass('Enter password: ')
  print(email, password)
  try:
    auth.sign_in_with_email_and_password(email, password)
  except:
    print("Login failed")

def register():
  print("Enter details:")
  email = input("Enter email: ")
  password = getpass('Enter password: ')
  print(email, password)
  try:
    auth.create_user_with_email_and_password(email, password)
    print("Login success!")
  except:
    print("Login failed...")

def database():
  while True:
    print(menuDatabase)
    choice = input("Database action: ")
    if choice == "0":
      break
    elif choice == "1":
      print("Getting data...")
      data = db.child("/").get()
      print(data.val())
    elif choice =="2":
      print("Posting data...")
      key = input("Key: ")
      value = input("Value: ")
      try:
        db.child("/").child(key).set(value)
      except:
        print("Post data error!")


while True:
  print("Hello! Welcome to Firebase\n")
  if auth.current_user != None:
    print("Hello, {}".format(auth.current_user['email']))
  print(menuMain)
  choice = input("What will it be: ")
  if choice == "0":
    break
  elif choice == "1":
    login()
  elif choice == "2":
    register()
  elif choice == "3":
    database()

    

    
