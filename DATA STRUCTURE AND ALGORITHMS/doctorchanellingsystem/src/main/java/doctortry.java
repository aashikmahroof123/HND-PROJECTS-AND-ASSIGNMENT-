// List to store registered doctors
public static List<Doctor> doctors = new ArrayList<>();

public static void registerDoctor() {
    try {
        // Doctor ID input and validation
        System.out.print("Enter Doctor ID: ");
        String id = input.nextLine();
        if (id.isEmpty()) {
            throw new IllegalArgumentException("Doctor ID cannot be empty.");
        }

        // Doctor name input and validation
        System.out.print("Enter Doctor Name: ");
        String name = input.nextLine();
        if (name.isEmpty()) {
            throw new IllegalArgumentException("Doctor name cannot be empty.");
        }

        // Specialization input and validation
        System.out.print("Enter Specialization: ");
        String specialization = input.nextLine();
        if (specialization.isEmpty()) {
            throw new IllegalArgumentException("Specialization cannot be empty.");
        }

        // Time slot input
        System.out.print("Enter Available Time Slot: ");
        String timeSlot = input.nextLine();

        // Consultation fee input and validation
        System.out.print("Enter Consultation Fee: ");
        double fee = input.nextDouble();
        input.nextLine(); // Consume the newline character
        if (fee < 0) {
            throw new IllegalArgumentException("Consultation fee cannot be negative.");
        }

        // Add doctor to the list
        doctors.add(new Doctor(id, name, specialization, timeSlot, fee));
        System.out.println("✅ Doctor registered successfully.");

    } catch (InputMismatchException e) {
        System.out.println("❌ Invalid input. Please enter correct numeric values.");
        input.nextLine(); // clear the buffer
    } catch (IllegalArgumentException e) {
        System.out.println("❌ " + e.getMessage());
    } catch (Exception e) {
        System.out.println("❌ Unexpected error: " + e.getMessage());
    }
}

