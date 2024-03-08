package Util;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class cool {
    public static void main(String[] args) {
        Map<Character, Integer> counts = new HashMap<>();
        PriorityQueue<Character> maxHeap = new PriorityQueue<>((a, b)
        -> counts.get(b) - counts.get(a));

        maxHeap.addAll(counts.keySet());
    }
}
