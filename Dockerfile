# Usar uma imagem base do Python
FROM python:3.10-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar todos os arquivos do projeto para dentro do container
COPY . /app

# Definir o comando padrão para rodar a aplicação
CMD ["python", "calculadora.py"]
