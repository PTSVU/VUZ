package vuz.java.pract6;

public class FurnitureTest {
    public static void main(String[] args) {
        FurnitureShop shop = new FurnitureShop(2);
        Furniture chair = new Chair("wooden");
        Furniture table = new Table("glass");

        shop.addFurniture(chair, 0);
        shop.addFurniture(table, 1);

        shop.showInventory();
    }
}
