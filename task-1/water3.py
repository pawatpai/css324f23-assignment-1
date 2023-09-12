def initial_state():
    return (8, 0, 0)  # (8-liter bottle, 5-liter bottle, 3-liter bottle)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    a, b, c = s
    # pour from one to another

    # pour to a
    remaining = 8 - a
    if b>0 and remaining>0:
      if b>remaining:
        yield ((8, b-remaining, c), remaining)
      else :
        yield ((a+b, 0, c), b)
    if c > 0 and remaining>0:
      if c>remaining:
        yield ((8, b, c-remaining), remaining)
      else :
        yield ((a+c, b, 0), c)
    
    # pour to b
    remaining = 5 - b
    if a>0 and remaining>0:
      if a>remaining:
        yield ((a-remaining, 5, c), remaining)
      else:
        yield ((0, b+a, c), a)
    if c>0 and remaining>0:
      if c>remaining:
        yield ((a, 5, c-remaining), remaining)
      else:
        yield ((a, b+c, 0), c)

     # pour to c
    remaining = 3 - c
    if a>0 and remaining>0:
     if a>remaining:
      yield ((a-remaining, b, 3), remaining)
     else:
      yield ((0, b, c+a), a)
    if b>0 and remaining>0:
     if b>remaining:
      yield ((a, b-remaining, 3), remaining)
     else:
      yield ((a, 0, c+b), b)