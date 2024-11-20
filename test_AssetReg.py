
import pytest
from unittest.mock import patch
from AssetReg import asset_register, asset, util, msg  # Adjust import according to your file structure

@pytest.fixture
def asset_reg():
    return asset_register()

# Add an asset to the system
def test_add_asset(asset_reg):
    asset_reg.assets.clear()   
    inputs = [

        'Test Asset',       # Asset name
        '123456',           # Blue badge
        '2',                # Device type (Laptop)
        'A description',    # Description
        'IT Department',    # Department
        '16.A',             # Room number
        'Notes',            # Additional notes
        '',                 # Press Enter to Continue
    ]
    
    with patch('builtins.input', side_effect=inputs):
        asset_reg.add_asset()
    
def test_add_asset_validation(asset_reg):
    asset_reg.assets.clear() 

    inputs = [
        'Te',               # Validation Asset name
        '',                 # Press Enter to Continue
        'Test Asset',       # Asset name
        '12345',            # Validation Blue badge
        '',                 # Press Enter to Continue
        '123456',           # Blue badge
        '7',                # Validation Device type
        '',                 # Press Enter to Continue
        '2',                # Device type (Laptop)
        'A',                # Validation Description
        '',                 # Press Enter to Continue
        'A description',    # Description
        'I',                # Validation Department
        '',                 # Press Enter to Continue
        'IT Department',    # Department
        '16.AAAA',          # Validation Room number
        '',                 # Press Enter to Continue
        '16.A',             # Room number
        'Notes',            # Additional notes
        '',                 # Press Enter to Continue
    ]
    
    with patch('builtins.input', side_effect=inputs):
        asset_reg.add_asset()

