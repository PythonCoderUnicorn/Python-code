
# BAJORAN ORB OF PROPHACY
# BY: ZANE DAX
# JUN 29, 2021


import numpy as np

x = np.random.randint(1,20)
print(x)


prophacy = ['The path ahead will be filled with temptations but stay steady','Your path is set, no need to worry as the Prophets know you will prevail','In your home, you will find some troubling details, things will be altered','Knowing your strengths is only 1 side of the equation','Take the hate for Cardassians and put into positive energy','Your Pah is strong, you are on the righteous path', 'Your fight is not with whom you think it is, there are layers','Victories are sweet like jumja sticks when you work hard for them, do not take shortcuts','In the garden you will find what you need, do not rush the adventure, savour the experience','Planting a tree in memory of loved ones is the path forward', 'Any peace you have is because of your Pah','Be careful of surprises, watch out for deception', 'You are guided to follow your passion, not latinum'
]

num = int(input(f'Enter a number (1:{len(prophacy)-1}): '))
print(f':: {num}')

if (num >=1 and num <= len(prophacy)):
    print(prophacy[x] )
elif (num < 1):
    print('too low')
elif (num > len(prophacy)):
    print('too high')
else:
    print('not a valid number ')