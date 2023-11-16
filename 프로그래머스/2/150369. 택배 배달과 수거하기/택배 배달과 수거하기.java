// 각 집마다 배달할 재활용 택배 상자의 개수와 수거할 빈 재활용 택배 상자의 개수를 알고 있을 때, 
// 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리를 구하려 합니다. 
// 각 집에 배달 및 수거할 때, 원하는 개수만큼 택배를 배달 및 수거할 수 있습니다.
import java.util.*;

class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        Integer hit1 = 0;
        Integer hit2 = 0;
        for(int i=n-1; i>= 0; i--){
            if (deliveries[i] > 0){
                hit1 = i;
                break;
            }
            if (i == 0 && deliveries[i] == 0){
                hit1 = -1;
            }
        }
        for(int i=n-1; i>= 0; i--){
            if (pickups[i] > 0){
                hit2 = i;
                break;
            }
            if (i == 0 && pickups[i] == 0){
                hit2 = -1;
            }
        }
        
        while (true){
            Integer cap_left = cap;
            Integer pickup_left = cap;
            Integer to_add = Math.max(hit1, hit2);
            answer += (to_add+1)*2;
            
            for(int i=hit1; i >= 0; i--){
                if (deliveries[i] == 0){
                    if (i == 0){
                        hit1 = -1;
                    }
                    continue;
                }

                Integer remove = Math.min(deliveries[i], cap_left);
                deliveries[i] -= remove;
                cap_left -= remove;
                
                if (deliveries[i] > 0){
                    hit1 = i;
                    break;
                }
                if (i==0 & deliveries[i]== 0){
                    hit1 = -1;
                    break;
                }
            }
            
            for(int i=hit2; i >= 0; i--){
                if (pickups[i] == 0){
                    if (i == 0){
                        hit2 = -1;
                    }
                    continue;
                }
                Integer remove = Math.min(pickups[i], pickup_left);
                pickups[i] -= remove;
                pickup_left -= remove;
                if (pickups[i] > 0){
                    hit2 = i;
                    break;
                }
                if (i==0 & pickups[i]== 0){
                    hit2 = -1;
                    break;
                }
            }
            
            if (hit1 == -1 & hit2 == -1){
                break;
            }
        }
            
        
        return answer;
    }
}