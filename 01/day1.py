# PART 1
'''
depths = []

with open( './input.txt' ) as f:
    for line in f:
        depths.append( int( line.strip() ) )

inc = 0

for i in range ( 1, len( depths ) ):
    if depths[i] > depths[i-1]:
        inc += 1

print( inc )
'''

# PART 2
depths = []
depths_n = []
 
with open( './input.txt' ) as f:
    for line in f:
        depths.append( int( line.strip() ) )

inc = 0

for i in range(0, len(depths) - 2):
    depths_n.append( depths[i] + depths[i + 1] + depths[i + 2] )

for i in range ( 1, len( depths_n ) ):
    if depths_n[i] > depths_n[i-1]:
        inc += 1

print( inc )
