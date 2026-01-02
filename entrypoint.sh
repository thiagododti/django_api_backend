#!/bin/sh

echo "Aguardando banco de dados..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "Banco disponível."

python manage.py migrate --noinput

python manage.py createsuperuser \
  --noinput \
  --username "$DJANGO_SUPERUSER_USERNAME" \
  --email "$DJANGO_SUPERUSER_EMAIL" || true

exec "$@"
