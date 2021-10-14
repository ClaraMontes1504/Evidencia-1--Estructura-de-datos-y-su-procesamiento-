#EVIDENCIA 1
from collections import namedtuple
import datetime
import pandas as pd


Ventas = namedtuple("Ventas", ("fecha", "descripcion","cantidad","precio","total"))
lista_ventas = []

DiccionarioVentas = {}



SEPARADOR = ("*" * 20) + "\n"

while True:
    
    
    print("\nMENÚ")
    print("1) Agregar venta")
    print("2) Busqueda especifica")
    print("3) Salir")
    
    respuesta = int(input("Elija una opción: "))
    
    if respuesta == 3:
        print("Gracias por su compra, buen día")
        break
    
    if respuesta == 1:
            lista_ventas = []
            while True:
                folio = int(input('\nIngrese el folio: '))
                if folio in DiccionarioVentas.keys():
                    print('Este folio ya existe, porfavor ingresa otro')
                else:
                    break
            while True:
                diccionario_compras= {}
                agregarArticulo =1
                while agregarArticulo==1:
                    fecha = datetime.date.today()
                    descripcion= input('Introduce un articulo: ')
                    precio=float(input('Introduce el precio del articulo: '))
                    cantidad = float(input('Introduce la cantidad: '))
                    total = precio * cantidad
                    diccionario_compras[descripcion]=total
                    # Lista
                    venta = Ventas(fecha, descripcion,cantidad,precio,total) 
                    lista_ventas.append(venta)
                    
                    # DiccionarioVentas
                    DiccionarioVentas[folio] = lista_ventas

                    agregarArticulo=int(input('¿Desea añadir más articulos? \n1)Si \n2)No: '))
                    
                break
                         
    
    elif respuesta == 2:
        busqueda = int(input("Ingresa la folio a buscar: "))
        #df_diccionario_ventas = pd.DataFrame(diccionario_ventas)
        df_DiccionarioVentas = pd.DataFrame(DiccionarioVentas[busqueda])
        print(df_DiccionarioVentas)
                    
        sumtotal = df_DiccionarioVentas["total"].sum()
        iva = sumtotal * .16
        totaliva = sumtotal + iva
        print(SEPARADOR)
        print(f"Total : ${sumtotal}")
        print(f"Total + IVA : ${totaliva}")
        
        
        
        
        
        
        
        