#!usr/local/bin


class AVG:
    def __init__(self):
        self.sum = 0
        self.size = 0
        self.avg = 0

    def update_size(self):
        self.size += 1

    def update_sum(self, num):
        self.sum += num

    def calculate_avg(self):
        return self.sum * 1.0 / self.size
