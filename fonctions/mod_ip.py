#=[site officiel]=====================
#<<<<<mod_ip by W3YZOH0RTH>>>>>
#=====[http://progject.free.fr/]=======
import urllib
import socket

# fonctions
#	get_ip_ext()
#		-> string
#	get_ip_int()
#		-> string

def get_ip_ext():
    return urllib.urlopen('http://progject.free.fr/api/ip.php').read()

def get_ip_int():
    return socket.getaddrinfo(socket.gethostname(), None)[0][4][0]
