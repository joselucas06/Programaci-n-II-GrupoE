import tkinter as tk #importar libreria de tkinter
from tkinter import messagebox
    
    
    
ventanaPrincipal = tk.Tk ()
ventanaPrincipal.title("Sistema de Registro de Doctores")
ventanaPrincipal.geometry("600x400")
ventanaPrincipal.configure(bg="#ffffff")
  
nombreLabel=tk.Label(ventanaPrincipal,text="Nombre completo : ")
nombreLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w",)
entryNombre=tk.Entry(ventanaPrincipal)
entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
entryNombre.configure(bg="white")
    
direccionLabel=tk.Label(ventanaPrincipal,text="Direccion: ")
direccionLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w",)
entryDireccion=tk.Entry(ventanaPrincipal)
entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
entryDireccion.configure(bg="white")
   
telefonoLabel=tk.Label(ventanaPrincipal,text="Telefono: ")
telefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w",)
entryTelefono=tk.Entry(ventanaPrincipal)
entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
entryTelefono.configure(bg="white")
    
EspecialidadLabel=tk.Label(ventanaPrincipal, text="Especialidad:")
EspecialidadLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
Espacialidad=tk.StringVar(value="Pediatria")
Espacialidad=tk.StringVar(value="Cardiologia")
Espacialidad=tk.StringVar(value="Neurologia")
rbPediatria=tk.Radiobutton(ventanaPrincipal, text="pediatria", variable=Espacialidad, value="pediatria")
rbPediatria.grid(row=3, column=1, sticky="w")    
rbCardiologia=tk.Radiobutton(ventanaPrincipal, text="Cardiologia", variable=Espacialidad, value="Cardiologia")
rbCardiologia.grid(row=4, column=1, sticky="w")
rbNeurologia=tk.Radiobutton(ventanaPrincipal, text="Neurologia", variable=Espacialidad, value="Neurologia")
rbNeurologia.grid(row=5, column=1, sticky="w")
    
turnoLabel=tk.Label(ventanaPrincipal, text="Disponibilidad")
turnoLabel.grid(row=6, column=0, padx=10, pady=5, sticky="w")
mañana=tk.BooleanVar()
tarde=tk.BooleanVar()
noche=tk.BooleanVar()
   
cdMañana=tk.Checkbutton(ventanaPrincipal,text="Mañana", variable=mañana)
cdMañana.grid(row=6, column=1, sticky="w")
cdTarde=tk.Checkbutton(ventanaPrincipal,text="Tarde", variable=tarde)
cdTarde.grid(row=7, column=1, sticky="w")
cdNoche=tk.Checkbutton(ventanaPrincipal,text="Noche", variable=noche)
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
            f"Nombre:{entryNombre.get()}\n"
            f"Dirección:{entryDireccion.get()}\n"
            f"Telefono:{entryTelefono.get()}\n"
            f"Especialidad:{Espacialidad.get()}\n"
            f"Disponibilidad:{DTextos}\n"
            )
    messagebox.showinfo("Datos Registrados",info)
    ventanaPrincipal.destroy()
btnRegistrar=tk.Button(ventanaPrincipal, text="datos registrados", command=registrarDatos)
btnRegistrar.grid(row=9, column=0, columnspan=2, pady=15)
ventanaPrincipal.mainloop()