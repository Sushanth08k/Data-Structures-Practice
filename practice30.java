#2683. Neighboring Bitwise XOR
// Input: derived = [1,1,0]
// Output: true
// Explanation: A valid original array that gives derived is [0,1,0].
// derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1 
// derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
// derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0

class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        int ans=0;
        for (int i=0;i<derived.length;i++){
            ans=ans^derived[i];
        }
        return ans==0;
    }
}