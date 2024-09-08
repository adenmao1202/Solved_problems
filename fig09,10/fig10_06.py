#Figure 10.6

from fig10_05 import mergeSort

def lastNameFirstName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else: #last names the same, sort by first name
        return arg1[0] < arg2[0]

def firstNameLastName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else: #first names the same, sort by last name
        return arg1[1] < arg2[1]

if __name__ == '__main__':
    L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
    newL = mergeSort(L, lastNameFirstName)
    print('Sorted by last name =', newL)
    newL = mergeSort(L, firstNameLastName)
    print('Sorted by first name =', newL)

