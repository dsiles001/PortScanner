import socket

openports = []

def scan(target, port):
    testsock = socket.socket()
    try:
        testsock.settimeout(2)
        testsock.connect((domain, port))
        print(f"{port} is open")
    except:
        print("Couldn't connect")
        pass
    finally:
        testsock.close()


s = socket.socket()

domain = input("Enter Target Domain: ")
IPaddr = socket.gethostbyname(domain)
print(IPaddr)

for portnum in range(1000):
    scan(domain, portnum)




