# Create a class named Mobile with attributes ModelName,Company,Price and with methods:
# set_attributes, print_details and can_afford

class Mobile:
    def set_attributes(self, model_name, company, price):
        setattr(self, 'ModelName', model_name)
        setattr(self, 'Company', company)
        setattr(self, 'Price', price)

    def can_afford(self):
        if getattr(self, 'Price') < 30000:
            print(f"{getattr(self, 'Company')} {getattr(self, 'ModelName')} is affordable")
        else:
            print(f"{getattr(self, 'Company')} {getattr(self, 'ModelName')} is not affordable")

    def print_details(self):
        print(f"Model: {getattr(self, 'ModelName')}")
        print(f"Company: {getattr(self, 'Company')}")
        print(f"Price: {getattr(self, 'Price')}")


m = Mobile()
m.set_attributes('Nord', 'onePlus', 27999)
m.print_details()
m.can_afford()
