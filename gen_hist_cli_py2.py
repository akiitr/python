#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from numpy import histogram,percentile,array
import argparse
from math import floor

# Constants
CHARS={'full_top':'┃', 'half_top':'╻', 'fill':'┃'}

def draw_hist(normed_hist_list,shape,args):
    """ takes a list of histogram bin counts and shape(min,max) of input """
    
    # TODO make the offset configurable
    y_offset = '       '
    y_label  = ' prop. '

    print ""
    # Build plot from top level
    for depth in range(args.height-1,-1,-1):

        # Draw Y axis
        if depth == args.height/2:
            sys.stdout.write(y_label+'│')
        else:
            sys.stdout.write(y_offset+'│')

        # Draw bars
        for item in normed_hist_list:
            floored_item = floor(item)
            if floored_item >= depth:
                if floored_item == depth and item % 1 < 0.75 and item%1 >0.25:
                    sys.stdout.write( CHARS['half_top'] )
                elif floored_item == depth and item % 1 > 0.75 :
                    sys.stdout.write( CHARS['full_top'] )
                elif floored_item > depth:
                    sys.stdout.write( CHARS['fill'] )
                else:
                    sys.stdout.write(' ')
                continue
            else:
                sys.stdout.write(' ')
        print ""

    # Draw X axis 
    print y_offset + '└'+ "─"*(args.bins+2)
    print y_offset + str(shape[0]) + ' '*(args.bins-3) + str(shape[1])


def parse_args():
    parser = argparse.ArgumentParser(description='draw a histogram from stdin', add_help=False)
    parser.add_argument('-b', '--bins', type=int, help='the number of bins (default=60)', default=60)
    parser.add_argument('-h', '--height', type=int, help='the height of the plot (default=10)', default=10)
    parser.add_argument('-?', '--help', action='help', help='show this help and exit')
    return parser.parse_args(sys.argv[1:])


def main():

    args = parse_args()
    input_data = sys.stdin.read().strip('\n')
    input_list = input_data.split('\n')
    
    temp = []
    
    # Convert input to floats
    try:
        input_list = map(float,input_list)
    except:
      #raise SystemError("Failed to convert input to float")
    
      # AK: a way to remove the text from column but slow
      for i in input_list:
        try:
          temp.append(float(i))
        except:
          continue
      input_list = temp
	# AK: Done

    hist_list,bin_edges = histogram(input_list,bins=args.bins)
    max_count = max(hist_list)
    shape = ( min(input_list), max(input_list) )
    normed_hist_list = [ float(x)*args.height/max_count for x in hist_list ]
    
    # Draw the histogram
    draw_hist(normed_hist_list,shape,args)
 
    # Calculate stats on data
    print '\ncount      :',len(input_list)
    print 'Mean	:',array(input_list).mean()
    print 'Var	:',array(input_list).var()
    print 'Std_dev	:',array(input_list).std()

    for perc in [25,50,75]:
        print "{0}th perc. :".format(perc), percentile(input_list,perc)
    

if __name__ == '__main__':
    main()
