class Solution {
    public boolean isPalindrome(int x) {
        String s = Integer.toString(x);
        boolean solution = true;
        for (int l=0;l < (s.length()/2); l++) {
            if (s.charAt(l) != s.charAt(s.length()-(l+1))) {
                solution = false;
            }
    } return solution;
}
}