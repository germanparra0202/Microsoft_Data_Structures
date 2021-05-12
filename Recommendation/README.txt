The Recommendation System Directions
The goal of this system is to improve your experience when working in your shell.

Before following the directions listed below, it will be useful to add or append a history 
file that is in the same folder as the below functions.Running ./get_history.py will create
a history.txt file with all of your data from the user's history log, or if that file 
exists, it will simply append an new data to this file. If you'd like to change the name 
of "history.txt", simply enter into the get_history.py file and change the hardcoded name. 

1) Have a directory that contains the following files:
	- initialize.oy
	- login.py
	- login_funcs.py
	- ngram_class.py
	- predict.py
	- get_history.py
	- some sort of history data, this can be multiple files
		- We have provided several history files because they must be formatted with a date
		  and a time. Use any of these files for the history data or add the following
		  to the end of your .bashrc file (accessed from the home directory) to use your
		  own history
			- export HISTTIMEFORMAT="%m/%d/%y %T "
		- If you are using your own history, run 
					history > history.txt
		  to get the file
2) Run the initialization script with the name(s) of the history data following it
	- ./initialize.py file1.txt file2.txt
	a) This will prompt the user to input the name of 3 directories. If the absolute path is
	   not found for the directory, then it will ask the user to input a different one
	b) Once the user has input 3 directories, the script checks the validity of the history
	   files. If there is an issue with the data, then it will state "No valid files provided".
	   If this is displayed, then run the initialization script again but with different 
	   files. It will not prompt the user to input directories again if this is the case.
3) There should now be 2 new text files. One is called directory_data.txt and the other is
   ngram_data.txt
4) Type "pwd" into the command line and copy the response
	- This should be the absolute path to the directory that all the files are stored in
5) Open login.py to edit and paste the absolute path into the line that says "cwd=''"
	- This is on line 19 and right under the comment that says #TODO
6) Edit the .profile file from your home directory and paste the same path from the login.py
   script on a newline. Then put login.py at the end of the path
	- It should look like absolute-path-to-file/login.py
7) Now when the user logs in, the 3 directories will pop-up giving them the option to 
   immediately change to them by inputing a number or skipping it by inputting anything 
   else.
8) To run the mock shell, run predict.py. This will prompt the user to input 2 commands and
   once done, will begin giving a recommendation for the third command
	- use n to skip the command
	- use q to quit the mock shell
	
