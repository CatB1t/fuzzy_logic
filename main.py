def fuzzify(fuzzy_sets, crisp_value):
    memberships = []

    def y_triangle(delta_y, delta_x):
        m = delta_y / delta_x
        # our y values range from 0 to 1, therefore we know that if our slope is positive
        # then Y start must be 0, otherwise 1
        b = (delta_y > 0) - m * f_set[-1]
        return m * crisp_value + b

    for f_set in fuzzy_sets:
        if f_set[-1] >= crisp_value >= f_set[0]:
            # Triangular
            if len(f_set) == 3:
                # Line equation y = mx+b
                d_y = (-1 if f_set[0] == f_set[1] else 1)
                d_x = f_set[-1] - f_set[0]
                memberships.append(y_triangle(d_y, d_x))
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
                    memberships.append(y_triangle(d_y, d_x))
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


coreTemp = [[0, 0, 40], [30, 35, 45, 50], [40, 80, 80]]
print(fuzzify(coreTemp, 45))  # The output will be [0,1,0.125]

fanSpeed = [[0,0,2500], [1000,2500,4000], [2500, 5000, 5000]]
fanMemDegrees = [0,0,0.333]
print(defuzzify(fanSpeed, fanMemDegrees)) # The output will be 4166