# Estructuras Selectivas

## Operadores Relacionales
Se encarga de comparar o verificar relaciones entre valores (Numeros, Textos, Valores logicos:TRUE-FALSE)
Realiza una operación lógica entre 2 valores fijos, nos ayudan a tomar decisiones

**Entrada 1** <-Operador relacional-> **Entrada 2**

<table>
<tr><th>Operador</th><th>Descripción</th><th>Ejemplo</th></tr>
<tr><td> = </td><td>Igual a</td><td>5 = 5 -> TRUE</td></tr>
<tr><td> < </td><td>Menor que</td><td>3 < 5 -> TRUE</td></tr>
<tr><td> > </td><td>Mayor que</td><td>5 > 3 -> TRUE</td></tr>
<tr><td> <= </td><td>Menor o igual que</td><td>3 <= 3 -> TRUE</td></tr>
<tr><td> >= </td><td>Mayor o igual que</td><td>5 >= 3 -> TRUE</td></tr>
</table>

## Expresiones logicas
Son expresiones que al evaluarlas nos devuelven un valor logico (TRUE o FALSE)
**Expresión lógica** -> TRUE o FALSE
<table>
<tr><th>Operador</th><th>Descripción</th><th>Ejemplo</th></tr>
<tr><td> AND </td><td>Y lógico</td><td>A AND B -> TRUE</td></tr>
<tr><td> OR </td><td>O lógico</td><td>A OR B -> TRUE</td></tr>
<tr><td> NOT </td><td>Negación lógica</td><td>NOT
A -> FALSE</td></tr>
</table>

## Tablas de verdad
### Operador AND
| A     | B     | A AND B |
|-------|-------|---------|
| TRUE  | TRUE  | TRUE    |
| TRUE  | FALSE | FALSE   |
| FALSE | TRUE  | FALSE   |
| FALSE | FALSE | FALSE   |
### Operador OR
| A     | B     | A OR B  |
|-------|-------|---------|
| TRUE  | TRUE  | TRUE    | 
| TRUE  | FALSE | TRUE    |
| FALSE | TRUE  | TRUE    |
| FALSE | FALSE | FALSE   |
### Operador NOT
| A     | NOT A |
|-------|-------|
| TRUE  | FALSE |
| FALSE | TRUE  |

## Estructuras Selectivas
Nos permiten tomar decisiones en base a una condición (Expresión lógica)
### Simples
Se evalúa una condición, si es verdadera se ejecuta un bloque de instrucciones, si es falsa no se hace nada.
```SI <condición> ENTONCES
    <instrucciones si condición es verdadera>
FIN_SI
```
### Doble
Se evalúa una condición, si es verdadera se ejecuta un bloque de instrucciones, si es falsa se ejecuta otro bloque de instrucciones.
```SI <condición> ENTONCES
    <instrucciones si condición es verdadera>
SINO
    <instrucciones si condición es falsa>
FIN_SI
```
### Múltiple
Se evalúa una condición, si es verdadera se ejecuta un bloque de instrucciones, si es falsa se evalúa otra condición, y así sucesivamente.
```SI <condición1> ENTONCES
    <instrucciones si condición1 es verdadera> 
SINO_SI <condición2> ENTONCES
    <instrucciones si condición2 es verdadera>
SINO
    <instrucciones si ninguna condición es verdadera>
FIN_SI
```
### Anidada
Se pueden anidar estructuras selectivas dentro de otras estructuras selectivas.
```SI <condición1> ENTONCES
    SI <condición2> ENTONCES
        <instrucciones si condición1 y condición2 son verdaderas>
    SINO
        <instrucciones si condición1 es verdadera y condición2 es falsa>
    FIN_SI
SINO
    <instrucciones si condición1 es falsa>
FIN_SI
```
### Apiladas
Se pueden apilar estructuras selectivas una tras otra.
```SI <condición1> ENTONCES
    <instrucciones si condición1 es verdadera>
FIN_SI
SI <condición2> ENTONCES
    <instrucciones si condición2 es verdadera>
FIN_SI
SI <condición3> ENTONCES
    <instrucciones si condición3 es verdadera>
FIN_SI
```
