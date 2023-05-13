class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # holds the hash map and the values of data
        #holds every previous element before current element
        previousmap = {} #value : index

        #loops through the numbers array 
        for i, n in enumerate(nums):

            #finds the difference between the target number
            #and the current iteration number
            difference = target - n 

            #if the difference value is in the previousmap
            #it will return the coordinates of values
            if difference in previousmap:

                #returns the value of the difference
                #and the location of the index
                return [previousmap[difference] , i]

            #if difference value not found in 
            #previousmap it will add the value 'n' and will
            #set the value of the 'n' to index 'i' 
            previousmap[n] = i

            #if the difference value is not found in
            #previousmap it will iterate to the next
            #value untill found   


        return
