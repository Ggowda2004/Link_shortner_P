#!/bin/sh
set -e

cat > /usr/share/nginx/html/env.js <<EOF
window.RUNTIME_CONFIG = {
  VITE_API_BASE_URL: "${VITE_API_BASE_URL:-}" 
};
EOF

exec "$@"
