unique = []
for x in objects:
    for u in unique:
        if x is u:
            break
    else:
        unique.append(x)
print(len(unique))