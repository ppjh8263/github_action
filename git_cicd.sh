#!/bin/bash
source ~/.poetry/env
poetry install
poetry shell
poe force-cuda11
python api.py
