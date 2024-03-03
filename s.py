class CustomerInfo:
  def __init__(self, customer_info):
      self.customer_info = customer_info

class Items:
  def __init__(self, items):
      self.items = items

class ShippingAddress:
  def __init__(self, shipping_address):
      self.shipping_address = shipping_address

class OrderCost:
  def __init__(self, total_cost):
      self.total_cost = total_cost

class OrderValidator:
  def validate_order(self, items, customer_address):
    print("Validating order data: checking item availability and customer address validity")
class EmailSender:
  def send_order_confirmation_email(self, customer_email):
    print("Sending order confirmation email to customer")
class InventoryUpdater:
  def update_inventory(self, items):
    print("Updating inventory levels after order processing")

#This WAP follows SRP by seperating every responsibility into its own class
#The code would be very readable since everything is seperated and independent, which 
#allows for  each class to be individually understood and analyzed.
#It is reuseable because none of the functions rely on eachother.
#None of the functions have to depend on eachother. It would interfere with the single 
#responsibility part of the SRP. 
#
def main():
  # Creating some random sample info for you
  customer_info = CustomerInfo("John Doe")
  items = Items(["Item1", "Item2"])
  shipping_address = ShippingAddress("123 Main Street")
  order_cost = OrderCost(100)

  # Validating order
  order_validator = OrderValidator()
  order_validator.validate_order(items.items, shipping_address.shipping_address)

  # Sending the email
  email_sender = EmailSender()
  email_sender.send_order_confirmation_email("john.doe@example.com")

  # Updating the inventory
  inventory_updater = InventoryUpdater()
  inventory_updater.update_inventory(items.items)
if __name__ == "__main__":
  main()