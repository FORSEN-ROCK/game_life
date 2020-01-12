## At first all code here

## Class of cell
class BaseCell(object):
    def __init__(self, id, is_life=False):
        self._is_life = is_life
        self._id = id

    def __str__(self):
        form = 'x'

        if self._is_life:
            form = '*'

        return form

    def get_is_life(self):
        return self._is_life

    def die(self):
        self._is_life = False

    def revive(self):
        self._is_life = True

    def check_status(self, universe):
        '''This method takes object of class and Universe(place of game)
           It checks rules for cell and desades can this cell die or 
           revive
           Returns true(if the rules are executed)
        '''

        is_executed = True

        return is_executed


def create_universe(cls=BaseCell, source_file='test_universe.txt'):
    '''This function takes two required arguments class of cell and
       source file name

       It reads the file by line and creates cells.

       Required file format:
            1. All lines must be the same length
            2. At the end of line must be '\n'
            3. Bitween lines can't be none-line
            4. The cells are separeted by ' '
            5. If cell is live - *, else - x

       Returns universe (matrix)
    '''

    universe = []
    cell_number = 0 # for id of cell

    file = open(source_file, 'r')
    universe_shot = file.read()

    if len(universe_shot) > 0:
        lines = universe_shot.split('\n')

        for line in lines:
            universe_line = [] # line of cell
            cells = line.split(' ')

            for cell in cells:
                is_life = False

                if cell == '*':
                    is_life = True

                universe_line.append(cls(cell_number, is_life))
                cell_number += 1

            universe.append(universe_line)

    #else:

    return universe

def print_universe(universe, on_display=True, file_name='universe.txt'):
    pass

def game(universe, check_ages=False):
    pass

if __name__ == '__main__':
    universe = create_universe()
    print(universe)
    print(len(universe))