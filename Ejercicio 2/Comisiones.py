nombre = input("Nombre del vendedor: ") # se pregunta el vendedor
ventas = int(input("Diga sus ventas: ")) # se solicita la cantidad de venta y se setea el tipo de dato

comision = round(ventas * 13 /100,2) # se hace el calculo para el 13% por venta y a la vez se redonde con 2 decimales


print(f"Hola , {nombre} tus comisiones de este mes son {comision}")# se muestra el total de venta mas comision