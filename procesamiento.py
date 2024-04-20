import pandas as pd

def limpiar_columnas(df):
    # Renombrar columnas eliminando espacios y tildes, y convirtiendo a minúsculas
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    
    # Eliminar columnas repetidas
    df.drop(columns=['id', 'tipomoneda'], inplace=True)
    
    # Eliminar coma de la columna 'dispositivo_legal'
    df['dispositivo_legal'] = df['dispositivo_legal'].replace({',': ''}, regex=True)
    
    return df

def dolarizar_montos(df):
    # Utilizar API de sunat para obtener valor actual del dólar
    # Supongamos que obtenemos el valor del dólar y lo almacenamos en una variable llamada 'valor_dolar'
    valor_dolar = 3.75  # Este valor es solo un ejemplo
    
    # Dolarizar montos de inversión y transferencia
    df['monto_inversion_dolarizado'] = df['monto_inversion'] / valor_dolar
    df['monto_transferencia_dolarizado'] = df['monto_transferencia'] / valor_dolar
    
    return df

def puntuar_estado(df):
    # Cambiar valores de la columna 'estado'
    df['estado'] = df['estado'].map({'Actos Previos': 1, 'Resuelto': 0, 'Ejecucion': 2, 'Concluido': 3})
    
    return df

def generar_reporte_ubigeos(df):
    # Eliminar duplicados y almacenar en base de datos
    ubigeos_df = df[['ubigeo', 'region', 'provincia', 'distrito']].drop_duplicates()
    # Guardar en la base de datos
    
def generar_reporte_top5_costo_urbanas(df):
    # Generar reporte para cada región
    regiones = df['region'].unique()
    for region in regiones:
        region_df = df[(df['region'] == region) & (df['tipo'] == 'Urbano')]

        if not region_df.empty:
            top5_df = region_df.sort_values(by='costo_inversion', ascending=False).head(5)
            # Guardar top5_df en un archivo Excel con el nombre de la región

# Aquí podríamos llamar a las funciones anteriores y cargar el archivo 'reactiva.xlsx'
# Por ejemplo:
# df = pd.read_excel('./data/reactiva.xlsx')
# df = limpiar_columnas(df)
# df = dolarizar_montos(df)
# df = puntuar_estado(df)
# generar_reporte_ubigeos(df)
# generar_reporte_top5_costo_urbanas(df)
