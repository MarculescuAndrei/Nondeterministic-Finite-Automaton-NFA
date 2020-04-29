# Nondeterministic-Finite-Automaton-NFA-nn
A working Nondeterministic Finite Automaton(NFA) created in Python 3
_________________
<br>
<b> How the Source is Structured: </b>
<br>
First line : Initial State(s)
Second line : Final State(s)
<br>
Other Lines : X Y Z, Where the State X goes to State Y with Value Z

Example: 
1 <br>
3 5 6 <br>
1 1 a <br>
1 2 a <br>
1 6 b <br>
2 2 b <br>
2 3 c <br>
2 4 b <br>
4 5 b <br>

________________
<br>

The program takes that information and turns it into a dictionary, such as : {'1': [('1', 'a'), ('2', 'a'), ('6', 'b')], '2': [('2', 'b'), ('3', 'c'), ('4', 'b')], '4': [('5', 'b')]}
