import json


class Cars:
    def __init__(self, name, color, price, **kwargs):
        self.name = name
        self.color = color
        self.price = price
        self.__dict__.update(**kwargs)

    def add_data(self):
        with open('Car_data.json') as file:
            data_to_add = json.load(file)
        data_to_add.append({
            'name': f'{self.name}',
            'color': f'{self.color}',
            'price': f'{self.price}'
        })
        with open('Car_data.json', 'w') as file:
            json.dump(data_to_add, file, indent=4)

    def find_by_name(self):
        with open('Car_data.json') as file:
            data_to_find = json.load(file)
            for i in data_to_find:
                if i['name'] == self:
                    print(i['name'], i['color'], i['price'])

    def edit_name(self):
        with open('Car_data.json') as file:
            data_to_find = json.load(file)
            for i in data_to_find:
                if i['name'] == self:
                    i['name'] = input('Enter new name: ')
                with open('Car_data.json', 'w') as f:
                    json.dump(data_to_find, f, indent=4)

    def edit_color(self):
        with open('Car_data.json') as file:
            data_to_find = json.load(file)
            for i in data_to_find:
                if i['name'] == self:
                    i['color'] = input('Enter new color: ')
                with open('Car_data.json', 'w') as f:
                    json.dump(data_to_find, f, indent=4)

    def edit_price(self):
        with open('Car_data.json') as file:
            data_to_find = json.load(file)
            for i in data_to_find:
                if i['name'] == self:
                    i['price'] = input('Enter new price: ')
                with open('Car_data.json', 'w') as f:
                    json.dump(data_to_find, f, indent=4)

    @staticmethod
    def get_info():
        with open('Car_data.json') as json_file:
            data = json.load(json_file)
            for i in data:
                print(i)


def question():
    q1 = input(
        'Choose action\n'
        '1 - get list of cars\n'
        '2 - add new car\n'
        '3 - find car info\n'
        '4 - edit car info\n'
        'q - quit\n'
    )
    if q1 == '1':
        Cars.get_info()
        print('')
        question()
    elif q1 == '2':
        car_name, car_color, car_price = (input('Enter name, color, price:\n').
                                          split(', ' or ' ' or ','))
        Cars.add_data(Cars(car_name, car_color, car_price))
        print('Car added!\n''')
        question()
    elif q1 == '3':
        name = input('Enter name of car for info: ')
        Cars.find_by_name(name)
        question()
    elif q1 == '4':
        name = input('Enter name of car for info: ')
        Cars.find_by_name(name)
        param = input('What do you want to change?\n'
                      '1 - name\n'
                      '2 - color\n'
                      '3 - price\n')
        if param == '1':
            Cars.edit_name(name)
            print('New name edited!\n''')
            question()
        if param == '2':
            Cars.edit_color(name)
            print('New color edited!\n''')
            question()
        if param == '3':
            Cars.edit_price(name)
            print('New price edited!\n''')
            question()
    elif q1 == 'q':
        quit()


print('Welcome to <Car Garage!>')
question()
