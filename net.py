# Programa en Python para automatizar la modificación de Ips Host/Gateway de nuestro Terminal
# Por Fran-Byte

import tkinter as tk
from tkinter import ttk
import subprocess
import netifaces
import socket
import ctypes



# Función vinculada al cambio de selección en el menú desplegable de CHECK
def actualizar_numero_pings(selection):
    if selection == "Normal Check":
        test_ping.numero_pings = 20
    elif selection == "Extended Check":
        test_ping.numero_pings = 200





# Ejecuta el comando netsh para activar/desactivar el WiFi (CLASE)
class WIFI:
    def __init__(self):
        self.interface_name = "Wi-Fi"
    
    def enable(self):
        subprocess.run(["netsh", "interface", "set", "interface", self.interface_name, "enable"])
        
    def disable(self):
        subprocess.run(["netsh", "interface", "set", "interface", self.interface_name, "disable"])

wifi = WIFI()

def check_multiple_ethernet_adapters():
    # Ejecutar el comando "ipconfig" en la terminal
    output = subprocess.check_output(['ipconfig', '/all']).decode('latin-1')
    
    adapters_count = 0
    
    # Iterar a través de las líneas de salida del comando ipconfig
    for line in output.split('\n'):
        # Si la línea contiene la cadena "Ethernet adapter" o "Adaptador de Ethernet", es un adaptador de Ethernet
        if 'Ethernet adapter' in line or 'Adaptador de Ethernet' in line:
            adapters_count += 1
    
    # Devuelve True si hay más de un adaptador de Ethernet habilitado, de lo contrario, devuelve False
    return adapters_count > 1


# Función para salir del programa
def salir():
    wifi.enable()

    # Vamos a hacer el proceso inverso y habilitar las conexiones ethernet desabilitadas si las hubiera
    adaptador = adaptador_seleccionado.get()

    adaptersSinEternetValida = adapters  # Recogemos toda la lista de adaptadores de red
    
    

    if len(adaptersSinEternetValida) != 0:  # Si no hay ethernets que desabilitar saltamos este paso
        
        for x in adaptersSinEternetValida:       # Iteramos la lista de ethernets NO utilizadas     
            
            
            a='netsh interface set interface '
            c=' admin=enable'
            
            d=a+'"'+x+'"'+c
            dhcpCommand = d
            print(d)
            command = dhcpCommand.split()
            subprocess.run(command)


    cambiar_dhcp()

    ventana.destroy()


# Función restaurar Ethernets
def restore_ethernets():
    wifi.enable()

    # Vamos a hacer el proceso inverso y habilitar las conexiones ethernet desabilitadas si las hubiera
    adaptador = adaptador_seleccionado.get()

    adaptersSinEternetValida = adapters  # Recogemos toda la lista de adaptadores de red
    
    

    if len(adaptersSinEternetValida) != 0:  # Si no hay ethernets que desabilitar saltamos este paso
        
        for x in adaptersSinEternetValida:       # Iteramos la lista de ethernets NO utilizadas     
            
            
            a='netsh interface set interface '
            c=' admin=enable'
            
            d=a+'"'+x+'"'+c
            dhcpCommand = d
            print(d)
            command = dhcpCommand.split()
            subprocess.run(command)


    cambiar_dhcp()

    

# Obtiene el identificador de la ventana de la línea de comandos
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# Deshabilita la opción de cerrar la ventana de la línea de comandos
hmenu = ctypes.windll.user32.GetSystemMenu(hwnd, False)
ctypes.windll.user32.DeleteMenu(hmenu, 6, 0x400)



# Ejecutar el comando "ipconfig" en la terminal
output = subprocess.check_output(['ipconfig', '/all']).decode('latin-1')



# Creando entorno gráfico
ventana = tk.Tk()
ventana.iconbitmap(default='error')

# Deshabilitando acción de cerrar en el entorno gráfico
def disable_event():
    pass
ventana.protocol("WM_DELETE_WINDOW", disable_event)

# Establecer dimensiones de la ventana
ventana.geometry("640x625")

# Establecer el color de fondo de la ventana
ventana.configure(bg="#F0F0F0")
#ventana.configure(bg="light gray")

# Creamos un borde con efecto de relieve
borde = tk.Frame(ventana, bd=2, relief='groove', bg='#F0F0F0')
#borde = tk.Frame(ventana, bd=2, relief='raised', bg='light gray')

