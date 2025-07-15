@echo off

set packages=%USERPROFILE%/packages

python "go.py" %*
if exist "go_temp.cmd" call "go_temp.cmd"