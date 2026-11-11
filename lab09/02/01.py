def sublist(lst, *num):
    res = []  
    
    for n in num: 
        res.append(lst[n])  
        
    return res

lst = [ 'Anna', 'Barbara', 'Clara', 'Diana', 'Eva', 'Flora']
print(sublist(lst, 0, 2, 5))


