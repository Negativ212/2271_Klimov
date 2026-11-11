n = 5
tblmul = [[(j+1)*(i+1) for j in range(n)] for i in range(n)]
print(*tblmul,sep='\n')
