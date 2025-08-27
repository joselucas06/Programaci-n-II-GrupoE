import tkinter as tk
from tkinter import messagebox, ttk
 
def mostrarEdad():
    tk.messagebox.showinfo("Edad", f"La edad seleccionada es: {spin.get()}")
 
ventanaPrincipal=tk.Tk()
 
labelEdad=tk.Label(ventanaPrincipal, text="Edad:")
labelEdad.grid(row=0, column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(ventanaPrincipal, from_=1, to=100)
spin.grid(row=0, column=1, padx=10, pady=10)
boton=tk.Button(ventanaPrincipal, text="Obtener valor", command=lambda:mostrarEdad())
boton.grid(row=1, column=0, padx=10, pady=10)
 
ventanaPrincipal.mainloop()