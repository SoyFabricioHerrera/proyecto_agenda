import tkinter as tk
from tkinter import simpledialog

# Clase para gestionar cada rubro
class Rubro:
    def __init__(self, ventana, nombre, eliminar_callback):
        self.frame = tk.Frame(ventana, bd=2, relief="groove", padx=10, pady=10)
        self.frame.pack(side="left", fill="both", expand=True)

        self.nombre = nombre
        self.eliminar_callback = eliminar_callback

        self.etiqueta = tk.Label(self.frame, text=nombre, font=("Arial", 12, "bold"))
        self.etiqueta.pack()

        self.entrada = tk.Entry(self.frame)
        self.entrada.pack()

        self.boton_agregar = tk.Button(self.frame, text="Agregar", command=self.agregar_elemento)
        self.boton_agregar.pack()

        self.boton_eliminar = tk.Button(self.frame, text="Eliminar seleccionado", command=self.eliminar_elemento)
        self.boton_eliminar.pack()

        self.boton_limpiar = tk.Button(self.frame, text="Limpiar lista", command=self.limpiar_lista)
        self.boton_limpiar.pack()
        ##Listbox se utiliza para mostrar una lista de elemento los cuales el usuario puede seleccionar##

        self.lista = tk.Listbox(self.frame)
        self.lista.pack(fill="both", expand=True)

        self.boton_eliminar_frame = tk.Button(self.frame, text="Eliminar Rubro", command=self.eliminar_frame)
        self.boton_eliminar_frame.pack()

    def agregar_elemento(self):
        item = self.entrada.get()
        if item:
            self.lista.insert(tk.END, item)
            self.entrada.delete(0, tk.END)

    def eliminar_elemento(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.lista.delete(seleccion)

    def limpiar_lista(self):
        self.lista.delete(0, tk.END)

    def eliminar_frame(self):
        self.frame.destroy()  # Destruir el frame y todos sus widgets
        self.eliminar_callback(self)  # Notificar a la aplicación principal para eliminar la referencia

# Función para agregar un nuevo rubro
def agregar_rubro():
    nombre_rubro = simpledialog.askstring("Nuevo Rubro", "Ingrese el nombre del rubro:")
    if nombre_rubro:
        rubro = Rubro(ventana, nombre_rubro, eliminar_rubro)
        rubros.append(rubro)

# Función para eliminar un rubro de la lista principal
def eliminar_rubro(rubro):
    rubros.remove(rubro)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Compras por Rubros Dinámicos")

# Botón para agregar nuevos rubros
boton_agregar_rubro = tk.Button(ventana, text="Agregar Nuevo Rubro", command=agregar_rubro)
boton_agregar_rubro.pack(side="top", pady=10)

# Lista para almacenar los rubros dinámicos
rubros = []

# Iniciar el bucle principal
ventana.mainloop()
