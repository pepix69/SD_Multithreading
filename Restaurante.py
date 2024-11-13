import threading
import time
import random

# Opciones de pedidos disponibles
MENU = ["Pizza", "Hamburguesa", "Ensalada", "Pasta", "Sopa"]

# Duración estimada de preparación de cada tipo de comida (en segundos)
PREPARATION_TIMES = {
    "Pizza": 5,
    "Hamburguesa": 4,
    "Ensalada": 2,
    "Pasta": 6,
    "Sopa": 3
}

# Número de mesas y camareros
NUM_MESAS = 5
NUM_CAMAREROS = 3

# Estado de las mesas y control de los pedidos pendientes
mesas = [None] * NUM_MESAS  # Guarda el pedido actual de cada mesa
pedidos_pendientes = threading.Condition()  # Para sincronizar mesas y camareros

# Función para representar una mesa que realiza un pedido
def mesa_func(mesa_id):
    global mesas
    pedido = random.choice(MENU)  # Selecciona un pedido al azar
    print(f"Mesa {mesa_id + 1}: Pedido de {pedido}")
    
    # Coloca el pedido en la lista de mesas
    with pedidos_pendientes:
        mesas[mesa_id] = pedido
        pedidos_pendientes.notify_all()  # Notifica a los camareros de un nuevo pedido

# Función para representar a un camarero que atiende y prepara pedidos
def camarero_func(camarero_id):
    global mesas
    while True:
        pedido, mesa_id = None, None
        with pedidos_pendientes:
            # Espera hasta que haya un pedido pendiente
            while all(pedido is None for pedido in mesas):
                # Si todas las mesas están vacías, terminar el hilo
                if all(pedido is None for pedido in mesas):
                    return
                pedidos_pendientes.wait()
            
            # Busca una mesa que tenga un pedido listo para preparar
            for i in range(NUM_MESAS):
                if mesas[i] is not None:
                    pedido = mesas[i]
                    mesa_id = i
                    mesas[i] = None  # Limpia el pedido de la mesa una vez tomado
                    break
        
        if pedido is None:
            break  # Termina si no hay más pedidos
            
        # Simula el tiempo de preparación del pedido
        print(f"Camarero {camarero_id + 1}: Preparando {pedido} para la Mesa {mesa_id + 1}")
        time.sleep(PREPARATION_TIMES[pedido])
        print(f"Camarero {camarero_id + 1}: Entregando {pedido} a la Mesa {mesa_id + 1}")

# Creación de hilos para las mesas
hilos_mesas = []
for i in range(NUM_MESAS):
    hilo_mesa = threading.Thread(target=mesa_func, args=(i,))
    hilos_mesas.append(hilo_mesa)
    hilo_mesa.start()

# Creación de hilos para los camareros
hilos_camareros = []
for i in range(NUM_CAMAREROS):
    hilo_camarero = threading.Thread(target=camarero_func, args=(i,))
    hilos_camareros.append(hilo_camarero)
    hilo_camarero.start()

# Esperar a que todas las mesas hayan realizado sus pedidos
for hilo in hilos_mesas:
    hilo.join()

# Esperar a que todos los camareros hayan entregado todos los pedidos
for hilo in hilos_camareros:
    hilo.join()

print("Todos los pedidos han sido atendidos y entregados.")