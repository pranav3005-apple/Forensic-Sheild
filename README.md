# 🛡️ Forensic Shield - USB Write Protection System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.0-lightgrey)
![Real-time](https://img.shields.io/badge/Real--time-Protection-orange)
![Forensic](https://img.shields.io/badge/Forensic-Compliant-green)

> A professional-grade digital evidence protection system that automatically detects USB devices and applies **real write protection** to maintain forensic integrity for legal proceedings.

---

## 📋 Table of Contents
- [Installation](#-installation)
- [Usage](#-usage)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Technical Details](#-technical-details)
- [Use Cases](#-use-cases)
- [Contributing](#-contributing)
- [Support](#-support)
- [Acknowledgments](#-acknowledgments)

---

## 🚀 Installation

### **Prerequisites**
- Python **3.8+**
- **Windows OS** (required for USB write protection)

### **Quick Start**
```bash
# Clone the repository
git clone https://github.com/yourusername/forensic-shield.git
cd forensic-shield

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
````

### **Dependencies**

Create a `requirements.txt` file with:

```
flask==2.3.0
psutil==5.9.0
```

---

## 💻 Usage

### **Starting the System**

```bash
python main.py
```

The system will start:

* **USB Detection & Protection Engine**
* **Web Dashboard:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

### **Basic Operations**

| Operation               | Description                     |
| ----------------------- | ------------------------------- |
| 🟢 **Start System**     | `python main.py`                |
| 🌐 **Access Dashboard** | Open `http://127.0.0.1:5000`    |
| 💽 **Simulate USB**     | Click “Simulate USB Connection” |
| 🧪 **Test Protection**  | Click “Test Protection”         |
| 📦 **Export Logs**      | Click “Export Forensic Logs”    |

#### **Example Protection Log**

```
[14:23:45] 🎯 NEW USB DEVICE DETECTED: D:\
[14:23:45] 🛡️ APPLYING WRITE PROTECTION...
[14:23:45]    Removing write permissions...
[14:23:45] 🧪 TESTING WRITE PROTECTION ON D:\...
[14:23:45]    ✅ Read access: Can view 8 files
[14:23:45]    ✅ WRITE TEST PASSED: Cannot create new files
[14:23:45]    ✅ FOLDER TEST PASSED: Cannot create new folders
```

---

## 🌟 Features

### 🔒 **Core Protection Features**

* **Automatic USB Detection** – Instantly detects when USB drives are plugged in.
* **Real Write Blocking** – Prevents file/folder creation, modification, or deletion.
* **Read Access Maintained** – Allows safe forensic analysis of data.
* **Integrity Verification** – Confirms write protection is working.
* **Forensic Compliance** – Preserves chain of custody for evidence.

### 📊 **Real-time Monitoring**

* **Live Status Updates** (every 3 seconds)
* **Server-Sent Events (SSE)** for live logs
* **Dynamic Connection Indicators**
* **Automatic Log Stream Refresh**

### 🎮 **Interactive Controls**

* USB Connection Simulation
* Attack/Threat Testing
* Forensic Log Export
* Live Terminal with real-time updates

### 🎨 **Professional Dashboard**

* **Cyberpunk UI** – Neon green/blue design
* **Responsive Layout** – Works on desktop & mobile
* **Interactive Feedback** – Animated buttons & live metrics
* **Enterprise Ready** – Suitable for demos & production

---

## 📁 Project Structure

```
forensic-shield/
├── main.py                 # Main application launcher
├── requirements.txt        # Python dependencies
├── src/
│   ├── core/
│   │   └── detector.py     # USB detection & protection engine
│   └── web/
│       ├── app.py          # Flask web server
│       └── templates/
│           └── index.html  # Dashboard interface
└── logs/                   # Forensic activity logs (auto-created)
```

---

## 🔌 API Endpoints

### **Dashboard Routes**

| Method | Endpoint                 | Description                  |
| ------ | ------------------------ | ---------------------------- |
| GET    | `/`                      | Dashboard Interface          |
| GET    | `/api/status`            | System Status                |
| GET    | `/api/devices`           | Connected USB Devices        |
| GET    | `/api/logs`              | Activity Logs                |
| GET    | `/api/protection_status` | Real-time Protection Metrics |

### **Interactive Endpoints**

| Method | Endpoint                   | Description             |
| ------ | -------------------------- | ----------------------- |
| POST   | `/api/simulate_protection` | Simulate USB Connection |
| POST   | `/api/simulate_attack`     | Test Protection System  |
| POST   | `/api/disconnect_usb`      | Simulate USB Removal    |
| GET    | `/api/export_logs`         | Download Logs           |
| POST   | `/api/clear_logs`          | Clear Terminal Display  |

### **Real-time Features**

| Method | Endpoint             | Description                      |
| ------ | -------------------- | -------------------------------- |
| GET    | `/api/live_logs`     | Server-Sent Events for live logs |
| GET    | `/api/system_health` | System performance metrics       |

---

## 🛠️ Technical Details

### **Protection Mechanism**

```python
def protect_device(drive):
    """Apply write protection to USB device"""
    # 1. Remove write permissions
    # 2. Set read-only access
    # 3. Enable integrity monitoring
    # 4. Verify protection is active
```

### **Real-time Features**

* Server-Sent Events (SSE) for log streaming
* Dashboard auto-refresh without reloads
* Instant threat response logging
* Persistent state management

---

## 🎯 Use Cases

### 🔍 Digital Forensics

* Evidence Preservation
* Legal Chain of Custody
* Secure Incident Response

### 🏢 Enterprise Security

* Data Loss Prevention
* USB Device Policy Enforcement
* Comprehensive Audit Trail

### 🎓 Education & Demos

* Security Training Modules
* Forensic Education Tools
* Product Demonstrations

---

## 🤝 Contributing

We welcome community contributions to enhance **Forensic Shield**!

### **Development Setup**

```bash
# Fork the repository
git clone https://github.com/yourusername/forensic-shield.git
cd forensic-shield

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### **Contribution Steps**

1. **Fork** the project
2. **Create** your feature branch

   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes

   ```bash
   git commit -m "Add some AmazingFeature"
   ```
4. **Push** to your branch

   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**


## 🆘 Support

For support and queries:

📧 **Email:** [pranav.gosula99@gmail.com](mailto:pranav.gosula99@gmail.com)


---

## 🙏 Acknowledgments

* Built with **Python** and **Flask**
* Inspired by **Digital Forensic Best Practices**
* **Cyberpunk UI** design elements
* Real-time web technologies

---

> **Forensic Shield** — Protecting Digital Evidence. 🛡️

```

