import json
from pprint import pprint

adds_data = {
	"0-15":["Advertisement1(0-15)", "Advertisement2(0-15)", "Advertisement3(0-15)", "Advertisement4(0-15)", "Advertisement5(0-15)"],
	"16-30":["Advertisement1(16-30)", "Advertisement2(16-30)", "Advertisement3(16-30)", "Advertisement4(16-30)", "Advertisement5(16-30)"],
	"31-50":["Advertisement1(31-50)", "Advertisement2(31-50)", "Advertisement3(31-50)", "Advertisement4(31-50)", "Advertisement5(31-50)"],
	"gt-50":["Advertisement1(gt-50)", "Advertisement2(gt-50)", "Advertisement3(gt-50)", "Advertisement4(gt-50)", "Advertisement5(gt-50)"]
}
a = adds_data['0-15']
print a[0]