package com.mycompany.doctorchanelingsystem;

/**
 *
 * @author user
 */
public class Doctor_1 {

    public Doctor_1() {
        this.specialization = specialization;
        this.name = null;
    }
    private final String id = null;
    private final String name;
    private final String specialization;
    private final String[] availableSlots = null;
    private final double fee = 0;

    public Doctor_1tring id, String name, String specialization, String[] availableSlots, double fee) {
        this.id = id;
        this.name = name;
        this.specialization = specialization;
        this.availableSlots = availableSlots;
        this.fee = fee;
    }

    public String getId() {
        return id;
    }

    public String getSpecialization() {
        return specialization;
    }

    public String[] getAvailableSlots() {
        return availableSlots;
    }

    /**
     *
     * @return
     */
    @Override
    public String toString() {
        StringBuilder slots = new StringBuilder();
        for (String slot : availableSlots) {
            slots.append(slot).append(" ");
        }
        return "Doctor ID: " + id + ", Name: " + name + ", Specialization: " + specialization + 
               ", Fee: " + fee + ", Slots: " + slots;
    }
}