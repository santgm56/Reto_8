# Reto 8 - Menu Order Iterable

## Estudiante: `Santiago Gamboa Martínez`

### Ejercicio:

<details><summary>Descripción del Ejercicio</summary>

1. The menu once again....(I am running out of ideas). Well the task is quite easy, take the Menu code from Reto 3 and implement a new Class that creates and iterable with all the items in an order, it should allow looping and contain all item attributes.

</details>

## 📖 Descripción

Para este reto, modifiqué el código del `reto 3` que implementa un sistema de gestión de pedidos para un restaurante, donde los artículos del menú pueden agregarse a una orden y procesarse de manera iterativa. La tarea principal que tuve que hacer fue modificar el código original del menú (Reto 3) e implementar una nueva clase que hiciera que los elementos de un pedido fueran iterables, permitiendo recorrerlos de forma sencilla y accediendo a todos sus atributos.

## 🔄 Implementación de Iterabilidad

Para lograr que la clase `Order` sea iterable, se implementaron los métodos especiales `__iter__()` y `__next__()`. Estos métodos permiten que un objeto de `Order` pueda ser recorrido con un bucle `for`, accediendo a los elementos de manera secuencial.

### 📌 Definición en Código

```python
class Order:
    def __init__(self):
        self.items = []  # Lista que almacena los objetos de tipo MenuItem
        self._index = 0  # Índice interno para la iteración

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def __iter__(self):
        self._index = 0  # Reinicia el índice al comienzo de la iteración
        return self  # Devuelve la instancia de Order como su propio iterador

    def __next__(self):
        if self._index >= len(self.items):
            raise StopIteration  # Se detiene la iteración cuando se recorren todos los elementos
        item = self.items[self._index]  # Obtiene el elemento actual
        self._index += 1  # Avanza al siguiente índice
        return item  # Devuelve el elemento actual
```

### Explicación Paso a Paso de la Implementación

1. **Método `__iter__()`**

   - Reinicia el índice interno `_index` a `0`.
   - Retorna `self`, ya que la misma clase `Order` actuará como su propio iterador.

2. **Método `__next__()`**
   - Verifica si `_index` ha alcanzado el número total de elementos en `items`.
   - Si ya no hay más elementos, lanza `StopIteration`, lo que detiene la iteración.
   - Si hay elementos disponibles, obtiene el elemento actual basado en `_index`.
   - Incrementa `_index` en `1` para apuntar al siguiente elemento en la siguiente iteración.
   - Devuelve el elemento actual, permitiendo que el bucle `for` lo procese.

### ¿El Código Cumple Todos los Requisitos?

Sí, el código cumple con todos los requisitos del ejercicio:

- Creé una nueva clase (`Order`) que gestiona los pedidos.
- Implementé la iterabilidad con `__iter__()` y `__next__()`.
- Se pueden recorrer todos los elementos del pedido con `for item in order`.
- Cada ítem mantiene todos sus atributos (nombre, precio, descuento).
