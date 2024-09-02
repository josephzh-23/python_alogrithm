'''
Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.


'''
'''
By doing n & (n-1) -> makes the least significant bits 0 from 1 

Example:
              l      here l means least significant bits here
 n:     1 1 0 1 0 0 
 n-1    1 1 0 0 1 1
n & n-1 1 1 0 0 0 0 


Bits questions are easier to do in java then other languages here as said 
public int hammingWeight(int n) {
    int sum = 0;
    while (n != 0) {
        sum++;
        n &= (n - 1);
    }
    return sum;
}

'''