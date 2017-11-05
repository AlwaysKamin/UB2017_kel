

class template2x4():
    x = [0, 0, 0, 0]
    y = [0, 0, 0, 0]

    def template_one(self):
        self.x = [175, 2000, 175, 500]
        self.y = [100, 300, 120, 10]

    #TODO change template_two to something else
    def template_two(self):
        self.x = [175, 2000, 1000, 1000]
        self.y = [100, 100, 100, 250]

    #
    def template_three(self):
        self.x = [200, 300, 175, 2000]
        self.y = [50, 150, 100, 100]

    def returnTemplate(self):
        return self.x, self.y