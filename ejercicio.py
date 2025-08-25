import tkinter as tk #importar libreria de tkinter
from tkinter import messagebox
 
def nuevoPaciente():
    ventanaRegistro=tk.Toplevel(ventanaPrincipal) #crea una ventana secundaria(independiente asociada a la ventana principal)
    ventanaRegistro.title("Registrode paciente")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="lightblue")
    #nombre
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre: ")
    nombreLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w",)
    entryNombre=tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
    entryNombre.configure(bg="white")
   
    direccionLabel=tk.Label(ventanaRegistro,text="Direccion: ")
    direccionLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w",)
    entryDireccion=tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    entryDireccion.configure(bg="white")
   
    telefonoLabel=tk.Label(ventanaRegistro,text="Telefono: ")
    telefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w",)
    entryTelefono=tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
    entryTelefono.configure(bg="white")
#Sexo(radiobutton)
    sexoLabel=tk.Label(ventanaRegistro, text="sexo:")
    sexoLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    sexo=tk.StringVar(value="masculino")
    sexo=tk.StringVar(value="femenino")
    rbMasculino=tk.Radiobutton(ventanaRegistro, text="masculino", variable=sexo, value="masculino")
    rbMasculino.grid(row=3, column=1, sticky="w")    
    rbFemenino=tk.Radiobutton(ventanaRegistro, text="femenino", variable=sexo, value="femenino")
    rbFemenino.grid(row=4, column=1, sticky="w")
   
    enfLabel=tk.Label(ventanaRegistro, text="enfermedades base")
    enfLabel.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    diabetes=tk.BooleanVar()
    hipertension=tk.BooleanVar()
    asma=tk.BooleanVar()
   
    cdDiabetes=tk.Checkbutton(ventanaRegistro,text="Diabetes", variable=diabetes)
    cdDiabetes.grid(row=5, column=1, sticky="w")
    cdHipertencion=tk.Checkbutton(ventanaRegistro,text="Hipertencion", variable=hipertension)
    cdHipertencion.grid(row=6, column=1, sticky="w")
    cdAsma=tk.Checkbutton(ventanaRegistro,text="Asma", variable=asma)
    cdAsma.grid(row=7, column=1, sticky="w")
   
    def registrarDatos():
        enfermedades=[]
        if diabetes.get():
            enfermedades.append("diabetes")
        if hipertension.get():
            enfermedades.append("hipertencion")
        if asma.get():
            enfermedades.append("asma")
        if len(enfermedades)>0:
            enfermedadesTextos=','.join(enfermedades)
        else:
            enfermedadesTextos='ninguna'
        info = (
            f"nombre:{entryNombre.get()}\n"
            f"Dirección:{entryDireccion.get()}\n"
            f"Telefono:{entryTelefono.get()}\n"
            f"sexo:{sexo.get()}\n"
            f"enfermedades:{enfermedadesTextos}\n"
            )
        messagebox.showinfo("Datos Registrados",info)
        ventanaRegistro.destroy()
    btnRegistrar=tk.Button(ventanaRegistro, text="datos registrados", command=registrarDatos)
    btnRegistrar.grid(row=9, column=0, columnspan=2, pady=15)
   
   
def buscarPaciente():
    messagebox.showinfo("Buscar paciente", "espacio para buscar paciente")
def eliminarPaciente():
    messagebox.showinfo("Eliminiar paciente", "espacio para eliminar paciente")  
    
    
