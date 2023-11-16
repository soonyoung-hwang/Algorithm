import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        HashSet<String> fruits = new HashSet<>();
        HashMap<String, HashSet<String>> reportById = new HashMap<>();
        for (String id : id_list){
            reportById.put(id, new HashSet<>());
        }
        
        for (String reportHistory : report){
            String[] temp = reportHistory.split(" ");
            String report_id = temp[0];
            String reported_id = temp[1];
            HashSet<String> tempSet = reportById.get(reported_id);
            tempSet.add(report_id);
        }
        
        HashMap<String, Integer> counts = new HashMap<>();
        for (String id : id_list){
            counts.put(id, 0);
        }

        for (String id : id_list){
            HashSet<String> ids = reportById.get(id);
            int numberOfElements = ids.size();
            if (numberOfElements >= k){
                for (String who : ids){
                    counts.put(who, counts.get(who)+1);
                }    
            }
        }
        for (int i=0; i < id_list.length; i++){
            answer[i] = counts.get(id_list[i]);
        }
        
        
        return answer;
    }
}