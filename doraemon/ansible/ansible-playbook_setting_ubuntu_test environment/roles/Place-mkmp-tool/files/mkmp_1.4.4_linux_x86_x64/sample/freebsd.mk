Q           := @
CC          := $(CROSS_COMPILE)gcc
SRCS        := $(wildcard *.c)
OBJS		:= $(SRCS:.c=.o)
TARGET		:= mkmp
LIBS		:= -lpthread -lcam libmkmp.a
CFLAGS		:= -Wall -I ./include
LDFLAGS		:= $(LIBS) -static
LIB_PACKAGE	:= ../library/

.PHONY: all clean distclean

all: .depend $(TARGET)

%.o: %.c Makefile
	$(Q)echo "  Compiling '$<' ..."
	$(Q)$(CC) $(CFLAGS) -o $@ -c $<

$(TARGET): $(OBJS)
	$(Q)echo "  $(COLOR_G)Building '$@' LIB VER=$(LIB_VER) ...$(COLOR_W)"
	$(Q)$(CC) -o $@ $(OBJS) $(LDFLAGS)

clean distclean: 
	$(Q)echo "  Cleaning '$(TARGET)' ..."
	$(Q)rm -f .depend *~ *.a $(OBJS) $(TARGET)

libs:
	$(Q)echo "  Generating 'LIBs' ..."	
	@for i in $(LIB_PACKAGE); do\
		(cd $$i && gmake);\
	done

	$(Q)cp $(LIB_PACKAGE)/*.a .
	$(Q)cp $(LIB_PACKAGE)/include/*.h ./include/.

.depend dep depend:
	$(Q)echo "  Generating '$@' ..."
	$(Q)$(CC) $(CFLAGS) -M *.c > $@

ifeq (.depend, $(wildcard .depend))
    include .depend
endif

