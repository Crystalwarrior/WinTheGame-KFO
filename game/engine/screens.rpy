##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

label splashscreen:
    # SPLASH SCREEN (anything to happen before main menu)
    $ renpy.sound.play("sfx/static_loop.ogg", channel=1,loop=True)
    scene static
    if not persistent.seen_splash:
        show splash_warning at mid with dissolve
        $ renpy.pause(5.0,hard=True)
        hide splash_warning with dissolve
        $ renpy.pause(0.5)
        show splash_logo at mid with slowdissolve
        $ renpy.pause(2.0,hard=True)
        hide splash_logo with slowdissolve
        play music "sfx/accent_dumdum.ogg" noloop
        $ renpy.pause(1.0)
        play sound "sfx/splash_intro.ogg"
        $ renpy.pause(0.6,hard=True)
        show splash_hand
        $ renpy.pause(3.0)
        play sound "sfx/beep_win.ogg"
        $ renpy.pause(0.65,hard=True)
        show splash_kfo with dissolve
        $ persistent.seen_splash = True
    else:
        $ renpy.sound.play("sfx/static.ogg", channel=1)
    $ renpy.sound.play("sfx/main_menu_type.ogg")
    
    return
    
screen main_menu:
    # This ensures that any other menu screen is replaced.
    tag menu

    
    
    # The background of the main menu.
    window:
        background "static"
    add "gui/bullets.png" xpos 0 yalign 1.0
    
    add "gui/hand.png"
    imagebutton idle im.MatrixColor("gui/splash_kfo.png",im.matrix.brightness(-0.1)) hover "gui/splash_kfo.png" action OpenURL("https://crystalwarrior.github.io/KFO-website/") xanchor 0.0 yanchor 0.0 xpos 0 ypos 0 focus_mask True
    # The main menu buttons.
    imagebutton idle "gui/newgame1.png" hover "gui/newgame2.png" action Start() xanchor 0.0 yanchor 0.0 xpos 70 ypos 357
    imagebutton idle "gui/loadgame1.png" hover "gui/loadgame2.png" action ShowMenu("load") xanchor 0.0 yanchor 0.0 xpos 70 ypos 422
    imagebutton idle "gui/config1.png" hover "gui/config2.png" action ShowMenu("preferences") xanchor 0.0 yanchor 0.0 xpos 70 ypos 484
    imagebutton idle "gui/exit1.png" hover "gui/exit2.png" action Quit(confirm=False) xanchor 0.0 yanchor 0.0 xpos 70 ypos 547
    add "winthegame" xpos 68 ypos 285
    
    
    
init -2 python:
    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"


#############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say

screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        if who is not None:
            frame xalign 0.055 yalign 0.94:
                xpadding 5 ypadding 5
                add SideImage() 


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.93
        yanchor 1.0
        vbox:
            style "menu"
            style_group "menu_size"
            spacing 2
            
            for caption, action, chosen in items:
                    
                if action:  
                    button:
                        xalign 0.5
                        action action
                        style "menu_choice_button"    
                        
                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)
    style.menu_choice_button.size_group = "menu_size"


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
        



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation

screen navigation:
    
    
    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav" xalign .5 yalign .98 background None

        has vbox
        if show_buttons:
            hbox:
                add "gui/bracket_small.png" ypos 7
                textbutton _("quick load") action Jump("_quick_load") xalign 0.0 style "menu_buttons" text_style "menu_buttons_text"
            hbox:
                add "gui/bracket_small.png" ypos 7
                textbutton _("quick save") action Jump("_quick_save") xalign 0.0 style "menu_buttons" text_style "menu_buttons_text"
    # The various buttons.
    frame:
        style_group "gm_nav" xalign .98 yalign .98 background None

        
        has vbox
        hbox:
            add "gui/bracket_small.png" ypos 7
            textbutton _("return") action Return() xalign 0.0 style "menu_buttons" text_style "menu_buttons_text"
        if show_buttons:
            hbox:
                add "gui/bracket_small.png" ypos 7
                textbutton _("save game") action ShowMenu("save") xalign 0.0  style "menu_buttons" text_style "menu_buttons_text"
            hbox:
                add "gui/bracket_small.png" ypos 7
                textbutton _("load game") action ShowMenu("load") xalign 0.0 style "menu_buttons" text_style "menu_buttons_text"
        hbox:
            add "gui/bracket_small.png" ypos 7
            textbutton _("config") action ShowMenu("preferences") xalign 0.0 style "menu_buttons" text_style "menu_buttons_text"
        hbox:
            add "gui/bracket_small.png" ypos 7
            textbutton _("main menu") action MainMenu() xalign 0.0 style "menu_buttons" text_style "menu_buttons_text"
        hbox:
            add "gui/bracket_small.png" ypos 7
            textbutton _("quit") action Quit() xalign 0.0 style "menu_buttons" text_style "menu_buttons_text"
        


init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    style.create('menu_buttons', 'button')
    style.menu_buttons.background = None
    style.menu_buttons.yalign = 0.0
    style.create('menu_buttons_text', 'button_text')
    style.menu_buttons_text.text_align = 0.0    
    style.menu_buttons_text.color = "#00ff00"
    style.menu_buttons_text.hover_color = "#ffffff"  
    style.menu_buttons_text.selected_color = "#ffffff"
    style.menu_buttons_text.insensitive_color = "#353535"
    


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
screen file_picker:

    hbox xalign 0.5:
            style_group "file_picker_nav"
            
            textbutton _("Previous"):
                action FilePagePrevious() style "digi_button" text_style "digi_button"

            textbutton _("Auto"):
                action FilePage("auto") style "digi_button" text_style "digi_button"

            for i in range(1, 11):
                textbutton str(i):
                    action FilePage(i) style "digi_button" text_style "digi_button"
                    
            textbutton _("Next"):
                action FilePageNext() style "digi_button" text_style "digi_button"
    frame:
        style "file_picker_frame" ypos 30 xmargin 10 background None

        has vbox
        # The buttons at the top allow the user to pick a
        # page of files.
        

        $ columns = 2
        $ rows = 4
                
        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"
            
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True xminimum 375
                    style "digi_button"
                    hbox:
                        xfill True xminimum 370
                        # Add the screenshot.
                        frame:
                            xpadding 6 ypadding 6 
                            add FileScreenshot(i)
                        
                        # Format the description, and add it as text.
                        $ description = "%s\n%s" % (
                            FileTime(i, empty=_("Empty Slot")),
                            FileSaveName(i))
                        null width 5
                        text description  text_align 0.0 xalign 0.0 #style "digi_button_text"
                        if FileSaveName(i) != "":
                            imagebutton idle "gui/trash1.png" hover "gui/trash2.png" action FileDelete(i) xalign 0.99 yalign 0.99
                        key "save_delete" action FileDelete(i)
    vbox:
        xpos 5 ypos 0.995 yanchor 1.0 xanchor 0.0
        hbox:
            if persistent.won_game_traditional:
                add "icons/trophy_ascii.png" yalign 1.0
            if persistent.won_game_destroy:
                add "icons/trophy_ascii2.png"  yalign 1.0
            
            #add "icons/trophy_ascii3.png" yalign 1.0
            # add "icons/trophy_ascii_small.png" yalign 1.0
            if persistent.won_game_name:
                add "icons/trophy_ascii_ribbon.png" yalign 1.0
            
        text ("Game Version: {color=#FFF}"+config.version+"{/color}") size 15 color "#00ff00"
        
        
screen file_picker:
    variant "small"
    hbox xalign 0.5:
            style_group "file_picker_nav"
            
            textbutton _("<"):
                action FilePagePrevious() style "digi_button" text_style "digi_button"

            textbutton _("Auto"):
                action FilePage("auto") style "digi_button" text_style "digi_button"

            for i in range(1, 11):
                textbutton str(i):
                    action FilePage(i) style "digi_button" text_style "digi_button"
                    
            textbutton _(">"):
                action FilePageNext() style "digi_button" text_style "digi_button"
    frame:
        style "file_picker_frame" ypos 30 xmargin 10 background None

        has vbox
        # The buttons at the top allow the user to pick a
        # page of files.
        

        $ columns = 2
        $ rows = 4
                
        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"
            
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True xminimum 375
                    style "digi_button"
                    hbox:
                        xfill True xminimum 370
                        # Add the screenshot.
                        frame:
                            xpadding 6 ypadding 6 
                            add FileScreenshot(i)
                        
                        # Format the description, and add it as text.
                        $ description = "%s\n%s" % (
                            FileTime(i, empty=_("Empty Slot")),
                            FileSaveName(i))
                        null width 5
                        text description  text_align 0.0 xalign 0.0 #style "digi_button_text"
                        if FileSaveName(i) != "":
                            imagebutton idle "gui/trash1.png" hover "gui/trash2.png" action FileDelete(i) xalign 0.99 yalign 0.99
                        key "save_delete" action FileDelete(i)
    vbox:
        xpos 5 ypos 0.995 yanchor 1.0 xanchor 0.0
        hbox:
            if persistent.won_game_traditional:
                add "icons/trophy_ascii.png" yalign 1.0
            if persistent.won_game_destroy:
                add "icons/trophy_ascii2.png"  yalign 1.0
            
            #add "icons/trophy_ascii3.png" yalign 1.0
            # add "icons/trophy_ascii_small.png" yalign 1.0
            if persistent.won_game_name:
                add "icons/trophy_ascii_ribbon.png" yalign 1.0
            
        text ("Game Version: {color=#FFF}"+config.version+"{/color}") size 15 color "#00ff00"
                    
                    
screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

    

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox
                hbox:
                    add "gui/bracket.png"
                    label _("display")
                textbutton _("window") action Preference("display", "window") style "digi_button" text_style "digi_button" xalign 1.0
                textbutton _("fullscreen") action Preference("display", "fullscreen") style "digi_button" text_style "digi_button" xalign 1.0


            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("text speed")
                        text "How fast the text shows." size 10
                bar value Preference("text speed")
            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("auto-attack")
                        text  "No need to aim during battles." size 10
                hbox xalign 1.0:
                    textbutton _("on") action SetField(persistent, 'autoattack', True) style "digi_button" text_style "digi_button"
                    textbutton _("off") action SetField(persistent, 'autoattack', False) style "digi_button" text_style "digi_button"
            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("always act")
                        text  "You can always use items, even during enemy turn and at 0 HP." size 10
                hbox xalign 1.0:
                    textbutton _("on") action SetField(persistent, 'always_act', True) style "digi_button" text_style "digi_button"
                    textbutton _("off") action SetField(persistent, 'always_act', False) style "digi_button" text_style "digi_button"

        vbox:
            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("skip")
                        text  "Fast forward through things you've seen or everything?" size 10
                hbox xalign 1.0:
                    textbutton _("seen") action Preference("skip", "seen") style "digi_button" text_style "digi_button" xalign 1.0
                    textbutton _("everything") action Preference("skip", "all") style "digi_button" text_style "digi_button" xalign 1.0

            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("for choices")
                        text  "Keep fast forwarding after choices or stop?" size 10
                hbox xalign 1.0:
                    textbutton _("stop") action Preference("after choices", "stop") style "digi_button" text_style "digi_button" xalign 1.0
                    textbutton _("go on") action Preference("after choices", "skip") style "digi_button" text_style "digi_button" xalign 1.0

            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("sanity sounds")
                        text  "Heartbeat sounds when low on sanity or health." size 10
                hbox xalign 1.0:
                    textbutton _("on") action SetField(persistent, 'sanity_sounds', True) style "digi_button" text_style "digi_button" xalign 1.0
                    textbutton _("off") action SetField(persistent, 'sanity_sounds', False) style "digi_button" text_style "digi_button" xalign 1.0

        vbox:
            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    label _("music vol.")
                bar value Preference("music volume")
                null height 5
                hbox:
                    xalign 1.0
                    textbutton "mute":
                            action Preference("music mute", "toggle") style "digi_button" text_style "digi_button"

            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    label _("sound vol.")
                bar value Preference("sound volume")
                null height 5
                hbox:
                    xalign 1.0
                    if config.sample_sound:
                        textbutton "test":
                            action Play("sound", config.sample_sound) style "digi_button" text_style "digi_button"
                    textbutton "mute":
                            action Preference("sound mute", "toggle") style "digi_button" text_style "digi_button"

            frame:
                style_group "pref"
                has vbox

                textbutton _("config joystick") action ShowMenu("joystick_preferences") style "digi_button" text_style "digi_button" xalign 1.0
            
    vbox:
        xpos 5 ypos 0.995 yanchor 1.0 xanchor 0.0
        hbox:
            if persistent.won_game_traditional:
                add "icons/trophy_ascii.png" yalign 1.0
            if persistent.won_game_destroy:
                add "icons/trophy_ascii2.png"  yalign 1.0
            
            #add "icons/trophy_ascii3.png" yalign 1.0
            # add "icons/trophy_ascii_small.png" yalign 1.0
            if persistent.won_game_name:
                add "icons/trophy_ascii_ribbon.png" yalign 1.0
        hbox:
            text ("Game Version: {color=#FFF}"+config.version+"{/color}") size 15 color "#00ff00" yalign 0.5
            null width 10
            textbutton "update" action updater.Update("http://happybackwards.com/files/WinTheGame-dists/updates.json") style "digi_button" text_style "digi_button" yalign 0.5
            
            
