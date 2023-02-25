#!/bin/bash

# Kill all existing tmux sessions
tmux kill-server

# Change to your project directory
cd /root/newportfolio

# Fetch latest changes from main branch and reset to latest commit
git fetch && git reset origin/main --hard

# Activate the Python virtual environment
source /root/newportfolio/env/bin/activate
# Upgrade pip to the latest version
pip install --upgrade pip
# Install Python dependencies using pip
pip install -r requirements.txt

# Start a new tmux session and run the Flask server
tmux new-session -d -s myflaskserver 'cd /root/newportfolio && source /root/newportfolio/env/bin/activate && flask run --host=0.0.0.0'

echo "Flask server started in a new tmux session"
#clone repo to root and ssh 
