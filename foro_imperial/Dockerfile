# Usa una imagen oficial de Python como base. 'slim' es una versión ligera.
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor.
WORKDIR /app

# Copia el archivo de requerimientos al directorio de trabajo.
COPY requirements.txt .

# Instala las dependencias de Python listadas en el archivo.
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de tu aplicación al contenedor.
COPY foro_imperial.py .

# Expone el puerto 8080 para que el contenedor pueda recibir tráfico en él.
EXPOSE 8080

# El comando que se ejecutará cuando el contenedor se inicie.
# Usamos gunicorn para lanzar la aplicación de forma robusta.
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "foro_imperial:app"]