import sys, os, random, time

class Board:
    def __init__(self, size):
        # Tamanho do tabuleiro (size x size)
        self.size = size
        # Tabuleiro, preenchido com False inicialmente
        self.board = [[False for j in range(self.size)] for i in range(self.size)]
        # Contagem de tempo para impressão no terminal
        self.time = time.time()
        # Comando de limpeza do terminal
        self.cmd_clear = "cls" if os.name == "nt" else "clear"

        # Início
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
        # Caso tenha passado da última coluna, retorna, uma vez que não há mais casas para verificar
        if col >= self.size:
            return True

        # Primeira coluna: É selecionada uma linha aleatoriamente
        if col == 0:
            i = random.randint(0, self.size - 1)
            self.board[i][col] = True
        
        for i in range(self.size):
            if self.is_safe(i, col):
                if col != 0:
                    self.board[i][col] = True
                # Impressão no terminal, 30 vezes por segundo
                if time.time() - self.time > 0.03:
                    self.time = time.time()
                    os.system(self.cmd_clear)
                    print(self)
                # Verifica a próxima coluna    
                if self.find_positions(col+1):
                    return True
                # Volta atrás (backtracking) caso não haja casa segura para a rainha
                self.board[i][col] = False
        return False

    def is_safe(self, row, col):
        # Verifica na mesma coluna
        for i in range(col):
            if self.board[row][i]:
                return False
            
        # Verifica na diagonal superior para a esquerda
        i = row
        j = col
        while i >= 0 and j >= 0:
            if self.board[i][j]:
                return False
            i -= 1
            j -= 1
        
        # Verifica na diagonal inferior para a esquerda
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
