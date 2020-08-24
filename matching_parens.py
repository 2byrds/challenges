# match {[(
# for instance {[()]}

__open__={'{':'}','[':']','(':')'}
__close__={'}':'{',']':'[',')':'('}

def is_open(char):
    return __open__.get(char) != None

def is_close(char):
    return __close__.get(char) != None

def match(input):
    print('\n\nLooking for matching parens in: ',input)
    
    stack = []
    count = 0
    for cur in input:
        print('Inspecting ',cur)
        if is_open(cur):
            print('\tFound open ',cur)
            stack.append(cur)
        elif is_close(cur):
            if len(stack) > 0:
                corr = stack.pop()
                if __close__.get(cur) == corr:
                    print('\tFound closing ',cur,' at char #',count, ' with corr = ', corr)
                else:
                    print('Invalid matching parens string.  Error on character #', count, ' = ',cur,'. expecting ', __close__.get(cur))
                    return                    
            else:
                print('Invalid matching parens string.  Error on character #', count, ' = ',cur)
                return
        else:
            print('\tIgnoring other char ', cur)
        count+=1
    
    if len(stack) > 0:
        print('Invalid matching parens string.  Parens remain open: ',stack)
    else:
        print('Valid matching parens string: ',input)
            

#matching
print('------------------------------------------------')
match('(((())))')
match('(([[{{}}]]))')
match('{[()]}')
match('')

#no match
match('[[[[[')
match('(((')
match('(((')
match('(((')
match('}}}')
match('}]])))')
match('(([[{{}}]])')
match('(([[{{}]]))')