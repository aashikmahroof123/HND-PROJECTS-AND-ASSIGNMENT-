package com.mycompany.doctorchanelingsystem;

public class Appointment {
    private final Patient patient;
    private final Doctor doctor;
    private final String timeSlot;

    public Appointment(Patient patient, Doctor doctor, String timeSlot) {
        this.patient = patient;
        this.doctor = doctor;
        this.timeSlot = timeSlot;
    }

    public Patient getPatient() {
        return patient;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    /**
     *
     * @return
     */
    @Override
    public String toString() {
        return "Appointment -> Patient: " + patient.getName() + ", Doctor: " + doctor.getId() + ", Slot: " + timeSlot;
    }
}