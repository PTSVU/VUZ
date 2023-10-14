package vuz.java.pract6;

abstract class Dog {
    private String name;
    private int age;

    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public abstract void bark();

    @Override
    public String toString() {
        return "Name: " + name + ", Age: " + age;
    }
}

class Labrador extends Dog {
    public Labrador(String name, int age) {
        super(name, age);
    }

    @Override
    public void bark() {
        System.out.println("Labrador is barking.");
    }
}

class Bulldog extends Dog {
    public Bulldog(String name, int age) {
        super(name, age);
    }

    @Override
    public void bark() {
        System.out.println("Bulldog is barking.");
    }
}

