# Update the code block below to only search directories that start with
# the letter "l" (lower case "L").

import os
start_here = '/usr'
loop = 0
for root, dirs, files in os.walk(start_here):
    loop += 1
    print(loop)
    print('Root is:  %s' % root)
    if loop >= 20:
        break


