class Solution {
    public String solution(String s, String l) {
        String ans = "";
        for(int i=0;i<s.length();i++) {
            if(s.charAt(i) != l.charAt(0)) {
                ans += s.charAt(i);
            }
        }
        return ans;
    }
}
