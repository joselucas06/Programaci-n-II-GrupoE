import tkinter as tk
from tkinter import ttk,messagebox
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Libro de Pacientes y Doctores")
ventanaPrincipal.geometry("400x600")

#crear contenedor notebook(pestañas)
pestañas=ttk.Notebook(ventanaPrincipal)
#crear frames
frame_pacientes=ttk.Frame(pestañas)
pestañas.add(frame_pacientes,text="Pacientes")
pestañas.pack(expand=True,fill="both")



nombreLabel=tk.Label(frame_pacientes,text="Nombre completo : ")
nombreLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w",)
entryNombre=tk.Entry(frame_pacientes)
entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
entryNombre.configure(bg="white")

labelFechaN=tk.Label(frame_pacientes,text="Fecha de Nacimiento : ")
labelFechaN.grid(row=1, column=0, padx=5, pady=5, sticky="w",)
fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1,column=1,sticky="W",padx=5,pady=5)

labelEdad=tk.Label(frame_pacientes,text="Edad:")
labelEdad.grid(row=2,column=0,sticky="W",padx=5,pady=5)
edadP=tk.Entry(frame_pacientes,state="readonly")
edadP.grid(row=2,column=1,sticky="w",padx=5,pady=5)

labelGenero=tk.Label(frame_pacientes,text="Genero:")
labelGenero.grid(row=3,column=0,sticky="w",padx=5,pady=5)

genero=tk.StringVar()
genero.set("masculino")
radiomasculino=ttk.Radiobutton(frame_pacientes,text="Masculino", variable=genero,value="Masculino")
radiomasculino.grid(row=3,column=1,sticky="w",padx=5)
radiofemenino=ttk.Radiobutton(frame_pacientes,text="Femenino", variable=genero,value="Femenino")
radiofemenino.grid(row=4,column=1,sticky="w",padx=5)

labelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5,column=0,sticky="w",padx=5,pady=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5,column=1,sticky="w",padx=5,pady=5)

labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de Seguro")
labelTipoSeguro.grid(row=6,column=0,sticky="w",padx=5,pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")
combotipoSeguro=ttk.Combobox(frame_pacientes,values=["Publico","Privado","Ninguno"],textvariable=tipo_seguro)
combotipoSeguro.grid(row=6,column=1,sticky="W",padx=5,pady=5)
labelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud:")
labelCentroMedico.grid(row=7,column=0,sticky="W",padx=5,pady=5)
centroMedico=tk.StringVar()
centroMedico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(frame_pacientes,values=["Hospital Central","Clinica Norte","Centro Sur"],textvariable=centroMedico)
comboCentroMedico.grid(row=7,column=1,sticky="w",padx=5,pady=5)



#frame doctores
frame_Doctores=ttk.Frame(pestañas)
pestañas.add(frame_Doctores,text="Doctores")
pestañas.pack(expand=True,fill="both")


ventanaPrincipal.mainloop()