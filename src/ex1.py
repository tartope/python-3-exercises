from ValidationException import ValidationException


def validate_file(file_name):
    with open(file_name, "r") as file:
        next(file)
        # for count, line in enumerate(file):
        #     line_values = line.split(',')
        #     # print(line_values)
        #     # if second value is number -> throw exceptions
        #     try:
        #         int(line_values[1])
        #     except:
        #         raise ValidationException(f"Invalid mileage: {line_values[1]}")

        for line in file:
            try:
                int(line[3:])
            except:
                raise ValidationException(f"Invalid mileage: {line[3:]}")



def ex1():
    try:
        validate_file("../files/input.txt")
    except ValidationException as ve:
        print(ve)

ex1()

# Comment