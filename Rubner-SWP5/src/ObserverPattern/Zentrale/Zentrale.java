package ObserverPattern.Zentrale;

import ObserverPattern.Anzeige.AnzeigePull;
import ObserverPattern.Anzeige.AnzeigePush;
import ObserverPattern.Anzeige.Messdaten;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public abstract class Zentrale {
    private List<AnzeigePush> anzeigePushList = new ArrayList();
    private List<AnzeigePull> anzeigePullList = new ArrayList();

    public Zentrale() {
    }

    public void addAnzeigePush(AnzeigePush anzeigePush) {
        this.anzeigePushList.add(anzeigePush);
    }

    public void removeAnzeigePush(AnzeigePush anzeigePush) {
        this.anzeigePushList.remove(anzeigePush);
    }

    public void addAnzeigePull(AnzeigePull anzeigePull) {
        this.anzeigePullList.add(anzeigePull);
    }

    public void removeAnzeigePull(AnzeigePull anzeigePull) {
        this.anzeigePullList.remove(anzeigePull);
    }

    public void notifyAlleBeobachter(Messdaten messdaten) {
        Iterator var2 = this.anzeigePushList.iterator();

        while(var2.hasNext()) {
            AnzeigePush anzeigePush = (AnzeigePush)var2.next();
            anzeigePush.getMessdaten(messdaten);
        }

        var2 = this.anzeigePullList.iterator();

        while(var2.hasNext()) {
            AnzeigePull anzeigePull = (AnzeigePull)var2.next();
            anzeigePull.getMessdaten();
        }

    }
}