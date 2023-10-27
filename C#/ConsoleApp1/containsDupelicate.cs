// See https://aka.ms/new-console-template for more information
using System;
using System.Dynamic;
using System.Collections.Generic;

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> numSet = new HashSet<int>(nums);
        if (nums.Length != numSet.Count )
        {
            return true;
        }
        return false;

        
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Your code can go here
        Solution solution = new Solution();
        int[] nums = { 1, 2, 3, 4, 1 };
        bool hasDuplicate = solution.ContainsDuplicate(nums);
        nums = new int[] {1,1,1,3,3,4,3,2,4,2};
        Console.WriteLine("Has duplicate: " + hasDuplicate);
        hasDuplicate = solution.ContainsDuplicate(nums);
        Console.WriteLine("Has duplicate: " + hasDuplicate);
    }
}
