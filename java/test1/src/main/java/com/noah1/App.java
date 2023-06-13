package com.noah1;
import java.util.HashSet;
import java.util.*;

/**
 * Hello world!
 *
 */
// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
public class App 
{
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        App app = new App();
        int[] result = app.twoSum(nums, target);
        System.out.println(Arrays.toString(result));
    }

    public static boolean containsDuplicate(int[] nums) {
        // implementation goes here
        HashSet<Integer> found = new HashSet<Integer>();

        for (Integer item : nums) {
            if (found.contains(item))
            {
                return true;
            }
            else
            {
                found.add(item);
            }
            
        }

        return false;
    }

    //Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    // You may assume that each input would have exactly one solution, and you may not use the same element twice.
    // You can return the answer in any order.
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> maped = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++)
        {
            int needed = target - nums[i];
            
            if(maped.containsKey(needed))
            {
                int[]output = {maped.get(needed), i};
                return output;
            }
            else
            {
                maped.put(nums[i], i);
            }
        }
        int[] output = {};
        return output;
    }

    
}
