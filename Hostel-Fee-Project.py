class College:
    def __init__(self):
        self.base_fee = 200000

    def calculate_stream_fee(self, stream):
        if stream.lower() == "y":
            return self.base_fee * 0.10
        return 0

    def calculate_hostel_fee(self, hostel):
        if hostel.lower() == "y":
            return 200000
        return 0

    def calculate_food_fee(self, months):
        return months * 2000

    def calculate_transport_fee(self, transport_type):
        if transport_type.lower() == "semester":
            return 13000 * 2
        elif transport_type.lower() == "annual":
            return 13000 * 4
        else:
            raise ValueError("Invalid transportation option")


class Course(College):   # Inheritance
    def __init__(self):
        super().__init__()
        self.course_list = ["HR", "Finance", "Marketing"]

    def calculate_total_fee(self):
        try:
            print("Select course from list:")
            for course in self.course_list:
                print(course)

            course_name = input("Enter course name: ").strip()

            if course_name.lower() not in [c.lower() for c in self.course_list]:
                raise ValueError("Invalid course name")


            stream = input("You want analytical stream (Y/N): ")
            hostel = input("You want hostel facility (Y/N): ")
            food_months = int(input("Enter number of months for food: "))
            transport = input("Enter transportation type (semester/annual): ")

            total_fee = self.base_fee

            total_fee += self.calculate_stream_fee(stream)
            total_fee += self.calculate_hostel_fee(hostel)
            total_fee += self.calculate_food_fee(food_months)
            total_fee += self.calculate_transport_fee(transport)

            print("Total annual cost is:", total_fee)

        except ValueError as ve:
            print("Input Error:", ve)

        except Exception as e:
            print("Something went wrong:", e)


# Object creation
obj = Course()
obj.calculate_total_fee()
