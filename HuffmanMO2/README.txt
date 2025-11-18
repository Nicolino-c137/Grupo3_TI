---------------EXPLICACIÓN DEL ALGORITMO DE HUFFMAN MARKOVIANO DE ORDEN 2---------------
Este algoritmo es una variante del algoritmo de Huffman original, en este se tiene en cuenta dependencias entre símbolos modelando la fuente como un proceso de Markov de orden 2.
Es decir que, en lugar de codificar cada símbolo por separado, la codificación se adapta al contexto formado por los dos símbolos anteriores. En otras palabras, la probabilidad del símbolo 
actual depende de los dos símbolos previos. A partir de esto, se construye un árbol de Huffman diferente para cada contexto posible.
1° Se identifica todos los contextos posibles, cada contexto es un par (a,b)
2° Para cada contexto se calculan las frecuencias de los símbolos que pueden seguir a ese contexto. A partir de estas frecuencias se construye el árbol de Huffman, se ordenan las frecuencias
de mayor a menor y de forma iterativa se toman los dos símbolos menos frecuentes para formar un árbol mayor, que en la rama izquierda de este tiene un símbolo y en la rama derecha otro símbolo.
La rama izquierda tendrá como etiqueta un cero, mientras que la derecha un uno.
Esto se repite por la cantidad de contextos que hay en total.
3° Codificación: los dos primeros símbolos se transmiten usando un método fijo, por lo general se utiliza un pseudo ASCII. Luego se parte del estado actual y se codifica la transición del contexto
al símbolo que le sigue, esto es teniendo el cuenta los árboles de Huffman obtenidos anteriormente. Se avanza un caracter y se repite el proceso hasta terminar de recorrer toda la fuente.
4° Decodificación: Debido a que los dos primeros símbolos están codificados en pseudo ASCII se tiene en cuenta la longitud de dicho código, luego se busca a que símbolos corresponde y obtenemos la 
decodificación de los dos primeros símbolos. Al tener esto sabremos que árbol de Huffman utilizar ya que tenemos conocimiento sobre el contexto. Se consumen tanto bits según la altura del árbol.
El nodo hoja será el símbolo que representa la codificación.
NOTA: debido a que la cadena de la fuente se repite sistemáticamente, el primer símbolo de la cadena será el consecuente de los últimos dos símbolos de la fuente.

---------------EXPLICACIÓN DEL CÓDIGO---------------
En el archivo prueba.txt se debe de colocar la cadena a codificar, luego se invocará una función llamada compresor. En esta lo primero que sucede es la identificación de los contextos y el conteo de
las frecuencias de los símbolos consecuentes. Luego se construyen los árboles de Huffman para cada contexto y a su vez se crea un diccionario que contendrá los códigos pseudo ASCII de cada contexto.
Realizado este preprocesamiento se procede con la compresión según el 3° paso del algoritmo de Huffman Markoviano de orden 2. Con los bits obtenidos se los convierte en bytes para así generar el archivo 
comprimido.bin, mientras que en un archivo a parte cabecera.json se guardan los árboles de cada contexto y los códigos pseudo ASCII.
Obtenido esto se invoca la función descomprimir. En esta básicamente lo que sucede es que se lee el archivo cabecera.json y el contenido del archivo comprimido.bin, donde luego los bytes se transforman 
en una cadena de bits. Se recupera el contexto inicial y a partir de este se procede con la decodificación donde el resultado se guarda en un archivo descomprimido.txt

---------------FORMA DE USAR EL COMPRESOR/DESCOMPRESOR---------------
1° En el archivo prueba.txt colocar la cadena que se desea comprimir
2° Ejecutar el archivo main.py
3° Si se desea verificar que la compresión/descompresión realmente funciona se puede comparar el contenido del archivo prueba.txt con el contenido descomprimido.txt. También es posible ver cuanto se ha 
comprimido buscando el archivo comprimido.bin, click derecho en el, propiedades y se puede ver el tamaño en disco del mismo. De forma análoga para el archivo prueba.txt
