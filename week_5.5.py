class ValidateAge(Exception):
    def __init__(self, message: object) -> None:
        self.message = message
def validate_age(age):
    if age < 0:
        raise ValidateAge("Entered Age is Negative")
    elif age > 200:
        raise ValidateAge("Entered age is very High")
    else:
        print("Age is valid")
try:
    age = int(input("Enter your age : "))
    validate_age(age)
except ValidateAge as e:
    print(f"{e}")



