import math

import random

class player:
    def __init__(self, letter):
        #letter is X or O
        self.letter = letter
    def get_move(self, game):
        pass
    #we want all players to get their next move given a game
class randomcomputerplayer(player):#inheritance, adicionando funçoes de outra classe nessa > máquina, essa função diz respeito aos movimentos da máquina
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #pass deve ser utilizado quando queremos que um código seja válido, mas ainda não pretendemos implementá-lo
        square = random.choice(game.available_moves())
        return square

class humanplayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None #Ainda nao tem valor > The None keyword is used to define a null variable or an object  Nota : todas as variaveis com None se referem a ao mesmo objeto
        while not valid_square:
            square = input(self.letter + '\'s turn.input move (0-8):>')#aqui diz para escolher um numero para colocar o X ou O.
            #we're going to check that this is a correct value by trying to cast
            #it to an integer, and if it's not, then we say its invalid
            #if that spot is not available on the board, we also say its invalid, i'll do this in the code below

            try:
                val = int(square)
                if val not in game.available_moves(): # se o valor que coloquei em val (que era nulo) não for integer : mostrar erro de valor
                    raise ValueError #Aqui forçamos o erro a ocorrer .The raise statement allows the programmer to force a specific exception to occur.
                valid_square = True

            except ValueError:#E aqui pegamos o erro que forçamos a ocorrer e printamos 'invalid square. try again '.
                print('Invalid square. Try again')

        return val #retornando valor (número) para o movimento.


