def bottle_word(number):
    if number == 1:
        return ('bottle')
    else:
        return ('bottles')

song = ''
for i in range (10,0,-1):
    for j in range (2):
        song = song + '''there were {0} green {1}, hanging on a wall\n'''.format(i, bottle_word(i))
    song = song + '''and if one green bottle should accidentally fall, there would be\n 
{0} green {1} hanging on that wall\n'''.format(i-1, bottle_word(i-1))
song = song + 'There is a lot of glass sitting on the floor.\n'
print song
