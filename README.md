# PortScanner
Input:

  The script will prompt you to enter a domain name or URL. It also accepts IP addresses of the domains you want to scan.
  Once the input is set, it will prompt you to enter the port or ports you would like to scan on the domain. If you only want
  to scan one port, just input the one port. If you want to scan multiple ports, enter each port number separated by a space. If   
  there are no port numbers entered, the script will by default scan ports 1-1024. 

Output:

  The script will go through each port to check if the port is opened or closed. 
  
  The port number, along with the service it provides, will be displayed if the port is open: [-] {port} is opened.

  If the port is closed, it will simply display that the port is closed.
  
