#pull in ROOT
ROOT_INCLUDES='root-config --cflags'
ROOT_ALL='root-config --cflags --libs'

#compiler
CC=g++ -g -02
CC11=${CC} -std=gnu++0x
CCC=${CC} -c

all: Sean

Sean: scanning.cpp 
	${CC} \
	${ROOT_ALL} \
	-o scanning.exe \
	scanning.cpp

