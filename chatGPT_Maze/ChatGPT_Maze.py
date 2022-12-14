import turtle, random
# 1 = open up, 2 = open down, 3 = open right, 4 = open left

grid_width, grid_height = 10, 10

class WallPiece:
  def __init__(self):
    self.turtle = turtle.Turtle()
    self.open_walls = {"up": False, "down": False, "left": False, "right": False}


class Grid:
  def __init__(self, grid_width, grid_height):
    # create a 10x10 grid of WallPiece instances
    self.grid = [[WallPiece() for i in range(10)] for j in range(10)]
    self.end_x, self.end_y = grid_width/2, grid_height/2
    self.grid_width, self.grid_height = grid_width, grid_height

    # set the ending position of the grid
    self.set_ending_position()

    # set the entrance of the grid
    self.set_entrance()

  def set_ending_position(self):
    # set the type of the middle 2x2 to "ending"
    for i in range(self.end_x-1, self.end_x+1):
      for j  in range(self.end_y-1, self.end_y+1):
        self.grid[self.start_x][self.start_y].type = "ending"

  def set_entrance(self):
    # choose a random entrance
    entrance = random.choice([(0, random.randint(0, self.grid_height-1)), (self.grid_width-1, random.randint(0, self.grid_height-1)), (random.randint(0, self.grid_width-1), 0), (random.randint(0, self.grid_width-1), self.grid_height-1)])
    self.start_x, self.start_y = entrance
    if self.start_x == 0:
      self.grid[self.start_x][self.start_y].open_walls["up"] = True
    elif self.start_x == 9:
      self.grid[self.start_x][self.start_y].open_walls["down"] = True
    elif self.start_y == 0:
      self.grid[self.start_x][self.start_y].open_walls["right"] = True
    elif self.start_y == 9:
      self.grid[self.start_x][self.start_y].open_walls["left"] = True
    # set the open_side and type of the entrance
    
  def generate_exit(self):
    possible_moves = ["up", "down", "left", "right"]
    self.safe_path = []
    current_x, current_y = game_grid.start_x, game_grid.start_y

    while (current_x, current_y) != (game_grid.end_x, game_grid.end_y):
      # choose a random move
      move = random.choice(possible_moves)
      
      # update the current position based on the move
      if move == "up":
          current_y = max(current_y - 1, 0)  # make sure not to go past the grid bounds
      elif move == "down":
          current_y = min(current_y + 1, self.grid_height - 1)  # make sure not to go past the grid bounds
      elif move == "left":
          current_x = max(current_x - 1, 0)  # make sure not to go past the grid bounds
      elif move == "right":
          current_x = min(current_x + 1, self.grid_width - 1)  # make sure not to go past the grid bounds
      self.grid[current_x][current_y].open_walls[move] = True
          
      # add the move to the path
      self.safe_path.append(move)

game_grid = Grid(grid_width, grid_height)

