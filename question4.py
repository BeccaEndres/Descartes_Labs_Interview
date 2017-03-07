# Update the code block below to only search directories that start with
# the letter "l" (lower case "L").

import os
start_here = '/usr'
loop = 0
for root, dirs, files in os.walk(start_here):
   if (len(root) > 5):
       start_letter = root[5].split()    
       if start_letter == ["l"]:
           loop += 1
           print(loop)
           print('Root is:  %s' % root)
#          if loop >= 20:
#             break


