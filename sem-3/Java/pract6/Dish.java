package vuz.java.pract6;

abstract class Dish {
    private String material;

    public Dish(String material) {
        this.material = material;
    }

    public abstract void use();

    @Override
    public String toString() {
        return "This dish is made of " + material;
    }
}

class Plate extends Dish {
    public Plate(String material) {
        super(material);
    }

    @Override
    public void use() {
        System.out.println("Using a plate to eat.");
    }
}

class Cup extends Dish {
    public Cup(String material) {
        super(material);
    }

    @Override
    public void use() {
        System.out.println("Using a cup to drink.");
    }
}

