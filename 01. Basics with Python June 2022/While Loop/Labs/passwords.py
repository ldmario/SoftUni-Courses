user_name = input()
password = input()
user_password = ""
while True:
    user_password = input()
    if user_password == password:
        print(f"Welcome {user_name}!")
        break
