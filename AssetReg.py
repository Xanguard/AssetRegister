# Minimum character integers.
class  constraits:

    min_char_length = int(2)
    # Room numbers are always below 4 characters. For example 16.B is the longest character length. 
    max_char_room_length = int(5)
    # Blue Badge numbers are alwasy 6 digits.
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
    def update_cancelled():
        util.clear()
        print("------------------------")
        print(f"Update process cancelled.")
        print("------------------------")
        input("Press Enter to continue...")
        util.clear()
    
    def caret_exit():
        print("Type '^' to exit at any point.")
        print("-------------------------")
    
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

    def print_blue_badge_numerical_error():
        msg.print_error_asset_message("Blue Badge Number should be numerical.")

    def print_blue_badge_duplicate_error():
        msg.print_error_asset_message("Asset number already exists")

    def print_description_length_error():
        msg.print_error_asset_message("Asset description too short, must be atleast 3 characters long.")

    def print_department_length_error():
        msg.print_error_asset_message("Asset department too short, must be atleast 3 characters long.")

    def print_room_length_error():
        msg.print_error_asset_message("Asset room number too long, must be below 5 characters long.")   

# Definition of the list.  
class asset:
    def __init__(self, name, blue_badge, device_type, description, department, room_number, notes, date_added):
        self.name = name
        self.blue_badge = blue_badge
        self.device_type = device_type
        self.description = description
        self.department = department
        self.room_number = room_number
        self.notes = notes
        self.date_added = date_added

