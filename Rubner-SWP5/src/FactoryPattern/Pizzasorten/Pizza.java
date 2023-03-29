
package FactoryPattern.Pizzasorten;

import java.io.PrintStream;

public class Pizza {
    private String name;

    public Pizza(String name) {
        this.name = name;
    }

    public String einpacken() {
        return "Packe " + this.name + " ein  |\n";
    }

    public String backen() {
        return "Backe " + this.name + "\t| \n";
    }

    public String schneiden() {
        return "Schneide " + this.name + " |\n";
    }

    public void PizzaMachen() {
        PrintStream var10000 = System.out;
        String var10001 = this.backen();
        var10000.println(var10001 + this.schneiden() + this.einpacken());
    }
}
