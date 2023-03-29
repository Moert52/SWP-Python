package ObserverPattern.Anzeige;

import ObserverPattern.Zentrale.ZentraleKufstein;

public class AnzeigePullSchwoich implements AnzeigePull {
    private ZentraleKufstein zentrale;
    private double feuchtigkeit;

    public AnzeigePullSchwoich(ZentraleKufstein zentrale) {
        this.zentrale = zentrale;
    }

    public void getMessdaten() {
        this.feuchtigkeit = this.zentrale.getAktuelleMessdaten().getFeucht();
        System.out.printf("Feuchtigkeit von der Zentrale geholt | Feucht: %.2f \n", this.feuchtigkeit);
    }
}
