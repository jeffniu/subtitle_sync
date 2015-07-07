#!/usr/local/opt/python/bin/python
# increase or decrease srt format subtitle time

import datetime 
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input_file", dest="infilename", help="subtitle file name")
parser.add_option("-o", "--output_file", dest="outfilename", help="your output subtitle filename")
parser.add_option("-a", "--adjust", dest="adjust", help="seconds to increase or decrease")

(options, args) = parser.parse_args(sys.argv)

print "input: " + options.infilename
print "output: " + options.outfilename
print "adust: " + options.adjust

infile = open(options.infilename, 'r')
outfile = open(options.outfilename, 'w')

outlines = []
for line in infile:
	items = line.split()
	outitems = []
	for item in items:
		try:
			t = datetime.datetime.strptime(item, "%H:%M:%S,%f")
			adj = int(options.adjust)
			t = t + datetime.timedelta(seconds=adj)
			outitems.append(t.strftime("%H:%M:%S,%f")[:-3])
		except Exception, e:
			print e
			outitems.append(item)
	outline = " ".join(outitems)
	outlines.append(outline)

outfile.write("\n".join(outlines))

infile.close()
outfile.close()

