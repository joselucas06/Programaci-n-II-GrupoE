#importacion de librerias
import tkinter as tk
from tkinter import ttk,messagebox
from datetime import datetime
 
#funcion para enmascarar fecha
def enmascarar_fecha(texto):
    limpio="".join(filter(str.isdigit,texto))
    formato_final=""
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio) > 2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
   
    if fechaP.get() != formato_final:
        fechaP.delete(0,tk.END)
        fechaP.insert(0,formato_final)    
       
    if len (fechaP.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaP.get(),"%d-%m-%Y").date()
        edad=fecha=fecha_actual.year-fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
 
#Guardar el archivo
def guardar_en_archivo():
    with open("paciente. text", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|"
            f"{paciente['Genero']}|{paciente['Grupo Sanguineo']}|"
            f"{paciente['Tipo de Seguro']}|{paciente['Centro Medico']}\n")          
           
           
           
#Guardar el archivo doctores

def guardar_en_archivo_doctores():
    with open("doctores.txt", "w", encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(f"{doctor['Nombre']}|{doctor['Especialidad']}|{doctor['Edad']}|{doctor['Telefono']}\n")

def cargar_desde_archivo_doctores():
    try:
        with open("doctores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 4:
                    doctor = {
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "Edad": datos[2],
                        "Telefono": datos[3]
                    }
                    doctores_data.append(doctor)
        cargar_treeview_doctores()
    except FileNotFoundError:
        open("doctores.txt", "w", encoding="utf-8").close()
        
        
#lista de pacientes (inicialmente vacia)
paciente_data=[]
#funcion para registarar pacientes
def registrarPaciente():
    #crear diccionario con los datos ingresados
    paciente={
        "Nombre":nombreP.get(),
        "Fecha de Nacimiento":fechaP.get(),
        "Edad": edadVar.get(),
        "Genero": genero.get(),
        "Grupo Sanguineo": entryGrupoSanguineo.get(),
        "Tipo de Seguro": tipo_seguro.get(),
        "Centro Medico": centro_medico.get()
    }
    #Agregar pacientes a la lista
    paciente_data.append(paciente)
    #Linea modificada 07/09/2025
    guardar_en_archivo()
    # recargar treeview
    cargar_treeview()
    #funcion para cargar treview
   
   
def cargar_treeview():
    #Limpiar el treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
       
#insertar cada paciente
    for i, item in enumerate(paciente_data):
        treeview.insert(
            "","end", iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Genero"],
                item["Grupo Sanguineo"],
                item["Tipo de Seguro"],
                item["Centro Medico"]
            )
        )
 
def cargar_desde_archivo_pacientes():
    try:
        with open("paciente.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==7:
                    paciente={
                        "Nombre":datos[0],
                        "Fecha de Nacimiento":datos[1],
                        "Edad":datos[2],
                        "Genero":datos[3],
                        "Grupo Sanguineo":datos[4],
                        "Tipo de Seguro":datos[5],
                        "Centro Medico":datos[6]
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("paciente.txt", "w", encoding="utf-8").close()
                   
                   
 
#lista de doctores (inicialmente vacia)
doctores_data=[]
def registrarDoctores():
    doctor = {
        "Nombre": entry_nombreD.get(),
        "Especialidad": especialidad_var.get(),
        "Edad": spinbox_edadD.get(),
        "Telefono": entry_telefono.get()
    }
    doctores_data.append(doctor)
    guardar_en_archivo_doctores()
    cargar_treeview_doctores()
 
def cargar_treeview_doctores():
    for doctor in treeviewD.get_children():
        treeviewD.delete(doctor)
    for i, item in enumerate(doctores_data):
        treeviewD.insert("", "end", iid=str(i), values=(
            item["Nombre"],
            item["Especialidad"],
            item["Edad"],
            item["Telefono"]
        ))
 
       
#insertar cada paciente
    for i, item in enumerate(doctores_data):
        treeview.insert(
            "","end", iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["Edad"],
                item["Telefono"]
            )
        )
               
#crear ventana principal
ventana_principal= tk.Tk()
ventana_principal.title("Libro de pacientes y doctores")
ventana_principal.geometry("900x900")
 
#Crear contenedor Notebook(pesttañas)
pestañas=ttk.Notebook(ventana_principal)
 
#crear frames (uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
 
#Agregar pestañas al notebook
pestañas.add(frame_pacientes,text="Pacientes")
 
#Mostrar las pestañas en la ventaña
pestañas.pack(expand=True, fill="both")
 
#Crear pestaña doctores
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores,text="Doctores")
pestañas.pack(expand=True, fill="both")
 
#Nombre
labelNombre=tk.Label(frame_pacientes, text= "Nombre Completo:")
labelNombre.grid(row=0,column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1, sticky="w", pady=5, padx=5)
 
#Fecha de nacimiento
labelNacimiento=tk.Label(frame_pacientes, text= "Fecha de Nacimiento:")
labelNacimiento.grid(row=1,column=0, sticky="w", pady=5, padx=5)
validacion_fecha=ventana_principal.register(enmascarar_fecha)
fechaP=ttk.Entry(frame_pacientes, validate="key", validatecommand=(validacion_fecha,"%P"))
fechaP.grid(row=1,column=1, sticky="w", pady=5, padx=5)
 
#Edad (readonly)
labelEdad=tk.Label(frame_pacientes, text="Edad:")
labelEdad.grid(row=2,column=0, sticky="w", pady=5,padx=5)
edadVar=tk.StringVar()
edadP=tk.Entry(frame_pacientes,textvariable=edadVar,state="readonly")
edadP.grid(row=2, column=1, sticky="w",pady=5, padx=5)
 
#Genero
labelGenero=tk.Label(frame_pacientes, text="Genero:")
labelGenero.grid(row=3, column=0,sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino") #Valor por Defecto
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino",variable=genero, value="Femenino")
radioFemenino.grid(row=4,column=1, sticky="w",padx=5)
 
#Grupo sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", padx=5, pady=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5, column=1,sticky="w",padx=5,pady=5)
 
#Tipos de seguro
labelTipoSeguro=tk.Label(frame_pacientes, text="Tipo de seguro:")
labelTipoSeguro.grid(row=6, column=0, sticky="w", pady=5, padx=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")# valor por defaut
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Publico","Privado","Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6,column=1,sticky="w",pady=5,padx=5)
 
#CENTRO MEDICO
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de salud:")
labelCentroMedico.grid(row=7, column=0,sticky="w",padx=5, pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")#Valor por deafut
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central","Clinica Norte","Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w",padx=5,pady=5)
 
#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=8,column=0,columnspan=2, pady=5,sticky="w")
 
#Boton registrar
btn_registrar=tk.Button(btn_frame,text="Registrar", command=registrarPaciente)
btn_registrar.grid(row=0,column=0,padx=5)
 
#Boton eliminar
btn_eliminar= tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.grid(row=0,column=1,padx=5)
#crear Treeview para mostrar pacientes
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM"), show="headings")
#Definir encabezados
treeview.heading("Nombre",text="Nombre Completo")
treeview.heading("FechaN", text="Fecha Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS",text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Medico")
#Definir anchos de columnas
treeview.column("Nombre",width=120)
treeview.column("Edad", width=120, anchor="center")
treeview.column("Genero",width=50, anchor="center")
treeview.column("GrupoS",width=100,anchor="center")
treeview.column("TipoS",width=100,anchor="center")
treeview.column("CentroM",width=120)
#Ubicar el TreeView en la cuadricula
treeview.grid(row=7,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)
 
#Scrollbar vertical
scroll_y=ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7, column=2, sticky="ns")
 
#DOCTORES
#Nombre
label_nombreD = tk.Label(frame_doctores, text="Nombre:")
label_nombreD.grid(row=0, column=0, sticky="w", pady=5, padx=5)
entry_nombreD = tk.Entry(frame_doctores)
entry_nombreD.grid(row=0, column=1, sticky="w", pady=5, padx=5)
 
#Especialidad (Combobox)
label_especialidad = tk.Label(frame_doctores, text="Especialidad:")
label_especialidad.grid(row=1, column=0, sticky="w", pady=5, padx=5)
especialidad_var = tk.StringVar()
especialidad_var.set("Neurología")  # Valor por defecto
combo_especialidad = ttk.Combobox(frame_doctores,textvariable=especialidad_var, values=["Neurología", "Cardiología", "Pediatría", "Traumatología"])
combo_especialidad.grid(row=1, column=1, sticky="w", pady=5, padx=5)
 
#Edad con Spinbox
label_edadD = tk.Label(frame_doctores, text="Edad:")
label_edadD.grid(row=2, column=0, sticky="w", pady=5, padx=5)
spinbox_edadD = tk.Spinbox(frame_doctores, from_=1, to=100, state="readonly")
spinbox_edadD.grid(row=2, column=1, sticky="w", pady=5, padx=5)
 
#Teléfono
label_telefono = tk.Label(frame_doctores, text="Teléfono:")
label_telefono.grid(row=3, column=0, sticky="w", pady=5, padx=5)
entry_telefono = tk.Entry(frame_doctores)
entry_telefono.grid(row=3, column=1, sticky="w", pady=5, padx=5)
 
#Botones Registrar y Eliminar
btn_frameD = tk.Frame(frame_doctores)
btn_frameD.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")
 
btn_registrarD = tk.Button(btn_frameD, text="Registrar", bg="green", fg="white",command=registrarDoctores)
btn_registrarD.grid(row=0, column=0, padx=5)
 
btn_eliminarD = tk.Button(btn_frameD, text="Eliminar", bg="red", fg="white")
btn_eliminarD.grid(row=0, column=1, padx=5)
 
# Tabla Treeview para mostrar doctores
treeviewD = ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
treeviewD.heading("Nombre", text="Nombre")
treeviewD.heading("Especialidad", text="Especialidad")
treeviewD.heading("Edad", text="Edad")
treeviewD.heading("Telefono", text="Teléfono")
 
treeviewD.column("Nombre", width=150)
treeviewD.column("Especialidad", width=150)
treeviewD.column("Edad", width=50, anchor="center")
treeviewD.column("Telefono", width=100)
 
treeviewD.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
 
# Scrollbar vertical
scroll_yD = ttk.Scrollbar(frame_doctores, orient="vertical", command=treeviewD.yview)
treeviewD.configure(yscrollcommand=scroll_yD.set)
scroll_yD.grid(row=5, column=2, sticky="ns")
 
cargar_desde_archivo_pacientes()
cargar_desde_archivo_doctores()
ventana_principal.mainloop()