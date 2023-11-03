# Importa o módulo pyodbc para conexão com o banco de dados
import pyodbc

# Importa o módulo tkinter para criar interfaces gráficas
from tkinter import *
from tkinter import ttk

def register_new_user():
    # Cria uma nova janela superior (Toplevel) para o cadastro.
    register_user_window = Toplevel(login_window)
    register_user_window.title("Sign up")
    register_user_window.configure(bg="#ADD8E6")

    # Define as dimensões da janela de cadastro.
    width_window = 420
    height_window = 220

    # Obtém o tamanho da tela do usuário.
    width_screen = register_user_window.winfo_screenwidth()
    height_screen = register_user_window.winfo_screenheight()

    # Centraliza a janela no meio da tela.
    pos_x = (width_screen // 2) - (width_window // 2)
    pos_y = (height_screen // 2) - (height_window // 2)

    register_user_window.geometry('{}x{}+{}+{}'.format(width_window, height_window, pos_x, pos_y))

    title_lbl = Label(register_user_window, text="Create an account", font="Arial 14 bold", bg="#ADD8E6")
    title_lbl.grid(row=0, column=0, columnspan=2, pady=10)

    username_lbl = Label(register_user_window, text="Enter your username", font="Arial 12 bold", bg="#ADD8E6")
    username_lbl.grid(row=1, column=0, sticky="e")

    password_lbl = Label(register_user_window, text="Enter your password", font="Arial 12 bold", bg="#ADD8E6")
    password_lbl.grid(row=2, column=0, sticky="e")

    # Cria campos de entrada para o nome de usuário e senha
    new_username_entry = Entry(register_user_window, font="Arial 14")
    new_username_entry.grid(row=1, column=1, pady=10, padx=10)

    new_password_entry = Entry(register_user_window, show="*", font="Arial 14")
    new_password_entry.grid(row=2, column=1, pady=10, padx=10)

    def save_user():
        new_user = new_username_entry.get()
        new_password = new_password_entry.get()

        # Configuração da conexão com o banco de dados
        dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db")

        # Cria uma nova conexão com o banco de dados
        conexao = pyodbc.connect(dadosConexao)

        # Cria um novo cursor para executar SQL na nova conexão
        cursor = conexao.cursor()

        # Executa uma operação SQL para inserir os dados no banco de dados.
        cursor.execute("INSERT INTO Usuarios (Nome, Senha) VALUES (?, ?)", (new_user, new_password))

        # Grava as alterações no banco de dados.
        conexao.commit()

        # Feche a janela de cadastro após a conclusão
        register_user_window.destroy()

    btn_save_cadastro = Button(register_user_window, text="Confirm", font=("Arial", 12), command=save_user)
    btn_save_cadastro.grid(row=3, column=1, columnspan=1, pady=10)

    btn_cancel_cadastro = Button(register_user_window, text="Cancel", font=("Arial", 12), command=register_user_window.destroy)
    btn_cancel_cadastro.grid(row=3, column=0, columnspan=1, pady=10)

    # Define as colunas 0 e 1 para ocupar todo o espaço disponível
    register_user_window.grid_columnconfigure(0, weight=1)
    register_user_window.grid_columnconfigure(1, weight=1)



# Função para verificar as credenciais do usuário
def validate_user():
    # Realiza a conexão com o banco de dados usando pyodbc
    # Abre um cursor para executar consultas SQL
    conection = pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db")
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?", (username_entry.get(), password_entry.get()))

    # Recebe o resultado da consulta
    User = cursor.fetchone()

    if User:
        # Fecha a janela de login
        login_window.destroy()

        # Configuração da conexão com o banco de dados
        dataConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db") 

        # Cria uma nova conexão com o banco de dados
        conection = pyodbc.connect(dataConexao)

        # Cria um novo cursor para executar SQL na nova conexão
        cursor = conection.cursor()

        # Seleciona a tabela de produtos no banco de dados
        conection.execute("SELECT * FROM Produtos")

        print("successfully connected")

        def list_products():
            for i in treeview.get_children():
                treeview.delete(i)

            cursor.execute("SELECT * FROM Produtos")

                #armazena valores da query
            products = cursor.fetchall
            
            # Adiciona os produtos à TreeView
            for product in products:
                treeview.insert("", "end", values=(product[0], product[1], product[2], product[3]))

        window = Tk()
        window.title("Tela Principal")

        window.configure(bg="#f5f5f5")

        window.attributes("-fullscreen", True)

        Label(window, text="Nome do Produto: ", font="Arial 16", bg="#f5f5f5").grid(row=0,column=2, padx=10, pady=10)
        product_name = Entry(window, font="Arial 16")
        product_name.grid(row=0,column=3, padx=10, pady=10)

        Label(window, text="Descrição do Produto: ", font="Arial 16", bg="#f5f5f5").grid(row=0,column=5, padx=10, pady=10)
        product_description = Entry(window, font="Arial 16")
        product_description.grid(row=0,column=6, padx=10, pady=10)

        Label(window, text="Produtos", font="Arial 16", fg="blue" , bg="#f5f5f5").grid(row=2,column=0, columnspan=10, padx=10, pady=10)


        def register_new_product():
            
            register_window = Toplevel(window)
            register_window.title("Register New Product")
            register_window.configure(bg="#f5f5f5")

            width_window = 450
            height_window = 230

            #obter tamanho tela
            width_screen = register_window.winfo_screenwidth()
            height_screen = register_window.winfo_screenheight()

            #centralizar janela na tela
            pos_x  = (width_screen // 2) - (width_window // 2)
            pos_y  = (height_screen // 2) - (height_window // 2)

            register_window.geometry('{}x{}+{}+{}'.format(width_window, height_window, pos_x, pos_y))

            border_style = {"borderwidth": 2, "relief": "groove"}

            Label(register_window, text="Name:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=10, sticky="w")
            product_name_register = Entry(register_window, font=("Arial", 12), **border_style)
            product_name_register.grid(row=0, column=1, padx=10, pady=10)

            Label(register_window, text="Description:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=10, sticky="w")
            product_description_register = Entry(register_window, font=("Arial", 12), **border_style)
            product_description_register.grid(row=1, column=1, padx=10, pady=10)

            Label(register_window, text="Price:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=10, sticky="w")
            product_price_register = Entry(register_window, font=("Arial", 12), **border_style)
            product_price_register.grid(row=2, column=1, padx=10, pady=10)

            for i in range(5):
                    register_window.grid_rowconfigure(i, weight=1)

            for i in range(2):
                register_window.grid_columnconfigure(i, weight=1)
            
            def saveData():
                register_new_product = (product_name_register.get(), product_description_register.get(), product_price_register.get())

                #executa SQL para guardar no banco
                cursor.execute("INSERT INTO Produtos (Nome, Descricao, Preco) Values (?,?,?)", register_new_product)
                #grava no banco
                conection.commit()

                print("Dados Cadastrados com Sucesso!")

                #fecha a janela de cadastro
                register_window.destroy()

                list_products()

            btn_save_data = Button(register_window, text="Salvar", font=("Arial", 12), command=saveData)
            btn_save_data.grid(row=3,column=0, columnspan=2,padx=10,pady=10, sticky="NSEW")

            btn_cancel_data = Button(register_window, text="Cancelar", font=("Arial", 12), command=register_window.destroy)
            btn_cancel_data.grid(row=4,column=0, columnspan=2,padx=10,pady=10, sticky="NSEW")

        def edit_product(event):
            
            #obtem item selecionado
            select_item = treeview.selection()[0]

            #obtem valores
            select_values = treeview.item(select_item)['values']

            edit_product_window = Toplevel(window)
            edit_product_window.title("Editar Produto")
            edit_product_window.configure(bg="#f5f5f5")

            width_window = 500
            height_window = 200

            #obter tamanho tela
            width_screen = edit_product_window.winfo_screenwidth()
            height_screen = edit_product_window.winfo_screenheight()

            #centralizar janela na tela
            pos_x  = (width_screen // 2) - (width_window // 2)
            pos_y  = (height_screen // 2) - (height_window // 2)

            edit_product_window.geometry('{}x{}+{}+{}'.format(width_window, height_window, pos_x, pos_y))

            border_style = {"borderwidth": 2, "relief": "groove"}

            Label(edit_product_window, text="Product Name:", font=("Arial", 16), bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=10, sticky="w")
            product_name_edit= Entry(edit_product_window, font=("Arial", 16), **border_style, bg="#f5f5f5", textvariable=StringVar(value=select_values[1]))
            product_name_edit.grid(row=0, column=1, padx=10, pady=10)

            Label(edit_product_window, text="Product Description:", font=("Arial", 16), bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=10, sticky="w")
            product_description_edit = Entry(edit_product_window, font=("Arial", 16), **border_style, bg="#f5f5f5", textvariable=StringVar(value=select_values[2]))
            product_description_edit.grid(row=1, column=1, padx=10, pady=10)

            Label(edit_product_window, text="Product Price:", font=("Arial", 16), bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=10, sticky="w")
            product_price_edit = Entry(edit_product_window, font=("Arial", 16), **border_style, bg="#f5f5f5", textvariable=StringVar(value=select_values[3]))
            product_price_edit.grid(row=2, column=1, padx=10, pady=10)

            for i in range(5):
                    edit_product_window.grid_rowconfigure(i, weight=1)

            for i in range(2):
                edit_product_window.grid_columnconfigure(i, weight=1)
            
            def saveEdit():
                #obtem os novos valores selecionados na treeview
                product = product_name_edit.get()
                new_description = product_description_edit.get()
                new_price = product_price_edit.get()
                
                #atualiza itens
                treeview.item(select_item, values=(select_values[0], product, new_description, new_price))



                #executa SQL para guardar no banco
                cursor.execute("UPDATE Produtos SET Nome = ?, Descricao = ?, Preco = ? WHERE ID = ?", (product, new_description, new_price, select_values[0]))
                #grava no banco
                conection.commit()

                print("Data Registered Successfully!")

                #fecha a janela de cadastro
                edit_product_window.destroy()

                list_products()


            btn_save_edit = Button(edit_product_window, text="Alterar", font=("Arial", 16), bg="#008000", fg="#ffffff", command=saveEdit)
            btn_save_edit.grid(row=4,column=0, padx=20,pady=20)

            def delete_product_treeview():
                #recupera o id do registro selecionado
                select_item = treeview.selection()[0]
                id_item = treeview.item(select_item)['values'][0]

                #deleta registro
                cursor.execute("DELETE FROM Produtos WHERE ID = ?", (id_item))

                conection.commit()

                #fecha a janela de edição
                edit_product_window.destroy()

                #refresh data
                list_products()


            btn_cancel_edit = Button(edit_product_window, text="Deletar", font=("Arial", 16), bg="#FF0000", fg="#ffffff", command=delete_product_treeview)
            btn_cancel_edit.grid(row=4,column=1, padx=20,pady=20)

        btn_save = Button(window, text="Novo", command=register_new_product, font="Arial 26")
        btn_save.grid(row=4,column=0, columnspan=4, sticky="NSEW", padx=20, pady=5)

        style = ttk.Style(window)

        treeview = ttk.Treeview(window, style="mystyle.Treeview")

        style.theme_use("default")

        style.configure("mystyle.Treeview", font=("Arial", 12))

        treeview = ttk.Treeview(window, style="mystyle.Treeview", column=("ID", "Nome", "Descricao", "Preco"), show="headings", height=20)

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

        list_products()

        treeview.bind("<Double-1>", edit_product)


        #configura janela para usar barra de menus
        menu_bar = Menu(window)
        window.configure(menu=menu_bar)

        menu_arquivo = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Menu", menu=menu_arquivo)

        #Cria opção menu cadastrar
        menu_arquivo.add_command(label="Cadastrar", command=register_new_product)

        #Cria opção menu Sair
        menu_arquivo.add_command(label="Sair", command=window.destroy)

        #limpo dados da treeview
        def removeData():
            for i in treeview.get_children():
                #deleto linha por linha
                treeview.delete(i)

        def search_product(product_name, product_description):
            if not product_name.get() and not product_description.get():
                list_products()

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
            removeData()

            #preenche preview com dados filtrados
            for data in product:
                treeview.insert('', 'end', values=(data[0], data[1],data[2],data[3]))

        product_name.bind('<KeyRelease>', lambda e: search_product(product_name, product_description))
        product_description.bind('<KeyRelease>', lambda e: search_product(product_name, product_description))

        #deleta registro
        def delete():
                #recupera o id do registro selecionado
                select_item = treeview.selection()[0]
                id_item = treeview.item(select_item)['values'][0]

                #deleta registro
                cursor.execute("DELETE FROM Produtos WHERE ID = ?", (id_item))

                conection.commit()

                #refresh data
                list_products()

        btn_delete = Button(window, text="Deletar", command=delete, font="Arial 26")
        btn_delete.grid(row=4,column=4, columnspan=4, sticky="NSEW", padx=20, pady=5)


        #Inicializa Janela
        window.mainloop()

        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        conection.close()

    else:
        # Se a condição "if" anterior não for atendida, ou seja, se as credenciais de login forem incorretas
        # Cria um rótulo de aviso com texto "Nome de Usuário ou Senha incorretos" em vermelho
        msg_lbl = Label(login_window, text="Incorrect username or password.", fg="red")
        msg_lbl.grid(row=3,column=0,columnspan=2)

# Cria a janela principal
login_window = Tk()
login_window.title("Sign in")

# Configura janela principal
login_window.configure(bg="#00008B")
width_window = 450
height_window = 300

# Obtém o tamanho da tela
width_screen = login_window.winfo_screenwidth()
height_screen = login_window.winfo_screenheight()

# Calcula a posição para centralizar a janela na tela
pos_x  = (width_screen // 2) - (width_window // 2)
pos_y  = (height_screen // 2) - (height_window // 2)

# Define as dimensões e posição da janela principal
login_window.geometry('{}x{}+{}+{}'.format(width_window, height_window, pos_x, pos_y))

# Cria rótulos para título, nome de usuário e senha
title_lbl = Label(login_window, text="SysControl", font="Arial 20", bg="#00008B", fg="#ffffff")
title_lbl.grid(row=0,column=0,columnspan=2, pady=20) 

username_lbl = Label(login_window, text="Username", font="Arial 14 bold", bg="#00008B", fg="#ffffff")
username_lbl.grid(row=1,column=0,sticky="NSEW") #NSEW

password_lbl = Label(login_window, text="Password", font="Arial 14 bold", bg="#00008B", fg="#ffffff")
password_lbl.grid(row=2,column=0,sticky="NSEW") #NSEW

# Cria campos de entrada para o nome de usuário e senha
username_entry = Entry(login_window, font="Arial 14")
username_entry.grid(row=1,column=1,pady=10)

password_entry = Entry(login_window, show="*",font="Arial 14")
password_entry.grid(row=2,column=1, pady=10)

entrar_btn = Button(login_window, text="Create an account", font="Arial 12", bg="#eeeeee", command=register_new_user)
entrar_btn.grid(row=4, column=0,columnspan=1, padx=20, pady=10, sticky="NSEW")

entrar_btn = Button(login_window, text="Login", font="Arial 12", bg="#eeeeee", command=validate_user)
entrar_btn.grid(row=4, column=1,columnspan=2, padx=20, pady=10, sticky="NSEW")

sair_btn = Button(login_window, text="Exit", font="Arial 12", bg="#eeeeee", command=login_window.destroy)
sair_btn.grid(row=5, column=0,columnspan=2, padx=20, pady=10, sticky="NSEW")

# Define a configuração de peso para as linhas e colunas da grade da tela de login
for i in range(5):
    login_window.grid_rowconfigure(i, weight=1)
    login_window.grid_rowconfigure(i, weight=1)

for i in range(2):
    login_window.grid_columnconfigure(i, weight=1)

#Inicializa Janela
login_window.mainloop()