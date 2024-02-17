import socket

openports =[]
# scan function to take in the target domain and the port number
# to be scanned
def scan(target, port):

    testsock = socket.socket() # create a new object of socket

    # try to connect to the port within two seconds
    try: 
        testsock.settimeout(0.1) # has a limit of 2 seconds to make a connection with the domain's port
        testsock.connect((domain, port)) # try to make a connection with the domain's port
        try: 
            service = socket.getservbyport(port) # if a connection was made with the port, identify the service provided by that port
            openports.append(port)
            print(f"[-] Port {port} is open ({service})")

        except socket.error: # if the service or protocol was not identified
            print("No service or protocol identified")
            print(socket.error)

    # if no connection was able to be made with the port
    except:
        print(f"[-] Port {port} is closed.")
        pass

    # don't leave the port open once done
    finally:
        testsock.close()



s = socket.socket() # create a new object of type socket

domain = input("[+] Enter Target Domain: ") # take in the domain/target
IPaddr = socket.gethostbyname(domain) # get the IP address of the domain
# print(IPaddr)

ports = input("[+] Enter Port(s) you want to scan: ") # ports to scan on the domain
portList = [int(x) for x in ports.split()] # we will store each inputed port in a list. The split function is to distinguish into it's own indexes.
 

if len(portList) == 0: # if no ports were inputed, then the script will by default print out all the ports from 1-1024
    print("\n")
    print("[-] (DISCLAIMER) This may take a few minutes.")
    print("\n")
    for port in range(1,1024):
        scan(domain, port)
else: # if there are ports that the user specifically wanted to check
    for port in portList: # we will iterate through the list storing the ports the user entered to be scanned.
        scan(domain, port)

print("[-] Scan Complete")
print("[-] Open Ports: ")
print(openports)








