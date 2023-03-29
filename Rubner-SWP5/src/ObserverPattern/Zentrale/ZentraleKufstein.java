package ObserverPattern.Zentrale;

import ObserverPattern.Anzeige.Messdaten;

public class ZentraleKufstein extends Zentrale {
    private Messdaten messdaten;

    public ZentraleKufstein() {
    }

    public void setMessdaten(Messdaten messdaten) {
        this.messdaten = messdaten;
        this.notifyAlleBeobachter(messdaten);
    }

    public Messdaten getAktuelleMessdaten() {
        return this.messdaten;
    }
}