#funcion para doctores
def nuevoDoctor():
    ventanaRegistro=tk.Toplevel(ventanaPrincipal) #crea una ventana secundaria(independiente asociada a la ventana principal)
    ventanaRegistro.title("Sistema de Registro de Doctores")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="lightblue")
    
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre completo : ")
    nombreLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w",)
    entryNombre=tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
    entryNombre.configure(bg="white")
    
    direccionLabel=tk.Label(ventanaRegistro,text="Direccion: ")
    direccionLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w",)
    entryDireccion=tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    entryDireccion.configure(bg="white")
   
    telefonoLabel=tk.Label(ventanaRegistro,text="Telefono: ")
    telefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w",)
    entryTelefono=tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
    entryTelefono.configure(bg="white")
    
    EspecialidadLabel=tk.Label(ventanaRegistro, text="Especialidad:")
    EspecialidadLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    Espacialidad=tk.StringVar(value="Pediatria")
    Espacialidad=tk.StringVar(value="Cardiologia")
    Espacialidad=tk.StringVar(value="Neurologia")
    rbPediatria=tk.Radiobutton(ventanaRegistro, text="pediatria", variable=Espacialidad, value="pediatria")
    rbPediatria.grid(row=3, column=1, sticky="w")    
    rbCardiologia=tk.Radiobutton(ventanaRegistro, text="Cardiologia", variable=Espacialidad, value="Cardiologia")
    rbCardiologia.grid(row=4, column=1, sticky="w")
    rbNeurologia=tk.Radiobutton(ventanaRegistro, text="Neurologia", variable=Espacialidad, value="Neurologia")
    rbNeurologia.grid(row=5, column=1, sticky="w")
    
    turnoLabel=tk.Label(ventanaRegistro, text="Disponibilidad")
    turnoLabel.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    mañana=tk.BooleanVar()
    tarde=tk.BooleanVar()
    noche=tk.BooleanVar()
   
    cdMañana=tk.Checkbutton(ventanaRegistro,text="Mañana", variable=mañana)
    cdMañana.grid(row=6, column=1, sticky="w")
    cdTarde=tk.Checkbutton(ventanaRegistro,text="Tarde", variable=tarde)
    cdTarde.grid(row=7, column=1, sticky="w")
    cdNoche=tk.Checkbutton(ventanaRegistro,text="Noche", variable=noche)
    cdNoche.grid(row=8, column=1, sticky="w")
    
    def registrarDatos():
        disponibilidad=[]
        if mañana.get():
            disponibilidad.append("diabetes")
        if tarde.get():
            disponibilidad.append("hipertencion")
        if noche.get():
            disponibilidad.append("asma")
        if len(disponibilidad)>0:
            DTextos=','.join(disponibilidad)
        else:
            DTextos='No tiene disponibilidad'
        info = (
            f"nombre:{entryNombre.get()}\n"
            f"Dirección:{entryDireccion.get()}\n"
            f"Telefono:{entryTelefono.get()}\n"
            f"sexo:{Espacialidad.get()}\n"
            f"enfermedades:{DTextos}\n"
            )
        messagebox.showinfo("Datos Registrados",info)
        ventanaRegistro.destroy()
    btnRegistrar=tk.Button(ventanaRegistro, text="datos registrados", command=registrarDatos)
    btnRegistrar.grid(row=9, column=0, columnspan=2, pady=15)
    
    
    
    
    
    
def buscarDoctor():
    messagebox.showinfo("Buscar Doctor", "espacio para buscar Doctor")
def eliminarDoctor():
    messagebox.showinfo("Eliminiar Doctor", "espacio para eliminar Doctor")
       
ventanaPrincipal = tk.Tk ()
ventanaPrincipal.title("Sistema de Registro de Pacientes")
ventanaPrincipal.geometry("600x400")
ventanaPrincipal.configure(bg="#ffffff")
 
#barra menu
barraMenu=tk.Menu(ventanaPrincipal)
ventanaPrincipal.config(menu=barraMenu)
#Menu pacientes
menuPacientes=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Pacientes", menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Paciente", command=nuevoPaciente)
menuPacientes.add_command(label="Buscar paciente", command=buscarPaciente)
menuPacientes.add_command(label="Eliminar Paciente", command=eliminarPaciente)
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir", command=ventanaPrincipal.quit)
#menu doctores
menuDoctores=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor", command=nuevoDoctor)
menuDoctores.add_command(label="Buscar doctor", command=buscarDoctor)
menuDoctores.add_command(label="Eliminar doctor", command=eliminarDoctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir", command=ventanaPrincipal.quit)
#menu ayuda
menuAyuda=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="ayuda",menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=lambda:messagebox.showinfo("Acerca de","Version 1.0-Sistema Biomedicina"))
ventanaPrincipal.mainloop()