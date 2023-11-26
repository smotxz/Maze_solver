from gui import Line, Point

class Cell:

    def __init__(self, win=None):
        self.left_wall = True
        self.right_wall = True
        self.top = True
        self.bottom = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1 , y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.left_wall: 
            self._win.draw_line(Line(Point(x1, y1),Point(x1, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y1),Point(x1, y2)), "white")
        if self.right_wall:
            self._win.draw_line(Line(Point(x2,y1),Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x2,y1),Point(x2, y2)), "white")
        if self.top:
            self._win.draw_line(Line(Point(x1,y1),Point(x2, y1)))
        else:
            self._win.draw_line(Line(Point(x1,y1),Point(x2, y1)),"white")
        if self.bottom:
            self._win.draw_line(Line(Point(x1, y2),Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y2),Point(x2, y2)), "white" )


    def draw_move(self, next_cell, undo = False):
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        next_x = (next_cell._x1 + next_cell._x2)/2
        next_y = (next_cell._y1 + next_cell._y2)/2
        
        fill_color = "red"
        if undo:
            fill_color = "gray"

        if self._x1 > next_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(next_x, next_y), Point(next_cell._x2, next_y))
            self._win.draw_line(line, fill_color)

        elif self._x1 < next_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(next_cell._x1, next_y), Point(next_x, next_y))
            self._win.draw_line(line, fill_color)

        elif self._y1 > next_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(next_x, next_cell._y2), Point(next_x, next_y))
            self._win.draw_line(line, fill_color)


        elif self._y1 < next_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(next_x, next_y), Point(next_x, next_cell._y1))
            self._win.draw_line(line, fill_color)

       