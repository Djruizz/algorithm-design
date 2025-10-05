# Datos compuestos
## Listas
Secuencias ordenadas, mutables y dinamicas de datos.
Caracteristicas:
- Pueden contener datos de distintos tipos.
- Son indexadas, es decir, cada elemento tiene una posicion.
- Son mutables, es decir, se pueden modificar.
- Son mutables, es decir pueden ser alteradas despues
- Son dinamicas, es decir su tamaño puede variar a lo largo del programa
- Pueden contener elementos duplicados
- Son iterables.
### Operadores con listas
<table>
    <tr>
        <th>Función</th>
        <th>Definición</th>
    </tr>
    <tr>
        <td><kbd> mi_lista[0]</kbd></td>
        <td>Accede a un valor por su index</td>
    </tr>
    <tr>
        <td><kbd> mi_lista[0] = 1</kbd></td>
        <td>Permite modificar el valor de un elemento dado su index</td>
    </tr>
    <tr>
        <td><kbd> mi_lista.append(6)</kbd></td>
        <td>Invierte la cadena de texto</td>
    </tr>
    <tr>
        <td><kbd> mi_lista.insert(1,6)</kbd></td>
        <td>insertar un elemento en la posicion señalada</td>
    </tr>
    <tr>
        <td><kbd> mi_lista.remove(2)</kbd></td>
        <td>Elimina un elemento por su valor</td>
    </tr>
    <tr>
        <td><kbd> mi_lista.pop(0) </kbd></td>
        <td>Elimina un elemento por su index</td>
    </tr>
    <tr>
        <td><kbd> len(mi_lista)</kbd></td>
        <td>Muestra el tamaño de la lista</td>
    </tr>
    <tr>
        <td><kbd> max(mi_lista) </kbd></td>
        <td>Muestra el elemento mas grande de una lista</td>
    </tr>
    <tr>
        <td><kbd> min(mi_lista) </kbd></td>
        <td>Muestra el elemento mas pequeño de una lista</td>
    </tr>
    <tr>
        <td><kbd> sum(mi_lista) </kbd></td>
        <td>Suma todos los valores de la lista</td>
    </tr>
    <tr>
        <td><kbd> mi_lista.sort() </kbd></td>
        <td>Ordena la misma lista sin crear un duplicado</td>
    </tr>
    <tr>
        <td><kbd> sorted(mi_lista) </kbd></td>
        <td>Crea un duplicado de la lista pero ordenado</td>
    </tr>
    <tr>
        <td><kbd> reversed(mi_lista) </kbd></td>
        <td>Invierte el orden de una lista</td>
    </tr>
    <tr>
        <td><kbd> mi_lista + [2,3] </kbd></td>
        <td>Junta el contenido de 2 listas</td>
    </tr>
    <tr>
        <td><kbd> 3 in lista = True </kbd></td>
        <td>Comprueba que un elemento exista dentro de la lista</td>
    </tr>
</table>