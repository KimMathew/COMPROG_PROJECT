from classes import *
from libs.announcement import *

accounts = {  #pre-defined accounts
    'admin': 'password123',
    'Gelo': 'password456',
    'Elwin': 'password456',
    'Mochu': 'password456',
    'Jawo': 'password456',
    'Diola': 'password456',
    'Russel': 'password456',
    'Gian': 'password456',
    'Boris': 'password456',
    'Luna': 'password456',
    'Gab': 'password456',
}

while True:
    print("\nDORMI-PY") #Log-in Page
    print("\n[1] Log in")
    print("[2] Exit") 

    user_choice1 = int(input("\nYour Choice: "))

    if user_choice1 == 1: #Will allow user to input their username and password
        while True:
            current_user = input("\nEnter your username: ")
            password = input("Enter your password: ")

            if current_user in accounts and accounts[current_user] == password:
                print("\nLogin successful!")
                break

            else:
                print("\nInvalid username or password! Please Try Again!")
                continue 

        if current_user == "admin":  #Will determine if the user is the admin
            admin = Admin(current_user)
            print(f"\nWelcome {current_user}!")

            while True:
                show_announcement() #Display the announcements created by the admin
                options() #Display the options of the admin
                user_choice2 = int(input("\nYour Choice: "))

                if user_choice2 == 1: #Allow the admin to create an announcement
                    create_announcement()
                
                elif user_choice2 == 2: #Allow the admin to add liabilities
                    pass

                elif user_choice2 == 3: #Allow the admin to see the attendance table and the people at dorm
                    admin = Admin(current_user)
                    admin.attendace_table()
                    admin.who_is_at_home()

                elif user_choice2 == 4: #Log-out
                    break

                else: #Error-handler
                    print("\nInvalid choice. Please try again!")
                    continue
        
        else: #Will determine if the user is a regular
            regular = Regular(current_user)
            print(f"\nWelcome {current_user}!")

            flag = True

            while flag == True:
                show_announcement() #Will show the announcement created by the admin
                options() #Display the options of the regular
                user_choice2 = int(input("\nYour Choice: "))
                
                flag2 = True

                while flag2 == True:
                    if user_choice2 == 3:
                        print("\n[1] Time-in")
                        print("[2] Time-out")
                        print("[3] Who's currently at home?")
                        print("[4] Back")

                        user_choice3 = int(input("\nYour Choice: "))

                        if user_choice3 == 1: #Allow the user to time-in
                            present = "Time-in"
                            regular.attendance_checker(present, user_choice3)

                        elif user_choice3 == 2: #Allow the user to time-out 
                            present = "Time-out"
                            regular.attendance_checker(present, user_choice3)

                        elif user_choice3 == 3:  #Allow the user to see the people currently at dorm
                            regular = Regular(current_user)
                            regular.who_is_at_home()

                        elif user_choice3 == 4: #back
                            break

                        else: #Error-handler
                            print("\nInvalid choice. Please try again!")
                            continue

                    elif user_choice2 == 4: #Log-out
                        flag2 = False
                        flag = False

                    else: #Error-handler
                        print("\nInvalid choice. Please try again!")
                        break
    
    elif user_choice1 == 2: #Exit the system
        sys.exit()
        
    else: #Error-handler
        print("\nInvalid choice! Please Try Again!")


