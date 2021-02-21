/**
* @file messages.c
* @author Oliver Woehrer
* @date 14.11.2020
* @brief This module provides functions to print out messages for the user.
*/

#include "messages.h"
#include <stdio.h>	// I/O functions
#include <stdlib.h>	// provides exit()
#include <unistd.h>     // provides process ID
#include <string.h>	// for string handling
#include <errno.h>	// to use errno

char debug = 1;

/**
 * @brief This function prints the given message to the stderr stream
 * after adding a LF character to the end. It should be called as an error
 * occures. e.g when the return value of a function is invalid
 * @param msg Message to be printed
 */
void infoMessage(const char *msg) {
        fprintf(stderr, " > %s\n", msg);
}


/**
 * @brief prints the given message and a detailed error message acoording to the
 * global error code provided by errno.h. Adds a prefix [ERROR <progName>] before
 * the given message. Should only be called in main function and at last before
 * exiting the program.
 * @param msg massage to be printed
 */
void errorMessage(const char *msg) {
	fprintf(stderr, "[ERROR %s] %s %s\n", progName, msg, strerror(errno));
}

/**
 * @brief prints a (usages) message depending on the given string.
 * The program exits with an non-zero return code after the usage messages has been printed.
 * A pre-fix '[INFO <progName>] Usage: <progName>' is added at the beginning of the message
 * as well as a line feed character is added to the message.
 * @param msg message to be printed
 */
void usageMessage(const char* msg) {
        fprintf(stderr, "%s\nUSAGE: %s %s\n", msg, progName, usageSynopsis);
        exit(EXIT_FAILURE);
}

/**
 * @brief prints the given debug message and formates the message by adding the program
 * name as well at the current process ID at the start of the line. A LF is added to
 * the end of the string.
 * @warning can enabled/disabled by setting the 'debug' variable
 */
void debugMessage(const char *msg) {
        if (debug) fprintf(stderr, "[DEBUG %s(%d)] %s\n", progName, getpid(), msg);
}