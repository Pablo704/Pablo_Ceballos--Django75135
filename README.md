# Curso Python - Django
# Blog de Competencias Automovilísticas

Este proyecto es una aplicación web construida con Django siguiendo el patrón MVT (Model-View-Template). Permite registrar y visualizar información sobre carreras, pilotos y equipos, además de contar con un buscador para encontrar datos específicos.

---

## 🚀 Instalación y Configuración

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/blog_autos.git
   cd blog_autos
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplica migraciones a la base de datos:**
   ```bash
   python manage.py migrate
   ```

5. **Ejecuta el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

---

## 📌 Funcionalidades

### **1️⃣ Agregar Carreras, Pilotos y Equipos**
- 📍 Ubicación: `http://127.0.0.1:8000/admin/`
- Agrega nuevas carreras, pilotos y equipos desde la interfaz de administración.

### **2️⃣ Ver listado de Carreras**
- 📍 Página principal: `http://127.0.0.1:8000/`
- Se listan todas las carreras registradas con detalles (nombre, fecha, circuito, pilotos participantes, equipo, etc.).

### **3️⃣ Ver información de un Piloto específico**
- 📍 URL: `http://127.0.0.1:8000/pilotos/`
- Se muestran los pilotos registrados y su información (nombre, equipo, puntos acumulados, etc.).

### **4️⃣ Buscar una Carrera o un Piloto**
- 📍 Barra de búsqueda en la página principal.
- Puedes buscar carreras por nombre o fecha.
- También puedes buscar pilotos por nombre o equipo.

### **5️⃣ Agregar Nuevas Carreras y Pilotos desde la Web**
- 📍 Formularios en: `http://127.0.0.1:8000/nueva_carrera/` y `http://127.0.0.1:8000/nuevo_piloto/`
- Permite ingresar nuevas carreras y pilotos sin necesidad de usar el panel de administración.

### **6️⃣ Ver detalles de una Carrera específica**
- 📍 URL: `http://127.0.0.1:8000/carreras/<id>/`
- Muestra información completa de la carrera seleccionada: nombre, fecha, circuito, lista de pilotos y equipos participantes.

### **7️⃣ Sistema de Comentarios**
- En cada página de detalles de una carrera, los usuarios pueden dejar comentarios sobre el evento.
- 📍 Sección de comentarios en: `http://127.0.0.1:8000/carreras/<id>/`

### **8️⃣ Panel de Administración de Django**
- 📍 `http://127.0.0.1:8000/admin/`
- Desde aquí, los administradores pueden gestionar carreras, pilotos y equipos de manera sencilla.

---

## 🔥 Notas Finales
- Si necesitas restablecer la base de datos, puedes eliminar `db.sqlite3` y volver a correr `python manage.py migrate`.
- Puedes modificar los estilos en la carpeta `static/css/` para personalizar el diseño del sitio.
- Se recomienda poblar la base de datos con al menos 5 carreras y 10 pilotos para hacer pruebas completas.

---

¡Listo! 🚗💨 Ahora puedes comenzar a probar la aplicación. Si tienes dudas, revisa la documentación de Django en [https://docs.djangoproject.com/es/](https://docs.djangoproject.com/es/).

