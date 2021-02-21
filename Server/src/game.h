/**
* @file game.h
* @author Oliver Woehrer
* @date 20.02.2021
* @brief This module provides functions for processing the game.
*/

//Size of game board:
#define COL (7) // max range 0...255
#define ROW (6) // max range 0...255
typedef unsigned char range_t; // max size of gameboard

typedef struct { // holds all game info for each game
    unsigned int gameID;
    char board[COL][ROW];
    range_t target[COL]; // holds the possible coordinates for each row
    range_t move[2]; // lastMove[0]=col lastMoce[1]=row
    char token[2]; // holds token symbols as ASCII character
    unsigned char player; // holds the token of the player at turn
} game_t;

typedef enum {
    N, NE, E, SE, S, SW, W, NW
} direction_t;

game_t creatGame();
int isValidMove(game_t *g);
void placeToken(game_t *g);
void printBoard(game_t *g);
int hasWon(game_t *g);
void createRandomGame(game_t *game);