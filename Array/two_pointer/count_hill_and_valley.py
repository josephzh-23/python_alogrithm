
'''
Just need to check the current element and the one before and the one after here
-
class Solution {
public:
    int countHillValley(vector<int>& nums) {
        int n=nums.size();
        int count=0;
        int last=nums[0];
        for(int i=1;i<n-1;i++)
        {
            if(nums[i]==last)
            {
                last=nums[i];
                continue;
            }
            if(last<nums[i] && nums[i]>nums[i+1])
            {
                last=nums[i];
                count++;
            }
            else if(last>nums[i] && nums[i]<nums[i+1])
            {
                last=nums[i];
                count++;
            }
        }
        return count;
    }
};

'''