# First, add an asset then remove it.
def test_remove_asset(asset_reg):
    asset_reg.assets.clear() 
    
    asset_reg.assets.append(asset(name='Test Asset', blue_badge='123456', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    inputs = [
        '123456',           # Blue Badge
        '1',                # Confirm Deletion
        '',                 # Press Enter to Continue
    ]

    with patch('builtins.input', side_effect=inputs):  
        asset_reg.remove_asset()

# Deleting no assets in register.
def test_remove_asset_no_assets(asset_reg):
    asset_reg.assets.clear() 

    inputs = [
        '123456',           # Blue Badge
        '',                 # Press Enter to Continue
    ]

    with patch('builtins.input', side_effect=inputs):  
        asset_reg.remove_asset()

# Deleteing all assets in the Register, no assets to delete,
def test_remove_all_assets_no_assets(asset_reg):
    asset_reg.assets.clear() 

    inputs = [
        '',                 # Press Enter to Continue
    ]

    with patch('builtins.input', side_effect=inputs):  
        asset_reg.admin_all_remove()

# Deleteing all assets in the Register.
def test_remove_all_assets(asset_reg):
    asset_reg.assets.clear() 

    asset_reg.assets.append(asset(name='Test Asset 1', blue_badge='111111', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    asset_reg.assets.append(asset(name='Test Asset 2', blue_badge='222222', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    inputs = [
        '1',                 # Confirm delete all assets
        '',                  # Press Enter to Continue
    ]

    with patch('builtins.input', side_effect=inputs):  
        asset_reg.admin_all_remove()

# Deleteing all assets in the Register, and deciding agasint it.
def test_remove_all_assets_deactivation(asset_reg):
    asset_reg.assets.clear() 

    asset_reg.assets.append(asset(name='Test Asset 1', blue_badge='111111', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    asset_reg.assets.append(asset(name='Test Asset 2', blue_badge='222222', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    inputs = [
        '2',                 # Confirm delete all assets
        '',                  # Press Enter to Continue
    ]

    with patch('builtins.input', side_effect=inputs):  
        asset_reg.admin_all_remove()

def test_view_errors(asset_reg):
    asset_reg.assets.clear() 

    asset_reg.errored_assets.append(asset(name='T1', blue_badge='11111', device_type='La', 
                                description='AD', department='IT', 
                                room_number='16.AAA', notes='Notes', date_added=util.formatted_date))
    
    asset_reg.errored_assets.append(asset(name='T2', blue_badge='22222', device_type='La', 
                                description='AD', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    inputs = [
        '',                  # Press Enter to Continue
    ]

    with patch('builtins.input', side_effect=inputs):  
        asset_reg.display_errors()

# Add an asset then update each part of the asset. 
def test_update_asset(asset_reg):
    asset_reg.assets.clear() 

    asset_reg.assets.append(asset(name='Test Asset', blue_badge='123456', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))

    inputs = [
        # Search for Asset
        '123456',           # Blue badge to search
        # Update Name Test
        '1',                # Update name
        'Updated Asset',    # New name
        '',                 # Press Enter to continue
        # Update Device Type Test
        '2',                # Update device type selected
        '2',                # New Device type (Laptop)
        '',                 # Press Enter to continue
        # Update Description Test
        '3',                # Update description
        'New description',  # New Description
        '',                 # Press Enter to continue
        # Update Department Test
        '4',                # Update department
        'New department',   # New Department
        '',                 # Press Enter to continue
        # Update Room Test
        '5',                # Update Room
        '16.B',             # New Room
        '',                 # Press Enter to continue
        # Update notes
        '6',                # Update Notes
        'THIS IS A NOTE',   # New Note
        '',                 # Press Enter to continue
        # Exit update menu
        '7',
        '',    
    ]
    
    with patch('builtins.input', side_effect=inputs):
        asset_reg.update_asset()
        
def test_update_asset_validation(asset_reg):
    asset_reg.assets.clear() 

    asset_reg.assets.append(asset(name='Test Asset', blue_badge='123456', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))

    inputs = [
        # Search for Asset
        '123456',           # Blue badge to search
        # Update Name Test
        '1',                # Update name
        'Up',               # Validation name
        '',                 # Press Enter to continue
        'Updated Name'      # New Name
        # Update Device Type Test
        '2',                # Update device type selected
        '9',                # Validation Device Type
        '',                 # Press Enter to continue
        '2',                # New Device type (Laptop)
        '',                 # Press Enter to continue
        # Update Description Test
        '3',                # Update description
        'ND',               # Validation Description
        '',                 # Press Enter to continue
        'New description',  # New Description
        '',                 # Press Enter to continue
        # Update Department Test
        '4',                # Update department
        'ND',               # Validation Department
        '',                 # Press Enter to continue
        'New department',   # New Department
        '',                 # Press Enter to continue
        # Update Room Test
        '5',                # Update Room
        '50000',               # Validation Room
        '',                 # Press Enter to continue
        '16.B',             # New Room
        '',                 # Press Enter to continue
        # Exit update menu
        '7',
        '',
    ]
    
    with patch('builtins.input', side_effect=inputs):
        asset_reg.update_asset()

    # No asset to update. 

def test_update_asset_no_assets(asset_reg):
    asset_reg.assets.clear() 
    
    inputs = [
        '123456',           # Blue Badge
        '',                 # Press Enter to Continue
    ]

    with patch('builtins.input', side_effect=inputs):  
        asset_reg.update_asset()

# Test to display all assets. 
def test_display_assets(asset_reg):
    asset_reg.assets.clear() 

    asset_reg.assets.append(asset(name='Test Asset 1', blue_badge='111111', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    asset_reg.assets.append(asset(name='Test Asset 2', blue_badge='222222', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    asset_reg.assets.append(asset(name='Test Asset 3', blue_badge='333333', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    asset_reg.assets.append(asset(name='Test Asset 4', blue_badge='444444', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    asset_reg.assets.append(asset(name='Test Asset 5', blue_badge='555555', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    asset_reg.assets.append(asset(name='Test Asset 6', blue_badge='666666', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    asset_reg.assets.append(asset(name='Test Asset 7', blue_badge='777777', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    asset_reg.assets.append(asset(name='Test Asset 8', blue_badge='888888', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    inputs = ['']
    
    with patch('builtins.input', side_effect=inputs):
        asset_reg.display_assets()

def test_display_no__assets(asset_reg):
    asset_reg.assets.clear() 

    inputs = ['']       # Press Enter to continue
    
    with patch('builtins.input', side_effect=inputs):
        asset_reg.display_assets()

def test_search_asset_blue_badge(asset_reg):
    asset_reg.assets.clear() 

    asset_reg.assets.append(asset(name='Test Asset', blue_badge='123456', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    inputs = [
        '123456',       # Blue badge to search
        '',             # Press Enter to continue
    ]
    
    with patch('builtins.input', side_effect=inputs):
        asset_reg.search_assets()

def test_search_asset_name(asset_reg):
    asset_reg.assets.clear() 

    asset_reg.assets.append(asset(name='Test Asset', blue_badge='123456', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    
    inputs = [
        'Test Asset',   # Name to search
        '',             # Press Enter to continue
    ]

    with patch('builtins.input', side_effect=inputs):
        asset_reg.search_assets()

def test_search_asset_no_assets(asset_reg):
    asset_reg.assets.clear() 
    
    inputs = [
        'Test Asset',   # Name to search
    '',                 # Press Enter to continue   
    ]

    with patch('builtins.input', side_effect=inputs):
        asset_reg.search_assets()

def test_msg_error_asset_name_short():
    
    inputs = ['']       # Press Enter to continue   
    
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Asset Name too short, must be atleast 3 characters long.")

def test_msg_error_invalid_choice():
    
    inputs = ['']       # Press Enter to continue
    
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Invalid choice. Please try again.")

def test_msg_error_blue_badge_number_length():
    
    inputs = ['']       # Press Enter to continue
    
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Blue Badge Number must be exactly 6 digits long.")

def test_msg_error_blue_badge_number_numerical():
    
    inputs = ['']       # Press Enter to continue
    
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Blue Badge Number should be numerical.")

def test_msg_error_asset_number_exists():
    
    inputs = ['']       # Press Enter to continue
    
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Asset number already exists.")

def test_msg_error_asset_description_short():
    
    inputs = ['']       # Press Enter to continue
    
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Asset description too short, must be atleast 3 characters long.")

def test_msg_error_asset_department_short():
    
    inputs = ['']       # Press Enter to continue
    
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Asset department too short, must be atleast 3 characters long.")

def test_msg_error_asset_room_number_long():
    
    inputs = ['']       # Press Enter to continue
    
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Asset room number too long, must be below 5 characters long.")   

def test_print_invalid_choice_error():
    
    inputs = ['']       # Press Enter to continue
    
    with patch('builtins.input', side_effect=inputs):
        msg.print_general_error_message("Invalid choice. Please try again.") 

def test_print_no_assets_error():
    
    inputs = ['']       # Press Enter to continue
    
    with patch('builtins.input', side_effect=inputs):
        msg.print_general_error_message("No assets in the register!") 

def test_print_search_assets_error():
    
    inputs = ['']       # Press Enter to continue
    
    with patch('builtins.input', side_effect=inputs):
        msg.print_general_error_message("No assets found!") 

if __name__ == "__main__":
    pytest.main()
