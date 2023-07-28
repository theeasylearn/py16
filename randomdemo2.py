import random as rd 
playing_cards = ['2 Hearts', '2 Diamonds', '2 Clubs', '2 Spades', '3 Hearts', '3 Diamonds', '3 Clubs', '3 Spades', '4 Hearts', '4 Diamonds', '4 Clubs', '4 Spades', '5 Hearts', '5 Diamonds', '5 Clubs', '5 Spades', '6 Hearts', '6 Diamonds', '6 Clubs', '6 Spades', '7 Hearts', '7 Diamonds', '7 Clubs', '7 Spades', '8 Hearts', '8 Diamonds', '8 Clubs', '8 Spades', '9 Hearts', '9 Diamonds', '9 Clubs', '9 Spades', '10 Hearts', '10 Diamonds', '10 Clubs', '10 Spades', 'J Hearts', 'J Diamonds', 'J Clubs', 'J Spades', 'Q Hearts', 'Q Diamonds', 'Q Clubs', 'Q Spades', 'K Hearts', 'K Diamonds', 'K Clubs', 'K Spades', 'A Hearts', 'A Diamonds', 'A Clubs', 'A Spades']
print(playing_cards)
rd.shuffle(playing_cards)
print(playing_cards)
cardset1 = rd.choices(playing_cards,k=3)
cardset2 = rd.choices(playing_cards,k=3)
print(cardset1)
print(cardset2)