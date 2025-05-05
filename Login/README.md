# Autenticación Básica en Flask

## Descripción
Este proyecto implementa una autenticación básica en Flask usando Flask-Login, manejando usuarios autenticados y protegiendo rutas restringidas.
Además, se construyó un flujo de autenticación y un esquema de usuarios incluyendo nombre, contraseña en hash y roles/permisos.

## Diagrama de flujo

![Image](https://github.com/user-attachments/assets/4e6a35be-37c0-4a90-87b5-30389ccd1f61)

***

## Rutas

### `/` → Home Page
Contiene enlaces de navegación a login y dashboard.

![Image](https://github.com/user-attachments/assets/3b9676b8-5b26-4b39-96e2-35df4ed1c20e)

### `/login` → Login Page
Muestra un formulario para ingresar nombre de usuario y contraseña.
-  Si las credenciales son válidas, redirige al dashboard.

![Image](https://github.com/user-attachments/assets/6727e8fe-3660-4b74-a979-1ac462f5e5bf)

- Si las credenciales son inválidas, muestra un mensaje de error.

![Image](https://github.com/user-attachments/assets/db33b699-66ad-4e76-93f0-1117c856f4a3)

### `/dashboard` → Dashboard 
- Ruta protegida; solo accesible si el usuario ha iniciado sesión.
- Muestra un mensaje de bienvenida y el rol del usuario.

![Image](https://github.com/user-attachments/assets/44314df1-94d1-4787-b637-3dd50b0086db)

### `/logout` → Logout
- Cierra la sesión del usuario autenticado.
- Redirige de vuelta a la página de inicio (`/`).
***

##  Usuarios de prueba

![Image](https://github.com/user-attachments/assets/cc8e739e-ec3b-4f94-be13-948f7748dbcd)
