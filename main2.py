import os
import random

# Define os locais do jogo
locais = {
    'inicio': 'Você está em uma pequena clareira na floresta. Há uma trilha à direita e uma cabana à esquerda.',
    'cabana': 'Você está em uma cabana velha e empoeirada. Há um baú aqui.',
    'vila': 'Você chegou a uma pequena vila. Há uma taberna, um mercado e uma guilda aqui.',
    'mercado': 'Você está no mercado da vila. Há vários itens à venda.',
    'taberna': 'Você está na taberna da vila. Há alguns habitantes conversando e bebendo aqui.',
    'guilda': 'Você está na guilda. Aqui você pode vender drops de monstros.',
    'montanha': 'Você está na base de uma montanha alta. Há uma caverna aqui.',
    'caverna': 'Você está na caverna escura da montanha. É um lugar assustador.',
    'laberinto da caverna': 'Você encontrou um labirinto dentro da caverna.',
    'trilha escura': 'Você percorre uma grande trilha sem nenhuma iluminação.',
    'riacho': 'Você está ao lado de um riacho cristalino. A água é pura e refrescante.',
    'dangon': 'Você está em uma dungeon perigosa. É muito fácil encontrar monstros aqui.',
    '1º andar': 'Você chegou no primeiro andar da dungeon. Há muitos monstros aqui, cuidado!',
    '2º andar': 'Você chegou no 2º andar da dungeon. Os monstros aqui são mais fortes.',
    '3º andar': 'Você chegou no 3º andar da dungeon. A chance de achar drops melhores é maior.',
}

# Define as conexões entre os locais
conexoes = {
    'inicio': {'direita': 'vila', 'esquerda': 'cabana'},
    'vila': {'frente': 'montanha', 'direita': 'riacho'},
    'montanha': {'frente': 'caverna'},
    'caverna': {'frente': 'laberinto da caverna', 'direita': 'trilha escura'},
    'trilha escura': {'frente': '2º andar'},
    'cabana': {'frente': 'dangon'},
    'riacho': {'frente': 'montanha'},
    'dangon': {'frente': '1º andar'},
}

# Define o estado inicial do jogo
estado = {
    'local_atual': 'inicio',
    'item_pesquisado': False,
    'item_mercado': False,
    'moedas': 10,
    'vida': 100,
    'inventario': [],
    'monstro_encontrado': False,
    'arma': None,
    'historico': [],  # Histórico de locais visitados
    'monstro': None,
}

# Define os itens
item = {
    'nome': 'baú',
    'descricao': 'Um baú antigo e enferrujado. Pode conter algo interessante.',
    'pegou': False,
}

item_mercado = {
    'nome': 'poção',
    'descricao': 'Uma poção mágica que pode restaurar sua saúde.',
    'comprado': False,
}

armas_mercado = [
    {'nome': 'Espada', 'descricao': 'Uma espada afiada. Aumenta seu dano.', 'preco': 10, 'dano': 10},
    {'nome': 'Machado', 'descricao': 'Um machado pesado. Causa grande dano.', 'preco': 30, 'dano': 15},
    {'nome': 'Arco', 'descricao': 'Um arco com flechas. Permite ataques à distância.', 'preco': 25, 'dano': 12}
]

# Define personagens
personagens = {
    'mercador': 'O mercador sorri e diz: "Tenho itens e armas à venda."',
    'taberneiro': 'O taberneiro acena e diz: "Bem-vindo à nossa taberna! Sinta-se à vontade para conversar com os habitantes."',
    'guilda': 'O mestre da guilda diz: "Você pode vender seus drops de monstros aqui."'
}

# Define monstros
monstros = [
    {'nome': 'Goblin', 'vida': 30, 'dano': 10, 'drop': 'Pele de Goblin'},
    {'nome': 'Lobo', 'vida': 40, 'dano': 15, 'drop': 'Pele de Lobo'},
    {'nome': 'Troll', 'vida': 60, 'dano': 20, 'drop': 'Dente de Troll'},
    {'nome': 'Golem', 'vida': 90, 'dano': 15, 'drop': 'poção'},
    {'nome': 'Zumbi', 'vida': 50, 'dano': 6, 'drop': 'XP'},
    {'nome': 'Morcego', 'vida': 10, 'dano': 2, 'drop': 'asas de morcego'}

]

