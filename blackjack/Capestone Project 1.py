import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_score = 0 
pc_score = 0
player_hand = random.choices(cards, k=2)
pc_hand = random.choices(cards, k=1)
hit_me = True

def current_scores(player_hand, pc_hand, player_score, pc_score):
    for card in player_hand:
        player_score += card
    print(f"Your cards: {player_hand}, current score {player_score} ")
      
    for card in pc_hand:
       pc_score += card
    print(f"Computer's first card: {pc_score} ")

def final_scores(player_hand, pc_hand, player_score, pc_score):
    for card in player_hand:
       player_score += card
    print(f"Your final hand: {player_hand}, final score {player_score} ")
      
    for card in pc_hand:
       pc_score += card
    print(f"Computer's final hand: {pc_hand}, final score: {pc_score} ")
    
def declare_winner(player_hand, pc_hand, player_score, pc_score):
    if player_score == pc_score:
        print("It is a draw.")
        
    elif 22 > player_score > pc_score:
        print("You won!")
        
    elif 22 > pc_score > player_score:
        print("You lose!")

def overbetting (player_hand, pc_hand, player_score, pc_score):
#    if player_score > 21:
        print(final_scores(player_hand, pc_hand, player_score, pc_score))
        print("You went over, you lose!")
        hit_me = False
        
#    elif pc_score > 21:
#       print(final_scores(player_hand, pc_hand, player_score, pc_score))
#       print("Computer went over, you won!")
#       hit_me = False

def hit_again(player_hand, pc_hand, player_score, pc_score):
    if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        player_hand += random.choices(cards, k=1)
        current_scores(player_hand, pc_hand, player_score, pc_score)
        #overbetting(player_hand, pc_hand, player_score, pc_score)
        hit_again(player_hand, pc_hand, player_score, pc_score)
        
    elif input("Type 'y' to get another card, type 'n' to pass: ") == "n":
        final_scores(player_hand, pc_hand, player_score, pc_score)
        declare_winner(player_hand, pc_hand, player_score, pc_score)
    
    
while hit_me:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        current_scores(player_hand, pc_hand, player_score, pc_score)
        hit_again(player_hand, pc_hand, player_score, pc_score)
    
    

