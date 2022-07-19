

def reversed_list(l):
    l = l[::-1]
    for i in range(len(l)):
        l[i] = (l[i])[::-1]
    
    print(l) 
    
my_list = [[1, 2], [3, 4], [5, 6, 7]]
reversed_list(my_list)
 
