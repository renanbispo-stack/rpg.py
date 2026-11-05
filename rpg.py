import random 

#ATRIBUTOS 
guerreiro=([100,100,10,25])
ladino=([80,100,15,35])
mago=([60,100,5,45])
a=1
atk_player=0
#inimigos
bot_goblin=([80,100,15,35])
bot_lobo=([60,100,20,30])
bot_guerreiro=([100,100,10,25])
b=1
atk_bot=0
#introduçao
print("BEM-VINDO A BATALHA DE RPG DOS CAMPEÕES")
nome=input("ESCREVA O NOME DO SEU CAMPEÃO\n")
print("VAMOS LÁ PARA A NOSSA AVENTURA")

#escolha de personagem
while True:
    op_1=int(input("ESCOLHA ENTRE OS 3 CAMPEÕES PARA VER OS ATRIBUTOS (TODOS TEM 100 DE MANA) \n1-guerreiro\n2-ladino\n3-mago\n"))
    if op_1==1:
        op_2=int(input(f"O GUEREIRO TEM:\n{guerreiro[0]} DE VIDA\n{guerreiro[2]} ATK BASICO\n{guerreiro[3]} ATK PESADO\nDESEJA SELECIONAR ESSE?\n1-SIM\n2-NAO\n "))
        if op_2==1:
            player=guerreiro.copy()
            break
        else:
            print("")
    elif op_1==2:
        op_2=int(input(f"O LADINO TEM:\n{ladino[0]} DE VIDA\n{ladino[2]} ATK BASICO\n{ladino[3]} ATK PESADO\nDESEJA SELECIONAR ESSE?\n1-SIM\n2-NAO\n "))
        if op_2==1:
            player=ladino.copy()
            break
        else:
            print("")
    elif op_1==3:
        op_2=int(input(f"O MAGO TEM:\n{mago[0]} DE VIDA\n{mago[2]} ATK BASICO\n{mago[3]} ATK PESADO\nDESEJA SELECIONAR ESSE?\n1-SIM\n2-NAO\n"))
        if op_2==1:
            player=mago.copy()
            break
        else:
            print("")
#escolhendo um inimigo            
while True:
    inimigo1=random.randint(1,3)
    if inimigo1==1:
        print("O SEU INIMIGO SERA O GOBLIN")
        bot=bot_goblin.copy()
        break
    if inimigo1==2:
        print("O SEU INIMIGO SERA O LOBO")
        bot=bot_lobo.copy()
        break
    if inimigo1==3:
        print("O SEU INIMIGO SERA O GUERREIRO POSSUIDO")
        bot=bot_guerreiro.copy()
        break
#açoes
while True:
    a=1
    b=1
    atk_bot=0
    atk_player=0
    player[1]=player[1]+30
    bot[1]=bot[1]+30
    op_3=int(input("1-atk basico\n2-atk forte\n3-defesa\n4-cura"))
    op_bot=int(random.randint(1,4))
#AÇOES DE DEFESA
    if op_3==3:
        a=3
        print("VOCE SE DEFENDEU")

    if op_bot==3:
        b=3
        print("O DESAFIANTE SE DEFENDEU\n")
#PLAYER ATKS
    if op_3==1:
      
            if player[1]>=20:#verificaçao mana
                sorte_p=int(random.randint(1,10))
                player[1]=player[1]-20

                if sorte_p>=3:
                    atk_player=player[2]/b
                    atk_player=round(float(atk_player),1)
                else:
                    print("VOCE ERROU O SEU ATK FRACO")
                
            else:
                print("VOCE NAO TEM MANA O SUFICIENTE")
                
    elif op_3==2:
        if player[1]>=50:
            sorte_p=int(random.randint(1,10))
            player[1]=player[1]-50

            if sorte_p<=4:
                atk_player=player[3]/b
                atk_player=round(float(atk_player),1)
            else:
                    print("VOCE ERROU O SEU ATK FORTE")


        else: print("VOCE NAO TEM MANA O SUFICIENTE")

#player cura
    elif op_3==4:
        if player[1]>30:
            player[1]=player[1]-30
            sorte_p=int(random.randint(1,10))
            if sorte_p>=3:
                player[0]=player[0]+35
            else:print("VOCE ERROU A CURA")

        else: print("VOCE NAO TEM MANA")


#ATKS BOT
    if op_bot==1:
      
            if bot[1]>=20:#verificaçao mana
                sorte_bot=int(random.randint(1,10))
                bot[1]=bot[1]-20

                if sorte_bot>=3:
                    atk_bot=botr[2]/a
                    atk_bot=round(float(atk_bot),1)
                else:
                    print("O BOT ERROU O SEU ATK FRACO")
                
            else:
                print("O BOT NAO TEM MANA O SUFICIENTE")
                
    elif op_bot==2:
        if bot[1]>=50:
            sorte_bot=int(random.randint(1,10))
            bot[1]=bot[1]-50

            if sorte_bot<=4:
                atk_bot=bot[3]/a
                atk_bot=round(float(atk_bot),1)
            else:
                    print("O BOT ERROU O SEU ATK FORTE")


        else: print("O BOT NAO TEM MANA O SUFICIENTE")
#cura bot
    elif op_bot==4:
        if bot[1]>30:
            bot[1]=bot[1]-30
            sorte_bot=int(random.randint(1,10))
            if sorte_bot>=3:
                bot[0]=bot[0]+35
            else:print("VOCE ERROU A CURA")

        else: print("VOCE NAO TEM MANA")
  
    player[0]=player[0]-atk_bot
    bot[0]=bot[0]-atk_player
    if player[0]<=0:
        if bot[0]<=0:
            print("DEU EMPATE")
            break
        else:   
            print(f"O BOT GANHOU E FICOU COM {bot[0]} DE VIDA")
            break
    elif bot[0]<=0:
        if player[0]<=0:
            print("EMPATE")
            break
        else:
            print(f"VOCE GANHOU E FICOU COM{player[0]} DE VIDA")
            break
    print(f"{bot}{player}")