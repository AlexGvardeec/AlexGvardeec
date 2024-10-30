from webapp import db


# Создаем класс Category
class Category(db.Model):
    __tablename__ = 'categories_list'
    category_id = db.Column(db.Integer(), primary_key=True)
    category_name = db.Column(db.String(30), nullable=False)
    category_route = db.Column(db.String(30), nullable=False)
    items = db.relationship('Item', backref='market', lazy=True)

    def __init__(self, category_name, category_route):
        self.category_name = category_name
        self.category_route = category_route

    def __repr__(self):
        return (f'<Category(name={self.category_name}, '
                f'id={self.category_id}, '
                f'route={self.category_route}>')


# Создаем класс Item, указываем связь с подклассом Category
class Item(db.Model):
    __tablename__ = 'items_list'
    item_id = db.Column(db.Integer(), primary_key=True)
    item_name = db.Column(db.String(30), nullable=False)
    item_about = db.Column(db.String(500), nullable=False)
    item_class = db.Column(db.String(30), nullable=False)
    item_price = db.Column(db.Integer(), nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey('categories_list.category_id'), nullable=False)

    def __init__(self, item_name, item_about, item_class, item_price, category_id):
        self.item_name = item_name
        self.item_about = item_about
        self.item_class = item_class
        self.item_price = item_price
        self.category_id = category_id

    def __repr__(self):
        return (f'<Item(id={self.item_id}, '
                f'name={self.item_name}, '
                f'about={self.item_about}, '
                f'price={self.item_price}, '
                f'category_id={self.category_id})>')


bikes = [
    {
        'ID': 1,
        'name': 'Haro Lineage 20',
        'class': 'Взрослый BMX, диаметр колес 20\'',
        'about': 'Надежный и крепкий байк для начинающих',
        'price': 52499,
    },
    {
        'ID': 2,
        'name': 'WTP Envy 20',
        'class': 'Взрослый BMX, диаметр колес 20\'',
        'about': 'Легкий и крутой велосипед премиум-класса от бренда WTP',
        'price': 73599,
    },
    {
        'ID': 3,
        'name': 'Radio Dice 16',
        'class': 'Детский BMX, диаметр колес 16\'',
        'about': 'Велосипед для детей, начинающих свой путь в BMX',
        'price': 31999,
    },
]

parts = [
    {
        'ID': 1,
        'name': 'BSD ALVX 20.5',
        'class': 'рамы',
        'about': 'Отличная рама с короткими перьями',
        'price': 27999,
    },
    {
        'ID': 2,
        'name': 'CULT 2Shorty 20.5',
        'class': 'рамы',
        'about': 'Более крепкий аналог BSD ALVX',
        'price': 31999,
    },
    {
        'ID': 3,
        'name': 'Odyssey Twisted PC',
        'class': 'педали',
        'about': 'Пластиковые педали',
        'price': 2199,
    },
    {
        'ID': 4,
        'name': 'Fiction bikes Combo-seat',
        'class': 'седла',
        'about': 'Легкое комбо-седло',
        'price': 3299,
    },
]

lessons = [
    {
        'ID': 1,
        'name': 'Частное, 1 час',
        'class': 'индивидуальное',
        'about': 'Занятие с тренером 1 на 1, продолжительность 1 час',
        'price': 1500,
    },
    {
        'ID': 2,
        'name': 'Частное, 2 часа',
        'class': 'индивидуальное',
        'about': 'Занятие с тренером 1 на 1, продолжительность - 2 часа',
        'price': 2600,
    },
    {
        'ID': 3,
        'name': 'Группа, 1 час',
        'class': 'групповое',
        'about': 'Занятие в группе до 6 человек, продолжительность 1 час',
        'price': 1000,
    },
    {
        'ID': 4,
        'name': 'Группа, 2 часа',
        'class': 'групповое',
        'about': 'Занятие в группе до 6 человек, продолжительность - 2 часа',
        'price': 1600,
    },
]
