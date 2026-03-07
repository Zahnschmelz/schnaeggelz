#!/bin/bash

python3 -m venv --system-site-packages .venv
source ./.venv/bin/activate
python3 -m pip install -r requirements.txt

python3 ./main.py
