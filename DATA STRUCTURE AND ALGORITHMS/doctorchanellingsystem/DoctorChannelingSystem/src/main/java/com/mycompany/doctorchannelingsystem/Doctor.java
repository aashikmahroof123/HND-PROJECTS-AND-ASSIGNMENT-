public class Doctor {
    private String id, name, specialization, timeSlot;
    private double fee;

    public Doctor(String id, String name, String specialization, String timeSlot, double fee) {
        this.id = id;
        this.name = name;
        this.specialization = specialization;
        this.timeSlot = timeSlot;
        this.fee = fee;
    }

    @Override
    public String toString() {
        return id + " | " + name + " | " + specialization + " | " + timeSlot + " | " + fee;
    }

    // Getters and setters (optional if needed)
}
