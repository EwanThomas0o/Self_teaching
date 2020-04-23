def Advance_array(A):
    furthest_reached = 0
    last_ind = len(A)-1

    i = 0
    while i <=furthest_reached and furthest_reached < last_ind:
        furthest_reached = max(furthest_reached,A[i]+i)
        i+=1
    return furthest_reached >=last_ind #if we can get to last index then we print ture, if we can't we print false

A = [1,2,1,3,0,0,1]
print(Advance_array(A))


