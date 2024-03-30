import tkinter as tk
from tkinter import messagebox
import json

class SistemaCadastroDesktop:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro Prato Cidadão _ Prototipo ")

        # Variáveis de controle para os campos de entrada
        self.nome_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.numero_celular_var = tk.StringVar()
        self.numero_id_var = tk.StringVar()

        # Layout
        self.label_nome = tk.Label(root, text="Nome:")
        self.entry_nome = tk.Entry(root, textvariable=self.nome_var)

        self.label_email = tk.Label(root, text="Email:")
        self.entry_email = tk.Entry(root, textvariable=self.email_var)

        self.label_numero_celular = tk.Label(root, text="Número de Celular:")
        self.entry_numero_celular = tk.Entry(root, textvariable=self.numero_celular_var)

        self.label_numero_id = tk.Label(root, text="Número de ID:")
        self.entry_numero_id = tk.Entry(root, textvariable=self.numero_id_var)

        self.botao_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_usuario)
        self.botao_listar = tk.Button(root, text="Listar Usuários", command=self.listar_usuarios)

        # Posicionamento dos widgets usando grid
        self.label_nome.grid(row=0, column=0, sticky='e', padx=10, pady=10)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)
        self.label_email.grid(row=1, column=0, sticky='e', padx=10, pady=10)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)
        self.label_numero_celular.grid(row=2, column=0, sticky='e', padx=10, pady=10)
        self.entry_numero_celular.grid(row=2, column=1, padx=10, pady=10)
        self.label_numero_id.grid(row=3, column=0, sticky='e', padx=10, pady=10)
        self.entry_numero_id.grid(row=3, column=1, padx=10, pady=10)
        self.botao_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)
        self.botao_listar.grid(row=5, column=0, columnspan=2, pady=10)

        # Configurar o peso das linhas e colunas para tornar a interface responsiva
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)

        # Inicializar o sistema de cadastro
        self.sistema = SistemaCadastro("contatos.json")

    def cadastrar_usuario(self):
        nome = self.nome_var.get()
        email = self.email_var.get()
        numero_celular = self.numero_celular_var.get()
        numero_id = self.numero_id_var.get()

        if nome and email and numero_celular and numero_id:
            self.sistema.cadastrar_usuario(nome, email, numero_celular, numero_id)
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso.")
            self.nome_var.set("")
            self.email_var.set("")
            self.numero_celular_var.set("")
            self.numero_id_var.set("")
        else:
            messagebox.showwarning("Cadastro", "Por favor, preencha todos os campos.")

    def listar_usuarios(self):
        usuarios = self.sistema.listar_usuarios()
        messagebox.showinfo("Lista de Usuários", "\n".join(usuarios))

class Usuario:
    def __init__(self, nome, email, numero_celular, numero_id):
        self.nome = nome
        self.email = email
        self.numero_celular = numero_celular
        self.numero_id = numero_id

class SistemaCadastro:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.usuarios = self.carregar_usuarios()

    def carregar_usuarios(self):
        try:
            with open(self.arquivo, 'r') as file:
                usuarios = json.load(file)
                return [Usuario(user['nome'], user['email'], user['numero_celular'], user['numero_id']) for user in usuarios]
        except FileNotFoundError:
            return []

    def salvar_usuarios(self):
        with open(self.arquivo, 'w') as file:
            usuarios_serializados = [
                {'nome': user.nome, 'email': user.email, 'numero_celular': user.numero_celular, 'numero_id': user.numero_id}
                for user in self.usuarios
            ]
            json.dump(usuarios_serializados, file)

    def cadastrar_usuario(self, nome, email, numero_celular, numero_id):
        novo_usuario = Usuario(nome, email, numero_celular, numero_id)
        self.usuarios.append(novo_usuario)
        self.salvar_usuarios()

    def listar_usuarios(self):
        return [f'Nome: {usuario.nome}, Email: {usuario.email}, Número de Celular: {usuario.numero_celular}, Número de ID: {usuario.numero_id}' for usuario in self.usuarios]

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaCadastroDesktop(root)
    root.mainloop()
