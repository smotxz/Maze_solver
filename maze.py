from cell import Cell

import random
import time

class Maze:
    def __init__(
        self, x1 , y1, num_rows, num_col, 
        cell_size_x, cell_size_y,win=None, 
        seed=None
    ):
        self.cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_col
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._brake_entrence_and_exit()
        self._brake_walls_r(0,0)
        self._reset_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self.cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _brake_entrence_and_exit(self):
        self.cells[0][0].top = False
        self._draw_cell(0,0)
        self.cells[self.num_cols -1][self.num_rows -1].bottom = False
        self._draw_cell(self.num_cols -1,self.num_rows-1)

    def _brake_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            need_to_visit = []

            if i > 0 and not self.cells[i-1][j].visited:
                need_to_visit.append((i-1, j))
           
            if i < self.num_cols - 1 and not self.cells[i+1][j].visited:
                need_to_visit.append((i+1,j))

            if j > 0 and not self.cells[i][j-1].visited:
                need_to_visit.append((i, j-1))
            
            if j< self.num_rows -1 and not self.cells[i][j+1].visited:
                need_to_visit.append((i, j + 1))

            if len(need_to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            direction_idx = random.randrange(len(need_to_visit))
            next_idx = need_to_visit[direction_idx]

            if next_idx[0] == i + 1:
                self.cells[i][j].right_wall = False
                self.cells[i + 1][j].left_wall = False
            
            if next_idx[0] == i -1 :
                self.cells[i][j].left_wall = False
                self.cells[i - 1][j].right_wall = False
            
            if next_idx[1] == j + 1 :
                self.cells[i][j].bottom = False
                self.cells[i][j + 1].top = False
            
            if next_idx[1] == j - 1 :
                self.cells[i][j].top = False
                self.cells[i][j - 1].bottom = False
            
            self._brake_walls_r(next_idx[0], next_idx[1])
    
    def _reset_visited(self):
        for i in range(self.num_cols):
            for j in range( self.num_rows):
                
                self.cells[i][j].visited = False
    

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()

        self.cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True 

        if i > 0 and not self.cells[i][j].left_wall and not self.cells[i-1][j].visited:
            self.cells[i][j].draw_move(self.cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i-1][j], True)

        if  i < self.num_cols - 1 and not self.cells[i][j].right_wall and not self.cells[i + 1][j].visited:
            self.cells[i][j].draw_move(self.cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i + 1][j], True)


        if j > 0 and not self.cells[i][j].top and not self.cells[i][j - 1].visited:
            self.cells[i][j].draw_move(self.cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j - 1], True)

        if j < self.num_rows - 1 and not self.cells[i][j].bottom and not self.cells[i][j + 1].visited :
            self.cells[i][j].draw_move(self.cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j + 1], True)

        return False


            
            