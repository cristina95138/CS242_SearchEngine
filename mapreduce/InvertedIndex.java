import java.io.IOException;
import java.util.*;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.MapContext;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;

public class InvertedIndex {
  public static Set<String> stopWords = new HashSet<>(Arrays.asList("job", "title", "summary", "url", "description", "company", "location"));
  public static class InvertedIndexMapper
       extends Mapper<Object, Text, Text, Text>{

    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {

      String DocId = ((FileSplit) context.getInputSplit()).getPath().getName();
      
      StringTokenizer itr = new StringTokenizer(value.toString().replaceAll("[^a-zA-Z0-9]", " ").toLowerCase(), " \\'-\",");
      
      while (itr.hasMoreTokens()) {
        word.set(itr.nextToken().replaceAll("\\s", ""));
        if(stopWords.contains(word.toString()))
          continue;
        context.write(word, new Text(DocId));
      }
    }
  }

  public static class InvertedIndexReducer
       extends Reducer<Text,Text,Text,Text> {
    
    public void reduce(Text key, Iterable<Text> values,
                       Context context
                       ) throws IOException, InterruptedException {

      HashMap<String,Integer> mp = new HashMap<String,Integer>();
      for (Text val : values) {
        if (mp.containsKey(val.toString())) {
          mp.put(val.toString(), mp.get(val.toString()) + 1);
        } else {
          mp.put(val.toString(), 1);
        }
      }
      StringBuilder docList = new StringBuilder();
      for(String docID : mp.keySet()){
        if(mp.get(docID) > 5)
          docList.append(docID + ":" + mp.get(docID) + " ");
      }
      if(docList.toString().length() > 2)
        context.write(key, new Text(docList.toString()));
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "inverted index");
    job.setJarByClass(InvertedIndex.class);
    job.setMapperClass(InvertedIndexMapper.class);
    job.setReducerClass(InvertedIndexReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(Text.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}