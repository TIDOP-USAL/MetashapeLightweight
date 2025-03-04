# Requisitos instalación

* Entorno conda
  * `conda --version` = conda 25.1.1. Actualize con `conda update conda`
  * `conda create -n metashape_2_2_0 python=3.11`
  * `conda activate metashape_2_2_0`
  * `pip install Metashape-2.2.0-cp37.cp38.cp39.cp310.cp311-none-win_amd64.whl`
  * `conda install -c conda-forge gdal=3.9.2`
  * `conda install -c conda-forge laspy=2.5.4`
  * `conda install -c conda-forge pyqt=5.15.10`
* Agisoft Metashape 2.2.0 [link](https://download.agisoft.com/metashape-pro_2_2_0_x64.msi) + activar licencia en GUI.
* Módulo python de Metashape Pro 2.2.0 [link](https://download.agisoft.com/Metashape-2.2.0-cp37.cp38.cp39.cp310.cp311-none-win_amd64.whl)
* Modelos del geoide para descargar [link](https://www.agisoft.com/downloads/geoids/)

# Requisitos de uso

## Advertencias generales

* EPSG permitidos: 25830, 25830+5782, 4326, 4326+3855, 4258+5782, 4083+9397, 4081+9397.
* El procesamiento con CPU será activado si ninguna GPU es seleccionada
* La carpeta de resultados será borrada en cada ejecución.
* No se permiten caracteres especiales en la definición de los parámetros de entrada.
* Los parámetros de orientación interna que no se calibren se mantendrán fijos tras la importación.
* La captura de las imágenes debe ser con tomas cenitales.

## Importación de orientaciones externas

Para importar **orientaciones externas** desde archivo CSV, éste debe tener la siguiente estructura:
* Separador de campos `;`
* Separador decimal `.`
* Sin cabecera
* Sin primera fila de títulos o encabezados
* Para coordenadas geodésicas:
  * Campos: `label,longitude,latitude,altitude`
  * Unidades: deg
* Para coordenadas proyectadas:
  * Campos: `label,east,north,altitude`
  * Unidades: según EPSG
  
## Importación de puntos de apoyo

Para importar **GCP** desde archivo CSV, éste debe tener la siguiente estructura:
* Separador de campos `;`
* Separador decimal `.`
* Sin cabecera
* Sin primera fila de títulos o encabezados
* Para coordenadas geodésicas:
  * Campos: `label,longitude,latitude,altitude`
  * Unidades: deg
* Para coordenadas proyectadas:
  * Campos: `label,east,north,altitude`
  * Unidades: según EPSG

## Fotointerpretación de los puntos de apoyo

* No deben quedar puntos de apoyo desmarcados = check points.
* Cada punto debe estar fotointerpretado en al menos 3 imágenes.
* Para mejorar la visualización de imágenes térmicas, ir a Tools / Set Brightness... / Estimate.
* No se debe modificar ningún otro parámetro o configuración del proyecto.

## Importación de región de interés

Para utilizar una **región de interés**, debe:
* Estar previamente definida en un archivo SHP
* Tipo: `Polygon`
* Contener una sola entidad
* CRS: EPSG:4326

## Importación de malla de tileado

Para utilizar **una malla vectorial en archivo GPKG** el archivo debe haber sido creado previamente por este programa.

# Instrucciones de ejecución

1. Ejecutar el archivo `MetashapeLightweight.bat`
