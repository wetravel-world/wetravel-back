#!/bin/bash
set -e

# Print masked DATABASE_URL so Railway deploy logs show what's being used
python - << 'EOF'
import os

url = os.environ.get('DATABASE_URL', 'NOT SET')
if '@' in url:
    scheme = url.split('://')[0]
    after_scheme = url.split('://')[1]
    user_pass, host_db = after_scheme.split('@', 1)
    user = user_pass.split(':')[0] if ':' in user_pass else user_pass
    print(f'[predeploy] DATABASE_URL: {scheme}://{user}:****@{host_db}')
else:
    print(f'[predeploy] DATABASE_URL: {url}')
EOF

python manage.py migrate --noinput
