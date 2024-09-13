from bitarray import bitarray

class life:
    
#     def __init__():
#         print("I'm alive!")
    
    # def read_grid(filename):
      def __init__(self,filename):
            self.filename = filename
            self.grid = []
         
              with open(filename) as f:
                self.w,self.h = map(int, f.readline().split(maxsplit=1))
        
                 for y in range(self.h + 2):
                    self.grid.append(bitarray(self.w + 2))
        
                 for no, line in enumerate(f):
                     try:
                         y, x = map(int, line.split(maxsplit=1))

                    if y < 0 or x < 0:
                         raise ValueError

                    except ValueError:
                        raise Exception(f"Invalid cell on line {no + 2}.")

                    grid[y + 1][x + 1] = 1

    return grid

# @profile
def tick(self, n=1):
    for i in range:
        for y, row in enumerate(self.grid[1:-1]):
            y2 = y+2
             curr = [0] * (self.w + 2)
            for x, cell in enumerate(row[1:-1]):
                count = self.grid[y][x] + self.grid[y][x+1] +self.grid[y][x+2] + self.grid[y+1][x] +self. grid[y+1][x+2] + self.grid[y+2][x] + self.grid[y+2][x+1]+self.grid [y+2][x+2]
                curr[x+1] = 1 if count == 3 or (cell and count == 2) else 0
            if y > 0:
                 self.grid[y] = prev
                prev = curr
        self.grid[y-1] = curr
             

    return nextgrid

filename = "input_5x5.txt"

grid = read_grid(filename)
print(grid)

nextgrid=tick(grid)
print(nextgrid)






















