package com.mycompany.doctorchannellingsystem;

public class PatientStack {
    private PatientNode top;

    public PatientStack() {
        top = null;
    }

    public void push(Patient patient) {
        PatientNode newNode = new PatientNode(patient);
        newNode.next = top;
        top = newNode;
    }

    public Patient pop() {
        if (isEmpty()) {
            System.out.println("No patient in stack!");
            return null;
        }
        Patient popped = top.data;
        top = top.next;
        return popped;
    }

    public boolean isEmpty() {
        return top == null;
    }

    public void displayStack() {
        PatientNode current = top;
        while (current != null) {
            current.displayNode();
            current = current.next;
        }
    }
}//end class