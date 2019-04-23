import math

def phi(n):
    '''
    Euler-Totient Function: returns the number of integers
    from 0 to n inclusive that are coprime to n.
    '''
    amount = 0        
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

def rrs(n):
    '''
    Returns a set of the reduced-residue system (in order)
    of the integer n. All of these integers are between 0 to n
    and are coprime to n.
    '''
    rrs = []
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            rrs.append(k)
    return rrs

number = int(input('Enter a number greater than 0: '))
print()
phinumber = phi(number)
rrs = rrs(number)
# Initializing the original table:
# Each list in bd is column.
# Each group of indices is a row.
bd = []
for col in range(1, phinumber + 1):
    bd.append([])
    for row in range(1, phinumber + 1):
        bd[col - 1].append((row ** col) % number)


bd2 = []
# Creating a new table similar to the original table except with labels of primitive roots/other patterns.
for col in range(1, phinumber + 1):
    bd2.append([0] * phinumber)
    for row in range(1, phinumber + 1):
        
        # Calculating the sum of the column
        colsum = sum(bd[col - 1])
        rowsum = 0
        primcheck = set()
        
        # Calculating the sum of the row and check for primitive root
        for rowelement in range(0, phinumber):
            rowsum += bd[rowelement][row - 1]
            primcheck.add(bd[rowelement][row - 1])
        
        if len(primcheck) != phinumber and colsum == rowsum:
            bd2[col - 1][row - 1] = str(bd[col - 1][row - 1]) + ' *'
        #elif len(primcheck) == phinumber and colsum != rowsum:
            #bd2[col - 1][row - 1] = str(bd[col - 1][row - 1]) + '**'
        elif len(primcheck) == phinumber:
            bd2[col - 1][row - 1] = str(bd[col - 1][row - 1]) + ' !'
            if colsum == rowsum:
                bd2[col - 1][row - 1] += '*'
        else:
            bd2[col - 1][row - 1] = str(bd[col - 1][row - 1]) 

# Calculating list of primitive roots from the first column
primroots = []      
for col_element in range(0, phinumber):
    col_one_el = bd2[0][col_element]
    intpart2 = ''
    for char in col_one_el:
        if char.isdigit():
            intpart2 += char
    if col_one_el.count('!') == 1:
        primroots.append(int(intpart2))


# Fixing error where some numbers are incorrectly labeled as primitive roots.
for col in range(0, phinumber):
    for row in range(0, phinumber):
        element = bd2[col][row]
        intpart = ''
        for char in element:
            if char.isdigit():
                intpart += char
        if element.count('!') > 0 and not int(intpart) in primroots:
            bd2[col][row] = element.replace('!', '')
            
for col_label in range(1, phinumber + 1):
    print('\ta^{}'.format(col_label), end='')
print()

for col in range(1, phinumber + 1):
    print('a = {}:'.format(col), end='')
    
    for row in range(1, phinumber + 1):
        print('\t' + bd2[row - 1][col - 1], end='')
                  
    print()
print('\nList of primitive roots: {}'.format(primroots))
print('\nLegend: ')
print('\t* = Not a primitive root, but the sum of the row and columns are equal')
print('\t! = Primitive root')
print('\t!* = Primitive root, and the sum of the row and columns are equal')
