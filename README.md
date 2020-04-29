# Nondeterministic-Finite-Automaton-NFA
A working Nondeterministic Finite Automaton(NFA) created in Python 3
_________________

<p align="center">
<b> How the Source is Structured: </b>
</p>

<br>

First line : Initial State(s)
<br>
Second line : Final State(s)
<br>
Other Lines : X Y Z, Where the State X goes to State Y with Value Z<br>

<br>

<b>Example:</b> 
<br>

1 <br>
3 5 6 <br>
1 1 a <br>
1 2 a <br>
1 6 b <br>
2 2 b <br>
2 3 c <br>
2 4 b <br>
4 5 b <br>
<br>
________________


The program takes that information and turns it into a dictionary, such as : {'1': [('1', 'a'), ('2', 'a'), ('6', 'b')], '2': [('2', 'b'), ('3', 'c'), ('4', 'b')], '4': [('5', 'b')]}
<br>



A key is a State that can go to another state, and it's corresponding elements are tuples where the first element represents the State that the 'key' goes to, and the 2nd element is the value of the move.
<br>

________________
<br>
<p align="center">
<b>Visual Representation:</b>
<br>
 <img src="https://i.imgur.com/NZO9GGx.jpg">
 </p>
