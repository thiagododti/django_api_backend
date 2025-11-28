#!/bin/sh
set -e

# Aplica migrações
python manage.py migrate --noinput

# Coleta estáticos
python manage.py collectstatic --noinput || echo "Falha collectstatic (talvez nenhum arquivo)"

# Inicia o servidor WSGI via gunicorn na porta definida
exec gunicorn core.wsgi:application \
  --bind 0.0.0.0:${PORT:-3050} \
  --workers 3 \
  --timeout 120
