# Nested lists

if __name__ == '__main__':

    students = []   
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if len(name) > 0:
            students.append([name, score])
        else:
            print("Values out of pattern. Try again.")
    
    second_highest = sorted(set([score for name, score in students]))[1]
        
    # get number of elements with second highest score
    qtd = sum(1 for name, score in students if score == second_highest)

    #get a list of elements with the same score
    indexes = [idx for idx, element in enumerate(students) if element[1] == second_highest]

    if len(indexes) == 1:
        print(students[indexes[0]][0])
    else:
        # if more than one, get a list of them
        names = []
        for i in indexes:
            names.append(students[i][0])
        names.sort()
        for name in names:
            print(name)

