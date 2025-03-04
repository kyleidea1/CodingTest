class Solution {
    public int[] solution(int[] n) {
        int even = 0;
        int odd = 0;

        for (int i = 0; i < n.length; i++) {
            if (n[i] % 2 == 0) {
                even += 1;
            } else {
                odd += 1;
            }
        }

        // 결과를 담을 배열 생성
        int[] ans = {even, odd};

        return ans;  // 짝수와 홀수 개수를 반환
    }
}
