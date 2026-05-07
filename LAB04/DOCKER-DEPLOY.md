# Despliegue con Docker

## Pasos

1. **Construir imagen en el directorio**
   ```bash
   docker build . -t i_daw_8080
   ```

2. **Ejecutar contenedor**
   ```bash
   docker run -d --name c_daw_8080 -p 8080:3000 i_daw_8080
   ```

3. **Acceder a la aplicación**
   ```
   http://127.0.0.1:8080/lab04
   ```

## Verificación

- La interfaz carga correctamente
- Se listan los archivos Markdown
- Se puede abrir un archivo
- Se puede crear un archivo nuevo

## Detener

```bash
docker stop c_daw_8080
docker rm c_daw_8080
docker rmi i_daw_8080
```
