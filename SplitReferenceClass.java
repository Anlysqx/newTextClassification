package splitdata;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SplitReferenceClass {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(new File("D:/AAA/nlpdata/remov_dupli_result.txt")));
        HashMap<String,List<String>> map = new HashMap<>();
        String line = "";
        while ((line = br.readLine())!=null && !line.trim().equals("")){
            String[] list = line.split("&&&");
            if (!map.keySet().contains(list[1])){
                List<String> list1 = new ArrayList<>();
                list1.add(list[0]);
                map.put(list[1],list1);
            }else{
                List<String> list1 = map.get(list[1]);
                list1.add(list[0]);
            }
        }
        List<String> list = map.get("music");

        for (String str:list){
            System.out.println(str);
        }
        br.close();
        System.out.println(list.size());

        for(String className:map.keySet()){
            PrintWriter pw = new PrintWriter(new FileWriter(new File("D:/AAA/nlpdata/classFile/"+className+".txt")));
            List<String> list1 = map.get(className);
            for (String strline:list1){
                pw.println(strline);
            }
            pw.close();
        }

    }
}
