package ProxyPattern;

public class ColorDrucker implements Drucker{
    @Override
    public void drucken(String dokument) {
        System.out.printf("Das Dokument %s wird in Farbe gedruckt\n", dokument);
    }

    @Override
    public void switchTo(String s) {

    }
}
