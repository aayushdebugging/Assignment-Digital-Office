# ISRO Rover Movement Simulator

A Python program simulating the navigation of robotic rovers on a rectangular plateau as per the specifications of ISRO's rover deployment on the Moon. This was developed as part of an internship assignment to process rover movements based on user input and compute their final positions and directions.

---

## Features
- Navigate rovers on a rectangular grid plateau.
- Accept user input for plateau dimensions, rover starting positions, and movement commands.
- Process commands (`L`, `R`, `M`) to rotate or move the rover.
- Handle multiple rovers sequentially.
- Validate inputs and ensure boundary constraints are met.

---

## How It Works

### **Input**
1. **Plateau Dimensions**: Upper-right coordinates defining the plateau.
2. **Rover's Starting Position**: 
   - Format: `x y D` 
   - `x` and `y` are coordinates, `D` is the direction (`N`, `E`, `S`, `W`).
3. **Movement Commands**: A string of `L`, `R`, and `M`:
   - `L`: Rotate the rover 90° left (counterclockwise).
   - `R`: Rotate the rover 90° right (clockwise).
   - `M`: Move the rover forward in its current direction.

---

### **Output**
- The final position and direction of each rover after processing all commands.

---

### **Logic**
1. **Plateau Setup**:
   - Define the boundaries of the rectangular plateau.
2. **Command Processing**:
   - For each rover:
     - Parse the starting position and commands.
     - Execute the commands to calculate the rover's new position and direction.
3. **Movement Constraints**:
   - Ensure the rover remains within the bounds of the plateau.
4. **Result**:
   - Output the final coordinates and direction for each rover.


