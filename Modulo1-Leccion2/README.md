# Modulo 1 - Leccion 2: Cliente/Servidor

## Descripción
En este servidor de Flask se ha implementado una arquitectura cliente-servidor sencilla, la cual cuenta con dos rutas principales: GET /info y POST /mensaje. El objetivo de este proyecto es prácticar cómo interactúan cliente y servidor mediante peticiones HTTP usando Flask.

## Diagrama de flujo
![Image](https://github.com/user-attachments/assets/464156e5-97ef-4d34-81cf-e5845866f243)

***
## Rutas
### GET /info
El servidor devuelve un JSON que contiene información básica sobre el API (descripción y nombre).
- Utilizado para que un cliente pueda obtener detalles del sistema.

![Image](https://github.com/user-attachments/assets/ec3572f9-3be5-4ffb-94f6-f0aeb5f131e5)


### POST /mensaje
El servidor recibe un JSON con un mensaje enviado por el cliente, y responde con otro JSON que incluye el contenido del mensaje personalizado.
- Utilizado para procesar datos enviados por el cliente.

![Image](https://github.com/user-attachments/assets/a18c339d-1bf1-4e30-96f8-b63f981f7393)