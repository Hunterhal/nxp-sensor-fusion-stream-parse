Tested on FRDM K22F_AGM01 shield  
UART Port is COM5 and baudrate is 115200 change according to project needs  
Check user guide of NXP for further information https://www.nxp.com/docs/en/user-guide/NSFK_Prod_UG.pdf   
The packets are created with 0x7E that is '~' character    
Unforunately, start and stop bits are same this increase the work load on receiver side. Also another char canbe used to separate the data, this may increase the packet size and UART is very limited with baudrate  

To-Do List:  



Future:  
Add Qt framework for better visualization  