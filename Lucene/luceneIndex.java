import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.document.*;
import org.apache.lucene.index.FieldInfo;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.queryparser.classic.MultiFieldQueryParser;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.store.ByteBuffersDirectory;
import org.apache.lucene.util.Version;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

import java.io.*;
import java.text.ParseException;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;


// import static constant.constant.JSON_FILE_PATH;


public class luceneIndex {

    public static JSONArray removeDuplicates (JSONArray arr) {
       
        JSONArray temp=new JSONArray();
        Set<String> set =new HashSet<String>();

        for (int i = 0; i < arr.size(); i++) {
            JSONObject jobject = (JSONObject) arr.get(i);
            String str = jobject.toJSONString();
       
            if(set.contains(str)) continue;
            else{
                set.add(str);
                temp.add(arr.get(i));
            }
        }
        return temp;
    }
    public static JSONArray parseJSON() throws FileNotFoundException {

        InputStream jsonFile = new FileInputStream("indeed_combined.json");
        Reader readJSON = new InputStreamReader(jsonFile);
        Object fileObj = JSONValue.parse(readJSON);
        JSONArray arr = (JSONArray) fileObj;
        return removeDuplicates(arr);
    }
    
    public static void main(String[] args) throws IOException, ParseException, FileNotFoundException{

        long start = System.currentTimeMillis();
        
        Analyzer analyzer = new StandardAnalyzer();

        // For Testing
        Directory directory = new ByteBuffersDirectory();

        IndexWriterConfig config = new IndexWriterConfig(analyzer);
        // config.setRAMBufferSizeMB(48);
        // config.setMaxBufferedDocs(30000);
        IndexWriter iw = new IndexWriter(directory, config);

        // Parsing json file to an array
        JSONArray arr = parseJSON();

        // adding documents
        for(JSONObject obj : (List<JSONObject>) arr) {
            Document doc = new Document();
            doc.add(new TextField("job_title", (String)obj.get("job_title"), Field.Store.YES));
            doc.add(new TextField("summary", (String)obj.get("summary"), Field.Store.YES));
            doc.add(new TextField("company", (String)obj.get("company"), Field.Store.YES));
            doc.add(new TextField("location", (String)obj.get("location"), Field.Store.YES));
            doc.add(new TextField("job_description", (String)obj.get("job_description"), Field.Store.NO));
            doc.add(new TextField("url", (String)obj.get("url"), Field.Store.NO));
            iw.addDocument(doc);
        }
        iw.close();

        // Searching the index

        DirectoryReader indexReader = DirectoryReader.open(directory);
        IndexSearcher indexSearcher = new IndexSearcher(indexReader);
        QueryParser parser = new QueryParser("job_title", analyzer);
        try {
            Query query = parser.parse("cashier");

            System.out.println(query.toString());
            ScoreDoc[] hits = indexSearcher.search(query, 10).scoreDocs;

            for(ScoreDoc hit:hits) {
                Document doc = indexSearcher.doc(hit.doc);
                System.out.println(hit.score + " " + doc.get("location"));
        }

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        // Closing the opened resources
        indexReader.close();
        directory.close();

        long end = System.currentTimeMillis();
        float sec = (end - start) / 1000F; 
        System.out.println("This Program rus in " + sec + " seconds");
    }
}
