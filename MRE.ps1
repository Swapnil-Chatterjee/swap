clear

For ($i=0; $i -le 10000; $i++) {



Write-Host -ForegroundColor 12 "  __  __          _ __          __     _____  ______            _   _          _  __     _______ _____  _____ 
 |  \/  |   /\   | |\ \        / /\   |  __ \|  ____|     /\   | \ | |   /\   | | \ \   / / ____|_   _|/ ____|
 | \  / |  /  \  | | \ \  /\  / /  \  | |__) | |__       /  \  |  \| |  /  \  | |  \ \_/ / (___   | | | (___  
 | |\/| | / /\ \ | |  \ \/  \/ / /\ \ |  _  /|  __|     / /\ \ | . ` | / /\ \ | |   \   / \___ \  | |  \___ \ 
 | |  | |/ ____ \| |___\  /\  / ____ \| | \ \| |____   / ____ \| |\  |/ ____ \| |____| |  ____) |_| |_ ____) |
 |_|  |_/_/    \_\______\/  \/_/    \_\_|  \_\______| /_/    \_\_| \_/_/    \_\______|_| |_____/|_____|_____/ 



"

Start-Sleep -Seconds 3

Write-Host -ForegroundColor 10 "Analyzing File Details:

"
Start-Sleep -Seconds 1

Write-Host "File Name: Security_Checklist.exe.xlsx
"
Start-Sleep -Seconds 1


Write-Host "File Size - 576512 bytes
"
Start-Sleep -Seconds 1

Write-Host "File Hashes:
"
Write-Host "SHA256 - 5D2204F3A20E163120F52A2E3595DB19890050B2FAA96C6CBA6B094B0A52B0AA"
Write-Host "SHA1 - BD0BF9C987288CA434221D7D81C54A47E913600A"
Write-Host "MD5 - 3F400F30415941348AF21D515A2FC6A3
"
Start-Sleep -Seconds 1


Write-Host "First Bytes - M Z .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. @ .. .. .. .. .. .. .. .. 
"
Start-Sleep -Seconds 1


Write-Host "Entropy - 6.616
"
Start-Sleep -Seconds 1

Write-Host "Signature - Microsoft Visual C++
"
Start-Sleep -Seconds 1


Write-Host "Tooling - Visual Studio 2015
"
 Start-Sleep -Seconds 1


Write-Host "File Type - Executable
"
Start-Sleep -Seconds 1

Write-Host "CPU - 32-bit
"
Start-Sleep -Seconds 1

Write-Host "Subsystem - Console
"
Start-Sleep -Seconds 1

Write-Host "Compiler Timestamp - Fri Apr 22 20:31:36 2022
"
Start-Sleep -Seconds 1

#Write-Host -ForegroundColor 10 "File Section Info:
#"
#C:\Tools\die\diec.exe -e C:\Users\REM\Desktop\Scripts\BlackBasta\sample.ex
#Start-Sleep -Seconds 1

Write-Host "

"
Write-Host -ForegroundColor 10 "Idenifying Intresting Strings:"
Start-Sleep -Seconds 3

Write-Host "
Please run program as admin
Service deleted
started as service
bcdedit /deletevalue safeboot
C:\Windows\System32\bcdedit.exe /deletevalue safeboot
C:\Windows\SysNative\bcdedit.exe /deletevalue safeboot
/C shutdown -r -f -t 0 "

Write-Host "

"
Write-Host -ForegroundColor 10 "Looking for Indicators:
"
Start-Sleep -Seconds 5

Write-Host "URL: https://aazsbsgya565vlu2c6bzy6yfiebkcbtvvcytvolt33s77xypi7nypxyd.onion
"
Start-Sleep -Seconds 1


Write-Host "Files Dropped:

dlaksjdoiwq.jpg
fkdjsadasd.ico
"
Start-Sleep -Seconds 1


Write-Host "Registry key created:

HKEY_CLASSES_ROOT\.basta
"

Start-Sleep -Seconds 1


Write-Host "
Threat Type: Ransomeware

Threat Family: BlackBasta "
Start-Sleep -Seconds 1

Write-Host "
"
Write-Host -ForegroundColor 10 "Understaing Possible Capablities:"
Start-Sleep -Seconds 5

Write-Host "
+-----------------------------+-------------------------------------------------------------------------------+
| MBC Objective               | MBC Behavior                                                                  |
|-----------------------------+-------------------------------------------------------------------------------|
| ANTI-BEHAVIORAL ANALYSIS    | Conditional Execution::Runs as Service [B0025.007]                            |
|                             | Virtual Machine Detection [B0009]                                             |
| ANTI-STATIC ANALYSIS        | Executable Code Obfuscation::Argument Obfuscation [B0032.020]                 |
|                             | Executable Code Obfuscation::Stack Strings [B0032.017]                        |
| DATA                        | Check String [C0019]                                                          |
|                             | Encode Data::Base64 [C0026.001]                                               |
|                             | Encode Data::XOR [C0026.002]                                                  |
|                             | Non-Cryptographic Hash::FNV [C0030.005]                                       |
| DEFENSE EVASION             | Obfuscated Files or Information::Encoding-Standard Algorithm [E1027.m02]      |
| DISCOVERY                   | File and Directory Discovery [E1083]                                          |
|                             | System Information Discovery [E1082]                                          |
| FILE SYSTEM                 | Get File Attributes [C0049]                                                   |
|                             | Move File [C0063]                                                             |
|                             | Read File [C0051]                                                             |
|                             | Writes File [C0052]                                                           |
| IMPACT                      | Data Destruction::Delete Shadow Copies [E1485.m04]                            |
| OPERATING SYSTEM            | Environment Variable::Set Variable [C0034.001]                                |
|                             | Registry::Set Registry Key [C0036.001]                                        |
| PROCESS                     | Allocate Thread Local Storage [C0040]                                         |
|                             | Create Process [C0017]                                                        |
|                             | Create Thread [C0038]                                                         |
|                             | Terminate Process [C0018]                                                     |
+-----------------------------+-------------------------------------------------------------------------------+"

Write-Host "


"
Write-Host -ForegroundColor 10 "TTPs Identifies:"
Start-Sleep -Seconds 5

Write-Host "
+------------------------+------------------------------------------------------------------------------------+
| ATT&CK Tactic          | ATT&CK Technique                                                                   |
|------------------------+------------------------------------------------------------------------------------|
| DEFENSE EVASION        | Indicator Removal::File Deletion T1070.004                                         |
|                        | Obfuscated Files or Information T1027                                              |
|                        | Obfuscated Files or Information::Indicator Removal from Tools T1027.005            |
|                        | Virtualization/Sandbox Evasion::System Checks T1497.001                            |
| DISCOVERY              | File and Directory Discovery T1083                                                 |
|                        | System Information Discovery T1082                                                 |
|                        | System Service Discovery T1007                                                     |
| EXECUTION              | Shared Modules T1129                                                               |
|                        | System Services::Service Execution T1569.002                                       |
| IMPACT                 | Inhibit System Recovery T1490                                                      |
|                        | Service Stop T1489                                                                 |
| PERSISTENCE            | Create or Modify System Process::Windows Service T1543.003                         |
+------------------------+------------------------------------------------------------------------------------+ "

Write-Host "


"


Start-Sleep -Seconds 10


Clear-Host

}