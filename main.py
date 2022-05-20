def fuzzify(fuzzy_sets, crisp_value):
    memberships = []

    def y_triangle(delta_y, delta_x, point_x, point_y):
        m = delta_y / delta_x
        b = point_y - m * point_x
        return m * crisp_value + b

    for f_set in fuzzy_sets:
        if f_set[-1] >= crisp_value >= f_set[0]:
            # Triangular
            if len(f_set) == 3:
                # Right angle triangle
                if f_set[0] == f_set[1] or f_set[-1] == f_set[-2]:
                    d_y = (-1 if f_set[0] == f_set[1] else 1)
                    d_x = f_set[-1] - f_set[0]
                    memberships.append(y_triangle(d_y, d_x, 0.5, f_set[1]))
                # Isosceles triangle
                else:
                    if crisp_value >= f_set[1]:
                        d_y = -1
                        d_x = f_set[-1] - f_set[1]
                    else:
                        d_y = 1
                        d_x = f_set[1] - f_set[0]
                    memberships.append(y_triangle(d_y, d_x, f_set[1], 1))
            # Trapezoidal
            elif len(f_set) == 4:
                if f_set[1] <= crisp_value <= f_set[-2]:
                    memberships.append(1)
                else:
                    # Right triangle of the trapezoid
                    if crisp_value > f_set[-2]:
                        x1, y1, x2, y2 = f_set[-2], 1, f_set[-1], 0
                    # Left triangle of the trapezoid
                    elif crisp_value < f_set[1]:
                        x1, y1, x2, y2 = f_set[0], 0, f_set[1], 1
                    d_y = y2 - y1
                    d_x = x2 - x1
                    memberships.append(y_triangle(d_y, d_x, x1, y1))
        else:
            memberships.append(0)

    return memberships


def defuzzify(fuzzy_sets, memberships):
    assert len(fuzzy_sets) == len(memberships), "Lists must be equal length"

    memberships_sum = 0
    for i in range(len(fuzzy_sets)):
        centroid = sum(fuzzy_sets[i]) / len(fuzzy_sets[i])
        memberships_sum += centroid * memberships[i]

    return memberships_sum / sum(memberships)


def assignment_test_cases():
    coreTemp = [[0, 0, 40], [30, 35, 45, 50], [40, 80, 80]]
    print(fuzzify(coreTemp, 45))  # The output will be [0,1,0.125]

    fanSpeed = [[0, 0, 2500], [1000, 2500, 4000], [2500, 5000, 5000]]
    fanMemDegrees = [0, 0, 0.333]
    print(defuzzify(fanSpeed, fanMemDegrees))  # The output will be 4166


#
def project_test_cases():
    systolic_blood_pressure = [[80, 100, 120], [110, 120, 130], [125, 150, 175, 200]]
    print("Fuzzification: {}".format(fuzzify(systolic_blood_pressure, 100)))

    healthy = [[0, 1, 2], [1.5, 2, 2.5], [2, 2.5, 3]]
    memberships = [0.5, 0.5, 0]
    print("Defuzzification: {}".format(defuzzify(healthy, memberships)))


project_test_cases()
