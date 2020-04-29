# Nondeterministic-Finite-Automaton-NFA-nn
A working Nondeterministic Finite Automaton(NFA) created in Python 3
_________________
<br>
<b> How the Source is Structured: </b>
<br>
First line : Initial State(s)
Second line : Final State(s)

Other Lines : X Y Z, Where the State X goes to State Y with Value Z

Example: 
1
3 5 6
1 1 a 
1 2 a
1 6 b
2 2 b 
2 3 c
2 4 b
4 5 b

________________
<br>

The program takes that information and turns it into a dictionary, such as : {'1': [('1', 'a'), ('2', 'a'), ('6', 'b')], '2': [('2', 'b'), ('3', 'c'), ('4', 'b')], '4': [('5', 'b')]}
