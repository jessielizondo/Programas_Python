#############################################
#EXPLICACION CREADOR DE HISTOGRAMAS NORMALES#
#############################################

import numpy as np    # Importa la librería NumPy y la renombra como "np" 
import pandas as pd   # Importa la librería pandas y la renombra como "pd"


# Se definen algunas variables:
n = 100      # n = número de valores que se van a generar
media = 5    # media (loc) para la distribución normal
desv = 2     # desviación estándar (scale) para la distribución normal


# Genera 'n' valores aleatorios de una distribución normal con media=5 y desviación=2
datos = np.random.normal(size=n, loc=media, scale=desv)

# Redondea los valores generados al entero más cercano y los convierte a tipo int
datos = datos.round(0).astype(int)

# Se crea una lista vacía para guardar valores "filtrados" (podemos llamarlo trimming)
datos_trim = []

# Se recorre cada valor del array 'datos'
for i in range(len(datos)):
    # Si el valor de datos[i] cumple que:
    #  (datos[i] <= abs(media) + 2*desv) O
    #  (datos[i] >= abs(media) - 2*desv)
    # entonces se añade a datos_trim.
    #
    # En palabras: si datos[i] está dentro de un cierto rango alrededor de la media (± 2*desv)
    # se incluye en la nueva lista. (Ojo que la condición con 'or' tal como está escrita 
    # siempre va a incluir prácticamente todos los valores en la mayoría de casos, 
    # pero así está en el ejemplo.)
    if datos[i] <= abs(media) + 2*desv or datos[i] >= abs(media) - 2*desv:
        datos_trim.append(datos[i])

# Se convierte la lista filtrada 'datos_trim' a un DataFrame de pandas
datos_trim = pd.DataFrame(datos_trim)

# Se asigna el nombre 'Datos' a la columna de ese DataFrame
datos_trim.columns = ['Datos']

# Calcula la frecuencia de cada valor (conteo) agrupando por la columna 'Datos'
histograma = datos_trim.groupby('Datos').size()

# Se recorre cada valor único (índice) dentro de 'histograma'
for i in range(len(histograma)):

    # Si el índice (el valor mismo que aparece en 'Datos') es >= 0, se usa el signo "+"
    # en caso contrario se deja el signo vacío ""
    if histograma.index[i] >= 0:
        s = "+"
    else:
        s = ""

    # Se hace un print "especial" para mostrar una especie de histograma por consola:
    #   - Primero imprime el signo s ("+" o "")
    #   - Luego imprime el valor del índice (histograma.index[i])
    #   - Después se calcula un número de espacios para alinear el texto (basado en
    #     la longitud máxima de los valores del índice).
    #   - Por último, se imprime un número de asteriscos proporcional a la frecuencia
    #     de ese valor, en concreto usando: round(100 * frecuencia / total_de_datos_trim).
    #
    # El 'sep=""' en print evita que Python separe los argumentos con espacios adicionales.
    print( 
        s, # Dato que generamos que salio de una distribucion normal
        histograma.index[i], 
        ' '*(1+len(str(np.max([np.max(histograma.index), 
                               abs(np.min(histograma.index))]))) - 
                               len(str(abs(histograma.index[i])))), # Cantidad de asteriscos que depende de cuantas veces se repitio ese numero
        '*'*round(100*histograma.iloc[i]/len(datos_trim)), 
        sep = "" 
        )