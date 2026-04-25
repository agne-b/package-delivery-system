# Package Delivery System – Coursework Report

---

## 1. Introduction

### Goal of the coursework

The goal of this coursework is to design and implement an **object-oriented Package Delivery System** using Python.  
The program allows users to create, store, manage, and update delivery packages through a console interface.

The system demonstrates:

- Object-oriented programming (OOP)
- Abstract classes and inheritance
- Data validation and error handling
- File persistence (saving/loading data)

---

### What is the application?

The application is a **console-based logistics management system** that simulates package handling operations in a delivery company environment.

Users can:

- Create Standard or Express packages
- Enter sender and receiver addresses
- View all stored packages
- Update delivery status
- Save and load data from file

---

### How to run the program

1. Open the project folder
2. Make sure all Python files are in the same directory
3. Run the main program:

```bash
python main.py
```

### How to use the program

After running, a menu appears:

1. Create package
2. Show packages
3. Update status
4. Save and exit

### User workflow

- Create packages by entering required data  
- View saved packages  
- Update package delivery status  
- Save and exit the system

All inputs are validated to prevent crashes.

---

## 2. Body / Analysis

This section explains how the system is designed and how it meets the coursework requirements.

The application is built using **object-oriented programming (OOP)** principles in Python. The system is structured into multiple classes that work together to simulate a package delivery system.

---

## UML Class Overview

![UML Diagram](uml.png)

The system consists of the following main classes:

- Package (abstract class)
- StandardPackage
- ExpressPackage
- Address
- PackageFactory
- DataManager

These classes work together to create, manage, and store delivery packages.

---

## 2. Body / Analysis

This section explains the design and implementation of the Package Delivery System and how it satisfies the required functional and object-oriented programming principles.

The system is built using **object-oriented programming (OOP)** and is structured into multiple interacting classes. Each class is responsible for a specific part of the system, which ensures modularity, readability, and maintainability.

---

### 2.1 Overall System Design

The application follows a layered class structure where different responsibilities are separated:

- Core domain classes (Package, Address)
- Specialized package types (StandardPackage, ExpressPackage)
- System logic (DeliveryService / DataManager / PackageFactory)

This separation allows the system to simulate real-world logistics behavior in a simplified but structured way.

The UML diagram illustrates the relationships between these classes.

---

### 2.2 Abstraction

Abstraction is used to define a general structure for all packages without exposing implementation details.

The `Package` class acts as an abstract base class that defines shared attributes and methods for all package types.

---

#### Example:

```python
from abc import ABC, abstractmethod

class Package(ABC):
    def __init__(self, package_id, weight, sender, receiver):
        self._package_id = package_id
        self._weight = weight
        self._sender = sender
        self._receiver = receiver
        self._status = "Created"

    @abstractmethod
    def calculate_cost(self):
        pass
```

---

### Explanation:

- The `Package` class is marked as abstract using `ABC`
- It cannot be instantiated directly
- It defines common attributes (`package_id`, `weight`, `sender`, `receiver`) shared by all packages
- The method `calculate_cost()` is declared but not implemented
- This forces all subclasses to provide their own implementation
- It ensures a consistent structure across all package types

---

### 2.3 Inheritance

Inheritance is another key object-oriented programming principle used in this system. It allows new classes to reuse existing code from a parent class while also extending or modifying its behavior.

In this project, inheritance is implemented by creating specific package types (`StandardPackage`, `ExpressPackage`) that inherit from the base `Package` class.

---

### Example:

```python
class StandardPackage(Package):
class ExpressPackage(Package):
```

---

### Explanation:

- The `StandardPackage` and `ExpressPackage` classes inherit from the `Package` base class  
- They reuse shared attributes such as `package_id`, `weight`, `sender` and `receiver`

---

### 2.4 Polymorphism

Polymorphism is an object-oriented programming principle that allows different classes to be treated through a common interface while each class can behave differently based on its implementation.

In this system, polymorphism is mainly demonstrated through the `calculate_cost()` method, which is shared across different package types but produces different results depending on the object.

---

### Example:

```python
class StandardPackage(Package):
    def calculate_cost(self):
        return round(self._base_rate * self._weight, 2)


class ExpressPackage(Package):
    def calculate_cost(self):
        return round(self._base_rate * self._weight + self._express_fee, 2)
```

---

### Explanation:

- The same method call `calculate_cost()` is used for different package objects  
- The `StandardPackage` and `ExpressPackage` classes provide their own implementations of this method  
- The correct version of the method is chosen at runtime depending on the object type  
- This allows one function to work with multiple types of packages  
- The system does not need to know the exact class of the object in advance

---

### 2.5 Composition

Composition is an object-oriented programming principle where one class is made up of one or more objects from other classes. It represents a strong “has-a” relationship, meaning that a class contains other objects as part of its structure.

In this system, composition is used to build a `Package` using `Address` objects for both sender and receiver information.

---

### Example:

```python
from address import Address

class Package(ABC):
    def __init__(self, package_id, weight, sender, receiver):
        self._package_id = package_id
        self._weight = weight
        self._sender = sender
        self._receiver = receiver
```

---

### Explanation:

- The `Package` class contains `sender` and `receiver` attributes  
- Both `sender` and `receiver` are instances of the `Address` class  
- These `Address` objects are created outside the `Package` class and passed in as parameters  
- The `Package` class stores and uses these objects as part of its structure  
- This is a clear example of composition because the package is made up of address objects

---

### 2.6 Aggregation

Aggregation is an object-oriented programming principle where one class contains references to objects of another class, but those objects can exist independently of the container class. It represents a weak “has-a” relationship.

In this system, aggregation is used in the part of the program that manages multiple `Package` objects (for example, a manager or system class that stores packages in a list).

---

### Example:

