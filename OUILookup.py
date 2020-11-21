from getmac import get_mac_address#Librería para obtener la mac
import sys#Librerias para obtener datos al ejecutar el programa
import getopt

argv1=str(sys.argv[1].upper())
argv2=str(sys.argv[2].upper())
def eMac(x):#Funcion para buscar la mac y su correspondiente
    cont=-1
    b=x in texto
    for i in texto:
        cont=cont+1
        if(i==x):
            print("Mac address: ",i)
            print("Vendor: ",texto[cont+1])
    if(b!=True):
        print("Vendo: Not found")
def eIp(x):#Libreria para encontrar la mac en casi de ingresar una ip
    ip_mac=str(get_mac_address(ip=x))
    cont=-1
    bol=ip_mac in texto
    for i in texto:
        cont=cont+1
        if(i==ip_mac):
            print("Mac address: ",i)
            print("Vendor: ",texto[cont+1])
    if(bol!=True or ip_mac=="None"):
        print("Error: ip is outside the host network")
      
r=open("manuf.txt","r",encoding='utf-8')#Se abre,lee y cierra el archivo manuf con las mac dadas
texto=r.read().split()
r.close()

if("IP"in argv1):#Condiciones de ejecucion
    eIp(argv2)
if("MAC" in argv1):
    eMac(argv2)


    



       
            

    
