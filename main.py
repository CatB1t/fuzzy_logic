def fuzzify(fuzzy_sets, crisp_value):
    memberships = []
    return memberships

def defuzzify(memberships, fuzzy_sets):
    pass

coreTemp = [[0, 0, 40], [30, 35, 45, 50], [40, 80, 80]]
print(fuzzify(coreTemp, 45))  # The output will be [0,1,0.125]

fanSpeed = [[0,0,2500], [1000,2500,4000], [2500, 5000, 5000]]
fanMemDegrees = [0,0,0.333]
print(defuzzify(fanSpeed, fanMemDegrees))