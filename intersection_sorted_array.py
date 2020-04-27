#intersection of two sorted arrays.
#There is a funtion that actually does this for you! set(A).intersection(B) for two arrays A & B.
#Intersection is a member of the set class so that's why we have to change either to a Set, also returns a set.
#However since we know the arrays are sorted we can create an algorithm with a faster runtime than .intersection()!

def intersection_sorted_array(A,B):
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else: j += 1
    return intersection
