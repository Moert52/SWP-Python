package ObserverPattern.Anzeige;



public class Messdaten {
    private final double temperatur;
    private final double feuchtigkeit;

    public Messdaten(double temperatur, double feuchtigkeit) {
        this.temperatur = temperatur;
        this.feuchtigkeit = feuchtigkeit;
    }

    public Double getTemp() {
        return this.temperatur;
    }

    public Double getFeucht() {
        return this.feuchtigkeit;
    }
}




