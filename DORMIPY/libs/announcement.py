import time as tm
from datetime import time, timedelta, datetime
import schedule

announcement_list = []

def remove_announcement():
    del announcement_list[0]
    return schedule.CancelJob

def create_announcement():
    announcement = input("What would you like to announce? ")
    duration = int(input("For how many days should this announcement be displayed? "))
    announcement_list.append(announcement)
    schedule.every(duration).seconds.do(remove_announcement)
    
def show_announcement():
    schedule.run_pending()
    tm.sleep(1)
    if announcement_list == []:
        print("No announcements")
    else:
        print(announcement_list)    
    