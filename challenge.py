#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

__author__ = "Agustin Palau"
__version__ = "1.0.1"
__email__ = "apalau@frd.utn.edu.ar"
__status__ = "Challenge Test"

# Se importan los paquetes a utilizar
import pyRofex
import sys

if len(sys.argv) == 6:
    if sys.argv[2] == "-u" and sys.argv[4] == "-p":
        symbol = str(sys.argv[1])
        user = str(sys.argv[3])
        password = str(sys.argv[5])
        try:
            print("---------------------------")
            print("Iniciando sesion en Remarkets")
            pyRofex.initialize(
                user = user,
                password = password,
                account = "REM5130",
                environment = pyRofex.Environment.REMARKET
            )
            print("Consultando simbolo")
            md = pyRofex.get_market_data(
                ticker = symbol,
                entries = [
                    pyRofex.MarketDataEntry.BIDS,
                    pyRofex.MarketDataEntry.LAST
                ]
            )
            
        except Exception as e: 
            print(f"Ha ocurrido un error => {type(e).__name__}: {e}")
        try:
            if md['status'] == 'OK':
                la = md['marketData']['LA']['price']
                print(f"Ultimo precio operado: {la}")
                print("Consultando BID")
                bid = md['marketData']['BI'][0]['price']
                if bid:
                    print(f"Precio de BID: {bid}")
                    price = bid - 0.01
                    price = round(price, 2)
                    print(f"ingresando orden a {price}")
                else:
                    price = 72.25
                    print(f"No hay BIDs activos")
                    print(f"ingresando orden a {price}")
                order = pyRofex.send_order(
                    ticker = symbol,
                    side = pyRofex.Side.BUY,
                    size = 10,
                    price = price,
                    order_type = pyRofex.OrderType.LIMIT
                )
                print("Cerrando sesion en Remarkets")
                print("---------------------------")
            else:
                print("Simbolo invalido")
                print("Cerrando sesion")
                print("---------------------------")
        except:
            print("Ha ocurrido un error, intente nuevamente en otro rango horario")
            print("Cerrando sesion")
            print("---------------------------")
    else:
        print("Error de parametros")
else:
    print("Error: verifique que los parametros ingresados sean los correctos")

