parents = [i for i in range(5)]
rank = [1] * 5

# these two lists above represents que parents of wich child and the number of its children , in this case I used a random number (5) but you can replace this "5" for the length of edges.

# Now comes the two main parts , the find function and union function

def find(n):
    p = parents[n]

    while p != parents[p]:
        parents[p] = parents[parents[p]]
        p = parents[p]
    
    return p

    # the point of the function above is basically find out who is the main father of some specific node
    # you can see that we gonna keep doing this until the variable "p" be exactly like its "father" or in other words until we find the node wich is the father of itself.

def union(n1, n2):
    p1, p2 = find(n1), find(n2)

    if p1 == p2:
        return False
    
    if rank[p1] > rank[p2]:
        parents[p2] = p1
        rank[p1] += rank[p2]
    
    else:
        parents[p1] = p2
        rank[p2] += rank[p1]
    
    return True

# the function above will try to union the two nodes , in case of the p1 and p2 are equal that means the both are already connected (they have the same father) otherwise we will define the new father to one of them, usually the father who has more children in its own tree absorb the another node as a child as well, and I'm saying tree because that is the point of the union find , you kind of transform a graph in a tree.


for n1, n2 in edges:
    if not union(n1, n2):
        return [n1, n2]

