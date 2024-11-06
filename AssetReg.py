class  constraits:
# Minimum character integers.
    min_char_length = int(2)
    blue_badge_length = int(6)

class util:
    # Import OS Type
    import os
    
    # Define time for sleep function
    from time import sleep
    
    # Get current date and define current date and format. 
    import datetime
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime('%d/%m/%Y')
    
    # ANSI escape squence to remove lines in console. Used in "Add Asset" function to remove the past lines 1 by 1 back to the previous prompt.
    # "\xb" is the escape character in ASCII, which is used to introduce an ANSI escape sequence.
    # "[1A" is an escape sequence in ASCII, which moves the cursor on the terminal up 1 line. The "1" signifies how far, the "A" signifies the direction. 
    # "[2K" is an escape sequence in ASCII, which erases the current line. The "2" is how many lines, the "k" is the code for "erase line" 
    def delete_line():
        print("\x1b[1A\x1b[2K", end="")

    # clear function, with validation of which os.
    def clear():
        if util.os.name == 'nt':
            _ = util.os.system('cls')
        else:
            _ = util.os.system('clear')

class msg:
    # General error message without delete lines, clears the screen the displays the message then clears the screen again.
    def print_general_error_message(message):
        util.clear()
        print("------------------------")
        print(message)
        print("------------------------")
        input("Press Enter to continue...")
        util.clear()

    def print_invalid_choice_error():
        msg.print_general_error_message("Invalid choice. Please try again.")

    def print_no_assets_error():
        msg.print_general_error_message("No assets in the register!")

    def print_search_assets_error():
        msg.print_general_error_message("No assets found!")   

    #Used in displaying the asset validation error message. When enter is pressed, the error message is cleared by the delete line utility.  
    def print_error_asset_message(message):
        print("------------------------")
        print(message)
        print("------------------------")
        input("Press Enter to continue...")
        util.delete_line()
        util.delete_line()
        util.delete_line()
        util.delete_line()
        util.delete_line()
        if message == ("Invalid choice. Please try again."):
            util.delete_line()
            util.delete_line()
            util.delete_line()
            util.delete_line()
            util.delete_line()
            
    # msg to print specific error msg
    def print_asset_name_length_error():
        msg.print_error_asset_message("Asset Name too short, must be atleast 3 characters long.")

    def print_asset_invalid_choice_error():
        msg.print_error_asset_message("Invalid choice. Please try again.")

    def print_blue_badge_length_error():
        msg.print_error_asset_message("Blue Badge Number must be exactly 6 digits long.")

    def print_blue_badge_numerical_err1or():
        msg.print_error_asset_message("Blue Badge Number should be numerical.")

    def print_blue_badge_duplicate_error():
        msg.print_error_asset_message("Asset number already exists")

    def print_description_length_error():
        msg.print_error_asset_message("Asset description too short, must be atleast 3 characters long.")

    def print_location_length_error():
        msg.print_error_asset_message("Asset location too short, must be atleast 3 characters long.")
       

# Definition of the list.  
class asset:
    def __init__(self, name, blue_badge, device_type, description, location, date_added):
        self.name = name
        self.blue_badge = blue_badge
        self.device_type = device_type
        self.description = description
        self.location = location
        self.date_added = date_added

