package FactoryPattern.Standorte;

import FactoryPattern.Pizzasorten.Pizza;

public class RostockPizzeria extends PizzeriaMertos {
    private String name;
    private String standort;

    public RostockPizzeria(String name, String standort) {
        this.name = name;
        this.standort = standort;
    }

    public String getPizzariaName() {
        return this.name;
    }

    public String getPizzeriaStandort() {
        return this.standort;
    }

    protected Pizza neuePizzaMachen(String zuMachendePizza) {
        System.out.printf("In der Pizzeria:   in   wird jetzt eine neue Pizza gemacht: \n", this.getPizzariaName(), this.getPizzeriaStandort());
        return this.machPizza(zuMachendePizza);
    }
}
