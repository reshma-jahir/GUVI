noy = int(input())
if noy > 2:
    for i in range(2, noy):
        if noy % i == 0:
            print('yes')
            break
    else:
        print('no')
elif noy == 2:
    print('no')
