class Solution {
    public int[] solution(int[] n) {
        int[] answer = new int[n.length];
        for(int i=0;i<n.length;i++) {
            answer[i] = n[n.length-i-1];
        } 
        return answer;
    }
}