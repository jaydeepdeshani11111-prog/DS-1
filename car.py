import pandas as pd

data = {
    "Car ID": [1, 2, 3, 4, 5],
    "Brand": ["Toyota", "ford", "Hyundai", "Tata", "Mahindra"],
    "Model": ["Innova", "Endeavour", "i20", "Nexon", "XUV700"],
    "Price": [2500000, 1500000, 1000000, 1200000, 2300000],
    "Fuel Type": ["Diesel", "Petrol", "Petrol", "Diesel", "Diesel"],
    "Mileage": [12, 17, 20, 18, 15]
}

cars = pd.DataFrame(data)
 
print("Car Details Dataset:")
print(cars)


print("\nSpecific Information (Brand and Price):")
print(cars[["Brand", "Price"]])


print("\nCars with Price > 1,500,000:")
print(cars[cars["Price"] > 1500000])


print("\nDiesel Cars:")
print(cars[cars["Fuel Type"] == "Diesel"])