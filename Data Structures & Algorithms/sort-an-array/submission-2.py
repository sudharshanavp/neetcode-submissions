class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, left, right, mid):
            left_arr = arr[left:mid + 1]
            right_arr = arr[mid + 1:right + 1]
            i = j = 0
            k = left

            left_len = len(left_arr)
            right_len = len(right_arr)

            while i < left_len and j < right_len:
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i+=1
                else:
                    arr[k] = right_arr[j]
                    j+=1
                k+=1
            
            while i < left_len:
                arr[k] = left_arr[i]
                i+=1
                k+=1
            
            while j < right_len:
                arr[k] = right_arr[j]
                j+=1
                k+=1
            
        def mergeSort(arr, left, right):
            if left < right:
                mid = ( left + right ) // 2
                mergeSort(arr, left, mid)
                mergeSort(arr, mid + 1, right)
                merge(arr, left, right, mid)
        mergeSort(nums, 0, len(nums) - 1)
        return nums
 
            

        