# Asset Register List.  
class asset_register:
    def __init__(self):
        self.assets = []

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            for asset in self.assets:
                f.write(f"{asset.name},{asset.blue_badge},{asset.device_type},{asset.description},{asset.location},{asset.date_added}\n")

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                name, blue_badge, device_type, description, location,date_added = line.strip().split(',')
                amend_asset = asset(name, blue_badge, device_type, description, location,date_added)
                self.assets.append(amend_asset)

    # Add Asset to the Asset register.
    def add_asset(self):
        util.clear()
        print("Add Asset Function - Type '^' to exit at any point.")
        while True:
            name = input("Enter asset name: ")
            if name == "^":
                util.clear()
                return
            elif len(name) <=  constraits.min_char_length:
                msg.print_asset_name_length_error()
            else:
                break    
        while True:
            blue_badge = input("Enter asset blue badge number: ")
            primary_key_validate = [asset for asset in self.assets if blue_badge in asset.blue_badge]
            if blue_badge == "^":
                util.clear()
                return
            elif len(blue_badge) !=  constraits.blue_badge_length:
                msg.print_blue_badge_length_error()
            elif blue_badge.isnumeric() == False:
                msg.print_blue_badge_numerical_error()
            elif not primary_key_validate:
                break
            else:
                msg.print_blue_badge_duplicate_error()
        while True:
            print("Select asset type:")
            print("1. Workstation")
            print("2. Laptop")
            print("3. Mobile")
            print("4. Periferal")
            asset_type_selection = input("Select Asset Type: ")
            if asset_type_selection == "^":
                util.clear()
                return
            elif asset_type_selection == "1":
                device_type = "Workstation"
                break
            elif asset_type_selection == "2":
                device_type = "Laptop"
                break
            elif asset_type_selection == "3":
                device_type = "Mobile"
                break
            elif asset_type_selection == "4":
                device_type = "Periferal"
                break
            else:
                msg.print_asset_invalid_choice_error()        
        while True:
            description = input("Enter asset description: ")
            if description == "^":
                util.clear()
                return
            elif len(description) <=  constraits.min_char_length:
                msg.print_description_length_error()
            else:
                break
        while True:
            location = input("Enter asset location: ")
            if location == "^":
                util.clear()
                return
            elif len(location) <=  constraits.min_char_length:
                msg.print_location_length_error()
            else:
                break
        amend_asset = asset(name, blue_badge, device_type, description, location, util.formatted_date)
        self.assets.append(amend_asset)
        print("------------------------")
        print("Asset added successfully!")
        print("------------------------")
        input("Press Enter to continue...")
        util.clear()

    # Remove asset from the asset register.
    def remove_asset(self):
        util.clear()
        print("Remove Asset Function")
        blue_badge = input("Enter asset blue badge number: ")
        # Searchs for inputted asset.
        remove_asset_search = [asset for asset in self.assets if asset.blue_badge == blue_badge]
        
        # If asset is not in search then print "Asset not found"
        if not remove_asset_search:
            msg.print_search_assets_error()
            return  
        
        # If an asset is found then continue with removal menu. 
        util.clear()
        print("------------------------")
        print(f"Are you sure you would like to delete asset "+ blue_badge + "?")
        print("------------------------")
        print("1. Yes")
        print("2. No")
        print("------------------------")
        
        # Removal confirmation check.
        delete_confirmation = input("Enter your choice: ")
        
        
        if delete_confirmation == "1":
            util.clear()
            for asset in remove_asset_search:
                self.assets.remove(asset)
            print("------------------------")
            print(f"Asset " + blue_badge + " removed successfully!")
            print("------------------------")
            input("Press Enter to continue...")
            util.clear()
            return
        elif delete_confirmation == "2":
            util.clear()
            return
        else:
            util.clear()
            msg.print_asset_invalid_choice_error()   
            util.clear()
            return
        
    # Update asset in the asset register.
    def update_asset(self):
        util.clear()
        print("Update Asset Function")
        blue_badge = input("Enter asset blue badge number: ")
        update_asset_search = [asset for asset in self.assets if asset.blue_badge == blue_badge]
        if not update_asset_search:
            msg.print_search_assets_error()
            return
        
        while True:
            #Update Menu
            for asset in update_asset_search:
                util.clear()
                print("Asset Update Menu for: "+blue_badge)
                print("------------------------")
                print("Current Details:")
                print(f"Name:        {asset.name}")
                print(f"Device Type: {asset.device_type}")
                print(f"Description: {asset.description}")
                print(f"Location:    {asset.location}")
                print("------------------------")
                print("1. Update Name")
                print("2. Update Device Type")
                print("3. Update Description")
                print("4. Update Location")
                print("5. Exit Update Menu")
                print("------------------------")
                
                choice = input("Enter your choice: ")
                
                #Update Menu - Name
                if choice == "1":
                    util.clear()
                    print("Asset Name Update Menu for: "+blue_badge)
                    print("------------------------")
                    print("Current Details:")
                    print(f"Name:        {asset.name}")
                    print("------------------------")
                    while True:    
                        asset.name = input("Enter new asset name: ")
                        if len(asset.name) <=  constraits.min_char_length:
                            msg.print_asset_name_length_error()
                        else:
                            break
                    util.clear()
                    print("------------------------")
                    print("Name updated for asset number " + asset.blue_badge + ".")
                    print("------------------------")
                    input("Press Enter to continue...")
                    util.clear()
                                      
        
                #Update Menu - Type
                elif choice == "2":
                    util.clear()
                    print("Device Type Update Menu for: "+blue_badge)
                    print("------------------------")
                    print("Current Details:")
                    print(f"Device Type: {asset.device_type}")
                    print("------------------------")
                    while True:
                        print("Select a new asset type:")
                        print("1. Workstation")
                        print("2. Laptop")
                        print("3. Mobile")
                        print("4. Periferal")
                        asset_type_selection = input("Select Asset Type: ")
                        if asset_type_selection == "^":
                            util.clear()
                            return
                        elif asset_type_selection == "1":
                            asset.device_type = "Workstation"
                            break
                        elif asset_type_selection == "2":
                            asset.device_type = "Laptop"
                            break
                        elif asset_type_selection == "3":
                            asset.device_type = "Mobile"
                            break
                        elif asset_type_selection == "4":
                            asset.device_type = "Periferal"
                            break
                        else:
                            msg.print_asset_invalid_choice_error()   
                    util.clear()
                    print("------------------------")
                    print("Device type updated for asset number " + asset.blue_badge)
                    print("------------------------")
                    input("Press Enter to continue...")
                    util.clear()
                    
                
                #Update Menu - Description
                elif choice == "3":
                    util.clear()
                    print("Description Update Menu for: "+blue_badge)
                    print("------------------------")
                    print("Current Details:")
                    print(f"Description: {asset.description}")
                    print("------------------------")
                    while True:
                        asset.description = input("Enter amended description: ")
                        if len(asset.description) <=  constraits.min_char_length:
                            msg.print_description_length_error()
                        else:
                            break  
                    util.clear()
                    print("------------------------")
                    print("Description updated for asset number " + asset.blue_badge)
                    print("------------------------")   
                    input("Press Enter to continue...")
                    util.clear()
                    
            
                #Update Menu - Location
                elif choice == "4":
                    util.clear()
                    print("Asset Location Update Menu for: "+blue_badge)
                    print("------------------------")
                    print("Current Details:")
                    print(f"Location: {asset.location}")
                    print("------------------------")
                    while True:
                        asset.location = input("Enter amended asset location: ")
                        if len(asset.location) <=  constraits.min_char_length:
                            msg.print_location_length_error()
                        else:
                            break
                    util.clear()
                    print("------------------------")
                    print("Location updated for asset number " + asset.blue_badge)
                    print("------------------------")
                    input("Press Enter to continue...")
                    util.clear()
                    
                
                # Update Menu - Exit 
                elif choice == "5":
                    util.clear() 
                    print("------------------------")
                    print("Exiting update menu for asset " + blue_badge + ".")
                    print("------------------------")
                    input("Press Enter to continue...")
                    util.clear()
                    return
                else:
                    msg.print_invalid_choice_error()
                    
        
    # Display all assets in register.
    def display_assets(self):
        util.clear()
        if not self.assets:
            msg.print_no_assets_error()
        else:
            for asset in self.assets:
                print("------------------------")
                print(f"Name:              {asset.name}")
                print(f"Blue Badge Number: {asset.blue_badge}")
                print(f"Asset Type:        {asset.device_type}")
                print(f"Description:       {asset.description}")
                print(f"Location:          {asset.location}")
                print(f"Date Added:        {asset.date_added}")
                print("------------------------")
            input("Press Enter to continue...")
            util.clear()

    # Search assets and return a specific asset based on the name or blue badge number. 
    def search_assets(self):
        util.clear()
        query = input("Enter search query (name or blue badge number): ")
        results = [asset for asset in self.assets if query.lower() in asset.name.lower() or query in asset.blue_badge]
        if not results:
            msg.print_search_assets_error()
        else:
            for asset in results:
                print("------------------------")
                print(f"Name:              {asset.name}")
                print(f"Blue Badge Number: {asset.blue_badge}")
                print(f"Asset Type:        {asset.device_type}")
                print(f"Description:       {asset.description}")
                print(f"Location:          {asset.location}")
                print(f"Date Added:        {asset.date_added}")
            print("------------------------")
            input("Press Enter to continue...")
            util.clear()

    #Remove all assets admin function.
    def admin_all_remove(self):
        if not self.assets:
            msg.print_no_assets_error()
        else:
            util.clear()
            print("------------------------")
            print(f"Are you sure you would like to delete all assets?")
            print("------------------------")
            print("1. Yes")
            print("2. No")
            print("------------------------")
            all_delete_confirmation = input("Enter your choice: ")
        
            if all_delete_confirmation == "1":
                util.clear()
                self.assets.clear()
                print("------------------------")
                print("All assets removed successfully!")
                print("------------------------")
                input("Press Enter to continue...")
                util.clear()
            
            elif all_delete_confirmation == "2":
                util.clear()
            
            else:
                util.clear()
                msg.print_asset_invalid_choice_error()   
                util.clear()
            
