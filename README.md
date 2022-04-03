# Tugas Kecil 3 IF2211 Strategi Algoritma

**Dibuat oleh:** <br>
Flavia Beatrix Leoni A. S. - 13520051

## Deskripsi Singkat
Merupakan program dalam bahasa Python yang dapat digunakan untuk menyelesaikan persoalan 15-Puzzle dengan Algoritma Branch and Bound. Posisi awal persoalan 15-puzzle dapat dimasukkan dari file teks dan/atau dibangkitkan secara acak oleh program. Program akan menampilkan apakah puzzle dapat diselesaikan atau tidak dapat diselesaikan. Apabila persoalan dapat diselesaikan, program akan menampilkan urutan matriks dari posisi awal hingga posisi akhir beserta waktu eksekusi program dan jumlah simpul yang dibangkitkan.

## Requirement
- Python
- Library numpy, dapat di-install dengan menuliskan command berikut pada terminal
```
pip install numpy
```

## Cara Menggunakan
1. Pastikan semua requirement telah terinstall dengan baik
2. Buka terminal pada folder src
3. Jalankan program dengan menuliskan command berikut pada terminal
```
py main.py
```
4. Apabila pengguna ingin memberi masukan posisi awal 15-puzzle, buatlah sebuah file teks pada folder test dan tuliskan matriks yang merepresentasikan posisi awal persoalan 15-puzzle di dalamnya. Perhatikan bahwa sel kosong direpresentasikan dengan angka 16. Berikut merupakan contoh isi file `success1.txt`
```
1 2 3 4
5 6 16 8
9 10 7 11
13 14 15 12
```
5. Tulis masukan nama file pada program, seperti `success1.txt`
6. Program akan menampilkan hasil penyelesaian 15-puzzle