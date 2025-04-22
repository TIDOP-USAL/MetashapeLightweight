# Metashape Lightweight

1. [Qué es Metashape Lightweight](#qué-es-metashape-lightweight)
1. [Instalación](#instalacion)
1. [Datos de ejemplo](#datos-de-ejemplo)
1. [Instrucciones de uso y ejecución](#instrucciones-de-uso-y-ejecución)
   1. [Workflow](#parámetros-workflowflujo-de-trabajo)
   1. [Installarion](#parámetros-installationrequisitos-de-instalación)
   1. [Project](#parámetros-projectproyecto)
   1. [SplitTile](#parámetros-splittiledivisión-en-celdas)
   1. [Photo](#parámetros-photoimágenes)
   1. [OptimizeAlignment](#parámetros-optimizealigmentorientación)
   1. [PointCloud](#parámetros-pointcloudnube-de-puntos)
   1. [Raster](#parámetros-rasterproductos-ráster)

# Qué es **Metashape Lightweight**

Esta herramienta utiliza la API de Agisoft Metashape para procesar vuelos fotogramétricos con cámaras no métricas.
Las utilidades permiten procesar:
* con bajos requisitos de hardware,
* de forma semiautomática, lo más desatendida posible.

Los productos resultantes pueden ser:
* Nube de puntos densa, en formato `.laz`
* Modelos digitales de elevaciones, en formato `.tif`
* Ortomosaico, en formato `.tif`
* Informe de resultados generado por Metashape, en formato `.pdf`

Además, se exportan durante el procesamiento:
* `*_log.txt` Archivo de texto con histórico de eventos y mensajes relevantes sobre el proceso.
* `*.psz` y `*.files` Proyecto de Metashape completo, o de cada tile (si se hubiera dividido el trabajo).
* `*_initial.psz` y `*_initial.files` Proyecto de Metashape en un estadio previo a la optimización de parámetros de orientación interna (si se hubiera ejecutado tal calibración).
* `*_shapes.gpkg` Geometrías utilizadas, región de interés y tiles (si los hubiera).

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

Algunas advertencias generales de uso son:
* No se permiten caracteres especiales en la definición de los parámetros de entrada.
* EPSG permitidos: 25830, 25830+5782, 4326, 4326+3855, 4258+5782, 4083+9397, 4081+9397.

Los pasos para utilizar el programa son:
1. Haber terminado la instalación y la activación de la licencia como se indica en el apartado [Instalación](#instalación)
1. Adaptar las rutas de instalación en el archivo `MetashapeLightweight.bat` 
1. Ejecutar el archivo `MetashapeLightweight.bat`

## Parámetros `Workflow`|`Flujo de trabajo`

Estos parámetros describen los pasos que se van a ejecutar.

Es importante resaltar que:
* La carpeta de resultados será borrada en cada ejecución si se activa el paso `CleanPrevious`|``

## Parámetros `Installation`|`Requisitos de instalación`

Estos parámetros describen las condiciones de hardware e instalación que se van a utilizar.

Es importante resaltar que:
* El procesamiento con CPU debe ser activado si ninguna GPU es seleccionada.

## Parámetros `Project`|`Proyecto`

Estos parámetros describen el proyecto y los resultados que se van a alcanzar.

Es importante resaltar que:
* El archivo a importar como **región de interés**, debe:
  * Tener formato SHP
  * Ser de tipo = `Polygon`
  * Contener una sola entidad
  * Tener CRS = EPSG:4326

## Parámetros `SplitTile`|`División en celdas`

Estos parámetros describen las condiciones en las que se van a dividir las partes del trabajo fraccionado.

Es importante resaltar que:
* Para utilizar **una malla vectorial en archivo GPKG** el archivo debe haber sido creado previamente por este programa.
* En la edición manual de la capa solo está permitida la modificación del campo `ignore`.

## Parámetros `Photo`|`Imágenes`

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

## Parámetros `OptimizeAligment`|`Orientación`

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
* Los parámetros de orientación interna que no se calibren se mantendrán fijos tras la importación.

## Parámetros `PointCloud`|`Nube de puntos`

Estos parámetros describen las condiciones con las que se va a generar la nube densa del trabajo.

Es importante resaltar que:
* Para generar la nube densa, es necesario que el trabajo esté georreferenciado, es decir, que o bien las imágenes tengan orientaciones externas de partida, y/o se hayan utilizado puntos de apoyo para hacer calibrar la orientación interna de la cámara.

## Parámetros `Raster`|`Productos ráster`

Estos parámetros describen las condiciones con las que se va a generar los productos ráster, es decir, modelo digital de superficies, del terreno y ortomosaico.
