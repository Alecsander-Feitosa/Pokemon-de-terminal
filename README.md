# Pokémon Terminal

Versão simples de um jogo estilo Pokémon para terminal, desenvolvida em Python. Ideal para testes, aprendizado e diversão via linha de comando.

## 📝 Descrição
Este projeto traz:
- Um jogo inspirado em Pokémon, totalmente no terminal.
- Possibilidade de escolher personagens e realizar batalhas simples.
- Código em Python, fácil de explorar e expandir.
- Três arquivos: `main.py`, `Pokemon.py`, `pessoa.py`.

## ⚔️ Funcionalidades Principais
- Seleção de Pokémon inicial pelo jogador.
- Batalhas turn‑based entre Pokémon controlados por jogador e adversário.
- Geração de status como vida, ataque e defesa dos personagens.
- Loop principal de jogo controlado por `main.py`.

## 📂 Estrutura do Projeto
```
.
├── main.py       # Ponto de entrada do jogo; orquestra fluxo e interfaces
├── Pokemon.py    # Define a classe Pokémon: atributos, ações, evolução
└── pessoa.py     # Define a classe Jogador/Personagem, gerenciamento de equipe
```

## 🚀 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/Alecsander-Feitosa/Pokemon-de-terminal.git
   cd Pokemon-de-terminal
   ```
2. (Opcional) Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # no Linux/macOS
   venv\Scriptsctivate     # no Windows
   ```
3. Instale dependências, se houver (ajuste `requirements.txt` conforme necessidade):
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Como Jogar
Execute o comando:
```bash
python main.py
```
- Siga as instruções exibidas no terminal para escolher seu Pokémon e iniciar batalhas.
- O loop principal controla turnos de ataque, exibe status, e determina vitórias ou derrotas até o fim do combate.

## 🌟 Possíveis Melhorias
- Adicionar sistema de salvamento/carregamento.
- Incorporar evolução, diferentes tipos de ataque e defesa.
- Expandir para incluir mapas, lojas, ginásios e cores no terminal.
- Criar testes automatizados e interface de menu mais elaborada.

## 📜 Licença
Use o projeto conforme licença escolhida (MIT, GPL ou outra). Por padrão, ajuste conforme sua preferência ou adicione um arquivo **LICENSE** para especificar termos.
