# Flappy_bird_game
Flappybird game using python and the pygames module. Has additional features like saving, settings, and achievements. 


## How To Play ##
After clicking the 'Play Game' button, the tutorial screen will begin. Depending on the keybind (Default is 'space'), the user must press that button to start the actual game. As the bird travels, pipes will spawn and the user must guide the bird between the opening in the pipe. As the user progresses, they will recieve achievements based on certain criteria (see scorescreen for criteria). Afer a collision with either the pipes, the ground, or the roof, the game will end and the gameover screen will appear. Here the user can choose to restart or return back to the main. 


## Game Files Overview ##
The main loop is within the file __Flappy_Main.py__. Background logic to change the screens is housed within the __Flappy_Background.py__ file. All code files start with the prefix __Flappy__ and are within the the folder _Python Files_. If a file contians screen code, it is called __Flappy_Background__SCREEN-NAME.py__. Additional files for the game are called __Flappy_NAME__.py. The images folder contains four subfolders: Achiv, Buttons, Driver, and Numbers. 
- _Python Files_ Folder: Contains .py files that run the game. 
- _Achiv_ Folder: Contains .PNG pictures of achievements. 
- _Buttons_ Folder: Contains .PNG pictures of buttons and a .ttf file for text.
- _Driver_ Folder: Contains .PNG pictures of all main pictures for the game, such as background, bird, and logos.
- _Numbers_ Folder: Contains .PNG pictures of numbers 0-9.

![Flowchart](/README%20Images/flowchart.png)


## Screen Overviews ##
- __Start Screen__: Landing screen when the program opens. Contains the 'Play Game', 'Settings', and 'Scores' buttons. 
- __Tutorial Screen__: A bird will appear and oscillate on the screen. The user must press the binded jump key for the game to begin. Depending on when the user presses to jump, that is the position that the bird will start in. 
- __Game Screen__: This is the screen where the game is played. The user must dodge the pipes and increase their scores. Score can be seen at the top of the screen in front of the pipes while achievements are displayed at the top left corner. 
- __Gameover Screen__: After a collision is detected, the gameover screen will be displayed. This screen allows the user to restart and play again with same settings or go back to the menu.
- __Settings Screen__: Screen allows user to change the hitbox, jump key, gravity, animations, and bird type. The hitbox option has options Default (just bird), Default Box (bird in the from of a box), and Transform Box (more advanced hitbox that changes based on angle and direction). The jump key allows user to change the key used to jump during the game. Gravity allows user to change gravity coefficient during game. Animations is a on or off option whether the user wants to see animations between screens. Bird type allows user to change the bird type used for game. The two buttons at the bottom right, settings and game data, allow user to reset settings and saved game data, respectively. 
- __Score Screen__: Screen for where the user can see their 3 most recent games, average statistics, and global statistics. The next pages (2-4) allow the user to see their achievements and progress within them. Progress bars are below the achievements and descriptions are to the right. 

## Images Within Games ##
![Start Screen](/README%20Images/StartScreen.PNG)
![Start Screen](/README%20Images/TutorialScreen.PNG)
![Start Screen](/README%20Images/GameScreen.PNG)
![Start Screen](/README%20Images/GameoverScreen.PNG)
![Start Screen](/README%20Images/SettingsScreen.PNG)
![Start Screen](/README%20Images/ScoreScreen.PNG)
![Start Screen](/README%20Images/AchievementScreen.PNG)
