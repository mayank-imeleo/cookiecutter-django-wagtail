#!/bin/bash

# Start Celery Beat

celery -A config.celery beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler