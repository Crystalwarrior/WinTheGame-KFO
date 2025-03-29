## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = False

    ## These control the width and height of the screen.

    config.screen_width = 800
    config.screen_height = 600

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Win the Game - KFO"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "Win the Game - KFO"
    config.version = "0.8.3"
    
    config.window_icon = "winky.png"

    #########################################
    # Themes
    
    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles. It's
    ## the only theme we currently support.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.tv(
        # Color scheme: Muted Horror
                                    
        ## The color of an idle widget face.
        widget = "#00db00",

        ## The color of a focused widget face.
        widget_hover = "#00ff00",

        ## The color of te text in a widget.
        widget_text = "#d3ffd3",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#fff",

        ## The color of a disabled widget face. 
        disabled = "#232323",

        ## The color of disabled widget text.
        disabled_text = "#424242",

        ## The color of informational labels.
        label = "#0a8709",

        ## The color of a frame containing widgets.
        frame = "#015b01",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = Animation( im.Tile("map/bg1.jpg"),0.2,im.Tile("map/bg2.jpg"),0.2,im.Tile("map/bg3.jpg"),0.2,),

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = Animation( im.Tile("map/bg1.jpg"),0.2,im.Tile("map/bg2.jpg"),0.2,im.Tile("map/bg3.jpg"),0.2,),

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.            
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = Animation("gui/dialogue.png",0.5,"gui/dialogue2.png",2.0,"gui/dialogue3.png",0.05)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    style.window.left_margin = 0
    style.window.right_margin = 0
    style.window.top_margin = 0
    style.window.bottom_margin = 0

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.xpadding = 45
    style.window.top_padding = 30
    #style.window.bottom_padding = 6

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 158


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    style.default.font = "fonts/Commodore Angled v1.2.ttf"

    ## The default size of text.

    style.default.size = 16
    style.default.drop_shadow = [(1,1)]
    style.default.color = "#d3ffd3"

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = True

    ## Sounds that are used when button and imagemaps are clicked.

    style.button.activate_sound = "sfx/beep_on.ogg"
    style.imagemap.activate_sound = "sfx/beep_on.ogg"
    style.image_button.activate_sound = "sfx/beep_on.ogg"
    style.button.hover_sound = "sfx/beep2.ogg"
    style.image_button.hover_sound = "sfx/beep2.ogg"
    style.imagemap.hover_sound = "sfx/beep2.ogg"

    ## Sounds that are used when entering and exiting the game menu.

    config.enter_sound = "sfx/click.ogg"
    config.exit_sound = "sfx/click.ogg"

    ## A sample sound that can be played to check the sound volume.

    config.sample_sound = "sfx/blood1.ogg"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "music/bgs_ghost.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = None

    ## Used between screens of the game menu.
    config.intra_transition = None

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = None

    ## Used when returning to the main menu from the game.
    config.game_main_transition = None

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = None

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = None

    ## Used when a game is loaded.
    config.after_load_transition = None

    ## Used when the window is shown.
    config.window_show_transition = None

    ## Used when the window is hidden.
    config.window_hide_transition = None


    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
    config.save_directory = "deathgame-1313682820"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 0
    
    config.old_substitutions = True
    config.new_substitutions = True

    #########################################
    ## More customizations can go here.
    config.default_text_cps = 80
    
    style.nvl_window.xmargin=75
    style.nvl_window.ymargin=60
    style.nvl_window.xpadding=15
    style.nvl_window.ypadding=10
    style.nvl_window.background=Frame("gui/static.png",30,30)
    
    style.frame.background = Frame("gui/screen.png",10,10)
    style.frame.xpadding=10
    style.frame.top_padding=10
    style.frame.bottom_padding=10
    style.pref_frame.bottom_padding=15
    style.pref_frame.right_padding=15
    
    style.button.background = Frame("gui/bar_dark.png",5,5)
    style.button.hover_background = Frame("gui/bar_full.png",5,5)
    style.button.selected_background = Frame("gui/bar_full.png",5,5)
    style.button.selected_hover_background = Frame("gui/bar_hover.png",5,5)
    style.button.insensitive_background = Frame("gui/bar_empty.png",5,5)
    style.button_text.size = 18
    style.button.ypadding = 5
    
    style.skip_indicator.xpos = -300
    
    style.create('digi_button', 'button')
    style.digi_button.background = Frame("gui/digi_button5.png",5,5)
    style.digi_button.hover_background = Frame("gui/digi_button2.png",5,5)
    style.digi_button.selected_background = Frame("gui/digi_button1.png",5,5)
    style.digi_button.insensitive_background = Frame("gui/digi_button4.png",5,5)
    style.create('digi_button_text', 'button_text')
    style.digi_button.color = "#0a8709"
    style.digi_button.hover_color = "#00ff00"
    style.digi_button.selected_color = "#00ff00"
    style.digi_button.insensitive_color = "#373737"
    
    style.create('small_button_text', 'button_text')
    style.small_button_text.size = 12
    
    
    style.create('small_button', 'button')
    style.small_button.xalign=0.5
    style.small_button.xminimum=100
    
    style.create('equip_button_text', 'small_button_text')
    style.equip_button_text.insensitive_color = "#02e602"
    
    style.create('unequip_button_text', 'small_button_text')
    style.unequip_button_text.color = "#02e602"
    style.create('unequip_button', 'small_button')
    style.unequip_button.background = Frame("gui/bar_empty.png",5,5)  
    style.unequip_button.hover_background = Frame("gui/bar_dark.png",5,5)
    
    style.create('item_button', 'button')
    style.item_small_button.xalign=0.5
    style.item_small_button.xminimum=0
    
    config.mouse = { 'default' : (("gui/cursor.png", 0, 0), ("gui/cursor.png", 0, 0))}
    
    style.list_text.drop_shadow = None
    style.list_text.color = "#FFF"
    # style.list_row[0].background = None
    # style.list_row[1].background = None
    
    
    style.file_picker_button.background = Frame(im.MatrixColor("gui/bar_empty.png",im.matrix.opacity(0.95)),5,5)
    style.file_picker_button.hover_background = Frame(im.MatrixColor("gui/bar_full.png",im.matrix.opacity(0.7)),5,5)
    style.file_picker_button.selected_background = Frame(im.MatrixColor("gui/bar_dark.png",im.matrix.opacity(0.7)),5,5)
    style.file_picker_button.selected_hover_background = Frame(im.MatrixColor("gui/bar_hover.png",im.matrix.opacity(0.7)),5,5)
    style.file_picker_button.insensitive_background = Frame(im.MatrixColor("gui/bar_empty.png",im.matrix.opacity(0.5)),5,5)
    style.file_picker_button.ypadding = 5
    
    #style.file_picker_text.drop_shadow = None
    #style.file_picker_text.color = "#000"
    
    style.input.caret = "typing_caret"

    ##########################

    #Shake effect

init -4:
    python:
        import math
        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

#Center window on startup
init python hide:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    

         


## VARIANT SIZE SUPPORT        
init python:
    config.variants = ["small",None]
    # if renpy.variant("small"):
        # style.default.size = 25

 


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "WinTheGame"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Win The Game"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = True

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/**.rpy~', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    