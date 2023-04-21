accounts = { #from database
    'admin': 'password123',  
    'user': 'password456'    
}

class Admin:
    def __init__(self, username):
        self.username = username
        print(f"\nWelcome {username}!")

class Regular(Admin):
    def __init__(self, username):
        self.username = username
        print(f"\nWelcome {username}!")
    
    def attendance_checker(self, username, time_in):
        reasons_collection = ("School", "Meeting with Friends", "Meeting with family", "Going Home", "Buy Grocery", "Other Reason")

        if time_in:
            print(f"\n{username} is Time-in!")
        else:
            print("\nSelect your reason for leaving: ")
            for i, reason in enumerate(reasons_collection):
                print(f"[{i+1}] {reason}")

            main_reason = int(input("\nYour Choice: "))
            reason = reasons_collection[main_reason-1] if main_reason <= 5 else input("Please specify your reason for leaving: ")
            print(f"\n{username} is Time-out! Reason:", reason)

#Login Page
print("\nDORMI-PY")

while True:
    current_user = input("\nEnter your username: ")
    password = input("Enter your password: ")

    if current_user in accounts and accounts[current_user] == password:
        print("\nLogin successful!")
        break

    else:
        print("\nInvalid username or password! Please Try Again!")

if current_user == "admin": #from database
    admin = Admin(current_user)

else:
    regular = Regular(current_user)
    flag = True 

    while flag:
        print (f"\n[3] Attendance")
        user_choice1 = int(input("\nYour Choice: "))

        while True:
            if user_choice1 == 3:
                print("\n[1] Time-in")
                print("[2] Time-out")
                print("[3] Who's currently at home?")
                print("[4] Back")

                user_choice2 = int(input("\nYour Choice: "))

                if user_choice2 == 1:
                    regular.attendance_checker(current_user, True)
                elif user_choice2 == 2:
                    regular.attendance_checker(current_user, False)
                elif user_choice2 == 3: # Who's currently at home
                    pass
                elif user_choice2 == 4:
                    break
                else:
                    print("\nInvalid choice. Please try again!")

            else:
                print("\nInvalid choice. Please try again!")
                break
    
    