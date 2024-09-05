
# Descripción del proyecto.

Este proyecto se centra en limpiar y analizar un conjunto de datos desordenado sobre ataques de tiburones utilizando técnicas de manipulación de datos (Data Wrangling) en Python. El objetivo final es preparar el conjunto de datos para un análisis exploratorio y responder a hipótesis específicas sobre los patrones y tendencias en los ataques de tiburones. La limpieza incluye la eliminación de valores nulos, duplicados, manipulación de strings, y más.


# Hipótesis.
Durante el proyecto, formulamos las siguientes hipótesis para guiar nuestro proceso de análisis:

Los ataques de tiburones ocurren con mayor frecuencia en ciertas ubicaciones geográficas.
Los tiburones atacan más a personas que realizan actividades acuáticas como el surf.
Los ataques de tiburones son más comunes en hombres que en mujeres.


# Estructura del proyecto.
El proyecto se dividió en las siguientes fases:
- Análisis inicial del dataset:
  - Cargar el dataset en Python y revisar su estructura.
  - Identificar problemas como valores nulos, datos duplicados, y la necesidad de formatear   
    columnas.
 
- Limpieza de datos: Aplicar al menos cinco técnicas de limpieza de datos.
  - Eliminación de valores nulos y duplicados.
  - Formateo de strings para asegurar la coherencia.
  - Estandarización de las columnas para facilitar el análisis.
  - Aplicación de expresiones regulares (Regex) para la extracción de información relevante.
  - Revisión y manipulación de columnas que contienen fechas.
 
- Análisis Exploratorio de Datos (EDA):
  - Realizamos un análisis exploratorio para validar las hipótesis utilizando técnicas de agregación y visualización de datos en distintos gráficos.

- Presentación de resultados:
  - Los resultados fueron presentados a través de una narrativa clara que destaca los hallazgos más relevantes y visualizaciones que ilustran las tendencias identificadas.

# Estructura de archivos:
- main.ipynb: Cuaderno de Jupyter con todo el código de limpieza y análisis.
- clean.py: Archivo Python que contiene funciones reutilizables para la limpieza de datos.
- data/: Carpeta que contiene el dataset original y el dataset limpio.
- show_top: Carpeta que contiene las visualizaciones generadas durante el EDA.
- README.md: Documentación del proyecto.

# Tecnologías utilizadas.
- Lenguaje de programación: Python
- Librerías principales: 
  - pandas: Para manipulación y limpieza de datos.
  - matplotlib y seaborn: Para la creación de visualizaciones.

# Resultados.
- Hipótesis 1: Confirmada. Los ataques de tiburones son más frecuentes en zonas costeras de Estados Unidos de America, Australia y Sudáfrica.
- Hipótesis 2: Confirmada a medias. Las personas que practican surf tienen una mayor probabilidad de sufrir un ataque de tiburón. En cambio, no hemos podido confirmar la hipótesis de que las personas que 
  practican buceo tengan más probabilidades.
- Hipótesis 3: Confirmada. Los ataques de tiburones muestran una tendencia clara hacia personas del sexo masculino. 
  
# Conclusiones.
El análisis de los datos de ataques de tiburones permitió identificar patrones importantes que pueden ser útiles para empresas que venden experiencias acuáticas, como tours de buceo o clases de surf. 

# Equipo.
Este proyecto fue realizado por: 
- Alejandro Alegre 
- Haridian Lugo Morays 
- José Miguel Sánchez
- Hugo Ortuño Suárez


