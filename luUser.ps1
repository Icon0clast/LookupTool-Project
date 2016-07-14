Import-Module -Name ActiveDirectory

$pyUser = $args[0]

Get-ADUser $pyUser -properties * | select Name, Enabled, Lockedout, PasswordExpired, LastLogonDate, LastBadPasswordAttempt, Office, Mail, Manager