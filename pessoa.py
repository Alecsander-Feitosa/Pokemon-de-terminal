"""
                                        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                                        #                               Pokemo game (shell)                            #
                                        #                           Autor: Alecsander Feitosa                          #
                                        #                           Data de criação: 10/01/2025                        #
                                        #       Descrição: Projeto pessoal para criação de um pokemon de termianl      #
                                        #                                                                              #
                                        #                                  Uso: LIvre                                  #
                                        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""







import random
import time
from Pokemon import*                                                     


NOMES = ["Maria", "Joao", "isabela", "Geronimo", "Fransisco", "Ricardo",   #lista de nomes 
        "diego","Patricia", "Gustavo", "Marcelo", "Gary"
        ]


Pokemons_lista = [
    PokemonAgua("squirtle"),
    PokemonAgua("Arturtle"),
    PokemonAgua("Blastoise"),
    PokemonEletrico("pikachu"),
    PokemonEletrico("pichu"),
    PokemonEletrico("Raiochu"),
    PokemonFogo("charmander"),
    PokemonFogo("charmileon"),
    PokemonFogo("charizard")
    ]



class PESSOA:                                                              #Classe-pai (classe principal)                                     
    

    
    def __init__(self, nome=None, pokemons=[], dinheiro=100):                                         #(def)
        if nome:                                                           #(if) se tiver nome  
            self.nome = nome                                               #(self)= nome
        else:                                                              #(else) se nao tiver 
            self.nome = random.choice(NOMES)                               #(self) = desconhecido
        
        self.pokemons = pokemons                                           #(self)= pokemons  

        self.dinheiro = dinheiro 
    
   
            

    def __str__(self):
        return self.nome
    
    
    
    def mostrar_pokemons(self):                                            #(def)para mostrar pokemons
        if self.pokemons:                                                  #(if) Se tiver pokenmons
            print("____________________")
            print("{} tem:".format(self)) 
            time.sleep(0.5)
            for index, Pokemon in enumerate(self.pokemons):                                     #(for)vamos procurar (in) em 
             print("{} - {}".format(index, Pokemon)) 
        else: 
            time.sleep(0.5)
            print("-----------------------------------------")
            print("{} nao tem nenhum pokemon!".format(self))               #print + format
            


    def capturar(self, pokemon):                                           #(def)para capturar pokemons
        self.pokemons.append(pokemon)  
        time.sleep(1) 
        print ("{} capturou {}!".format(self, pokemon))                    #print + format



    def escolher_pokemons(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            time.sleep(0.5)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            time.sleep(0.5)
            print("{} nao tem pokemons para ser escolhido".format(self))   

    def mostrar_dinheiro (self):
        time.sleep(0.2)
        print("{} tem $ {}".format(self, self.dinheiro))
        print("----------------------------")
    
    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        time.sleep(0.2)
        print("_____________________________________")
        print("Voce ganhou $ {} na sua conta!".format(quantidade))
        print("_____________________________________")
        time.sleep(0.3)
        self.mostrar_dinheiro()
       
       
        
    def perder_dinheiro(self, quantidade):
        if self.dinheiro <= quantidade:
            self.dinheiro -= self.dinheiro 
        else:
            self.dinheiro -= quantidade
        time.sleep(0.3)
        print("_____________________________________")
        print("Voce perdeu $ {} ".format(quantidade))
        print("_____________________________________")
        time.sleep(0.3)



    def batalhar(self, pessoa):
        print("_____________________________")
        print("{} iniciou uma batalha com {}".format(self, pessoa))
        time.sleep(0.5)
        pessoa.mostrar_pokemons()
        time.sleep(0.5)
        self.mostrar_pokemons()
        time.sleep(0.5)
        print("_____________________________________")
        print(           "HORA DA ESCOLHA!          ")
        print("_____________________________________")
        pokemon_inimigo = pessoa.escolher_pokemons()
        print("_____________________________________")
        pokemon_aliado = self.escolher_pokemons()
        
        if pokemon_aliado and pokemon_inimigo:
            
            while True:
                vitoria_inimiga = pokemon_aliado.atacar(pokemon_inimigo)
                time.sleep(0.2)
                if vitoria_inimiga:
                    print("{} ganhou a batalha!".format(pessoa))
                    self.perder_dinheiro(pokemon_inimigo.level * 100)
                    break
                vitoria = pokemon_inimigo.atacar(pokemon_aliado)
                time.sleep(0.2)
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
        
        else:
            print("Batalha nao pode ser iniciada")  





class Player(PESSOA):                                                      #Classe filho
    tipo = "player"                                                        #tipo da classe 



    def escolher_pokemons(self):
            
            if self.pokemons:
                while True:
                    escolha = input("Escolha o pokemon para batalhar:")
                    try:
                        escolha = int(escolha)
                        pokemon_escolhido = self.pokemons[escolha]
                        time.sleep(0.2)
                        print("_____________________________________")
                        print("{} eu escolho voce!!!".format(pokemon_escolhido))
                        print("_____________________________________")
                        return pokemon_escolhido
                    except:
                        print("Escolha invalida")
            else:
                print("{} nao tem pokemons para ser escolhido".format(self)) 
                
    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(Pokemons_lista)
            print("Um pokemon selvagem apareceu: {}".format(pokemon))
            
            escolha = input ("Deseja capturar o pokemon (s/n)")
            
            
            if escolha == "s":
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                    self.mostrar_pokemons()
                else:
                    print("{} fugiu".format(pokemon))
            else:
                print("Ok, boa viagem")
                
                
        else:
            print("Essa exploraçao nao deu em nada")




class inimigo(PESSOA):
    tipo = "inimigo"



    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokmemons_aleatorios = []
            for i in range(random.randint(1, 6)):
              pokmemons_aleatorios.append(random.choice(Pokemons_lista))
            super().__init__(nome, pokemons= pokmemons_aleatorios)
        else:   
            super().__init__(nome, pokemons= pokemons)
                 
   






