# Define la versión de Python que deseas utilizar
FROM python:3.9

# Crea una carpeta de trabajo para tu aplicación
WORKDIR /app

# Copia tu código fuente a la imagen de Docker
COPY . .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Especifica el comando por defecto que se ejecutará cuando se inicie el contenedor
CMD [ "python", "./app.py" ]