import java.util.*;

public class DoctorChannellingSystem {
    static Scanner input = new Scanner(System.in);
    public static List<Doctor> doctors = new ArrayList<>();

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n--- Doctor Channeling System ---");
            System.out.println("1. Register Doctor");
            System.out.println("2. View Doctors");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
      String choice = input.nextLine();
            switch (choice) {
                case "1":
                    registerDoctor();
                    break;
                case "2":
                    viewDoctors();
                    break;
                case "3":
                    System.out.println("Exiting system...");
                    return;
                default:
                    System.out.println("❌ Invalid choice.");
            }
      
        }
    }

    public static void registerDoctor() {
        try {
            System.out.print("Enter Doctor ID: ");
            String id = input.nextLine();
            if (id.isEmpty()) throw new IllegalArgumentException("Doctor ID cannot be empty.");

            System.out.print("Enter Doctor Name: ");
            String name = input.nextLine();
            if (name.isEmpty()) throw new IllegalArgumentException("Doctor name cannot be empty.");

            System.out.print("Enter Specialization: ");
            String specialization = input.nextLine();
            if (specialization.isEmpty()) throw new IllegalArgumentException("Specialization cannot be empty.");

            System.out.print("Enter Available Time Slot: ");
            String timeSlot = input.nextLine();

            System.out.print("Enter Consultation Fee: ");
            double fee = input.nextDouble();
            input.nextLine(); // Clear the newline
            if (fee < 0) throw new IllegalArgumentException("Consultation fee cannot be negative.");

            doctors.add(new Doctor(id, name, specialization, timeSlot, fee));
            System.out.println("✅ Doctor registered successfully.");

        } catch (InputMismatchException e) {
            System.out.println("❌ Invalid input. Please enter numeric value for fee.");
            input.nextLine(); // clear buffer
        } catch (IllegalArgumentException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (Exception e) {
            System.out.println("❌ Unexpected error: " + e.getMessage());
        }
    }

    public static void viewDoctors() {
        if (doctors.isEmpty()) {
            System.out.println("No doctors registered yet.");
        } else {
            System.out.println("\n--- Registered Doctors ---");
            for (Doctor doc : doctors) {
                System.out.println(doc);
            }
        }
    }
}
