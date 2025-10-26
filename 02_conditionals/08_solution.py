password = 'SecuRe&*@786'

if len(password) < 6:
    print("weak")
elif len(password) <= 10:
    print("medium")
else:
    print("strong")
