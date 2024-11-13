# SD_Multithreading

##### Integrantes:
1. Giovanna Inosuli Campos Flores
2. Yavé Emmanuel Vargas Márquez
3. Martha Dalila Cardona Serna
4. José Refugio Salinas Uribe
5. José Ángel Montoya Zúñiga 
6. Rodrigo Olmos Gómez 
 
### Descripción
Este proyecto es una simulación de un restaurante utilizando multithreading en Python. El objetivo es demostrar el uso de hilos concurrentes para manejar múltiples mesas y camareros que procesan y preparan pedidos al mismo tiempo.


### Funcionamiento 
#### Mesas:

Cada mesa es un hilo que representa un cliente realizando un pedido al azar del menú disponible.


#### Camareros:

Los camareros son hilos que atienden y preparan los pedidos.
Usan un mecanismo de condición (Condition) para esperar y detectar cuando hay un nuevo pedido pendiente.
Una vez que un pedido es tomado, el camarero simula la preparación del pedido utilizando time.sleep() y, después de completarlo, entrega el pedido a la mesa correspondiente.


#### Sincronización:

El programa utiliza threading.Condition para sincronizar los pedidos entre mesas y camareros, evitando condiciones de carrera y garantizando la correcta entrega de pedidos.

### Estructura del Programa
El restaurante tiene 5 mesas y 3 camareros.
Cada mesa realiza un pedido de comida de forma aleatoria.
Los camareros atienden a las mesas y preparan los pedidos concurrentemente.
Se muestra el estado actual de cada pedido, desde su solicitud hasta su entrega.


### Menú y Tiempos de Preparación
Las opciones del menú y sus tiempos de preparación (en segundos) son:
1. Pizza: 5 segundos
2. Hamburguesa: 4 segundos
3. Ensalada: 2 segundos
4. Pasta: 6 segundos
5. Sopa: 3 segundos

### Prueba
![image](https://github.com/user-attachments/assets/e2eb2c6e-3608-4f2f-a4ca-29d660e98e03)
