#Aquí va la data a analizar y presentar luego.
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df =  pd.read_csv('/Users/genesisdenissematosrosario/Downloads/netflix-titles (1).csv', on_bad_lines='skip') 

#Punto 2
def topDirectores():
    directorCount = df.groupby('director').count().reset_index()
    directorCount = directorCount.rename(columns={'title': 'cantidadTitles'})
    directorMax = directorCount.nlargest(10, 'cantidadTitles')
    plt.figure(figsize=(14,8))
    sns.barplot(x= 'cantidadTitles', y= 'director',  data=  directorMax, palette='viridis')
    plt.title('Los 10 directores que tienen más películas/series en netflix')
    plt.xlabel('Número del título')
    plt.ylabel('Director')
    st.pyplot(plt)

#Punto 3
def comparacion():
    countTypes = df['type'].value_counts().reset_index()
    countTypes.columns = ['type', 'count']
    plt.figure(figsize=(8, 5))
    sns.barplot(x= 'type', y= 'count', data= countTypes, palette= 'pastel')
    plt.title('Comparación entre movies y tvshows')
    plt.xlabel('Tipo')
    plt.ylabel('Cantidad')
    st.pyplot(plt)

#Punto 4
def listedinTitulos():
    try:
        df =  pd.read_csv('/Users/genesisdenissematosrosario/Downloads/netflix-titles (1).csv', on_bad_lines='skip') 
        print("Archivo cargado exitosamente")
        print("Número de filas:", len(df))
        print("Columnas disponibles:", df.columns.tolist())
    except Exception as e:
        print("Error al cargar el archivo:", e)

    #Verificar y mostrar información sobre la columna listed_in
    print("\nAnálisis de géneros/clasificaciones:")
    if 'listed_in' not in df.columns:
        print("Error: La columna 'listed_in' no existe en el dataset")
    else: 
        #Mostrar algunos ejemplos de la columna
        print("Ejemplos de categorías:")
        print(df['listed_in'].head())

        #Procesar clasificaciones
        df['listed_in'] = df['listed_in'].fillna('Not Listed')  # Manejar valores nulos
        df['listed_in'] = df['listed_in'].str.split(', ')
        df_genres = df.explode('listed_in')
    
        #Contar clasificaciones
        genre_counts = df_genres['listed_in'].value_counts().reset_index()
        genre_counts.columns = ['Género', 'Cantidad']
        top_genres = genre_counts.head(5)

        #Mostrar conteos
        print("\nTop 5 géneros más comunes:")
        print(top_genres.to_string(index=False))

        plt.figure(figsize=(12, 6))
        ax = sns.barplot(x='Cantidad', y='Género', data=top_genres, palette='viridis')
        plt.title('Top 5 Géneros más Populares en Netflix', pad=20)
        plt.xlabel('Cantidad de Títulos')
        plt.ylabel('Género')

    for i, v in enumerate(top_genres['Cantidad']):
        ax.text(v, i, f' {v:,}', va='center')
    
    plt.tight_layout()
    st.pyplot(plt)

# Configuración del dashboard
st.title('Dashboard de Netflix')
st.sidebar.header('Selecciona una visualización')
option = st.sidebar.selectbox('Selecciona:', ('Directores', 'Series vs Películas', 'Clasificaciones'))

if option == 'Directores':
    topDirectores()
elif option == 'Series vs Películas':
    comparacion()
elif option == 'Listed_In titulos':
    listedinTitulos()