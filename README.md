   # AI-Enhanced Telecom Network Monitoring

## Resumen de la Tesis

Esta tesis explora el diseño y la implementación de un sistema de monitoreo de redes de telecomunicaciones que utiliza inteligencia artificial (IA) para mejorar la detección de anomalías, la predicción de fallos y la optimización del rendimiento de la red. El objetivo es demostrar cómo los algoritmos de aprendizaje automático pueden transformar el análisis tradicional de redes, permitiendo una gestión proactiva y adaptativa.

---

## Objetivos

- **Automatización del monitoreo:** Analizar en tiempo real grandes volúmenes de datos provenientes de redes de telecomunicaciones utilizando IA.
- **Detección temprana de anomalías:** Identificar patrones anómalos antes de que se conviertan en fallos críticos mediante modelos avanzados.
- **Optimización del rendimiento:** Ajustar parámetros de red de manera dinámica basándose en las predicciones del sistema.
- **Escalabilidad:** Adaptabilidad a distintos tamaños y topologías de red.

---

## Arquitectura del Sistema

1. **Ingesta de datos:** Captura y procesamiento inicial de datos generados por la red.
2. **Preprocesamiento:** Limpieza, normalización y transformación de los datos para su uso por los algoritmos de IA.
3. **Modelos de IA:** Implementación de modelos de clasificación, regresión y detección de anomalías.
4. **Panel de visualización:** Presentación intuitiva de métricas, alertas y recomendaciones.

---

## Consideraciones Éticas y de Autoría

> **Aviso Importante:**  
> Todo el código, modelos y documentación en este repositorio son originales o debidamente citados. Si alguna sección proviene de fuentes externas, se hará la debida atribución para evitar inconvenientes relacionados con derechos de autor o plagio.  
> Si detectas contenido que requiera corrección o atribución adicional, por favor abre un _issue_ o contacta a los autores.

---

## Descarga y Ubicación de los Datasets

Para que el código funcione correctamente, **es obligatorio descargar los siguientes archivos `.csv` y colocarlos en la misma carpeta desde la cual se ejecuta el código**:

- `UNSW_NB15_training-set.csv`
- `UNSW_NB15_testing-set.csv`
- `UNSW_NB15_TRAIN_FINAL.csv`
- `UNSW_NB15_TEST_FINAL.csv`

Estos archivos son requeridos por los scripts `Precesamiento.py` y `Ensamblaje_de_modelos.py`.  
Asegúrate de no modificar los nombres de los archivos.

**Próximamente:** aquí estarán disponibles los enlaces de descarga directa a cada archivo una vez alojados en sistemas de almacenamiento:

- [UNSW_NB15_training-set.csv (próximamente)](https://drive.google.com/file/d/1fVd4hRJSt76B6gRE7VQfiWQNLGy17Y24/view?usp=sharing)
- [UNSW_NB15_testing-set.csv (próximamente)](https://drive.google.com/file/d/1lriIdUiKcEmyPK3nf-jSFS1fISBz8zNZ/view?usp=sharing)
- [UNSW_NB15_TRAIN_FINAL.csv (próximamente)](https://drive.google.com/file/d/1_HbI6w2PMxD0QQoVkPs2-990KFAvOI1p/view?usp=sharing)
- [UNSW_NB15_TEST_FINAL.csv (próximamente)](https://drive.google.com/file/d/1ENFllk8v7RjdaY-75uyGjDGKLm_aGj4i/view?usp=sharing)

---

## Uso del Repositorio

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/HenryDav11/ai-enhanced-telecom-network-monitoring.git
   cd ai-enhanced-telecom-network-monitoring
   ```

2. **Descargar los archivos CSV:**  
   Descarga los archivos mencionados arriba y colócalos en la misma carpeta desde la cual ejecutarás los scripts.

3. **Configurar el entorno:**  
   Instala las dependencias necesarias desde el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar los scripts:**  
   Consulta la documentación y comentarios dentro de cada script para instrucciones detalladas.

---

## Contacto

Para dudas, sugerencias o reportar problemas de autoría, por favor contacta a:  
**Autor:** [HenryDav11](https://github.com/HenryDav11)  
**Correo:** [TuEmail@ejemplo.com] _(modifica por el correo real)_

---

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

¡Gracias por tu interés!  
_Si usas este trabajo, por favor cita adecuadamente y contribuye al desarrollo ético de IA en telecomunicaciones._
