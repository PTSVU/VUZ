package vuz.java.pract3;

public class Author {
    private String name;
    private String email;
    private char gender;

    public Author(String name, String email, char gender) {
        this.name = name;
        this.email = email;
        this.gender = gender;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public char getGender() {
        return gender;
    }

    @Override
    public String toString() {
        String genderLabel;
        if (gender == 'M') {
            genderLabel = "m";
        } else if (gender == 'F') {
            genderLabel = "f";
        } else {
            genderLabel = "u";
        }
        return name + " (" + genderLabel + ") at " + email;
    }
}
