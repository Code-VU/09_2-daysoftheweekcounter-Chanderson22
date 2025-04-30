def countDayOfTheWeek():
    # This first line is provided for you
    counter = dict()
    file_name = input("Enter a file name: ")
    try: 
        fhandle = open(file_name)
    except:
        print('The Princess is in another castle!')
        exit()
    for line in fhandle:
        line = line.rstrip()
        if not line.startswith('From '): continue
        words = line.split()
        days = words[2]
        if days not in counter:
            counter[days] = 1
        else:
            counter[days] += 1

    print(counter)


## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
