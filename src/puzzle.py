import numpy as np
from queue import PriorityQueue
import datetime

goal = np.arange(1,17).reshape(4,4)

class node:
  # merepresentasikan node pada tree yang terbentuk
  def __init__(self, matrix, level, parent, move):
    self.matrix = matrix
    self.level = level
    self.parent = parent
    self.move = move
    self.cost = self.calculateCost()
  
  def __lt__(self, other):
    # digunakan untuk priority queue
    return self.cost < other.cost

  def calculateCost(self):
    # menghitung taksiran ongkos dari simpul
    count = self.level
    for i in range(4):
      for j in range(4):
        if (self.matrix[i][j] != goal[i][j] and self.matrix[i][j] != 16):
          count += 1
    return count

  def createNode(self, move):
    # membuat child node berdasarkan move masukan
    mat = np.copy(self.matrix)
    idx_kosong = np.where(mat == 16)
    row = idx_kosong[0][0]
    col = idx_kosong[1][0]
    if (move == "up"):
      mat[row][col], mat[row-1][col] = mat[row-1][col], mat[row][col]
    elif (move == "down"):
      mat[row][col], mat[row+1][col] = mat[row+1][col], mat[row][col]
    elif (move == "left"):
      mat[row][col], mat[row][col-1] = mat[row][col-1], mat[row][col]
    elif (move == "right"):
      mat[row][col], mat[row][col+1] = mat[row][col+1], mat[row][col]
    
    level = self.level + 1
    newNode = node(mat, level, self, move)
    return newNode

  def possibleMove(self):
    # mengembalikan move yang dapat dilakukan
    moves = ["up", "down", "left", "right"]
    # agar tidak kembali ke posisi sebelumnya
    if (self.move == "up") : moves.remove("down")
    elif (self.move == "down") : moves.remove("up")
    elif (self.move == "left") : moves.remove("right")
    elif (self.move == "right") : moves.remove("left")

    idx_kosong = np.where(self.matrix == 16)
    # hapus move yang tidak valid
    if (idx_kosong[0][0] == 0):
      if "up" in moves:
        moves.remove("up")
    if (idx_kosong[0][0] == 3):
      if "down" in moves:
        moves.remove("down")
    if (idx_kosong[1][0] == 0):
      if "left" in moves:
        moves.remove("left")
    if (idx_kosong[1][0] == 3):
      if "right" in moves:
        moves.remove("right")
    
    return moves

  def isMatrixSame(self, mat):
    # mengecek apakah sama dengan matrix mat
    return (self.matrix == mat).all()

  def checkPuzzle(self):
    # mengecek apakah node merupakan goal node
    return self.isMatrixSame(goal)
  
  def displayPath(self):
    # menampilkan urutan matriks dari posisi awal ke posisi akhir
    if (self.parent):
      # print("Langkah:", self.move)
      self.parent.displayPath()
      print("\n==============")
      string = "MOVE " + self.move.upper()
      print(f"{string:^14}")
      print("--------------")
    displayMatrix(self.matrix)

def displayMatrix(mat):
  # menampilkan matrix
  for i in range(4):
    for j in range(4):
      if (mat[i][j] == 16):
        print("   ", end= "")
      else:
        print("{:3}".format(mat[i][j]), end= "")
    print()

def Kurang(i, mat):
  # menghitung banyaknya ubin bernomor j sedemikian sehingga j < 1 dan POSISI(j) > POSISI(i)
  arr = mat.reshape(-1)
  idx = np.where(arr == i)
  count = 0
  for a in range(idx[0][0]+1, 16):
    if (arr[a] < i):
      count += 1
  return count

def valueX(mat):
  # menentukan nilai X berdasarkan posisi awal sel kosong
  idx_kosong = np.where(mat == 16)
  if ((idx_kosong[0][0] + idx_kosong[1][0]) % 2 == 1):
    return 1
  return 0

def sumKurangPlusX(mat):
  # menghitung nilai dari ΣKurang(i) + X
  sum = valueX(mat)
  for i in range(1,17):
    sum += Kurang(i, mat)
  return sum

def isReachable(mat):
  # menentukan apakah puzzle dapat diselesaikan berdasarkan nilai ΣKurang(i) + X
  return (sumKurangPlusX(mat) % 2 == 0)

def hasChecked(currNode, checked):
  # mengecek apakah node telah diperiksa sebelumnya
  for mat in checked:
    if (currNode.isMatrixSame(mat)):
      return True
  return False

def solvePuzzle(puzzle):
  # menampilkan matriks posisi awal 15-puzzle
  print("\nMatriks posisi awal:")
  displayMatrix(puzzle)
  
  # nilai dari fungsi Kurang(i) untuk setiap ubin tidak kosong pada posisi awal
  print("\nNilai dari fungsi Kurang(i) untuk setiap ubin:")
  for i in range(1,17):
    print("Kurang({}) = {}".format(i, Kurang(i, puzzle)))

  # nilai dari ΣKurang(i) + X
  print("\nNilai dari ΣKurang(i) + X adalah", sumKurangPlusX(puzzle))

  startTime = datetime.datetime.now()
  if (isReachable(puzzle)):
    root = node(puzzle, 0, None, "-")
    liveNodes = PriorityQueue()
    liveNodes.put(root)
    checked = []
    moves = root.possibleMove()
    countNode = 1
    
    while (True):
      currNode = liveNodes.get()
      checked.append(currNode.matrix)

      if (not(currNode.checkPuzzle())):
        moves = currNode.possibleMove()
        for move in moves:
          newNode = currNode.createNode(move)
          countNode += 1
          if (not(hasChecked(newNode, checked))):
            liveNodes.put(newNode)
      else: # goal node ditemukan
        break

      if (liveNodes.empty()):
        break
    
    endTime = datetime.datetime.now()
    if (currNode.checkPuzzle()): # goal node ditemukan
      # menampilkan urutan matriks dari posisi awal hingga akhir
      print("\nUrutan matriks dari posisi awal hingga akhir:\n")
      currNode.displayPath()
      print("\nPuzzle berhasil diselesaikan!")
      # waktu eksekusi program
      executionTime = (endTime - startTime).total_seconds() * 1000
      print("Waktu eksekusi program adalah", executionTime, "milliseconds")
      # jumlah simpul yang dibangkitkan
      print("Jumlah simpul yang dibangkitkan sebanyak", countNode)

  else:
    print("Puzzle tidak dapat diselesaikan")