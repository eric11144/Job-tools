Q               := @
MAKE			:= make

ifeq ($(shell uname), Linux)
	MAKEFILE	:= linux.mk
	CFLAGS		:= -DOS_LINUX	
else
	MAKEFILE	:= freebsd.mk
	CFLAGS		:= -DOS_FREEBSD
	MAKE		:= gmake
endif

export CFLAGS	

all:
	$(Q)$(MAKE) -f $(MAKEFILE)

libs:
	$(Q)$(MAKE) -f $(MAKEFILE) libs

clean:
	$(Q)$(MAKE) -f $(MAKEFILE) clean
	$(Q)rm -f .depend *~ *.bak *.res *.o32 *.o64 a.out*
