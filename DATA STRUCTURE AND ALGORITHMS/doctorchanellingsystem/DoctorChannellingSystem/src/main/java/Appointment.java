package com.mycompany.doctorchannellingsystem;

 class Appointment {
    Patient patient;
    Doctor doctor;
    String timeSlot;
    Appointment next;
    
    public Appointment(Patient patient, Doctor doctor, String timeSlot) {
        this.patient = patient;
        this.doctor = doctor;
        this.timeSlot = timeSlot;
    }

    public Patient getPatient() {
        return patient;
    }

    public String toString() {
        return "Patient: " + patient.getName() + ", Doctor: " + doctor.toString() + ", Slot: " + timeSlot;
    }
}