package ProxyPattern;

public class ProxyDrucker implements Drucker{
    private boolean sw = true;
    private Drucker drucker;
    @Override
    public void drucken(String dokument) {
        if (this.sw == true) {
            this.drucker = new SWDrucker();
        } else {
            this.drucker = new ColorDrucker();

        }
        drucker.drucken(dokument);

    }

    public void switchTo(String dokument) {
        if (this.sw == true) {
            this.drucker = new SWDrucker();
            this.drucker.drucken(dokument);
            this.sw = false;
        } else {
            this.drucker = new ColorDrucker();
            this.drucker.drucken(dokument);
            this.sw = true;
        }
    }
}
