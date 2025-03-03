class Flowers:
    flower = True
    material = 'клетчатка'

    def __init__(self, name, color, num_petals, stem_length, smell, price, life_time, freshness):
        self.name = name
        self.color = color
        self.num_petals = num_petals
        self.stem_length = stem_length
        self.smell = smell
        self.price = price
        self.life_time = life_time
        self.freshness = freshness


class Roses(Flowers):
    def __init__(self, name, color, num_petals, stem_length, smell, spikes, price, life_time, freshness):
        super().__init__(name, color, num_petals, stem_length, smell, price, life_time, freshness)
        self.spikes = spikes


class Violets(Flowers):
    def __init__(self, name, color, num_petals, stem_length, smell, color_gradient, price, life_time, freshness):
        super().__init__(name, color, num_petals, stem_length, smell, price, life_time, freshness)
        self.color_gradient = color_gradient


rose_red = Roses('Роза', 'Красный', 14, '50 см', 'Сладкий пряный', True,
                 10, 5, 'fresh')
rose_white = Roses('Роза', 'Белый', 15, '40 см', 'Ирис', True, 12,
                   3, 'medium')
violet_purple = Violets('Фиалка', 'Фиолетовый', 5, '5 см', 'Сладкий пудровый',
                        True, 5, 8, 'fresh')
violet_blue = Violets('Фиалка', 'Небесный', 7, '8 см', 'Древесный',
                      False,6, 2, 'stale')

n_rose_red = input("Введите кол-во красных роз: ")
n_rose_white = input("Введите кол-во белых роз: ")
n_violet_purple = input("Введите кол-во фиолетовых фиалок: ")
n_violet_blue = input("Введите кол-во синих фиалок: ")

flowers_bouquet = []
flowers_bouquet.append(rose_red)
flowers_bouquet.append(rose_white)
flowers_bouquet.append(violet_purple)
flowers_bouquet.append(violet_blue)


class Booket:
    def __init__(self, flowers):
        self.flowers = flowers

    def display_flowers(self):
        print("\n")
        for flower in self.flowers:
            print(f"{flower.name} - {flower.color} цвет: {flower.price}$, {flower.num_petals} лепестков, "
                  f"длина стебля {flower.stem_length}, запах {flower.smell}, живет {flower.life_time} дней, "
                  f"свежесть {flower.freshness}")

    def calculate_cost(self, n_rose_red, n_rose_white, n_violet_purple, n_violet_blue):
        cost_rose_red = int(rose_red.price) * int(n_rose_red)
        cost_rose_white = int(rose_white.price) * int(n_rose_white)
        cost_violet_purple = int(violet_purple.price) * int(n_violet_purple)
        cost_violet_blue = int(violet_blue.price) * int(n_violet_blue)

        total_cost = (cost_rose_red + cost_rose_white + cost_violet_purple + cost_violet_blue)

        print(f"\nИтого: {total_cost}$ за букет")

    def withering_time(self, n_rose_red, n_rose_white, n_violet_purple, n_violet_blue):
        life_booket = ((int(rose_red.life_time) * int(n_rose_red) + int(rose_white.life_time) * int(n_rose_white)
                        + int(violet_purple.life_time) * int(n_violet_purple) + int(violet_blue.life_time)
                        * int(n_violet_blue)) / (int(n_rose_red) + int(n_rose_white) + int(n_violet_purple)
                                                 + int(n_violet_blue)))
        print(f"\nВремя увядания букета по среднему времени жизни всех цветов: {life_booket} в календарных сутках")

    def sort_flowers(self, attribute):
        if attribute in ('color', 'price', 'num_petals', 'stem_length', 'smell', 'life_time', 'freshness'):
            self.flowers.sort(key=lambda flower: getattr(flower, attribute))
        else:
            print("Неверный атрибут для сортировки.")

    def search_flowers(self, attribute, value):
        found_flowers = [
            flower for flower in self.flowers if getattr(flower, attribute) == value
        ]

        if found_flowers:
            print(f"Найденные цветы по {attribute} = {value}:")
            for flower in found_flowers:
                print(f"{flower.name} - {flower.color} цвет: {flower.price}$")
        else:
            print(f"Цветы с {attribute} = {value} не найдены.")


booket = Booket(flowers_bouquet)

booket.display_flowers()
booket.calculate_cost(n_rose_red, n_rose_white, n_violet_purple, n_violet_blue)
booket.withering_time(n_rose_red, n_rose_white, n_violet_purple, n_violet_blue)

# Сортировка
print("\nСортировка по: color, price, num_petals, stem_length, smell, life_time, "
      "freshness")
booket.sort_flowers(input("Введите параметр: "))
booket.display_flowers()

# Поиск по среднему времени жизни
filter_value = input("\nВведите значение для фитрации по life_time: ")
booket.search_flowers('life_time', int(filter_value))
