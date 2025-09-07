car1 = {"name":"Harrier", "type":"EV Car", "brand":"TATA"}
car2 = {"name":"Venue", "type":"Petrol Car", "brand":"Hyundai"}
car3 = {"name":"Wagon R", "type":"Petrol Car", "brand":"Maruti Suzuki"}

cars = {
    "car1": car1,
    "car2": car2,
    "car3": car3
}

#access nested dictionary
for key, value in cars.items():
    print("\n"+key+":"+ str(value))

    for x, obj in value.items():
        print(x + ":" + str(obj))