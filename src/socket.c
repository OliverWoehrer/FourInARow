/**
 * @file socket.c
 * @author Oliver Woehrer
 * @date 07.10.2021
 * @brief provides functions for socket communications
 */
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <string.h>
#include "messages.h"

#define CLIENT_MODE 1
#define SERVER_MODE 2

typedef char socket_mode_t;
static struct addrinfo *myAI; // address info struct

static int openSocket(const char *hostName, const char *portName, socket_mode_t mode) {
    //Set hints for connection criteria:
    struct addrinfo hints;
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    if(mode == SERVER_MODE) hints.ai_flags = AI_PASSIVE;

    //Make address info struct:
    int ret = getaddrinfo(hostName, portName, &hints, &myAI);
    if(ret != 0) { // getAddrInfo failed
        fprintf(stderr, " > getaddrinfo failed! %s\n", gai_strerror(ret));
        return -1; // clean up and termination in main
    }

    //Create socket:
    int socketFD = socket(myAI->ai_family, myAI->ai_socktype, myAI->ai_protocol);
    if (socketFD < 0) infoMessage("socket() failed.");

    return socketFD; // could be invalid FD!
}

/**
 * @brief creates a socket and connects as a client to the given address.
 * This function fills the address info struct creates a socket
 * and opens the connection to the given host at the given port. If any
 * of these steps fail, a info message is printed an a negativ value is
 * return. On success the file descriptor of the socket stream is returned
 * @param hostName name of the connection host
 * @param portName name of the connection port
 * @return File descriptor of the socket stream on success, negativ value
 */
int initClient(const char *hostName, const char *portName) {
    //Create socket:
    int socketFD = openSocket(hostName, portName, CLIENT_MODE);
    if(socketFD < 0) { // invalid file descriptor
        infoMessage("Failed to open a socket.");
        return -1;
    }
    //Open connection:
    if(connect(socketFD, myAI->ai_addr,myAI->ai_addrlen) < 0) {
        infoMessage("connection() failed."); // connect returned error code
        return -1;
    }
    return socketFD;
}

/**
 * @brief fills the address info struct creates a socket
 * and binds the socket to the port. If any of these steps fail, a info
 * message is printed an a negativ value is return. On success the file
 * descriptor of the socket stream is returned
 * @param portName name of the connection port
 * @return File descriptor of the socket stream on success, negativ value
 */
int initServer(const char *portName) {
    //Create socket:
    int socketFD = openSocket(NULL, portName, SERVER_MODE);
    if(socketFD < 0) { // invalid file descriptor
        infoMessage("Failed to open a socket.");
        return -1;
    }

    //Allow reuse of address:
    int optval = 1;
    setsockopt(socketFD, SOL_SOCKET, SO_REUSEADDR, &optval,sizeof(optval));
    
    //Open connection:
    if(bind(socketFD, myAI->ai_addr,myAI->ai_addrlen) < 0) {
        infoMessage("bind() failed."); return -1;
    }
    //Mark connection as passiv:
    if(listen(socketFD, 1) < 0) {
        infoMessage("listen() failed."); return -1;
    }

    return socketFD;
}

/**
 * @brief frees the address info struct and closes the
 * file descriptor for the socket connection. On successfull closing 0
 * is returned, -1 otherwise.
 * @param socketFD file descriptor of the socket connection
 * @return On successfull closing 0 is returned, -1 otherwise.
 */
int closeSocket(int socketFD) {
    freeaddrinfo(myAI);
    if(close(socketFD) != 0) {
        errorMessage("close() failed on socket file desciptor.");
        return -1;
    }
    return 0;
}