package duiplicateRemove;

import java.io.*;
import java.util.HashMap;
import java.util.Map;

public class RemoveDuplicate {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(new File("D:/AAA/nlpdata/result.txt")));
        Map<String,String> map = new HashMap<>();
        String line = "";
        while ((line = br.readLine())!=null && !line.trim().equals("")){
            String[] list = line.split("&&&");
            map.put(list[0],list[1]);
        }
        PrintWriter pw = new PrintWriter(new FileWriter(new File("D:/AAA/nlpdata/remov_dupli_result.txt")));
        for (String key:map.keySet()){
            StringBuffer sb = new StringBuffer();
            sb.append(key);
            sb.append("&&&");
            sb.append(map.get(key));
            pw.println(sb.toString());
        }
        br.close();
        pw.close();
    }
}
