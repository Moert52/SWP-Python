package ObserverPattern.Anzeige;


import ObserverPattern.Zentrale.ZentraleKufstein;

public class AnzeigePullEbbs implements AnzeigePull {
    private ZentraleKufstein zentrale;
    private double temperatur;

    public AnzeigePullEbbs(ZentraleKufstein zentrale) {
        this.zentrale = zentrale;
    }

    public void getMessdaten() {
        this.temperatur = this.zentrale.getAktuelleMessdaten().getTemp();
        System.out.printf("Temperatur von der Zentrale geholt | Temp: %.2f \n", this.temperatur);
    }
}
