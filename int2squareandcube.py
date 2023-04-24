#function for squaring numbers
def square(x):
    return x ** 2
#function for cubing numbers
def cube(x):
    return x ** 3

#open integers.txt for reading
with open("integers.txt") as my_file:
    numbers = my_file.read().split()
#create lists for even and odd numbers
even_numbers = []
odd_numbers = []
#check each number and sort them in the lists
for i in numbers:
#if even add in even number list
    if int(i) % 2 == 0:
        even_numbers.append(i)
#if odd add in odd number list
    else:
        odd_numbers.append(i)
#create double.txt for even numbers getting square
with open("double.txt", "w") as double_file:
    for even in even_numbers:
        double_file.write(square(even) + "\n")
#create triple.txt for odd numbers getting cube
with open("triple.txt", "w") as triple_file:
    for odd in odd_numbers:
        triple_file.write(square(odd) + "\n")