# Define os locais onde monstros podem aparecer
locais_com_monstros = {
    'inicio': 0.2,
    'cabana': 0.3,
    'montanha': 0.4,
    'caverna': 0.5,
    'riacho': 0.1,
    'dangon': 1.0,
    '1º andar': 2.0,
    '2º andar': 3.0,
    '3º andar': 4.0
}

# Função para limpar o terminal de acordo com o sistema operacional
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para mostrar o mapa do jogo
def mostrar_mapa():
    print("""
    Mapa do Jogo:
    
    Cabana - Dangon - 1º andar - 2º andar - 3º andar
      |
    Início - Vila - Montanha - Caverna - Labirinto
                |
              Riacho
    """)

# Função para mostrar o local atual do jogador
def mostrar_local():
    local = estado['local_atual']
    print(locais[local])
    if estado['monstro_encontrado']:
        print(f'Você encontrou um {estado["monstro"]["nome"]}!\n')

# Função para verificar o status atual do jogador
def verificar_status():
    print(f"\nStatus do Jogador:\nVida: {estado['vida']}\nMoedas: {estado['moedas']}\nInventário: {', '.join(estado['inventario'])}\nArma: {estado['arma']}\n")

# Função para mostrar os comandos disponíveis
def mostrar_comandos():
    print("\nComandos disponíveis:")
    print('"direita" - Mover para a direita.')
    print('"esquerda" - Mover para a esquerda.')
    print('"adiante" - Mover para frente.')
    print('"entrar mercado" - Entrar no mercado (apenas a partir da vila).')
    print('"sair mercado" - Sair do mercado.')
    print('"entrar taverna" - Entrar na taverna (apenas a partir da vila).')
    print('"sair taverna" - Sair da taberna.')
    print('"entrar guilda" - Entrar na guilda (apenas a partir da vila).')
    print('"sair guilda" - Sair da guilda.')
    print('"pegar" - Pegar um item (se disponível).')
    print('"comprar" - Comprar um item no mercado.')
    print('"vender" - Vender drops de monstros na guilda.')
    print('"falar" - Falar com um personagem (se disponível).')
    print('"verificar status" - Verificar seu status atual (vida, moedas, inventário, arma).')
    print('"limpar" - Limpar o terminal.')
    print('"voltar" - Voltar para o local anterior.')
    print('"atacar" - Atacar um monstro (se encontrado).')
    print('"fugir" - Tentar fugir de um monstro (se encontrado).')
    print('"fim de jogo" - Sair do jogo.')
    print('"comandos" - Mostrar os comandos disponíveis.')
    print()

# Função para mover para a direita
def mover_direita():
    local_atual = estado['local_atual']
    if local_atual in conexoes and 'direita' in conexoes[local_atual]:
        estado['historico'].append(local_atual)
        estado['local_atual'] = conexoes[local_atual]['direita']
        verificar_monstro()
        mostrar_local()
    else:
        print("Você não pode mover para a direita a partir deste local.")

# Função para mover para a esquerda
def mover_esquerda():
    local_atual = estado['local_atual']
    if local_atual in conexoes and 'esquerda' in conexoes[local_atual]:
        estado['historico'].append(local_atual)
        estado['local_atual'] = conexoes[local_atual]['esquerda']
        verificar_monstro()
        mostrar_local()
    else:
        print("Você não pode mover para a esquerda a partir deste local.")

# Função para mover para frente
def mover_frente():
    local_atual = estado['local_atual']
    if local_atual in conexoes and 'frente' in conexoes[local_atual]:
        estado['historico'].append(local_atual)
        estado['local_atual'] = conexoes[local_atual]['frente']
        verificar_monstro()
        mostrar_local()
    else:
        print("Você não pode mover para frente a partir deste local.")

