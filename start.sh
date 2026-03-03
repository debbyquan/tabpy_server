#!/bin/sh
set -eu

echo "PORT=$PORT"
echo "Starting TabPy on 127.0.0.1:9004 ..."
tabpy --host 127.0.0.1 --port 9004 --logging-level INFO &

TABPY_PID=$!
echo "TabPy pid=$TABPY_PID"

echo "Starting Caddy on :$PORT ..."
exec caddy run --config /etc/caddy/Caddyfile --adapter caddyfile
