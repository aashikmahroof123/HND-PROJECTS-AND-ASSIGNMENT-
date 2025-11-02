package com.mycompany.doctorchannellingsystem;

public class StackApp {

    public static void main(String[] args) {
        PatientStack stack = new PatientStack();

        // Adding sample patients
        stack.push(new Patient("roy", "0771234567", "roy@example.com", "Colombo", 30, "Diabetes"));
        stack.push(new Patient("Aashik", "0772345678", "Aashik@example.com", "Kandy", 29, "Asthma"));
        stack.push(new Patient("nimal", "0773456789", "nimal@example.com", "gampola ", 45, "High BP"));
        stack.push(new Patient("hasir", "0774567890", "hasir@example.com", "batticola", 25, "dengue fever"));
         stack.push(new Patient("hasir", "0774567890", "hasir@example.com", "batticola", 25, "dengue fever"));
          stack.push(new Patient("hasir", "0774567890", "hasir@example.com", "batticola", 25, "dengue fever"));
           stack.push(new Patient("hasir", "0774567890", "hasir@example.com", "batticola", 25, "dengue fever"));
            stack.push(new Patient("hasir", "0774567890", "hasir@example.com", "batticola", 25, "dengue fever"));
             stack.push(new Patient("hasir", "0774567890", "hasir@example.com", "batticola", 25, "dengue fever"));
              stack.push(new Patient("hasir", "0774567890", "hasir@example.com", "batticola", 25, "dengue fever"));
               stack.push(new Patient("hasir", "0774567890", "hasir@example.com", "batticola", 25, "dengue fever"));
                stack.push(new Patient("roy", "0771234567", "roy@example.com", "Colombo", 30, "Diabetes"));
        stack.push(new Patient("Aashik", "0772345678", "Aashik@example.com", "Kandy", 29, "Asthma"));
        stack.push(new Patient("nimal", "0773456789", "nimal@example.com", "gampola ", 45, "High BP"));
         stack.push(new Patient("roy", "0771234567", "roy@example.com", "Colombo", 30, "Diabetes"));
        stack.push(new Patient("Aashik", "0772345678", "Aashik@example.com", "Kandy", 29, "Asthma"));
        stack.push(new Patient("nimal", "0773456789", "nimal@example.com", "gampola ", 45, "High BP"));
 
        // Popping and displaying each patient
        while (!stack.isEmpty()) {
            Patient p = stack.pop();
            System.out.println("Popped Patient: " + p);
        }

        // Check if stack is empty
        if (stack.isEmpty()) {
            System.out.println("*******************************************************");
            System.out.println("The stack is now empty.");
        }
    }
}