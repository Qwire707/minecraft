class Mapmanager:
    def __init__(self):
        self.model = 'models/block'
        self.texture = 'textures/brick.png'
        self.color = (72, 13, 136, 0.8)

        self.start_new()

        # for x in range(10):
        #     for y in range(10):
        #         self.add_block((x, y, 1))
        #
        # self.add_block((1, 1, 1))
        # self.add_block((1, 1, 2))
        # self.add_block((1, 1, 3))
        # self.add_block((1, 2, 3))
        # self.add_block((2, 2, 3))
        #
        #
        # self.add_block((3, 3, 4))
        # self.add_block((5, 3, 5))
        # self.add_block((7, 3, 7))
        # self.add_block((7, 5, 9))
        # self.add_block((9, 5, 9))
        # self.add_block((11, 6, 11))
        #
        #
        # self.add_block((13, 6, 13))
        # self.add_block((13, 7, 13))

    def add_block(self, position: tuple) -> None:
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setColor(self.color)
        self.block.setPos(position)
        self.block.reparentTo(self.land)

    def start_new(self):
        self.land = render.attachNewNode('Land')

    def load_map(self, filename: str):
        with open (filename, 'r') as file:
            y = 0
            for line in file:
                x = 0
                line_lst = line.split(' ')
                for z in line_lst:
                    for i in range(int(z) + 1):
                        self.add_block((x, y, i))
                    x += 1
                y += 1
            return x, y
