import random
#declare vars and define functions
black_numbers=[1,3,5,7,9,10,12,14,16,18,21,23,25,27,29,30,32,34,36]
result_values=[]
player_money=500
player_bets=[]

def number_bet(player_wallet):
    number_question=input("Voulez-vous miser sur un nombre? o/n  ")
    if number_question == "o":
        number_bet=int(input("Combien misez-vous ?  "))
        number_input=int(input("Choisissez un nombre. Faites vos jeux!  "))
        player_bets.append(number_input)
        player_bets.append("Nombre")
        player_bets.append(number_bet)
        player_wallet-=number_bet
    return player_wallet

def bet_questions(player_wallet,type1, type2):
    question=input("Voulez-vous miser sur "+type1+"/"+type2+" o/n")
    if question=="o":
        bet=int(input("Combien voulez-vous miser"))
        choice=input("Faites vos jeux!"+type1+"1 "+type2+" 2")
        if choice=="1":
            player_bets.append(type1)
            player_bets.append(bet)
        elif choice =="2":
            player_bets.append(type2)
            player_bets.append(bet)
        player_wallet-=bet
    return player_wallet

def tourne_roulette():
    print(" ")
    i=0
    while i<random.randint(25,55):
        print (random.randint(0,36))
        i+=1
    result = random.randint(0,36)
    return result

def announce_result(result):
    print(" ")
    print (result)
    result_values.append(result)
    if result==0:
        result_color="Ni noir, ni rouge"
    elif result in black_numbers:
        result_color="Noir"       
    else:
        result_color="Rouge"
    print (result_color+",")
    result_values.append(result_color)

    if result==0:
        result_even_odds="Ni pair, ni impair"
    elif result%2==1:
        result_even_odds="Impair"
    else:
        result_even_odds="Pair"

    print(result_even_odds+",")    
    result_values.append(result_even_odds)
    
    if result ==0:
        result_manque="Ni Manque, ni passe"
    elif result<18:
        result_manque="Manque"
    else:
        result_manque="Passe"
    print("et "+result_manque)
    result_values.append(result_manque)
    return result_values

def player_did_bet(value1_of_2, value2_of_2, bets_list):
    if value1_of_2 in bets_list:
        return bets_list.index(value1_of_2)
    elif value2_of_2 in bets_list:
        return bets_list.index(value2_of_2)
    else:
        return False


def determine_gains(bet_type,bet, result, amount, multiplier):
    gain_from_play=0
    if bet==result:
        gain_from_play+=int(amount)*multiplier
        print("Vous gagnez "+str(gain_from_play)+" pour "+bet_type)
        
    else:
        print("Vous perdez pour "+bet_type)
    return gain_from_play

def play_roulette(player_bet, casino_result, wallet):
    announce_result(tourne_roulette())
    print(player_bet)
    print(casino_result)

    if player_did_bet('Nombre','Nombre',player_bet):
        index_bet=player_did_bet('Nombre','Nombre',player_bet)
        index_amount= index_bet+1
        wallet+=determine_gains('Nombre',player_bet[index_bet], casino_result[0], player_bet[index_amount],36)
        print(wallet)

    if player_did_bet('Rouge','Noir',player_bet):
        index_bet=player_did_bet('Rouge','Noir',player_bet)
        index_amount= index_bet+1
        wallet+=determine_gains('Rouge/Noir',player_bet[index_bet], casino_result[1], player_bet[index_amount],2)
        print(wallet)

    if player_did_bet('Pair','Impair',player_bet):
        index_bet=player_did_bet('Pair','Impair',player_bet)
        index_amount= index_bet+1
        wallet+=determine_gains('Pair/Impair',player_bet[index_bet], casino_result[2], player_bet[index_amount],2)
        print(wallet)

    if player_did_bet('Passe','Manque',player_bet):
        index_bet=player_did_bet('Passe','Manque',player_bet)
        index_amount= index_bet+1
        wallet+=determine_gains('Passe/Manque',player_bet[index_bet], casino_result[3], player_bet[index_amount],2)
        print(wallet)
        
    print("Il vous reste "+str(wallet))
    return wallet

def play_game(player_money):
    player_money=number_bet(player_money)
    print("Il vous reste "+str(player_money))
    player_money=bet_questions(player_money,"Rouge","Noir")
    print("Il vous reste "+str(player_money))
    player_money=bet_questions(player_money,"Pair","Impair")
    print("Il vous reste "+str(player_money))
    player_money=bet_questions(player_money,"Manque","Passe")
    print("Il vous reste "+str(player_money))
    print("Rien ne va plus")
    new_money=play_roulette(player_bets, result_values, player_money)
    return new_money

def continue_game(player_money):
    continue_playing=input("Continuer à jouer ? o/n   ")
    if continue_playing=="o":
        play_game(player_money)
        continue_game(player_money)
    else:
        print("Vous avez "+str(player_money)+". Merci d'avoir joué!")

#run
print("Vous avez "+str(player_money)+" $")
play_game(player_money)
continue_game(player_money)

#bug: le porte-monnaie se réinitialise à chaque partie
#bug: réinitiliser les listes player_bets et results


# test_gains_rouge=determine_gains("Rouge/Noir","Rouge","Rouge",50,2)
# test_gains_noir=determine_gains("Rouge/Noir","Noir","Rouge",50,2)

# test_list=["Rouge","Impair","Manque"]

# test_bet= player_did_bet("Passe","Manque", test_list)
# print(test_bet)
