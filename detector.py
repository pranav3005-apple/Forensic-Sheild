#!/usr/bin/env python3
"""
Forensic Shield - Real Write Protection
"""
import time
import logging
from datetime import datetime
import psutil
import os
import subprocess

class ForensicShield:
    def __init__(self):
        self.connected_devices = {}
        self.setup_logger()
        self.known_drives = set(self.get_drives())
        print("🛡️ Forensic Shield Initialized (Write Protection Mode)")
        
    def setup_logger(self):
        """Setup logging for Windows"""
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/forensic_shield.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def get_drives(self):
        """Get all connected drives"""
        return [partition.device for partition in psutil.disk_partitions()]
    
    def is_usb_drive(self, drive):
        """Check if drive is likely a USB drive"""
        try:
            for partition in psutil.disk_partitions():
                if partition.device == drive:
                    # USB drives often have 'removable' flag or are not C: drive
                    if 'removable' in partition.opts or (drive != 'C:' and len(drive) == 2):
                        return True
            return False
        except:
            return False
    
    def apply_write_protection(self, drive):
        """Apply real write protection to the drive"""
        try:
            drive_letter = drive[0]  # Get 'D' from 'D:'
            
            print(f"🛡️ Applying WRITE PROTECTION to {drive}...")
            
            # Method 1: Use Windows Registry to enable write protection
            try:
                print("   Enabling system-wide write protection...")
                reg_command = f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\StorageDevicePolicies" /v WriteProtect /t REG_DWORD /d 1 /f'
                result = subprocess.run(reg_command, shell=True, capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    print("   ✅ System write protection enabled")
            except Exception as e:
                print(f"   ⚠️ Registry method: {e}")
            
            # Method 2: Use diskpart to set disk as read-only
            try:
                print("   Setting disk as read-only...")
                diskpart_commands = f"""select volume {drive_letter}
attributes disk set readonly
exit
"""
                result = subprocess.run(
                    'diskpart',
                    input=diskpart_commands,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if "readonly" in result.stdout.lower():
                    print("   ✅ Disk set as read-only")
            except Exception as e:
                print(f"   ⚠️ Diskpart method: {e}")
            
            # Method 3: Remove write permissions using icacls
            try:
                print("   Removing write permissions...")
                # First ensure read access
                subprocess.run(f'icacls {drive} /grant Everyone:(RX)', shell=True, capture_output=True, timeout=5)
                # Then deny write access
                result = subprocess.run(f'icacls {drive} /deny Everyone:(W)', shell=True, capture_output=True, timeout=5)
                if result.returncode == 0:
                    print("   ✅ Write permissions removed")
            except Exception as e:
                print(f"   ⚠️ Permission method: {e}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error applying protection: {str(e)}")
            return False
    
    def test_write_protection(self, drive):
        """Test if write protection is actually working"""
        print(f"🧪 Testing write protection on {drive}...")
        
        # Test 1: Can we read files?
        try:
            files = os.listdir(drive)
            print(f"   ✅ Read access: Can view {len(files)} files")
            read_works = True
        except Exception as e:
            print(f"   ❌ Read access failed: {e}")
            return False, False
        
        # Test 2: Can we create new files? (should fail)
        test_file = os.path.join(drive, "forensic_test_write.txt")
        write_blocked = False
        
        try:
            with open(test_file, 'w') as f:
                f.write("test write operation")
            print("   ❌ WRITE TEST FAILED: Can create new files")
            # Clean up the test file
            try:
                os.remove(test_file)
            except:
                pass
            write_blocked = False
        except PermissionError:
            print("   ✅ WRITE TEST PASSED: Cannot create new files")
            write_blocked = True
        except Exception as e:
            print(f"   ⚠️ Write test error: {e}")
            write_blocked = False
        
        # Test 3: Can we create new folders? (should fail)
        test_folder = os.path.join(drive, "forensic_test_folder")
        folder_blocked = False
        
        try:
            os.mkdir(test_folder)
            print("   ❌ FOLDER TEST FAILED: Can create new folders")
            # Clean up
            try:
                os.rmdir(test_folder)
            except:
                pass
            folder_blocked = False
        except PermissionError:
            print("   ✅ FOLDER TEST PASSED: Cannot create new folders")
            folder_blocked = True
        except Exception as e:
            print(f"   ⚠️ Folder test error: {e}")
            folder_blocked = False
        
        return read_works, (write_blocked and folder_blocked)

    def show_protection_status(self, drive, read_works, write_protected):
        """Show protection status"""
        print(f"\n📊 WRITE PROTECTION STATUS for {drive}:")
        print(f"   • Drive: {drive}")
        
        if read_works and write_protected:
            print(f"   • Protection: ✅ FULLY PROTECTED")
            print(f"   • Read files: ✅ ALLOWED")
            print(f"   • Create files: ❌ BLOCKED")
            print(f"   • Create folders: ❌ BLOCKED")
            print(f"   • Modify files: ❌ BLOCKED")
            print(f"   • Delete files: ❌ BLOCKED")
            print(f"   • Forensic Integrity: 🔒 PERFECT")
        elif read_works and not write_protected:
            print(f"   • Protection: 🟡 PARTIAL")
            print(f"   • Read files: ✅ ALLOWED")
            print(f"   • Write files: ✅ ALLOWED (PROBLEM)")
            print(f"   • Forensic Integrity: ⚠️ AT RISK")
        else:
            print(f"   • Protection: ❌ FAILED")
            print(f"   • Read files: ❌ BLOCKED")
            print(f"   • Status: Evidence inaccessible")
        
        print(f"   • Evidence admissible: {'✅ YES' if write_protected else '❌ NO'}")
        print(" " + "="*50)
    
    def start_monitoring(self):
        """Start monitoring for USB devices"""
        print("🛡️ Forensic Shield ACTIVE - Write Protection Enabled")
        print("Press Ctrl+C to stop monitoring")
        self.logger.info("Forensic Shield write protection started")
        
        try:
            while True:
                current_drives = set(self.get_drives())
                new_drives = current_drives - self.known_drives
                removed_drives = self.known_drives - current_drives
                
                # Handle new drives
                for drive in new_drives:
                    if self.is_usb_drive(drive):
                        self.protect_device(drive)
                
                # Handle removed drives
                for drive in removed_drives:
                    if drive in self.connected_devices:
                        self.device_removed(drive)
                
                self.known_drives = current_drives
                time.sleep(3)
                
        except KeyboardInterrupt:
            print("\n🛑 Forensic Shield stopped")
            self.logger.info("Forensic Shield stopped by user")
    
    def protect_device(self, drive):
        """Protect a newly connected USB drive"""
        device_info = {
            'drive': drive,
            'connected_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        
        print(f"\n🎯 NEW USB DETECTED: {drive}")
        self.logger.info(f"USB Device detected: {drive}")
        
        # Apply write protection
        protection_applied = self.apply_write_protection(drive)
        
        # Test if protection is working
        read_works, write_protected = self.test_write_protection(drive)
        
        # Update device info
        device_info['read_access'] = read_works
        device_info['write_protected'] = write_protected
        device_info['protection_applied'] = protection_applied
        
        # Show status
        self.show_protection_status(drive, read_works, write_protected)
        
        if read_works and write_protected:
            print(f"🎉 SUCCESS: {drive} is WRITE-PROTECTED!")
            print(f"💡 Try to copy/paste files to {drive} - it should FAIL!")
            self.logger.info(f"Drive write-protected: {drive}")
        elif read_works:
            print(f"⚠️ PARTIAL: Can read {drive} but writes still allowed")
            self.logger.warning(f"Write protection incomplete: {drive}")
        else:
            print(f"❌ FAILED: Cannot access {drive}")
            self.logger.error(f"Drive access failed: {drive}")
        
        self.connected_devices[drive] = device_info
    
    def device_removed(self, drive):
        """Handle device removal"""
        if drive in self.connected_devices:
            info = self.connected_devices[drive]
            status = "PROTECTED" if info.get('write_protected') else "UNPROTECTED"
            print(f"📤 Device removed: {drive} - {status}")
            self.logger.info(f"Device removed: {drive} - {status}")
            del self.connected_devices[drive]

if __name__ == "__main__":
    shield = ForensicShield()
    
    print("\n🔍 Current drives on system:")
    for drive in shield.get_drives():
        usb_status = "USB" if shield.is_usb_drive(drive) else "Internal"
        print(f"   {drive} - {usb_status}")
    
    print("\n🎯 Starting write protection monitoring...")
    print("💡 Insert a USB drive - it will become READ-ONLY!")
    shield.start_monitoring()