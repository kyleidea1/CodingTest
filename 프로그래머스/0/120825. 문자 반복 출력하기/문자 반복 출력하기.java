class Solution {
    public String solution(String s, int n) {
        String ans = "";
        for(int i = 0; i < s.length(); i++) {
            for(int j = 0; j < n; j++) {
                ans += s.charAt(i);
            }
        }
        return ans;
    }
}