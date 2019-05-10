package readjson;

import com.alibaba.fastjson.JSONReader;

import java.io.*;

public class ReadJson {
    public static void main(String[] args) throws FileNotFoundException {
        String jsonString = "[\n" +
                "  {\n" +
                "    \"id\": 1,\n" +
                "    \"merchant_id\": \"2609509842712408242\",\n" +
                "    \"client_id\": \"clientId\",\n" +
                "    \"dialog_id\": \"1234\",\n" +
                "    \"ver\": 2,\n" +
                "    \"query\": \"播放刘德华歌曲\",\n" +
                "    \"data\": \"{\\\"result\\\":[{\\\"code\\\":0,\\\"data\\\":{\\\"audio_list\\\":[{\\\"album\\\":\\\"\\\",\\\"audio_url\\\":\\\"http://ipub5.soundai.me:90/music/v1/991e2da355d27192557afb148b3d351c.mp3\\\",\\\"title\\\":\\\"123木头人\\\"},{\\\"album\\\":\\\"\\\",\\\"audio_url\\\":\\\"http://ipub5.soundai.me:90/music/v1/886da9266c0a59e39b8a2141bec27eee.mp3\\\",\\\"title\\\":\\\"17岁(Live)\\\"},{\\\"album\\\":\\\"\\\",\\\"audio_url\\\":\\\"http://ipub5.soundai.me:90/music/v1/62497987cd6d84b528e7630e3054ca25.mp3\\\",\\\"title\\\":\\\"17岁(粤)\\\"},{\\\"album\\\":\\\"\\\",\\\"audio_url\\\":\\\"http://ipub5.soundai.me:90/music/v1/9ffeed5f99259cba36bdfe6dff0a0260.mp3\\\",\\\"title\\\":\\\"Broadway Opening(Live)\\\"},{\\\"album\\\":\\\"\\\",\\\"audio_url\\\":\\\"http://ipub5.soundai.me:90/music/v1/11f49d0cbad473f6b1cb489cb61785a2.mp3\\\",\\\"title\\\":\\\"Duet Dance(Live)\\\"},{\\\"album\\\":\\\"\\\",\\\"audio_url\\\":\\\"http://ipub5.soundai.me:90/music/v1/9c6e47b171a2fb2af681886dd8c84131.mp3\\\",\\\"title\\\":\\\"Natural(Live) - live\\\"},{\\\"album\\\":\\\"\\\",\\\"audio_url\\\":\\\"http://ipub5.soundai.me:90/music/v1/1289052cf678ebcb120b47e690941f06.mp3\\\",\\\"title\\\":\\\"Prelude To 爱你一万年(Live)\\\"},{\\\"album\\\":\\\"\\\",\\\"audio_url\\\":\\\"http://ipub5.soundai.me:90/music/v1/bb15faed1e651af80516db03f4c48677.mp3\\\",\\\"title\\\":\\\"Prelude To 魔鬼在恋爱(Live)\\\"},{\\\"album\\\":\\\"\\\",\\\"audio_url\\\":\\\"http://ipub5.soundai.me:90/music/v1/d38aabd5344c97a3927af3e03e2b90d7.mp3\\\",\\\"title\\\":\\\"一个人睡(Live) - live\\\"},{\\\"album\\\":\\\"\\\",\\\"audio_url\\\":\\\"http://ipub5.soundai.me:90/music/v1/14537c6d6072c75fc3da68b01010799c.mp3\\\",\\\"title\\\":\\\"一起嗌(粤)\\\"}],\\\"answer\\\":\\\"为您播放刘德华的123木头人\\\",\\\"parameters\\\":{\\\"artist\\\":\\\"刘德华\\\"}},\\\"domain\\\":\\\"music\\\",\\\"message\\\":\\\"\\\",\\\"selected\\\":true,\\\"source\\\":\\\"ruyi\\\"},{\\\"code\\\":400,\\\"data\\\":{},\\\"selected\\\":false,\\\"source\\\":\\\"sai\\\"},{\\\"code\\\":400,\\\"message\\\":\\\"ok\\\",\\\"selected\\\":false,\\\"source\\\":\\\"situo\\\"}]}\",\n" +
                "    \"cost\": 869,\n" +
                "    \"timestamp\": \"2018-09-25 02:11:50\",\n" +
                "    \"device_id\": null\n" +
                "  },\n" +
                "  {\n" +
                "    \"id\": 2,\n" +
                "    \"merchant_id\": \"3163684076898702361\",\n" +
                "    \"client_id\": \"2946107899\",\n" +
                "    \"dialog_id\": \"1537868053196250928\",\n" +
                "    \"ver\": 1,\n" +
                "    \"query\": \"想我了\",\n" +
                "    \"data\": \"{\\\"result\\\":[{\\\"code\\\":0,\\\"data\\\":{\\\"answer\\\":[{\\\"content\\\":\\\"天天都想你 \\\",\\\"result\\\":\\\"T\\\",\\\"setContent\\\":true,\\\"setResult\\\":true,\\\"setText\\\":false,\\\"setUrl\\\":false}],\\\"operation\\\":\\\"ANSWER\\\"},\\\"domain\\\":\\\"chat\\\",\\\"message\\\":\\\"\\\",\\\"selected\\\":true,\\\"source\\\":\\\"qihoo\\\"}]}\",\n" +
                "    \"cost\": 1053,\n" +
                "    \"timestamp\": \"2018-09-25 02:34:29\",\n" +
                "    \"device_id\": null\n" +
                "  }]";
        // 如果json数据以形式保存在文件中，用FileReader进行流读取！！
        // path为json数据文件路径！！
        JSONReader reader = new JSONReader(new FileReader("D:/AAA/nlpdata_recordone.json"));

        // 为了直观，方便运行，就用StringReader做示例！
        File file = new File("D:/AAA/nlpdata/result.txt");
        PrintStream ps = new PrintStream(new FileOutputStream(file));

//        JSONReader reader = new JSONReader(new StringReader(jsonString));
        reader.startArray();
        System.out.println("start array...");

        while (reader.hasNext()) {
            reader.startObject();
            OneQuery oneQuery = new OneQuery();
            while (reader.hasNext())
            {
                String arrayListItemKey = reader.readString().trim();
                if (arrayListItemKey.equals("device_id")){
                    reader.readObject();
                    continue;
                }
                String arrayListItemValue = "";
                try{
                    arrayListItemValue = reader.readObject().toString().trim();
                }catch (NullPointerException e){
                    arrayListItemKey = "null";
                }

                if (arrayListItemKey.equals("query")){
                    oneQuery.setQuery(arrayListItemValue);
                }else if (arrayListItemKey.equals("data")){

                    String oneData = arrayListItemValue;
                    JSONReader reader2 = new JSONReader(new StringReader(oneData));
                    reader2.startObject();
                    String key = reader2.readString();
                    if (key.equals("result")) {

                        reader2.startArray();
                        while (reader2.hasNext()) {
                            reader2.startObject();
                            while (reader2.hasNext()) {
                                String arrayListItemKey2 = reader2.readString().trim();
                                String arrayListItemValue2 = reader2.readObject().toString().trim();
                                if (arrayListItemKey2.equals("domain")) {
                                    oneQuery.setDomain(arrayListItemValue2);
                                }
                            }
                        }
                    }
                }
            }
            StringBuffer sb = new StringBuffer();
            sb.append(oneQuery.getQuery());
            sb.append("&&&");
            sb.append(oneQuery.getDomain());
            ps.println(sb.toString());
            reader.endObject();
        }
        reader.endArray();
        ps.close();
    }
}
