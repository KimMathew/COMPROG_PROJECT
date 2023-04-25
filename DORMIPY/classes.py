import csv
import sys
import pandas as pd

class Admin:
    def __init__(self, username):
        self.username = username

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
    
    def options(self):
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
            
            if choice == 2: # getting the reason of the user for time-out
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

            if choice == 1: # change reasons to default
                print(f"\n{self.username} is Time-in!")
                for i in range(len(rows)):
                    if self.username in rows[i]:
                        rows[i][2] = "none"
                        break
                    
        with open('attendance.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(rows)

    def options(self):
        print("\n[1] Announcements")
        print("[2] Liabilities")
        print("[3] Attendance")
        print("[4] Log out")





