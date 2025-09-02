Se ha probado el programa con los archivos que se encuentran en la propia carpeta, un .zip, un .txt y un .exe
Para todos los casos se puede ver que la entropía de la fuente con símbolos vistos en forma dependiente es menor a la entropía vista con símbolos
vistos en forma independiente. Esto demuestra que la variable condicionante reduce la incertidumbre promedio, un claro ejemplo de esto es cuando
nos encontramos con un caracter "q", sabemos que es muy posible que el caracter que le siga sea una "u" por lo que entonces se reduce la sorpresa
Ocurre lo contrario con la redundancia, a mayor entropía menor será la redundancia, a menor entropía mayor será la redundancia. Esto es porque
la redundancia indica cuánta información de más contiene una fuente, en comparación con la máxima entropía que se podría tener.
Para el primer caso, se puede ver que la entropía del comprimido (7.996 bits) es muy cercana a la entropía máxima (8 bits) pero la redundancia es
menor al 1% y esto sucede porque los archivos comprimidos buscan eliminar la redundancia.
Para el txt, la entropía (3.96 bits) es cercana a la entropía máxima (4.643 bits) pero la redundancia es bastante considerable, ronda entre un 
14% y un 38%. Esto es debido a que los caracteres de un texto (en este caso en español) no aparecen con igual probabilidad, por ejemplo "e" y "a"
son muchos más probables que la "z" y "x", además de las dependencias que existen entre las letras como se vio con el ejemplo de la "q" y la "u".
Por último para el ejecutable sucede algo parecido con el txt (en este caso) debido a que es una mezcla de símbolos con alta entropía y símbolos
con baja entropía.

Se tuvo que quitar el archivo ejecutable debido a que excedia el tamaño máximo para poder subirse al repositorio.