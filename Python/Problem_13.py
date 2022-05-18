def getLargeSum():
    
    print(str(sum(readFile()))[:10])



def readFile():

    lines = []
    with open('D:\\Users\\DIEGO\\Documents\\Amazon Interview\\Project Euler\\files\\numbers.txt', 'r') as reader:
        for line in reader:
            lines.append(int(line.strip('\n')))

    return lines

getLargeSum()