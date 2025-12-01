# Django API Backend

Backend em Django 5 + Django REST Framework, preparado para APIs REST com autenticação JWT, documentação OpenAPI/Swagger e filtros/paginação. Inclui deploy via Docker (Gunicorn) e suporte a SQLite/PostgreSQL.

## Visão Geral
- API REST com DRF e JWT (access/refresh/verify).
- Documentação interativa em `/docs` e schema em `/schema`.
- Paginação padrão (10 itens/página) e filtros via `django-filter`.
- CORS habilitado (por padrão permite `http://localhost:3000`).
- Usuário customizado (`apps.usuario.Usuario`) e módulo de clientes (`apps.cliente`).

## Tecnologias
- Django 5.2, Django REST Framework 3.16
- SimpleJWT, drf-spectacular (Swagger), django-filter, django-cors-headers
- Python 3.12, Gunicorn (produção), Pillow, psycopg2 (PostgreSQL opcional)

## Requisitos
- Python 3.12+
- Docker e Docker Compose (opcional, para containerização)

## Variáveis de Ambiente (.env)
Crie um arquivo `.env` na raiz. Exemplo mínimo (SQLite):
```
SECRET_KEY=troque_esta_chave
DEBUG=true
ALLOWED_HOSTS=*
BANCO_SELECIONADO=1
JWT_ACCESS_MINUTES=60
JWT_REFRESH_DAYS=1
LOG_REGISTER=false
PORT=3050
```

Para usar PostgreSQL (`BANCO_SELECIONADO=2`):
```
BANCO_SELECIONADO=2
DB_NAME_POSTGRE=meu_banco
DB_USER_POSTGRE=meu_usuario
DB_PASSWORD_POSTGRE=minha_senha
DB_HOST_POSTGRE=localhost
DB_PORT_POSTGRE=5432
```

Observações:
- Em produção, sempre defina `SECRET_KEY` segura e `DEBUG=false`.
- Ajuste CORS em `core/settings.py` (lista `CORS_ALLOWED_ORIGINS`).
- Logs rotativos podem ser habilitados com `LOG_REGISTER=true` (diretório `logs/`).

## Como Rodar (Local)
No Windows PowerShell:
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```
Aplicação disponível em `http://localhost:8000`.

## Como Rodar (Docker)
Este compose usa uma rede externa `mynet`. Crie-a uma vez:
```
docker network create mynet
```
Suba a aplicação:
```
docker compose up -d --build
```
Aplicação disponível em `http://localhost:3050` (porta mapeada no `docker-compose.yml`).

Parar e remover containers:
```
docker compose down
```

## Documentação da API
- Base URL (dev): `http://localhost:8000`
- Base URL (Docker): `http://localhost:3050`
- Swagger UI: `http://localhost:3050/docs/` (interativo)
- OpenAPI Schema: `http://localhost:3050/schema/` (JSON/YAML)

Todos os endpoints, parâmetros, exemplos de uso e códigos de resposta estão documentados no Swagger. Utilize as URLs acima para consultar a documentação atualizada da API.

## Paginação e Ordenação
- Paginação por página (`page`, `page_size=10` padrão).
- Ordenação pode ser adicionada conforme necessidade (não incluída por padrão).

## Estrutura Simplificada
```
apps/
	cliente/ (CRUD de clientes)
	usuario/ (usuário customizado + endpoint autenticado)
core/
	settings.py (DRF, JWT, CORS, DB, logs)
	urls.py (JWT, Swagger, apps)
```

## Desenvolvimento
- Migrações: `python manage.py makemigrations && python manage.py migrate`
- Superusuário: `python manage.py createsuperuser`
- Coletar estáticos: `python manage.py collectstatic`

## Notas
- Banco selecionado por `BANCO_SELECIONADO` (1=SQLite, 2=PostgreSQL).
- Em produção, rode atrás de um proxy reverso (Nginx) e configure `ALLOWED_HOSTS`.
- Ajuste `CORS_ALLOWED_ORIGINS` conforme o front-end.

