# 📊 Análisis del Rendimiento de Jugadores de la NBA

**Proyecto de Business Intelligence sobre la temporada 2023/2024**

## 📁 Contenido del repositorio

-   **/api_extraccion/** → Script en Python para obtener los datos desde
    la API.\
-   **/powerbi/** → Archivo `.pbix` del dashboard completo.\
-   **README.md** → Documentación del proyecto.

## 🏀 Introducción

En la era del dato, el análisis cuantitativo es esencial para la toma de
decisiones. Este proyecto desarrolla una aplicación de Business
Intelligence en Power BI, basada en datos reales extraídos de la API
pública api-nba, con el objetivo de crear una herramienta visual,
comprensible e interactiva.

## 🎯 Objetivos

### ✔️ Objetivo general

Crear un dashboard en Power BI para analizar el rendimiento de jugadores
de la NBA durante la temporada 2023/2024.

### ✔️ Objetivos específicos

-   Extraer estadísticas mediante Python y la API api-nba.\
-   Limpiar, transformar y modelar datos.\
-   Crear modelo estrella.\
-   Diseñar visualizaciones útiles y comparativas.

## 🛠️ Metodología

### 1️⃣ Extracción de datos

Script Python que genera un CSV con estadísticas por jugador.

### 2️⃣ Transformación en Power BI

Renombrado, normalización y creación de columnas como Condición y Rival.

### 3️⃣ Modelado de datos

Modelo estrella con tabla de hechos y dimensiones.

### 4️⃣ Visualizaciones

-   Puntos totales\
-   Media de puntos\
-   Rendimiento frente a rivales\
-   Porcentaje de tiro\
-   Evolución de puntos\
-   Comparación local vs visitante

## 📈 Resultados

El dashboard permite analizar rendimiento individual, comparaciones y
tendencias.

## 🔍 Evaluación crítica

### ✔️ Puntos fuertes

Modelo sólido, visualizaciones claras y métricas personalizadas.

### ⚠️ Limitaciones

API limitada, análisis de una sola temporada y valores nulos.

## 🧭 Conclusiones

Proyecto que demuestra la aplicabilidad del BI en el deporte utilizando
datos abiertos.

## 🔮 Trabajos futuros

-   Ampliar temporadas\
-   Añadir más variables\
-   Automatizar pipeline\
-   Análisis predictivo

## 📦 Cómo ejecutar este proyecto

``` bash
python extractor_nba.py
```

## 👥 Autores

-   Álvaro Suárez Carbonell\
-   Alberto Vargas Miñagorri