screen preferences:
    variant "small"
    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox
                hbox:
                    add "gui/bracket.png"
                    label _("display")
                textbutton _("window") action Preference("display", "window") style "digi_button" text_style "digi_button" xalign 1.0
                textbutton _("fullscreen") action Preference("display", "fullscreen") style "digi_button" text_style "digi_button" xalign 1.0


            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("text speed")
                        text "How fast the text shows." size 10
                bar value Preference("text speed")
            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("auto-attack")
                        text  "No need to aim during battles." size 10
                hbox xalign 1.0:
                    textbutton _("on") action SetField(persistent, 'autoattack', True) style "digi_button" text_style "digi_button"
                    textbutton _("off") action SetField(persistent, 'autoattack', False) style "digi_button" text_style "digi_button"
            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("always act")
                        text  "You can always use items, even during enemy turn and at 0 HP" size 10
                hbox xalign 1.0:
                    textbutton _("on") action SetField(persistent, 'always_act', True) style "digi_button" text_style "digi_button"
                    textbutton _("off") action SetField(persistent, 'always_act', False) style "digi_button" text_style "digi_button"

        vbox:
            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("skip")
                        text  "Fast forward through things you've seen or everything?" size 15
                textbutton _("only seen") action Preference("skip", "seen") style "digi_button" text_style "digi_button" xalign 1.0
                textbutton _("everything") action Preference("skip", "all") style "digi_button" text_style "digi_button" xalign 1.0

            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("for choices")
                        text  "Keep fast forwarding after choices or stop?" size 15
                hbox xalign 1.0:
                    textbutton _("stop") action Preference("after choices", "stop") style "digi_button" text_style "digi_button" xalign 1.0
                    textbutton _("go on") action Preference("after choices", "skip") style "digi_button" text_style "digi_button" xalign 1.0

            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    vbox:
                        label _("sanity sounds")
                        text  "Heartbeat sounds when low on sanity or health." size 15
                hbox xalign 1.0:
                    textbutton _("on") action SetField(persistent, 'sanity_sounds', True) style "digi_button" text_style "digi_button" xalign 1.0
                    textbutton _("off") action SetField(persistent, 'sanity_sounds', False) style "digi_button" text_style "digi_button" xalign 1.0

        vbox:
            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    label _("music vol.")
                bar value Preference("music volume")
                null height 5
                hbox:
                    xalign 1.0
                    textbutton "mute":
                            action Preference("music mute", "toggle") style "digi_button" text_style "digi_button"

            frame:
                style_group "pref"
                has vbox

                hbox:
                    add "gui/bracket.png"
                    label _("sound vol.")
                bar value Preference("sound volume")
                null height 5
                hbox:
                    xalign 1.0
                    if config.sample_sound:
                        textbutton "test":
                            action Play("sound", config.sample_sound) style "digi_button" text_style "digi_button"
                    textbutton "mute":
                            action Preference("sound mute", "toggle") style "digi_button" text_style "digi_button"

            frame:
                style_group "pref"
                has vbox

                textbutton _("start skip") action Skip() style "digi_button" text_style "digi_button" xalign 1.0
            
    vbox:
        xpos 5 ypos 0.995 yanchor 1.0 xanchor 0.0
        hbox:
            if persistent.won_game_traditional:
                add "icons/trophy_ascii.png" yalign 1.0
            if persistent.won_game_destroy:
                add "icons/trophy_ascii2.png"  yalign 1.0
            
            #add "icons/trophy_ascii3.png" yalign 1.0
            # add "icons/trophy_ascii_small.png" yalign 1.0
            if persistent.won_game_name:
                add "icons/trophy_ascii_ribbon.png" yalign 1.0
        hbox:
            text ("Game Version: {color=#FFF}"+config.version+"{/color}") size 15 color "#00ff00" yalign 0.5
            null width 10


