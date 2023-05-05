import random

class Game:
    def __init__(self):
        self.life: int = 20
        self.win: bool = False
        self.hand: list = []
        self.Allosaurus: int = 0
        self.Evo_neoform: int = 0
        self.Evo_eldritch: int = 0
        self.noEvo: bool = False
        self.g_cards: int = 0
        self.g_lands: int = 0
        self.ug_lands: int = 0
        self.free_mana: int = 0

    def __str__(self):
        return f"""
                There is {self.Allosaurus} allosaurus, {self.free_mana} free mana, and {self.ug_lands} U/G lands to go on.
                Evos: {self.Evo_neoform} neoforms and {self.Evo_eldritch} eldritch.
                """

    def Game_setup(self, deck, handsize):
        self.life = 20
        self.hand = []
        self.win = False
        self.Allosaurus = 0
        self.Evo_neoform = 0
        self.Evo_eldritch = 0
        self.noEvo = False
        self.g_cards = 0
        self.g_lands = 0
        self.ug_lands = 0
        self.free_mana = 0
        #Itterating through hand to get the game stat
        self.hand = random.choices(deck, k=handsize)
        for cards in self.hand:
            self.Converter(cards) #Using external converter to update the state of the game.

    def Converter(self, card):
    
        #Lands

        ## Fetches
        if card == "Misty Rainforest":
            self.ug_lands += 1
            self.g_lands += 1
        elif card == "Windswept Heath":
            self.ug_lands += 1
            self.g_lands += 1
        elif card == "Wooded Foothills":
            self.ug_lands += 1
            self.g_lands += 1  

        ## Duals

        elif card == "Botanical Sanctum":
            self.ug_lands += 1
            self.g_lands += 1

        elif card == "Breeding Pool":
            self.ug_lands += 1
            self.g_lands += 1

        elif card == "Waterlogged Grove":
            self.ug_lands += 1  
            self.g_lands += 1

        elif card == "Gemstone Mine":
            self.ug_lands += 1
            self.g_lands += 1 


        ## monoG lands

        elif card == "Forest":
            self.g_lands += 1

        elif card == "Snow-Covered Forest":
            self.g_lands += 1

        # Turntimber
        elif card == "Turntimber Symbiosis":
            self.g_lands += 1
            self.g_cards += 1

        # Chancellor

        elif card == "Chancellor of the Tangle":
            self.free_mana += 1
            self.g_cards += 1
            
        ## Evo

        elif card == "Neoform":
            self.Evo_neoform += 1
            self.g_cards += 1

        elif card == "Eldritch Evolution":
            self.Evo_eldritch += 1
            self.g_cards += 1
            
        # Allosaurus

        elif card == "Allosaurus Rider":
            self.Allosaurus += 1
            self.g_cards += 1

        elif card == "Summoner's Pact":
            self.Allosaurus += 1
            self.g_cards += 1

        # other green cards

        elif card == "Autochthon Wurm":
            self.g_cards += 1

        elif card == "Edge of Autumn":
            self.g_cards += 1

        elif card == "Life Goes On":
            self.g_cards += 1

        elif card == "Manamorphose":
            self.g_cards += 1

        elif card == "Nourishing Shoal":
            self.g_cards += 1

        elif card == "Once Upon a Time":
            self.g_cards += 1

        elif card == "Veil of Summer":
            self.g_cards += 1

        elif card == "Wild Cantor":
            self.g_cards += 1

    def Combo(self):
    
        if self.Allosaurus > 0:
            if self.Evo_eldritch > 0:
                if self.g_lands > 0 and self.free_mana >= 2:
                    if self.g_cards >= 6:
                        self.win = True
                if self.g_lands == 0 and self.free_mana >= 3:
                    if self.g_cards >= 7:
                        self.win = True
            elif self.Evo_neoform > 0:
                if self.ug_lands > 0 and self.free_mana >= 1:
                    if self.g_cards >= 5:
                        self.win = True
            else: self.noEvo = True
        

        #while mana > 0:

class Test:
    def __init__(self, deck=None):
        self.deck = deck
        self.win: int
        self.games: int
        self.grizzlehands: int
        self.noAllosaurus: int
        self.noChancellor: int
        self.noEvo: int
        self.window: Tk()

    def __str__(self):
        ratio_win = (self.win/self.games)*100
        ratio_noallo = (self.noAllosaurus/self.games)*100
        ratio_noevo = (self.noEvo/self.games)*100
        ratio_nochan = (self.noChancellor/self.games)*100
        return f"""
                With this deck without mulligans you should win {self.win} out of {self.games} games. This is {ratio_win}%.
                In {self.noAllosaurus} ({ratio_noallo}%) games there was no dino.
                In {self.noEvo} ({ratio_noevo}%) games there was a dino but no evos
                In {self.noChancellor} ({ratio_nochan}%) games there was no free mana.
                """

    def Test_go(self, deck, i, handsize):
        self.deck = deck
        self.win = 0
        self.games= 0
        self.grizzlehands= 0
        self.noAllosaurus = 0
        self.noChancellor = 0
        self.noEvo = 0

        for a in range(i):
            self.games += 1
            Current_game = Game()
            #hand = ['Eldritch Evolution', 'Neoform', 'Chancellor of the Tangle', 'Chancellor of the Tangle', 'Botanical Sanctum', 'Allosaurus Rider', 'Allosaurus Rider']
            Current_game.Game_setup(self.deck, handsize)
            Current_game.Combo()
            if Current_game.Allosaurus == 0: self.noAllosaurus += 1
            if Current_game.noEvo == True: self.noEvo += 1
            if Current_game.free_mana == 0: self.noChancellor += 1
            if Current_game.win == True: 
                self.win += 1
            #print(Current_game.hand) # if you want detailed info about each game
            #print(Current_game)
            
              
        print("Done!")