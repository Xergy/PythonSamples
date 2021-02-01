
number_inputs = 3
truths = list(itertools.product([True, False], repeat=number_inputs))

for truth in truths:
    position = 0
    if number_inputs == 1:
        p = truth[0] 
    elif number_inputs == 2:
        p, q = truth[0], truth[1]
    elif number_inputs == 3:
        p, q, r = truth[0], truth[1], truth[2]
    elif number_inputs == 4:
        p, q, r, s = truth[0], truth[1], truth[2], truth[3]
    else:
        p, q, r, s, t = truth[0], truth[1], truth[2], truth[3], truth[4]
        position = 0

    #print("-" * 20 * number_inputs)
    while position < number_inputs:
        print(truth[position], end="\t\t")
        position += 1

    try:
        truth = eval(statement)  # evaluates the statement as a python statement
        print(truth)
    except ValueError:
        print("Unable to evaluate. Check statement and try again. ")