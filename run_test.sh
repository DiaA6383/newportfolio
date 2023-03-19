#!/bin/bash
source /root/newportfolio/env/bin/activate
cd /root/
python -m unittest discover -v tests/