# Função para voltar ao local anterior
def voltar():
    if estado['historico']:
        estado['local_atual'] = estado['historico'].pop()
        mostrar_local()
    else:
        print("Você não pode voltar mais.")

# Função para entrar na taberna
def entrar_taberna():
    if estado['local_atual'] == 'vila':
        estado['historico'].append(estado['local_atual'])
        estado['local_atual'] = 'taberna'
        mostrar_local()
    else:
        print("Você não pode entrar na taberna a partir deste local.")

# Função para sair da taberna
def sair_taberna():
    if estado['local_atual'] == 'taberna':
        estado['local_atual'] = estado['historico'].pop()
        mostrar_local()
    else:
        print("Você não pode sair da taberna a partir deste local.")

# Função para entrar no mercado
def entrar_mercado():
    if estado['local_atual'] == 'vila':
        estado['historico'].append(estado['local_atual'])
        estado['local_atual'] = 'mercado'
        mostrar_local()
    else:
        print("Você não pode entrar no mercado a partir deste local.")

# Função para sair do mercado
def sair_mercado():
    if estado['local_atual'] == 'mercado':
        estado['local_atual'] = estado['historico'].pop()
        mostrar_local()
    else:
        print("Você não pode sair do mercado a partir deste local.")

# Função para entrar na guilda
def entrar_guilda():
    if estado['local_atual'] == 'vila':
        estado['historico'].append(estado['local_atual'])
        estado['local_atual'] = 'guilda'
        mostrar_local()
    else:
        print("Você não pode entrar na guilda a partir deste local.")

# Função para sair da guilda
def sair_guilda():
    if estado['local_atual'] == 'guilda':
        estado['local_atual'] = estado['historico'].pop()
        mostrar_local()
    else:
        print("Você não pode sair da guilda a partir deste local.")

# Função para pegar um item
def pegar_item():
    if estado['local_atual'] == 'cabana' and not item['pegou']:
        print(f"Você pegou um(a) {item['nome']}!")
        estado['inventario'].append(item['nome'])
        item['pegou'] = True
    else:
        print("Não há itens para pegar aqui.")

# Função para comprar um item no mercado
def comprar_item():
    if estado['local_atual'] == 'mercado':
        print("Itens disponíveis para compra:")
        for i, arma in enumerate(armas_mercado, 1):
            print(f"{i}. {arma['nome']} - {arma['preco']} moedas ({arma['descricao']})")
        
        escolha = input("Escolha o número do item que deseja comprar: ").strip()
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(armas_mercado):
                arma_selecionada = armas_mercado[escolha - 1]
                if estado['moedas'] >= arma_selecionada['preco']:
                    estado['moedas'] -= arma_selecionada['preco']
                    estado['arma'] = arma_selecionada['nome']
                    print(f"Você comprou {arma_selecionada['nome']}!")
                else:
                    print("Você não tem moedas suficientes para comprar este item.")
            else:
                print("Escolha inválida.")
        else:
            print("Entrada inválida.")
    else:
        print("Você não está no mercado.")

# Função para vender drops de monstros na guilda
def vender_drop_monstro():
    if estado['local_atual'] == 'guilda':
        if estado['inventario']:
            drop = estado['inventario'].pop(0)  # Vende o primeiro item do inventário
            print(f"Você vendeu {drop} por 5 moedas.")
            estado['moedas'] += 5
        else:
            print("Você não tem drops de monstros para vender.")
    else:
        print("Você não está na guilda.")

# Função para falar com um personagem
def falar_personagem():
    if estado['local_atual'] == 'mercado':
        print(personagens['mercador'])
    elif estado['local_atual'] == 'taberna':
        print(personagens['taberneiro'])
    elif estado['local_atual'] == 'guilda':
        print(personagens['guilda'])
    else:
        print("Não há ninguém para falar aqui.")

