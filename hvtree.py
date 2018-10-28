from tkinter import *;
import sys;

root = Tk();

if (len(sys.argv) != 3):
	message = "Invalid input.\n\n'rfractal.py n',"
	+ " n being the recursion depth.";
	print(message);
	
order = int(sys.argv[1]);
factor = float(sys.argv[2]);
length = 100;
size = 1000;
c_size = 1000;
padding = length/2;

c = Canvas(root, width=c_size, height=c_size);
c.pack();

def grow(x, y, length, order, horizontal, factor):
        if(order == 1):
                return;

        length = length*factor;
        if (horizontal):
                c.create_line(x-length/2, y, x+length/2, y);
                horizontal = False;
                grow(x-length/2, y, length, order-1, horizontal, factor);
                grow(x+length/2, y, length, order-1, horizontal, factor);
        else:
                c.create_line(x, y-length/2, x, y+length/2);
                horizontal = True;
                grow(x, y-length/2, length, order-1, horizontal, factor);
                grow(x, y+length/2, length, order-1, horizontal, factor);

c.create_line(450, 500, 550, 500);
grow(450, 500, 100, order, False, factor);
grow(550, 500, 100, order, False, factor);
print("Completed!");
root.mainloop();
