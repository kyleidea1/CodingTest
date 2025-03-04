class Solution {
    public String solution(String s) {
        String ans = "";
        for(int i = 0; i < s.length();i++) {
            ans += s.charAt(s.length()-1-i);
        }
        return ans;
    }
}