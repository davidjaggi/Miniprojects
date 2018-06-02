import numpy as np

def grid_dimensions(string, tuple_of_2_inits):
    h, w = tuple_of_2_inits
    output = [ch for ch in list(string) if ch.isalpha()]
    output += ['X']*((w*h)-len(output))
    return [output[offs:offs+h] for offs in range(0, len(output),h)]

def clock(array):
    output = []
    while len(array) > 1:
        output += array.pop(0)
        array = np.rot90(array).tolist()
    output += array.pop(0)
    return output

def spiral(array, direction):
    array = np.rot90(array).tolist()
    if direction != 'clockwise':
        array = np.transpose(array).tolist()
    return clock(array)

def main(inp):
    string, dimension, direction = inp
    output = grid_dimensions(string, dimension)
    output = spiral(output, direction)
    return ''.join(output)

print(main(("WE ARE DISCOVERED. FLEE AT ONCE", (9, 3), 'clockwise')))
print(main(("why is this professor so boring omg", (6, 5), 'counter-clockwise')))
print(main(("Solving challenges on r/dailyprogrammer is so much fun!!", (8, 6), 'counter-clockwise')))
print(main(("For lunch let's have peanut-butter and bologna sandwiches", (4, 12), 'clockwise')))
print(main(("I've even witnessed a grown man satisfy a camel", (9,5), 'clockwise')))
print(main(("Why does it say paper jam when there is no paper jam?", (3, 14), 'counter-clockwise')))