import pandas as pd
import os
import db
import requests
import controller as ctr

message="""
    1)Insertar data:
    2)Actualizar data del dolar
"""
print(message)
option=int(input('ingrese la tarea a realizar: '))

def insertarData():
    compra=input('ingrese el siguiente data compra: ')
    venta=input('ingrese el siguiente data venta: ')
    moneda=input('ingrese el siguiente data moneda: ')
    fecha=datetime.datetime.now()
    data=(compra,venta,moneda,fecha)
    try:
        ctr.insertTipo(data)
    except Exception as e:
         print("error al ingresar data")
         print(e)

def listTipo():
    print("Lista")
    data=ctr.controllerTipo()
    for row in data:
        print(row)

if __name__=='__main__':
    if option=='1':
        insertarData()
        listTipo()

def actualizarTipo():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    data = rq.get(url)
    if data.status_code==200:
        print(data.json())
        data=data.json()
        dolar_compra = data['compra']
        dolar_venta = data['venta']
        dolar_moneda=data['moneda']
        fecha_actualizacion=datetime.datetime.now()
        data=(dolar_compra,dolar_venta,dolar_moneda,fecha_actualizacion)
        try:
            ctr.insertTipo(data)
        except Exception as e:
            print("error al ingresar data")
            print(e)
    else:
        print("error de api")

    if __name__ == '__main__':
        if option == '2':
            insertarData()
            listTipo()

