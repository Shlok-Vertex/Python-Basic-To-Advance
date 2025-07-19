# 🐍 Python Installation and Setup Guide.

This guide explains how to install and set up Python on Windows, macOS, and Linux. 🚀

---

## 🪟 Windows. 

1. **Download Python:**
   - Go to the [official Python website](https://www.python.org/downloads/).
   - Download the latest Python installer for Windows.

2. **Run the Installer:**
   - Double-click the downloaded `.exe` file.
   - **Important:** Check the box that says **"Add Python to PATH"**.
   - Click **Install Now** and follow the prompts.

3. **Verify Installation:**
   - Open **Command Prompt** (`Win + R`, type `cmd`, press Enter).
   - Run:
     ```
     python --version
     ```
   - You should see the installed Python version.

---

## 🍏 macOS. 

1. **Check for Pre-installed Python:**
   - Open **Terminal**.
   - Run:
     ```
     python3 --version
     ```
   - If Python 3 is not installed or you want the latest version, continue below.

2. **Install Homebrew (if not installed):**
   - In Terminal, run:
     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

3. **Install Python:**
   - Run:
     ```
     brew install python
     ```

4. **Verify Installation:**
   - Run:
     ```
     python3 --version
     ```

---


- Activate the virtual environment:
  - **Windows:** `venv\Scripts\activate`
  - **macOS/Linux:** `source venv/bin/activate`

---

## 🔗 Useful Links.

- [Python Downloads](https://www.python.org/downloads/)
- [Python Documentation](https://docs.python.org/3/)
- [Homebrew](https://brew.sh/)


