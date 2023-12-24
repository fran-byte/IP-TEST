# Programa en Python para automatizar la modificación de Ips Host/Gateway de nuestro Terminal
# Por Fran-Byte

import tkinter as tk
import socket
import netifaces
import subprocess
import os
import configparser
from configparser import ConfigParser
import ctypes
import time

# Ejecuta el comando netsh para activar/desactivar el WiFi (CLASE)
class WIFI:
    def __init__(self):
        self.interface_name = "Wi-Fi"
    
    def enable(self):
        subprocess.run(["netsh", "interface", "set", "interface", self.interface_name, "enable"])
        
    def disable(self):
        subprocess.run(["netsh", "interface", "set", "interface", self.interface_name, "disable"])

wifi = WIFI()

# Desactivamos WiFi para trabajar correctamente solo con la red Ethernet
wifi.disable()


# Función para salir del programa
def salir():
    wifi.enable()

    # Vamos a hacer el proceso inverso y habilitar las conexiones ethernet desabilitadas anteriormente si las hubiera

    adaptador = adaptador_seleccionado.get()

    adaptersSinEternetValida = adapters  # Recogemos toda la lista de adaptadores de red
    
    

    if len(adaptersSinEternetValida) != 0:  # Si no hay ethernets que desabilitar saltamos este paso
        
        for x in adaptersSinEternetValida:       # Iteramos la lista de ethernets NO utilizadas y las habilitamos de nuevo para dejar el PC como antes de ejecutar el Programa   
            
            
            a='netsh interface set interface '
            c=' admin=enable'
            
            d=a+'"'+x+'"'+c
            dhcpCommand = d
            print(d)
            command = dhcpCommand.split()
            subprocess.run(command)




    ventana.destroy()


# Obtiene el identificador de la ventana de la línea de comandos
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# Deshabilita la opción de cerrar la ventana de la línea de comandos
hmenu = ctypes.windll.user32.GetSystemMenu(hwnd, False)
ctypes.windll.user32.DeleteMenu(hmenu, 6, 0x400)



# Ejecutar el comando "ipconfig" en la terminal
output = subprocess.check_output(['ipconfig', '/all']).decode('latin-1')



# Creando entorno gráfico 
ventana = tk.Tk()

# Deshabilitando acción de cerrar en el entorno gráfico
def disable_event():
    pass
ventana.protocol("WM_DELETE_WINDOW", disable_event)

# Establecer dimensiones de la ventana
ventana.geometry("750x700")

# Establecer el color de fondo de la ventana
ventana.configure(bg="#F0F0F0")
#ventana.configure(bg="light gray")

# Creamos un borde con efecto de relieve
borde = tk.Frame(ventana, bd=2, relief='groove', bg='#F0F0F0')
#borde = tk.Frame(ventana, bd=2, relief='raised', bg='light gray')

# Colocamos el borde en la ventana con un espacio de 10 píxeles
#borde.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
borde.place(relx=0.03, rely=0.03, relwidth=0.9, relheight=0.9)

# Impedimos que la ventana sea manipulable
ventana.resizable(False, False)
ventana.title("Terminal IP Conf")




# Crear listas de IPs
ip_host = ["192.168.0.24", "192.168.1.2","192.168.0.2", "10.117.3.84", "192.168.0.205", "192.168.1.1"]
ip_gateway = ["192.168.0.25", "192.168.0.30", "192.168.0.1", "192.168.0.5", "192.168.1.1", "10.117.3.85", "192.168.0.201", "192.168.1.2"]


# Obtener lista de adaptadores de red

adapters = []

# Iterar a través de las líneas de salida del comando ipconfig
for line in output.split('\n'):
    # Si la línea contiene la cadena "Ethernet adapter" o "Adaptador de Ethernet", es un adaptador de Ethernet (Ojo al parche! dependiendo de versiones de Windows)
    if 'Ethernet adapter' in line or 'Adaptador de Ethernet' in line:
        # Obtener el nombre del adaptador eliminando el prefijo "Ethernet adapter " o "Adaptador de Ethernet "
        adapter_name = line.split(':')[0].replace('Ethernet adapter ', '').replace('Adaptador de Ethernet ', '').strip()
        adapters.append(adapter_name)



# Variables para guardar las IPs y adaptador seleccionados
ip_seleccionada_host = tk.StringVar()
ip_seleccionada_gateway = tk.StringVar()
adaptador_seleccionado = tk.StringVar()

# Crear etiquetas para las selecciones de IP y adaptador

label_host = tk.Label(ventana, bg="#F0F0F0")
label_host.grid(row=1, column=0)


label_host = tk.Label(ventana, text="Set Host IP:", anchor='w', bg="#F0F0F0", font=("Calibri", 12))
label_host.grid(row=3, column=0, padx=30, pady=10, sticky=tk.W)

label_gateway = tk.Label(ventana, text="Set Gateway IP:", anchor='w', bg="#F0F0F0", font=("Calibri", 12))
label_gateway.grid(row=4, column=0, padx=30, pady=10, sticky=tk.W)

label_adaptador = tk.Label(ventana, text="Available Network Adapters:", anchor='w', bg="#F0F0F0", font=("Calibri", 12))
label_adaptador.grid(row=5, column=0, padx=30, pady=10, sticky=tk.W)



# Crear desplegables con las IPs
ip_menu_host = tk.OptionMenu(ventana, ip_seleccionada_host, *ip_host)
ip_menu_host.config(bg="#F0F0F0", font=("Calibri", 12),)
ip_menu_host.grid(row=3, column=2, padx=10, pady=10)

ip_menu_gateway = tk.OptionMenu(ventana, ip_seleccionada_gateway, *ip_gateway)
ip_menu_gateway.config(bg="#F0F0F0", font=("Calibri", 12),fg="blue")
ip_menu_gateway.grid(row=4, column=2, padx=10, pady=10)

# Crear desplegable con los adaptadores de red
adaptador_menu = tk.OptionMenu(ventana, adaptador_seleccionado, *adapters)
adaptador_menu.config(bg="#F0F0F0", font=("Calibri", 12))
adaptador_menu.grid(row=5, column=2, padx=10, pady=10)

# Establecer el valor predeterminado del desplegable de host
ip_seleccionada_host.set(ip_host[0])

ip_menu_gateway = tk.OptionMenu(ventana, ip_seleccionada_gateway, *ip_gateway)
ip_menu_gateway.config(bg="#F0F0F0", font=("Calibri", 12), fg="blue")
ip_menu_gateway.grid(row=4, column=2, padx=10, pady=10)

# Establecer el valor predeterminado del desplegable de gateway
ip_seleccionada_gateway.set(ip_gateway[0])

# Establecer el valor predeterminado del desplegable de adaptador
adaptador_seleccionado.set(adapters[0])

# Enviar_ping a Gateway (CLASE)
class PingPong():



    def __init__(self, numero_pings):
        
        self.numero_pings = numero_pings

    def enviar_ping(self):

        gateway = ip_seleccionada_gateway.get()
        for i in range(1, self.numero_pings):

            response = subprocess.call(['ping', '-n', '1', gateway])
            
            if response == 0:                              
                
                label_resultado.config(text=f" {i+1} PING to {gateway}: ok",fg="#F0F0F0", bg="dark green")
               	
            else:
                
                label_resultado.config(text=f" PING Error to {gateway}", fg="#F0F0F0", bg="dark red")

                break

          

# Nº de Tests
test_ping = PingPong(50)

# Crear botón para enviar Ping     
boton_ping = tk.Button(ventana, text="Ping to Gateway", command=test_ping.enviar_ping, width=25)
boton_ping.config(bg="#F0F0F0", font=("Calibri", 12))
boton_ping.grid(row=8, column=0, columnspan=2, padx=10, pady=10)