# Função para verificar se um monstro aparece
def verificar_monstro():
    local = estado['local_atual']
    if local in locais_com_monstros:
        chance = locais_com_monstros[local]
        if random.random() < chance:
            estado['monstro_encontrado'] = True
            estado['monstro'] = random.choice(monstros)
            print(f"\nUm {estado['monstro']['nome']} apareceu!\n")
        else:
            estado['monstro_encontrado'] = False

# Função para atacar o monstro
def atacar():
    if estado['monstro_encontrado']:
        arma_dano = 5  # Dano base sem arma
        if estado['arma']:
            for arma in armas_mercado:
                if arma['nome'] == estado['arma']:
                    arma_dano = arma['dano']
                    break
        
        monstro = estado['monstro']
        dano_causado = arma_dano
        dano_recebido = monstro['dano']

        monstro['vida'] -= dano_causado
        estado['vida'] -= dano_recebido

        print(f"Você atacou o {monstro['nome']} e causou {dano_causado} de dano.")
        print(f"O {monstro['nome']} atacou você e causou {dano_recebido} de dano.")
        
        if monstro['vida'] <= 0:
            print(f"Você derrotou o {monstro['nome']}!")
            estado['inventario'].append(monstro['drop'])
            estado['monstro_encontrado'] = False
            estado['monstro'] = None
        elif estado['vida'] <= 0:
            print("Você foi derrotado pelo monstro. Fim de jogo.")
            exit()
    else:
        print("Não há nenhum monstro para atacar.")

# Função para fugir do monstro
def fugir():
    if estado['monstro_encontrado']:
        if random.random() < 0.5:
            print("Você conseguiu fugir do monstro!")
            estado['monstro_encontrado'] = False
            estado['monstro'] = None
            voltar()
        else:
            monstro = estado['monstro']
            dano_recebido = monstro['dano']
            estado['vida'] -= dano_recebido
            print(f"Você falhou em fugir. O {monstro['nome']} atacou você e causou {dano_recebido} de dano.")
            
            if estado['vida'] <= 0:
                print("Você foi derrotado pelo monstro. Fim de jogo.")
                exit()
    else:
        print("Não há nenhum monstro para fugir.")

# Função principal para executar o jogo
def jogar():
    limpar_terminal()
    print("Bem-vindo a Astravia!")
    print("Uma vez existiu um guerreiro que foi capaz de quase que iradicar todo o mal do mundo, em sua jornada ele deixou um grande tesouro, muitos tentaram encontrar e mesmo depois de 320 anos de sua morte nunca foi encontrado, mas sera que isso ira mudar?")
    mostrar_comandos()
    nome_personagem = input("Ola guerreiro, prezer em conhecelo, como posso chamalo? ").strip()
    limpar_terminal()
    print(f"\nOlá, {nome_personagem}! Sua aventura começa agora.\n")
    mostrar_local()

    while True:
        comando = input("oque fara?: ").strip().lower()

        if comando == 'fim de jogo':
            print("Fim de jogo. Até a próxima!")
            break
        elif comando == 'direita':
            mover_direita()
        elif comando == 'esquerda':
            mover_esquerda()
        elif comando == 'voltar':
            voltar()
        elif comando == 'adiante':
            mover_frente()
        elif comando == 'entrar mercado':
            entrar_mercado()
        elif comando == 'sair mercado':
            sair_mercado()
        elif comando == 'entrar taverna':
            entrar_taberna()
        elif comando == 'sair taverna':
            sair_taberna()
        elif comando == 'entrar guilda':
            entrar_guilda()
        elif comando == 'sair guilda':
            sair_guilda()
        elif comando == 'pegar':
            pegar_item()
        elif comando == 'comprar':
            comprar_item()
        elif comando == 'vender':
            vender_drop_monstro()
        elif comando == 'falar':
            falar_personagem()
        elif comando == 'verificar status':
            verificar_status()
        elif comando == 'limpar':
            limpar_terminal()
        elif comando == 'atacar':
            atacar()
        elif comando == 'fugir':
            fugir()
        elif comando == 'comandos':
            mostrar_comandos()
        else:
            print("Comando inválido. Digite 'comandos' para ver a lista de comandos disponíveis.")

jogar()
