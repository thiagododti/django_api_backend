# Use uma imagem oficial Python minimal
FROM python:3.12-slim

# Variáveis de ambiente para comportamento Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=3050

# Cria diretório de trabalho
WORKDIR /app

# Instala dependências do sistema (para psycopg2 / build)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements primeiro para cache eficiente
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Cria diretórios necessários
RUN mkdir -p staticfiles media

# Coleta arquivos estáticos (ignora se nada existir ainda)
RUN python manage.py collectstatic --noinput || echo "Sem estáticos para coletar ainda"

# Expõe a porta
EXPOSE 3050

# Copia entrypoint e dá permissão
COPY entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//' /entrypoint.sh && chmod +x /entrypoint.sh

# Comando de entrada
ENTRYPOINT ["/entrypoint.sh"]
