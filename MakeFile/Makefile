CC = gcc
CFLAGS = -Wall -g
#LFLAGS = -L/./lib
LIBS = -lm

IDIR = ./include
INCLUDES = -I$(IDIR)
OUT_DIR = ./obj
SRC_DIR = ./src

SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(SRCS:.c=.o)
DEPS = $(wildcard $(IDIR)/*.h)

TARGET = helloworld

.PHONY: depend clean

all:	$(TARGET)
	@echo Simple helloworld makefile created by Andrei

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(INCLUDES) -o $(TARGET) $(OBJS) $(LFLAGS) $(LIBS)
	@mv $(SRC_DIR)/*.o $(OUT_DIR)/

.c.o: %.c
	$(CC) $(CLFAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -f $(OUT_DIR)/*.o $(TARGET)
	@echo Cleaning the makefile created by Andrei

depend: $(SRCS)
	makedepend $(INCLUDES) $^

# keep this line don't erase
