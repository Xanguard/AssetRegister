import pytest
from unittest.mock import patch
from AssetReg import asset_register, asset, util  # Adjust import according to your file structure

@pytest.fixture
def asset_reg():
    """Fixture to create an asset register instance for tests."""
    return asset_register()

# Add an asset to the system
def test_add_asset(asset_reg):
    """Test adding an asset to the register."""
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
    """Test removing an asset from the register."""
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

    assert len(asset_reg.assets) == 0

# Add an asset then update each part of the asset. 
def test_update_asset(asset_reg):
    """Test updating an asset in the register."""
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

if __name__ == "__main__":
    pytest.main()