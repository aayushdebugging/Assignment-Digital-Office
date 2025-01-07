ISRO Rover Movement Simulator
A Python program simulating the navigation of robotic rovers on a rectangular plateau as per the specifications of ISRO's rover deployment on the Moon. This was developed as part of an internship assignment to process rover movements based on user input and compute their final positions and directions.

Features
Navigate rovers on a rectangular grid plateau.
Accept user input for plateau dimensions, rover starting positions, and movement commands.
Process commands (L, R, M) to rotate or move the rover.
Handle multiple rovers sequentially.
Validate inputs and ensure boundary constraints are met.
How It Works
Input:

Plateau dimensions (upper-right coordinates).
Rover's starting position in the format x y D (where D is one of N, E, S, W).
Movement commands as a string of L, R, and M:
L: Rotate the rover 90° left (counterclockwise).
R: Rotate the rover 90° right (clockwise).
M: Move the rover forward in its current direction.
Output:

The final position and direction of each rover after processing all commands.
Logic:

For each rover, calculate the new position and direction based on the commands while ensuring the rover remains within the bounds of the plateau.
