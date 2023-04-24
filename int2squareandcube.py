#open integers.txt for reading
with open("integers.txt") as my_file:
    numbers = my_file.read().split()
#create lists for even and odd numbers
even_numbers = []
odd_numbers = []
#check each number and sort them in the lists
#create double.txt for even numbers getting square
#create triple.txt for odd numbers getting cube