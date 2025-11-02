package com.mycompany.doctorchannellingsystem;

 class Doctor {
     String id;
     String name;
     String specialization;
     String[] slots;
     double fee;
     Doctor next;

    public Doctor(String id, String name, String specialization, String[] slots, double fee) {
        this.id = id;
        this.name = name;
        this.specialization = specialization;
        this.slots = slots;
        this.fee = fee;
    }

    public String getId() {
        return id;
    }

    public String getSpecialization() {
        return specialization;
    }

    public String toString() {
        return "Doctor ID: " + id + ", Name: " + name + ", Specialization: " + specialization + ", Fee: " + fee;
    }
}
