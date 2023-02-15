isp = {'(':0, '+':1, '-':1, '*':2, '/':2}
icp = {'(':3, '+':1, '-':1, '*':2, '/':2}

exp = input()
stack = []

for token in exp:
    if 'A' <= token <= 'Z':
        print(token, end='')
    elif token == ')' and stack:
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    else:
        if stack and isp[stack[-1]] >= icp[token]:
            while stack and isp[stack[-1]] >= icp[token]:
                print(stack.pop(), end='')
        stack.append(token)
while stack:
    print(stack.pop(), end='')


'''
-
ABC*+
'''