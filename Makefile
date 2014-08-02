# This file is not needed to compile the external modules. The preferred way to
# build the module is with distutils. Run one of the following commands:
#  - setup.py build_ext  # Just build extenal modules
#  - setup.py test       # Build external modules 'in place' and run testsuite
#  - setup.py install    # Build external modules and install package
#
CC=gcc
RM=rm -vf
CFLAGS=-Wall -Werror -fpic
TARGET=cmath.so

default: $(TARGET)

%.so: %.o
	$(CC) -shared -o $@ $+

%.o: %.c
	$(CC) -c $(CFLAGS) $+

clean:
	@$(RM) *.o *.so

