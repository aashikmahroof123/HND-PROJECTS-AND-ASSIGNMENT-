package com.mycompany.doctorchannellingsystem;

import java.util.*;
import java.util.ArrayList;
import java.util.Scanner;


//doctor channeling system of xyz private limited
class Doctorchanelingsystem {

    static Scanner input = new Scanner(System.in);
    static List<Patient> patients = new ArrayList<>();
    static List<Doctor> doctors = new ArrayList<>();
    static Queue<Appointment> waitingList = new LinkedList<>();
    static List<Appointment> appointments = new ArrayList<>();

    public static void main(String[] args) {
Doctorchanelingsystem system = new Doctorchanelingsystem();
 Scanner input = new Scanner(System.in);
        while (true) {
            System.out.println("");
            System.out.println("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$");
            System.out.println("Doctor Channeling System of XYZ Private Limited");
            System.out.println("1. Register Patient");
            System.out.println("2. Register Doctor");
            System.out.println("3. Search Doctor");
            System.out.println("4. Book Appointment");
            System.out.println("5. Cancel Appointment");
            System.out.println("6. Request Reschedule");
            System.out.println("7. Show All Appointments");
            System.out.println("8. Exit");
            System.out.println("9. Display All Registered Patients");
            System.out.println("10. Display All Registered Doctors");
            System.out.print("Enter your choice:1  |  2|  3|  4|  5|  6|  7|  8|  9|  10   ");
            int choice = input.nextInt();
            input.nextLine();  // clear buffer

            if (choice == 1) {
                registerPatient();
            } else if (choice == 2) {
                registerDoctor();
            } else if (choice == 3) {
                searchDoctor();
            } else if (choice == 4) {
                bookAppointment();
            } else if (choice == 5) {
                cancelAppointment();
            } else if (choice == 6) {
                requestReschedule();
            } else if (choice == 7) {
                displayAppointments();
            } else if (choice == 8) {
                System.out.println("YOU ARE EXIT FROM THE XYZ CHANELLING SYSTEM. THANK YOU, WELCOME!");
                break;
            } else if (choice == 9) {
                displayAllPatients();
            } else if (choice == 10) {
                displayAllDoctors();
            } else {
                System.out.println("Invalid choice. Try again.");
            }
        }

        input.close();
    }

    public static void displayAllPatients() {
        System.out.println("**** **** Registered Patients **** ****");
        if (patients.isEmpty()) {
            System.out.println("**** No patients registered ****.");
        } else {
            for (int i = 0; i < patients.size(); i++) {
                System.out.println((i + 1) + ". " + patients.get(i));
            }
        }
    }

    public static void displayAllDoctors() {
        System.out.println("**** **** Registered Doctors **** ****");
        if (doctors.isEmpty()) {
            System.out.println("**** No doctors registered ****.");
        } else {
            for (int i = 0; i < doctors.size(); i++) {
                System.out.println((i + 1) + ". " + doctors.get(i));
            }
        }
    }
//register a patient in xyz private limited
    public static void registerPatient() {
Scanner input = new Scanner(System.in);
        System.out.println("");
        System.out.println("**** **** Register Patient **** ****");
        System.out.print("Name: ");
        String name = input.nextLine();
        System.out.print("Mobile: ");
        String mobile = input.nextLine();
        System.out.print("Email: ");
        String email = input.nextLine();
        System.out.print("City: ");
        String city = input.nextLine();
        System.out.print("Age: ");
        int age = input.nextInt();
        input.nextLine(); // consume newline
        System.out.print("Medical History: ");
        String history = input.nextLine();

        patients.add(new
         Patient(name, mobile, email, city, age, history));
        System.out.println("Patient registered successfully for the XYZ private limited!");
    }
//register a doctor in xyz private limited
    static void registerDoctor() {
        Scanner input = new Scanner(System.in);
        System.out.println(" ");
        System.out.println("**** **** Register Doctor **** ****");
        System.out.print("Doctor ID: ");
        String id = input.nextLine();
        System.out.print("Name: ");
        String name = input.nextLine();
        System.out.print("Specialization: ");
        String specialization = input.nextLine();
        System.out.print("Available Time Slots (comma-separated): ");
        String[] slots = input.nextLine().split(", ");
        System.out.print("Consultation Fee: ");
        double fee = input.nextDouble();
        input.nextLine();

        doctors.add(new
         Doctor(id, name, specialization, slots, fee));
        System.out.println("Doctor registered successfully for the XYZ private limited!");
    }
// searching the doctor in xyz limited
    static void searchDoctor() {
        System.out.print(" ");
        System.out.print("Enter specialization to search: ");
        System.out.print("Prefered day for visit the chaneling: ");
        String spec = input.nextLine();
        for (Doctor doc : doctors) {
            if (doc.getSpecialization().equalsIgnoreCase(spec)) {
                System.out.println(doc);
            }
        }
    }
//book and appoinment in xyz private limited
    static void bookAppointment() {
        System.out.print(" ");
        System.out.print("Enter patient name: ");
        String patientName = input.nextLine();
        System.out.print("Enter doctor ID: ");
        String docId = input.nextLine();

        Patient foundPatient = null;
        for (Patient p : patients) {
            if (p.getName().equalsIgnoreCase(patientName)) {
                foundPatient = p;
                break;
            }
        }

        Doctor foundDoctor = null;
        for (Doctor d : doctors) {
            if (d.getId().equalsIgnoreCase(docId)) {
                foundDoctor = d;
                break;
            }
        }

        if (foundPatient != null && foundDoctor != null) {
            System.out.print("Enter preferred time slot: ");
            String slot = input.nextLine();

            appointments.add
        (new Appointment(foundPatient, foundDoctor, slot));
            System.out.println("Appointment booked and message sent to patient!");
        } else {
            System.out.println("Patient or Doctor not found.");
        }
    }
//cancel the doctor appoinment
    public static void cancelAppointment() {
        System.out.print("");
        System.out.print("Enter patient name to cancel appointment: ");
        String name = input.nextLine();

        Iterator<Appointment> iter = appointments.iterator();
        while (iter.hasNext()) {
            Appointment a = iter.next();
            if (a.getPatient().getName().equalsIgnoreCase(name)) {
                iter.remove();
                System.out.println("Appointment cancelled. Message sent to patient.");
                if (!waitingList.isEmpty()) {
                    Appointment next = waitingList.poll();
                    appointments.add(next);
                    System.out.println("Next patient in queue notified for slot.");
                }
                return;
            }
        }

        System.out.println("No appointment found for that name.");
    }
//resedule
    static void requestReschedule() {
        System.out.print(" ");
        System.out.print("Enter patient name for rescheduling: ");
        String name = input.nextLine();
        for (Appointment a : appointments) {
            if (a.getPatient().getName().equalsIgnoreCase(name)) {
                waitingList.add(a);
                System.out.println("Patient added to queue for rescheduling.");
                return;
            }
        }
        System.out.println("Appointment not found.");
    }
// display all reservations 
    static void displayAppointments() {
        System.out.println("");
        System.out.println("Scheduled Appointments for the XYZ private limited:");
        for (Appointment a : appointments) {
            System.out.println(a);
        }
    }
}