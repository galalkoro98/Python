# Listen to this story: a boy and his father, a computer programmer, 
# are playing with wooden blocks. They are building a pyramid.
# Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. 
# The pyramid is stacked according to one simple principle: 
# each lower layer contains one block more than the layer above.
# The figure illustrates the rule used by the builders:
# Your task is to write a program which reads the number of blocks the builders have, 
# and outputs the height of the pyramid that can be built using these blocks.
# Note: the height is measured by the number of fully completed layers – 
# if the builders don't have a sufficient number of blocks and cannot complete the next layer, 
# they finish their work immediately.

# input 20: the output is 5
# input 1000: the output is 44
# input 4: the output is errors

blocks = int(input("Entre the number blocks: "))
height = 0

while True:
    blocks = blocks - ( 1 + height ) 
    if blocks < 0 or not blocks % 1 == 0:
        break
    else:
        height += 1
        if height > 0:
            print ("Height now at", height)