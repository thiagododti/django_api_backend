FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=America/Sao_Paulo

WORKDIR /app

RUN apt-get update \
    && apt-get install -y tzdata netcat-openbsd libpq-dev gcc \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . .

RUN mkdir -p /vol/web/static /vol/web/media

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["gunicorn", "core.wsgi:application","--bind", "0.0.0.0:8000","--workers", "3","--threads", "2","--timeout", "60"]
