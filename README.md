# Django-Gym-Admin
Proyecto realizado en Django para la administracion de los clientes de un gimnasio.

##
Se utilizo herencia de HTML desde core. Todos los modelos tienen un formulario para cargar datos en la DB y un buscador segun nombre.
El proyecto tiene home con un menu para navegar por los 3 models.
Al ingresar en Clientes o Entrenadores, hay un menu adicional para elegir Ver o Crear.

### Clientes:


- Buscar: `clientes/cliente/list`
- Crear: `clientes/cliente/create`


### Entrenadores:

- Buscar: `entrenadores/entrenador/list`
- Crear: `entrenadores/entrenador/create`


### Clases no posee un menu individual. Se accede directo a ver el listado de las clases o a crearlas.

- Buscar: `entrenadores/clase/list`

- Crear: `entrenadores/clase/create`