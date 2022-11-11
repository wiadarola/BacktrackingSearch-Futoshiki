# ai_project2
<h3>Futoshiki Solver Using Backtracking-Search</h3>

Uses an input file with an initial and desired state to solve a futoshiki puzzle.<br><br>
<h3>Output is of the form:</h3>


<h3>Sample Input</h3>
0 0 0 0 0 0<br>
3 0 0 0 0 0<br>
0 3 0 0 6 4<br>
0 0 0 0 4 0<br>
0 0 0 0 0 0<br>
0 0 0 0 1 3<br><br>

0 0 > 0 0<br>
0 0 0 0 0<br>
0 0 0 0 0<br>
0 0 0 < 0<br>
0 > 0 0 ><br>
\> 0 0 0 0<br>

v 0 0 0 0 0<br>
0 0 0 0 0 0<br>
0 0 0 ^ 0 0<br>
0 0 0 0 0 ^<br>
v 0 0 0 0 0<br>

<h3>Sample Output</h3>
4 6 3 1 2 5 <br>
3 1 2 4 5 6 <br>
1 3 5 2 6 4 <br>
2 5 6 3 4 1 <br>
6 4 1 5 3 2 <br>
5 2 4 6 1 3
