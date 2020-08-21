testcases=int(input())
result=[]
for i in range(testcases):
    line1=input()
    line2=input()
    result.append(line1)
    result.append(line2)
    n=0
    solution=''
    while(n<=len(line1)-1):
        if(line1[n]==line2[n]):
            solution=solution+'.'
        else:
            solution=solution+'*'
        n=n+1
    result.append(solution)
    result.append(' ')
for j in result:
    print(j)
