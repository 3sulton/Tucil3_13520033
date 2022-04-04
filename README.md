# 15-Puzzle Solver
> Sebuah program dalam bahasa python untuk menyelesaikan permainan 15-puzzle dengan menggunakan algoritma Branch and Bound

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Usage](#usage)
* [Running](#running)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
Program ini akan menampilkan langkah langkah penyelesaian 15-puzzles. Langkah langkah tersebut diperoleh dengan menggunakan algoritma Branch and Bound. Nilai bound tiap simpul adalah penjumlahan cost yang diperlukan untuk sampai suatu simpul x dari akar, dengan taksiran cost simpul x untuk sampai ke goal. Taksiran cost yang digunakan adalah jumlah ubin tidak kosong yang tidak berada pada tempat sesuai susunan akhir (goal state)


## Technologies Used
- Python - version 3.9.1
## Usage
- clone repository github ini dengan mengetikkan di CMD

```
git clone https://github.com/3sulton/Tucil3_13520033.git
```
- akan muncul folder my-15-puzzles. Arahkan path pada cmd ke dalam folder `src` tersebut dengan menuliskan `cd Tucil3_13520033/src`

## Running
- setelah cmd berada di dalam folder `src`, ketik command berikut
```
    py main.py
```
- Pengguna dapat memilih untuk mendapatkan puzzle secara random atau dapat menggunakan puzzle sendiri
```
Please enter the method to generate puzzle:
1. Random
2. Manual from file
Your choice: 
```
- Apabila memilih untuk memasukkan puzzle sendiri, buat sebuat file berisi puzzle dengan nomor 1 - 15, slot kosong ditulis dengan huruf x. Contoh:

```
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 x
```
- masukkan file puzzle tersebut ke dalam folder `tests`
- misalkan kita akan menjalankan file puzzle `matriks2.txt` yang berada di dalam folder tests
```
Please enter the method to generate puzzle:
1. Random
2. Manual from file
Your choice: 2
1. Run all the file in the tests folder
2. Run a specific file
Your choice: 2
Please enter the file name: matriks2.txt
```
- program akan menampilkan solusi dari persoalan apabila puzzle dapat dipecahkan

```
====================================
Your puzzle:
+----+----+----+----+
| 01 | 02 | 03 | 04 |
+----+----+----+----+
| 05 | 06 |    | 08 |
+----+----+----+----+
| 09 | 10 | 07 | 11 |
+----+----+----+----+
| 13 | 14 | 15 | 12 |
+----+----+----+----+
====================================
Puzzle Parity:
01 : 0
02 : 0
03 : 0
04 : 0
05 : 0
06 : 0
07 : 0
08 : 1
09 : 1
10 : 1
11 : 0
12 : 0
13 : 1
14 : 1
15 : 1
16 : 9
------------------------------------
sum of kurang: 15
X: 1
sum of kurang + X: 16
====================================

Puzzle can be solved
Start solving...

====================================
Solution found
+----+----+----+----+
| 01 | 02 | 03 | 04 |
+----+----+----+----+
| 05 | 06 |    | 08 |
+----+----+----+----+
| 09 | 10 | 07 | 11 |
+----+----+----+----+
| 13 | 14 | 15 | 12 |
+----+----+----+----+
+----+----+----+----+
| 01 | 02 | 03 | 04 |
+----+----+----+----+
| 05 | 06 | 07 | 08 |
+----+----+----+----+
| 09 | 10 |    | 11 |
+----+----+----+----+
| 13 | 14 | 15 | 12 |
+----+----+----+----+
+----+----+----+----+
| 01 | 02 | 03 | 04 |
+----+----+----+----+
| 05 | 06 | 07 | 08 |
+----+----+----+----+
| 09 | 10 | 11 |    |
+----+----+----+----+
| 13 | 14 | 15 | 12 |
+----+----+----+----+
+----+----+----+----+
| 01 | 02 | 03 | 04 |
+----+----+----+----+
| 05 | 06 | 07 | 08 |
+----+----+----+----+
| 09 | 10 | 11 | 12 |
+----+----+----+----+
| 13 | 14 | 15 |    |
+----+----+----+----+
====================================
--- 0.01699972152709961 seconds ---
Arised Node: 10

```
## Project Status
Project is: _complete_


## Acknowledgements
- Pustaka ini dibuat untuk memenuhi Tugas Kecil 3 IF2211 Strategi Algoritma
- Proyek ini didasarkan pada dokumen [ini](http://www.cs.umsl.edu/~sanjiv/classes/cs5130/lectures/bb.pdf) untuk pemeriksaan reachable puzzle [ini](https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/) untuk pendekatan algoritma branch and bound
- Many thanks to Pak Rinaldi Munir selaku pengajar K03 IF2211 Strategi Algoritma


## Contact
Created by [@3sulton](https://www.github.com/3sulton) - 13520033 / Tri Sulton Adila
