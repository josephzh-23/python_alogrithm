package Graph.Edges_question;

class DSU22 {
    private int[] size;
    private int[] root;
    public int count;

    public DSU22(int N) {
        size = new int[N];
        root = new int[N];
        count = N;
        for (int i = 0; i < N; i++) {
            root[i] = i;
        }
    }

    private int find(int x) {
        if (root[x] != x) {
            root[x] = find(root[x]);
        }
        return root[x];
    }

    void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY) return;

        if (size[rootX] <= size[rootY]) {
            root[rootX] = rootY;
            size[rootY] += size[rootX];
        } else {
            root[rootY] = rootX;
            size[rootX] += size[rootY];
        }
        count--;
    }
}


public class most_stones_removed {
    public int removeStones(int[][] stones) {
        int N = stones.length;
        DSU22 dsu = new DSU22(N);

        for (int i = 0; i < stones.length; i++) {
            for (int j = i + 1; j < stones.length; j++) {

                // Same row or same column then we will try to union it
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    dsu.union(i, j);
                }
            }
        }

        return N - dsu.count;
    }
}