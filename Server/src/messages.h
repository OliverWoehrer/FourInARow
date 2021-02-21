/**
* @file messages.h 
* @author Oliver Woehrer
* @date 14.11.2020
* @brief This module provides functions to print out messages for the user.
*/
#ifndef MESSAGES_H
#define MESSAGES_H

const char* progName; // name of the executable, should be set in main at runtime
const char* usageSynopsis; // string of the usage synopsis, set at runtime
char debug;


void infoMessage(const char* msg);
void errorMessage(const char *msg);
void usageMessage(const char* msg);
void debugMessage(const char *msg);

#endif /* MESSAGES_H */