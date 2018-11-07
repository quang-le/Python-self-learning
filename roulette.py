import random
#declare vars and define functions
black_numbers=[1,3,5,7,9,10,12,14,16,18,21,23,25,27,29,30,32,34,36]
result_values=[]
player_money=500
player_bets=[]

def number_bet():
    number_question=input("Voulez-vous miser sur un nombre? o/n  ")
    if number_question == "o":
        number_bet=int(input("Quelle est votre mise ?  "))
        number_input=int(input("Choisissez un nombre. Faites vos jeux!  "))
        player_bets.append(number_input)
        player_bets.append("Nombre")
        player_bets.append(number_bet)

def bet_questions(type1, type2):
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
        print(bets_list.index(value1_of_2))
        return bets_list.index(value1_of_2)
    elif value1_of_2 in bets_list:
        print(bets_list.index(value2_of_2))
        return bets_list.index(value2_of_2)
    else:
        return False


def determine_gains(bet_type,bet, result, amount, multiplier, wallet):
    gain_from_play=0
    if bet==result:
        gain_from_play=int(amount)*multiplier
        wallet+=gain_from_play
        print("Vous gagnez "+str(gain_from_play)+" pour "+bet_type)
        
    else:
        print("Vous perdez pour "+bet_type)

def play_roulette(player_bet, casino_result):
    announce_result(tourne_roulette())
    print(player_bet)
    print(casino_result)

    if player_did_bet('Nombre','Nombre',player_bet):
        print('results nombre')
        index_bet=player_did_bet('Nombre','Nombre',player_bet)
        index_amount= index_bet+1
        print(index_bet)
        print(index_amount)
        determine_gains('Nombre',player_bet[index_bet], casino_result[1], player_bet[index_amount],36,player_money)
        print("ready to go further")


    if player_did_bet('Rouge','Noir',player_bet):
        print('results rouge noir')
        index_bet=player_did_bet('Rouge','Noir',player_bet)
        index_amount= index_bet+1
        determine_gains('Rouge/Noir',player_bet[index_bet], casino_result[1], player_bet[index_amount],2,player_money)
        print("ready to go further")

    if player_did_bet('Pair','Impair',player_bet):
        print('results pair impair')
        index_bet=player_did_bet('Pair','Impair',player_bet)
        index_amount= index_bet+1
        determine_gains('Pair/Impair',player_bet[index_bet], casino_result[1], player_bet[index_amount],2,player_money)
        print("ready to go further")

    if player_did_bet('Passe','Manque',player_bet):
        print ('results pass manque')
        index_bet=player_did_bet('Passe','Manque',player_bet)
        index_amount= index_bet+1
        determine_gains('Passe/Manque',player_bet[index_bet], casino_result[1], player_bet[index_amount],2,player_money)
        print("ready to go further")

    print("Il vous reste "+str(player_money))



#run
print("Vous avez "+str(player_money)+" $")
number_bet()
bet_questions("Rouge","Noir")
bet_questions("Pair","Impair")
bet_questions("Manque","Passe")
print("Rien ne va plus")
play_roulette(player_bets, result_values)
