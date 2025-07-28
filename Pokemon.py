import time
import random

class POKEMON:                                                                          #classe principal 
    def __init__(self, especie, level=None, nome=None ):                                   #(self)= a o proprio objeto #(tipo e especie)sao as variaveis do objeto #(nome) argumento nao abrigatorio                 
        self.especie = especie                                                          #identaçao da variavel-especie
        self.level =  level                                                             #identaçao da variavel-level
        if nome:                                                                        #se tiver nome 
            self.nome = nome                                                            #vai ser    
        else:                                                                           #se nao tiver 
            self.nome = especie                                                         #vai ser 
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
    
        self.ataque = self.level * 5
        self.vida = self.level * 10



    def __str__(self):                                                                  #(def) str
        return "{}({})".format(self.nome, self.level,)                                  #.format - Formato da apresentaçao 
    
    
    
    def atacar(self, pokemon): 
        ataque_efetivo = int (self.ataque * random.random() * 1.3)
        pokemon.vida -= ataque_efetivo
        time.sleep(0.3)
        print("")
        print(">{} perdeu {} pontos de vida<".format(pokemon, ataque_efetivo))
        print("")
        if self.vida <= 0 :
            time.sleep(0.3)
            print("_____________________________________")
            print("{} Foi derrotado!".format(self))
            print("_____________________________________")
            return True
        else:
            
            return False


      
class PokemonEletrico(POKEMON):                                                         #Classe secundaria -!sintaxe NomeDaClasse(classe princlpal)
    tipo = "eletrico"                                                                   #"invariavel" - variavel fixa
    
    
    
    def atacar(self, POKEMON):                                                          #def-Ataque
        print("{} lançou um raio do trovao em {}".format (self, POKEMON))               #format de ataque
        return super().atacar(POKEMON)
        
        
        
        

class PokemonFogo(POKEMON):                                                             #Classe secundaria -!sintaxe NomeDaClasse(classe princlpal)
    tipo = "fogo"                                                                       #"invariavel" - variavel fixa
    
    def atacar(self, POKEMON):                                                          #def-Ataque    
        print("{} lançou uma rajada de fogo em {}".format (self, POKEMON))              #format de ataque
        return super().atacar(POKEMON)





class PokemonAgua(POKEMON):                                                             #Classe secundaria -!sintaxe NomeDaClasse(classe princlpal)
    tipo = "agua"                                                                       #"invariavel" - variavel fixa
    
    def atacar(self, POKEMON):                                                          #def-Ataque
        print("{} lançou um jato de agua em {}".format (self, POKEMON))  
        return super().atacar(POKEMON)

















