
from pygame import draw


UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3


class Player:
    """A snake controlled by a player"""

    # Member variables
    __body_positions = []  # A list of tuples containing x and y coordinates of each segment of the snake
    __color = ()           # The color of the snake
    __size = 0             # The size of each segment in the snake
    __direction = 0        # The direction the snake is moving

    def __init__(self, start_pos, color, size=10, direction=UP):
        """Constructor"""
        self.__body_positions = [start_pos,
                                (start_pos[0], start_pos[1] + size),
                                (start_pos[0], start_pos[1] + size * 2),
                                (start_pos[0], start_pos[1] + size * 3)]
        self.__color = color
        self.__size = size
        self.__direction = direction

    def add_segment(self):
        """Adds a new segment to the end of the snake"""
        self.__body_positions.append(self.__body_positions[-1])

    def is_colliding(self, positions):
        """Returns True if the snake's head collides with any of the given positions"""
        if self.__body_positions[0] in positions:
            return True
        else:
            return False

    def draw(self, surface):
        """Draws all of the snake segments onto the given surface"""
        for pos in self.__body_positions:
            draw.rect(surface, self.__color, (pos[0], pos[1], self.__size, self.__size))

    def get_body_positions(self):
        """Returns the list of segements of the snake"""
        return self.__body_positions

    def get_color(self):
        """Returns the color of the snake"""
        return self.__color

    def get_direction(self):
        """Returns the direction that the snake is moving"""
        return self.__direction

    def get_size(self):
        """Returns the size of the snake"""
        return self.__size

    def move(self):
        """Moves the snake in whatever direction it's facing"""
        for i in range(len(self.__body_positions) - 1, -1, -1):
            # Update the positions
            if i == 0:
                if self.__direction == UP:
                    self.__body_positions[i] = (self.__body_positions[i][0], self.__body_positions[i][1] - self.__size)
                elif self.__direction == LEFT:
                    self.__body_positions[i] = (self.__body_positions[i][0] - self.__size, self.__body_positions[i][1])
                elif self.__direction == DOWN:
                    self.__body_positions[i] = (self.__body_positions[i][0], self.__body_positions[i][1] + self.__size)
                elif self.__direction == RIGHT:
                    self.__body_positions[i] = (self.__body_positions[i][0] + self.__size, self.__body_positions[i][1])
            else:
                self.__body_positions[i] = self.__body_positions[i - 1]

    def set_direction(self, direction):
        """Changes the direction the snake is moving to the given direction"""
        self.__direction = direction
