def count_returns(
    position=0
    return_count=0 
    for move in A:
        if move==1: 
           position+=1
        elif move==-1:
           position-=1 
        if position==0:
           return_count+=1 
return return_count 
N=int(input())
A=list(map(int,input().split())) 
result=count_returns (N, A) 
print(result)
