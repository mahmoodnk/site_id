# site_id
Add site ID to a csv file. 



```
usage: site_id.py [-h] [--new_name NEW_NAME] filename site_id output_dir

Add site ID to a given file.

positional arguments:
  filename             Specify the CSV file that you want to add site ID to.
  site_id              Site ID to be added.
  output_dir           Specify where to save the new file.

optional arguments:
  -h, --help           show this help message and exit
  --new_name NEW_NAME  Option to change name of the output file. Default is
                       set to the file's original name. Be sure not to
                       overwrite the data if keeping the same name.
```



Example: Add site ID = 123456 to the dummy_data CSV file and save in the new_directory folder.

```
python site_id.py dummy_data.csv 123456 ./new_directory
```

Output: Output with site ID is saved at {path}/new_directory/dummy_data.csv




##### Notes - 
(1) If you want the filename to remain the same on output, make sure not to overwrite your original files by specifying a different directory for output (output_dir).

(2) Both absolute and relative paths are considered valid input.

(3) The script specifies Python installed through Anaconda Navigator. You may need to change this for your own machine.
