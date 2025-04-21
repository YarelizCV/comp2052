# Manejo y validacion de usuario con Flask-WTF
Github: [Modulo2-Leccion2](https://github.com/YarelizCV/comp2052/tree/main/Modulo2-Leccion2)

## Descripción
En este proyecto se han utilizado herramientas como **Flask** y **Flask-WTF**. Se han implementado validaciones para los campos de: nombre, correo y contraseña. 

***

## Validaciones implementadas

Este formulario cuenta con las siguientes validaciones:

- **Nombre**:
    - Obligatorio 
    - Mínimo 3 caracteres

- **Correo**:
    - Obligatorio
    - Contener el formato de correo válido

- **Contraseña**:
    - Obligatoria
    - Contar con mínimo 6 caracteres
    - Deben de coincidir 

***
## Pestañas de validación

### Validación del largo del nombre
Si el nombre no cuenta con los caracteres necesarios mostrará un aviso.

![Image](https://github.com/user-attachments/assets/18c6ebe5-c41c-4504-80bb-34f7b3182f88)

### Nombre vacío
Si no se llena este campo mostrará un aviso de que se debe rellenar.

![Image](https://github.com/user-attachments/assets/2083f9e1-7d9c-4013-8a56-4da98087cccf)

### Correo inválido
Si no cumple con el formato necesario se mostrará un aviso de que el correo es inválido.

![Image](https://github.com/user-attachments/assets/409e62ee-9ed4-4a86-8e92-00cb769d0c32)

### Correo vacío
Si el campo no es llenado mostrará un aviso.

![Image](https://github.com/user-attachments/assets/e9aa93af-5680-481d-8785-8bc26f239281)

### Contraseña corta
Mostrará un aviso si la contraseña no cumple con el mínimo de 6 caracteres

![Image](https://github.com/user-attachments/assets/3f980071-0f60-4b25-b7f3-c0456bdb906d)

### Contraseña distinta
Mostrará un aviso si las contraseñas no coinciden.

![Image](https://github.com/user-attachments/assets/8ab0dbc7-135d-467c-98d2-7c16bf38c1e1)

### Validación de registro
Se redigirá a una nueva pestaña donde se confirmirá tu registro.

![Image](https://github.com/user-attachments/assets/23b225a7-cca0-44b1-afe8-745b55985864)


