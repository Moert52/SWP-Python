

package FactoryPattern;

import FactoryPattern.Pizzasorten.Pizza;

public class Main {
    public Main() {
    }

    public static void main(String[] args) {
        Pizza BerlinSucukpizza = PizzeriaFactory.getPizzeriaPizza("BerlinSucuk");
        Pizza Calzonepizza = PizzeriaFactory.getPizzeriaPizza("HamburgCalzone");
    }
}
