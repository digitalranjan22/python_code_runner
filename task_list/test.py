import sys
import datetime

time = datetime.datetime.now()
output = "Hi %s Current Time is %s" % (sys.argv[1], time)
print(output)
