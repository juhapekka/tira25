class DataAnalyzer:
    def __init__(self):
        self.amo = 0
        self.mid_x = 0
        self.mid_y = 0
        self.mid_xy = 0
        self.mid_xx = 0
        self.mid_yy = 0

    def add_point(self, x, y):
        # TODO
        # sum(i^n) = 1^n * (y_i - (ax_i + b))^2 ->sigmat?

        self.amo += 1
        self.mid_x += x
        self.mid_y += y
        self.mid_xy += x * y
        self.mid_xx += x * x
        self.mid_yy += y * y

    def calculate_error(self, a, b):
        return self.mid_yy - 2 * (a * self.mid_xy + b * self.mid_y) + a**2 * self.mid_xx + b * (2 * a * self.mid_x + b * self.amo)
    
if __name__ == "__main__":
    analyzer = DataAnalyzer()

    analyzer.add_point(1, 1)
    analyzer.add_point(3, 2)
    analyzer.add_point(5, 3)
    print(analyzer.calculate_error(1, 0)) # 5
    print(analyzer.calculate_error(1, -1)) # 2
    print(analyzer.calculate_error(3, 2)) # 293

    analyzer.add_point(4, 2)
    print(analyzer.calculate_error(1, 0)) # 9
    print(analyzer.calculate_error(1, -1)) # 3
    print(analyzer.calculate_error(3, 2)) # 437