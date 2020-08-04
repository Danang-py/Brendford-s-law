#For a given dataset, - Get, or make, the data set to examine

#- Find the percent of numbers that start with 1...
#... - Then the percent of numbers that start with 2...
#.... - and so forth, until you have all 9 percentages

#- See if the percentages are close (or match) Benford's law.... if not, then there is something fishy here 




#let start to build a function that will take a list of number and return a dict 
#the dict will have: key 1 to 10 and the values will be the percentages
import re #to preceed regex

testlist = [112, 123, 977, 2, 96, 356, 8765, 564, 356, 75, 38, 45, 8, 93, 762, 873, 9876, 3456, 876, 34567, 64321, 12345]

def percent(list1):
    results = {}
    total = len(list1)
    for z in range(1,10):
        pattern = f'^{z}\d*'
        number = []
        for i in list1:
            one = re.search(pattern, str(i))
            if one != None:
                number.append(one)
        results[z] = str((round(len(number)/total, 4)*100)) + "%"

    return results

x = percent(testlist)
print(x)
