package sorting;//package sorting_heaps;
//
//class Solution{
//
//    public int search(int[] nums, int target){
//
//        int start = 0;
//        int end = nums.length -1;
//        while (start< end){
//            int mid = start + (end-start)/2;
//            if(nums[mid] == target){
//                return mid;
//            }else if(nums[mid] > target){
//                end = mid;
//            }else{
//                start = mid+ 1;
//            }
//        }
//        if(nums[start] == target){
//            return start;
//        }
//        return -1;
//    }
//}