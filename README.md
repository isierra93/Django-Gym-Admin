# Django-Gym-Admin
Proyecto realizado en Django para la administracion de los clientes de un gimnasio.

##
Se utilizo herencia de HTML desde core. Todos los modelos tienen un formulario para cargar datos en la DB y un buscador segun nombre.
El proyecto tiene home con un menu para navegar por los 3 models.
Al ingresar en Clientes o Entrenadores, hay un menu adicional para elegir Ver o Crear.

### Clientes:


- Listar: `clientes/cliente/list`
- Crear: `clientes/cliente/create`
- Borrar: `clientes/cliente/delete/<int:pk>`
- Actualizar: `clientes/cliente/update/<int:pk>`


### Entrenadores:

- Listar: `entrenadores/entrenador/list`
- Crear: `entrenadores/entrenador/create`
- Borrar: `entrenadores/entrenador/delete/<int:pk>`
- Actualizar: `entrenadores/entrenador/update/<int:pk>`

### Clases no posee un menu individual. Se accede directo a ver el listado de las clases o a crearlas.

- Listar: `entrenadores/clase/list`
- Crear: `entrenadores/clase/create`
- Borrar: `entrenadores/clase/delete/<int:pk>`
- Actualizar: `entrenadores/clase/update/<int:pk>`

## Futuras mejoras:

VAN ACAAAAAAAA

Autor:
Nombre: Ivan Sierra
Comision: 57830
LinkedIn: https://www.linkedin.com/in/isierra93/
