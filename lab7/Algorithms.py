class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)



def checkDuplicates(arr):
    n = len(arr)

    
    st = set()

    
    for i in range(n):
        
        
        if arr[i] in st:
            return True
        else:
            st.add(arr[i])

   
    return False

if __name__ == "__main__":
    arr = [4, 5, 6, 4]
    print(checkDuplicates(arr))
