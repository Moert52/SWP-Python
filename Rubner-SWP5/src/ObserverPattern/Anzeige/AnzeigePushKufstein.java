package ObserverPattern.Anzeige;

import ObserverPattern.Zentrale.ZentraleKufstein;

public class AnzeigePushKufstein implements AnzeigePush {
    public AnzeigePushKufstein() {
    }

    public void getMessdaten(Messdaten messdaten) {
        System.out.printf("Jetztige Temperatur: %.2f \nJetztige Feutchigkeit: %.2f\n", messdaten.getTemp(), messdaten.getFeucht());
    }
}
