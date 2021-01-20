CC = gcc
DEFS = -D_DEFAULT_SOURCE -D_POSIX_C_SOURCE=200809L
CFLAGS = -Wall -g -std=c99 -pedantic $(DEFS)

NAME = test

.PHONY: all clean

all: $(NAME)

$(NAME): $(NAME).o
	$(CC) $(LDFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

$(NAME).o: $(NAME).c

clean:
	rm -rf *.o $(NAME)