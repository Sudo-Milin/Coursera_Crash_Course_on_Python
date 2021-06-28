### Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.

# Function defined
def car_listing(car_prices):
  # An empty result variable is created inorder to store detail for cars.
  result = ""
  # Now the keys-values from dictionary is iterated and each key-value for every iteration is stored in result variable in a well formatted way.
  for model, cost in car_prices.items():
    # items() method is used in order to iterate over two variables i.e. key and value in dictionary.
    result += "{} costs {} dollars".format(model, cost) + "\n"
  # Finally result variable is returned.
  return result

# Function call
print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
