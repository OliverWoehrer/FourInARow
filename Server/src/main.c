#include <stdio.h>	// I/O functions
#include <stdlib.h>	// provides exit()
#include <unistd.h>
#include <string.h>	// for string handling
#include <signal.h>
#include <sys/socket.h>
#include <errno.h>

#include "messages.h" // provides formated error messages
#include "socket.h"
//#include "shared.h"
#include "game.h"

#define USAGE_SYNOPSIS "[-p PORT]"

//Message strings:
extern const char *progName; // program name string used in messages.h
extern const char *usageSynopsis; // usage synopsis string used in messages.h

//Signal handling:
struct sigaction sigint_action; // pre-defined struct holding signal config
volatile sig_atomic_t loop = 1;
static void stopLoop();
static void initSignalHandler(int signal, void (*sig_handler)(int), struct sigaction *sa);




int main(int argc, char *argv[]) {
    //Set strings at runtime:
    progName = argv[0]; // set program name
    usageSynopsis = USAGE_SYNOPSIS; // set synopsis string for usage messages
    char status = EXIT_FAILURE; // is set on SUCCESS when terminating successfully at the end 
    debugMessage("Start.");


    //Get program arguments:
    char c;
    char p_flag=0;
    const char *p_opt=NULL; 
    while((c=getopt(argc, argv, "p:")) != -1) {
        switch(c) {
            case 'p':
                p_flag++;
                p_opt = optarg;
                break;
            case '?': // unknown character and default are both invalid
            default:
                usageMessage("Unknown flag option.");
                goto getProgArguments; // clean exit
        }
    }


    //Check program arguments:
    if(argc - optind != 0) usageMessage("Invalid arguments.");
    if(p_flag > 1) usageMessage("Only one port is valid.");
    const char *portName = p_flag ? p_opt : "8080"; // set port number
    unsigned char i = 0;
    while (portName[i] != '\0') { // check for valid port number
        if ('0' <= portName[i] && portName[i] <= '9') { i++; continue; }
        usageMessage("Invalid port string!");
        goto checkProgArguments; // clean exit
    }   


    //Establish socket connection:
    int socketFD = initServer(portName); // socket file descriptor
    if(socketFD < 0) { // error handling
        errorMessage("Failed to establish socket.");
        goto establishSocketConnection; // clean exit
    }


    //Mount shared memory:
    //TODO

    //Create down and up pipes:
    int downPipeFD[2]; // stdin of children, parent --> child 
    int upPipeFD[2]; // stdout of children, parent <-- child
    if (pipe(downPipeFD) == -1 || pipe(upPipeFD) == -1) { // create all pipes
        errorMessage("Failed to create pipes.");
        goto createPipes; // clean exit
    }

    //Initialize signal handler:
    initSignalHandler(SIGINT, stopLoop, &sigint_action);
    initSignalHandler(SIGTERM, stopLoop, &sigint_action);


    //Loop server; wait for incoming request:
    debugMessage("Loop.");
    //while(loop) {
        game_t game = creatGame();
        createRandomGame(&game);
        printBoard(&game);
        goto interrupt;

        /* ORIGINAL PROCESS FLOW :
        //Wait for client connection:
        int connectionFD = accept(socketFD, NULL, NULL);
        if(connectionFD == -1) { // error handling
            if(errno == EINTR)  goto interrupt; // loop again
            errorMessage("Failed to accept connection.");
            goto acceptConnection; // clean exit
        }

        //Fork at new accept:
        //DATA STRUCT = fork();
        if (0 == -1) errorMessage("Failed to fork after accept.");
        else if (0 == 0) { // is child process 
            //Read request:

            //Process new turn:

            //Send response:
        
        } else { // is parent process
            // LOOP AGAIN!
        }
        */

        


        interrupt:/* empty lable */;
    //}
    

    //Terminate program:
    status = EXIT_SUCCESS; // set status, terminated successfully!
    //acceptConnection:
    createPipes:
    //mountSharedMemory:
    establishSocketConnection:
        closeSocket(socketFD);
    checkProgArguments:
    getProgArguments:
        printf("Done.\n");
        exit(status);
}

static void stopLoop() {
    loop = 0;
}

static void initSignalHandler(int signal, void (*sig_handler)(int), struct sigaction *sa) {//Initialize signal handling:
    memset(sa, 0, sizeof(*sa)); // initialize config memory to 0
    (*sa).sa_handler = stopLoop;
    sigaction(signal, sa, NULL); // set sigaction
}