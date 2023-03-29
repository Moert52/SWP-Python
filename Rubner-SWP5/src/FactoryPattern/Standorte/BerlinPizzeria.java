//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

package FactoryPattern.Standorte;

import FactoryPattern.Pizzasorten.Pizza;

public class BerlinPizzeria extends PizzeriaMertos {
    private String name;
    private String standort;

    public BerlinPizzeria(String name, String standort) {
        this.name = name;
        this.standort = standort;
    }

    public String getPizzariaName() {
        return this.name;
    }

    public String getPizzeriaStandort() {
        return this.standort;
    }

    public Pizza neuePizzaMachen(String zuMachendePizza) {
        System.out.printf("In der Pizzeria: %s in %s wird jetzt eine neue Pizza gemacht: \n", this.getPizzariaName(), this.getPizzeriaStandort());
        return this.machPizza(zuMachendePizza);
    }
}



