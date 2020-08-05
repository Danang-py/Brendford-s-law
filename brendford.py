#For a given dataset, - Get, or make, the data set to examine

#- Find the percent of numbers that start with 1...
#... - Then the percent of numbers that start with 2...
#.... - and so forth, until you have all 9 percentages

#- See if the percentages are close (or match) Benford's law.... if not, then there is something fishy here 


import sys #allow to import command line argument
import re     #to preceed regex
import pandas as pd  #to read and proceed csv file 
from scipy.stats import chisquare #to get a p-value helping us to decide if the data follow brendford's law or not


#The list corresponding to the percentages of the repartition for Brendord's law
brendfordlist = [30.1, 17.61, 12.49, 9.69, 7.92, 6.69, 5.80, 5.12, 4.58]


#let start to build a function that will take a list of number and return a dict 
#the dict will have: key 1 to 10 and the values will be the percentages
def percent(list1):
    results = {}
    total = len(list1)
    for z in range(1,10):
        pattern = '^0*[,.]{0,1}0*'+f'{z}\d*'
        number = []
        for i in list1:
            one = re.search(pattern, str(i))
            if one != None:
                number.append(one)
        results[z] = (round(len(number)/total, 4)*100)
    return results

def check(percents):
    chilist = [value for value in percents.values()]
    results = chisquare(chilist, brendfordlist)
    print(f'the p-value for the chisquare test is: {results[1]}')
    if results[1] < 0.05:
        print(f"We can reject the hypothesis that our numbers follow bendford's law (at 5% error tolerance)")
        return False
    else:
        print(f"The data follow Brendford's law")
        return True
    

#take the command line arguments and proceed
args = sys.argv[1:]


def main():
    #check if args:
    if len(args) == 0:
        print("brendford.py must take argument(s): \nusage: brendofrd.py arg \n arg can be a file (.csv or .txt) or a list of numbers")
        return

    #check the type of file or the type of data
    if len(args) == 1:
        ext = "\.(txt|csv)$"
        extension = re.search(ext, args[0])

        if extension is None:
            pass

        elif extension.group(0) == ".csv":
            print('opening .csv file...')
            content = pd.read_csv('filename', sep=',')
            ##todo

        elif extension.group(0) == ".txt":
            print('opening .txt file...')
            with open(args[0], 'r') as f:
                content = f.read()
            pattern = "0*[,.]{0,1}0*\d+"
            numbers = re.findall(pattern, content)
            print(f"numbers in file are: {numbers}")
            percents = percent(numbers)
            print(percents)
            check(percents)

        else:
            print("extension not allowed! \n Must be .csv or .txt")
            return
    
    else:
        print(percent(args))
        check(percent)


if __name__ == "__main__":
    main()


