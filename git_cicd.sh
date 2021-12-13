#!/bin/bash

git pull origin main
conda activate torch
pip install -r requirements.txt
