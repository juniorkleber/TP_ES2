from tkinter import Tk, Button, Entry, Label, ttk, Toplevel, Menu
import pyodbc

class ProductInterface:
    def __init__(self, main_window):
        self.main_window = main_window
        self.setup_ui()

    def setup_ui(self):
        self.create_product_widgets()
        self.create_treeview()
        # Outros componentes da interface podem ser configurados aqui

    def create_product_widgets(self):
        # Configuração de widgets para adicionar, editar e excluir produtos
        pass

    def create_treeview(self):
        self.treeview = ttk.Treeview(self.main_window, columns=("ID", "Nome", "Descricao", "Preco"), show="headings")
        # Configuração das colunas, cabeçalhos, etc.
        self.treeview.grid(row=3, column=0, columnspan=10, sticky="NSEW")

    def list_products(self):
        # Operações para listar os produtos na TreeView
        pass

    def register_new_product(self):
        # Operações para registrar um novo produto
        pass

    def edit_product(self, event):
        # Operações para editar um produto
        pass

    def delete_product_treeview(self):
        # Operações para deletar um produto da TreeView
        pass

    def search_product(self, product_name, product_description):
        # Operações para buscar produtos com base no nome e descrição
        pass

def register_new_user(login_window):
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


def open_main_interface():
    # Cria uma nova janela para a tela principal
    main_window = Tk()
    main_window.title("SysControl")
    main_window.configure(bg="#eeeeee")
    main_window.attributes("-fullscreen", True)

    #Configura Janela de atalhos
    menu_bar = Menu(main_window)
    main_window.configure(menu=menu_bar)

    menu_arquivo = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Menu", menu=menu_arquivo)

    #Cria opção menu Cadastrar
    menu_arquivo.add_command(label="Cadastrar")

    #Cria opção menu Sair
    menu_arquivo.add_command(label="Sair", command=main_window.destroy)

    # Cria rótulos e campos de entrada para nome e descrição do produto
    Label(main_window, text="Search by", font="Arial 14", bg="#eeeeee").grid(row=0,column=1, padx=10, pady=10)

    Label(main_window, text="Product Name: ", font="Arial 14", bg="#eeeeee").grid(row=0,column=2, padx=10, pady=10)
    product_name = Entry(main_window, font="Arial 14")
    product_name.grid(row=0,column=3, padx=10, pady=10)

    Label(main_window, text="Product Description: ", font="Arial 14", bg="#eeeeee").grid(row=0,column=5, padx=10, pady=10)
    product_description = Entry(main_window, font="Arial 14")
    product_description.grid(row=0,column=6, padx=10, pady=10)

    Label(main_window, text="All Products", font="Arial 18 bold", fg="black" , bg="#eeeeee").grid(row=2,column=0, columnspan=10, padx=10, pady=10)

    btn_save = Button(main_window, text="New Product", font="Arial 26")
    btn_save.grid(row=4,column=0, columnspan=4, sticky="NSEW", padx=20, pady=5)

    # Cria um botão "Deletar" na janela que chama a função delete() quando clicado
    btn_delete = Button(main_window, text="Delete", font="Arial 26")
    btn_delete.grid(row=4,column=4, columnspan=4, sticky="NSEW", padx=20, pady=5)
    

    # Cria a conexão com o banco de dados
    connection = pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db")

    # Cria uma instância da classe ProductInterface
    product_interface = ProductInterface(main_window, connection)

    # Mantém a janela principal aberta
    main_window.mainloop()

    # Feche a conexão com o banco de dados após fechar a janela principal
    connection.close()

def validate_user(username, password):
    # Sua lógica para validar o usuário aqui
    # Retorne True se as credenciais forem válidas, caso contrário, retorne False
    conection = pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto.db")
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?", (username, password))
    user = cursor.fetchone()
    
    if user:
        return True
    else:
        return False

def show_login_window():
    # Cria a janela principal
    login_window = Tk()
    login_window.title("Sign in")

    def show_register_window():
        register_new_user(login_window)

    def verify_login():
        username = username_entry.get()
        password = password_entry.get()

        # Validação das credenciais
        if validate_user(username, password):
            login_window.destroy()  # Feche a janela de login
            open_main_interface()  # Abra a nova janela

        else:
            # Se a condição "if" anterior não for atendida, ou seja, se as credenciais de login forem incorretas
            # Cria um rótulo de aviso com texto "Nome de Usuário ou Senha incorretos" em vermelho
            msg_lbl = Label(login_window, text="Incorrect username or password.", fg="red")
            msg_lbl.grid(row=3,column=0,columnspan=2)


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

    entrar_btn = Button(login_window, text="Create an account", font="Arial 12", bg="#eeeeee", command=show_register_window)
    entrar_btn.grid(row=4, column=0,columnspan=1, padx=20, pady=10, sticky="NSEW")

    entrar_btn = Button(login_window, text="Login", font="Arial 12", bg="#eeeeee", command=verify_login)
    entrar_btn.grid(row=4, column=1,columnspan=2, padx=20, pady=10, sticky="NSEW")

    sair_btn = Button(login_window, text="Exit", font="Arial 12", bg="#eeeeee", command=login_window.destroy)
    sair_btn.grid(row=5, column=0,columnspan=2, padx=20, pady=10, sticky="NSEW")

    # Define a configuração de peso para as linhas e colunas da grade da tela de login
    for i in range(5):
        login_window.grid_rowconfigure(i, weight=1)
        login_window.grid_rowconfigure(i, weight=1)

    for i in range(2):
        login_window.grid_columnconfigure(i, weight=1)


    
    login_window.mainloop()

    

# Execução da aplicação
show_login_window()