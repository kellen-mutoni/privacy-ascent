#!/usr/bin/python3


auth = __import__('auth').auth
mood_tracker_menu = __import__('mood').mood_tracker_menu
resources_menu = __import__('resources').resources_menu


# ---- Welcome Screen ----
def welcome_screen():
    print("WELCOME TO PRIVACY ASCENT")
    print("Mental Health Navigator\n")
    print("Your safe space to monitor your mental well-being")

# ---- Main Menu (After Login) ----
def main_menu(username, user_id):
    """Main menu displayed after successful login."""
    while True:
        print("\n" *2)
        print(f"----- MAIN MENU - Welcome, {username}! -----")
        print("\n1. Mood Tracker")
        print("2. Mental Health Resources")
        print("3. Log Out")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        # Mood Tracker
        if choice == "1":
            mood_tracker_menu(user_id, username)
        
        # Mental Health Resources
        elif choice == "2":
            resources_menu()
        
        # Log Out
        elif choice == "3":
            print(f"\n----- Goodbye, {username}! Take care of yourself. -----\n")
            break
        
        else:
            print("\n----- Invalid choice. Please try again. -----")



# ---- Guest Menu ----
def guest_menu():
    while True:
        print("\nGUEST MODE\n")
        print("1. View Mental Health Resources")
        print("2. Create Account/ Log in")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            resources_menu()
        
        elif choice == "2":
            user = auth()
            if user:
                main_menu(user['username'], user['user_id'])
            
        elif choice == "3":
            print("\n----- Thank you for visiting Privacy Ascent. Stay well! -----\n")
            break
        
        else:
            print("\n----- Invalid choice. Please try again. -----")


# ---- Start Menu ----
def main():
    while True:
        welcome_screen()
        print("\nWhat would you like to do today?")
        print("1. Sign In")
        print("2. Continue as Guest")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            user = auth()
            if user:
                main_menu(user['username'], user['user_id'])
        elif choice == "2":
            guest_menu()
        elif choice == "3":
            print("\n----- Thank you for using Privacy Ascent. Take care! -----")
            break
        else:
            print("\n----- Invalid choice. Please try again. -----")

main()
