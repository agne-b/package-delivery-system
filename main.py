from data_manager import DataManager
from package_factory import PackageFactory

def create_package_interactively():
  print("\n---- Create new package ----")

  while True:
    package_id = input("Enter package ID: ").strip()
    if package_id:
      break
    else:
      print("Package ID cannot be empty")

  while True:
    package_type = input("Enter package type (Standard/Express): ").strip().capitalize()
    if package_type in ["Standard", "Express"]:
      break
    else:
      print("Invalid input! Please enter Standard or Express.")

  while True:
    try:
      weight = float(input("Enter weight: "))
      if weight <= 0:
        print("Weight must be positive")
      else:
        break
    except ValueError:
      print("Invalid input! Please enter a number")
                     
  while True:
    sender = input("Enter sender: ").strip()
    if sender:
      break
    else:
      print("Sender cannot be empty")
      
  while True:
    receiver = input("Enter receiver: ").strip()
    if receiver:
      break
    else:
      print("Receiver cannot be empty")

  package = PackageFactory.create_package(
    package_type, package_id, weight, sender, receiver
  )
  print("Package created successfully")
  return package

def show_packages(packages):
  print("\n---- All packages ----")
  if not packages:
    print("No packages found")
    return
  for p in packages:
    print(
      f"ID:{p.package_id} Type:{p.get_type()} "
      f"Weight:{p.weight} From:{p.sender} To:{p.receiver} "
      f"Status:{p.get_status()} "
    )

def update_status(packages):
  package_id = input("Enter package ID to update status: ")

  for p in packages:
    if p.package_id == package_id:

      while True:
        new_status = input("Enter new status: ").strip()
        
        if new_status in allowed_statuses:
          p.update_status(new_status)
          print("Status updated")
          return
        else:
          print("Invalid status! Try again.")

  print("Package not found")

def main():
  packages = DataManager.load_packages()

  while True:
    print("\n---- PACKAGE DELIVERY SYSTEM ----")
    print("1. Create package")
    print("2. Show packages")
    print("3. Update status")
    print("4. Save and exit")

    choice = input("Choose option: ").strip()

    if choice == "1":
      packages.append(create_package_interactively())

    elif choice == "2":
      show_packages(packages)

    elif choice == "3":
      update_status(packages)

    elif choice == "4":
      DataManager.save_packages(packages)
      print("Saved! Goodbye. ")

    else:
      print("Invalid choice")
if __name__ == "__main__":
  main()
    


  
  
  
    
  
