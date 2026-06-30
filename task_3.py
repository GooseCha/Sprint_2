class PointsForPlace:
    def __init__(self, points=0):
        self.points = points

    @staticmethod
    def get_points_for_place(place=int):
        if place > 100:
            print("Баллы начисляются только первым 100 участникам")
        elif place < 1:
            print("Спортсмен не может занять нулевое или отрицательное место")
        else:
            points = 101 - place
        return points


class PointsForMeters:
    def __init__(self, points=0):
        self.points = points

    @staticmethod
    def get_points_for_meters(meters=int):
        if meters < 0:
            print("Количество метров не может быть отрицательным")
        else:
            points = 0.5 * meters
        return points


class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self, points=0):
        super().__init__(points)

    def get_total_points(self, meters, place):
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
