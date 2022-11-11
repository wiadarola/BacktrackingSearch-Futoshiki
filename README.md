# ai_project2
<h3>Futoshiki Solver Using Backtracking-Search</h3>
"Futoshiki is played on a square grid. The objective is to place the numbers such that each row and column contains only one of each digit. Some digits may be given at the start. Inequality constraints are initially specified between some of the squares, such that one must be higher or lower than its neighbor. These constraints must be honored in order to complete the puzzle" (Wikipedia).<br>
Uses an input file with an initial and desired state to solve a futoshiki puzzle.<br>

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

<br><h3>Futoshiki Example</h3>
![image](https://user-images.githubusercontent.com/91436116/201365407-4cc5a94e-1ab1-4a58-9dcf-2ab86c5cde83.png)<br>
![image](https://user-images.githubusercontent.com/91436116/201365450-a1f1e6b1-6fe4-4d7d-8f2a-c3c0a54a2a42.png)

