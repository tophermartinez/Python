
mi_texto = "Esta es una prueba"

resultado = mi_texto[2] #busca la letra en el indice 2

print(resultado)

resultado = mi_texto.index(-5) #busca la letra en el indice -5
resultado = mi_texto.index(5)# busca la letra en el indice 5
resultado = mi_texto.index("prueba") #busca la palabra prueba y devulelve donde inicia
resultado = mi_texto.index("a") #busca la letra a y devulelve donde inicia
resultado = mi_texto.index("a",5) #busca la letra a desde el indice 5 en adelantey devulelve donde inicia
resultado = mi_texto.index("a",5,10) #busca la letra a desde el indice 5 hasta el 10 devulelve donde inicia
resultado = mi_texto.rindex("a") #busca desde derecha a izquierda y devuelve el indice

print(resultado)
