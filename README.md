# Iterative Drying Oil Mass Balance Process Plant for Exercise I

This program uses two class types chemical, stream, and feeds them into different unit operations which manipulate them as per the exercise brief. The returned stream is assigned a new number, but mass is conserved throughout the system. This way of doing things means that there can be error checks implemented into update functions within the stream so that debugging is easy if values do happen to stray from the norm.
# Introduction
This repository has the files necessary for running the CET I process calculation exercise simulator for the castor oil drying facility. It is coded in a way such that things may be changed in order to swap the amount of production or conversion rates by simply inspecting the plant / changing the temp:conversion,select dict.

# Main Method
Main method is responsible for collating functions and returning the optimal working conditions for each of the values within the two reactor dictionaries. The master list is an arr of [(profit, operating, materials, dca_tonnage), large_reactor, temperature]. It is a little confusing, but I found this to be the easiest way to extract all of the information from the process plant in a concise manner. It also allows back-searches of optimal data to understand everything about that particular operation.

The main method can be altered in order to print out information about different streams as you wish, the program is written in such a manner that you are able to change the main method relatively easily without the danger of affecting the core function of the program.

# Functions
The functions folder contains all of the "unit operations" necessary for the main method to run, including the plant.py file which collates all of the existing functions beside opex into one iterative plant. The plant iterates 1000 times by default, and testing has found this to be more than suitable to reach a steady state -- however it can be modified should you want to.

# Classes
The classes folder contains the two classes that are at the heart of this program -- stream & chemical. The chemical class allows for storage of information relating to each chemical used within the plant, and allows easy interconversion between moles and mass. The stream class stores the molflow and massflow of each of the pipes in the PFD -- but there are important things to note. The core principle of this program is based on conservation of atoms, rather than mass in kg -- and hence the massflow() function needs to be called in order to update the stream before the outputs in terms of mass flow are accurate. 

# PFD and Context
Below you can find the PFD used to create this exercise, along with some of the appendix data used in order to achieve mass balance and calculate the different fractional splitting within the unit operations. If you have any questions or find any issues or have any suggested improvements please contac me via email on [css47 @ cam . ac . uk]

![pfd](https://i.imgur.com/7Df4cK2.png)

![reactor data](https://i.imgur.com/Quco6lv.png)

![separator/financial data](https://i.imgur.com/tSjVdls.png)

These images are courtesy of:

CET Part I Exercise Sheet 1. Process Calculations. Drying Oil Exercise. KY \& MT. University of Cambridge, 2022.