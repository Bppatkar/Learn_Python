import time

print("Chai is here")
userName = "bhanu"

print(userName)


# ? open terminal in the same folder and write python so python will start working and then store file in a variable

# //! u will see the exact line of code in whatever sequence we have written
# f = open('chai.py')Ctrl click to launch VS Code Native REPL
# >>> f = open('chai.py')
# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'print("Chai is here")\n'
# >>> f.readline()
# 'userName = "bhanu"\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'print(userName)\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# '# ? open terminal in the same folder and store file in a variable\n'


# //! we can see in raw form also
# //? using __next__()
# f= open('chai.py')

# >>> f = open('chai.py')
# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'print("Chai is here")\n'
# >>> f.readline()
# 'userName = "bhanu"\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'print(userName)\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# '# ? open terminal in the same folder and store file in a variable\n'

# //! UseCases of 'NOT'
test = "Bhanu"

if not test:
    print("kuch to hai")


test1 = ""

if not test1:
    print("kuch ni hai")
