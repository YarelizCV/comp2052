# Modulo1-Lección3: Gestionar usuarios

## Descripción
Este proyecto de Flask se enfoca en gestionar usuarios utilizando almacenamiento en memoria(listas). El objetivo de este proyecto es practicar lectura, validación y devolición de datos mediante JSON, manejar error apropiadamente y estructurar un pequeño backend funcional.

***

## Rutas
Utilizando POSTMAN.

### GET /info
Devuelve un JSON que describe el sistema (autor, descripción y versión)

![Image](https://github.com/user-attachments/assets/2b821c71-df81-40e4-8019-959e827a9edc)

### POST /crear_usuario
Recibe datos en JSON (`nombre` y `correo`), los valida y si son correctos, crea un nuevo usuario y lo guarda en una lista.

![Image](https://github.com/user-attachments/assets/6dcdf097-b8d9-417c-a139-72af56317c7d)

Mensaje que se mostraría si falta algún dato.

![Image](https://github.com/user-attachments/assets/ba22a5a2-9b77-40b4-bf70-03684ba8a33f)

### POST /usuario
Devuelve un JSON con la lista de todos los usuarios creados hasta el momento.

![Image](https://github.com/user-attachments/assets/6bacfde7-1d85-4bea-8647-d644aa2df208)
