                                                 Informe Grupo 33
		              Tarea 3 
Participantes:
-Ignacia Delaigue     - 201704160-9


Resumen de lo hecho en la TAREA 3:
En la carpeta Tarea3 se encuentran varios archivos, explicamos a continuación:

-config.py se encuentra la configuración predeterminada con la respectiva contraseña, base de datos (su nombre), etc, solo fue reemplazado según lo explicado en ayudantia. 

-main.py vendría siendo nuestro main echo en py apoyado por Flask, aquí es donde se encuentran las api con sus links de consultas, teniendo los metodos GET POST PUT y DELETE por cada tabla. Tambien se encuentran las 3/8 consultas que se me pidieron

-models.py tenemos el modelo de las tablas de nuestra nueva base de datos, con las respectivas tablas del modelo establecido en la tarea 2 

-archivos_nombres.php vendria siendo la vista de la tabla en su backend

-archivos_nombres.html vendria siendo la vista de la tabla en su frontend

-Se probó en postman y al menos mostraba los get y post

-los archivos html y php deben unirse al curl, ya que es el vinculo que une la api con nueva base de datos (deberian ser los mismo de la tarea 2)


_________________________________________
Supuestos y Consideraciones a lo largo del trabajo de la Tarea 2 para tener en consideración: 

- La tabla "usuario" fue reecha al igual que la base de datos entera (por ello se llama posgress y no posgres), esto debido a que "id" de "usuario" tuviera caracter serial, para que fuera atomatico su uso. 

- Se cambió la cantidad de caracteres en "contraseña" debido a que al hacer hashpass, tiraba 60 caracteres. 

-Se agregó una imagen con los datos de los alumnos (nosotros) en la página principal, guardada en la carpeta img. (imagen propia).

-Se hizo uso de html para darle cierta estetica a la imagen implementada. (codigo propio)

-Se eliminó un include (por ejemplo, que se encontraba en el navbar) debido a que generaba un bucle de redireccionamiento infinito, este include estaba incluido de primera en los archivos entregados en la tarea.

-Se modifico la imagen del comienzo por otra. 

-Se modificó varias extensiones de archivo de html a php.

-Se asume que todos los días se va a ingresar los valores de las monedas, aunque estos no cambien. 
_________________________________________
                                                       DIFICULTADES TAREA 3

Se me presentó dificultades en lo que es unir todas las partes de la tarea

__________________________________________
		EXPLICACIÓN DE LOS ARCHIVOS

Carpeta CRUD: 
Se tienen archivos para la administración de usuarios, con sus roles, monedas y asignaciones. Su función es crear usuarios, eliminar, modificar entre otros. 

CSS: 
Fuentes

IMG:
Imagenes (se agregó imagen propia)

INCLUDE: 
Header: Boostrap (diseño)
navbar: barra de navegacion de la pagina. 

SESION:
Como iniciar sesión
Como registrarse
Como validar iniciar sesión
Como validar desconectarse de la sesión

USER:
Perfil del usuario
Billetera del Usuario. 




__________________________________________
                                                   TIEMPO EN LA TAREA

Estimadores (todos medidos en horas[h]):

Ignacia Delaigue: 

Analisis del Enunciado: 1 [h]
Modifiaciones y Ajustes al Modelo: 5 [h]
Diseño de Plataforma: 5[h]
Desarrollo de Plataforma: 10[h]
Pruebas Finales: - [h]



