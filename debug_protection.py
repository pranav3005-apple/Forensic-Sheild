#!/usr/bin/env python3
"""
Debug script to test write protection
"""
import os
import subprocess

def test_current_protection(drive):
    """Test if we can write to the drive"""
    print(f"\n🧪 Testing write protection on {drive}...")
    
    test_file = os.path.join(drive, "forensic_test_file.txt")
    
    try:
        # Try to create a file
        print(f"📝 Attempting to create: {test_file}")
        with open(test_file, 'w') as f:
            f.write("test write operation")
        print("❌ WRITE SUCCEEDED - Protection NOT working")
        
        # Clean up
        try:
            os.remove(test_file)
            print("🧹 Cleaned up test file")
        except:
            print("⚠️ Could not clean up test file")
        return False
        
    except PermissionError as e:
        print(f"✅ WRITE BLOCKED - Protection IS working!")
        print(f"   Error: {e}")
        return True
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
        return False

def check_drive_attributes(drive):
    """Check drive attributes using Windows commands"""
    drive_letter = drive[0]
    print(f"\n🔍 Checking attributes for {drive}...")
    
    try:
        # Check using attrib command
        result = subprocess.run(
            f'attrib {drive}',
            shell=True,
            capture_output=True,
            text=True
        )
        print(f"📋 Attrib output: {result.stdout.strip()}")
        
        # Check using fsutil
        result = subprocess.run(
            f'fsutil fsinfo volumeinfo {drive}',
            shell=True,
            capture_output=True,
            text=True
        )
        if "ReadOnly" in result.stdout:
            print("✅ Drive shows as ReadOnly in fsutil")
        else:
            print("❌ Drive does not show as ReadOnly in fsutil")
            
    except Exception as e:
        print(f"⚠️ Error checking attributes: {e}")

if __name__ == "__main__":
    drive = "D:\\"  # Change this to your USB drive letter
    
    print("🛡️ Forensic Shield - Protection Debug Tool")
    print("=" * 50)
    
    # Check current state
    check_drive_attributes(drive)
    
    # Test protection
    protection_working = test_current_protection(drive)
    
    print(f"\n🎯 RESULT: Write protection is {'WORKING' if protection_working else 'NOT WORKING'} on {drive}")