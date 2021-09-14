import main

import time
from main import humanplayer, randomcomputerplayer, player

class tictactoe():
    def __init__(self):
        self.board = self.make_board() # we will use a single list to rep 3x3 board
        self.current_winner = None  #keep track winner

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board (self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:#THIS IS INDEXING INTO OUR LENTH NINE LIST #ROW É FILEIRA. PARA CADA FILEIRA EM [....]
            print('| ' + '| '.join(row) + ' |')# PARA CADA FILEIRA VAMOS PRINTAR OS SEPARADORES, E JUNTA-LOS (.JOIN(ROW))
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' |'.join(row) + ' |')


    def make_move(self, square, letter):
            #if valid move, then make the move(assign square to letter
            #then return true. if invalid, return false
            if self.board[square] == ' ': # definindo self.board[square] como ' '
                self.board[square] = letter # colocando a letra no lugar do espaço
                if self.winner(square, letter): # if it's true, then...
                    self.current_winner = letter
                return True
            return False



    def winner (self, square, letter ):
        #winner if 3 in a row anywhere
        #first let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) *3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind +i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals
        #but only if the square is an even number (0,2,4,6)
        #these are the only moves possible to win a diagonal
        if square % 2 == 0 :
            diagonal1 = [self.board[i] for i in [0,4,8]] # left to right diagonal
            if all ([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] # right to left diagonal
            if all ([spot == letter for spot in diagonal2]):
                return True

        return False


    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')#Isso vai contar o numero de espaços na borda(espaços diponiveis)

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']  # Enumerate is going to essencially create a list and assign tuples that have the index comma the value at that index for x, x; é o metodo para enumerar, um loop para enumerar todos os locais ' ' de self.board
        # exemplo : i, spot in enumerate - vai enumerar os locais ' ', ja que spot veio dps do "i," e spot está definido como ' '  for (i, x) in enumerate(self.board):
        # ['x', 'x', 'o'] -->[(0, 'x'), (1, 'x'), (2, 'o')]
        '''
        Linha inutilizada abaixo indica outro modo de escrever o codigo acima ( return i for.....)
        moves = [] 
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append[i]

        return moves
        '''

def play(game, x_player, o_player, print_game = True)  :
    # returns the winner of the game(the letter)or None for a tie
    if print_game:
        game.print_board_nums()


    letter = 'X' #starting letter
    # iterate while the game stil has empty squares
    #(we don't have to worry about winner because we'll  just return that
    #which breaks the loop)
    while game.empty_squares():#enquanto o jogo ainda tem locais (quadrados) vazios: continuar
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)

        else:
            square = x_player.get_move(game)

        # let's define a function to make a move!
        if game.make_move(square, letter): # Se make move é valido, lembrando que make move é valido apenas quando retorna True.
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()#aqui queremos ver a nova representaçao da borda dps do local ser preenchido
                print(' ')

            if game.current_winner:
                if print_game:
                    print(letter + ' Player wins!')

                return letter

            letter = 'O' if letter == 'X' else 'X' # that's a list comprehension
            ''' 
            Outra forma de escrever isso seria :
            if letter == 'X':
                letter = 'O'
                
            else :
                letter = 'X'
                
            '''

            time.sleep(.9) # tempo de resposta
            
                

    if print_game:
            print('It\'s a tie !')



if __name__ == '__main__':
    x_player = randomcomputerplayer('X')
    o_player = humanplayer('O')
    t = tictactoe()
    play(t, x_player, o_player, print_game=True)