# Función para guardar las IPs y adaptador seleccionados
def guardar_ip_y_adaptador():

                                                                                   



     # habilitamos adaptador por si lo hubieramos desabilitado en el primer cambio

    adaptador = adaptador_seleccionado.get()
            
    a='netsh interface set interface '
    c=' admin=enable'
            
    d=a+'"'+adaptador+'"'+c
    dhcpCommand = d
    print(d)
    command = dhcpCommand.split()
    subprocess.run(command)


    ip_host = ip_seleccionada_host.get()
    ip_gateway = ip_seleccionada_gateway.get()
    adaptador = adaptador_seleccionado.get()
    label_resultado.config(text=f"ESTABLISHED COMMS ENVIRONMENT\n    → Host IP: {ip_host}\n    → Gateway IP: {ip_gateway}\n    → Adapter: {adaptador}", bg="#F7F9B7", fg="black", font=("Calibri", 12))
    
    a = 'netsh interface ip set address name='
    c = " static "
    mask = " 255.255.255.0 "
    d = a + '"' + adaptador + '"' + c + ip_host + mask + ip_gateway
    dhcpCommand = d
    command = dhcpCommand.split()
    subprocess.run(command)
    delay = 4
    print("\n  > > > Configure Static IP with the Command [ ", d, " ]")

    # **************** Deshabilitar otras Ethernets no utilizadas
    # **************** 1º Recoger información de ethernet no utilizadas y almacenarlas en una lista

    adaptersSinEternetValida = adapters.copy()  # Copiar la lista para evitar modificar la original
    
    if adaptador in adaptersSinEternetValida:
        adaptersSinEternetValida.remove(adaptador) # Borramos adaptador que no queremos deshabilitar de la lista de adaptadores de red

        label_resultado2.config(text=f"        NETS DISABLED: \n    → ['WIFI']\n    → {adaptersSinEternetValida}", bg="#F9B7B7", fg="black", font=("Calibri", 12))

        if len(adaptersSinEternetValida) != 0:  # Si no hay ethernets que deshabilitar saltamos este paso
            for x in adaptersSinEternetValida:       # Iteramos la lista de ethernets NO utilizadas     
                a = 'netsh interface set interface '
                c = ' admin=disable'
                d = a + '"' + x + '"' + c
                dhcpCommand = d
                print(d)
                command = dhcpCommand.split()
                subprocess.run(command)
    else:
        label_resultado2.config(text="Selected adapter not found in the list.", bg="white", fg="black", font=("Calibri", 12))





            

# IP en DHCP
def cambiar_dhcp():

    adaptador = adaptador_seleccionado.get()
    

    a="netsh interface ip set address "
    c=" dhcp"
    d=a+'"'+adaptador+'"'+c
    print(d)
    dhcpCommand = d
    import subprocess
    command = dhcpCommand.split()
    subprocess.run(command)
    delay = 1
    gws = netifaces.gateways()
    gateway = socket.gethostbyname(socket.gethostname())
    label_resultado.config(text=f" The IP is now Dynamic", bg="#EFEF00", fg="black")

    print("\n>>   Done !! - Now our ",adaptador," address is Dynamic: DHCP")




# Crear botón para convertir IP a DHCP
button_dhcp = tk.Button(ventana, text='Change to DHCP', command=cambiar_dhcp, width=25)
button_dhcp.config(bg="#F0F0F0", font=("Calibri", 12))
button_dhcp.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

# Crear botón para guardar las IPs y adaptador seleccionados
boton_guardar = tk.Button(ventana, text="Save", command=guardar_ip_y_adaptador, width=15)
boton_guardar.config(bg="#F0F0F0", font=("Calibri", 12))
boton_guardar.grid(row=6, column=2, padx=10, pady=10)

# Crear un recuadro 1 para mostrar las IPs y adaptador seleccionados                                          
label_resultado = tk.Label(ventana, text="- COMMUNICATIONS ENVIRONMENT -", bg="#F7F9B7", width=33, height=4, relief="sunken", anchor="w", justify="left", wraplength=350, font=("Calibri", 12))
label_resultado.grid(row=7, column=0, columnspan=2, padx=35, sticky=tk.W, pady=10)

# Crear un recuadro 2 para mostrar las IPs y adaptador seleccionados
label_resultado2 = tk.Label(ventana, text="                   - NETS DISABLED -", bg="#F9B7B7", width=33, height=4, relief="sunken", anchor="w", justify="left", wraplength=350, font=("Calibri", 12))
label_resultado2.grid(row=7, column=1, columnspan=2, padx=35, sticky=tk.W, pady=10)


# Crear etiqueta advertencia
label_advertencia = tk.Label(ventana, text="By Fran Byte", anchor='w', bg="#F0F0F0", fg="#F9B7B7", font=("Calibri", 12))
label_advertencia.grid(row=12, column=0, padx=125, pady=0, sticky=tk.W)


# Crear botón para habilitar Wifi y Salir   
boton_habilitar_wifi = tk.Button(ventana, text="EXIT →", command=salir, width=25, fg="green")
boton_habilitar_wifi.config(bg="#F0F0F0", font=("Calibri", 12))
boton_habilitar_wifi.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="s")


ventana.mainloop()


