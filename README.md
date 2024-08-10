# Simulation of Newton's Law of Universal Gravitation
Welcome to the Simulation of Newton's Law of Universal Gravitation project! This application simulates the gravitational force between masses using Newton's law of universal gravitation. It employs a Linear Congruential Generator (LCG) algorithm to generate pseudo-random values for variables such as the distance between objects, mass of the object, and starting position of objects. This README file will guide you through the setup, usage, and features of the project.

## Table of Contents
- [Features]($Features)
- [Installation]($Installation)
- [Notes]($Notes)
- [Screenshots]($Screenshots)
- [Contributing]($Contributing)

## Features
- <b>Simulation of Gravitational Force</b>: Simulates the gravitational force between masses based on Newton's law of universal gravitation.
- <b>Pseudo-Random Variable Generation</b>: Uses LCG algorithm to generate pseudo-random values for the radius, mass, and distance between masses.
- <b>Pygame Window</b>: Pygame library is used to demonstrate the simulation.

## Installation
1- Clone the repositry:
  ```
    git clone https://github.com/yourusername/Gravity-Simulator.git
  ```
2- Navigate to the project directory:
```
  cd Gravity-Simulator
```
3- Run Force8.3.py file ( Make sure you installed appropriate libraries and dependencies) 

Enjoy!

## Notes
- Newton's Law of Universal Gravitation: The formula used for calculating the gravitational force is:
  
  ```math
  F = G \frac{m_1 \cdot m_2}{r^2}
  ```
  where 𝐹 is the gravitational force, 𝐺 is the gravitational constant, 𝑚1 and 𝑚2 are the masses, and 𝑟 is the distance between the centers of the masses.

- <b>LCG Algorithm</b>: The LCG algorithm used for generating pseudo-random values follows the formula
  ```math
       X_{n+1} = (aX_n + c) \mod m
  ```
  where 𝑎, 𝑐, and 𝑚 are constants, and 𝑋 is the sequence of pseudo-random values.

## Screenshots
Here we have 20 balls attracting each other ( time is acclerated in order show effects of objects attracting each other! ) 
![8-10-2024 (18-36-37)](https://github.com/user-attachments/assets/290789ee-5039-4a77-a91f-c25eec352b5a)

## Contributing
Contributions are welcome! To contribute to this project, follow these steps:
1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature/your-feature).
6. Open a Pull Request.
Please ensure your code adheres to the project's coding standards and include relevant tests.

Thank you for using the Simulation of Newton's Law of Universal Gravitation! If you have any questions or need further assistance, feel free to open an issue on the GitHub repository. Enjoy exploring the wonders of gravity!
