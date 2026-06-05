# Lab 08 — Destinos Turísticos en Django

Aplicación web desarrollada con Django para gestionar destinos turísticos.  
**Asignatura:** Desarrollo de Aplicaciones Web  
**Docente:** Mgter. Carlo Corrales Delgado

---

## Estructura del Proyecto

```
lab08/
├── lab08/                  # Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── destinos_turisticos/    # Aplicación principal
│   ├── templates/
│   │   └── destinos_turisticos/
│   │       ├── base.html
│   │       ├── lista.html
│   │       ├── form.html
│   │       └── confirmar_eliminar.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## Instalación y Ejecución

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd lab08

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# 5. Crear superusuario (para el admin)
python manage.py createsuperuser

# 6. Ejecutar el servidor
python manage.py runserver
```

Luego abrir: http://127.0.0.1:8000/

---

## Funcionalidades

- **Listar** todos los destinos turísticos en tarjetas.
- **Agregar** un nuevo destino con imagen.
- **Modificar** los datos de un destino existente.
- **Eliminar** un destino con confirmación previa.
- Destinos con oferta se muestran con etiqueta especial.
- Panel de administración en `/admin/`.

## Modelo `DestinosTuristicos`

| Campo              | Tipo          | Descripción                   |
|--------------------|---------------|-------------------------------|
| `nombreCiudad`     | CharField     | Nombre de la ciudad           |
| `descripcionCiudad`| TextField     | Descripción del destino       |
| `imagenCiudad`     | ImageField    | Foto del destino (opcional)   |
| `precioTour`       | DecimalField  | Precio en soles               |
| `ofertaTour`       | BooleanField  | Si está en oferta o no        |

## Tags DTL utilizados

- `{% for %}` — para iterar sobre todos los destinos
- `{% if %}` — para mostrar imagen o ícono por defecto, y para la etiqueta de oferta
- `{% url %}` — para los enlaces de navegación
- `{% csrf_token %}` — en todos los formularios
- `{% block %}` / `{% extends %}` — para la herencia de plantillas
