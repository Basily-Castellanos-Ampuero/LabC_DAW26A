# ─────────────────────────────────────────────────────────────────
# Dockerfile — Lab 04: Markdown Navigator
# Imagen: node:20-alpine (ligera y segura)
# Puerto: 3000 (interno) → 8080 (host)
# ─────────────────────────────────────────────────────────────────

# Etapa 1: imagen base ligera
FROM node:20-alpine

# Metadatos de la imagen
LABEL maintainer="DAW Lab 04"
LABEL description="Markdown Navigator - Ajax + NodeJS"

# Crear directorio de trabajo dentro del contenedor
WORKDIR /app

# ── Instalar dependencias primero (aprovecha la caché de Docker) ──
# Copiar solo package.json antes del código fuente
COPY package.json ./

# Instalar dependencias de producción únicamente
RUN npm install --omit=dev

# ── Copiar el código fuente ───────────────────────────────────────
COPY server.js   ./
COPY index.html  ./

# Crear directorio para archivos Markdown y copiar los de ejemplo
RUN mkdir -p markdown_files
COPY markdown_files/ ./markdown_files/

# ── Seguridad: ejecutar como usuario no-root ──────────────────────
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN chown -R appuser:appgroup /app
USER appuser

# ── Exponer el puerto que usa el servidor ─────────────────────────
EXPOSE 3000

# ── Healthcheck: verifica que el servidor responda ────────────────
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD wget -qO- http://localhost:3000/lab04 || exit 1

# ── Comando de inicio ─────────────────────────────────────────────
CMD ["node", "server.js"]
