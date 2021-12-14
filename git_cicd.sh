#!/bin/bash
git pull origin main
source ~/.poetry/env
poetry install
poetry shell
poe force-cuda11
python api.py