init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5
    style.pref_frame.background = None
    
    style.label_text.color = "#00ff00"

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    vbox:
        xcenter 0.5
        ycenter 0.5
        frame:
            style_group "yesno"
    
            xfill True
            xmargin .05
            ypos .1
            yanchor 0
            ypadding .05
            
            has vbox:
                xalign .5
                yalign .5
                spacing 20
                
            label _(message):
                xalign 0.5
    
            hbox:
                xalign 0.5
                spacing 100
                
                textbutton _("Yes") action yes_action style "ascii_button" text_style "ascii_button_text"
                textbutton _("No") action no_action style "ascii_button" text_style "ascii_button_text"


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.color = "#d3ffd3"
    style.yesno_label_text.size = 20
    
    style.create('ascii_button_text', 'button_text')
    style.ascii_button_text.size = 25
    style.ascii_button_text.color = "#00db00"
    style.ascii_button_text.hover_color = "#FFF"
    style.create('ascii_button', 'button')
    style.ascii_button.background = "gui/bracket.png"
    style.ascii_button.left_padding = 30
    style.ascii_button.top_padding = 0
    
    layout.ARE_YOU_SURE = "Are you sure?{image=gui/frowny.png}"
    layout.DELETE_SAVE ="Are you sure you want to {color=#00db00}delete{/color} this?{image=gui/frowny.png}"
    layout.OVERWRITE_SAVE = "Are you sure you want to {color=#00db00}overwrite{/color} this?{image=gui/frowny.png}"
    layout.LOADING = "Loading will {color=#00db00}lose unsaved progress{/color}. Are you sure you want to do this?{image=gui/frowny.png}"
    layout.QUIT = "Are you sure you want to {color=#00db00}quit{/color}?{image=gui/frowny.png}"
    layout.MAIN_MENU = "Are you sure you want to {color=#00db00}return to the main menu{/color}? This will lose unsaved progress.{image=gui/frowny.png}"
    
    
############ Updater ################
    
screen updater:

        add "bg/static.jpg"

        frame:

            xalign .5
            ypos 100
            xpadding 20
            ypadding 20

            xmaximum 400
            xfill True

            has vbox

            label _("Updater")

            null height 10

            if u.state == u.ERROR:
                text _("An error has occured:")
            elif u.state == u.CHECKING:
                text _("Checking for updates.")
            elif u.state == u.UPDATE_NOT_AVAILABLE:
                text _("This program is up to date.")
            elif u.state == u.UPDATE_AVAILABLE:
                text _("[u.version] is available. Do you want to install it?")
            elif u.state == u.PREPARING:
                text _("Preparing to download the updates.")
            elif u.state == u.DOWNLOADING:
                text _("Downloading the updates.")
            elif u.state == u.UNPACKING:
                text _("Unpacking the updates.")
            elif u.state == u.FINISHING:
                text _("Finishing up.")
            elif u.state == u.DONE:
                text _("The updates have been installed. The program will restart.")
            elif u.state == u.DONE_NO_RESTART:
                text _("The updates have been installed.")
            elif u.state == u.CANCELLED:
                text _("The updates were cancelled.")

            if u.message is not None:
                null height 10
                text "[u.message!q]"

            if u.progress is not None:
                null height 10
                bar value u.progress range 1.0

            if u.can_proceed or u.can_cancel:
                null height 10

            if u.can_proceed:
                textbutton _("Proceed") action u.proceed xfill True

            if u.can_cancel:
                textbutton _("Cancel") action u.cancel xfill True
        
            

            

    
