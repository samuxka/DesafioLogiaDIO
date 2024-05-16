class Ninja:
    ninjaAttack = 'Vento cortante'

    def __init__(self, nome, idade, classes):
        self.nome = nome
        self.idade = idade
        self.classes = classes

    def attack(self):
        print(f"O Heroi {self.nome}, da classe {self.classes[0]} atacou usando {self.ninjaAttack}")

class Monge:
    mongeAttack = 'Punho de serenidade'

    def __init__(self, nome, idade, classes):
        self.nome = nome
        self.idade = idade
        self.classes = classes

    def attack(self):
        print(f"O Heroi {self.nome}, da classe {self.classes[1]} atacou usando {self.mongeAttack}")

class Mago:
    magoAttack = 'Explosão Arcana'

    def __init__(self, nome, idade, classes):
        self.nome = nome
        self.idade = idade
        self.classes = classes

    def attack(self):
        print(f"O Heroi {self.nome}, da classe {self.classes[2]} atacou usando {self.magoAttack}")

class Guerreiro:
    guerreiroAttack = 'Martelo da Justiça divina'

    def __init__(self, nome, idade, classes):
        self.nome = nome
        self.idade = idade
        self.classes = classes

    def attack(self):
        print(f"O Heroi {self.nome}, da classe {self.classes[3]} atacou usando {self.guerreiroAttack}")

classes = ['Ninja', 'Monge', 'Mago', 'Guerreiro']

def checkClass(classes, nome, idade):
    if tipo == '1':
        personagem = Ninja(nome, idade, classes)
    elif tipo == '2':
        personagem = Monge(nome, idade, classes)
    elif tipo == '3':
        personagem = Mago(nome, idade, classes)
    elif tipo == '4':
        personagem = Guerreiro(nome, idade, classes)
    else:
        print('Opção inválida')
        return

    personagem.attack()

nome = input('Nome do seu herói: ')
idade = input('Idade do seu herói: ')
print('1 - Ninja, 2 - Monge, 3 - Mago, 4 - Guerreiro')
tipo = input('Classe do seu herói: ')

checkClass(classes, nome, idade)
