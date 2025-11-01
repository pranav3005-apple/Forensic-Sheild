#!/usr/bin/env python3
"""
COMPLETE Reset for USB Drive Access
"""
import subprocess
import os
import time

def full_drive_reset(drive):
    """Completely reset drive permissions and attributes"""
    print(f"🛠️ Performing COMPLETE reset on {drive}...")
    print("This may take a moment...")
    
    # Step 1: Remove ALL icacls denials and set full permissions
    icacls_commands = [
        f'icacls {drive} /reset',
        f'icacls {drive} /grant Everyone:F /T',
        f'icacls {drive} /grant Users:F /T',
        f'icacls {drive} /grant Administrators:F /T'
    ]
    
    for cmd in icacls_commands:
        try:
            print(f"   Running: {cmd.split()[0]}...")
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15)
            if result.returncode == 0:
                print(f"      ✅ {cmd.split()[0]} successful")
            else:
                print(f"      ⚠️ {cmd.split()[0]} returned {result.returncode}")
        except subprocess.TimeoutExpired:
            print(f"      ⏰ {cmd.split()[0]} timed out")
        except Exception as e:
            print(f"      ❌ {cmd.split()[0]} error: {e}")
    
    # Step 2: Remove ALL read-only attributes
    print("   Removing read-only attributes...")
    try:
        result = subprocess.run(
            f'attrib -R {drive}\\* /S /D',
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=30
        )
        if result.returncode == 0:
            print("      ✅ Attrib reset successful")
        else:
            print(f"      ⚠️ Attrib returned {result.returncode}")
    except subprocess.TimeoutExpired:
        print("      ⏰ Attrib timed out")
    
    # Step 3: Use diskpart to clear read-only flag at disk level
    print("   Resetting disk-level read-only...")
    try:
        drive_letter = drive[0]
        diskpart_commands = f"""
select volume {drive_letter}
attributes disk clear readonly
exit
"""
        result = subprocess.run(
            'diskpart',
            input=diskpart_commands,
            shell=True,
            capture_output=True,
            text=True,
            timeout=15
        )
        if result.returncode == 0:
            print("      ✅ Diskpart reset successful")
        else:
            print(f"      ⚠️ Diskpart returned {result.returncode}")
    except subprocess.TimeoutExpired:
        print("      ⏰ Diskpart timed out")
    
    # Step 4: Final permission reset
    print("   Final permission cleanup...")
    try:
        result = subprocess.run(
            f'icacls {drive} /setowner "Everyone" /T /C',
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        print("      ✅ Final cleanup done")
    except:
        print("      ⚠️ Final cleanup skipped")
    
    print(f"\n🎉 COMPLETE RESET FINISHED for {drive}")
    print("💡 You may need to:")
    print("   1. Unplug the USB drive")
    print("   2. Wait 10 seconds") 
    print("   3. Plug it back in")
    print("   4. Try accessing it again")

def test_drive_access(drive):
    """Test if we can access the drive"""
    print(f"\n🧪 Testing access to {drive}...")
    try:
        files = os.listdir(drive)
        print(f"   ✅ SUCCESS! Can access {drive}")
        print(f"   📁 Found {len(files)} files/folders")
        return True
    except Exception as e:
        print(f"   ❌ STILL BLOCKED: {e}")
        return False

if __name__ == "__main__":
    drive = "D:\\"  # Change to your USB drive letter
    
    print("🛡️ Forensic Shield - COMPLETE Drive Reset")
    print("=" * 50)
    
    # Run complete reset
    full_drive_reset(drive)
    
    # Test access
    access_restored = test_drive_access(drive)
    
    if access_restored:
        print(f"\n🎉 DRIVE FIXED! {drive} is now accessible")
    else:
        print(f"\n⚠️ Drive still has issues. Try:")
        print(f"   1. Run this script as Administrator")
        print(f"   2. Restart your computer")
        print(f"   3. Try a different USB port")
