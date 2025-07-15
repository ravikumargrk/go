@echo off

set packages=%USERPROFILE%/packages
set diffs=Z:\EU\AUTH\SMV\diffxlsx
set payloads=Z:\EU\AUTH\SMV\payloads

python "C:\Users\E161262\OneDrive - Mastercard\Documents\TASKS\go\go.py" %*
if exist "C:\Users\E161262\OneDrive - Mastercard\Documents\TASKS\go\go_temp.cmd" call "C:\Users\E161262\OneDrive - Mastercard\Documents\TASKS\go\go_temp.cmd"