class Aluno:
    def __init__(self, id = '', nome = '', idade = 0, ra = '', curso = '', cep = '', rua = '', bairro = '', localidade = '', uf = ''):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__ra = ra
        self.__curso = curso
        self.__cep = cep
        self.__rua = rua
        self.__bairro = bairro
        self.__localidade = localidade
        self.__uf = uf

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
    def ra(self):
        return self.__ra
   
    @ra.setter
    def ra(self, ra):
        self.__ra = ra
    
    @property
    def curso(self):
        return self.__curso
   
    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def cep(self):
        return self.__cep
   
    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def rua(self):
        return self.__rua
   
    @rua.setter
    def rua(self, rua):
        self.__rua = rua
    
    @property
    def bairro(self):
        return self.__bairro
   
    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def localidade(self):
        return self.__localidade
   
    @localidade.setter
    def localidade(self, localidade):
        self.__localidade = localidade

    @property
    def uf(self):
        return self.__uf
   
    @uf.setter
    def uf(self, uf):
        self.__uf = uf