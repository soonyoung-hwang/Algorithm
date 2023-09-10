import java.util.*;
class Solution {
    boolean flag;
    String[] answer;
    public String[] solution(String[][] tickets) {
        answer = new String[tickets.length+1];
        
        Arrays.sort(tickets, (o1,o2)->{if(o1[0].toString().contentEquals(o2[0].toString())) return o1[1].toString().compareTo(o2[1].toString());
                                      else{
                                          return o1[0].toString().compareTo(o2[0].toString());
                                      }});
        
        answer[0] = "ICN";
        boolean[] visited = new boolean[tickets.length];
        
        flag = false;
        dfs(tickets, 0, tickets.length, visited);
        
        return answer;
    }
    
    public void dfs(String[][] tickets, int i, int n, boolean[] visited){
        if(i==visited.length){
            flag = true;
            return;
        }
        if (flag==true){
            return;
        }

        System.out.println("Processing.\n");
        for(int j=0;j<visited.length;j++){
            if(visited[j]==false && answer[i].equals(tickets[j][0])){
                visited[j] = true;
                if (flag==true){
                    break;
                }
                answer[i+1] = tickets[j][1];
                System.out.println(tickets[j][1]);
                
                dfs(tickets, i+1, n, visited);
                visited[j] = false;

            }
        }
        return;
    }
}