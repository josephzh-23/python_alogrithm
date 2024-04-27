package min_max;//import java.util.*;
//
//public class Main {
//    public static void Backtracking.Tree.Hard.Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main(String[] args) {
//
//        int newPx = 3;
//        int newPy = 4;
//        String s = newPx + "," + newPy;
//        System.out.println("Hello world!");
//
//        Map<Integer, Integer> counts = new HashMap();
//        // Translate the following as said
//        PriorityQueue<Map.Entry<Integer, Integer>> pq =
//                new PriorityQueue<>((a, b) -> b.getValue()- a.getValue());
//
//    }
//
//    public List<String> topKFrequent(String[] words, int k){
//        Map<String, Integer> map = new HashMap<>();
//
//        for(String word: words){
//            map.put(word, map.getOrDefault(word, 0) + 1);
//        }
//
//        PriorityQueue<String> pq = new PriorityQueue<>(new Comparator<String>() {
//            @Override
//            public int compare(String word1, String word2) {
//                int freq1 = map.get(word1);
//                int freq2 = map.get(word2);
//
//                // If their freq the same then compare alphabetically
//                if(freq1 == freq2) return word2.compareTo(word1);
//                return freq1 - freq2;
//            }
//        });
//
//        for(Map.Entry<String, Integer> entry: map.entrySet()){
//            pq.add(entry.getKey());
//            if(pq.size() > k)pq.poll();
//        }
//
//        List<String> result = new ArrayList<>();
//        while(!pq.isEmpty()) result.add(pq.poll());
//
//        Collections.reverse(result);
//        return result;
//    }
//
//
//    public List<Integer> preorderTraversal(Tree.Basic.TreeNode root){
//        return Graph.Edges_question.dfs(root, new ArrayList());
//    }
//    private List<Integer> Graph.Edges_question.dfs(Tree.Basic.TreeNode root, List<Integer> list){
//
//        if(root==null){
//            return list;
//        }
//        list.add(root.value);
//        list = Graph.Edges_question.dfs(root.left, list);
//        return Graph.Edges_question.dfs(root.right, list);
//    }
//}
//
//
//
//
//
//
//
//
//
//
//
//
//
