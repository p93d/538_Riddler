# https://fivethirtyeight.com/features/does-your-gift-card-still-have-free-drinks-on-it/
import random


num_sims = 10000

# As we run out of drinks, store the remaining drinks
# on the other card in this list
drinks_left = []

for _ in range(num_sims):

    # two cards with 50 free drinks
   drinks = [50, 50]

   # randomly select one of the cards on each visit
   # until one of them runs out
   while True:
       # pick a card
       card_used = random.getrandbits(1)

       if drinks[card_used] == 0:
           drinks_left.append(sum(drinks))
           break
       else:
           drinks[card_used]+= -1


print(sum(drinks_left) / len(drinks_left))
print(drinks_left.count(0) / len(drinks_left))