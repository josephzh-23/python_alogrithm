//package Final;
//
//import com.aspose.words.*;
//
//import static jdk.internal.net.http.SocketTube.listOf;
//
//public class ReadWordDocumentInJava {
//
//	public static void Sliding_window.maining_window.Sliding_window.Graph.Hard.main(String[] args) throws Exception {// Main function to read Word file in Java
//
//
////		var words = ("why", "how", "what")
//	    // Create a license object to avoid limitations of the trial version
//	    // while reading the Word file
////	    License licWordToPdf = new License();
////	    licWordToPdf.setLicense("Aspose.Words.lic");
//
//	    // Load the source Word file to be read
//
//	    Document doc = new Document("/Users/josephzh/Desktop/photo_app.docx");
//
//
//
//	    // Read all the paragraph in the document and display its contents
//	    for (Object obj : doc.getChildNodes(NodeType.PARAGRAPH, true))
//	    {
//		Paragraph para = (Paragraph)obj;
//		System.out.println(para.toString(SaveFormat.TEXT));
//	    }
//
//	    // Read all the Runs in the document and display style and text
//	    for (Object obj : doc.getChildNodes(NodeType.RUN, true))
//	    {
//		Run run = (Run)obj;
//		Font font = run.getFont();
//		System.out.println(font.getName() + "," + font.getSize());
//		System.out.println(run.getText());
//	    }
//
//	    System.out.println("Done");
//	}
//}