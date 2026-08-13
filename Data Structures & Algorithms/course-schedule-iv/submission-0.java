class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        boolean[][] reachable = new boolean[numCourses][numCourses];

        for (int i = 0; i < prerequisites.length; i++) {
            int a = prerequisites[i][0], b = prerequisites[i][1];
            reachable[a][b] = true;
        }

        for (int k = 0; k < numCourses; k++) {
            for (int i = 0; i < numCourses; i++) {
                for (int j = 0; j < numCourses; j++) {
                    if (reachable[i][k] && reachable[k][j]) {
                        reachable[i][j] = true;
                    }
                }
            }
        }

        List<Boolean> res = new ArrayList<>();
        for (int[] query : queries) {
            int a = query[0], b = query[1];
            if (reachable[a][b]) {
                res.add(true);
            } else {
                res.add(false);
            }
        }

        return res;
    }
}