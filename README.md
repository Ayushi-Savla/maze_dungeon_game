# MAZE DUNGEON GAME USING PYTHON

![Screenshot 2024-12-05 235535](https://github.com/user-attachments/assets/8eed82b1-99a8-47e4-8608-787ce82302b7)

# What it does
This is a simple maze game where the player controls an animated person. They navigate through the maze as they collect different collectibles/treasures. When all collectibles/treasures have been collected, it transitions to the next level. Once all the levels have been completed within the 1 minute time duration, the game ends. The player's score is constantly updated as they collect the treasures.
# Dependencies
To build this game, the following dependencies were used:
  1. Turtle to generate the player and the maze.
  2. Random to randomise the enemy movements.
  3. Math to calculate position of the player as well as to calculate collisions.
# Installation and Running
The game created can be created or installed through the following procedure:
  1. Download the latest version of Python onto your machine. This can be done from this link: [Download Python](https://www.python.org/downloads/). It is applicable for both Windows/MacOS systems.
  2. Once the downloaded file is completely downloaded, click on it to execute the file which will install the Python program on the machine.
  3. Once the installation is complete, to verify that Python downloaded successfully, navigate to the command prompt/terminal and type the following command: `python --version` which will display the version of python downloaded.
  4. To run a test to see if it installed properly, use the following:
     ```
     py
     print("Hello World!")
     ```
     It should return the output: *Hello World!*
  5. In the navigation window/bar, search for the IDLE Shell which is downloaded together with other Python modules. Click on it to open it and you can run the same command above to test if it is working.
  6. Ensure to have Git downloaded to clone the repository from GitHub. [Download Git](https://git-scm.com/downloads)
  7. Clone the repository using this link: [Maze Dungeon Python Game](https://github.com/Ayushi-Savla/maze_dungeon_game) or directly from a terminal/command line using the commands: 
     ```
     git clone https://github.com/Ayushi-Savla/maze_dungeon_game.git
     cd maze_dungeon_game
     ```
  8. **Install the dependencies** using the `pip` command from any python editor like Pycharm or directly from a command line terminal. In our case, we made use of the following dependencies:
     ```
     pip install turtle
     pip install random
     pip install math
     pip install pygame
     ```
  9. Once your environment is set, with all the dependencies and the files downloaded, run the command `python main.py` to run the main script. If using an IDE like Pycharm or Visual Studio, once you have cloned the repository, just run the main file from the IDE by clicking the **run** button.
