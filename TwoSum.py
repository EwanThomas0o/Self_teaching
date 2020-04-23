                #METHOD 1
#This is a brute force method and takes o(n^2) which is not fun!

#Time-Complexity: O(n^2)
#Space-Complexity: O(1)

def two_sum_brute(A, target): #Takes target and array in as inputs 
    for i in range(len(A)-1): #Loops from 0 to length-1, you'll see why now...
        for j in range(i+1, len(A)): #J goes from i to i+1 up to the end of the matrix checking to see if the vals add == target. The +1 is why we don't take i to len(A)
            if A[i] + A[j] == target:  #The check
                print(A[i],A[j]) #prints the numbers in the array that give the target 
                return True
    return False

#Lets try and get away from this brute force method...

                #METHOD 2

#Time-Complexity: O(n)
#Space-Complexity: O(n)

def two_sum_hash(A, target):
    ht = dict() #Empty dictionary called 'ht'. Dics have keys and values. We store the number and its compliment to the target i.e target is 13. if we find a 4 then ht[7]=4 so if we find a 7 we know we can two sum
    for i in range(len(A)):
        if A[i] in ht:  #Checking to see if the value is already in the dictionary
            print(ht[A[i]],A[i])
            return True
        else:
            ht[target-A[i]] = A[i] #for a number not in the dict, we find its compliment to the target, and make this a key in the dic with the value that makes the target
            return False

                #METHOD 3

#Time-Complexity: O(n)
#Space-Complexity: O(1)     The best solution yet!

def two_sum_best(A,target): #Use two indicies to track the begining and end of the array, remember we are using sorted arrays!
    i = 0          
    j = len(A)-1 #Remember A[-1] is the last element in an array!
    while i < j: #Inidicies meet in the middle
        if A[i] + A[j] == target:
            print(A[i],A[j])
            return True         #Standard throughout
        elif A[i] + A[j] < target: #If we are using sorted arrays and the combo is smaller then targert then we know we must advance one to get a bigger number!
            i += 1
        else: j-=1 #If we need a smaller number (so just else) then we make j go back one, this process then continues throughout the loop! THE POWER OF TWO INDICIES
    return False


A = [2,3,4,5,7,8]
target = 12

two_sum_best(A,target)