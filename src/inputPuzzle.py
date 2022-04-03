import numpy as np

goal = np.arange(1,17).reshape(4,4)

def isPuzzleValid(puzzle):
  # mengecek apakah puzzle masukan merupakan puzzle yang valid
  arr = (np.sort(puzzle, axis=None)).reshape(4,4)
  return (arr == goal).all()

def inputPuzzle():
  print("Pilih cara untuk memberi masukan puzzle:")
  print("1. Dari file teks masukan")
  print("2. Dibangkitkan secara acak oleh program")

  try:
    opt = int(input(" > "))
    if (opt == 1):
      # input dari file
      print("\n*NOTE: posisi ubin kosong direpresentasikan dengan 16 pada file teks")
      filename = "../test/" + input("Masukkan nama file: ")
      return readFile(filename)

    elif (opt == 2):
      # posisi awal puzzle dibangkitkan secara acak
      puzzle = np.arange(1,17)
      np.random.shuffle(puzzle)
      puzzle = puzzle.reshape(4,4)
      return puzzle

    else:
      print("Masukan tidak valid!\n")
      return inputPuzzle()

  except:
    print("Masukan tidak valid!\n")
    return inputPuzzle()

def readFile(filename):
  # membaca matrix dari file teks masukan
  try:
    with open(filename) as file:
      puzzle = np.zeros([4,4], dtype = "int")
      for i in range(4):
        line = file.readline().split()
        for j in range(4):
          puzzle[i][j] = int(line[j])
      if (isPuzzleValid(puzzle)):
        return puzzle
      else:
        print("Puzzle tidak valid!\n")
        return inputPuzzle()

  except FileNotFoundError:
    print("File tidak ditemukan!\n")
    return inputPuzzle()