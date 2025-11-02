package com.mycompany.doctorchannellingsystem;

public class Patient 
 {
  private  String name;
  private  String mobile;
  private  String email;
  private  String city;
  private  int age;
  private  String medicalhistory;
    

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

    public void setName(String name) {
        this.name = name;
    }

    public String getMobile() {
        return mobile;
    }

    public void setMobile(String mobile) {
        this.mobile = mobile;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getMedicalHistory() {
        return medicalHistory;
    }

    public void setMedicalHistory(String medicalHistory) {
        this.medicalHistory = medicalHistory;
    }

  