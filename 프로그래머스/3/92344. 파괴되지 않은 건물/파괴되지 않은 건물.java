import java.util.*;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int R = board.length;
        int C = board[0].length;
        HashMap<Integer, Integer> typeToDamage = new HashMap<>();
        typeToDamage.put(1, -1);
        typeToDamage.put(2, 1);
        
        int type, r1, c1, r2, c2, degree, multi;
        
        
        for (int[] each_skill : skill){
            type = each_skill[0];
            r1 = each_skill[1];
            c1 = each_skill[2];
            r2 = each_skill[3];
            c2 = each_skill[4];
            degree = each_skill[5];
            
            for(int i=r1; i < r2+1; i++){
                for(int j=c1; j <c2+1; j++){
                    board[i][j] += degree * typeToDamage.get(type);
                }
            }
        }
        
        for(int i=0; i < R; i++){
            for(int j=0; j < C; j++){
                if (board[i][j] >= 1){
                    answer += 1;
                }
            }
        }
        
        
        return answer;
    }
}