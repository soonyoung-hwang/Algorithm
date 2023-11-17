// 본 풀이는 카카오 테크블로그의 답안을 보고 풀었습니다.
import java.util.*;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int R = board.length;
        int C = board[0].length;
        HashMap<Integer, Integer> typeToDamage = new HashMap<>();
        typeToDamage.put(1, -1);
        typeToDamage.put(2, 1);
        
        int[][] accumulated = new int[R][C];
        for(int i=0; i < R; i++){
            for(int j=0; j < C; j++){
                accumulated[i][j] = 0;
            }
        }
        
        
        int type, r1, c1, r2, c2, degree, multi;
        
        
        for (int[] each_skill : skill){
            type = each_skill[0];
            r1 = each_skill[1];
            c1 = each_skill[2];
            r2 = each_skill[3];
            c2 = each_skill[4];
            degree = each_skill[5];
            
            accumulated[r1][c1] += degree * typeToDamage.get(type);
            if (r2+1 < R){
                accumulated[r2+1][c1] -= degree * typeToDamage.get(type);
            }
            if (c2+1 < C){
                accumulated[r1][c2+1] -= degree * typeToDamage.get(type);
            }
            if (r2+1 < R && c2+1 < C){
                accumulated[r2+1][c2+1] += degree * typeToDamage.get(type);
            }
        }

        for(int j=0; j < C; j++){
            for(int i=1; i < R; i++){
                accumulated[i][j] += accumulated[i-1][j];
            }
        }
        
        for(int i=0; i < R; i++){
            for(int j=1; j < C; j++){
                accumulated[i][j] += accumulated[i][j-1];
            }
        }
        
        
        for(int i=0; i < R; i++){
            for(int j=0; j < C; j++){
                if (board[i][j] + accumulated[i][j] >= 1){
                    answer += 1;
                }
            }
        }
        
        return answer;
    }
}