```python
class DataManager:
    @staticmethod
    def load_packages():
        packages = []
class DeliveryService:
    def __init__(self):
        self._couriers = []
        self._packages = DataManager.load_packages()
```

---

### Explanation:

- The `DeliveryService` class stores a list of couriers and packages  
- The `_packages` attribute is initialized using `DataManager.load_packages()`  
- The `DataManager` class is responsible for loading package data from a file  
- The `DeliveryService` does not create `Package` objects itself  
- Instead, it receives already created `Package` objects from `DataManager`  
- These `Package` objects exist independently of the `DeliveryService` class  
- The service class only keeps references to them and uses them when needed

---

### 2.7 Data Persistence

Data persistence is the ability of a program to save data permanently so that it can be reused after the program is closed and restarted. In this system, data persistence is implemented using CSV file handling in the `DataManager` class.

The system saves all package information into a file and later reloads it to restore the previous state of the application.

---

### Example:

```python
import csv

class DataManager:
    FILE_NAME = "packages.csv"

    @staticmethod
    def save_packages(packages):
        file = open(DataManager.FILE_NAME, "w", newline="")
        writer = csv.writer(file)

        writer.writerow(["id", "type", "weight", "sender", "receiver", "status"])

        for p in packages:
            writer.writerow([
                p.package_id,
                p.get_type(),
                p.weight,
                p.sender.get_full_address(),
                p.receiver.get_full_address(),
                p.get_status()
            ])

        file.close()
```

---

### Explanation:

- The `save_packages()` method writes package data into a CSV file  
- Each package object is converted into a row of structured text data  
- Important attributes such as `package_id`, `type`, `weight`, `sender`, `receiver`, and `status` are stored  
- The file is opened in write mode, meaning old data is replaced with new data  
- This ensures the file always contains the latest version of the system data

---

### 2.8 Encapsulation

Encapsulation is an object-oriented programming principle that restricts direct access to an object’s internal data and ensures that data is only accessed or modified through controlled methods.

In this system, encapsulation is implemented by using private attributes (prefixed with `_`) and providing public methods or properties to access and modify them safely.

---

### Example:

```python
class Package(ABC):

    def __init__(self, package_id, weight, sender, receiver):
        self._package_id = package_id
        self._weight = weight
        self._sender = sender
        self._receiver = receiver
        self._status = "Created"

    @property
    def package_id(self):
        return self._package_id

    @property
    def weight(self):
        return self._weight

    def get_status(self):
        return self._status

    def update_status(self, new_status):
        if self._status == "Delivered":
            raise ValueError("Cannot change delivered package")

        self._status = new_status
```

---

### Explanation:

- Class attributes are marked as private using `_` (e.g. `_package_id`, `_weight`, `_status`)  
- Direct access to internal variables is restricted from outside the class  
- Data is accessed through controlled methods such as getters (`@property`)  
- The `update_status()` method controls how the package status can be changed  
- Validation logic is applied inside methods to protect data integrity  
- This ensures that the object’s state cannot be changed in an unsafe way

---

### 2.9 Factory Method (Design Pattern)

The Factory Method is a creational design pattern used to create objects without exposing the exact instantiation logic to the user. Instead of creating objects directly, a separate factory class is responsible for deciding which class to instantiate.

In this system, the `PackageFactory` class is used to create different types of packages based on the provided input.

---

### Example:

```python
class PackageFactory:
    @staticmethod
    def create_package(package_type, package_id, weight, sender, receiver):
        if package_type == "Standard":
            return StandardPackage(package_id, weight, sender, receiver)
        elif package_type == "Express":
            return ExpressPackage(package_id, weight, sender, receiver)
        else:
            raise ValueError("Unknown package type")
```

---

### Usage in DeliveryService:

```python
package = PackageFactory.create_package(
    package_type,
    package_id,
    weight,
    sender,
    receiver
)
```

---


### Explanation:

- The `PackageFactory` class is responsible for creating package objects  
- It decides which class to instantiate based on `package_type` (`Standard` or `Express`)  
- The `DeliveryService` class does not create package objects directly  
- Instead, it calls the factory method to handle object creation  
- This centralises and hides the object creation logic inside one class  
- It makes the system easier to extend and maintain

---

## 3. Results and Summary

- The application successfully implements a functional package delivery system using object-oriented programming principles.  
- All core features work as expected, including package creation, status updates, and data persistence using CSV files.  
- The system demonstrates proper use of OOP concepts such as inheritance, polymorphism, abstraction, encapsulation, composition, and aggregation.  
- One of the main challenges was designing a clean class structure that separates responsibilities between different components.  
- Another challenge was ensuring proper validation of input data to prevent invalid package creation and runtime errors.

---

## 4. Conclusions

This coursework project successfully implemented a **Package Delivery System** using object-oriented programming principles in Python.

The final system demonstrates a clear and structured design that models real-world logistics operations. It supports creating and managing different types of packages, tracking their status, and storing data persistently using file handling.

The main achievement of this work is the correct application of OOP concepts, including inheritance, polymorphism, abstraction, encapsulation, composition, and aggregation. These principles helped to create a modular, reusable, and maintainable system.

In terms of future improvements, the system could be extended by adding a graphical user interface (GUI), integrating a database instead of CSV files, or implementing real-time tracking features for deliveries. These enhancements would make the application more realistic and closer to a production-level system.

---

## 5. Resources and References

- Python Official Documentation  
  https://docs.python.org/3/

- Python `abc` module (Abstract Base Classes)  
  https://docs.python.org/3/library/abc.html

- Python `csv` module documentation  
  https://docs.python.org/3/library/csv.html

- Factory Method Design Pattern  
  https://refactoring.guru/design-patterns/factory-method

- Course materials / lecture notes provided during the module 



