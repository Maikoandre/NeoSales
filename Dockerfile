# Use uma imagem base do Python
FROM python:3.12-slim

# Defina as variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crie e defina o diretório de trabalho
WORKDIR /app

# Instale o uv, a ferramenta de pacotes Python
RUN pip install uv

# Copie o arquivo de dependências
COPY requirements.txt ./

# Instale as dependências a partir do requirements.txt
RUN uv pip install --no-cache-dir --system -r requirements.txt

# Copie o restante do código do projeto
COPY . .

# Exponha a porta 8000
EXPOSE 8000

# Comando para rodar as migrações e iniciar o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]