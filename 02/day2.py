'''
# Part 1
depth = 0
hor = 0

with open( './input.txt' ) as f:
    for cmd in f:
        cmd = cmd.strip().split(' ')

        if cmd[0] == 'forward':
            hor += int( cmd[1] )

        elif cmd[0] == 'down':
            depth += int( cmd[1] )

        elif cmd[0] == 'up':
            depth -= int( cmd[1] )

print( depth * hor )
'''

# Part 2
depth = 0
hor = 0
aim = 0

with open( './input.txt' ) as f:
    for cmd in f:
        cmd = cmd.strip().split(' ')

        if cmd[0] == 'forward':
            hor += int( cmd[1] )
            depth += aim * int( cmd[1] )

        elif cmd[0] == 'down':
            aim += int( cmd[1] )

        elif cmd[0] == 'up':
            aim -= int( cmd[1] )

print( depth * hor )
