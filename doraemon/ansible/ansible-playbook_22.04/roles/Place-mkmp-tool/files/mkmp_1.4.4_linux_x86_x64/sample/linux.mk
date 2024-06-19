Q               := @
CC				:= $(CROSS_COMPILE)gcc	
SRCS            := $(wildcard *.c)

TARGET_32       := mkmp_32
OBJS_32         := $(SRCS:.c=.o32)
LIBS_32			:= libmkmp_32.a	-lpthread
CFLAGS_32       := -m32 $(CFLAGS) -Wall -I ./include 
LDFLAGS_32      := -m32 $(LIBS_32)

TARGET_64       := mkmp_64
OBJS_64         := $(SRCS:.c=.o64)
LIBS_64			:= libmkmp_64.a -lpthread
CFLAGS_64       := $(CFLAGS) -Wall -I ./include 
LDFLAGS_64      := $(LIBS_64)

LIB_PACKAGE		:= ../library/

ifeq ($(shell uname -m), i686)
	TARGET		:= $(TARGET_32)
else ifeq ($(shell uname -m), x86_64)
	TARGET		:= $(TARGET_64)
endif

ifeq ($(OS), all)
	TARGET		:= $(TARGET_32) $(TARGET_64)   
endif

.PHONY: all clean

all: $(DEPEND) $(TARGET)

%.o32: %.c Makefile
	$(Q)echo "  Compiling '$<' ..."
	$(Q)$(CC) $(CFLAGS_32) -o $@ -c $<

%.o64: %.c Makefile
	$(Q)echo "  Compiling '$<' ..."
	$(Q)$(CC) $(CFLAGS_64) -o $@ -c $<

$(TARGET_32): $(OBJS_32)
	$(Q)echo "  Building '$@' ..."
	$(Q)$(CC) -o $@ $(OBJS_32) $(LDFLAGS_32)

$(TARGET_64): $(OBJS_64)
	$(Q)echo "  Building '$@' ..."
	$(Q)$(CC) -o $@ $(OBJS_64) $(LDFLAGS_64)

libs:
	$(Q)echo "  Generating 'LIBs' ..."	
	@for i in $(LIB_PACKAGE); do\
		(cd $$i && make);\
	done

	$(Q)cp $(LIB_PACKAGE)*.a .
	$(Q)cp $(LIB_PACKAGE)*.so .
	$(Q)cp $(LIB_PACKAGE)include/*.h ./include/.

clean: 
	$(Q)echo "  Cleaning '$(TARGET_32)' ..."
	$(Q)rm -f .depend *~ $(OBJS_32) $(TARGET_32) a.out*
	$(Q)echo "  Cleaning '$(TARGET_64)' ..."
	$(Q)rm -f .depend *~ $(OBJS_64) $(TARGET_64) a.out*

$(DEPEND) dep depend:
	$(Q)echo "  Generating '$@' ..."
	$(Q)$(CC) $(CFLAGS_32) -M *.c > $@
	$(Q)$(CC) $(CFLAGS_64) -M *.c > $@

ifeq ($(DEPEND), $(wildcard $(DEPEND)))
    include $(DEPEND)
endif
