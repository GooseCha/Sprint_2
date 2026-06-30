class PointsForPlace:
    def __init__(self, points=0):
        self.points = points

    @staticmethod
    def get_points_for_place(place=int):
        if place > 100:
            print("Баллы начисляются только первым 100 участникам")
            return 0
        elif place < 1:
            print("Спортсмен не может занять нулевое или отрицательное место")
            return 0
        else:
            return 101 - place


class PointsForMeters:
    def __init__(self, points=0):
        self.points = points

    @staticmethod
    def get_points_for_meters(meters=int):
        if meters < 0:
            print("Количество метров не может быть отрицательным")
            return 0
        else:
            return 0.5 * meters


class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self, points=0):
        super().__init__(points)

    def get_total_points(self, meters=0, place=0):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
