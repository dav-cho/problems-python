##
#### Scraps
###############

def test_dict():
    test = {
        1 > 0: '1 > 0, true',
        0 > 1: '0 > 1, false',
        10 != 10: '10 == 10, true'
    }

    print(test[True])


def max_ball(v):
    g = 9.81 ** 2
    mps = v * 1000 / 3600
    
    for t in range(5):
        height = mps * t - 0.5 * g * t ** 2
        print(t, height)
    
    
max_ball(15)
    
#     t = mx = 0
#     for s in range(50):
#         height = v * s - 0.5 * g * s ** 2
#         if height > mx:
#             mx = height
#             t = s
#     return t
