@echo off
SETLOCAL
set ANACONDA_PATH=C:/miniconda
set ANACONDA_ENV_NAME=metashape_2_2_0
call %ANACONDA_PATH%/Scripts/activate.bat %ANACONDA_ENV_NAME%
python  main_gui.py
ENDLOCAL
