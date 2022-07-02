############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random
from art import logo

def deal_card():
  """Returns a random card from the cards list (deck)."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return(random.choice(cards))

def calculate_score(card_received_list):
  """Take a list of cards received by user or computer and return the score calculated from the cards"""
  #first exception, check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in the game.
  if sum(card_received_list) == 21 and len(card_received_list) == 2:
    return 0  
  #second exception, check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.    
  elif 11 in card_received_list and sum(card_received_list) > 21:
      card_received_list.remove(11)
      card_received_list.append(1)
  
  return sum(card_received_list) 

#Create a function called compare() and pass in the user_score and computer_score. If the computer and user scores are both over 21, the user loses. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "Both went over but unfortunately you lose 😞"
  elif user_score == computer_score:
    return "It's a draw 😐"
  elif computer_score == 0:
    return "You lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "You win with a Blackjack 😊"
  elif user_score > 21:
    return "You lose because you went over 😭"
  elif computer_score > 21:
    return "You win because opponent went over 😁"
  elif user_score > computer_score:
    return "You win because your score is higher 😅"
  elif user_score < computer_score:
    return"You lose because your score is lower 😠"
 

def play_game():
  print(logo)
  #Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  end_game = False
  while not end_game:
  #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")
    if computer_score == 0 or user_score == 0 or user_score > 21:
      end_game = True
    #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards listist. If no, user ended.
    else:
      should_continue = input("Type 'y' to draw another card , type 'n' to pass: ").lower()
      if should_continue == "y":
        user_cards.append(deal_card())   
      else:
        end_game = True
  
  #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"    Your final hand: {user_cards}, final score: {user_score}")
  print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

  #Ask the user if they want to restart the game. If they answer yes, start a new game of blackjack and show the logo from art.py.
while input("Do you want to play the Blackjack game coded by the future exceptional programmer Allen Chi? Type 'y' to play or 'n' to pass: ").lower() == "y":
  play_game()
    