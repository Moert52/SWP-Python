package ProxyPattern;

public class SWDrucker implements Drucker{
    @Override
    public void drucken(String dokument) {
        System.out.printf("Das Dokument %s wird in schwarz weiß gedruckt \n", dokument);
    }

    @Override
    public void switchTo(String s) {

    }
}
