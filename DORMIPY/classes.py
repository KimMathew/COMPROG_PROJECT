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

class Regular(Admin):
    def __init__(self, username):
        self.username = username

    def attendance_checker(self, status, user_choice2):
        # update on csv
        with open('attendance.csv', mode='r', newline='') as csv_file:
            updater = csv.reader(csv_file)
            rows = list(updater)

            # updating the status
            for i in range(len(rows)):
                if self.username in rows[i]:
                    rows[i][1] = status
                    break

            # updating the reasons
            reasons_collection = (
                "School", "Meeting with Friends", "Meeting with family", "Going Home", "Buy Grocery", "Other Reason")
            
            # getting the reason of the user for time-out
            if user_choice2 == 2:
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

            # change reasons to default
            if user_choice2 == 1:
                print(f"\n{self.username} is Time-in!")
                for i in range(len(rows)):
                    if self.username in rows[i]:
                        rows[i][2] = "none"
                        break
                    
        with open('attendance.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(rows)

def options():
    print("\n[1] Announcement")
    print("[2] Liabilities")
    print("[3] Attendance")
    print("[4] Log out")