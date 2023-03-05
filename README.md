# MTG_Modern-Allosaurus-T1-kill
A simple app to calculate the odds of winning in the 1st turn with modern Allosaurus combo.

If you only want the results... well, the chance of winning in T1 is ~~ 3.22%. Mainly because of a lack of free mana (>60% and there is not enough for now in modern).
Moreover, even with dinos and summoners pacts chance to get any of them is ~ 64%; then in 25% there are no evos or green cards to play dino without discarding evo..., and in 35% not enough mana. So i will rather cut the Chancellors from the deck right now (March 2023).

BUT... If you want to play with it go on:

# Getting started

## Packages

First of all you need pandas for data processing. Easiest way is going for pip install.

> pip install pandas

# Running app

The script is easy and strightforward. It takes the decklist from Deck.txt. The format is the same as in the mtg goldfish so you can just copy-paste the imported decklist. Changing it manually is also OK since most of the cards are unnecessary for T1 combo so they are not even taken into account by the script. Anyway look up for typos, but all the necessary combo pieces are already in the file. 

There are only a few cards scripted (see Converter in Game class). If anything important will be added to the deck, it should be scripted there.