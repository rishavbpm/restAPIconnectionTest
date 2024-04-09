## Description
The functionality of this program is to test the connection with BPWin REST API server. 
After running the script or opening the built .exe, there will be a GUI showing up. 
There is a "check" button on the GUI, and a log window. 
Open BPWin 8.0.1 and later version, click on this "check", the RestAPIConnectionTest program will make an attempt to call the "/health" endpoint. 
If it succeed, it will return the following json: 

```
{
    "Success": 1,
    "Message": "BPWin is ready."
}
```

Otherwise, it fails, meaning that the BPWin REST API server is not on. 


## Build process
- The python version used for the initial code is 3.8.18.
- Note that this program uses pyinstaller 6.4.0. You will need this to build it into .exe.
- In the cmd line, natigate to the directory with .py file in it, and type this command: 
```pyinstaller --noconsole --onefile RestAPIConnectionTest.py```
