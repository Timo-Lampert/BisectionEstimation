import decimal
import math

func = lambda x: x
precision = 8
gapprecision = 10  # checks for crosspoints in 1/n gaps.
anyfound = 0
points = []


def bisectionAlgorithm(x, x1):
    x2 = (x + x1) / 2
    while decimal.Decimal(str(x2)).as_tuple().exponent > -1 * precision:  # get accuracy to 8
        x2 = (x + x1) / 2
        rootcheck = func(x) * func(x2)
        if rootcheck < 0:

            x1 = x2

        elif rootcheck > 0:

            x = x2

        elif rootcheck == 0:
            return x2
    return x2


def calculateCrossPoints(x):
    currentX = x / gapprecision - max

    if x == 0:
        point['x'] = currentX - 1
        point['y'] = func(currentX - 1)

    anyFound = 0
    newPoint['y'] = func(currentX)
    newPoint['x'] = currentX

    # y = 0 between x0 and x1?
    if (((newPoint['y'] < 0 and point['y'] >= 0)
         or (point['y'] < 0 and newPoint['y'] >= 0))
        or newPoint['y'] == 0) \
            and point not in points:

        print(f"Zero point found between {point['x']} and {newPoint['x']}")
        result = ""
        global anyfound
        anyfound = 1
        # are the points directly at x0/x1?

        if func(point['x']) == 0:
            result = f"(exact match) {point['x']}"
            points.append(point)
        elif func(newPoint['x']) == 0:
            result = f"(exact match) {newPoint['x']}"
            points.append((newPoint))
        else:
            result = str(bisectionAlgorithm(point['x'], newPoint['x']))
        print("       closest estimation " + result)

    point['x'] = newPoint['x']
    point['y'] = newPoint['y']


if __name__ == '__main__':

    print("insert polynomial function to check y=0 for")
    f = input()
    f = f.replace("^", "**")

    func = lambda x: eval(f)
    print("range on x axis: ")
    max = int(input())
    print("precision of decimal places")
    precision = int(input())

    point = {'x': 0, 'y': 0}
    newPoint = {'x': 0, 'y': 0}
    if (gapprecision > 10000 or precision > 8):
        print("Precison set high, may take longer")

    for x in range(max * gapprecision * 2):
        try:
            calculateCrossPoints(x)
        except:
            pass
    if anyfound == 0:
        print("No crosspoints found")
