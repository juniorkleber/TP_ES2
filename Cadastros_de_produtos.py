#modulo para conexão com o bd
import pyodbc

#modulo de intefaces graficas
from tkinter import *
from tkinter import ttk

def verifica_credenciais():
    #realiza conexao com o bd
    conexao = pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db")
    #abre um cursor para executar o sql
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?", (username_entry.get(), password_entry.get()))

    #recebe o resultado da query
    usuario = cursor.fetchone()

    if usuario:
        main_window.destroy()

        dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db") 

        #cria conexao
        conexao = pyodbc.connect(dadosConexao)

        #cusor para executar o sql
        cursor = conexao.cursor()

        #selecionar tabela
        conexao.execute("SELECT * FROM Produtos")

        print("conectado com sucesso")

        def list_data():
            for i in treeview.get_children():
                treeview.delete(i)

            cursor.execute("SELECT * FROM Produtos")

                #armazena valores da query
            valores = cursor.fetchall
            
            #adiciona valores na treeview
            for valor in valores():
                #preenche linha
                treeview.insert("", "end", values=(valor[0],valor[1],valor[2],valor[3],))


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


        def Cadastrar():
            
            register_window = Toplevel(window)
            register_window.title("Cadastrar Produto")
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

            Label(register_window, text="Nome do Produto:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=10, sticky="w")
            product_name_register = Entry(register_window, font=("Arial", 12), **border_style)
            product_name_register.grid(row=0, column=1, padx=10, pady=10)

            Label(register_window, text="Descrição do Produto:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=10, sticky="w")
            product_description_register = Entry(register_window, font=("Arial", 12), **border_style)
            product_description_register.grid(row=1, column=1, padx=10, pady=10)

            Label(register_window, text="Preco do Produto:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=10, sticky="w")
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
                conexao.commit()

                print("Dados Cadastrados com Sucesso!")

            

                #fecha a janela de cadastro
                register_window.destroy()

                list_data()


            btn_save_data = Button(register_window, text="Salvar", font=("Arial", 12), command=saveData)
            btn_save_data.grid(row=3,column=0, columnspan=2,padx=10,pady=10, sticky="NSEW")

            btn_cancel_data = Button(register_window, text="Cancelar", font=("Arial", 12), command=register_window.destroy)
            btn_cancel_data.grid(row=4,column=0, columnspan=2,padx=10,pady=10, sticky="NSEW")

        def edit_data(event):
            
            #obtem item selecionado
            select_item = treeview.selection()[0]

            #obtem valores
            select_values = treeview.item(select_item)['values']

            edit_window = Toplevel(window)
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
            product_name_edit= Entry(edit_window, font=("Arial", 16), **border_style, bg="#f5f5f5", textvariable=StringVar(value=select_values[1]))
            product_name_edit.grid(row=0, column=1, padx=10, pady=10)

            Label(edit_window, text="Descrição do Produto:", font=("Arial", 16), bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=10, sticky="w")
            product_description_edit = Entry(edit_window, font=("Arial", 16), **border_style, bg="#f5f5f5", textvariable=StringVar(value=select_values[2]))
            product_description_edit.grid(row=1, column=1, padx=10, pady=10)

            Label(edit_window, text="Preco do Produto:", font=("Arial", 16), bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=10, sticky="w")
            product_price_edit = Entry(edit_window, font=("Arial", 16), **border_style, bg="#f5f5f5", textvariable=StringVar(value=select_values[3]))
            product_price_edit.grid(row=2, column=1, padx=10, pady=10)

            for i in range(5):
                    edit_window.grid_rowconfigure(i, weight=1)

            for i in range(2):
                edit_window.grid_columnconfigure(i, weight=1)
            
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
                conexao.commit()

                print("Dados Cadastrados com Sucesso!")

                #fecha a janela de cadastro
                edit_window.destroy()

                list_data()


            btn_save_edit = Button(edit_window, text="Alterar", font=("Arial", 16), bg="#008000", fg="#ffffff", command=saveEdit)
            btn_save_edit.grid(row=4,column=0, padx=20,pady=20)

            def delete_register():
                #recupera o id do registro selecionado
                select_item = treeview.selection()[0]
                id_item = treeview.item(select_item)['values'][0]

                #deleta registro
                cursor.execute("DELETE FROM Produtos WHERE ID = ?", (id_item))

                conexao.commit()

                #fecha a janela de edição
                edit_window.destroy()

                #refresh data
                list_data()


            btn_cancel_edit = Button(edit_window, text="Deletar", font=("Arial", 16), bg="#FF0000", fg="#ffffff", command=delete_register)
            btn_cancel_edit.grid(row=4,column=1, padx=20,pady=20)

        btn_save = Button(window, text="Novo", command=Cadastrar, font="Arial 26")
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

        list_data()

        treeview.bind("<Double-1>", edit_data)


        #configura janela para usar barra de menus
        menu_bar = Menu(window)
        window.configure(menu=menu_bar)

        menu_arquivo = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Menu", menu=menu_arquivo)

        #Cria opção menu cadastrar
        menu_arquivo.add_command(label="Cadastrar", command=Cadastrar)

        #Cria opção menu Sair
        menu_arquivo.add_command(label="Sair", command=window.destroy)

        #limpo dados da treeview
        def removeData():
            for i in treeview.get_children():
                #deleto linha por linha
                treeview.delete(i)

        def filter_data(product_name, product_description):
            if not product_name.get() and not product_description.get():
                list_data()

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

        product_name.bind('<KeyRelease>', lambda e: filter_data(product_name, product_description))
        product_description.bind('<KeyRelease>', lambda e: filter_data(product_name, product_description))

        #deleta registro
        def delete():
                #recupera o id do registro selecionado
                select_item = treeview.selection()[0]
                id_item = treeview.item(select_item)['values'][0]

                #deleta registro
                cursor.execute("DELETE FROM Produtos WHERE ID = ?", (id_item))

                conexao.commit()

                #refresh data
                list_data()

        btn_delete = Button(window, text="Deletar", command=delete, font="Arial 26")
        btn_delete.grid(row=4,column=4, columnspan=4, sticky="NSEW", padx=20, pady=5)


        #Inicializa Janela
        window.mainloop()

        cursor.close()
        conexao.close()

    else:
        msg_lbl = Label(main_window, text="Nome de Usuário ou Senha incorretos", fg="red")
        msg_lbl.grid(row=3,column=0,columnspan=2)

#janela principal
main_window = Tk()
main_window.title("Tela de Login")

main_window.configure(bg="#f5f5f5")

width_window = 450
height_window = 300

#obter tamanho tela
width_screen = main_window.winfo_screenwidth()
height_screen = main_window.winfo_screenheight()

#centralizar janela na tela
pos_x  = (width_screen // 2) - (width_window // 2)
pos_y  = (height_screen // 2) - (height_window // 2)

main_window.geometry('{}x{}+{}+{}'.format(width_window, height_window, pos_x, pos_y))


#Label
title_lbl = Label(main_window, text="Tela de Login", font="Arial 20", fg="blue", bg="#f5f5f5")
title_lbl.grid(row=0,column=0,columnspan=2, pady=20) 

username_lbl = Label(main_window, text="Nome de Usuário", font="Arial 14 bold", bg="#f5f5f5")
username_lbl.grid(row=1,column=0,sticky="e") #NSEW

password_lbl = Label(main_window, text="Senha", font="Arial 14 bold", bg="#f5f5f5")
password_lbl.grid(row=2,column=0,sticky="e") #NSEW

#Entry
username_entry = Entry(main_window, font="Arial 14")
username_entry.grid(row=1,column=1,pady=10)

password_entry = Entry(main_window, show="*",font="Arial 14")
password_entry.grid(row=2,column=1, pady=10)

entrar_btn = Button(main_window, text="Entrar", font="Arial 14", command=verifica_credenciais)
entrar_btn.grid(row=4, column=0,columnspan=2, padx=20, pady=10, sticky="NSEW")

sair_btn = Button(main_window, text="Sair", font="Arial 14", command=main_window.destroy)
sair_btn.grid(row=5, column=0,columnspan=2, padx=20, pady=10, sticky="NSEW")


for i in range(5):
    main_window.grid_rowconfigure(i, weight=1)

for i in range(2):
    main_window.grid_columnconfigure(i, weight=1)

    
#Inicializa Janela
main_window.mainloop()