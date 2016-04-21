stack = {'global': {'parent': None, 'vars': []}}
out = []

def add(ns, var):
    stack[ns]['vars'].append(var)
    
def create(ns, parent):
    stack[ns] = {'parent': parent, 'vars': []}

def get(ns,var):
    if var in stack[ns]['vars']:
        out.append(ns)
        return ns
    if stack[ns]['parent'] == None:
        out.append(None)
        return None
    return get(stack[ns]['parent'], var)

for i in range(0, int(input())):
    args = input().split()
    locals()[args[0]](args[1], args[2])

for i in out:
    print(i)