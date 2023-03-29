
package FactoryPattern.Standorte;

import FactoryPattern.Pizzasorten.Pizza;
import FactoryPattern.Pizzasorten.Pizzasorten;

public abstract class PizzeriaMertos {
    public PizzeriaMertos() {
    }

    public abstract String getPizzariaName();

    public abstract String getPizzeriaStandort();

    public Pizza machPizza(String zuMachendePizza) {
        Pizza pizza = Pizzasorten.doPizza(zuMachendePizza);
        pizza.PizzaMachen();
        return pizza;
    }

    protected abstract Pizza neuePizzaMachen(String var1);
}
