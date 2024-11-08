import pytest
from unittest.mock import patch
from AssetReg import asset_register, asset, util, msg  # Adjust import according to your file structure

@pytest.fixture
def asset_reg():
    return asset_register()

# Add an asset to the system
def test_add_asset(asset_reg):
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
    

# First, add an asset then remove it.
def test_remove_asset(asset_reg):
    asset_reg.assets.append(asset(name='Test Asset', blue_badge='123456', device_type='Laptop', 
                                description='A description', department='IT', 
                                room_number='16.A', notes='Notes', date_added=util.formatted_date))
    inputs = [
        '123456',           # Blue Badge
        '1',                # Confirm Deletion
        '',                 # Press Enter to Continue
    ]

    with patch('builtins.input', side_effect=inputs):  # Confirm delete and press Enter
        asset_reg.remove_asset()

# Add an asset then update each part of the asset. 
def test_update_asset(asset_reg):
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
        

# Test to display all assets. 
def test_display_assets(asset_reg):
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


def test_displayno__assets(asset_reg):
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        asset_reg.display_assets()

def test_msg_error_asset_name_short():
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Asset Name too short, must be atleast 3 characters long.")

def test_msg_error_invalid_choice():
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Invalid choice. Please try again.")

def test_msg_error_blue_badge_number_length():
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Blue Badge Number must be exactly 6 digits long.")

def test_msg_error_blue_badge_number_numerical():
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Blue Badge Number should be numerical.")

def test_msg_error_asset_number_exists():
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Asset number already exists.")

def test_msg_error_asset_description_short():
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Asset description too short, must be atleast 3 characters long.")

def test_msg_error_asset_department_short():
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Asset department too short, must be atleast 3 characters long.")

def test_msg_error_asset_room_number_long():
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        msg.print_error_asset_message("Asset room number too long, must be below 5 characters long.")   

def test_print_invalid_choice_error():
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        msg.print_general_error_message("Invalid choice. Please try again.") 

def test_print_no_assets_error():
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        msg.print_general_error_message("No assets in the register!") 

def test_print_search_assets_error():
    inputs = ['']
    with patch('builtins.input', side_effect=inputs):
        msg.print_general_error_message("No assets found!") 

if __name__ == "__main__":
    pytest.main()