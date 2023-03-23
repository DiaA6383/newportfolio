#!/bin/bash

# Fetch latest changes from main branch and reset to latest commit
git fetch && git reset origin/main --hard

# Activate the Python virtual environment and install dependencies
source /Users/alejandrodiaz/newportfolio/env/bin/activate
pip install -r requirements.txt

# Restart myportfolio service
sudo systemctl restart myportfolio

echo "Site redeployed and myportfolio service restarted"
