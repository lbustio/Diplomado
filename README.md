# Diplomado en Big Data & Data Analytics — Analítica de Datos en Python

**Universidad Iberoamericana, Ciudad de México**
**Dr. Lázaro Bustio Martínez** — [lazaro.bustio@ibero.mx](mailto:lazaro.bustio@ibero.mx)

Repositorio de materiales del módulo **"Analítica de Datos en Python"**, parte del Diplomado en Big Data & Data Analytics. Incluye las diapositivas, ejercicios, tareas y notebooks de las 5 sesiones del curso.

## Contenido del curso

| Sesión | Tema | Notebook / material destacado |
|---|---|---|
| 1 | Introducción al espacio de trabajo Python: aspectos esenciales del lenguaje, Jupyter Lab, tipos de datos, importación de archivos planos. | `Sesión 1/Tarea/Tarea Sesión 1.py` |
| 2 | Manejo de tablas en Python: NumPy, Series y DataFrames de pandas, creación/indexado/transformación de tablas. | `Sesión 2/Códigos Sesión 2/Sesión2.ipynb` |
| 3 | Análisis Exploratorio de Datos: limpieza de datos, `query`/`filter`/`sort_values`/`groupby`, series temporales, `pivot`/`melt`, expresiones regulares. | `Sesión 3/Ejercicio de clase/Titanic.ipynb` |
| 4 | Representación gráfica de datos: matplotlib orientado a objetos, visualización estadística con seaborn, galería de +20 tipos de gráficos. | `Sesión 4/Códigos/Visualizacion.ipynb` |
| 5 | **Proyecto integral**: detección de malware en APKs de Android a partir de sus permisos, aplicando EDA, agrupamiento (KMeans) y clasificación (SVM, Random Forest, KNN). | `Sesión 5/Actividad Práctica - Sesión 5.ipynb` |

## Estructura del repositorio

```
├── Sesión 1.../Sesión 5/     Material completo de cada sesión: diapositivas (.pptx),
│                             tareas, ejercicios de clase y lecturas complementarias.
├── Codigo/                   Espejo ligero solo con los notebooks, scripts y datasets
│                             (sin diapositivas ni PDFs), pensado para que el
│                             estudiante clone/descargue únicamente lo que necesita
│                             para programar. Ver Codigo/readme.md.
├── Referencias/              Lecturas y hojas de referencia adicionales de Python.
└── Guía de Estudio.docx      Cronograma, políticas del curso y bibliografía sugerida.
```

> **Nota:** las carpetas `Bibliografía/` (libros de texto con derechos de autor) y `Burocráticos/` (documentos administrativos internos) existen en el material de clase pero **no se publican** en este repositorio público.

## Requisitos

- Python 3.x
- Jupyter Notebook (Google Colab, Visual Studio Code, PyCharm, etc.)
- Bibliotecas: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `plotly`

Cada notebook incluye sus propias celdas `%pip install` para instalar lo que haga falta.

## Cómo usar este repositorio

- Si vas a **seguir las clases y hacer los ejercicios**, trabaja directamente en la carpeta de cada `Sesión N`.
- Si solo quieres **el código y los datos** sin el resto del material (diapositivas, PDFs), usa la carpeta `Codigo/`.

## Contribuciones

¡Bienvenidas! Abre un *issue* o un *pull request* para corregir errores, mejorar la documentación o proponer contenido adicional.

## Autor

[Dr. Lázaro Bustio Martínez](https://github.com/lbustio) — [lazaro.bustio@ibero.mx](mailto:lazaro.bustio@ibero.mx)

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta [LICENSE.md](LICENSE.md) para más detalles.
