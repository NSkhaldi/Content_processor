import random
import time
import glob
import os
import sys
import collections
from collections import Counter

#Default list of hosts
hosts=['Hannibal','Samatchi', 'Hanny', 'Steeve','Mustafa' ]

#dashboard global variables
connected_hosts, received_hosts, active_hosts=Counter(),Counter(),Counter()

#log out of order time. Useful for including log files created slightly before init_datetime but still have entry lines in the interval. 
log_ofo_time=9