class Result:

    all = [] #this isn't in the read me so we need to go based off the error message. 

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        Result.all.append(self) #this connects to all=[] which should solve our final error message
        
        self.player.results(self) #can also be player.results(self)
        self.player.games_played(game) #need to pass in a game whenever this is initialized. 
        
        self.game.results(self)
        self.game.players(player)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception
        
    @property
    def player (self):
        return self._player
    
    @player.setter
    def player (self, player):
        from classes.player import Player
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception
        
    @property
    def game (self):
        return self._game
    
    @game.setter
    def game (self, game):
        from classes.game import Game
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception
