#!/anaconda3/bin/python
# -*- coding: utf-8 -*-

# Written by: Nuha Mahmood
# Description: A script to add site ID to a given file. 
# Last modified: 11-3-2020 (election day :o)


import pandas as pd
import argparse
import os



# Help: Command line argument descriptions.

parser = argparse.ArgumentParser(
    description = 
    '''Add site ID to a given file.''')

# Positional arguments - required

parser.add_argument('filename', type=os.path.abspath, help = 'Specify the CSV file that you want to add site ID to.')

parser.add_argument('site_id', help = 'Site ID to be added.')

parser.add_argument('output_dir', type=os.path.abspath, help = 'Specify where to save the new file.')

# Optional arguments

parser.add_argument('--new_name', type=os.path.abspath, help = 'Option to change name of the output file. Default is set to the file\'s original name. Be sure not to overwrite the data if keeping the same name.')


def add_site_id(filename, site_id, output_dir, new_name = None):
    # read in file
    df = pd.read_csv(filename)
    
    # add site id
    df['site_id'] = str(site_id)
    
    # get base of filename - option to use a new name or keep the old filename
    base_name = os.path.basename(os.path.normpath(filename)) if new_name is None else os.path.basename(os.path.normpath(new_name))
    base = str(base_name).split('.')[0]
    
    # save new file
    df.to_csv(output_dir + "/" + base + '.csv', index = False)
    new_loc = (output_dir + "/" + base + '.csv')
    
     # Terminal output - confirmation 
    print(f"Output with site ID is saved at {new_loc}")


def main():
    args = parser.parse_args()
    add_site_id(args.filename, args.site_id, args.output_dir, args.new_name)
    
    
    
if __name__ == '__main__':
    main()