
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
 

 
# Enmascara la fecha y calcula edad automáticamente
def enmascarar_fecha(texto):
    limpio = "".join(filter(str.isdigit, texto))
    formato_final = ""
    if len(limpio) > 8:
        limpio = limpio[:8]
    if len(limpio) > 4:
        formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio) > 2:
        formato_final = f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final = limpio
 
    # Actualizar campo si cambió
    if fechaP.get() != formato_final:
        fechaP.delete(0, tk.END)
        fechaP.insert(0, formato_final)
 
    # Calcular edad si fecha completa
    try:
        if len(fechaP.get()) == 10:
            fecha_actual = datetime.now().date()
            fecha_nacimiento = datetime.strptime(fechaP.get(), "%d-%m-%Y").date()
            edad = fecha_actual.year - fecha_nacimiento.year - (
                (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
            )
            edadVar.set(str(edad))
        else:
            edadVar.set("")
    except Exception:
        edadVar.set("")
    return True
 

 
def guardar_en_archivo():
    """Guarda la lista de pacientes en paciente.txt"""
    with open("paciente.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(
                f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|"
                f"{paciente['Genero']}|{paciente['Grupo Sanguineo']}|"
                f"{paciente['Tipo de Seguro']}|{paciente['Centro Medico']}\n"
            )
 
def guardar_en_archivo_doctores():
    """Guarda la lista de doctores en doctores.txt (nuevo formato con experiencia, genero, hospital)"""
    with open("doctores.txt", "w", encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(
                f"{doctor['Nombre']}|{doctor['Especialidad']}|{doctor['Experiencia']}|{doctor['Genero']}|{doctor['Hospital']}\n"
            )
 
def cargar_desde_archivo_pacientes():
    """Carga pacientes desde paciente.txt"""
    try:
        with open("paciente.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 7:
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Genero": datos[3],
                        "Grupo Sanguineo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Medico": datos[6]
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        # Crear archivo vacío si no existe
        open("paciente.txt", "w", encoding="utf-8").close()
 
def cargar_desde_archivo_doctores():
    """Carga doctores desde doctores.txt (formato nuevo)"""
    try:
        with open("doctores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 5:
                    doctor = {
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "Experiencia": datos[2],
                        "Genero": datos[3],
                        "Hospital": datos[4]
                    }
                    doctores_data.append(doctor)
        cargar_treeview_doctores()
    except FileNotFoundError:
        open("doctores.txt", "w", encoding="utf-8").close()
 

paciente_data = []
 
def registrarPaciente():
    if not nombreP.get().strip():
        messagebox.showwarning("Aviso", "Ingrese el nombre del paciente.")
        return
    paciente = {
        "Nombre": nombreP.get().strip(),
        "Fecha de Nacimiento": fechaP.get().strip(),
        "Edad": edadVar.get().strip(),
        "Genero": genero.get(),
        "Grupo Sanguineo": entryGrupoSanguineo.get().strip(),
        "Tipo de Seguro": tipo_seguro.get(),
        "Centro Medico": centro_medico.get()
    }
    paciente_data.append(paciente)
    guardar_en_archivo()
    cargar_treeview()
    limpiar_campos_paciente()
 
def cargar_treeview():
    # Limpiar el treeview de pacientes
    for item in treeview.get_children():
        treeview.delete(item)
    for i, item in enumerate(paciente_data):
        treeview.insert(
            "", "end", iid=str(i),
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
 
def eliminar_paciente():
    sel = treeview.selection()
    if not sel:
        messagebox.showinfo("Info", "Seleccione un paciente para eliminar.")
        return
    confirm = messagebox.askyesno("Confirmar", "¿Eliminar el paciente seleccionado?")
    if not confirm:
        return
    # eliminar todos los seleccionados (aunque normalmente 1)
    ids = sorted([int(i) for i in sel], reverse=True)
    for idx in ids:
        paciente_data.pop(idx)
    guardar_en_archivo()
    cargar_treeview()
 
def limpiar_campos_paciente():
    nombreP.delete(0, tk.END)
    fechaP.delete(0, tk.END)
    edadVar.set("")
    genero.set("Masculino")
    entryGrupoSanguineo.delete(0, tk.END)
    tipo_seguro.set("Publico")
    centro_medico.set("Hospital Central")
 
# ------------------ Doctores: registrar, cargar, eliminar ------------------
 
doctores_data = []
 
def registrarDoctores():
    # validaciones básicas
    if not entry_nombreD.get().strip():
        messagebox.showwarning("Aviso", "Ingrese el nombre del doctor.")
        return
    if not combo_especialidad.get().strip():
        messagebox.showwarning("Aviso", "Seleccione la especialidad.")
        return
    if not combo_hospital.get().strip():
        messagebox.showwarning("Aviso", "Seleccione el hospital.")
        return
 
    doctor = {
        "Nombre": entry_nombreD.get().strip(),
        "Especialidad": combo_especialidad.get().strip(),
        "Experiencia": spinbox_experiencia.get().strip(),
        "Genero": generoD.get(),
        "Hospital": combo_hospital.get().strip()
    }
    doctores_data.append(doctor)
    guardar_en_archivo_doctores()
    cargar_treeview_doctores()
    limpiar_campos_doctor()
 
def cargar_treeview_doctores():
    # Limpiar treeview de doctores
    for item in treeviewD.get_children():
        treeviewD.delete(item)
    for i, item in enumerate(doctores_data):
        treeviewD.insert("", "end", iid=str(i), values=(
            item["Nombre"],
            item["Especialidad"],
            item["Experiencia"],
            item["Genero"],
            item["Hospital"]
        ))
 
def eliminar_doctor():
    sel = treeviewD.selection()
    if not sel:
        messagebox.showinfo("Info", "Seleccione un doctor para eliminar.")
        return
    confirm = messagebox.askyesno("Confirmar", "¿Eliminar el doctor seleccionado?")
    if not confirm:
        return
    ids = sorted([int(i) for i in sel], reverse=True)
    for idx in ids:
        doctores_data.pop(idx)
    guardar_en_archivo_doctores()
    cargar_treeview_doctores()
 
def limpiar_campos_doctor():
    entry_nombreD.delete(0, tk.END)
    combo_especialidad.set("")
    spinbox_experiencia.delete(0, tk.END)
    spinbox_experiencia.insert(0, "0")
    generoD.set("Masculino")
    combo_hospital.set("")
 
# ------------------ Interfaz ------------------
 
ventana_principal = tk.Tk()
ventana_principal.title("Libro de pacientes y doctores")
ventana_principal.geometry("900x700")
 
# Notebook (pestañas)
pestañas = ttk.Notebook(ventana_principal)
 
# Frames por pestaña
frame_pacientes = ttk.Frame(pestañas)
frame_doctores = ttk.Frame(pestañas)
 
pestañas.add(frame_pacientes, text="Pacientes")
pestañas.add(frame_doctores, text="Doctores")
pestañas.pack(expand=True, fill="both")
 
# ------------------ Pestaña Pacientes ------------------
 
# Nombre
labelNombre = tk.Label(frame_pacientes, text="Nombre Completo:")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP = tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)
 
# Fecha de nacimiento con máscara
labelNacimiento = tk.Label(frame_pacientes, text="Fecha de Nacimiento:")
labelNacimiento.grid(row=1, column=0, sticky="w", pady=5, padx=5)
validacion_fecha = ventana_principal.register(enmascarar_fecha)
fechaP = ttk.Entry(frame_pacientes, validate="key", validatecommand=(validacion_fecha, "%P"))
fechaP.grid(row=1, column=1, sticky="w", pady=5, padx=5)
 
# Edad (readonly)
labelEdad = tk.Label(frame_pacientes, text="Edad:")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadVar = tk.StringVar()
edadP = tk.Entry(frame_pacientes, textvariable=edadVar, state="readonly")
edadP.grid(row=2, column=1, sticky="w", pady=5, padx=5)
 
# Género
labelGenero = tk.Label(frame_pacientes, text="Genero:")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero = tk.StringVar()
genero.set("Masculino")
radioMasculino = ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino = ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)
 
# Grupo sanguíneo
labelGrupoSanguineo = tk.Label(frame_pacientes, text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", padx=5, pady=5)
entryGrupoSanguineo = tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5, column=1, sticky="w", padx=5, pady=5)
 
# Tipo de seguro
labelTipoSeguro = tk.Label(frame_pacientes, text="Tipo de seguro:")
labelTipoSeguro.grid(row=6, column=0, sticky="w", pady=5, padx=5)
tipo_seguro = tk.StringVar()
tipo_seguro.set("Publico")
comboTipoSeguro = ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro, state="readonly")
comboTipoSeguro.grid(row=6, column=1, sticky="w", pady=5, padx=5)
 
# Centro médico
labelCentroMedico = tk.Label(frame_pacientes, text="Centro de salud:")
labelCentroMedico.grid(row=7, column=0, sticky="w", padx=5, pady=5)
centro_medico = tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico = ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico, state="readonly")
comboCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5)
 
