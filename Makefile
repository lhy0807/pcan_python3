############################################################################
#			Copyright (c) 2014 Robotnik Automation, SLL	   #
#			    				  		   #
############################################################################
EXE			= _pcan_module.so
BUILD		     	= ./build/
LIBDIR			= ./lib/
SRC			= ./src/
PYTHONDIR		= ./pcan_python/
LIBS			= -lpcan
INC			= -I/usr/include/python3.8 -I/usr/include -I/opt/ros/noetic/include/libpcan
INSTALLDIR		= /usr/lib


SWIG			= swig
SWIGFLAGS		= -python
CPP		        = gcc
CCFLAGS	         	= -c -fpic 
MAKE			= make
LD			= ld
LDFLAGS			= -share -L/opt/ros/noetic/lib/
MKDIR_P 		= mkdir -p

OBJECTS =	\
			$(BUILD)pcan_module.o \
			$(BUILD)pcan_module_wrap.o


default: $(LIBDIR)$(EXE)


$(BUILD)pcan_module.o : $(SRC)pcan_module.c
	${MKDIR_P} $(BUILD)
	$(CPP) $(CCFLAGS) $(INC) -o $(BUILD)pcan_module.o $(SRC)pcan_module.c

$(BUILD)pcan_module_wrap.o : $(SRC)pcan_module.i
	${MKDIR_P} $(BUILD)
	$(SWIG) $(SWIGFLAGS) $(INC) -o $(SRC)pcan_module_wrap.c -outdir $(PYTHONDIR) $(SRC)pcan_module.i 
	$(CPP) $(CCFLAGS) $(INC) -o $(BUILD)pcan_module_wrap.o $(SRC)pcan_module_wrap.c


$(LIBDIR)$(EXE) : $(OBJECTS)	
	${MKDIR_P} $(LIBDIR)
	ld $(LDFLAGS) $(LIBS) $(OBJECTS) -o $(LIBDIR)$(EXE)

clean:
	rm -fv $(BUILD)*.o
	rm -fv $(LIBDIR)$(EXE)
	rm $(PYTHONDIR)pcan_module.py $(SRC)pcan_module_wrap.c

install:
	$(MAKE);
	cp $(LIBDIR)$(EXE) $(INSTALLDIR);
	python3 setup.py install

