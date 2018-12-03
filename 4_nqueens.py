import sys, os, random, time

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[False for j in range(self.size)] for i in range(self.size)]
        self.time = time.time()
        self.cmd_clear = "cls" if os.name == "nt" else "clear"
        os.system(self.cmd_clear)
        if self.find_positions():
            os.system(self.cmd_clear)
            print(self)
        else:
            os.system(self.cmd_clear)
            print("Solucao nao encontrada. Ultimo estado:")
            print(self)

    def __str__(self):
        s = ""
        for i in range(self.size):
            for j in range(self.size):
                s += "|"
                s += "X" if self.board[i][j] else " "
            s += "|" + os.linesep
        return s

    def find_positions(self, col = 0):
        if col >= self.size:
            return True

        if col == 0:
            i = random.randint(0, self.size - 1)
            self.board[i][col] = True
        
        for i in range(self.size):
            if self.is_safe(i, col):
                if col != 0:
                    self.board[i][col] = True
                if time.time() - self.time > 0.03:
                    self.time = time.time()
                    os.system(self.cmd_clear)
                    print(self)
                if self.find_positions(col+1):
                    return True
                self.board[i][col] = False
        return False

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i]:
                return False
            
        i = row
        j = col
        while i >= 0 and j >= 0:
            if self.board[i][j]:
                return False
            i -= 1
            j -= 1
        
        i = row
        j = col
        while i < self.size and j >= 0:
            if self.board[i][j]:
                return False
            i += 1
            j -= 1
        
        return True


if len(sys.argv) < 2:
    print("Uso: " + sys.argv[0] + " quantidade_de_rainhas")
    quit()

Board(int(sys.argv[1]))
