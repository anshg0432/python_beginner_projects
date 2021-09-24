import random

t=1
while t:
    x= random.randint(1,6)
    if x ==1:
        print('[---------]')
        print('[         ]')
        print('[    0    ]')
        print('[         ]')
        print('[-------- ]')
    
    elif x==2:
        print('[---------]')
        print('[    0    ]')
        print('[         ]')
        print('[    0    ]')
        print('[-------- ]')
    elif x==3:
        print('[---------]')
        print('[    0    ]')
        print('[    0    ]')
        print('[    0    ]')
        print('[-------- ]')
    elif x==4:
        print('[---------]')
        print('[  0   0  ]')
        print('[         ]')
        print('[  0   0  ]')
        print('[---------]')
    elif x==5:
        print('[---------]')
        print('[  0   0  ]')
        print('[    0    ]')
        print('[  0   0  ]')
        print('[-------- ]')
    else:
        print('[---------]')
        print('[  0   0  ]')
        print('[  0   0  ]')
        print('[  0   0  ]')
        print('[---------]')
    k = input("enter y to roll again ")
    if k == 'y':
        t=1
    else:
        t=0
