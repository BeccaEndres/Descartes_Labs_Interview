# Question 3: fix the problem with this script
# Question 3 extra credit: How else might this fail?
import sys
import time
def main(t):

    """This should output something like 1473539489.174058"""
    time.sleep(t)
    print "seconds since the epoch is %f" % time.time()
if __name__ == "__main__":
    try:
       t = int(sys.argv[1])
       if t < 0:
	   t = 1
    except:
        t = 1
    main(t)


# This script might also fail if the user inputs a large number 
