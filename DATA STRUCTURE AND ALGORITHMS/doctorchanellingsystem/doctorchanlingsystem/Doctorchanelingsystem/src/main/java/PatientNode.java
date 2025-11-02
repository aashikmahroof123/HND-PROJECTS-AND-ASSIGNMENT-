package com.mycompany.doctorchannellingsystem;

public class PatientNode {//node.java
    Patient data;//data part
    PatientNode next;//pointer

    public PatientNode(Patient data) {//constructor method
        this.data = data;
        this.next = null;
    }

    public void displayNode() {//
        System.out.println(data.toString());
    }
}