# Colocamos el borde en la ventana con un espacio de 10 píxeles
borde.place(relx=0.03, rely=0.03, relwidth=0.9, relheight=0.9)
#borde.place(relx=0.01, rely=0.01, relwidth=0.9, relheight=0.9)

# Impedimos que la ventana sea manipulable
ventana.resizable(False, False)
ventana.title("Network Analyzer by Fran Byte")




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


# Crear etiquetas con borde
label_host = tk.Label(ventana, text=" Set Host IP: ", anchor='w', font=("Calibri", 12), bg="#F0F0F0", bd=1, relief="groove")
label_host.grid(row=3, column=0, padx=30, pady=10, sticky=tk.W)

label_gateway = tk.Label(ventana, text=" Set Gateway IP: ", anchor='w', font=("Calibri", 12), bg="#F0F0F0", bd=1, relief="groove")
label_gateway.grid(row=4, column=0, padx=30, pady=10, sticky=tk.W)

label_adaptador = tk.Label(ventana, text=" Available Network Adapters: ", anchor='w', font=("Calibri", 12), bg="#F0F0F0", bd=1, relief="groove")
label_adaptador.grid(row=5, column=0, padx=30, pady=10, sticky=tk.W)


ip_seleccionada_host.set(ip_host[0])

# Crear desplegables con las IPs
ip_menu_host = tk.OptionMenu(ventana, ip_seleccionada_host, *ip_host)
ip_menu_host.config(bg="#373737", font=("Calibri", 12), fg="red")
ip_menu_host.grid(row=3, column=2, padx=10, pady=10)



ip_menu_gateway = tk.OptionMenu(ventana, ip_seleccionada_gateway, *ip_gateway)
ip_menu_gateway.config(bg="#373737", font=("Calibri", 12),fg="blue")
ip_menu_gateway.grid(row=4, column=2, padx=10, pady=10)

# Crear desplegable con los adaptadores de red
adaptador_menu = tk.OptionMenu(ventana, adaptador_seleccionado, *adapters)
adaptador_menu.config(bg="#373737", font=("Calibri", 12))
adaptador_menu.grid(row=5, column=2, padx=10, pady=10)

ip_seleccionada_gateway.set(ip_gateway[0])

adaptador_seleccionado.set(adapters[0])

# Variables para la barra de progreso
progress_value = tk.DoubleVar()
progress_bar = ttk.Progressbar(ventana, variable=progress_value, length=200, mode='determinate')
progress_bar.grid(row=9, column=0)




# Enviar_ping a Gateway (CLASE)
# Enviar_ping a Gateway (CLASE)
class PingPong():
    def __init__(self, numero_pings):
        self.numero_pings = numero_pings
        self.pings_erroneos = 0  # Inicializamos el contador de pings incorrectos
        self.max_pings_erroneos = 2  # Definimos el número máximo de pings incorrectos permitidos

    def enviar_ping(self, i=1):
        gateway = ip_seleccionada_gateway.get()

        if check_multiple_ethernet_adapters():
            print("Attention, Impossible to do the test, First, Save SETTINGS.")
            label_resultado.config(text=f"Attention\nImpossible to do the test\nFirst, Save SETTINGS.", fg="#FB5656", bg="#000000")


            return
       

        
        response_gateway = subprocess.call(['ping', '-n', '5', '-l', '12500', gateway]) 

        if response_gateway == 0:
            label_resultado.config(text=f" ══ SUCCESSFUL CONNECTION ══\n                        {gateway}", fg="#F0F0F0", bg="dark green")
            self.pings_erroneos = 0  # Reiniciamos el contador de pings incorrectos
        else:
            label_resultado.config(text=f" ═══ CONNECTION ERROR ═══\n                        {gateway}", fg="#F0F0F0", bg="dark red")
            self.pings_erroneos += 1  # Incrementamos el contador de pings incorrectos

        # Actualizar la barra de progreso
        progress_value.set(i / self.numero_pings * 100)

        if self.pings_erroneos < self.max_pings_erroneos and i < self.numero_pings:
            # Si el número de pings incorrectos es menor que el máximo permitido y aún quedan pings por enviar, continuar el test
            ventana.after(50, lambda: self.enviar_ping(i + 1))
        else:
            # Si se alcanza el número máximo de pings incorrectos o se envían todos los pings, detener el test
            progress_value.set(0)
            if self.pings_erroneos >= self.max_pings_erroneos:
                label_resultado.config(text=f"                    ██            ██\n                        ██    ██    \n                            ███        \n                        ██    ██        \n                    ██            ██", fg="#FB5656", bg="#000000")

            else:
                label_resultado.config(text=f"             ████      ██      ██\n           ██    ██    ██  ██ \n           ██    ██    █████ \n           ██    ██    ██  ██  \n             ████      ██      ██", fg="#21B428", bg="#000000")

            self.pings_erroneos = 0  # Reiniciar el contador de pings incorrectos








