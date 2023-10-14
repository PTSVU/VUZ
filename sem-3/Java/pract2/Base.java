package vuz.java.pract2;

public class Base {

    int pract_num = 2;
    int task_num;

    public Base(int task_num) {
        this.task_num = task_num;
        if (pract_num > 0) {
            if (task_num == 0) {
                System.out.println("Практическая " + pract_num + "\n");
            }
            if (task_num > 0) {
                System.out.println("Практическая " + pract_num + ", задание " + task_num + "\n");
            }
        }
    }
}
