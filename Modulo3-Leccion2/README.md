# Gestión de Usuarios con roles en flask

## Descripción
Aplicación web desarrollada en Python Flask que permite el manejo de usuarios con diferentes roles (Admin y User).
 
***
## Características:
- Autenticación (usuarios que inician sesión)
- Autorización (roles y permisos usando Flask-Principal)
- Protección de rutas según si el usuario es admin o user
- Simulación de usuarios en memoria

***
## Diagrama de flujo
![Image](https://github.com/user-attachments/assets/1ac23ba3-4903-49fe-9aa4-bf1a6a2fafdd)

## Funciones:

### Login
Se le pide al usuario su Usuario y Contraseña

![Image](https://github.com/user-attachments/assets/60573555-e24a-477b-bc22-cf28884fd3cb)

Muestra mensaje de error en caso de colocar las credenciales incorrectas.

![Image](https://github.com/user-attachments/assets/d1f5eec0-282e-4dd5-9867-133add0262b5)

### Admin
Cuenta con acceso completo.

![Image](https://github.com/user-attachments/assets/a93ec580-30ac-4a47-ad99-28026190842d)

### User
Cuenta con acceso limitado.

![Image](https://github.com/user-attachments/assets/7854937c-a341-43de-a524-9c21eed89b5a)

### Logout
Cierra la sesión iniciada.

![Image](https://github.com/user-attachments/assets/12c756e1-d2e0-4cb5-b86c-32e464310b97)
