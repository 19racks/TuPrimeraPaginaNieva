Mi Primera Página Web con Python y Django
¡Hola! Esta es mi primera página web que hice con Python y Django.

¿Que tiene este proyecto?
Herencia de plantillas: Todas las páginas tienen una base común (base.html) para que se vean similares.

Modelos: Hay tres modelos:

Autor: Guarda el nombre, el correo y la fecha de registro.
Categoría: Solo guarda el nombre de la categoría.
Post: Contiene el título, contenido, el autor (relacionado con Autor), la categoría (relacionada con Categoría) y la fecha de creación.
Formularios: Hay formularios para agregar autores, categorías y posts, además de uno para buscar posts por título.

Patrón MVT: Los datos están en models.py, la lógica está en views.py y las plantillas en la carpeta de plantillas.

Cómo probarlo (el orden es importante, porque si no haces las cosas en este orden, no podrás ver nada o no funcionará del todo bien)
Inicio (http://127.0.0.1:8000/)
¿Qué hace?: Muestra todos los posts que hay.
¿Cómo probarlo?: Abre esta URL primero. Si no hay posts, verás "No hay posts aún". Cuando agregues algunos, aparecerán con su título, autor y categoría.

Agregar Autor (http://127.0.0.1:8000/agregar-autor/)
¿Qué hace?: Te permite crear un autor nuevo.
¿Cómo probarlo?: Ingresa un nombre (por ejemplo, "Juan") y un email (por ejemplo, "juan@email.com"). Luego haz clic en "Guardar" y serás redirigido al inicio.

Agregar Categoría (http://127.0.0.1:8000/agregar-categoria/)
¿Qué hace?: Puedes agregar una nueva categoría.
¿Cómo probarlo?: Escribe algo como "Tecnología", haz clic en "Guardar" y serás redirigido al inicio.

Agregar Post (http://127.0.0.1:8000/agregar-post/)
¿Qué hace?: Permite crear un post con título, contenido, autor y categoría
¿Cómo probarlo?: Escribe un título (como "Mi primer post"), contenido (como "Hola mundo"), selecciona el autor y la categoría que creaste antes, y haz clic en "Guardar". Luego verifica que aparezca en el inicio.

Buscar Posts (http://127.0.0.1:8000/buscar-post/)
¿Qué hace?: Permite buscar posts por título y te devuelve el resultado más cercano o el concreto.
¿Cómo probarlo?: Escribe algo del título (por ejemplo, "Arte con Maria"), haz clic en "Buscar" y deberías ver el post con el autor (ej. "Arte con Maria - Maria").

Dónde encontrar cada cosa
Modelos: En blog/models.py encontrarás los modelos Autor, Categoría y Post
Formularios: Los formularios están en blog/forms.py
Vistas: La lógica de las vistas está en blog/views.py
Plantillas: Los archivos HTML están en blog/templates/blog/, todos usan base.html
Rutas: Las URLs están en blog/urls.py, donde las conecto con las vistas
