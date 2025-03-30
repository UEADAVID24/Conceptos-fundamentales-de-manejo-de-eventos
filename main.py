import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese una tarea válida.")

def marcar_completada():
    seleccion = lista_tareas.curselection()
    if seleccion:
        indice = seleccion[0]
        tarea = lista_tareas.get(indice)
        if not tarea.startswith("✔"):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, f"✔ {tarea}")
    else:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion[0])
    else:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

def editar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        indice = seleccion[0]
        tarea_actual = lista_tareas.get(indice)
        entrada_tarea.delete(0, tk.END)
        entrada_tarea.insert(0, tarea_actual)
        lista_tareas.delete(indice)
    else:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para editar.")

def agregar_con_enter(event):
    agregar_tarea()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x450")

# Entrada de texto
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_con_enter)

# Botones
btn_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

btn_editar = tk.Button(root, text="Editar Tarea", command=editar_tarea)
btn_editar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(root, width=50, height=15)
lista_tareas.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()

