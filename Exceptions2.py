class MyException(Exception):
    pass


class ExceptionsDemo:

    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
        except (ZeroDivisionError, TypeError) as error:
            print(f"{type(error).__name__} detected")

    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
        except (IndexError, TypeError) as error:
            print(f"{type(error).__name__} Detected")

    def access_dict(self, dic, key):
        try:
            print("Value:", dic[key])
        except (KeyError, TypeError) as error:
            print(f"{type(error).__name__} detected")

    def read_file(self, filename):
        try:
            with open(filename, "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("FileNotFoundError detected")

    def access_attribute(self, obj):
        try:
            print(obj.tnonexistent_attribue)
        except AttributeError:
            print("AttributeError detected")

    def check_positive(self, number):
        try:
            if number < 0:
                raise MyException("The number must be positive.")
            print("Valid number:", number)
        except MyException as error:
            print(f"MyException Detected: {error}")


if __name__ == "__main__":
    demo = ExceptionsDemo()

    demo.divide(10, 0)
    demo.divide("10", 2)

    demo.access_list([1, 2, 3], 5)
    demo.access_list(1, 0)

    demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")
    demo.access_dict("not_a_dict", "b")

    demo.read_file("text_2.txt")
    demo.read_file("text.txt")

    demo.access_attribute(object())
    demo.check_positive(-5)
