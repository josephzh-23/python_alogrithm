package Graph;

import java.util.*;

public class restore_array_java {

    public int[] restoreArray(int[][] ap) {

        HashMap<Integer, List<Integer>> hm = new HashMap<>();
        int n = ap.length;
        for (int i = 0; i < ap.length; i++) {
            hm.putIfAbsent(ap[i][0], new ArrayList<>());
            hm.get(ap[i][0]).add(ap[i][1]);
            hm.putIfAbsent(ap[i][1], new ArrayList<>());
            hm.get(ap[i][1]).add(ap[i][0]);
        }
        int start = 0;

        // Once you get the start here hten you can add htis in the next one as
        // discussed
        for (Map.Entry<Integer, List<Integer>> mp : hm.entrySet()) {
            if (mp.getValue().size() == 1) {
                start = mp.getKey();
                break;
            }
        }

        int[] ans = new int[n];
        HashSet<Integer> seen = new HashSet<>();
        dfs(hm, start, 0, seen, ans);
        return ans;
    }

    public void dfs(HashMap<Integer, List<Integer>> hm, int start,
                    int index, HashSet<Integer> seen, int[] ans) {

        ans[index] = start;
        seen.add(start);
        for (Integer neigh : hm.get(start)) {
            if (!seen.contains(neigh)) {
                dfs(hm, neigh, index + 1, seen, ans);
            }
        }
    }
}
