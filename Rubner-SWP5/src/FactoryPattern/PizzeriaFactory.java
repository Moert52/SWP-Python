
package FactoryPattern;

import FactoryPattern.Pizzasorten.Pizza;
import FactoryPattern.Standorte.BerlinPizzeria;

public class PizzeriaFactory {
    public PizzeriaFactory() {
    }

    public static Pizza getPizzeriaPizza(String pizza) {
        if (pizza.contains("Berlin")) {
            return (new BerlinPizzeria("BerlinosMertos", "Berlin")).neuePizzaMachen(pizza);
        } else if (pizza.contains("Hamburg")) {
            return (new BerlinPizzeria("HamMertorug", "Hamburg")).neuePizzaMachen(pizza);
        } else {
            return pizza.contains("Rostock") ? (new BerlinPizzeria("Roertstock", "Rostock")).neuePizzaMachen(pizza) : null;
        }
    }
}
