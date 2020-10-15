# Write a program which asks the user for student grades until the user types "done".
# The program should then compute the mean and median grades for all the students, rounded to two decimal places.
# See the instructions for further details.

def run():
    getting_input = True
    output = []
    while getting_input:
        inp = input("Next grade: ")
        output.append(inp)
        if inp == "done":
            getting_input = False
    x = output[:-1]
    float_list = []
    for i in x:
        float_list.append(float(i))
    #Mean
    add = 0
    for i in range(0, len(float_list)):
        add = add + float_list[i]
        mean = add / len(float_list)
    mean_format = round(mean, 2)

    print("Mean: " + str(mean_format))

    #Median
    sorted_list = sorted(float_list)
    if len(sorted_list) == 1:
        new = ''
        for i in sorted_list:
            new += str(i)
        print("Median: " + str(new))
    elif len(sorted_list) % 2 == 0:
        middle = int((len(sorted_list)) / 2)
        print(middle)
        l = sorted_list[middle - 1 :middle + 1]
        print(l)
        add = 0
        for i in range(0, len(l)):
            add = add + l[i]
            divide = add / 2
        p = round(divide, 2)
        print("Median: " + str(p))
    else:
        w = int(len(sorted_list) / 2)
        q = sorted_list[w]
        e = round(q, 2)
        print("Median: " + str(e))
    
    


if __name__ == "__main__":
    run()