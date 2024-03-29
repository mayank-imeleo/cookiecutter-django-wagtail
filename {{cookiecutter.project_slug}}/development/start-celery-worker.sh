#!/bin/bash

# Start a Celery worker

celery -A config.celery worker --loglevel=INFO