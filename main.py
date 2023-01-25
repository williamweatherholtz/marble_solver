import numpy as np
from dataclasses import dataclass

@dataclass
class Move:
    start: int
    end: int


@dataclass
class Position:
    '''
    i.e. a specific layout of pieces that can be objectively scored, not an x,y coordinate
    '''
    board: np.ndarray
    movelist: list


class Board:
    def __init__(self, size, invalids=None, empties=None):
        '''
        assume it's square if no empties or invalids are provided
        though there should always be one empty, I suppose
        '''
        if invalids is None:
            invalids = []
        if empties is None:
            empties = []
        
        self.array = np.ones(size)

        for idx in invalids:
            self.array[idx] = None

        for idx in empties:
            self.array[idx] = 0

        # a list of positions and methods to reach
        self.positions = []

    def __repr__(self):
        return str(self.array)

    def solve(self):
        pass

    @static_method
    def find_candidate_moves(self):
        '''
        Find each empty space, and see if there is a 1->1->0 sequence starting at it.
        If so, then it is a valid move.  A move will result in a 0->0->1 in these
        cells.
        '''
        zero_rs, zero_cs = np.where(self.array == 0)

        moves = []
        
        for r, c in zip(zero_rs, zero_cs):
            # try the 4 cardinal directions for candidate moves
            print (r, c)

            #try North
            if np.array_equal(self.array[r, c-2:c+1],
                              np.array([1, 1, 0])):
                moves.append(Move(start=(r, c), end=(r, c-3)))
                
                self.positions
                #print("N")
                
            # S
            if np.array_equal(self.array[r, c:c+3],
                              np.array([0, 1, 1])):
                moves.append(Move(start=(r, c), end=(r, c+3)))
                #print("s")

            # E
            if np.array_equal(self.array[r:r+3, c],
                              np.array([0, 1, 1])):
                moves.append(Move(start=(r, c), end=(r+3, c)))
                #print("e")

            # W
            if np.array_equal(self.array[r-2:r+1, c],
                              np.array([1, 1, 0])):
                moves.append(Move(start=(r, c), end=(r-3, c)))
                #print("W")

        print (moves)

        

        
if __name__ == '__main__':
    shape = (7, 7)

    #there are L-shaped slots missing in each corner
    invalids = [ (0,0), (1, 0), (0, 1),
                 (0,6), (0, 5), (1, 6),
                 (6,0), (6, 1), (5, 0),                 
                 (6,6), (6, 5), (5, 6)]

    empties = [(3, 3)]
    
    board = Board(shape, invalids, empties)
    print(board)
    board.find_candidate_moves()
