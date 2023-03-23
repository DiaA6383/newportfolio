#!/bin/bash

# Change to your project directory
cd /root/newportfolio

# Fetch latest changes from main branch and reset to latest commit
git fetch && git reset origin/main --hard

# Activate the Python virtual environment and install dependencies
source /root/newportfolio/env/bin/activate
pip install -r requirements.txt

# Restart myportfolio service
systemctl restart myportfolio

echo "Site redeployed and myportfolio service restarted"



