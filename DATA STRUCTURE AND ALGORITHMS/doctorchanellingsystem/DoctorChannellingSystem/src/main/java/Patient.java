package com.mycompany.doctorchannellingsystem;

 class Patient 
 {
    String name;
    String mobile;
    String email;
    String city;
    int age;
    String medicalhistory;
    Patient next;

  public   Patient(String name, String mobile, String email, String city, int age, String history) {
        this.name = name;
        this.mobile = mobile;
        this.email = email;
        this.city = city;
        this.age = age;
        this.medicalhistory = medicalhistory;
    }

   public  String getName() {
        return name;
    }

    public String toString() {
        return "Name: " + name + ", Mobile: " + mobile + ", Email: " + email + ", City: " + city + ", Age: " + age + ",medicalHistory: " + medicalhistory;
    }
}