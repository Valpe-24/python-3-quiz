from ValidationException import ValidationException

def validate_file(file_path):
    numbers = '0123456789'
    lines = []
    with open(file_path, "r") as file1:
        while True:
            line = file1.readline().split()

            if not line:
                break
            lines.append(line)

    for i in range(len(lines)):
        for letters in lines[i][0]:
            if letters in numbers:
                raise ValidationException(f"Invalid first name: {lines[i][0]}")

def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)


test()
