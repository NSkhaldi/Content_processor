# What's inside?

*  A tool that genreate files continuously
*  A tool that simultanuously does operations on the content of those files, starting each x time from the most recent file.

## Files
The repo contains:
*  Folders 
    *  scripts: contains the log generation simulator and the log processing script
    *  aktools: The package containig the processing tools and conf file
    *  tests: containing the tests
    *  data: contains the data source data for the first part and for the tests
    *  output: contains the generated log data
    *  docs: contains a jupyter notebook and its pdf file
    
*  Files
   *   README.md
   *   LICENSE.md
   *   setup.py
   *   .gitignore


## Notes and asssumptions 

*   I assumed that a unique log file generation should not take more than some x time to generate.
*   Each predefined amount of time log files are processed
*   The logs are in each iteration reduced and sorted by time
*   The processing start with the file that is currently generated
*   The log file are parsed starting from the end (recent values first)
*   By 'hostanem that generated most connections', I considered the involvement  of the host and not him being the source.
*   I assumed that a host can connect to itself
*   I assumed that when hosts have the same highest number of connection, all of them should be displayed
*   Insted of repeating the host's name multiple times (ex: A host receives multiples connections from another), I considered for the sake of visibility to use collection for occurences count.
*   I assumed that log files will be archived/flexibily stored so I didn't create a routine to delete them 
*   CPU optimization was considered sleeping the process in each iteration
*   Memory optimization was considered by using built-in functions and my code syntax knowledge (less variables, comprehension lists...).


## Prerequisites

*   Python environment (version used: 3.8.3 )

## Installing

*   Clone/Download this git repository

*   Run the setup.py file 

```
python setup.py install
```

*   Run the log file generation

```
python generate_log_files.py <nb of line not exceeding 10000>
```

*   Run the main processing script with the right arguments

```
python scripts/main.py <existing hostname> <time to reprocess (s)>
```

## Demo & Proof of concept
*   By default a list of 3 hosts, It can changed it the aktool/conf.py file. Don't forget to run the setup again to consider the changes.

```
['Hannibal', 'Hanny', 'Steeve']
```


*   For the proof of concept you can start by generating logs with 6 lines.
```
python generate_log_files.py  6
```
*   After the log is created. the message 'log file <index> finished'
The output will look like
```
log file 1 finished
log file 2 finished
log file 3 finished
log file 4 finished
log file 5 finished
log file 6 finished
log file 7 finished
log file 8 finished
log file 9 finished
...
```

*   By default the log file out of order time is 9s. I considered it useful to include log files created slightly before init_datetime but still have entry lines in the interval. This time should be increased if the number of lines is increased.
It can be set in the aktool/conf.py file

*   Then we can proceed and run our processing script to output:
    *    Hosts that connected to  Hannibal in the last 10 s
    *    Hosts that received connection from Hannibal in the last 10 s
    *    the hostname that generated most connections in the last 10 s

By:

```
python scripts/main.py Hannibal 10
```
'Hannibal' being the hostname and 10 the number of seconds by which the process looks backward and also by which it repeats itself.
So each 10 s it will calculate again.

An output should normally look like:
```
It is :  13:31:58 12/14/20.  the next output is in 10 s. 

Hosts that connected to  Hannibal in the last 10 s are:  {'Hannibal': 1} 

Hosts that received connection from Hannibal in the last 10 s are:  {'Steeve': 3, 'Hanny': 1, 'Hannibal': 1} 

The hostname that generated most connections in the last 10 s is:  {'Hannibal': 5}
```

## Running the tests

*   The test script is in the /tests folder and uses short and long log files to test the tools
To run the tests: 
```
python -m unittest tests/tests.py
```
*   If everything alright this message should pop up:

```
.......
----------------------------------------------------------------------
Ran 7 tests in 0.045s

OK
```
## Some of the links used
https://www.geeksforgeeks.org/python-reversed-vs-1-which-one-is-faster/
https://www.csestack.org/difference-between-sort-sorted-python-list-performance/#:~:text=Sort%20vs%20Sorted%20Performance,-Which%20one%20is&text=Creating%20a%20list%20of%201000000%20integers%20selected%20randomly.&text=Here%2C%20sort()%20method%20is%20executing%20faster%20than%20sorted()%20function.&text=Here%2C%20sorted()%20function%20method,execution%20time%20in%20both%20cases.
https://www.geeksforgeeks.org/python-ways-to-flatten-a-2d-list/

## Authors

* **Anass Khaldi** 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