# Botones pacientes
btn_frame = tk.Frame(frame_pacientes)
btn_frame.grid(row=8, column=0, columnspan=2, pady=5, sticky="w")
btn_registrar = tk.Button(btn_frame, text="Registrar", command=registrarPaciente)
btn_registrar.grid(row=0, column=0, padx=5)
btn_eliminar = tk.Button(btn_frame, text="Eliminar", command=eliminar_paciente, bg="red", fg="white")
btn_eliminar.grid(row=0, column=1, padx=5)
 
# Treeview pacientes
treeview = ttk.Treeview(frame_pacientes, columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM"), show="headings")
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Medico")
 
treeview.column("Nombre", width=160)
treeview.column("FechaN", width=100, anchor="center")
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=80, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=140)
 
treeview.grid(row=9, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
 
# Scrollbar vertical pacientes
scroll_y = ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=9, column=2, sticky="ns")
 
 
# Nombre
label_nombreD = tk.Label(frame_doctores, text="Nombre:")
label_nombreD.grid(row=0, column=0, sticky="w", pady=5, padx=5)
entry_nombreD = tk.Entry(frame_doctores)
entry_nombreD.grid(row=0, column=1, sticky="w", pady=5, padx=5)
 
# Especialidad (Combobox)
label_especialidad = tk.Label(frame_doctores, text="Especialidad:")
label_especialidad.grid(row=1, column=0, sticky="w", pady=5, padx=5)
especialidad_var = tk.StringVar()
combo_especialidad = ttk.Combobox(frame_doctores, textvariable=especialidad_var,
                                  values=["Neurología", "Cardiología", "Pediatría", "Traumatología", "Medicina General"],
                                  state="readonly")
