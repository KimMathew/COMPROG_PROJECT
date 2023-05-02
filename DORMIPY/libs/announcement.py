def show_announcement():
    with open('announcement.txt', 'r') as f:
        announcements = f.readlines()
        if announcements:
            print('\nList of announcements:')
            [print(f'[{i+1}] {announcement.strip()}') for i, announcement in enumerate(announcements)]
        else:
            print("\nNo Announcement to be shown")

def announcement_admin():

    while True:
        print("\nManage your announcements:\n")
        print("\n[1] View all announcements")
        print("\n[2] Create a new announcement")
        print("\n[3] Remove an announcement")
        print("\n[4] Back\n")

        choice = input("Select an action [1-4]: ")
        if choice == '1':
            show_announcement()

        elif choice == '2':
            with open('announcement.txt', 'a') as f:
                f.write(input("What do you want to announce? "))
                f.write("\n")
                print("\nYour announcement has been added")
        
        elif choice == '3':
            with open('announcement.txt', 'r') as f:
                announcements = f.readlines()
            if announcements:
                print("List of announcements:")
                [print(f'[{i+1}] {announcement.strip()}') for i, announcement in enumerate(announcements)]
                try:
                    to_remove = int(input('Enter the number of the announcement you want to remove: '))
                    announcements.pop(to_remove-1)
                    with open('announcement.txt', 'w') as f:
                        f.writelines(announcements)
                    print('\nAnnouncement removed successfully.')
                except (ValueError, IndexError):
                    print('\n\nInvalid choice!')
            else:
                print("\nNo Announcement to be removed")

        elif choice == '4':
            print("\nExiting admin announcement...")
            break
        
        else:
            print("\nInvalid input! Please try again")



    
