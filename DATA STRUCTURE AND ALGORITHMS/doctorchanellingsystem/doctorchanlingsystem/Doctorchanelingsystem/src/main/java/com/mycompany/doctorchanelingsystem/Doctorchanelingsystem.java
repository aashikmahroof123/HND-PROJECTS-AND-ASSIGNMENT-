package com.mycompany.doctorchanelingsystem;

import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;


public class Doctorchanelingsystem {
    static Scanner input = new Scanner(System.in);
    static List<patient> patient = new ArrayList<>();
    static List<Doctor> Doctor_1 = new ArrayList<>();
    static Queue<Appointment> waitingList = new LinkedList<>();
    static List<Appointment> appointments = new ArrayList<>();

    public static void main(String[] args) {
        boolean running = true;

        while (running) {
            System.out.println("\n--- Doctor Channeling System ---");
            System.out.println("1. Register Patient");
            System.out.println("2. Register Doctor");
            System.out.println("3. Search Available Doctors");
            System.out.println("4. Book Appointment");
            System.out.println("5. Cancel Appointment");
            System.out.println("6. Reschedule Appointment");
            System.out.println("7. View All Appointments");
            System.out.println("8. Exit");
            System.out.print("Enter your choice: ");
            int choice = input.nextInt();
            input.nextLine();  // consume newline

            switch (choice) {
                case 1 -> registerPatient();
                case 2 -> registerDoctor();
                case 3 -> searchDoctors();
                case 4 -> bookAppointment();
                case 5 -> cancelAppointment();
                case 6 -> rescheduleAppointment();
                case 7 -> displayAppointments();
                case 8 -> running = false;
                default -> System.out.println("Invalid choice! Try again.");
            }
        }
    }

    static void registerPatient() {
        System.out.print("Enter name: ");
        String name = input.nextLine();
        System.out.print("Enter mobile number: ");
        String mobile = input.nextLine();
        System.out.print("Enter email ID: ");
        String email = input.nextLine();
        System.out.print("Enter city: ");
        String city = input.nextLine();
        System.out.print("Enter age: ");
        int age = input.nextInt();
        input.nextLine();
        System.out.print("Enter medical history: ");
        String medicalHistory = input.nextLine();

        Patient patient = new Patient(name, mobile, email, city, age, medicalHistory);
        patient.add(patient);
        System.out.println("Patient registered successfully.");
    }

    static void registerDoctor() {
        System.out.print("Enter doctor ID: ");
        String id = input.nextLine();
        System.out.print("Enter name: ");
        String name = input.nextLine();
        System.out.print("Enter specialization: ");
        String specialization = input.nextLine();
        System.out.print("Enter number of available slots: ");
        int slotCount = input.nextInt();
        input.nextLine();
        String[] slots = new String[slotCount];
        for (int i = 0; i < slotCount; i++) {
            System.out.print("Enter slot " + (i + 1) + ": ");
            slots[i] = input.nextLine();
        }
        System.out.print("Enter consultation fee: ");
        double fee = input.nextDouble();
        input.nextLine();

        Doctor doctor = new Doctor(id, name, specialization, slots, fee);
        doctors.add(doctor);
        System.out.println("Doctor registered successfully.");
    }

    static void searchDoctors() {
        System.out.print("Enter specialization to search: ");
        String specialization = input.nextLine();
        boolean found = false;
        for (Doctor doc : doctors) {
            if (doc.getSpecialization().equalsIgnoreCase(specialization)) {
                System.out.println(doc);
                found = true;
            }
        }
        if (!found) {
            System.out.println("No doctors found with that specialization.");
        }
    }

    static void bookAppointment() {
        if (patients.isEmpty() || doctors.isEmpty()) {
            System.out.println("Please register patient and doctor first.");
            return;
        }

        System.out.print("Enter patient name: ");
        String patientName = input.nextLine();
        Patient selectedPatient = null;
        for (Patient p : patients) {
            if (p.getName().equalsIgnoreCase(patientName)) {
                selectedPatient = p;
                break;
            }
        }
        if (selectedPatient == null) {
            System.out.println("Patient not found.");
            return;
        }

        System.out.print("Enter doctor ID: ");
        String doctorId = input.nextLine();
        Doctor selectedDoctor = null;
        for (Doctor d : doctors) {
            if (d.getId().equalsIgnoreCase(doctorId)) {
                selectedDoctor = d;
                break;
            }
        }
        if (selectedDoctor == null) {
            System.out.println("Doctor not found.");
            return;
        }

        System.out.println("Available Slots:");
        String[] slots = selectedDoctor.getAvailableSlots();
        for (int i = 0; i < slots.length; i++) {
            System.out.println((i + 1) + ". " + slots[i]);
        }
        System.out.print("Select slot number: ");
        int slotNum = input.nextInt();
        input.nextLine();
        if (slotNum < 1 || slotNum > slots.length) {
            System.out.println("Invalid slot selected.");
            return;
        }

        String slotChosen = slots[slotNum - 1];
        Appointment newAppointment = new Appointment(selectedPatient, selectedDoctor, slotChosen);
        appointments.add(newAppointment);
        System.out.println("Appointment booked and confirmation sent to " + selectedPatient.getName());
    }

    static void cancelAppointment() {
        System.out.print("Enter patient name to cancel: ");
        String patientName = input.nextLine();
        Appointment toCancel = null;
        for (Appointment app : appointments) {
            if (app.getPatient().getName().equalsIgnoreCase(patientName)) {
                toCancel = app;
                break;
            }
        }

        if (toCancel != null) {
            appointments.remove(toCancel);
            System.out.println("Appointment cancelled for " + patientName);

            if (!waitingList.isEmpty()) {
                Appointment next = waitingList.poll();
                appointments.add(next);
                System.out.println("Next patient from waiting list notified: " + next.getPatient().getName());
            }
        } else {
            System.out.println("No appointment found for that patient.");
        }
    }

    static void rescheduleAppointment() {
        System.out.print("Enter patient name to reschedule: ");
        String patientName = input.nextLine();
        Appointment toReschedule = null;

        for (Appointment app : appointments) {
            if (app.getPatient().getName().equalsIgnoreCase(patientName)) {
                toReschedule = app;
                break;
            }
        }

        if (toReschedule != null) {
            appointments.remove(toReschedule);
            waitingList.add(toReschedule);
            System.out.println("Appointment moved to waiting queue for " + patientName);
        } else {
            System.out.println("No appointment found for that patient.");
        }
    }

    static void displayAppointments() {
        if (appointments.isEmpty()) {
            System.out.println("No appointments scheduled.");
        } else {
            for (Appointment app : appointments) {
                System.out.println(app);
            }
        }
    }
}