# Aplicación Flask: Gestión de Productos de Supermercado

## Descripción general del proyecto
Este proyecto consiste en una aplicación simple desarrollada con Flask que facilita la administración de artículos de un supermercado. Hace uso de plantillas HTML dinámicas con la herencia Jinja2 para dividir la lógica de la presentación (Back-End y Front-End), y posibilita la creación y modificación de productos a través de una interfaz limpia y atractiva. 
La aplicación utiliza un archivo JSON (productos. json) para almacenar datos y simular una base de datos local. 

***

## Estructura del proyecto
- `app.py`: servidor Flask con rutas para listar, crear y editar productos.

- `templates/`: contiene las plantillas base.html, index.html, create.html y edit.html.

- `static/style.css`: define estilos y botones dinámicos con buen diseño.

- `productos.json`: archivo que guarda los productos creados.

- `README.md`: documentación del repositorio.

***
## Funcionamiento

### 1. Página inicial
Al iniciar la pagina solo se mostrará lo que será la tabla y las opciones para crear un producto o regresar a la página de inicio

![Image](https://github.com/user-attachments/assets/3beb3acc-1e98-4244-885e-719fa63873c9)

### 2. Crear producto
Permite añadir un nuevo producto con nombre, precio y categoría.

![Image](https://github.com/user-attachments/assets/618b5659-870e-4919-b640-f89a2a3771d2)

![Image](https://github.com/user-attachments/assets/54a5b807-0bc9-4155-a229-2d7af483f735)


### 3. Página inicial luego de añadir un producto
Se mostrarán todos los productos creados y con la posibilidad de editar los mismos.

![Image](https://github.com/user-attachments/assets/f2d43316-7d65-47a8-84ab-9df03a7eb759)

### 4. Editar producto
Permite modificar los datos de un producto existente.

![Image](https://github.com/user-attachments/assets/0d37ea8c-ef92-4df0-bc08-5e3ad8f1f71c)

***

## Reflexión
Dividir el Back-End del Front-End mejora en gran medida la claridad, el orden y la capacidad de crecimiento de un proyecto. Esta separación permite que cada componente del sistema se desarrolle, actualice y mantenga de manera independiente: el Back-End se ocupa de la lógica y los datos, mientras que el Front-End se centra en cómo se presenta al usuario. 

En este proyecto, el uso de plantillas Jinja2 ayudó a reutilizar estructuras HTML comunes y a mantener el código organizado y consistente. Esta división también favorece la colaboración entre equipos y permite expandir la aplicación sin afectar las funciones ya existentes. En resumen, mejora la eficacia del desarrollo y la calidad del producto final. 