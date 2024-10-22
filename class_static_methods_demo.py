class Calculator:
  """
  A class for performing basic arithmetic operations.
  """
  calculation_type = "Arithmetic Operations"  # Class attribute

  @staticmethod
  def add(a, b):
    """
    Static method to add two numbers.

    Args:
      a (int): First number.
      b (int): Second number.

    Returns:
      int: The sum of a and b.
    """
    return a + b

  @classmethod
  def multiply(cls, a, b):
    """
    Class method to multiply two numbers.

    Args:
      cls (class): The Calculator class itself.
      a (int): First number.
      b (int): Second number.

    Returns:
      int: The product of a and b.
    """
    print(f"Calculation type: {cls.calculation_type}")
    return a * b


from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()