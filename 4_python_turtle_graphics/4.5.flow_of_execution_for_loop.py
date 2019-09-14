# 4.5. Flow of Execution of the for Loop
'''
As a program executes, the interpreter always keeps track of which statement is about to be executed. We call this the control flow, or the flow of execution of the program. When humans execute programs, they often use their finger to point to each statement in turn. So you could think of control flow as “Python’s moving finger”.

Control flow until now has been strictly top to bottom, one statement at a time. We call this type of control sequential. In Python flow is sequential as long as successive statements are indented the same amount. The for statement introduces indented sub-statements after the for-loop heading.

Flow of control is often easy to visualize and understand if we draw a flowchart. This flowchart shows the exact steps and logic of how the for statement executes.

        * Check the 4.5.flow_chart.png image

A codelens demonstration is a good way to help you visualize exactly how the flow of control works with the for loop. Try stepping forward and backward through the program by pressing the buttons. You can see the value of name change as the loop iterates through the list of friends.

'''

for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi " + name + "! Please come to my party on Saturday!")
