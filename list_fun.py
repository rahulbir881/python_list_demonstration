#function of list
def add_names(name,names):
    names.append(name)

def search(name,names):
    pos=names.index(name)
    print(f"{name} present in {pos+1} position")

def display(names):
    for i in names:
        print(i,end=' ')