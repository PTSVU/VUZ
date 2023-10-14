package vuz.java.pract6;

abstract class Furniture {
    private String type;

    public Furniture(String type) {
        this.type = type;
    }

    public abstract void use();

    @Override
    public String toString() {
        return "This is a " + type;
    }
}

class Chair extends Furniture {
    public Chair(String type) {
        super(type);
    }

    @Override
    public void use() {
        System.out.println("Sitting on a chair.");
    }
}

class Table extends Furniture {
    public Table(String type) {
        super(type);
    }

    @Override
    public void use() {
        System.out.println("Using a table.");
    }
}

class FurnitureShop {
    private Furniture[] inventory;

    public FurnitureShop(int capacity) {
        inventory = new Furniture[capacity];
    }

    public void addFurniture(Furniture furniture, int index) {
        if (index >= 0 && index < inventory.length) {
            inventory[index] = furniture;
        } else {
            System.out.println("Invalid index.");
        }
    }

    public void showInventory() {
        System.out.println("Furniture Inventory:");
        for (Furniture furniture : inventory) {
            if (furniture != null) {
                System.out.println(furniture);
                furniture.use();
            }
        }
    }
}

