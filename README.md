# PROYECTO FINAL - CATS AND DOG BLOG

Sitio Web que permite crear páginas tipo blog para que los usuarios registrados creen contenido sobre sus mascotas, en específico sobre Perros y Gatos.

## CONSIDERACIONES IMPORTANTES

El sistema permite registrar nuevos escritores de blog, loguearse, crear/editar/publicar/eliminar páginas y/o contenido que el usuario considere que quiere compartir en Internet.

- Para agregar contenido se debe estar registrado en la plataforma

- Las personas registradas solo podran hacer operaciones CRUD sobre su propio contenido

- Se puede agregar una imagen principal del contenido (no obligatorio)

- Para visualizar el contenido y que sea público para todos, el mismo debe publicarse desde la administración del sitio. 

- Los usuarios registrados, pueden ingresar haciendo click en la imagen de la parte superior derecha (después de loguearse), y desde allí modificar su perfil, incluyendo agregar o modificar su Avatar. 

- Si no se agrega imagen principal al Blog, se le asignará una por defecto. Esta se visualiza solamente en la vista pública donde todas las personas tienen acceso. 

## CONFIGURACIÓN

1. Crea una carpeta en tu computadora y dento de ésta debes clonar el Repositorio

> `git clone https://github.com/dahguz1980/petsBlog.git

2. Abre el Visual Studio Code y Abre la Carpeta ***petsBlog***

3. Abre el Archivo requirements.txt dentro de VSCode y presiona el botón "crear entorno".

- primero elegir el entorno virtual `venv`, 
- luego el intérprete Python (última versión)
- y finalmente pregunta por las dependencias: elegimos requirements.txt.

   Una vez ejecutado se debe crear el entorno virtual .venv 

4. Activar el entorno virtual

> En Windows ejecuta `.\venv\Scripts\activate`

> En Mac o Linux ejecuta `source .venv/bin/activate`

5. Abre el terminal en VSC, verifica que el entorno virtual está activo (.venv) 

> Ejecuta `pip list` y verifica que todas las dependencias están instaladas

6. Ingresa en la carpeta project y ejecuta: 

    ***En Mac cambiar python por python3***

> `python manage.py collectstatic` 
> 
> `python manage.py makemigrations`
> 
> `python manage.py migrate`
> 
> `python manage.py runserver`

7. Ingresa en el Browser de tu preferencia y ingresa a la siguiente dirección: 

> `http:\\localhost:8000`


