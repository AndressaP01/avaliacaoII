class SimpleCLI:
    def __init__(self):
        self.commands={}
    def add_command(self,name,function):
        self.commands[name]=function
    def run(self):
        while True:
            command=input("Entre com um comando: ")
            if command=="quit":
                print("Godbye")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command")

class PersonCLI(SimpleCLI):
    def __init__(self,school_database):
        super().__init__()
        self.school_database=school_database
        self.add_command("create",self.create_school)
        self.add_command("read",self.read_school)
        self.add_command("update", self.update_school)
        self.add_command("delete", self.delete_school)

    def create_teacher(self):
        nome=input("Entre com o nome: ")
        dataNascimento=input("data de nascimento: ")
        cpf = input("cpf: ")
        self.school_database.create_person(nome,dataNascimento,cpf)


    def update_teacher(self):
        id=input("Entre com id: ")
        nome= input("Entre com o novo nome: ")
        dataNasc = input("Entre com a nova data de nascimento: ")
        self.school_database.update_person(id,nome,dataNasc)

    def delete_teacher(self):
        id=input("Entre com o id: ")
        self.school_database.delete_person(id)

    def run(self):
        print("Welcome to the person CLI!")
        print("Available commands: create, read,update,delete,quit")
        super().run()


