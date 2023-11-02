# EmployeeHub
This is an Open-source python project using Tkinter as frontend and MySQL as backend.



FOR BACKEND:


STEP 1:Open MySQL Workbench create new database named it as employee_management_system.

STEP 2:Create new table named it emp.

STEP 3: Write below query in the script-

CREATE TABLE `employee_management_system`.`emp` (

   `Department` VARCHAR(45) NULL,
   
   `Nme` VARCHAR(45) NULL,
   
   `DesIgnition` VARCHAR(45) NULL,
   
   `Email` VARCHAR(45) NULL,
   
   `Address` VARCHAR(45) NULL,
   
   `Married_status` VARCHAR(45) NULL,
   
   `DOB` VARCHAR(45) NULL,
   
   `DOJ` VARCHAR(45) NULL,
   
   `Gender` VARCHAR(45) NULL,
   
   `ID_proof_type` VARCHAR(45) NULL,
   
   `ID_proof` VARCHAR(45) NOT NULL,
   
   `Phone` VARCHAR(45) NULL,
   
   `Country` VARCHAR(45) NULL,
   
   `Salary` VARCHAR(45) NULL,
   
   PRIMARY KEY (`ID_proof`)
);



RESULT SCREENSHOT:

![image](https://github.com/vivek030502/EmployeeHub/assets/110586449/213beb5c-6d74-4726-bce3-d39d53de92f9)


![image](https://github.com/vivek030502/EmployeeHub/assets/110586449/a965be36-b428-42ec-a9eb-ffcdf258e70c)
