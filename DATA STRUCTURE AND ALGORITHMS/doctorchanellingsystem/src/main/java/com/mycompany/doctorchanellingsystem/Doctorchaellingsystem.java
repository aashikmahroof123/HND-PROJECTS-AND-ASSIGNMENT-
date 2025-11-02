package com.mycompany.doctorchannellingsystem;

import java.util.*;

public class Doctorchaellingsystem {

    static Scanner input = new Scanner(System.in);
    static List<Patient> patients = new ArrayList<>();

    public static void main(String[] args) {
        registerPatient(); // Call the method directly for test
    }

    public static void registerPatient() {
        try {
            System.out.print("Enter Patient Name: ");
            String name = input.nextLine();
            if (name.isEmpty()) {
                throw new IllegalArgumentException("Name cannot be empty.");
            }

            System.out.print("Enter Mobile Number: ");
            String mobile = input.nextLine();

            System.out.print("Enter Email: ");
            String email = input.nextLine();
            if (!email.contains("@")) {
                throw new IllegalArgumentException("Invalid email format.");
            }

            System.out.print("Enter City: ");
            String city = input.nextLine();

            System.out.print("Enter Age: ");
            int age = input.nextInt();
            input.nextLine();
            if (age <= 0) {
                throw new IllegalArgumentException("Age must be greater than 0.");
            }

            System.out.print("Enter Medical History: ");
            String history = input.nextLine();

            patients.add(new Patient(name, mobile, email, city, age, history));
            System.out.println(" Patient registered successfully.");

        } catch (InputMismatchException e) {
            System.out.println(" Invalid input type. Please enter numbers where required.");
            input.nextLine();
        } catch (IllegalArgumentException e) {
            System.out.println(" " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Unexpected error: " + e.getMessage());
        }
    }

    public static class Patient {
        private String name, mobile, email, city, medicalHistory;
        private int age;

        public Patient(String name, String mobile, String email, String city, int age, String history) {
            this.name = name;
            this.mobile = mobile;
            this.email = email;
            this.city = city;
            this.age = age;
            this.medicalHistory = history;
        }

        public String toString() {
            return name + " | " + mobile + " | " + email + " | " + city + " | " + age + " | " + medicalHistory;
        }
    }
}
