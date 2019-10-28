# 15.4 Layout Mangers
'''
A widget will not be visible in a window until you assign it a size and location within it’s parent widget. Assigning a specific size and location to every widget is tedious and error-prone. In addition, the desired behaviour for most GUI interfaces is that the widgets resize and relocate in reasonable ways if their parent window is re-sized. Trust me, you don’t what to write code to resize and relocate widgets every time you develop a GUI program! Therefore, layout managers are included in the Tkinter module to do this work for you. You just have to give some basic positioning information to a layout manager so it can calculate a position and a size for each widget.

There are three layout managers in the Tkinter module:

Layout Manager      Description

place               You specify the exact size and position of each     
                    widget.

pack                You specify the size and position of each widget 
                    relative to each other.

grid                You place widgets in a cell of a 2-dimensional table 
                    defined by rows and columns.

You should never mix and match these layout managers. Use only one of
them for the widget layout within a particular “parent widget”.
(Widgets are organized in a hierarchy, which is explained in the
next lesson.)

'''

# 15.15.1. Summary
'''
To summarize, let’s review two very important rules:

A widget will not be visible in a window until you assign it a size and
location within it’s parent widget.

You should never mix and match layout managers; use only one type of
layout manager for the widgets within a particular parent widget.

You have attempted 1 of 1 activities on this page.
'''