# Función para guardar las IPs y adaptador seleccionados
def guardar_ip_y_adaptador():
    # Desactivamos WiFi para trabajar correctamente solo con la red Ethernet
    wifi.disable()

    adaptador = adaptador_seleccionado.get()
    a = 'netsh interface set interface '
    c = ' admin=enable'
    d = a + '"' + adaptador + '"' + c
    dhcpCommand = d
    print(d)
    command = dhcpCommand.split()
    subprocess.run(command)

    ip_host = ip_seleccionada_host.get()
    ip_gateway = ip_seleccionada_gateway.get()
    adaptador = adaptador_seleccionado.get()
    label_resultado.config(text=f"ESTABLISHED COMMS ENVIRONMENT\n    → Host IP: {ip_host}\n    → Gateway IP: {ip_gateway}\n    → Adapter: {adaptador}", bg="#373737", fg="#21B428", font=("Calibri", 12))

    a = 'netsh interface ip set address name='
    c = ' static '
    mask = ' 255.255.255.0 '
    d = a + '"' + adaptador + '"' + c + ip_host + mask + ip_gateway
    dhcpCommand = d
    command = dhcpCommand.split()
    subprocess.run(command)
    delay = 4
    print("\n  > > > Configure Static IP with the Command [ ", d, " ]")
    adaptersSinEternetValida = adapters.copy()

    if adaptador in adaptersSinEternetValida:
        adaptersSinEternetValida.remove(adaptador)

    resultado_frame.actualizar_estado(adaptador, True)  # Actualiza el estado a Online solo para la interfaz actual
    resultado_frame.limpiar_widgets()

    if len(adaptersSinEternetValida) != 0:
        for x in adaptersSinEternetValida:
            a = 'netsh interface set interface '
            c = ' admin=disable'
            d = a + '"' + x + '"' + c
            dhcpCommand = d
            print(d)
            command = dhcpCommand.split()
            subprocess.run(command)

            resultado_frame.actualizar_estado(x, False)  # Actualiza el estado a Offline para la interfaz deshabilitada

    # Colorear solo el interior del círculo
    resultado_frame.widgets[adaptador]['canvas'].config(background='light green')


    # Actualizar la interfaz gráfica
    ventana.update()



            

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
    label_resultado.config(text=f" The IP is now Dynamic", bg="#373737", fg="#21B428")

    print("\n>>   Done !! - Now our ",adaptador," address is Dynamic: DHCP")

    wifi.enable()

    # Vamos a hacer el proceso inverso y habilitar las conexiones ethernet desabilitadas si las hubiera
    adaptador = adaptador_seleccionado.get()

    adaptersSinEternetValida = adapters  # Recogemos toda la lista de adaptadores de red
    
    

    if len(adaptersSinEternetValida) != 0:  # Si no hay ethernets que desabilitar saltamos este paso
        
        for x in adaptersSinEternetValida:       # Iteramos la lista de ethernets NO utilizadas     
            
            
            a='netsh interface set interface '
            c=' admin=enable'
            
            d=a+'"'+x+'"'+c
            dhcpCommand = d
            print(d)
            command = dhcpCommand.split()
            subprocess.run(command)






    adaptersCopy=adapters
    # Colorear solo el interior del círculo

    for x in adaptersCopy: 
        resultado_frame.widgets[x]['canvas'].config(background='light green')


    # Actualizar la interfaz gráfica
    ventana.update()













label_resultado = tk.Label(ventana, text="- COMMUNICATIONS ENVIRONMENT -", bg="#373737", fg="#21B428",width=33, height=5, relief="sunken", anchor="w", justify="left", wraplength=350, font=("Calibri", 12))
label_resultado.grid(row=7, column=0, columnspan=2, padx=35, sticky=tk.W, pady=10)

class ResultadoFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.widgets = {}  # Almacena los widgets creados dinámicamente
        self.inicializar_widgets()  # Llamamos a esta función para inicializar los widgets al inicio

    def inicializar_widgets(self):
        for i, adapter in enumerate(adapters):
            self.agregar_interfaz(adapter, True)  # Añadimos todas las interfaces como activas al inicio

    def agregar_interfaz(self, nombre_interfaz, online):
        color_interior = '#F0F0F0' if online else 'light green'
        color_exterior = self.master.cget('bg')  # Color de fondo de la ventana
        canvas = tk.Canvas(self, width=20, height=20, highlightthickness=0)
        
        # Crear un círculo relleno (interior) con color y un círculo exterior del color de la ventana
        canvas.create_oval(5, 5, 15, 15, fill=color_interior, outline=color_exterior)
        canvas.grid(row=len(self.widgets), column=0, padx=(0, 5))

        etiqueta = tk.Label(self, text=nombre_interfaz, font=("Calibri", 12), anchor="w", bg="#F0F0F0")
        etiqueta.grid(row=len(self.widgets), column=1, sticky=tk.W)

        # Agregar widgets al diccionario para poder actualizarlos más tarde
        self.widgets[nombre_interfaz] = {'canvas': canvas, 'label': etiqueta}



    def actualizar_estado(self, nombre_interfaz, online):
        if nombre_interfaz in self.widgets:
            color = 'light green' if online else '#F0F0F0'
            self.widgets[nombre_interfaz]['canvas'].config(bg=color)

    def limpiar_widgets(self):
        # Eliminar widgets huérfanos que ya no están asociados a interfaces
        for interfaz, widget_info in list(self.widgets.items()):
            if interfaz not in adapters:
                widget_info['canvas'].destroy()
                widget_info['label'].destroy()
                del self.widgets[interfaz]

resultado_frame = ResultadoFrame(ventana)
resultado_frame.grid(row=7, column=1, columnspan=2, padx=35, sticky=tk.W, pady=10)







ip_menu_host = tk.OptionMenu(ventana, ip_seleccionada_host, *ip_host)
ip_menu_host.config(bg="#F0F0F0", font=("Calibri", 12), width=15)
ip_menu_host.grid(row=3, column=2, padx=10, pady=10)

ip_menu_gateway = tk.OptionMenu(ventana, ip_seleccionada_gateway, *ip_gateway)
ip_menu_gateway.config(bg="#F0F0F0", font=("Calibri", 12), width=15)
ip_menu_gateway.grid(row=4, column=2, padx=10, pady=10)

adaptador_menu = tk.OptionMenu(ventana, adaptador_seleccionado, *adapters)
adaptador_menu.config(bg="#F0F0F0", font=("Calibri", 12), width=15)
adaptador_menu.grid(row=5, column=2, padx=10, pady=10)

boton_guardar = tk.Button(ventana, text="Save Settings", command=guardar_ip_y_adaptador, width=19, fg="green")
boton_guardar.config(bg="#F0F0F0", font=("Calibri", 12))
boton_guardar.grid(row=6, column=2, padx=10, pady=10)

test_ping = PingPong(20)

boton_ping = tk.Button(ventana, text="   Connectivity Check  🗸   ", command=test_ping.enviar_ping)
boton_ping.config(bg="#F0F0F0", fg="#006400", font=("Calibri", 12, "bold"))
boton_ping.grid(row=8, column=0)

button_dhcp = tk.Button(ventana, text='Restore Ethernet Adapters', command=restore_ethernets, width=25)
button_dhcp.config(bg="#F0F0F0", font=("Calibri", 12))
button_dhcp.grid(row=8, column=1, columnspan=2, pady=10)

boton_habilitar_wifi = tk.Button(ventana, text="E X I T  →░", command=salir, width=25)
boton_habilitar_wifi.config( fg="red", font=("Calibri", 12))
boton_habilitar_wifi.grid(row=11, column=1, columnspan=2)




# Lista de opciones para el CHECK
check_options = ["Normal Check", "Extended Check"]
check_seleccionado = tk.StringVar(ventana)
check_seleccionado.set(check_options[0])  # Establecer el valor inicial

# Desplegable Opción CHECK
check_menu = tk.OptionMenu(ventana, check_seleccionado, *check_options, command=actualizar_numero_pings)
check_menu.config(bg="#F0F0F0", font=("Calibri", 12), width=15)
check_menu.grid(row=11, column=0, pady=10)



# Eliminar esta etiqueta e intentar ajustar los desajustes que se producen
label_advertencia = tk.Label(ventana, text="By Fran Byte", anchor='w', bg="#F0F0F0", fg="#F0F0F0", font=("Calibri", 12))
label_advertencia.grid(row=14, column=0, padx=125, pady=0)



adaptersBoot=adapters
    # Colorear solo el interior del círculo

for x in adaptersBoot: 
    resultado_frame.widgets[x]['canvas'].config(background='light green')




ventana.mainloop()


