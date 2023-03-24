#!/bin/bash

# Activate the virtual environment.
# The 'source' command reads and executes the contents of the specified file,
# in this case, the 'activate' script for the virtual environment.
source /Users/alejandrodiaz/newportfolio/env/bin/activate

pip install -r requirements.txt
#install the requirements.txt file
# Run the unittest discover command to find and run all tests in the 'tests' directory.
# The '-v' flag enables verbose output, providing more detailed information about the tests.
python -m unittest discover -v tests/

