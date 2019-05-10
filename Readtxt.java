package readjson;

import com.alibaba.fastjson.JSON;

import java.io.*;
import java.util.*;

//读取没有去重前的数据，进行分析
public class Readtxt {
    public static void main(String[] args) {
//        File f = new File("D:/AAA/result.txt");
        File f = new File("D:/AAA/nlpdata/result.txt");
        int totalnum = 0;
        Map<String,Integer> map = new HashMap<>();

        try {
            BufferedReader br = new BufferedReader(new FileReader(f));
            String line = "";
            while ((line = br.readLine())!=null && !line.trim().equals("")){

                totalnum++;
                String[] list = line.split("&&&");
                map.put(list[1],map.getOrDefault(list[1],0)+1);

            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("一共"+totalnum+"条数据");
        System.out.println("一共"+map.size()+"个类别");
        List<Map.Entry<String,Integer>> list = new ArrayList<>(map.entrySet());
        Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {
            @Override
            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
                return -(o1.getValue() - o2.getValue());
            }
        });
        list.forEach(ele->{
            System.out.println(ele.getKey()+" : "+ele.getValue());
        });
        try {
            PrintWriter pw = new PrintWriter(new FileOutputStream(new File("D:/AAA/class.txt")));
            pw.println(JSON.toJSONString(map));
            pw.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }


    }
}
