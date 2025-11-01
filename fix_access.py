#!/usr/bin/env python3
"""
Quick fix to restore access to USB drives
"""
import subprocess
import os

def fix_drive_access(drive):
    """Remove any denials and restore access"""
    print(f"🔧 Fixing access to {drive}...")
    
    # Commands to restore normal access
    commands = [
        f'icacls {drive} /remove:d Everyone',
        f'icacls {drive} /grant Everyone:(F)',
        f'icacls {drive} /grant Users:(F)',
        f'attrib -R {drive}\\* /S /D'
    ]
    
    for cmd in commands:
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"✅ {cmd.split()[0]} successful")
            else:
                print(f"⚠️ {cmd.split()[0]} failed")
        except Exception as e:
            print(f"⚠️ Error: {e}")
    
    print(f"🎉 Access restored to {drive}")
    print("You should now be able to read and write to the drive")

if __name__ == "__main__":
    drive = "D:\\"  # Change to your USB drive letter
    fix_drive_access(drive)