# Asset Register List.  
class asset_register:
    def __init__(self):
        self.assets = []
        self.errors = []  # List to collect error messages
        self.errored_assets = []  # List to keep track of errored assets

    # Validation constraints are checked to validate import data.
    def validate_asset_data(self, name, blue_badge, device_type, description, department, room_number, notes, date_added):
        valid = True
        if len(name) < constraits.min_char_length:
            self.errors.append(f"Asset {blue_badge} - Asset Name too short, must be at least 3 characters long.")
            valid = False
        if len(blue_badge) != constraits.blue_badge_length or not blue_badge.isdigit():
            self.errors.append(f"Asset {blue_badge} - Blue Badge Number must be exactly 6 digits long and numerical.")
            valid = False
        if device_type not in ["Workstation", "Laptop", "Mobile", "Periferal"]:
            self.errors.append(f"Asset {blue_badge} - Invalid asset type.")
            valid = False
        if len(description) < constraits.min_char_length:
            self.errors.append(f"Asset {blue_badge} - Asset description too short, must be at least 3 characters long.")
            valid = False
        if len(department) < constraits.min_char_length:
            self.errors.append(f"Asset {blue_badge} - Asset department too short, must be at least 3 characters long.")
            valid = False
        if len(room_number) > constraits.max_char_room_length:
            self.errors.append(f"Asset {blue_badge} - Asset room number too long, must be below 5 characters long.")
            valid = False
        if len(date_added) != 10:
            self.errors.append(f"Asset {blue_badge} - Date Added has an invalid format.")
            valid = False
        return valid

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            for asset in self.assets:
                f.write(f"{asset.name},{asset.blue_badge},{asset.device_type},{asset.description},{asset.department},{asset.room_number},{asset.notes},{asset.date_added}\n")
            # Optionally save errored assets as well
            for errored_asset in self.errored_assets:
                f.write(f"{errored_asset['line']}\n")

    # Read from file.
    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                name, blue_badge, device_type, description, department, room_number, notes, date_added = line.strip().split(',')
                if self.validate_asset_data(name, blue_badge, device_type, description, department, room_number, notes, date_added):
                    amend_asset = asset(name, blue_badge, device_type, description, department, room_number, notes, date_added)
                    self.assets.append(amend_asset)
                else:
                    self.errored_assets.append({
                        "line": line.strip(),
                        "name": name,
                        "blue_badge": blue_badge,
                        "device_type": device_type,
                        "description": description,
                        "department": department,
                        "room_number": room_number,
                        "notes": notes,
                        "date_added": date_added
                    })  # Store the errored asset details
                    
                    
                    print("------------------------")
                    print(f"Import Error - Skipping invalid asset data: {blue_badge}")
                    print("------------------------")
                    input("Press Enter to continue...")
                    util.clear()
                


    # Add Asset to the Asset register.
    def add_asset(self):
        util.clear()
        msg.caret_exit()
        print("Add Asset Function")
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
            department = input("Enter asset department: ")
            if department == "^":
                util.clear()
                return
            elif len(department) <=  constraits.min_char_length:
                msg.print_department_length_error()
            else:
                break
        while True:
            room_number = input("Enter asset room number: ")
            if room_number == "^":
                util.clear()
                return
            elif len(room_number) > constraits.max_char_room_length:
                msg.print_room_length_error()
            else:
                break
        while True:
            notes = input("Enter any additional information: ")
            if notes == "^":
                util.clear()
                return
            else:
                break
        amend_asset = asset(name, blue_badge, device_type, description, department, room_number, notes, util.formatted_date)
        self.assets.append(amend_asset)
        print("------------------------")
        print("Asset added successfully!")
        print("------------------------")
        input("Press Enter to continue...")
        util.clear()

    # Remove asset from the asset register.
    def remove_asset(self):
        util.clear()
        msg.caret_exit()
        print("Remove Asset Function")
        blue_badge = input("Enter asset blue badge number: ")
        # Searchs for inputted asset.
        remove_asset_search = [asset for asset in self.assets if asset.blue_badge == blue_badge]
        if blue_badge == "^":
            util.clear()
            return
        
        # If asset is not in search then print error.
        elif not remove_asset_search:
            msg.print_search_assets_error()
            return  
        
        # If an asset is found then continue with removal menu. 
        util.clear()
        print("------------------------")
        print(f"Are you sure you would like to delete asset {blue_badge}?")
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
            print(f"Asset {blue_badge} removed successfully!")
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
        msg.caret_exit()
        print("Update Asset Function")
        blue_badge = input("Enter asset blue badge number: ")
        update_asset_search = [asset for asset in self.assets if asset.blue_badge == blue_badge]
        
        if blue_badge == "^":
            util.clear()
            return
        
        elif not update_asset_search:
            msg.print_search_assets_error()
            return
        
        while True:
            #Update Menu - Main
            for asset in update_asset_search:
                util.clear()
                print(f"Asset Update Menu for: {blue_badge}")
                print("------------------------")
                print("Current Details:")
                print(f"Name:        {asset.name}")
                print(f"Device Type: {asset.device_type}")
                print(f"Description: {asset.description}")
                print(f"Department:  {asset.department}")
                print(f"Room:        {asset.room_number}")
                print(f"Notes:       {asset.notes}")
                print("------------------------")
                print("1. Update Name")
                print("2. Update Device Type")
                print("3. Update Description")
                print("4. Update Department")
                print("5. Update Room Number")
                print("6. Update Notes")
                print("7. Exit Update Menu")
                print("------------------------")
                
                choice = input("Enter your choice: ")
                
                #Update Menu - Name
                if choice == "1":
                    util.clear()
                    msg.caret_exit()
                    print(f"Asset Name Update Menu for: {blue_badge}")
                    print("------------------------")
                    print("Current Details:")
                    print(asset.name)
                    print("------------------------")
                    while True:    
                        updated_asset_name = input("Enter new asset name: ")
                        if updated_asset_name == "^":
                            util.clear()
                            msg.update_cancelled()
                            break
                        elif len(updated_asset_name) <=  constraits.min_char_length:
                            msg.print_asset_name_length_error()
                        else:
                            asset.name = updated_asset_name
                            util.clear()
                            print("------------------------")
                            print(f"Name updated for asset number {asset.blue_badge}")
                            print("------------------------")
                            input("Press Enter to continue...")
                            util.clear()
                            break          
        
                #Update Menu - Type
                elif choice == "2":
                    def updated_periferal(): 
                        util.clear()
                        print("------------------------")
                        print(f"Device type updated for asset number {asset.blue_badge}")
                        print("------------------------")
                        input("Press Enter to continue...")
                        util.clear()
                    util.clear()
                    msg.caret_exit()
                    print(f"Device Type Update Menu for: {blue_badge}")
                    print("------------------------")
                    print("Current Details:")
                    print(asset.device_type)
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
                            msg.update_cancelled()
                            break
                        elif asset_type_selection == "1":
                            asset.device_type = "Workstation"
                            updated_periferal()
                            break
                        elif asset_type_selection == "2":
                            asset.device_type = "Laptop"
                            updated_periferal()
                            break
                        elif asset_type_selection == "3":
                            updated_periferal()
                            asset.device_type = "Mobile"
                            break
                        elif asset_type_selection == "4":
                            updated_periferal()
                            asset.device_type = "Periferal"
                            break
                        else:
                            msg.print_asset_invalid_choice_error()   
                    
                #Update Menu - Description
                elif choice == "3":
                    util.clear()
                    msg.caret_exit()
                    print(f"Description Update Menu for: {blue_badge}")
                    print("------------------------")
                    print("Current Details:")
                    print(asset.description)
                    print("------------------------")
                    while True:
                        updated_asset_description = input("Enter amended description: ")
                        if updated_asset_description == "^":
                            util.clear()
                            msg.update_cancelled()
                            break
                        elif len(updated_asset_description) <=  constraits.min_char_length:
                            msg.print_description_length_error()
                        else:
                            asset.description = updated_asset_description
                            util.clear()
                            print("------------------------")
                            print(f"Description updated for asset number {asset.blue_badge}")
                            print("------------------------")   
                            input("Press Enter to continue...")
                            util.clear()
                            break
                    
            
                #Update Menu - Department
                elif choice == "4":
                    util.clear()
                    msg.caret_exit()
                    print(f"Asset Department Update Menu for: {blue_badge}")
                    print("------------------------")
                    print("Current Details:")
                    print(asset.department)
                    print("------------------------")
                    while True:
                        updated_asset_department = input("Enter amended asset department: ")
                        if updated_asset_department == "^":
                            util.clear()
                            msg.update_cancelled()
                            return
                        elif len(updated_asset_department) <=  constraits.min_char_length:
                            msg.print_department_length_error()
                        else:
                            asset.department = updated_asset_department
                            util.clear()
                            print("------------------------")
                            print(f"Department updated for asset number {asset.blue_badge}")
                            print("------------------------")
                            input("Press Enter to continue...")
                            util.clear()
                            break
                
                #Update Menu - Room
                elif choice == "5":
                    util.clear()
                    msg.caret_exit()
                    print(f"Asset Room Update Menu for: {blue_badge}")
                    print("------------------------")
                    print("Current Details:")
                    print(asset.room_number)
                    print("------------------------")
                    while True:
                        updated_asset_room_number = input("Enter asset room number: ")
                        if updated_asset_room_number == "^":
                            msg.update_cancelled
                            break
                        elif len(updated_asset_room_number) > constraits.max_char_room_length:
                            msg.print_room_length_error()
                        else:
                            asset.room_number = updated_asset_room_number
                            util.clear()
                            print("------------------------")
                            print(f"Room updated for asset number {blue_badge}")
                            print("------------------------")
                            input("Press Enter to continue...")
                            util.clear()
                            break

                #Update Menu - Notes
                elif choice =="6":
                    util.clear()
                    msg.caret_exit
                    print(f"Asset Notes Update Menu for: {blue_badge}")
                    print("------------------------")
                    print("Current Details:")
                    print(asset.notes)
                    print("------------------------")    
                    while True:
                        updated_asset_notes = input("Enter any additional information: ")
                        if updated_asset_notes == "^":
                            util.clear()
                            msg.update_cancelled()
                            return
                        else:
                            asset.notes = updated_asset_notes
                            util.clear()
                            print("------------------------")
                            print(f"Notes updated for asset number {blue_badge}")
                            print("------------------------")
                            input("Press Enter to continue...")
                            util.clear()
                            break

                # Update Menu - Exit 
                elif choice == "7":
                    util.clear() 
                    print("------------------------")
                    print(f"Exiting update menu for asset {blue_badge}")
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
                print(f"Department:        {asset.department}")
                print(f"Room Number:       {asset.room_number}")
                print(f"Notes:             {asset.notes}")
                print(f"Date Added:        {asset.date_added}")
                print("------------------------")
            input("Press Enter to continue...")
            util.clear()

    def display_errors(self):
        util.clear()
        if not self.errors:
            print("No errors found.")
        else:
            print("------------------------")
            print("Validation Errors - Please correct errors in input file for the following assets:")
            for error in self.errors:
                print(error)
            print("------------------------")
        input("Press Enter to continue...")
        util.clear()

    # Search assets and return a specific asset based on the name or blue badge number. 
    def search_assets(self):
        util.clear()
        msg.caret_exit()
        query = input("Enter search query (name or blue badge number): ")
        results = [asset for asset in self.assets if query.lower() in asset.name.lower() or query in asset.blue_badge]
        if query == "^":
            util.clear()
            return
        elif not results:
            msg.print_search_assets_error()
        else:
            for asset in results:
                print("------------------------")
                print(f"Name:              {asset.name}")
                print(f"Blue Badge Number: {asset.blue_badge}")
                print(f"Asset Type:        {asset.device_type}")
                print(f"Description:       {asset.description}")
                print(f"Department:        {asset.department}")
                print(f"Room Number:       {asset.room_number}")
                print(f"Notes:             {asset.notes}")
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
            print("2. Error Log")
            print("3. Exit Admin")
            print("------------------------")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.admin_all_remove()
            elif choice == "2":
                self.display_errors()
            elif choice == "3":
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
        print("6. Display Errors")
        print("7. Save & Exit")
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
            reg.display_errors()
        elif choice == "7":
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