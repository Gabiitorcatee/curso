import tkinter as tk
from tkinter import messagebox
from dados import adicionar_planetas, remover_planetas, listar_planetas, buscar_planetas, editar_planetas
from planetas import planetas


def adicionar():
    adicionar_planetas()
    messagebox.showinfo("Informação", "Planeta adicionado com sucesso!")

def remover():
    remover_planetas()
    messagebox.showinfo("Informação", "Planeta removido com sucesso!")

def listar():
    resultado = listar_planetas()
    messagebox.showinfo("Planetas", resultado)

def buscar():
    buscar_planetas()
    
def editar():
    editar_planetas()
    messagebox.showinfo("Informação", "Planeta editado com sucesso!")

# Configuração da janela principal
root = tk.Tk()
root.title("CRUD Planetas")
root.geometry("400x300")

# Botões da interface
btn_adicionar = tk.Button(root, text="Adicionar Planeta", command=adicionar)
btn_adicionar.pack(pady=10)

btn_remover = tk.Button(root, text="Remover Planeta", command=remover)
btn_remover.pack(pady=10)

btn_listar = tk.Button(root, text="Listar Planetas", command=listar)
btn_listar.pack(pady=10)

btn_buscar = tk.Button(root, text="Buscar Planeta", command=buscar)
btn_buscar.pack(pady=10)

btn_editar = tk.Button(root, text="Editar Planeta", command=editar)
btn_editar.pack(pady=10)

# Iniciar a aplicação
root.mainloop()
