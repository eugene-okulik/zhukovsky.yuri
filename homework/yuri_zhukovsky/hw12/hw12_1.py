class Flowers:
    flower = True
    smell = ''
    material = 'клетчатка'

    def __init__(self, color, num_petals, height):
        self.color = color
        self.num_petals = num_petals
        self.height = height


class Roses(Flowers):
        def __init__(self, color, num_petals, height, smel, spikes):
            super().__init__(color, num_petals, height, smel)
            self.spikes = spikes


class Violets(Flowers):
        def __init__(self, color, num_petals, height, smel, color_gradient):
            super().__init__(color, num_petals, height, smel)
            self.color_gradient = color_gradient


rose_red = Roses('Красный', 14, '50 см', 'Сладкий пряный', True)
rose_white = Roses('Белый', 15, '40 см', 'Ирис', True)
violet_purple = Violets('Фиолетовый', 5, '5 см', 'Сладкий пудровый', True)
violet_blue = Violets('Небесный', 7, '8 см', 'Древесный', True)