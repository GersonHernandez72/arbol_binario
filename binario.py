class Nodo:
    """Clase que representa un nodo del árbol binario."""
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    """Clase que representa un árbol binario."""
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        """Inserta un nuevo valor en el árbol binario."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        """Método auxiliar recursivo para insertar un valor."""
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:  # No se permiten duplicados
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)

    def recorrido_inorden(self):
        """Devuelve una lista con el recorrido en inorden del árbol."""
        resultado = []
        self._recorrido_inorden_recursivo(self.raiz, resultado)
        return resultado

    def _recorrido_inorden_recursivo(self, nodo_actual, resultado):
        if nodo_actual:
            self._recorrido_inorden_recursivo(nodo_actual.izquierdo, resultado)
            resultado.append(nodo_actual.valor)
            self._recorrido_inorden_recursivo(nodo_actual.derecho, resultado)

    def recorrido_preorden(self):
        """Devuelve una lista con el recorrido en preorden del árbol."""
        resultado = []
        self._recorrido_preorden_recursivo(self.raiz, resultado)
        return resultado

    def _recorrido_preorden_recursivo(self, nodo_actual, resultado):
        if nodo_actual:
            resultado.append(nodo_actual.valor)
            self._recorrido_preorden_recursivo(nodo_actual.izquierdo, resultado)
            self._recorrido_preorden_recursivo(nodo_actual.derecho, resultado)

    def recorrido_postorden(self):
        """Devuelve una lista con el recorrido en postorden del árbol."""
        resultado = []
        self._recorrido_postorden_recursivo(self.raiz, resultado)
        return resultado

    def _recorrido_postorden_recursivo(self, nodo_actual, resultado):
        if nodo_actual:
            self._recorrido_postorden_recursivo(nodo_actual.izquierdo, resultado)
            self._recorrido_postorden_recursivo(nodo_actual.derecho, resultado)
            resultado.append(nodo_actual.valor)

    def buscar(self, valor):
        """Busca un valor en el árbol y devuelve True si existe."""
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, valor)

    def eliminar(self, valor):
        """Elimina un valor del árbol si existe."""
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return nodo_actual
        if valor < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar_recursivo(nodo_actual.derecho, valor)
        else:
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            elif nodo_actual.derecho is None:
                return nodo_actual.izquierdo
            nodo_sucesor = self._minimo_valor(nodo_actual.derecho)
            nodo_actual.valor = nodo_sucesor.valor
            nodo_actual.derecho = self._eliminar_recursivo(nodo_actual.derecho, nodo_sucesor.valor)
        return nodo_actual

    def _minimo_valor(self, nodo):
        """Encuentra el nodo con el valor más bajo en un subárbol."""
        while nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo


# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolBinario()
    elementos = [50, 30, 70, 20, 40, 60, 80, 90]

    # Insertar elementos en el árbol
    for elemento in elementos:
        arbol.insertar(elemento)

    # Mostrar recorridos
    print("Recorrido inorden:", arbol.recorrido_inorden())
    print("Recorrido preorden:", arbol.recorrido_preorden())
    print("Recorrido postorden:", arbol.recorrido_postorden())

    # Buscar elementos
    print("¿El 10 está en el árbol?", arbol.buscar(10))
    print("¿El 90 está en el árbol?", arbol.buscar(90))

    # Eliminar un elemento
    arbol.eliminar(60)
    print("Recorrido inorden después de eliminar 60:", arbol.recorrido_inorden())
