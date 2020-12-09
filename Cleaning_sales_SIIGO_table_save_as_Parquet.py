# -*- coding: utf-8 -*-
"""
Cleaning sales SIIGO.xlsx and save as parquet data
"""

import pandas as pd
import numpy as np

#Read xlsx SIIGO file
path_file = 'Venta Acumulada x Vendedores SIIGO.xlsx'
vent1 = pd.read_excel(path_file, sheet_name='DATOS134733')

#Date recognition
day = list(vent1.columns.values)[15]
day = day.replace('/','_')

#Cleaning Schema 
vent1=vent1.loc[6:,:]
vent1.columns = ['ZONA','VENDED','CIUDAD', 'NOMBRE','LINEA-NOMBRE','LINIEA','DESCRIPCION_1','GRUPO-NOMBRE','GRUPO','DESCRIPCION_2','PRODUCTO','REFERENCIA','DESCRIPCION','MARCA','CANTIDAD','VALOR']
vent1 = vent1.reset_index()
vent1 = vent1.drop(['index'] , axis=1)

#Cleaning Tables
vent1['CIUDAD'] = vent1['CIUDAD'].str.replace(" ","")
vent1['NOMBRE'] = vent1['NOMBRE'].str.replace(" ","")
vent1['LINEA-NOMBRE'] = vent1['LINEA-NOMBRE'].str.replace(" ","")
vent1['GRUPO-NOMBRE'] = vent1['GRUPO-NOMBRE'].str.replace(" ","")
vent1['DESCRIPCION_1'] = vent1['DESCRIPCION_1'].str.replace(" ","")
vent1['DESCRIPCION_2'] = vent1['DESCRIPCION_2'].str.replace(" ","")
vent1['REFERENCIA'] = vent1['REFERENCIA'].str.replace(" ","")

#Save Data as Parquet in Raw Zone of Data Lake
vent1.to_parquet(r'C:\Users\Juan Carlos Rivera C\Documents\Data_Lake\Raw\{}_SALES_SIIGO.parquet'.format(day))