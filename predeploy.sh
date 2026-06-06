#!/bin/bash
set -e

python - << 'EOF'
import os
import dj_database_url

url = os.environ.get('DATABASE_URL', 'NOT SET')

# Show masked raw URL
if '@' in url:
    scheme = url.split('://')[0]
    after_scheme = url.split('://')[1]
    user_pass, host_db = after_scheme.rsplit('@', 1)
    user = user_pass.split(':')[0] if ':' in user_pass else user_pass
    print(f'[predeploy] DATABASE_URL: {scheme}://{user}:****@{host_db}')
else:
    print(f'[predeploy] DATABASE_URL: {url}')

# Show what dj_database_url actually parses — catches special char issues
parsed = dj_database_url.parse(url)
print(f'[predeploy] Parsed → host={parsed.get("HOST")} port={parsed.get("PORT")} name={parsed.get("NAME")} user={parsed.get("USER")} password_len={len(parsed.get("PASSWORD") or "")}')
EOF

python manage.py migrate --noinput
