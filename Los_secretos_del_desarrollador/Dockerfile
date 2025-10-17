# 1. La Base: Usamos una imagen oficial de Nginx.
# Nginx es un servidor web muy ligero y rápido, perfecto para esto.
# 'alpine' es una versión ultra-ligera de Linux.
FROM nginx:alpine

# 2. La Copia: Copiamos tu desafío.
# Copia el archivo 'index.html' de tu carpeta...
# ...dentro de la carpeta '/usr/share/nginx/html/' del contenedor.
# Esta es la carpeta donde Nginx busca las páginas web por defecto.
COPY index.html /usr/share/nginx/html/index.html