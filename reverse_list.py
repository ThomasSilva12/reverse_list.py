### Thomas Silva
### ENGR 103 Assignment 7b.
### Nov 15, 2023.



def reverse_list(my_list):

    start_index = 0
    end_index = len(my_list) - 1

    while start_index < end_index:

        my_list[start_index], my_list[end_index] = my_list[end_index], my_list[start_index]

        start_index += 1
        end_index -= 1

my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)
print(my_list)
