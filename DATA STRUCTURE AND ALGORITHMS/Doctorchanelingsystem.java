package com.mycompany.doctorchannellingsystem;

import java.util.Scanner;

public class Doctorchanelingsystem {  // <- rename if needed
    static Scanner sc = new Scanner(System.in);
    static PatientStack stack = new PatientStack();

    public static void main(String[] args) {
        while (true) {
            System.out.println("Doctor Channelling System of XYZ Pvt Ltd");
            System.out.println("1. Register Patient (Push)");
            System.out.println("2. Call Next Patient (Pop)");
            System.out.println("3. Display Waiting Stack");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            int choice = sc.nextInt();
            sc.nextLine(); // clear buffer

            if (choice == 1) {
                registerPatient();
            } else if (choice == 2) {
                callNextPatient();
            } else if (choice == 3) {
                stack.displayStack();
            } else if (choice == 4) {
                System.out.println("Exit from XYZ Channelling System. Thank you!");
                break;
            } else {
                System.out.println("Invalid choice. Try again.");
            }
        }
    }

    public static void registerPatient() {
        System.out.print("Enter Patient Name: ");
        String name = sc.nextLine();
        System.out.print("Mobile: ");
        String mobile = sc.nextLine();
        System.out.print("Email: ");
        String email = sc.nextLine();
        System.out.print("City: ");
        String city = sc.nextLine();
        System.out.print("Age: ");
        int age = sc.nextInt();
        sc.nextLine(); // clear buffer
        System.out.print("Medical History: ");
        String history = sc.nextLine();

        Patient p = new Patient(name, mobile, email, city, age, history);
        stack.push(p);
        System.out.println("Patient added to waiting list.");
    }

    public static void callNextPatient() {
        Patient p = stack.pop();
        if (p != null) {
            System.out.println("Calling patient:");
            System.out.println(p);
        }
    }
}