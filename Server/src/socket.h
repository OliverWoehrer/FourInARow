/**
 * @file socket.h
 * @author Oliver Woehrer
 * @date 07.10.2021
 * @brief provides functions for socket communications
 */
#ifndef SOCKET_H
#define SOCKET_H

//socket_mode_t CLIENT_MODE = 1;
//socket_mode_t SERVER_MODE = 2;


int initClient(const char *hostName, const char *portName);
int initServer(const char *portName);
int closeSocket(int socketFD);

#endif /* SOCKET_H */