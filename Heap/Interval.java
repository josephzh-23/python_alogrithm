package Heap;//package sorting_heaps;
//
//import java.util.Arrays;
//
//
//public class Interval{
//    int start;
//    int end;
//    Interval (int s, int e) { start = s; end = e;}
//}
//class Solution{
//
//
//    public int search(Interval[] intervals, int[] nums, int target){
//
//        Arrays.sort(intervals,(a, b)-> a.start - b.start );
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