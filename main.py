#!/usr/bin/env python3
"""
Forensic Shield - Simple Launcher
"""
import threading
import time
import sys
import os

def start_detector():
    """Start the USB detector"""
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
        from core.detector import ForensicShield
        from web.app import dashboard
        
        print("🛡️ Starting USB Protection...")
        shield = ForensicShield()
        
        # Connect detector to dashboard
        original_protect = shield.protect_device
        def enhanced_protect_device(drive):
            device_info = original_protect(drive)
            if device_info:
                dashboard.update_status(device_info, f"USB Protected: {drive}")
            return device_info
        shield.protect_device = enhanced_protect_device
        
        shield.start_monitoring()
    except Exception as e:
        print(f"❌ Detector: {e}")

def start_dashboard():
    """Start the web dashboard"""
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
        from web.app import dashboard
        print("🌐 Starting Dashboard...")
        dashboard.run()
    except Exception as e:
        print(f"❌ Dashboard: {e}")

if __name__ == "__main__":
    print("🚀 Forensic Shield - Cyber Protection System")
    print("   Access: http://127.0.0.1:5000")
    print("   Buttons:")
    print("   • SIMULATE USB - Shows protection logs")
    print("   • TEST PROTECTION - Simulates attacks") 
    print("   • EXPORT LOGS - Downloads activity log")
    print()
    
    detector_thread = threading.Thread(target=start_detector, daemon=True)
    detector_thread.start()
    time.sleep(2)
    start_dashboard()