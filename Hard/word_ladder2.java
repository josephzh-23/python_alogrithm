package Hard;

import java.util.*;

public class word_ladder2 {

    public int ladderLength(String beginWord, String endWord, List<String> wordList){

        // This is just to store the word list here
        Set<String> set = new HashSet<>(wordList);
        if(!set.contains(endWord)) return 0;

        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);

        Set<String> visited = new HashSet<>();
        visited.add(beginWord);

        int changes = 1;
        while(!queue.isEmpty()){
            int size = queue.size();

            // THis tells you how many changes took to get to endword
            // from beginword
            for(int i= 0; i< size; i++){
                String words = queue.poll();
                if(words.equals(endWord))return changes;

                for(int j= 0; j < words.length(); j++){
                    for(int k = 'a'; k <= 'z' ; k++){
                        char[] arr = words.toCharArray();
                        arr[j] = (char)k;

                        String str = new String(arr);
                        // Then we have found the string we are looking for
                        // in the string as per example in the notes
                        if(set.contains(str) && !visited.contains(str)){
                            queue.add(str);
                            visited.add(str);
                        }
                    }
                }
            }
            ++changes;
        }
        return changes;
    }
}
