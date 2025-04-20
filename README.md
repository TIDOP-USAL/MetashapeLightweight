1. [Metashape Lightweight](#metashape-lightweight)
1. [Advertencias generales de uso](#advertencias-generales-de-uso)
1. [Instalación](#instalacion)
1. [Datos de ejemplo](#datos-de-ejemplo)
1. [Instrucciones de uso y ejecución](#instrucciones-de-uso-y-ejecución)

# Qué es **Metashape Lightweight**

Esta herramienta utiliza la API de Agisoft Metashape para procesar vuelos fotogramétricos con cámaras no métricas.
Las utilidades permiten procesar:
- con bajos requisitos de hardware,
- de forma semiautomática, lo más desatendida posible.

# Advertencias generales de uso

* La carpeta de resultados será borrada en cada ejecución.
* No se permiten caracteres especiales en la definición de los parámetros de entrada.
* EPSG permitidos: 25830, 25830+5782, 4326, 4326+3855, 4258+5782, 4083+9397, 4081+9397.

# Instalación

* Descargas necesarias:
  * Agisoft Metashape 2.2.0 [link](https://download.agisoft.com/metashape-pro_2_2_0_x64.msi)
  * Módulo python de Metashape Pro 2.2.0 [link](https://download.agisoft.com/Metashape-2.2.0-cp37.cp38.cp39.cp310.cp311-none-win_amd64.whl)
  * Modelos del geoide para descargar [link](https://www.agisoft.com/downloads/geoids/)

* Entorno conda:
  * `conda --version`: Necesario conda 25.1.1. Actualize con `conda update conda`
  * `conda create -n metashape_2_2_0 python=3.11`
  * `conda activate metashape_2_2_0`
  * `pip install Metashape-2.2.0-cp37.cp38.cp39.cp310.cp311-none-win_amd64.whl`
  * `conda install -c conda-forge gdal=3.9.2`
  * `conda install -c conda-forge laspy=2.5.4`
  * `conda install -c conda-forge pyqt=5.15.10`
  * Instalar `*.msi`
  * Arrancar GUI y activar licencia

# Datos de ejemplo

## Set 'rail2024'

Ubicación: `./sample_data/rail2024`

Contenido:
* `*.JPG` Imágenes
* `eo_4326.csv` Orientaciones externas de las imágenes
* `gcp_25830-5782.csv` Puntos de apoyo
* `markers.xml` Archivo de puntos de apoyo importable en Metashape
* `params*.json` Ficheros de parámetros para los procesos de testeo propuestos
* `readme.md` Notas sobre el set de datos
* `roi_4326.shp` Geometría del área de trabajo
* `tile_grid_manual.gpkg` Geometrías de los tiles seleccionados para procesar

Los procesos de testeo propuestos utilizan los parámetros:

| FILE          | LABEL  | EO   | IO    | ROI  | Split |
|---------------|--------|------|-------|------|-------|
| params01.json | test01 | EXIF | False | FULL | False |
| params02.json | test02 | CSV  | False | FULL | False |
| params03.json | test03 | EXIF | False | SHP  | False |
| params04.json | test04 | EXIF | PSX   | SHP  | False |
| params05.json | test05 | EXIF | XML   | SHP  | False |

# Instrucciones de uso y ejecución

1. Adaptar las rutas de instalación en el archivo `MetashapeLightweight.bat` 
1. Ejecutar el archivo `MetashapeLightweight.bat`

## Parámetros `Workflow`

Estos parámetros describen los pasos que se van a ejecutar.

## Parámetros `InstallRequirement`

Estos parámetros describen las condiciones de hardware e instalación que se van a utilizar.

Es importante resaltar que:
* El procesamiento con CPU debe ser activado si ninguna GPU es seleccionada.

## Parámetros `Project`

Estos parámetros describen el proyecto y los resultados que se van a alcanzar.

## Parámetros `Photo`

Estos parámetros describen las condiciones de importación y proceso de las imágenes utilizadas.

Es importante resaltar que:
* La captura de las imágenes debe ser con tomas cenitales.
* Para importar **orientaciones externas** desde archivo CSV, éste debe tener la siguiente estructura:
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

## Parámetros `ROI`

Estos parámetros describen la región de interés con la que se va a recortar el trabajo ejecutado.

Es importante resaltar que:
* El archivo a importar como **región de interés**, debe:
  * Tener formato SHP
  * Ser de tipo = `Polygon`
  * Contener una sola entidad
  * Tener CRS = EPSG:4326

## Parámetros `OptimizeAligment`

Estos parámetros describen las condiciones en las que se va a ejecutar la optimización de la calibración de los parámtros de orientación interna de la cámara.

En importante resaltar que:
* Para importar **GCP** desde archivo CSV, éste debe tener la siguiente estructura:
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
* En caso de elegir la fotointerpretación de los puntos de apoyo:
  * No deben quedar puntos de apoyo desmarcados (llamados check points en Metashape).
  * Cada punto debe estar fotointerpretado en al menos 3 imágenes.
  * Para mejorar la visualización de imágenes térmicas, ir a Tools / Set Brightness... / Estimate.
  * No se debe modificar ningún otro parámetro o configuración del proyecto.
  
## Parámetros `CameraCalibration`

Estos parámetros describen los parámetros de orientación interna de la cámara que se van a considerar.

Es importante resaltar que:
* Los parámetros de orientación interna que no se calibren se mantendrán fijos tras la importación.

## Parámetros `PointCloud`

Estos parámetros describen las condiciones con las que se va a generar la nube densa del trabajo.

Es importante resaltar que:
* Para generar la nube densa, es necesario que el trabajo esté georreferenciado, es decir, que o bien las imágenes tengan orientaciones externas de partida, y/o se hayan utilizado puntos de apoyo para hacer calibrar la orientación interna de la cámara.

## Parámetros `SplitTile`

Estos parámetros describen las condiciones en las que se van a dividir las partes del trabajo fracionado.

Es importante resaltar que:
* Para utilizar **una malla vectorial en archivo GPKG** el archivo debe haber sido creado previamente por este programa.
* En la edición manual de la capa sólo está permitida la modificación del campo `ignore`.
