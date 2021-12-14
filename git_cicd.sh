#!/bin/bash
git pull origin main
source ~/.poetry/env
poetry install
poetry run poe force-cuda11
poetry run python api.py
