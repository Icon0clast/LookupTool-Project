import-module activedirectory

#Find logged in user of remote computer

$computer = $args[0]

(Get-WmiObject win32_computersystem -comp $computer| select -ExpandProperty username).Split('\')[1]  
