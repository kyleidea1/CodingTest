import java.util.Arrays;

class Solution {
    public int[] solution(int[] nums, int n1, int n2) {
        return Arrays.copyOfRange(nums,n1,n2+1);
    }
}