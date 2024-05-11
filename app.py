""" 
Following the course of Zero 2 Hero
Construction of the API STORE

We are going to use this API to:

1. Manage inventory
2. Manage sales
3. Strategic analysis

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Product:
    def __init__(self,inputs):
        self.name = inputs['name']
        self.units = inputs['units']
        self.adq_cost = inputs['adq_cost']
        self.sell_price = inputs['sell_price']
    
    def adquire(self,x):
        self.units = self.units + x
    
    def sell(self,x):
        remain = self.units -x 
        if remain >= 0:
            self.units =- x
            return x
        else:
            print("Not sufficient to fullfil sell")
            return self.units
            self.units = 0
    
    def change_adq_cost(self,x):
        self.adq_cost = x
    
    def chage_sell_price(self,x):
        self.sell_price = x 
        

properties = {
    'name': 'Sabritas',
    'units': 1,
    'adq_cost': 5,
    'sell_price': 20
}

sabritas = Product(properties)
print(f"nombre: {sabritas.name}, unidades:{sabritas.units}, costo: {sabritas.adq_cost}, precio venta: {sabritas.sell_price}")
print("")
sabritas.adquire(100)
print(f"nombre: {sabritas.name}, unidades:{sabritas.units}, costo: {sabritas.adq_cost}, precio venta: {sabritas.sell_price}")
print("")
