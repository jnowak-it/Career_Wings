# 🇵🇱 Ciąg Fibonacciego to sekwencja, w której każda kolejna liczba jest sumą dwóch poprzednich: 1, 1, 2, 3,
# 5, 8, 13... Napisz program, który zwróci listę pierwszych 30 elementów ciągu i przypisze ją do zmiennej
# fibonacci.

# 🇬🇧 The Fibonacci sequence is a sequence in which each next number is the sum of the two preceding ones:
# 1, 1, 2, 3, 5, 8, 13... Write a program that returns a list of the first 30 elements of the sequence and assigns it
# to the variable fibonacci.

num = 30
fibonacci = []
n = 0

while len(fibonacci) < num:
    if n == 0:
        fibonacci.append(0)
    elif n == 1 or n == 2:
        fibonacci.append(1)
    else:
        fibonacci.append(sum(fibonacci[-2:]))
    n += 1

print(fibonacci)
