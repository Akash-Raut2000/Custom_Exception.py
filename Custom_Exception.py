# Define a custom exception
class MyCustomError(Exception):
    pass

# Example usage
try:
    raise MyCustomError("This is a custom error message!")
except MyCustomError as e:
    print(f"Caught an exception: {e}")
