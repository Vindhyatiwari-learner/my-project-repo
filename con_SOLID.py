# single responsibility principle

class AccountDB:
   """Account DB management class """

   def get_account_number(self, _id):
       """Get account number"""
       pass

   def account_save(self, obj):
       """Save account number into DB"""
       pass


class Account:
   """Demo bank account class """

   def __init__(self, account_no: str):
       self.account_no = account_no
       self._db = AccountDB()

   def get_account_number(self):
       """Get account number"""
       return self.account_no

   def get(self, _id):
       """
       :param _id:
       :return:
       """
       return self._db.get_account_number(_id=_id)

   def save(self):
       """account save"""
       self._db.account_save(obj=self)

# Open and closed principle

class Discount:
   """Demo customer discount class"""
   def __init__(self, customer, price):
       self.customer = customer
       self.price = price
   def get_discount(self):
       """A discount method"""
       return self.price * 0.2
class VIPDiscount(Discount):
   """Demo VIP customer discount class"""
   def get_discount(self):
       """A discount method"""
       return super().get_discount() * 2
class SuperVIPDiscount(VIPDiscount):
   """Demo super vip customer discount class"""
   def get_discount(self):
       """A discount method"""
       return super().get_discount() * 2

# Liskov Substitution principle

class Vehicle:
   """A demo Vehicle class"""
   def __init__(self, name: str, speed: float):
       self.name = name
       self.speed = speed
   def get_name(self) -> str:
       """Get vehicle name"""
       return f"The vehicle name {self.name}"
   def get_speed(self) -> str:
       """Get vehicle speed"""
       return f"The vehicle speed {self.speed}"
class VehicleWithoutEngine(Vehicle):
   """A demo Vehicle without engine class"""
   def start_moving(self):
      """Moving"""
      raise NotImplemented
class VehicleWithEngine(Vehicle):
   """A demo Vehicle engine class"""
   def engine(self):
      """A vehicle engine"""
      pass
   def start_engine(self):
      """A vehicle engine start"""
      self.engine()
class Car(VehicleWithEngine):
   """A demo Car Vehicle class"""
   def start_engine(self):
       pass
class Bicycle(VehicleWithoutEngine):
   """A demo Bicycle Vehicle class"""
   def start_moving(self):
       pass

# Interface Segregation Principle

class Shape:
   """A demo shape class"""
   def draw(self):
      """Draw a shape"""
      raise NotImplemented
class Circle(Shape):
   """A demo circle class"""
   def draw(self):
      """Draw a circle"""
      pass
class Square(Shape):
   """A demo square class"""
   def draw(self):
      """Draw a square"""
      pass

# Dependency Inversion Principle

class BackendDeveloper:
   """This is a low-level module"""
   def develop(self):
       self.__python_code()
   @staticmethod
   def __python_code():
       print("Writing Python code")
class FrontendDeveloper:
   """This is a low-level module"""
   def develop(self):
       self.__javascript()
   @staticmethod
   def __javascript():
       print("Writing JavaScript code")
class Developers:
   """An Abstract module"""
   def __init__(self):
       self.backend = BackendDeveloper()
       self.frontend = FrontendDeveloper()
   def develop(self):
       self.backend.develop()
       self.frontend.develop()
class Project:
   """This is a high-level module"""
   def __init__(self):
       self.__developers = Developers()
   def develops(self):
       return self.__developers.develop()
project = Project()
print(project.develops())

