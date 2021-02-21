/**
* @file game.c
* @author Oliver Woehrer
* @date 20.02.2021
* @brief This module provides functions for processing the game.
*/

#include <stdio.h>	// I/O functions
#include <stdlib.h>	// provides exit()
#include <time.h>
#include "game.h"

/**
 * @brief Creates a new game struct and sets all the default values
 * @return newly created game struct
 */
game_t creatGame() {
    static unsigned int gid = 1; // game ID
    game_t new;
    new.gameID = gid;
    for (range_t col = 0; col < COL; col++) { // fill board
        new.target[col] = 0;
        for (range_t row = 0; row < ROW; row++) {
            new.board[col][row] = ' ';
        }
    }
    new.token[0] = 'O';
    new.token[1] = 'X';
    new.player = 0;
    return new;
}


/**
 * @brief Checks if the latest move is valid
 * @param game game struct containing the gameboard and latest move
 * @return 1 if the lastest move is valid, 0 otherwise
 */
int isValidMove(game_t *g) {
    if (g->move[0] < COL &&
        g->move[1] < ROW &&
        g->move[1] == g->target[g->move[0]])
    { return 1; } // is valid
    return 0;
}


/**
 * @brief Playes the token of the latest move into the actual game board
 * @param game game struct containing the gameboard and latest move 
 * @warning latest move needs to be checked!
 */
void placeToken(game_t *g) {
    g->board[g->move[0]][g->move[1]] = g->token[g->player]; // place token of player at turn
    g->target[g->move[0]]++; // increment target array
}


/**
 * @brief Prints the current game board to the console
 * @param g game struct to be printed 
 */
void printBoard(game_t *g) {
    for (range_t r = ROW; r > 0; r--) {
        printf("[%d] ",r-1);
        for (range_t c = 0; c < COL; c++) {
            printf("| %c ", g->board[c][r-1]);
        }
        printf("|\n");
    }
}

static int streak(game_t *g, range_t c, range_t r, direction_t dir) {
    switch (dir) {
        case N:
            r++;
            break;
        case NE:
            c++; r++;
            break;
        case E:
            c++;
            break;
        case SE:
            c++; r--;
            break;
        case S:
            r--;
            break;
        case SW:
            c--; r--;
            break;
        case W:
            c--;
            break;
        case NW:
            c--; r++;
            break;
        default:
            break;
    } // moved to new index
    if (c >= COL || r >= ROW) { return 0;}
    if (g->board[c][r] != g->token[g->player]) { return 0; }
    int ret = streak(g, c, r, dir);
    return 1 + ret;
}


/**
 * @brief checks if the last move has lead to a win
 * @param g game struct
 * @return 1 if win, 0 if no win is detected, -1 if an invalid token was found
 */
int hasWon(game_t *g) {
    if (g->board[g->move[0]][g->move[1]] == g->token[g->player]) {
        int horizont = streak(g,g->move[0],g->move[1],E) + streak(g,g->move[0],g->move[1],W);
        int diag1 = streak(g,g->move[0],g->move[1],NE) + streak(g,g->move[0],g->move[1],SW);
        int diag2 = streak(g,g->move[0],g->move[1],NW) + streak(g,g->move[0],g->move[1],SE);
        int south = streak(g,g->move[0],g->move[1],S);
        if ( horizont >= 3) return 1;
        if ( diag1 >= 3) return 1;
        if ( diag2 >= 3) return 1;
        if ( south >= 3) return 1;
        g->player = (g->player+1) & 1; // no win, change player at turn
        return 0;
    } else { // last move is not player at turn
        return -1; // invalid game status
    }
}


/**
 * @brief creates a random game status
 * @param g game struct
 */
void createRandomGame(game_t *g) {
    srand(time(NULL));   // Initialization, should only be called once.
    unsigned int l = 20;
    do { // loop until on player has won
        l--;
        int col;
        do { // make random move (if valid)
            col = rand() % COL; // Returns a pseudo-random integer between 0 and RAND_MAX.
            g->move[0] = col; 
            g->move[1] = g->target[col]; 
        } while (!isValidMove(g));
        placeToken(g);
    } while (!hasWon(g));
    printf("last move: [%d][%d]=%c\n",g->move[0],g->move[1],g->token[g->player]);
}