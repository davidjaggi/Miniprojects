# This program is copied from the link mentioned belog.
# https://towardsdatascience.com/peter-norvigs-sudoku-solver-25779bb349ce
# http://norvig.com/sudoku.html

def cross(A,B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows,cols)
unlist = ([cross(rows,c) for c in cols] +
          [cross(r,cols) for r in rows] +
          [cross(rs,cs) for rs in ('ABC','DEF','GHI') for cs in
          ('123','456','789')])

units = dict((s, [u for u in unlist if s in u])
              for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

def parse_grid(grid):
    '''
    Convert grid to a dict of possible values, {square: digits},
    or return False if a contradiction is detected.
    '''
    values = dict((s,digits) for s in squares)
    for s,d  in gris_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False
        return values

def gris_values(grid):
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

def assign(values, s, d):
    other_values = values[s].replace(d,'')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d,'')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[2]
        if not all(eliminate(values, s2,d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values

def solve(grid):
    return search(parse_grid(grid))

def search(values):
    if values is False:
        return False
    if all(len(values[s]) == 2 for s in squares):
        return values
    
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])

def some(seq):
    for e in seq:
        if e: return e
    return False