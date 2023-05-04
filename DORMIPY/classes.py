import csv
import sys
import pandas as pd

user_liabs = {
    'Russel': 'liabs_of_users/russel.txt',
    'Mochu': 'liabs_of_users/mochu.txt',
    'Gian': 'liabs_of_users/gian.txt',
    'Luna': 'liabs_of_users/luna.txt',
}

class Admin:
    def __init__(self, username):
        self.username = username

    def show_announcement(self): #Will show the announcement created by admin
        with open('announcement.txt', 'r') as f:
            announcements = f.readlines()
            if announcements:
                print('\nList of announcements:')
                [print(f'[{i+1}.] {announcement.strip()}') for i, announcement in enumerate(announcements)]
            else:
                print("\nNo Announcement to be shown")

    def announcement_admin(self): #Allow admin to view, create, or remove an announcement
        while True:
            print("\n[1] View all announcements")
            print("[2] Create a new announcement")
            print("[3] Remove an announcement")
            print("[4] Back")

            choice = input("\nYour Choice: ")
            if choice == '1': #View Announcement
                while True:
                    self.show_announcement()
                    choice2 = input("\nType 0 to back: ")

                    if choice2 == '0':
                        break
                    else:
                        print("\nInvalid Choice! Please Try Again!")
                        continue

            elif choice == '2': #Add Announcement
                with open('announcement.txt', 'a') as f:
                    f.write(input("\nWhat do you want to announce? "))
                    f.write("\n")
                    print("\nYour announcement has been added!")
            
            elif choice == '3': #Remove Announcement
                    with open('announcement.txt', 'r') as f:
                        announcements = f.readlines()
                    if announcements:
                        print("List of announcements:")
                        [print(f'[{i+1}] {announcement.strip()}') for i, announcement in enumerate(announcements)]
                        try:
                            to_remove = int(input('\nEnter the number of the announcement you want to remove: '))
                            announcements.pop(to_remove-1)
                            with open('announcement.txt', 'w') as f:
                                f.writelines(announcements)
                            print('\nAnnouncement removed successfully.')
                        except (ValueError, IndexError):
                            print('\nInvalid Choice!')
                    else:
                        print("\nNo Announcement to be removed")

            elif choice == '4':
                print("\nExiting admin announcement...")
                break
            
            else:
                print("\nInvalid input! Please try again")

    def attendace_table(self): #Will show the attendance table of the users
        table = pd.read_csv("attendance.csv")
        print("\n", table, "\n")

    def who_is_at_home(self): #Will display the people at home
        with open('attendance.csv', mode='r', newline='') as csv_file:
            updater = csv.reader(csv_file)
            rows = list(updater)
            for i in range(len(rows)):
                if rows[i][1] == 'Time-in':
                    print(f"{rows[i][0]} is currently at home.")
    
    def liab_admin(self):
        liabilities = {} # Load current liabilities from file
        with open('liabs_of_users/liabilities.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(':')
                if len(parts) != 2:
                    continue
                name, price = parts
                if not price.isdigit():
                    continue
                liabilities[name] = int(price)

        while True:
            print("\nWhat do you want to do?")
            print("[1] Add liability to all")
            print("[2] Remove liability to all")
            print("[3] Assign liability to a specific user")
            print("[4] Remove liability to a specific user")
            print("[5] Back")

            option = input("\nYour Choice: ")

            if option == '1':
                liab_name = input("\nInput the name of liability: ")
                liab_price = input("Price: ")
                price = int(liab_price)
                liabilities[liab_name] = price
                with open('liabs_of_users/liabilities.txt', 'a') as f:
                    f.write(f"{liab_name}:{price}\n")
                print(f"\n{liab_name} has been added with price {price}.")
            elif option == '2':
                while True:
                    with open('liabs_of_users/liabilities.txt', 'r') as f:
                        file_contents = f.read()
                        if len(file_contents) != 0:
                            print("\nWhich liability you want to remove?")
                            for i, name in enumerate(liabilities):
                                print(f"[{i+1}] {name}: {liabilities[name]}")
                            option_1 = input("\nInput the number of the liability you want to remove, or type 0 to cancel: ")

                            if option_1 == '0':
                                break
                            elif option_1.isdigit() and 1 <= int(option_1) <= len(liabilities): 
                                index = int(option_1) - 1
                                name = list(liabilities.keys())[index]
                                del liabilities[name]

                                with open('liabs_of_users/liabilities.txt', 'w') as f:
                                    for name, price in liabilities.items():
                                        f.write(f"{name}:{price}\n")
                                print(f"\n{name} has been removed.")
                                break
                            else:
                                print("\nInvalid input! Please try again!")
                                continue
                        else:
                            print("\nNo liabilities to be removed")
                            print("[Back]") 
                            option_2= input("\nYour Choice: ")

                            if option_2 == 'Back':
                                break          
                            else:
                                print("\nInvalid choice! Please try again!")
                                continue
            elif option == '3':
                while True:
                    print("\nWhich user do you want to assign a liability to?")
                    option_1 = input("Insert his/her username: ")
                    file_dict = {'Mochu': 'liabs_of_users/mochu.txt', # dictionary that maps usernames to filenames
                                'Russel': 'liabs_of_users/russel.txt',
                                'Gian': 'liabs_of_users/gian.txt',
                                'Luna': 'liabs_of_users/luna.txt',}
                
                    if option_1 in file_dict: # check if the entered username is in the dictionary
                        liab_name = input("Input the name of liability: ")
                        liab_price = input("Price: ")
                        price = int(liab_price)
                        liabilities[liab_name] = price

                        with open(file_dict[option_1], 'a') as f:
                            f.write(f"{liab_name}:{price}\n")
                        print(f"\n{liab_name} has been added with price {price}.")
                        break
                    else:
                        print("\nInvalid username! Please try again!")
                        continue
            elif option == '4':
                username_to_file = {
                    'Russel': 'liabs_of_users/russel.txt',
                    'Mochu': 'liabs_of_users/mochu.txt',
                    'Gian': 'liabs_of_users/gian.txt',
                    'Luna': 'liabs_of_users/luna.txt',
                }

                flag = True 
                while flag == True:
                    option_1 = input("\nEnter the username of the person from whom you want to remove a liability: ")
                    filename = username_to_file.get(option_1)

                    if filename:
                        with open(filename, 'r') as file1:
                            liab1 = file1.read().strip()

                        flag1 = True
                        while flag1 == True:
                            if not liab1:
                                print("\nNo liabilities to be removed")
                                print("[Back]") 
                                option_2 = input("\nYour Choice: ")

                                if option_2 == "Back":
                                    flag1 = False
                                    flag = False
                                    break
                                else:
                                    print("\nInvalid choice. Please try again!")
                                    continue

                            with open('liabs_of_users/liabilities.txt', 'r') as file2:
                                liab2 = file2.read()

                            liab_all = liab1 + liab2
                            liab_list = liab_all.split('\n')  # convert to list of liabilities
                            print("\nThe following liabilities are currently listed:")

                            for i, liab in enumerate(liab_list):
                                print(f"[{i+1}] {liab}")

                            item_number = int(input("\nEnter the corresponding number of the liability you want to remove: "))
                            try:
                                item_to_remove = liab_list[item_number-1]  # get the specified item
                            except IndexError:
                                print("\nInvalid input! Please try again!")
                                continue  

                            liab_list.remove(item_to_remove)  # remove the specified item
                            liab_all = '\n'.join(liab_list)  # convert back to string

                            with open(filename, 'w') as file1:
                                file1.write(liab_all)

                            with open('liabs_of_users/liabilities.txt', 'w') as file2:
                                file2.write(liab_all)

                            print(f"\n{item_to_remove} has been removed successfully.")
                            flag1 = False
                            flag = False
                            break

                    else:
                        print("\nInvalid username!")
                        continue

            elif option == '5':
                break
            else:
                print("\nInvalid input! Please try again")
                continue

    def options(self): #Options of Admin in Home Page
        print("\n[1] Make an Announcement")
        print("[2] Add/Remove Liabilities")
        print("[3] View Attendance")
        print("[4] Log out")

class Regular(Admin):
    def __init__(self, username):
        self.username = username

    def attendance_checker(self, status, choice):
        with open('attendance.csv', mode='r', newline='') as csv_file: # update on csv
            updater = csv.reader(csv_file)
            rows = list(updater)

            for i in range(len(rows)): # updating the status
                if self.username in rows[i]:
                    rows[i][1] = status
                    break

            reasons_collection = ( # updating the reasons
                "School", "Meeting with Friends", "Meeting with family", "Going Home", "Buy Grocery", "Other Reason")
            
            if choice == '2': # getting the reason of the user for time-out
                print("\nSelect your reason for leaving: ")
                for i, reason in enumerate(reasons_collection):
                    print(f"[{i + 1}] {reason}")

                main_reason = int(input("\nYour Choice: "))
                reason = reasons_collection[main_reason - 1] if main_reason <= 5 else input(
                    "Please specify your reason for leaving: ")
                
                print(f"\n{self.username} is Time-out! Reason:", reason)
                for i in range(len(rows)):
                    if self.username in rows[i]:
                        rows[i][2] = reason

            if choice == '1': # change reasons to default
                print(f"\n{self.username} is Time-in!")
                for i in range(len(rows)):
                    if self.username in rows[i]:
                        rows[i][2] = "none"
                        break
                    
        with open('attendance.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(rows)

    def reg_liab(self, username):
        filename = user_liabs.get(username)

        if filename:
            with open(filename, 'r') as file1:
                liab1 = file1.read()

            with open('liabs_of_users/liabilities.txt', 'r') as file2:
                liab2 = file2.read()

            liab_all = liab1 + liab2

            liab_list = liab_all.split('\n')  # convert to list of liabilities

            if any(liab_list):
                print("\nThe following liabilities are currently listed:")
                for i, liab in enumerate(liab_list):
                    print(f"{i+1}. {liab}")
            else:
                print("\nNo liabilities")

    def options(self):
        print("\n[1] Liabilities")
        print("[2] Attendance")
        print("[3] Log out")





