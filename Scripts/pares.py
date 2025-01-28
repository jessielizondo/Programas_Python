#################################
#CREADOR DE HISTOGRAMAS NORMALES#
#################################

import numpy as np 
import pandas as pd 

# Definir variables
n = 100 
media = 5 
desv = 2 

# Generar numeros aleatorios que sigan una distribucion normal
datos = np.random.normal(size = n, loc = media, scale = desv) 

# Transformar los números aleatorios generados en enteros
datos = datos.round(0).astype(int) 

# Quitar colas de distribucion (valores atipicos)
datos_trim = [] 
for i in range(len(datos)): 
  if datos[i] <= abs(media) + 2*desv or datos[i] >= abs(media) - 2*desv: 
    datos_trim.append(datos[i]) 

# Construir dataframe
datos_trim = pd.DataFrame(datos_trim) 
datos_trim.columns = ['Datos'] 

# Conteo (frecuencia) de cada uno de los datos
histograma = datos_trim.groupby('Datos').size() 

# Asignar "+" si cada dato generado es positivo
for i in range(len(histograma)): 
  if histograma.index[i]>=0: 
    s = "+" 
  else: 
    s = "" 
  # Imprimir cada dato generado, un espacio, y luego la cantidad de asteriscos que depende de la proporcion de veces que se observo ese dato
  print( 
    s, # Dato que generamos que salio de una distribucion normal
    histograma.index[i], 
    ' '*(1+len(str(np.max([np.max(histograma.index), 
                           abs(np.min(histograma.index))]))) - 
                           len(str(abs(histograma.index[i])))), # Cantidad de asteriscos que depende de cuantas veces se repitio ese numero
    '*'*round(100*histograma.iloc[i]/len(datos_trim)), 
    sep = "" 
    )
