@echo off

pushd %~dp0

for /f "tokens=* delims=" %%a in ('jsonextractor.bat params.json InstallRequirement.Env') do (
	set "ENV_PATH=%%~a"
)

SETLOCAL
%ENV_PATH%\python.exe .\main.py
ENDLOCAL

PAUSE