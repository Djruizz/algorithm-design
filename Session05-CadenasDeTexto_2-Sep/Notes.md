# Cadenas de Texto}

## Buscar en cadenas
<table>
    <tr>
        <th>Función</th>
        <th>Definición</th>
    </tr>
    <tr>
        <td><kbd> string[0] </kbd></td>
        <td>Consulta una posicion en una cadena de texto</td>
    </tr>
    <tr>
        <td><kbd> string[start:stop:step] </kbd></td>
        <td>Permite seleccionar una subcadena en especifico, con un punto de origen y final</td>
    </tr>
    <tr>
        <td><kbd> string[::-1] </kbd></td>
        <td>Invierte la cadena de texto</td>
    </tr>
</table>

## Manejo básico de cadenas
<table>
    <tr>
        <th>Función</th>
        <th>Definición</th>
    </tr>
    <tr>
        <td><kbd> len(s) </kbd></td>
        <td>Retorna el tamaño de la palabra</td>
    </tr>
    <tr>
        <td><kbd> max(s) </kbd></td>
        <td>Retorna el caracter de mayor valor ascii en la palabra</td>
    </tr>
    <tr>
        <td><kbd> min(s) </kbd></td>
        <td>Retorna el caracter de menor valor ascii en la palabra</td>
    </tr>
    <tr>
        <td><kbd> sorted(s) </kbd></td>
        <td>Crea una lista de caracteres, ordenada por los valores ascii</td>
    </tr>
    <tr>
        <td><kbd> reversed(s) </kbd></td>
        <td>Crea una lista de caracteres invertidos</td>
    </tr>
    <tr>
        <td><kbd> s.upper() </kbd></td>
        <td>Tranforma el texto a mayusculas</td>
    </tr>
    <tr>
        <td><kbd> s.lower() </kbd></td>
        <td>Tranforma el texto a minusculas</td>
    </tr>
    <tr>
        <td><kbd> s.capitalize() </kbd></td>
        <td>Tranforma la primera letra del texto a mayusculas y el resto a minusculas</td>
    </tr>
    <tr>
        <td><kbd> s.strip() </kbd></td>
        <td>Elimina los espacios en blanco al inicio y final del texto</td>
    </tr>
    <tr>
        <td><kbd> s.lstrip() </kbd></td>
        <td>Elimina los espacios en blanco al inicio del texto</td>
    </tr>
    <tr>
        <td><kbd> s.rstrip() </kbd></td>
        <td>Elimina los espacios en blanco al final del texto</td>
    </tr>
</table>

## Evaluando cadenas
<table>
    <tr>
        <th>Función</th>
        <th>Definición</th>
    </tr>
    <tr>
        <td><kbd> s.isalnum() </kbd></td>
        <td>Es alfanumérico (letras y números) y tiene al menos un carácter</td>
    </tr>
    <tr>
        <td><kbd> s.isaplha() </kbd></td>
        <td>Es alfabético (letras, números, caracteres) y tiene al menos un caracter</td>
    </tr>
    <tr>
        <td><kbd> s.isdigit() </kbd></td>
        <td>Es solo numérico y tiene al menos un carácter</td>
    </tr>
    <tr>
        <td><kbd> s.islower() </kbd></td>
        <td>Es un texto en minúsculas y tiene al menos un caracter</td>
    </tr>
    <tr>
        <td><kbd> s.isupper() </kbd></td>
        <td>Es un texto en mayusculas y tiene al menos un caracter</td>
    </tr>
</table>

## Buscar subcadenas
<table>
    <tr>
        <th>Función</th>
        <th>Definición</th>
    </tr>
    <tr>
        <td><kbd> s.endswith(z) </kbd></td>
        <td>Verifica si el texto termina con la subcadena</td>
    </tr>
    <tr>
        <td><kbd> s.startswith(z) </kbd></td>
        <td>Verifica si el texto inicia con la subcadena</td>
    </tr>
    <tr>
        <td><kbd> s.find(z) </kbd></td>
        <td>Retorna el indice de la primera aparicion de la subcadena</td>
    </tr>
    <tr>
        <td><kbd> s.rfind(z) </kbd></td>
        <td>Retoma el indice de la ultima aparición de la subcadena</td>
    </tr>
    <tr>
        <td><kbd> s.count(z) </kbd></td>
        <td>Retoma la cantidad de ocurrencias de la subcadena</td>
    </tr>
</table>

## Separar cadenas de listas
<table>
    <tr>
        <th>Función</th>
        <th>Definición</th>
    </tr>
    <tr>
        <td><kbd>split()</kbd></td>
        <td>VSepara untexto usando un caracter separador como delimitador para "partir" la cadena de una lista</td>
    </tr>
</table>