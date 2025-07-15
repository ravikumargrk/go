@echo off

set packages=%USERPROFILE%/packages
set diffs=Z:\EU\AUTH\SMV\diffxlsx
set payloads=Z:\EU\AUTH\SMV\payloads

python "go.py" %*
if exist "go_temp.cmd" call "go_temp.cmd"