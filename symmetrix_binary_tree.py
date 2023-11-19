def left(index):
    return 2*(index)+1
def right(index):
    return 2*(index)+2  
    
def binary(lt,index1,index2):
    if index1>=len(lt) and index2>=len(lt):
        return True
    if index1>=len(lt) or index2>=len(lt):
        return False
        
    if lt[index1]==lt[index2]:
       return binary(lt,left(index1),right(index2)) and binary(lt,right(index1),left(index2))
    return False
    
#given as list(array representation)
print("enter the nodes as list (if no node enter -1 as node)")
lt=[int(item) for item in input("Enter the nodes as list(level-wise):").split()]
print(lt)
# lt=[1,2,2,4,3,3,4] - symmetrix
# lt=[1,2,2,-1,3,3] - not symmetric
print(binary(lt,0,0))
