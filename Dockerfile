# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o resto do código da aplicação
COPY . .

# Definir o comando para iniciar a aplicação
CMD ["python", "app.py"]
