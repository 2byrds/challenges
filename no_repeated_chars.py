'''
Repeated chars problem
ABCDEabcde = abcde
a = a
aaaaaa = a
abcdefghidijkl=efghid
'''

def longest_nonrepeated(input):
    print('Getting longest nonrepeated from: ',input)
    input = input.lower()
    
    current = ''
    longest = ''
    for char in input:
        if char in current:
            if len(current) > len(longest):
                longest = current
            current=''
        else:
            current+=char
            if len(current) > len(longest):
                longest = current
    
    print('Longest nonrepeated: ',longest)


longest_nonrepeated('')
longest_nonrepeated('ABCDEabcde')
longest_nonrepeated('a')
longest_nonrepeated('aaaaaa')
longest_nonrepeated('abcddefghidijkl')