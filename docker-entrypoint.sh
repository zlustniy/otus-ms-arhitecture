#!/bin/sh

set -e

. /venv/bin/activate

exec python -m uvicorn otus_service.main:app --host 0.0.0.0 --port ${FASTAPI_PORT:-8000}