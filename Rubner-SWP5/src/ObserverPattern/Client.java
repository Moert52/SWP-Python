package ObserverPattern;

import ObserverPattern.Anzeige.AnzeigePullEbbs;
import ObserverPattern.Anzeige.AnzeigePullSchwoich;
import ObserverPattern.Anzeige.AnzeigePushKufstein;
import ObserverPattern.Anzeige.Messdaten;
import ObserverPattern.Zentrale.ZentraleKufstein;

public class Client {
    public static void main(String[] args) {
        ZentraleKufstein zentraleKufstein = new ZentraleKufstein();
        zentraleKufstein.addAnzeigePush(new AnzeigePushKufstein());
        zentraleKufstein.addAnzeigePush(new AnzeigePushKufstein());
        zentraleKufstein.addAnzeigePull(new AnzeigePullSchwoich(zentraleKufstein));
        zentraleKufstein.addAnzeigePull(new AnzeigePullEbbs(zentraleKufstein));
        zentraleKufstein.setMessdaten(new Messdaten(10.5, 3.5));
    }
}