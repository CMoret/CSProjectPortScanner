# CSProjectPortScanner

READ ME UNDER CONSTRUCTION

Language: Python

IDE: Visual Studios

Modules:Socket,Sys and datetime



This program ‘Port Scanner’ is used to verify open ports on a device by specifying its IP address.

 The program begins by importing essential libraries required for network connections, including 'socket', 'sys', and 'datetime'. 

It initializes when the user enters the target IP address, and then a port scanning loop iterates through a range of port numbers from 1 to 65534. 

The 'socket' library is utilized to establish connections with the target device. If a connection is not established within a certain timeout period or if the result indicates an open port, the program records this information. 

The final output may include exceptions or a list of open ports within the specified range.

<img width="1386" alt="PS2" src="https://github.com/CMoret/CSProjectPortScanner/assets/134563934/40485d39-51a4-4b07-9fdc-97e51822b21a">

<img width="1389" alt="PS1" src="https://github.com/CMoret/CSProjectPortScanner/assets/134563934/916df43f-361b-4e4e-9f5e-755b24342d4d">
