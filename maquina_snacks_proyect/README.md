# Máquina de Snacks 

Aplicación de consola (CLI) interactiva desarrollada en Python que simula el funcionamiento de una máquina expendedora automatizada. Permite a los usuarios comprar productos, ver el ticket de compra actual, consultar el inventario y añadir nuevos snacks.

El proyecto implementa la persistencia de datos mediante el manejo de archivos planos (`.txt`) y sigue los principios del paradigma de **Programación Orientada a Objetos (POO)**.


##  Características

- **Persistencia en Archivo:** El inventario se guarda y actualiza automáticamente en un archivo `snacks.txt`. Si el archivo no existe al iniciar, el sistema lo genera con un catálogo inicial.
- **Gestión de Inventario Dinámico:** Permite añadir nuevos productos al catálogo en tiempo real desde la consola.
- **Simulador de Carrito y Ticket:** Agrega productos a tu compra actual y genera un ticket detallado desglosando nombres, precios individuales y el cálculo automático del total.
- **Control de Identificadores:** Asignación automática y autoincremental de IDs únicos para cada snack a través de un contador estático de clase.
- **Robustez:** Control exhaustivo de excepciones para evitar que el programa se cierre ante entradas inválidas del usuario.


## Arquitectura del Proyecto

El código está estructurado de manera modular para separar las responsabilidades de los datos, la lógica de negocio y la interfaz de usuario:

- **`snack.py` (Clase Entidad):** Clase que representa el modelo de datos de un producto (ID, Nombre, Precio).
- **`servicio_snacks.py` (Capa de Datos):** Administra el inventario en memoria y controla la lectura y escritura del archivo físico `snacks.txt`.
- **`maquina_snacks.py` (Main):** Controla el bucle del programa, imprime el menú interactivo en la terminal y gestiona las interacciones y elecciones del usuario.
