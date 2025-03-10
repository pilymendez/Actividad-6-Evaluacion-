#Función 1
def cargar_dataset(archivo):
    import pandas as pd
    import os
    extension = os.path.splitext(archivo)[1].lower()   #Al archivo se le saca la extensión
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df =pd.read_excel(archivo)
        return(df)
    else:
            raise ValueError(f"Este formato no está soportado para esta función: {extension}")

#Función 2
#Columnas numéricas donde con método mean y constante
def sustitucion_nulos(df):
    import pandas as pd
    #Separo columnas cuantitativas y cualitativas del dataframe
    cuantitativas = df.select_dtypes(include=['float64','float','int','int64'])
    cualitativas = df.select_dtypes(include=['object', 'datetime','category'])

    #Columnas impares
    impares = cuantitativas.iloc[:, ::2]  
    pares = cuantitativas.iloc[:, 1::2]

    # Sustituyo valores nulos en columnas pares con el método mean
    pares = pares.fillna(round(pares.mean(),1))

    # Sustituyo valores nulos en columnas impares con la constante 99
    impares = impares.fillna(99)

    #Columnas cualitativas
    cualitativas = cualitativas.fillna('Este_es_un_valor_nulo')
         
     # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([pares,impares, cualitativas], axis=1)
    
    return(Datos_sin_nulos)


#Función 3
def valores_nulos(df):
    #Valores nulos por columna
    valores_nulos_cols = df.isnull().sum()
    #valores nulos por dataframe
    valores_nulos_df = df.isnull().sum().sum()

    return("Valores nulos por columna",valores_nulos_cols,
           "Valores nulos por dataframe",valores_nulos_df)

#Función 4
def rango_iqr (df):
    import pandas as pd
    import numpy as np 
    import matplotlib.pyplot as plt
    cuantitativas = df.select_dtypes(include=['float64','float','int','int64'])
    y = cuantitativas
    cualitativas = df.select_dtypes(include=['object', 'datetime','category'])

    percentile25 = y.quantile (0.25) #Q1
    percentile75 = y.quantile(0.75) #Q3
    iqr = percentile75 - percentile25

    Limite_Superior_iqr = percentile75 + 1.5 * iqr
    Limite_Inferior_iqr = percentile25 - 1.5 * iqr

    print("Limite superior permitido",Limite_Superior_iqr)
    print("Limite inferior permitido",Limite_Inferior_iqr)

    df1 = cuantitativas [(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
    df1 = df1.fillna(round(df1.mean(),1))

    df_limpios = pd.concat([cualitativas, df1], axis=1)

    return df_limpios.to_csv("Evaluacion_6.csv")
    
    


    