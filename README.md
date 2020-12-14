# What's inside?

This is a code challenge, written in the context of the 'Junior Data Operations Engineer' recrutment process at Clarity.ai .
It should be viewed and assessed by the concerned person.

## Files
The repo contains:
*  Folders 
    *  scripts: contains the log generation simulator and the log processing script
    *  aktools: The package containig the processing tools and conf file
    *  tests: containing the tests
    *  data: contains the data source data for the first part and for the tests
    *  output: contains the generated log data
    *  doc: contains a jupyter notebook and its pdf file
    
*  Files
   *   README.md
   *   LICENSE.md
   *   setup.py
   *   .gitignore


## Notes and sssumptions 

*   A unique log file generation should not take more than 5 min
*   Each predefined amount of time log files are processed
*   The logs are in each iteration reduced and sorted by time
*   The processing start with the file that is currently generated
*   The log file are parsed starting from the end (recent values first)
*   By 'hostanem that generated most connections', I considered the involvement  of the host and not him being the source.
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

## Demo

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
It is :  01:54:14 12/14/20.  the next output is in 10 s. 
Hosts that connected to  Hannibal in the last 10 s are:  Counter({'Steeve': 2, 'Hannibal': 1, 'Hanny': 1}) 
Hosts that received connection from Hannibal in the last 10 s are:  Counter({'Hannibal': 1, 'Hanny': 1, 'Steeve': 1}) 
the hostname that generated most connections in the last 10 s is:  [('Hanny', 4)]
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


## Authors

* **Anass Khaldi** 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

