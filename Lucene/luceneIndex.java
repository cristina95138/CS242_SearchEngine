import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.analysis.analysis.Analyzer;
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
import java.util.List;

// import static constant.constant.JSON_FILE_PATH;


public class luceneIndex {

    public static JSONArray parseJSON() {
        try {
            InputStream jsonFile = new FileInputStream("sample_data.json"); 
            Reader readJSON = new InputStreamReader(jsonFile);
            Object fileObj = JSONValue.parse(readJSON);
            JSONArray arr = (JSONArray) fileObj;
        return arr;
        } catch (Exception e) {
            System.out.println("Error" + e.getMessage());
        }
    }
    public void addDocuments(JSONArray jsonObjects) {
        
    }
    public static void main(String[] args) throws IOException, ParseException, FileNotFoundException{
        Analyzer analyzer = new StandardAnalyzer();

        // For Testing
        Directory directory = new RAMDirectory();

        IndexWriterConfig config = new IndexWriterConfig(analyzer);
        IndexWriter iw = new IndexWriter(directory, config);

        JSONArray arr = parseJSON();

        for(JSONObject obj : (List<JSONObject>) jsonObjects) {
            Document doc = new Document();
            doc.add(new TextField("job_title", (String)obj.get("job_title"), Field.Store.YES));
            doc.add(new TextField("summary", (String)obj.get("summary"), Field.Store.NO));
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
        Query query = parser.parse("cashier");

        System.out.println(query.toString());
        ScoreDoc[] hits = indexSearcher.search(query, 10).scoreDocs;

        for(ScoreDoc hit:hits) {
            Document doc = indexSearcher.doc(hit.doc);
            System.out.println(hit.score + " " + doc.get("location"));
        }

        indexReader.close();
        directory.close();

    }
}
