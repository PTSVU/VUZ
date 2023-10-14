package vuz.java.pract2;

class Dog {
    private String name;
    private int age;

    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int calculateHumanAge() {
        return age * 7;
    }

    @Override
    public String toString() {
        return "Dog{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}

class DogKennel {
    private Dog[] dogs;
    private int size;

    public DogKennel(int capacity) {
        dogs = new Dog[capacity];
        size = 0;
    }

    public void addDog(Dog dog) {
        if (size < dogs.length) {
            dogs[size] = dog;
            size++;
        } else {
            System.out.println("Питомник собак полон, нельзя добавить больше собак.");
        }
    }

    public void printKennel() {
        System.out.println("Собаки в питомнике:");
        for (int i = 0; i < size; i++) {
            System.out.println(dogs[i]);
        }
    }

    public static void main(String[] args) {
        DogKennel kennel = new DogKennel(3);

        Dog dog1 = new Dog("Барон", 3);
        Dog dog2 = new Dog("Рекс", 5);
        Dog dog3 = new Dog("Бобик", 2);

        kennel.addDog(dog1);
        kennel.addDog(dog2);
        kennel.addDog(dog3);

        kennel.printKennel();
    }
}
