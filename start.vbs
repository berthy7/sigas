Set WshShell = CreateObject("WScript.Shell")
WshShell.Run Chr(34) & "C:\Proyectos\proyecto_prueba\run_server.bat" & Chr(34), 0
Set WshShell = Nothing