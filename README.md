Tested on FRDM K22F_AGM01 shield  
UART Port is COM5 and baudrate is 115200 change according to project needs  
Check user guide of NXP for further information https://www.nxp.com/docs/en/user-guide/NSFK_Prod_UG.pdf   
The packets are created with 0x7E that is '~' character    
Unforunately, start and stop bits are same this increase the work load on receiver side. Also another char could be used to separate the data, this may increase the packet size and UART is very limited with baudrate  
Since devs follow this route page 71 and 72 are showing how to parse the data  
  
Remarks:   
    1) Stream coming continously from the port  
    2) Port read function reads given number of data  
    3) The packet that is read may contaion "....~~...~~...." or "~.....~~.....~~" or "~~.....~~...." the contionus reading must be done  
    4) Avoiding previous byte or next byte is important for robustness (may give unindex error)  
    5) Since 0x7E = '~' is used for start and termination. 0x7E is coded as 0x7D and 0x5E and 0x7D is coded as 0x7D and 0x5D
    6) Step 5 eliminates the fixed packet size it cannot be used  
    7) Instead a small finite state machine like code can be used 

To-Do List:  
Add other packets  

Future:  
Add Qt framework for better visualization  