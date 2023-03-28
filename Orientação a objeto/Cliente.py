from ContaBancaria import ContaBancaria

class Cliente:
    def __init__(self, id, nome, idade, email):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__email = email
        self.__conta_bancaria = None

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def conta_bancaria(self):
        return self.__conta_bancaria
    
    def adicionar_conta_bancaria(self, conta_bancaria: ContaBancaria):
        self.__conta_bancaria = conta_bancaria