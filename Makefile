# Makefile for the FEEG6003 coursework

#
# C compiler and options for system
#
CC=	cc
CFLAGS=-O3
LIB= -lm

SRCS=$(wildcard loop*.c)
EXCS=$(patsubst %.c,%,$(SRCS))
all: $(EXCS)

#
# Compile
#
% : %.c
	$(CC) $(CFLAGS) -o $@ $< $(LIB)
#
# Clean out object files and the executable.
#
clean:
	rm $(EXCS)