combo_especialidad.grid(row=1, column=1, sticky="w", pady=5, padx=5)
 
# Años de experiencia (Spinbox)
label_experiencia = tk.Label(frame_doctores, text="Años Experiencia:")
label_experiencia.grid(row=2, column=0, sticky="w", pady=5, padx=5)
spinbox_experiencia = tk.Spinbox(frame_doctores, from_=0, to=60, state="readonly", width=5)
spinbox_experiencia.delete(0, tk.END)
spinbox_experiencia.insert(0, "0")
spinbox_experiencia.grid(row=2, column=1, sticky="w", pady=5, padx=5)
 
# Género doctores
label_generoD = tk.Label(frame_doctores, text="Género:")
label_generoD.grid(row=3, column=0, sticky="w", pady=5, padx=5)
generoD = tk.StringVar(value="Masculino")
radioMasculinoD = ttk.Radiobutton(frame_doctores, text="Masculino", variable=generoD, value="Masculino")
radioMasculinoD.grid(row=3, column=1, sticky="w", padx=5)
radioFemeninoD = ttk.Radiobutton(frame_doctores, text="Femenino", variable=generoD, value="Femenino")
radioFemeninoD.grid(row=4, column=1, sticky="w", padx=5)
 
# Hospital (Combobox)
label_hospital = tk.Label(frame_doctores, text="Hospital:")
label_hospital.grid(row=5, column=0, sticky="w", pady=5, padx=5)
hospital_var = tk.StringVar()
combo_hospital = ttk.Combobox(frame_doctores, textvariable=hospital_var,
                              values=["Hospital Central", "Clinica Norte", "Centro Sur", "Clínica Vida"],
                              state="readonly")
combo_hospital.grid(row=5, column=1, sticky="w", pady=5, padx=5)
 
# Botones Doctores
btn_frameD = tk.Frame(frame_doctores)
btn_frameD.grid(row=6, column=0, columnspan=2, pady=10, sticky="w")
btn_registrarD = tk.Button(btn_frameD, text="Registrar", bg="green", fg="white", command=registrarDoctores)
btn_registrarD.grid(row=0, column=0, padx=5)
btn_eliminarD = tk.Button(btn_frameD, text="Eliminar", bg="red", fg="white", command=eliminar_doctor)
btn_eliminarD.grid(row=0, column=1, padx=5)
 
# Treeview doctores
treeviewD = ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Experiencia", "Genero", "Hospital"), show="headings")
treeviewD.heading("Nombre", text="Nombre")
treeviewD.heading("Especialidad", text="Especialidad")
treeviewD.heading("Experiencia", text="Años Exp.")
treeviewD.heading("Genero", text="Género")
treeviewD.heading("Hospital", text="Hospital")
 
treeviewD.column("Nombre", width=180)
treeviewD.column("Especialidad", width=140)
treeviewD.column("Experiencia", width=80, anchor="center")
treeviewD.column("Genero", width=80, anchor="center")
treeviewD.column("Hospital", width=160)
 
treeviewD.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
 
# Scrollbar vertical doctores
scroll_yD = ttk.Scrollbar(frame_doctores, orient="vertical", command=treeviewD.yview)
treeviewD.configure(yscrollcommand=scroll_yD.set)
scroll_yD.grid(row=7, column=2, sticky="ns")
 

 
cargar_desde_archivo_pacientes()
cargar_desde_archivo_doctores()
ventana_principal.mainloop()