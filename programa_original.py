# Importa o módulo pyodbc para conexão com o banco de dados
import pyodbc

# Importa o módulo tkinter para criar interfaces gráficas
from tkinter import *
from tkinter import ttk

#Função responsavel por criar um novo registro de usuário
def register():
    # Cria uma nova janela superior (Toplevel) chamada 'window4' para o cadastro.
    window1 = Toplevel(window3)
    window1.title("Sign up")
    window1.configure(bg="#ADD8E6")

    # Define as dimensões da janela de cadastro.
    width_window = 420
    height_window = 220

    # Obtém o tamanho da tela do usuário.
    width_screen = window1.winfo_screenwidth()
    height_screen = window1.winfo_screenheight()

    # Centraliza a janela no meio da tela.
    pos_x = (width_screen // 2) - (width_window // 2)
    pos_y = (height_screen // 2) - (height_window // 2)

    window1.geometry('{}x{}+{}+{}'.format(width_window, height_window, pos_x, pos_y))

    lbl1 = Label(window1, text="Create an account", font="Arial 14 bold", bg="#ADD8E6")
    lbl1.grid(row=0, column=0, columnspan=2, pady=10)

    lbl2 = Label(window1, text="Enter your username", font="Arial 12 bold", bg="#ADD8E6")
    lbl2.grid(row=1, column=0, sticky="e")

    lbl3 = Label(window1, text="Enter your password", font="Arial 12 bold", bg="#ADD8E6")
    lbl3.grid(row=2, column=0, sticky="e")

    # Cria campos de entrada para o nome de usuário e senha
    entry1 = Entry(window1, font="Arial 14")
    entry1.grid(row=1, column=1, pady=10, padx=10)

    entry2 = Entry(window1, show="*", font="Arial 14")
    entry2.grid(row=2, column=1, pady=10, padx=10)

    # Configuração dos campos dentro da tela
    for i in range(5):
        window1.grid_rowconfigure(i, weight=1)

    for i in range(2):
                window1.grid_columnconfigure(i, weight=1)

    #Conecta ao BD e realiza o INSERT do novo usuario
    def save():
        new_user = entry1.get()
        new_password = entry2.get()

        # Configuração da conexão com o banco de dados
        dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db")

        # Cria uma nova conexão com o banco de dados
        connection = pyodbc.connect(dadosConexao)

        # Cria um novo cursor para executar SQL na nova conexão
        cursor = connection.cursor()

        # Executa uma operação SQL para inserir os dados no banco de dados.
        cursor.execute("INSERT INTO Usuarios (Nome, Senha) VALUES (?, ?)", (new_user, new_password))

        # Grava as alterações no banco de dados.
        connection.commit()

        # Feche a janela de cadastro após a conclusão
        window1.destroy()

    #Botoes da tela de registro de usuário
    btn1 = Button(window1, text="Confirm", font=("Arial", 12), command=save)
    btn1.grid(row=3, column=1, columnspan=1, pady=10)

    btn2 = Button(window1, text="Cancel", font=("Arial", 12), 
                                 command=window1.destroy)
    btn2.grid(row=3, column=0, columnspan=1, pady=10)

    # Define as colunas 0 e 1 para ocupar todo o espaço disponível
    window1.grid_columnconfigure(0, weight=1)
    window1.grid_columnconfigure(1, weight=1)

# Função para verificar as credenciais do usuário
def user():
    # Realiza a conexão com o banco de dados usando pyodbc
    connection = pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db")

    # Abre um cursor para executar consultas SQL
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?", (username_entry.get(), password_entry.get()))

    # Recebe o resultado da consulta
    User = cursor.fetchone()

    #Aqui realizo um IF se o usuario é valido ele realiza todas a funcionalidades da aplicação
    #Caso contrário ele vai pro ELSE e retorna 'usuário invalido'
    if User:
        # Fecha a janela de login
        window3.destroy()

        # Configuração da conexão com o banco de dados
        dataConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db") 

        # Cria uma nova conexão com o banco de dados
        connection = pyodbc.connect(dataConexao)

        # Cria um novo cursor para executar SQL na nova conexão
        cursor = connection.cursor()

        # Seleciona a tabela de produtos no banco de dados
        connection.execute("SELECT * FROM Produtos")

        print("successfully connected")

        #Aqui é criado a tela principal e todas as suas configurações
        window2 = Tk()
        window2.title("Tela Principal")

        window2.configure(bg="#f5f5f5")
        window2.attributes("-fullscreen", True)

        Label(window2, text="Nome do Produto: ", font="Arial 16", bg="#f5f5f5").grid(row=0,column=2, padx=10, pady=10)
        name = Entry(window2, font="Arial 16")
        name.grid(row=0,column=3, padx=10, pady=10)

        Label(window2, text="Descrição do Produto: ", font="Arial 16", bg="#f5f5f5").grid(row=0,column=5, padx=10, pady=10)
        description = Entry(window2, font="Arial 16")
        description.grid(row=0,column=6, padx=10, pady=10)

        Label(window2, text="Produtos", font="Arial 16", fg="blue" , bg="#f5f5f5").grid(row=2,column=0, columnspan=10, padx=10, pady=10)

        def register_p():
            window4 = Toplevel(window2)
            window4.title("Register New Product")
            window4.configure(bg="#f5f5f5")

            width_window = 450
            height_window = 230

            #obter tamanho tela
            width_screen = window4.winfo_screenwidth()
            height_screen = window4.winfo_screenheight()

            #centralizar janela na tela
            pos_x  = (width_screen // 2) - (width_window // 2)
            pos_y  = (height_screen // 2) - (height_window // 2)

            window4.geometry('{}x{}+{}+{}'.format(width_window, height_window, pos_x, pos_y))

            border_style = {"borderwidth": 2, "relief": "groove"}

            Label(window4, text="Nome do Produto:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=10, sticky="w")
            name = Entry(window4, font=("Arial", 12), **border_style)
            name.grid(row=0, column=1, padx=10, pady=10)

            Label(window4, text="Descrição do Produto:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=10, sticky="w")
            description = Entry(window4, font=("Arial", 12), **border_style)
            description.grid(row=1, column=1, padx=10, pady=10)

            Label(window4, text="Preco do Produto:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=10, sticky="w")
            price = Entry(window4, font=("Arial", 12), **border_style)
            price.grid(row=2, column=1, padx=10, pady=10)

            for i in range(5):
                    window4.grid_rowconfigure(i, weight=1)

            for i in range(2):
                window4.grid_columnconfigure(i, weight=1)
            
            def save_p():
                register_new_product = (name.get(), description.get(), 
                                        price.get())

                 # Configuração da conexão com o banco de dados
                dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db")

                # Cria uma nova conexão com o banco de dados
                connection = pyodbc.connect(dadosConexao)

                #executa SQL para guardar no banco
                cursor.execute("INSERT INTO Produtos (Nome, Descricao, Preco) Values (?,?,?)", register_new_product)
                #grava no banco
                connection.commit()

                print("Dados Cadastrados com Sucesso!")

                #fecha a janela de cadastro
                window4.destroy()

                for i in treeview.get_children():
                    treeview.delete(i)

                cursor.execute("SELECT * FROM Produtos")

                #armazena valores da query
                valores = cursor.fetchall
                
                #adiciona valores na treeview
                for valor in valores():
                    #preenche linha
                    treeview.insert("", "end", values=(valor[0],valor[1],valor[2],valor[3],))


            btn1 = Button(window4, text="Salvar", font=("Arial", 12), command=save_p)
            btn1.grid(row=3,column=0, columnspan=2,padx=10,pady=10, sticky="NSEW")

            btn2 = Button(window4, text="Cancelar", font=("Arial", 12), 
                                     command=window4.destroy)
            btn2.grid(row=4,column=0, columnspan=2,padx=10,pady=10, sticky="NSEW")

        #Função para editar algum produto da treeview
        def edit(event):
            #obtem item selecionado
            select_item = treeview.selection()[0]

            #obtem valores
            select_values = treeview.item(select_item)['values']

            edit_window = Toplevel(window2)
            edit_window.title("Editar Produto")
            edit_window.configure(bg="#f5f5f5")

            width_window = 500
            height_window = 200

            #obter tamanho tela
            width_screen = edit_window.winfo_screenwidth()
            height_screen = edit_window.winfo_screenheight()

            #centralizar janela na tela
            pos_x  = (width_screen // 2) - (width_window // 2)
            pos_y  = (height_screen // 2) - (height_window // 2)

            edit_window.geometry('{}x{}+{}+{}'.format(width_window, height_window, pos_x, pos_y))

            border_style = {"borderwidth": 2, "relief": "groove"}

            Label(edit_window, text="Nome do Produto:", font=("Arial", 16), bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=10, sticky="w")
            name= Entry(edit_window, font=("Arial", 16), **border_style, bg="#f5f5f5", textvariable=StringVar(value=select_values[1]))
            name.grid(row=0, column=1, padx=10, pady=10)

            Label(edit_window, text="Descrição do Produto:", font=("Arial", 16), bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=10, sticky="w")
            description = Entry(edit_window, font=("Arial", 16), **border_style, bg="#f5f5f5", textvariable=StringVar(value=select_values[2]))
            description.grid(row=1, column=1, padx=10, pady=10)

            Label(edit_window, text="Preco do Produto:", font=("Arial", 16), bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=10, sticky="w")
            price = Entry(edit_window, font=("Arial", 16), **border_style, bg="#f5f5f5", textvariable=StringVar(value=select_values[3]))
            price.grid(row=2, column=1, padx=10, pady=10)

            for i in range(5):
                    edit_window.grid_rowconfigure(i, weight=1)

            for i in range(2):
                edit_window.grid_columnconfigure(i, weight=1)
            
            def saveEdit():
                #obtem os novos valores selecionados na treeview
                product = name.get()
                new_description = description.get()
                new_price = price.get()
                
                #atualiza itens
                treeview.item(select_item, values=(select_values[0], product, new_description, new_price))

                #executa SQL para guardar no banco
                cursor.execute("UPDATE Produtos SET Nome = ?, Descricao = ?, Preco = ? WHERE ID = ?", (product, new_description, new_price, select_values[0]))
                
                # Cria um novo cursor para executar SQL na nova conexão
            
                #grava no banco
                connection.commit()

                print("Dados Cadastrados com Sucesso!")

                #fecha a janela de cadastro
                edit_window.destroy()

                for i in treeview.get_children():
                    treeview.delete(i)

                cursor.execute("SELECT * FROM Produtos")

                    #armazena valores da query
                valores = cursor.fetchall
                
                #adiciona valores na treeview
                for valor in valores():
                    #preenche linha
                    treeview.insert("", "end", values=(valor[0],valor[1],valor[2],valor[3],))

            btn1 = Button(edit_window, text="Alterar", font=("Arial", 16), bg="#008000", fg="#ffffff", command=saveEdit)
            btn1.grid(row=4,column=0, padx=20,pady=20)

            def delete_product_treeview():
                #recupera o id do registro selecionado
                select_item = treeview.selection()[0]
                id_item = treeview.item(select_item)['values'][0]

                # Configuração da conexão com o banco de dados
                dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db")

                # Cria uma nova conexão com o banco de dados
                connection = pyodbc.connect(dadosConexao)

                #deleta registro
                cursor.execute("DELETE FROM Produtos WHERE ID = ?", (id_item))
                cursor = connection.cursor()
                connection.commit()

                #fecha a janela de edição
                edit_window.destroy()

                #refresh data
                for i in treeview.get_children():
                    treeview.delete(i)

                cursor.execute("SELECT * FROM Produtos")

                    #armazena valores da query
                valores = cursor.fetchall
                
                #adiciona valores na treeview
                for valor in valores():
                    #preenche linha
                    treeview.insert("", "end", values=(valor[0],valor[1],valor[2],valor[3],))

            btn_cancel_edit = Button(edit_window, text="Deletar", font=("Arial", 16), bg="#FF0000", fg="#ffffff", command=delete_product_treeview)
            btn_cancel_edit.grid(row=4,column=1, padx=20,pady=20)

        btn2 = Button(window2, text="Novo", command=register_p, font="Arial 26")
        btn2.grid(row=4,column=0, columnspan=4, sticky="NSEW", padx=20, pady=5)

        style = ttk.Style(window2)

        treeview = ttk.Treeview(window2, style="mystyle.Treeview")

        style.theme_use("default")

        style.configure("mystyle.Treeview", font=("Arial", 12))

        treeview = ttk.Treeview(window2, style="mystyle.Treeview", column=("ID", "Nome", "Descricao", "Preco"), show="headings", height=20)

        treeview.heading("ID", text="ID")
        treeview.heading("Nome", text="Nome do Produto")
        treeview.heading("Descricao", text="Descrição do Produto")
        treeview.heading("Preco", text="Preço do Produto")

        #primeira coluna = #0
        #NO = coluna nao estica para preencher espaço disponivel
        treeview.column("#0", width=0, stretch=NO)
        treeview.column("ID", width=100)
        treeview.column("Nome", width=300)
        treeview.column("Descricao", width=500)
        treeview.column("Preco", width=200)

        treeview.grid(row=3,column=0, columnspan=10, sticky="NSEW")

        for i in treeview.get_children():
                treeview.delete(i)

        cursor.execute("SELECT * FROM Produtos")

            #armazena valores da query
        valores = cursor.fetchall
        
        #adiciona valores na treeview
        for valor in valores():
            #preenche linha
            treeview.insert("", "end", values=(valor[0],valor[1],valor[2],valor[3],))

        treeview.bind("<Double-1>", edit)

        #configura janela para usar barra de menus
        menu_bar = Menu(window2)
        window2.configure(menu=menu_bar)

        menu_arquivo = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Menu", menu=menu_arquivo)

        #Cria opção menu cadastrar
        menu_arquivo.add_command(label="Cadastrar", command=register_p)

        #Cria opção menu Sair
        menu_arquivo.add_command(label="Sair", command=window2.destroy)

        #limpo dados da treeview
        def remove():
            for i in treeview.get_children():
                #deleto linha por linha
                treeview.delete(i)

        def filter_data(product_name, product_description):
            if not product_name.get() and not product_description.get():
                for i in treeview.get_children():
                    treeview.delete(i)

                cursor.execute("SELECT * FROM Produtos")

                    #armazena valores da query
                valores = cursor.fetchall
                
                #adiciona valores na treeview
                for valor in valores():
                    #preenche linha
                    treeview.insert("", "end", values=(valor[0],valor[1],valor[2],valor[3],))

                #se os campos estiverem vazios nao faz nada
                return
            
            sql = "SELECT * FROM Produtos"

            params = []

            if product_name.get():
                sql += " WHERE Nome LIKE ?"
                params.append('%' + product_name.get() + '%') 
            
            if product_description.get():
                if product_name.get():
                    sql += " AND "
                else:
                    sql += " WHERE"
                sql += " Descricao LIKE ?"
                params.append('%' + product_description.get() + '%')

            cursor.execute(sql, tuple(params))
            product = cursor.fetchall()

            #limpa os dados da treeview
            remove()

            #preenche preview com dados filtrados
            for data in product:
                treeview.insert('', 'end', values=(data[0], data[1],data[2],data[3]))

        name.bind('<KeyRelease>', lambda e: filter_data(name, description))
        description.bind('<KeyRelease>', lambda e: filter_data(name, description))

        #deleta registro
        def delete():
                #recupera o id do registro selecionado
                select_item = treeview.selection()[0]
                id_item = treeview.item(select_item)['values'][0]
                
                #deleta registro
                cursor.execute("DELETE FROM Produtos WHERE ID = ?", (id_item))

                connection.commit()

                #refresh data
                for i in treeview.get_children():
                    treeview.delete(i)

                cursor.execute("SELECT * FROM Produtos")

                    #armazena valores da query
                valores = cursor.fetchall
                
                #adiciona valores na treeview
                for valor in valores():
                    #preenche linha
                    treeview.insert("", "end", values=(valor[0],valor[1],valor[2],valor[3],))

        btn1 = Button(window2, text="Deletar", command=delete, font="Arial 26")
        btn1.grid(row=4,column=4, columnspan=4, sticky="NSEW", padx=20, pady=5)

        #Inicializa Janela
        window2.mainloop()

        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        connection.close()

    else:
        # Se a condição "if" anterior não for atendida, ou seja, se as credenciais de login forem incorretas
        # Cria um rótulo de aviso com texto "Nome de Usuário ou Senha incorretos" em vermelho
        msg_lbl = Label(window3, text="Incorrect username or password.", fg="red")
        msg_lbl.grid(row=3,column=0,columnspan=2)

# Cria a janela principal
window3 = Tk()
window3.title("Sign in")

# Configura janela principal
window3.configure(bg="#00008B")
width_window = 450
height_window = 300

# Obtém o tamanho da tela
width_screen = window3.winfo_screenwidth()
height_screen = window3.winfo_screenheight()

# Calcula a posição para centralizar a janela na tela
pos_x  = (width_screen // 2) - (width_window // 2)
pos_y  = (height_screen // 2) - (height_window // 2)

# Define as dimensões e posição da janela principal
window3.geometry('{}x{}+{}+{}'.format(width_window, height_window, pos_x, pos_y))

# Cria rótulos para título, nome de usuário e senha
title_lbl = Label(window3, text="SysControl", font="Arial 20", bg="#00008B", fg="#ffffff")
title_lbl.grid(row=0,column=0,columnspan=2, pady=20) 

username_lbl = Label(window3, text="Username", font="Arial 14 bold", bg="#00008B", fg="#ffffff")
username_lbl.grid(row=1,column=0,sticky="NSEW") #NSEW

password_lbl = Label(window3, text="Password", font="Arial 14 bold", bg="#00008B", fg="#ffffff")
password_lbl.grid(row=2,column=0,sticky="NSEW") #NSEW

# Cria campos de entrada para o nome de usuário e senha
username_entry = Entry(window3, font="Arial 14")
username_entry.grid(row=1,column=1,pady=10)

password_entry = Entry(window3, show="*",font="Arial 14")
password_entry.grid(row=2,column=1, pady=10)

btn1 = Button(window3, text="Create an account", font="Arial 12", bg="#eeeeee", command=register)
btn1.grid(row=4, column=0,columnspan=1, padx=20, pady=10, sticky="NSEW")

btn2 = Button(window3, text="Login", font="Arial 12", bg="#eeeeee", command=user)
btn2.grid(row=4, column=1,columnspan=2, padx=20, pady=10, sticky="NSEW")

btn3 = Button(window3, text="Exit", font="Arial 12", bg="#eeeeee", command=window3.destroy)
btn3.grid(row=5, column=0,columnspan=2, padx=20, pady=10, sticky="NSEW")

# Define a configuração de peso para as linhas e colunas da grade da tela de login
for i in range(5):
    window3.grid_rowconfigure(i, weight=1)
    window3.grid_rowconfigure(i, weight=1)

for i in range(2):
    window3.grid_columnconfigure(i, weight=1)

#Inicializa Janela
window3.mainloop()