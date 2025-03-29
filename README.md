# About the project
This is a Killing Fever Online fork of [WinTheGame by Happy Backwards](https://happybackwards.itch.io/win-the-game) [(lemmasoft forum topic)](https://lemmasoft.renai.us/forums/viewtopic.php?t=25603) licensed under [Creative Commons Attribution-NonCommercial](http://creativecommons.org/licenses/by-nc/4.0/). This fork intends to fix bugs, expand character interactions, additional content, add features, and more!

# [DOWNLOAD!](https://github.com/Crystalwarrior/WinTheGame-KFO/releases/latest)

# For Developers:
You need to use the [Renpy 6.17 SDK]([url](https://www.renpy.org/release/6.17)) to work on this project!
This is also my first time using Renpy, and this project also uses [dse-event-dispatcher](https://github.com/renpy/dse/blob/master/game/dse-event_dispatcher.rpy) which hasn't been updated in **6 years**. If anyone intends to upgrade this project to newer releases of Renpy, you'd have to figure out how to adapt all the code to work with the latest builds of Renpy.

# Basic Help
-----------------------------------------------------------------------------------------------------

To advance through the game, `left-click` or press the `space` or `enter` keys. When at a menu, `left-click` to make a choice, or use the arrow keys to select a choice and `enter` to activate it.

## Game Menu

When playing a game, `right-click` or press the `escape` key to enter the game menu. The game menu gives the following choices:

### Return

Returns to the game.

### Save Game

Allows you to save a game by clicking on a save slot.

### Load Game

Allows you to load a game by clicking on a save slot. Clicking on "Auto" accesses the automatic save slots.

### Preferences

Changes the game preferences (options/configuration):

#### Display

Switches between fullscreen and windowed mode.

#### Transitions

Controls the display of transitions between game screens.

#### Text Speed

Controls the rate at which text displays. The further to the right this slider is, the faster the text will display. All the way to the right causes text to be shown instantly.

#### Joystick

Lets you control the game using a joystick.

#### Skip

Chooses between skipping messages that have been already seen (in any play through the game), and skipping all messages.

#### Begin Skipping

Returns to the game, while skipping.

#### After Choices

Controls if skipping stops upon reaching a menu.

#### Auto-Forward Time

Controls automatic advance. The further to the left this slider is, the shorter the amount of time before the game advances. All the way to the right means text will never auto-forward.

#### Music, Sound, and Voice Volume

Controls the volume of the Music, Sound effect, and Voice channels, respectively. The further to the right these are, the louder the volume.

### Main Menu

Returns to the main menu, ending the current game.

### Help

Shows this help screen.

### Quit

Exits the game; the game will be closed and ended.

## Key and Mouse Bindings

### Left-click, Enter

Advances through the game, activates menu choices, buttons, and sliders.

### Space

Advances through the game, but does not activate choices.

### Arrow Keys

Selects menu choices, buttons, and sliders.

### Ctrl

Causes skipping to occur while the ctrl key is held down.

### Tab

Toggles skipping, causing it to occur until tab is pressed again.

### Mousewheel-Up, PageUp

Causes rollback to occur. Rollback reverses the game back in time, showing prior text and even allowing menu choices to be changed.

### Mousewheel-Down, PageDown

Causes rollforward to occur, cancelling out a previous rollback.

### Right-click, Escape

Enters the game menu. When in the game menu, returns to the game.

### Middle-click, H

Hides the text window and other transient displays.

### F

Toggles fullscreen mode

### S

Takes a screenshot, saving it in a file named screenshotxxxx.png, where xxxx is a serial number.

### Alt-H, Command-H

Hides (iconifies) the window.

### Alt-F4, Command-Q

Quits the game.

### Delete

When a save slot is selected, deletes that save slot.

# Legal Notice
---------------------------------------------------------------------------------------------------------

This game uses source code from a number of open source projects. For a list, and a location where the source code can be downloaded from, please view the LICENSE.txt file in the renpy directory, or visit [http://www.renpy.org/wiki/renpy/License](http://www.renpy.org/wiki/renpy/License "http://www.renpy.org/wiki/renpy/License") .
