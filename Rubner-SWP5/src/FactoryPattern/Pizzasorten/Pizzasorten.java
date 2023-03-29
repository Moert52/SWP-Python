
package FactoryPattern.Pizzasorten;

public class Pizzasorten {
    public Pizzasorten() {
    }

    public static Pizza doPizza(String name) {
        if (name.contains("Salami")) {
            System.out.println("Salami - Pizza !");
            return new Pizza(name);
        } else if (name.contains("Hawaii")) {
            System.out.println("Hawaii - Pizza !");
            return new Pizza(name);
        } else if (name.contains("Calzone")) {
            System.out.println("Calzone - Pizza !");
            return new Pizza(name);
        } else if (name.contains("Quattro Stagioni")) {
            System.out.println("Salami - Pizza !");
            return new Pizza(name);
        } else if (name.contains("Sucuk")) {
            System.out.println("Salami - Pizza !");
            return new Pizza(name);
        } else if (name.contains("Döner")) {
            System.out.println("Döner - Pizza !");
            return new Pizza(name);
        } else {
            return null;
        }
    }
}
