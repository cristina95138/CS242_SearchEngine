package indexing_json;

import path_constants.Constants;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.util.Iterator;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.LowerCaseFilter;
import org.apache.lucene.analysis.standard.StandardTokenizer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.FieldType;
import org.apache.lucene.index.IndexOptions;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class JobIndex {
    public Index() throws FileNotFoundException, IOException, ParseException {
        Directory dir = null;

        dir = FSDirectory.open(new File(Constants.INDEX_PATH_REDDIT).toPath());

        Analyzer analyzer;
        analyzer = new Analyzer() {

            @Override
            protected TokenStreamComponents createComponents(String fieldName) {

                TokenStreamComponents ts = new TokenStreamComponents(new StandardTokenizer());

                ts = new TokenStreamComponents(ts.getSource(), new LowerCaseFilter(ts.getTokenStream()));
                ts = new TokenStreamComponents( ts.getTokenizer(), new StopFilter( ts.getTokenStream(), StandardAnalyzer.ENGLISH_STOP_WORDS_SET));
                ts = new TokenStreamComponents( ts.getTokenizer(), new KStemFilter( ts.getTokenStream()));
                ts = new TokenStreamComponents( ts.getTokenizer(), new PorterStemFilter( ts.getTokenStream()));

                return ts;
            }
        };

        IndexWriterConfig config = new IndexWriterConfig(analyzer);

        config.setOpenMode(IndexWriterConfig.OpenMode.CREATE);

        IndexWriter ixwriter = null;
        ixwriter = new IndexWriter(dir, config);

        FieldType fieldTypeMetadata = new FieldType();
        fieldTypeMetadata.setOmitNorms(true);
        fieldTypeMetadata.setIndexOptions(IndexOptions.DOCS);
        fieldTypeMetadata.setStored(true);
        fieldTypeMetadata.setTokenized(false);
        fieldTypeMetadata.freeze();

        FieldType fieldTypeText = new FieldType();
        fieldTypeText.setIndexOptions(IndexOptions.DOCS_AND_FREQS_AND_POSITIONS);
        fieldTypeText.setStoreTermVectors(true);
        fieldTypeText.setStoreTermVectorPositions(true);
        fieldTypeText.setTokenized(true);
        fieldTypeText.setStored(true);
        fieldTypeText.freeze();

        InputStream instream = null;

        instream = new FileInputStream(Constants.FILE_PATH_REDDIT);

        instream.close();

        JSONArray jsonArray = (JSONArray) new JSONParser().parse(new FileReader(Constants.FILE_PATH_REDDIT));

        Iterator i = jsonArray.iterator();
        System.out.println("Indexing...");
        System.out.println("Please Wait...");
        int jCounter = 0;
        while (i.hasNext()) {
            jCounter++;
            JSONObject slide = (JSONObject) i.next();

            Document d = new Document();

            d.add(new Field("id", (String) slide.get("id"), fieldTypeMetadata));
            d.add(new Field("body", (String) slide.get("body"), fieldTypeText));
            d.add(new Field("score", (long) slide.get("score") + "", fieldTypeText));
            d.add(new Field("title", (String) slide.get("title"), fieldTypeText));
            //    d.add( new Field( "text", text, fieldTypeText ) );

            ixwriter.addDocument(d);
        } System.out.println("Indexed "+jCounter+" JSON Objects");

        ixwriter.close();
        dir.close();

    }
}