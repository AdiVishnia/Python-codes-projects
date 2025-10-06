cd .../
cd %USERPROFILE%\Desktop
mkdir CMDcodingtask
cd CMDcodingtask
netstat -ano > netstat_output.txt
findstr " :80 " netstat_output.txt >nul
if %errorlevel%==0 (
    echo Port 80 connection found!
) else (
    echo No port 80 connections found.
)
del netstat_output.txt
pause