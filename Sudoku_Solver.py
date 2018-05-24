# https://towardsdatascience.com/peter-norvigs-sudoku-solver-25779bb349ce

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
              