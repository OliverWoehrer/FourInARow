CC = gcc
DEFS = -D_BSD_SOURCE -D_SVID_SOURCE -D_DEFAULT_SOURCE -D_POSIX_C_SOURCE=200809L
CFLAGS = -Wall -g -std=c99 -pedantic $(DEFS)
LDFLAGS = -lm

SERVER_OBJECTS = src/main.o src/game.o src/messages.o src/socket.o

.PHONY: all clean
all: server

server: $(SERVER_OBJECTS)
	$(CC) $(LDFLAGS) -o $@ $^

%.o: %.c %.h
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -rf src/*.o server