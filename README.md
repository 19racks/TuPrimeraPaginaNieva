¿Qué tiene este proyecto?
- **Herencia de plantillas**: Todas las páginas usan una base común (base.html) para que se vean parecidas.
- **Modelos**: Hay tres:
  - Autor: Nombre, email y fecha de registro.
  - Categoría: Solo el nombre.
  - Post: Título, contenido, autor (conectado a Autor), categoría (conectada a Categoría) y fecha.
 **Formularios**: 
   Uno para agregar autores, categorías y posts.
   Uno para buscar posts por título.
 **Patrón MVT**: Los datos están en models.py, la lógica en views.py y el diseño en las plantillas.

## Cómo probarlo (orden para verlo funcionar correctamente, ya que si iniciamos de abajo para arriba no podremos encontrar nada y no funcionara del todo bien.)

1. **Inicio (http://127.0.0.1:8000/)**  
    **¿Qué hace?**: Te muestra todos los posts que hay.  
    **¿Cómo probarlo?**: Abrí esta URL primero. Si no hay posts, vas a ver "No hay posts aún". Después de agregar algunos, aparecerán con título, autor y categoría.  

2. **Agregar Autor (http://127.0.0.1:8000/agregar-autor/)**  
    **Qué hace**: Acá podés crear un autor nuevo.  
    **¿Cómo probarlo?**: Poné un nombre (como "Juan") y un email (como "juan@email.com"), dale a "Guardar" y te lleva al inicio.  

3. **Agregar Categoría (http://127.0.0.1:8000/agregar-categoria/)**  
    **¿Qué hace?**: Te deja crear una categoría.  
    **¿Cómo probarlo?**: Escribí algo como "Tecnología", clic en "Guardar" y volvés al inicio.  

4. **Agregar Post (http://127.0.0.1:8000/agregar-post/)**  
    **¿Qué hace?**: Acá creás un post con título, contenido, autor y categoría.  
    **¿Cómo probarlo?**: Poné un título (ej. "Mi primer post"), contenido (ej. "Hola mundo"), elegí el autor y categoría que creaste antes, y dale a "Guardar". Después, chequeá que aparezca en el inicio.  

5. **Buscar Posts (http://127.0.0.1:8000/buscar-post/)**  
    **¿Qué hace?**: Busca posts por sus titulos y te da el resultado mas aproximado o exacto.
    **¿Cómo probarlo?**: Escribí algo del título (ej. "Arte con maria"), clic en "Buscar" y deberías ver el post con su autor (ej. "Arte con maria - Maria").  

## Dónde está cada cosa
 **Modelos**: En blog/models.py están Autor, Categoría y Post
 **Formularios**: En blog/forms.py tenés los cuatro formularios
 **Vistas**: En blog/views.py está toda la lógica de las páginas
 **Plantillas**: En blog/templates/blog/ están los archivos HTML, todos usan base.html
 **Rutas**: En blog/urls.py conecto las URLs con las vistas
