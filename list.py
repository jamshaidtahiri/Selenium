with open("channel_list.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    
print(lines)    
    