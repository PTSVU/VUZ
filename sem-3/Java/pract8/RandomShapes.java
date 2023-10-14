package vuz.java.pract8;

import javax.swing.*;
import java.awt.*;
import java.util.Random;

abstract class Shape {
    private Color color;
    private int x;
    private int y;

    public Shape(Color color, int x, int y) {
        this.color = color;
        this.x = x;
        this.y = y;
    }

    public Color getColor() {
        return color;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public abstract void draw(Graphics g);
}

class Circle extends Shape {
    private int radius;

    public Circle(Color color, int x, int y, int radius) {
        super(color, x, y);
        this.radius = radius;
    }

    @Override
    public void draw(Graphics g) {
        g.setColor(getColor());
        g.fillOval(getX(), getY(), 2 * radius, 2 * radius);
    }
}

class Rectangle extends Shape {
    private int width;
    private int height;

    public Rectangle(Color color, int x, int y, int width, int height) {
        super(color, x, y);
        this.width = width;
        this.height = height;
    }

    @Override
    public void draw(Graphics g) {
        g.setColor(getColor());
        g.fillRect(getX(), getY(), width, height);
    }
}

public class RandomShapes {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Random Shapes");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(400, 400);
            Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

            JPanel panel = new JPanel() {
                @Override
                protected void paintComponent(Graphics g) {
                    super.paintComponent(g);
                    Random random = new Random();

                    for (int i = 0; i < 20; i++) {
                        int x = random.nextInt(300);
                        int y = random.nextInt(300);
                        int widthOrRadius = random.nextInt(50);
                        int height = random.nextInt(50);
                        Color color = new Color(random.nextInt(256), random.nextInt(256), random.nextInt(256));

                        if (i % 2 == 0) {
                            Circle circle = new Circle(color, x, y, widthOrRadius);
                            circle.draw(g);
                        } else {
                            Rectangle rectangle = new Rectangle(color, x, y, widthOrRadius, height);
                            rectangle.draw(g);
                        }
                    }
                }
            };

            int centerX = (screenSize.width - frame.getWidth()) / 2;
            int centerY = (screenSize.height - frame.getHeight()) / 2;
            frame.setLocation(centerX, centerY);

            frame.add(panel);
            frame.setVisible(true);
        });
    }
}