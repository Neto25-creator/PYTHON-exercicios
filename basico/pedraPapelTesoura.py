import os
import random, time

def limpar_tela():
    os.system("cls")

limpar_tela()
vitorias_user_jogo = 0
vitorias_robo_jogo = 0

vitorias_user_tentativa = 0
vitorias_robo_tentativa = 0
while vitorias_user_jogo != 2 and vitorias_robo_jogo != 2:
    print("\n==============================================")
    print("          PEDRA, PAPEL OU TESOURA")
    print("==============================================\n")
    escolha = input("👉 Escolha uma opção entre [pedra / papel / tesoura]: ")
    sorteio = random.randint(1,3)
    if sorteio == 1:
        robo = "pedra"
    elif sorteio == 2:
        robo = "papel"
    elif sorteio == 3: 
        robo = "tesoura"

    print(f"\n🤖 O robo escolheu: {robo}\n")

    if escolha == "pedra":
        if robo == escolha:
            print("⚖️ Empate na tentativa! Jogue outra.")
        elif robo == "tesoura":
            vitorias_user_tentativa += 1
            print("✅ Você ganhou essa tentativa!")
        else: 
            vitorias_robo_tentativa += 1
            print("❌ Você perdeu a tentativa!")

    if escolha == "papel":
        if robo == escolha:
            print("⚖️ Empate na tentativa! Jogue outra.")
        elif robo == "pedra":
            vitorias_user_tentativa += 1
            print("✅ Você ganhou essa tentativa!")
        else: 
            vitorias_robo_tentativa += 1
            print("❌ Você perdeu a tentativa!")

    if escolha == "tesoura":
        if robo == escolha:
            print("⚖️ Empate na tentativa! Jogue outra.")
        elif robo == "papel":
            vitorias_user_tentativa += 1
            print("✅ Você ganhou essa tentativa!")
        else: 
            vitorias_robo_tentativa += 1
            print("❌ Você perdeu a tentativa!")

    print(f"\n📊 Placar da rodada -> Você: {vitorias_user_tentativa} | Robo: {vitorias_robo_tentativa}")
    print("------------------------------------------------------------\n")

    if vitorias_user_tentativa == 2:
        vitorias_user_jogo += 1
        vitorias_robo_tentativa = 0
        vitorias_user_tentativa = 0
        print(f"🎉 Você venceu a rodada!\nRodadas do jogo -> Você: {vitorias_user_jogo} | Robo: {vitorias_robo_jogo}")
        time.sleep(5)
        limpar_tela()
    elif vitorias_robo_tentativa == 2:
        vitorias_robo_tentativa = 0 
        vitorias_user_tentativa = 0
        vitorias_robo_jogo += 1
        print(f"💀 Você perdeu a rodada!\nRodadas do jogo -> Você: {vitorias_user_jogo} | Robo: {vitorias_robo_jogo}")
        time.sleep(5)
        limpar_tela()

    if vitorias_user_jogo == 2:
        print("\n🏆 VOCÊ GANHOU O JOGO!\n")
    elif vitorias_robo_jogo == 2:
        print("\n🤖 VOCÊ PERDEU! O ROBO GANHOU!\n")
