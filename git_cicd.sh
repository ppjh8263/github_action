#!/bin/bash
soruce ~/.poetry/env
poetry install
poetry shell
poe force-cuda11
python api.py
