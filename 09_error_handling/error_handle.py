file = open("youtube.txt", "w")


# Syntax 1 for working on file
try:
    file.write("Bhanu Youtube Project")
finally:
    file.close()


# Syntax 2 for working on file

with open("youtube.txt", "w") as file:
    file.write("Chai aur python")
