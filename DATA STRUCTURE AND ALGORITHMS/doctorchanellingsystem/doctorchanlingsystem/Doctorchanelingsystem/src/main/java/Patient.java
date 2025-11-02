package com.mycompany.doctorchanelingsystem;

class Patient 
{
  String name;
  int mobile;
  String email;
  String city;
  int age;
  String medicalHistory;
  patient next;
}
class doctor 
{
  int id ;
  String name;
  String specialization;
  int[] availableSlots;
  double fee = 0;
  doctor next;

}
class appoinment
{
int id ;
int mobile;
int timeSlot;
appoinment next;
}       

import java.util.Scanner;
