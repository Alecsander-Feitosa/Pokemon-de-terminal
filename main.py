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





import pickle
import time

from Pokemon import *                                                                               #importando
from pessoa import*

def escolher_pokemon_inicial(Player):                                                               #(def) escolhendo pokemon
    print("{}, Escolha o pokemon que ira lhe acompanhar nessa jornada!".format(Player))             #texto de inicio

    pikachu = PokemonEletrico(especie="pikachu", level=1)                                                       #Pokemons disponiveis non
    charmander = PokemonFogo(especie="charmander", level=1)                                                     #Pokemons disponiveis non
    squirtle = PokemonAgua(especie="squirtle", level=1)                                                         #Pokemons disponiveis non

    print("Voce tem 3 escolhas:")                                                                       #escolha
    print("1-", pikachu)                                                                                #Pokemons disponiveis
    print("2-", charmander)                                                                             #Pokemons disponiveis
    print("3-", squirtle)                                                                               #Pokemons disponiveis

    while True:                                                                                          #criaçao de menu < 
        Escolha = input("escolha um pokemon:")                                                             #(input)texto de digitaçao
        
        if Escolha == "1":
            Player.capturar(pikachu)
            break
        elif Escolha == "2":
            Player.capturar(charmander)
            break
        elif Escolha == "3":
            Player.capturar(squirtle)
            break
        else:
            print("Escolha invalida")
            
            
            
def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as Error:
        print("Erro ao salvar jogo")
        print(Error)


   

def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com sucesso!")
            return player
    except Exception as Error:
        print("______________________")
        print("Loading nao encontrado")
        print("______________________")
        return None
        
        



if __name__ == "__main__":
    print("_____________________________________________")
    print("                                             |")
    print("Bem-vindo ao game Pokemon rpg de terminal    |")
    print("_____________________________________________|")
    time.sleep(0.2)
    print("⌛⌛⌛")
    time.sleep(0.5)
    
    player = carregar_jogo()
    if not player:

    
        nome = input("Ola, qual eh seu nome:")
        player = Player(nome)
        time.sleep(1)
        print("")
        print("Ola {}, esse eh um mundo habitado por pokemons a partir de agora sua missao eh se tornar um mestre dos pokemons".format(player))
        print("")
        time.sleep(1)
        print("Capture o maximo de pokemons que conseguir e lute com seus inimigos")
        print("__________________")
        time.sleep(1)
        player.mostrar_dinheiro()
        print("")
            
        if player.pokemons:
                time.sleep(0.5)
                print("Ja vi que voce possui alguns pokemons")
                player.mostrar_pokemons()
        else:
                time.sleep(0.7)
                print("Voce nao possui nenhum pokemon, Portanto precisa escolher um!")
                print("_____________________________________________________________")
                time.sleep(0.7)
                escolher_pokemon_inicial(player)
                time.sleep(0.7)
                print("")
            
        time.sleep(0.5)   
        print("Pronto! Agora que voce ja possui um pokemon enfrente seu arqui-rival Gary")
        gary = inimigo("gary", pokemons=[PokemonAgua("squirtle", level=1)])
        time.sleep(0.7)
        player.batalhar(gary)
        salvar_jogo(player)
    
    while True:
        time.sleep(0.5)
        print("_____________________________")
        print("O que deseja fazer:  ")
        print("1 - Batalhar com um inimigo")
        print("2 - explorar pelo mundo")
        print("3 - mostrar pokemons")
        print("4 - Mostrar dinheiro")
        print("0 - Sair do jogo")
        
        Escolha = input("...")
        if Escolha == "1":
            inimigo_aleatorio = inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif Escolha == "2":
            player.explorar()
            salvar_jogo(player)
        elif Escolha == "0":
            print("Fechando o jogo...")
            break
        elif Escolha == "3":
            player.mostrar_pokemons()
        elif Escolha == "4":
            player.mostrar_dinheiro()
        else:

            print("Escolha invalida")

