Import-Module -Name ActiveDirectory

$pyHost = $args[0]

Get-ADComputer $pyHost -properties * | select Name, Description, IPv4address, OperatingSystem, OperatingSystemServicePack, Enabled, LockedOut, LastLogonDate