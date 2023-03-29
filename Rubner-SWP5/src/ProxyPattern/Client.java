package ProxyPattern;

public class Client {
    public static void main(String[] args) {
        Drucker drucker = new ProxyDrucker();
        drucker.drucken("test.docx");
        drucker.switchTo("Diplom.docx");
        drucker.switchTo("Präsi.docx");

    }
}
