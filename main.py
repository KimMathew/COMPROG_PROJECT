from classes import *

accounts = {  #pre-defined accounts
    'Admin': 'password123',
    'Mochu': 'password456',
    'Russel': 'password456',
    'Gian': 'password456',
    'Luna': 'password456'}


while True:
    os.system('cls')
    print("\nDORMI-PY") 
    print("\n[1] Log in")
    print("[2] Exit") 
    user_choice1 = input("\nYour Choice: ")

    if user_choice1 == '1': #Will allow user to input their username and password
        while True:
            os.system('cls')
            current_user = input("\nEnter your username: ")
            password = input("Enter your password: ")
            if current_user in accounts and accounts[current_user] == password:
                print("\nLoading ", end="")
                for i in range(3):
                    time.sleep(1)
                    print(".", end="", flush=True)

                time.sleep(2)
                print(f"\n\nLogin successful!")
                print(f"\nWelcome {current_user}!")
                time.sleep(2)
                break
            else:
                print("\nInvalid username or password! Please Try Again!")
                time.sleep(1)
                continue 
        if current_user == "Admin":  #Will determine if the user is the admin
            admin = Admin(current_user)
            while True:
                os.system('cls')
                admin.options() 
                user_choice2 = input("\nYour Choice: ")
                if user_choice2 == '1': #Allow the admin to create an announcement
                    os.system('cls')
                    time.sleep(0.5)
                    admin.announcement_admin()
                elif user_choice2 == '2': #Allow the admin to add liabilities
                    os.system('cls')
                    time.sleep(0.5)
                    admin.liab_admin()
                elif user_choice2 == '3': #Allow the admin to see the attendance table and the people at dorm
                    os.system('cls')
                    time.sleep(0.5)
                    admin.attendace_table()
                    admin.who_is_at_home()

                elif user_choice2 == '4': #Log-out
                    print("\nLogging out ", end="")
                    for i in range(3):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    time.sleep(1)
                    print("\nYou have logged out.")
                    time.sleep(1.5)
                    break
                else: #Error-handler
                    print("\nInvalid choice. Please try again!")
                    time.sleep(1)
                    continue
        else: #Will determine if the user is a regular
            regular = Regular(current_user)
            flag = True

            while flag == True:
                os.system('cls')
                regular.show_announcement() #Will show the announcement created by the admin
                regular.options() 
                user_choice2 = input("\nYour Choice: ")
                flag2 = True

                while flag2 == True:
                    if user_choice2 == '1': #for Liabilities
                        os.system('cls')
                        regular.reg_liab(current_user)
                        print("[Back]")
                        user_choice3 = input("\nYour Choice: ")
                        if user_choice3 == "Back":
                            os.system('cls')
                            break
                        else:
                            print("\nInvalid choice. Please try again!")
                            time.sleep(1)
                            continue
                    elif user_choice2 == '2': #for Attendance
                        os.system('cls')
                        print("\n[1] Time-in")
                        print("[2] Time-out")
                        print("[3] Who's currently at home?")
                        print("[4] Back")
                        user_choice3 = input("\nYour Choice: ")
                        if user_choice3 == '1': #Allow the user to time-in
                            present = "Time-in"
                            regular.attendance_checker(present, user_choice3)
                            time.sleep(1.5)
                        elif user_choice3 == '2': #Allow the user to time-out 
                            present = "Time-out"
                            regular.attendance_checker(present, user_choice3)
                            time.sleep(1.5)
                        elif user_choice3 == '3':  #Allow the user to see the people currently at dorm
                            os.system('cls')
                            regular.who_is_at_home()

                        elif user_choice3 == '4': #back
                            break
                        else: 
                            print("\nInvalid choice. Please try again!")
                            continue
                    elif user_choice2 == '3': #Log-out
                        print("\nLogging out ", end="")
                        for i in range(3):
                            time.sleep(1)
                            print(".", end="", flush=True)
                        time.sleep(1)
                        print("\nYou have logged out.")
                        time.sleep(1.5)
                        flag2 = False
                        flag = False
                    else: 
                        print("\nInvalid choice. Please try again!")
                        break
    elif user_choice1 == '2': #Exit the system
        sys.exit()
    else: #Error-handler
        print("\nInvalid choice! Please Try Again!")
        time.sleep(1)
