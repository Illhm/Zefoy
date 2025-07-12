#!/data/data/com.termux/files/usr/bin/bash
# Termux installation script for Zefoy automation
set -e

# Update packages
pkg update -y
pkg upgrade -y

# Install Python and Git if not present
pkg install -y python git

# Upgrade pip and install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install Playwright browsers
playwright install --with-deps

echo "Setup complete. Run: python main.py --url <VIDEO_URL>"
