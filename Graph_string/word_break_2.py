'''

Using this problem we would then have

Slightly more advanced than before here

Return all such possible sentences in any order.

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

And then here is the code here


Part 1 here:
Initially, we might think of a brute-force approach
 where we systematically explore all possible ways to break the string into words from the dictionary. This leads us to the backtracking strategy, where we recursively try to form words from the string and

    add them to a current sentence if they are in the dictionary. If the current prefix doesn't lead to a valid solution, we backtrack by removing the last added word and trying the next possible word. This ensures we explore all possible segmentations of the string.


        At each step, we consider all possible end indices for substrings starting from the current index. For each substring, we check if it exists in the dictionary.

        If the substring is a valid word, we append it to the current sentence and recursively call the function with the updated index, which is the end index of the substring plus one.

Part 2 here:
If we reach the end of the string, it means we have found a valid segmentation, and we can add the current sentence to the results. However, if we encounter a substring that is not a valid word, we backtrack by returning from that recursive call and trying the next possible end index.

The backtracking approach will be inefficient due to the large number of recursive calls, especially for longer strings. To increase efficiency, we will convert the word dictionary into a set for constant-time lookups. However, the overall time complexity remains high because we explore all possible partitions.

The process is visualized below:



'''


