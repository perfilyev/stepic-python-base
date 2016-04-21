inheritance_graph = {}

def isParent(a,b):
    if a == b:
        return True
    if inheritance_graph[b]['parents'] == 0:
        return False
        
    for i in inheritance_graph[b]['parents']:
        if isParent(a, i):
            return True
    else: 
        return False
    
for i in range(0, int(input())):
    args = input().split()
    inheritance_graph[args[0]] = {'parents': []}
    if len(args) > 1:
        for className in args[2:]:
            inheritance_graph[args[0]]['parents'].append(className)
out = []            
for i in range(0, int(input())):
    a,b = input().split()
    out.append(('No', 'Yes')[isParent(a,b)])

for i in out:
    print(i)

# Sample input    
# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A