# Admin menu.
    def admin(self):
        password = input("Enter the admin password: ")
        if password != "1337":
            print("------------------------")
            print("Incorrect password")
            print("------------------------")
            input("Press Enter to continue...")
            util.clear()
            return
        while True:
            util.clear()
            print("------------------------")
            print("1. Remove all assets")
            print("2. Exit Admin")
            print("------------------------")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.admin_all_remove()
            elif choice == "2":
                util.clear()
                return
            else:
                msg.print_invalid_choice_error()
            
# Menu definition. 
def main():
    util.clear()
    reg = asset_register()
    reg.read_from_file('asset_register.txt')  # Read from file at startup
    while True:
        print("------------------------")
        print("Asset Register Menu:")
        print("1. Add Asset")
        print("2. Remove Asset")
        print("3. Update Asset")
        print("4. Display Assets")
        print("5. Search Assets")
        print("6. Save & Exit")
        print("------------------------")
        choice = input("Enter your choice: ")
        if choice =="":
            util.clear()
        elif choice == "1":
            reg.add_asset()
        elif choice == "2":
            reg.remove_asset()
        elif choice == "3":
            reg.update_asset()
        elif choice == "4":
            reg.display_assets()
        elif choice == "5":
            reg.search_assets()
        elif choice == "6":
            reg.write_to_file('asset_register.txt')  # write to asset_register file on exit
            util.clear()
            print("Successfully exited")
            break
        elif choice == "admin":
            reg.admin()
        else:
            msg.print_invalid_choice_error()

if __name__ == "__main__":
    main()