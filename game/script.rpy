############################
######### CONFIG ###########
############################

init -3:
    #Can rollback? (if you want to make the game harder and decisions semi-permanent.)
    #$ config.rollback_enabled = False

    #What screen is default when right-click or ESC key?
    $_game_menu_screen = "preferences_screen"
    
    #Show black gradient at the top of screen? (helps to see text)
    $ show_black_gradient = False

    #Sound channels
    $ renpy.music.register_channel("ambience", "sfx", True)
    $ renpy.music.register_channel("ambience2", "sfx", True)
    $ renpy.music.register_channel("sanity", "sfx", True)
    $ renpy.music.register_channel("typing", "sfx", False)
    $ renpy.music.register_channel("system", "sfx", False)
    $ renpy.music.register_channel("system2", "sfx", False)
    $ ambient_music_tracks = ["music/bgs_ghost2.ogg", "music/bgs_creepy.ogg", "music/bgs_reverbbells.ogg", "music/bgs_horizons.ogg", "music/bgs_breath.ogg", "music/bgs_slow.ogg"]

    #Typing Sounds
    python:
        config.window_show_transition = fade
        def callback(event, **kwargs):
            if event == "show":
                renpy.music.play("sfx/typing.ogg", channel="typing") #Default typing sound
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="typing")
        def callback_digi(event, **kwargs):
            if event == "show":
                renpy.music.play("sfx/typing_digi.ogg", channel="typing") #Datapad typing sound
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="typing")

label start:
    #Invincibility Cheat (You cannot die in battles)
    if config.developer: #Turn it on by default for developers
        $ cannot_die = True
    else:
        $ cannot_die = False
        
    #Hear heartbeat sounds when low on health or sanity? (can be annoying to some)
    $ sanity_sounds = True
    
    #GPS Toggle - Show little portraits of where the players are on the map
    ## Two items can be acquired to turn on map portraits: 
    ###1. GPS (see everyone who is alive)
    ### 2. Binoculars (these limit your view to only grids around you, and only people outside)
    if config.developer: #Turn GPS view on by default for developers
        $ show_gps = True
    else:
        $ show_gps = False
        
    #Show Player inventory in Stats? (only if GPS feature is active)
    $ show_p_inv = False
    
    #Show Player inventory all the time?
    $ show_p_inv_always = False
    
    #Set weapons and armor to nothing
    $ wpn = None
    $ armor = None
    
    #Starting Time (24-hour clock, aka military time)
    $ day = 1
    $ hour = 6
    
    #Time Limit (in days)
    $ time_limit = 7
    
    #Starting Inventory
    $ inventory = []
    
    #Starting health and sanity
    $ sanity = 100
    $ health = 100

    #Initialize variables
    $ classmates = []
    $ locations = []
    $ all_items = []
    $ party = []
    $ followers = []
    $ item_name = "blank"
    $ fancy_item_name ="blank"
    $ readback_buffer = []

    call events_init #Initialize events, REQUIRED!

    # The following code references from the items.rpy, locs.rpy, and chars.rpy. Instructions on how to make those are in each file.
    
    #######################ITEMS
    
    call game_init_items #Initialize items, REQUIRED!

    #Default wpn
    $ wpn = fist
    
    #What weapons can the player get at random at the beginning? (<< You may edit this as you like)
    $ starter_wpns = [bat, knife,shoe,shotgun,rifle,taser,potlid,uzi,slingshot,bbgun,sickle]
    if persistent.won_game_destroy: #Bonus items for winning a game
        $ starter_wpns.append(tommy)
    if persistent.won_game_name:
        $ starter_wpns.append(machinegun)
    if persistent.won_game_traditional:
        $ starter_wpns.append(flamethrower)
        
    #######################LOCATIONS
    
    call game_init_locs #Initialize locations, REQUIRED!
    
    $ find_all_exits() #detect the exits for all locs, REQUIRED!
       
    #Default starting location
    $ loc = c1
    $ loc.find() #find that location
    
    #######################CHARACTERS
    
    call game_init_chars #Initialize characters, REQUIRED!
        
    
    ## DEFAULT PLAYER CHARACTER
    $ you_are = you.name #Your name, "you" defined in chars.rpy
    #Assign Gender
    if you.gender == "Male":
        $ male = True
    else:
        $ male = False

    $ find_all_pop() #Calculate who is in what location, REQUIRED!
    
    #########################################################################
    ####################### FORBIDDEN ZONE REPORTS #######################
    #########################################################################
    #FZ Reports are automatic, timed reports that let the player know how many players are still alive and which zones are now instant-death zones.
    
    $ fz_reports = True #toggle False if you don't want any automated reports.
    $ fz_lingo = "forbidden zone" #what you call the death zones
    
    #Time Config
    ## When should the report of a new forbidden zone come about?
    $ fz_period = 12 #Grace period (number of hours between reports)
    $ fz_start_day = 2 #Day when reports start
    $ fz_start_hour = 0 #Hour when reports start
    
    #Forbidden Zones
    ## Listed in order they should be excluded (the time when they are is defined separately)
    $ zone_schedule = [
    a4, c1, g1, d4, c3, f2, d1, f4, g4, e1, c4, a1, d3, a2, g3, f3, f1
    ]
    
    #Forbidden Zone Increment
    ## Number of FZs to announce per report
    $ fz_num = 1

    #Random FZs
    ## Toggle to True if you want forbidden zones to be selected at random from the zone_schedule, for unpredictable games
    $ random_fz = False
    
    #Inspirational Music
    ## Play a song along with your reports
    $ fz_music = True
    $ fz_music_list = ["music/AveMaria.ogg", "music/CarminaBurana.ogg", "music/LibertyBellMarch.ogg", "music/RadezkyMarch.ogg", "music/StraussBlueDanube.ogg", ]
    
    #Max Reports
    ## Maximum allowed in one game
    $ max_reports = 21
    
    #########################
    
    ###Bear Trap Stuff
    # The trap is a special item that you can strategically place if you acquire it. If an AI student enters a location with set trap, it will capture that person. If they're a "coward" type, they will die instantly, but otherwise you can deal with them when you retrieve your trap. If the trap doesn't catch a player, it will capture a deer and give you meat.
    $ trap_set = False; trap_loc = None; needs_to_be = [0,0]; trap_caught_person = None; trap_time = [0,0] #(day, hour)
    
    #How long until the trap catches an animal?
    $ trap_required_time = [0,8] # [day, hour]
    #Default: requires 8 hours before it catches an animal (if you don't check it, it will stay in play until it catches a person)
    
    #########################
    
    #Developer menu
    $ renpy.sound.stop(channel=0)
    $ renpy.sound.stop(channel=1)
    scene static
    if config.developer:
        $ ui.text("{u}Developer Menu{/u}\n\n\"Start Game\" will turn developer mode off. To start the game with developer mode still on, launch from Developer Menu.\n\nInvincibility and the GPS feature are on by default unless developer mode is turned off.",xalign=0.5, yalign= 0.5,text_align=0.5)
        menu:
            "Start Game":
                jump real_start
            "Developer Menu":
                menu:
                    "New Game + Intro":
                        python:
                            for i in classmates:
                                i.type = "fixed"
                        jump intro
                    "New Game (no intro)":
                        python:
                            for i in classmates:
                                i.type = "fixed"
                        show shack
                        $ show_buttons = True
                        show screen health
                        $ renpy.music.play("music/bgs_slow.ogg")
                        jump letsgo
                    "Free Play (for testing)":
                        stop music fadeout 2.0
                        $ Mari.met = True
                        $ Jun.met = True
                        $ party_add(Mari)
                        $ party_add(Jun)
                        $ b1.forbid()
                        $ g2.forbid()
                        $ Goro.kill("rules")
                        $ show_buttons = True
                        show screen health
                        $ inventory = [[food,2],[chainsaw,1],[derringer,1]]
                        $ wpn = ak47
                        #$ gps.add()
                        jump grid_loc
                    "Freeplay Deathmatch":
                            $ freeplay = True
                            $ show_gps = False
                            jump freeplay_intro
                    "Test":
                        $ show_buttons = True
                        show screen health
                        $ food.add(amt=2,silent=True)
                        $ pistol.add(amt=1,silent=True)
                        #$ sword.add(1,silent=True)
                        $ grenades.add(amt=4,silent=True)
                        $ dynamite.add(amt=4,silent=True)
                        $ wpn = pistol
                        menu:
                            "Battles":               
                                scene mansion 
                                menu:
                                    "Hostile":
                                        $battle_start(Ikoma,2,"test battle","start",False)
                                    "Coward":
                                        $battle_start(Yuki,3,"test battle","start",False,flee=True)
                                    "Melee":
                                        $battle_start(Ai,0,"test battle","start",False)
                                    "Normal":
                                        $battle_start(Mari,0,"test battle","start",False)
                                        
                            "Puzzle":
                                jump puzzle
                            "Scenes":
                                menu:
                                    "Mansion":
                                        jump mansion_correct
                                    "Recruit Jun":
                                        scene cave_int
                                        jump cave_jun
                                    "Meet Hitomo":
                                        scene bridge
                                        jump find_hitomo
                                    "Tetsuo + Asai":
                                        scene forest3
                                        jump tetsuo_asai
                                    "GPS hospital":
                                        jump gps_hospital
                                    "Boat lie":
                                        jump takeshi_boat_lie
                            "Endings":
                                menu:
                                    "Inside the mansion":
                                        jump inside_mansion
                                    "Forbidden Zone Death":
                                        scene black
                                        jump forbidden_zone_fail
                                    "Time Limit Death":
                                        scene black
                                        jump time_limit_fail
                                    "Won The Game":
                                        scene black
                                        jump won_game
                                    "Credits":
                                        scene black
                                        jump credits
        
    else:
        jump real_start
    
init:
    $ story_mode = True
    $ intro_mode = True
    $ ammo_mode = False
    $ rand_start = False
    $ locs_can_be = []
    $ story_freemove = False
        
label real_start:
    #$ config.developer = False
    $ show_gps = False
    $ cannot_die = False    
    $ show_buttons = False
    $ freeplay = False
    call screen game_settings
    if ammo_mode:
        ##Ammo for guns
        $ bbgun.uses = 9
        $ revolver.uses = 9    
        $ pistol.uses = 5
        $ glock.uses = 7
        $ uzi.uses = 7
        $ bayonet.uses = 9 #ranged uses only
        $ ak47.uses = 9
        $ rifle.uses = 9
        $ shotgun.uses = 4
        $ shotgun_sawed.uses = 2
        $ shotgun_pump.uses = 9
        $ derringer.uses = 5
        $ tommy.uses = 9
        $ machinegun.uses = 9    
    
    if not story_mode:
        $ show_buttons = True
        $ freeplay = True
        jump freeplay_intro
    else:
        if not story_freemove:
            python: #fix characters until you find them, to help with cutscenes
                for i in classmates:
                    i.type = "fixed"
        if intro_mode:
            jump intro
        else:
            $ show_buttons = True
            show shack
            show screen health
            with dissolve
            $ renpy.music.play("music/bgs_slow.ogg")
            jump letsgo
        
screen game_settings:
    vbox yalign 0.5 xalign 0.5:
        add "gui/config_game.png" xalign 0.5
        #null height 10
        if persistent.won_game_traditional:
            hbox xalign 0.0:
                add "gui/bracket.png"
                label "story"
            hbox xalign 0.5 spacing 15:
                textbutton ("campaign") action SetVariable("story_mode",True) style "digi_button" text_style "digi_button"
                textbutton ("deathmatch") action SetVariable("story_mode",False) style "digi_button" text_style "digi_button"
            null height 10
        if persistent.seen_intro and story_mode:
            hbox xalign 0.0:
                add "gui/bracket.png"
                label "intro scene"
            hbox xalign 0.5 spacing 15:
                textbutton ("skip") action SetVariable("intro_mode",False) style "digi_button" text_style "digi_button"
                textbutton ("continue") action SetVariable("intro_mode",True) style "digi_button" text_style "digi_button"
            null height 10
        if not story_mode:
            hbox xalign 0.0:
                add "gui/bracket.png"
                label "randomize start"
            null height 10
            hbox xalign 0.5 spacing 15:
                textbutton ("yes") action SetVariable("rand_start",True) style "digi_button" text_style "digi_button"
                textbutton ("no") action SetVariable("rand_start",False) style "digi_button" text_style "digi_button"
            null height 10
        # if story_mode:
            # hbox xalign 0.0:
                # add "gui/bracket.png"
                # label "chars wait for you"
            # text "NPCs will stay in their starting loc until met." xpos 20 size 13   
            # null height 10
            # hbox xalign 0.5 spacing 15:
                # textbutton ("yes") action SetVariable("story_freemove",False) style "digi_button" text_style "digi_button"
                # textbutton ("no") action SetVariable("story_freemove",True) style "digi_button" text_style "digi_button"
            # null height 10
            
        hbox xalign 0.0:
            add "gui/bracket.png"
            label "sanity sounds"
        text "Heartbeat sounds when low on sanity or health." xpos 20 size 13
        null height 10
        hbox xalign 0.5 spacing 15:
            textbutton ("on") action SetVariable("sanity_sounds",True) style "digi_button" text_style "digi_button"
            textbutton ("off") action SetVariable("sanity_sounds",False) style "digi_button" text_style "digi_button"
        hbox xalign 0.0:
            add "gui/bracket.png"
            label "ammo system"
        text "Guns will eventually run out of bullets." xpos 20 size 13
        null height 10
        hbox xalign 0.5 spacing 15:
            textbutton ("on") action SetVariable("ammo_mode",True) style "digi_button" text_style "digi_button"
            textbutton ("off") action SetVariable("ammo_mode",False) style "digi_button" text_style "digi_button"
        hbox xalign 0.0:
            add "gui/bracket.png"
            label "time limit"
        text "How long you have to win the game." xpos 20 size 13
        null height 10
        hbox xalign 0.5 spacing 15:
            textbutton ("3 days") action SetVariable("time_limit",3) style "digi_button" text_style "digi_button"
            textbutton ("7 days") action SetVariable("time_limit",7) style "digi_button" text_style "digi_button"
            textbutton ("14 days") action SetVariable("time_limit",14) style "digi_button" text_style "digi_button"
        null height 10
            
        textbutton "Start Game" action Return(True) xalign 0.5

    
                    
label freeplay_intro:
    ##### Config stuff
    $ classmates.remove(Goro) #he's not a real character
    $ fz_period = 12
    $ fz_start_day = 1
    $ fz_start_hour = 6 
    $ zone_schedule = [
    a4, c1, g1, d4, c3, f2, d1, f4, g4, e1, c4, a1, d3, a2, g3, f3, f1
    ]
    $ fz_num = 2
    $ random_fz = True
    $ show_gps = True
    python:
        # remove cutscenes and hidden characters. Free for all!
        for i in classmates:
            if i.type == "fixed":
                i.type = "normal"
            if i.hidden:
                i.hidden = False
        #randomize starting locations for everybody
        if rand_start:
            for i in locations:
                locs_can_be.append(i)
            locs_can_be.remove(d5) #remove the island locs
            locs_can_be.remove(e5)   
            print "locs can be",locs_can_be
            for i in classmates:
                rand_start_loc = renpy.random.choice(locs_can_be)
                locs_can_be.remove(rand_start_loc)
                print i.name,rand_start_loc.name
                i.loc = rand_start_loc
            for i in locations:
                i.found = False
        
        
        
    
    ##### Begin Cutscene
    $ cutscene()
    $ loc = Shinobu.loc
    $ renpy.sound.queue("music/bgs_slow.ogg", channel=4, loop=False)
    $ find_all_pop()
    show screen health
    $ loc.find() #find this place if you haven't already
    $ loc_bg = loc.bg #custom bg for this loc
    if loc.sfx is not None:
        $ loc_sound = "sfx/"+loc.sfx+".ogg" #custom ambience for this loc
    $renpy.scene()
    $renpy.show(loc_bg)
    $ renpy.transition(slowdissolve)
    $ renpy.music.set_volume(1.0, 0, channel="ambience")
    if loc.sfx is not None:
        $renpy.music.play(loc_sound,channel="ambience", fadeout=1.0,fadein=1.0)
    "You wake up far from where you last remember."
    "You are playing \"the game\" again ... You don't need to read the datapad to know the drill."
    $ food.add(amt=2)
    "You find the {color=#FFF}water and rations{/color}."
    "The flap opens wider and you immediately see what must be your weapon ..."
    
    $ your_wpn= renpy.random.choice(starter_wpns)
    #$ renpy.block_rollback()

    $ your_wpn.add()
    call weapon_desc
    if your_wpn.wpn_rating > 0:
        $ wpn = your_wpn
    if your_wpn.defense > 0:
        $ armor = your_wpn
    "Time to play."
    jump grid_loc
                    
init -1:
    #Misc variables
    $ locations = []
    $ item_name = "blank"; fancy_item_name ="blank"
    $ sanity = 100; health = 100
    $ total_players, players_alive = 0, 0
    $ male = True
    $ on_cutscene = False
    $ show_time = True
    $ swap = False
    $ discarded = None
    $ wpn = None
    $ armor = None
    $ item_quantity = 0
    $ day = 1
    $ hour = 1
    $ item_to_show = None
    $ notify_y = .001
    $ advantage = 0
    $ enemy_wpn = None
    $ room_here = None
    $ has_followers = False
    $ won_the_game = False
    $ show_people_here = False
    $ already_know_who = False
    $ made_wish = False
    $ wish_safety_you = False
    $ wish_safety_mari = False
    $ wish_safety_jun = False
    $ wish_no_sin = False
    $ found_waterfall = False
    $ boat_repair = 0
    $ music_steps = 0
    $ inven_max = 4
    $ fz_ticker = 0
    $ report_count = 0
    $ show_report = False
    $ death_list = []
    $ who_has_arrows = False
    $ mari_bath_left = False
    $ show_drop_stuff = True
    $ interrupt_sleep = False
    $ yuki_lied = False
    $ takeshi_sad = False
    $ hide_health_stats = False
    $ can_flee = True
    $ f_advantage = False
    $ already_chopped = False
    $ tut_pickup = False
    $ tut_openbag = False
    $ tut_show_pickup = False
    $ tut_show_drop = False
    $ won_game_destroy = False
    $ won_game_name = False
    $ show_click_person_tut = False
    $ show_room_tut = False
    $ escape_plan = None
    $ e_him = "him"
    $ e_his = "his"
    $ e_he = "he"
    $ show_north = False
    $ show_south = False
    $ show_east = False
    $ show_west = False
    $ self_defense_argument = False
    
    #Check to see if player has ever won the game, for whatever bonus
    #Killed everyone, winner is u
    if persistent.won_game_traditional is None:
        $ persistent.won_game_traditional = False    
        
    #Gave computer your name
    if persistent.won_game_name is None:
        $ persistent.won_game_name = False  
        
    #Destroyed the computer
    if persistent.won_game_destroy is None:
        $ persistent.won_game_destroy = False  
        
    #Initialize the auto-battle feature in battle
    if persistent.autoattack is None:
        $ persistent.autoattack = True    
        
    #Check if player has seen intro splash screen before
    if persistent.seen_splash is None:
        $ persistent.seen_splash = False   
        
    
    #Show tutorials only once
    if persistent.ever_battled is None: #Battle Tut
        $ persistent.ever_battled = False
        
    if persistent.show_click_person_tut is None: #Grid Tut
        $ persistent.show_click_person_tut = True
        
    if persistent.show_room_tut is None: #Room Tut
        $ persistent.show_room_tut = True
        
    #Seen intro scene?
    if persistent.seen_intro is None:
        $ persistent.seen_intro = False


            
#GAME OVER SCREEN (bad ending)
label game_over:
    hide screen health
    hide screen health_enemy
    hide screen health_enemy2
    hide screen new_battle
    hide screen beep_yellow_continuous
    hide screen beep_red_continuous
    with dissolve
    stop music channel "sanity"
    play sound "sfx/gameover.ogg"
    play music "sfx/static.ogg" fadein 3.0 fadeout 1.0
    scene static with intro_dissolve
    play sound "sfx/main_menu_type.ogg"
    show game_over:
        xpos 0.27 ypos 0.5
    $ renpy.pause()         
    stop music fadeout 3.0
    scene black with intro_dissolve
    $ renpy.full_restart()
    
#DEATH BY FORBIDDEN ZONE
label forbidden_zone_fail:
    if sanity <= 20:
        $ renpy.block_rollback()
        hide screen health
        hide screen beep_red_continuous
        hide screen beep_yellow_continuous
        nvl clear
        play sound "sfx/beep_computer.ogg" channel 1
        memo "Oopsie! You've entered a {color=#ff0000}forbidden zone{/color}!"
        if (Mari in party or Mari.loc == loc):
            "Mari gasps and grasps her collar. You do, too. You look at each other."
        play sound "sfx/beep_alarm.ogg"
        memo "And you know what that means ..."
        if (Jun in party or Jun.loc == loc):
            jun scared "Oh shit ..."
        play sound "sfx/beep_alarm.ogg"
        memo "{color=#ff0000}You lose{/color}!"
        play sound "sfx/beep_alarm.ogg"
        memo ":("
        stop music
        stop music channel "sanity"
        stop ambience
        play sound "sfx/explosion.ogg" channel 1
        $ show_blood()
        $ renpy.pause(2.0)
        jump game_over
    else:
        "Oh no. You're in a forbidden zone."
        if (Mari in party or Mari.loc == loc):
            mari "Shinobu! Run!!"
        if (Jun in party or Jun.loc == loc):
            jun "Let's get out of here, right now!!"
        $ loc = runaway()
        jump grid_loc
    
#DEATH BY TIME LIMIT
label time_limit_fail:
    hide screen health
    hide screen beep_red_continuous
    hide screen beep_yellow_continuous
    nvl clear
    play sound "sfx/beep_computer.ogg" channel 1
    memo "Oh drats! We've run out of time to play!"
    if (Mari in party or Mari.loc == loc):
        "Mari gasps and grasps her collar. You do, too. You look at each other."
    memo "Since there is more than one player active, that means {color=#ff0000}everyone loses{/color}!"
    memo "I know, I know. We were just getting to the good part!"
    play sound "sfx/beep_alarm.ogg"
    memo "Oh well. There's always the next game."
    if (Jun in party or Jun.loc == loc):
        jun scared "Oh shit ..."
    play sound "sfx/beep_alarm.ogg"
    memo "You won't get to see it, but - well. Nevermind. Anyway."
    play sound "sfx/beep_alarm.ogg"
    memo "Bye bye. :("
    stop music
    stop music channel "sanity"
    stop ambience
    play sound "sfx/explosion.ogg" channel 1
    $ show_blood()
    $ renpy.pause(2.0)
    jump game_over
    
    
#VICTORY! 
label won_game:
    $ persistent.won_game_traditional = True
    hide screen health
    hide screen beep_red_continuous
    hide screen beep_yellow_continuous
    nvl clear
    play sound "sfx/helicopter_approach.ogg" channel 1
    $ renpy.sound.queue("sfx/helicopter.ogg",channel=1,loop=True)
    play sound "sfx/beep_on.ogg"
    dp "Congratulations, {color=#fff}<StudentName>{/color}!"
    dp "All players have been eliminated!"
    play sound "sfx/beep_win.ogg"
    dp "You have {color=#FF0000}won the game{/color}!"
    dp "{image=icons/trophy.jpg}\n\n:)"
    dp "A helicopter will be arriving shortly to pick you up and take you home."
    dp "I bet you can't wait to show your parents your new trophy! It's not real or anything. But you can show them that picture. I'm sure they'll believe you. You are alive, after all."
    dp "Oh, and the collar around your neck - which is kind of permanent. Sorry!"
    scene bg helicopter sky with dissolve
    "The beating sound of propellers gets louder and you look to the sky."
    nvl clear
    dp "You've been through thick and thin, seen friends and enemies alike fall ..."
    dp "But wasn't it F-U-N?"
    dp "On your ride back, please be sure to fill out the comment card provided. You can check the box at the bottom if you'd like to be considered for the next game!"
    dp "I can't promise you'll be selected, since there is quite a long waiting list to participate, but I will personally put in a good word for you, {color=#fff}<StudentName>{/color}! You have been by far my favorite contestant!"
    dp "I mean, the way you killed {color=#fff}<Student_Kill1>{/color} was just amazing! Such expertise!"
    nvl clear
    dp "Anyway, it seems like our time is coming to an end. I hope you enjoyed the game!"
    dp "We certainly enjoyed having you."
    dp "Bye! ;)"
    "The wind from the approaching helicopter is too much to bear and you stumble backwards to receive it."
    play sound "sfx/helicopter.ogg" channel 1
    scene bg helicopter with dissolve
    "It lands after several minutes. The door of the cabin slides open."
    "You run up to the doorway and step inside ..."
    scene black
    stop ambience fadeout 3.0
    stop music
    play sound "sfx/hit1.ogg"
    stop sound fadeout 2.0 channel 1
    "The masked men immediately force a bag over your head and knock you unconscious with a strong blow to your skull."
    $ won_the_game = True
    jump credits
    
#GAME CREDITS
label credits:
    $ persistent.won_game = True
    $ cutscene(togglegui=True)
    stop sound fadeout 1.0
    play music "music/Rhythm_Stalker.ogg"
    scene static with intro_dissolve
    show credits_montage
    $ renpy.pause(0.5)
    
    #Writer
    show credit_text "writer: aleema" with dissolve
    play sound "sfx/scream_woman_distant.ogg"
    show screen blood0
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    #Character Artist
    show credit_text "character art:\nStarling, Junoju" with dissolve
    show screen blood7
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    play sound "sfx/scream_man_distant.ogg"
    #BG Artist
    show credit_text "bg art: guttari nyanko" with dissolve
    show screen blood3
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    #Coding
    show credit_text "coding: aleema" with dissolve
    show screen blood4
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    show screen blood5
    play sound "sfx/scream_woman_distant2.ogg"
    #Musicians
    show credit_text "music:\n{size=-10}National Hsin Chuang Senior High School Wind\nFrequency Orchestra\nkyro_sk\ndonniedrost\nanchormejans\nduckett{/size}" with dissolve
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    show screen blood1
    #Musicians
    show credit_text "music:\n{size=-10}koan69\nscmixer\nSackJo22\nthanvannispen\nspinmeister{/size}" with dissolve
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    show screen blood6
    play sound "sfx/scream_man_distant2.ogg"
    #Musician (ending song)
    show credit_text "ending song:\n{size=-10}\"rhythm stalker\" - koan69{/size}" with dissolve
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    #Foley Artists
    show credit_text "sound effects:\n{size=-10}fruitcake.hotel\nsuonho\nsidadrumbum\nAnton\njunggle\nHardPCM\nCorsica_S\nJake548\nFreqMan\nelonen\nERH\nJustinBW\nh.quinius\nwildweasel\nJoelAudio\nmartian\nplagasul\nLithe-Fider{/size}" with dissolve
    show screen blood0
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    play sound "sfx/scream_group_female.ogg"
    #Foley Artists
    show credit_text "sound effects:\n{size=-10}Erdie\nhiramjustus\njobro\nStreety\nJKirsch\nsnottyboi\nMike Koenig\nJim Rogers\nSonic\ngezortenplotz\nNoiseCollector\nfogma\nCGEffex\nKNO_SFX\nVosvoy\nOmar Alvarado\nnextmaking\nEMSIarma\nTimbre{/size}" with dissolve
    show screen blood1
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    #Foley Artists
    show credit_text "sound effects:\n{size=-10}xyzr_kx\nPhreaKsAccount\nKrisboruff\nOpossum\nAndrew_Duke\nsagetyrtle\npagancow\nBenboncan\npauliep83\nWillHiccups\nJace\nIncarnadine\nConnum\nstijn\nMarianne Gagnon\nbattlestar10\nDouglas Vicente\nCaroline Ford\nStephan Schutze{/size}" with dissolve
    show screen blood7
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    play sound "sfx/scream_man_pain_distant.ogg"
    #Foley Artists
    show credit_text "sound effects:\n{size=-10}M-RED\nKoops\ndigifishmusic\nSyna_Max\nmzoern1\nljudman\nthanvannispen\nRobinhood76\nUncleSigmund\ncdrk\nmalexmedia\nmrjingles\nJustinBW \nreinsamba\nroscoetoon\nRoyal\nluftrum\nsea-fury\nkijjaz\nnathan-lomeli\nandre-rocha{/size}" with dissolve
    show screen blood4
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    #Misc Credits
    show credit_text "icon stock:\n{size=-10}superjiaojiao\nstockchroma\nprolific_stock\nISOStock\nCDuck2\nravenarcana\nm10tje{/size}" with dissolve
    show blood2 behind credit_text with dissolve
    $ renpy.pause(3.0)
    hide blood2 with dissolve
    $ renpy.pause(2.0)
    hide credit_text with dissolve
    #Misc Credits
    show credit_text "font: Devin Cook\n\nphotoshop brushes:\n{size=-10}AnnFrost\nScully7491\nShad0ws{/size}" with dissolve
    show screen blood5
    $ renpy.pause(5.0)
    hide credit_text with dissolve
    play sound "sfx/scream_group.ogg"
    #Engine Credit
    show credit_text "powered by ren'py" with dissolve
    hide credit_text with slowdissolve
    play sound "sfx/glass_break.ogg"
    hide credits_montage
    hide screen blood5
    show glass_crack
    $ renpy.pause(1.5, hard=True)
    play sound "sfx/glass_shatter.ogg"
    $ renpy.pause(0.7, hard=True)
    scene black
    $ renpy.pause(2.0)
    if won_the_game or won_game_name or won_game_destroy: #Bonus items if you've actually "won the game"
        play sound "sfx/beep_win.ogg"
        show screen bonus_items
        $ renpy.pause()
        hide screen bonus_items
        if won_the_game:
            memo "Because you're a muderous fiend, you'll now be able to play deathmatches with no story."
            memo "You're welcome. ;)"
        $ won_the_game = False
        $ won_game_destroy = False
        $ won_game_name = False
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    
#if you've WON THE GAME, shown after credits
screen bonus_items: 
    modal True
    zorder 100
    vbox:
        xpos .5 ypos .5
        xanchor 0.5 yanchor 0.5
        text "{color=#FFF}{u}You've unlocked a new item!{/u}{/color}" xpos 0.5 xanchor 0.5 size 22
        text "There will now be a chance to receive this item in your duffle bag." xpos 0.5 xanchor 0.5 size 15 text_align 0.5
        null height 3
        hbox:
            xcenter 0.5
            if won_the_game: #killed everyone
                frame:
                    xpos .5 ypos .5
                    xanchor 0.5 yanchor 0.5
                    has vbox
                    add "icons/flamethrower.jpg" xalign 0.5
                    text "Flamethrower" xalign 0.5
            if won_game_destroy: #destroyed the computer
                frame:
                    xpos .5 ypos .5
                    xanchor 0.5 yanchor 0.5
                    has vbox
                    add "icons/tommy.jpg" xalign 0.5
                    text "Tommy Gun" xalign 0.5
            if won_game_name: #did what computer told you to
                frame:
                    xpos .5 ypos .5
                    xanchor 0.5 yanchor 0.5
                    has vbox
                    add "icons/machinegun.jpg" xalign 0.5
                    text "Machine Gun" xalign 0.5
        textbutton "Continue" xminimum 100 action Return(0) xpos 0.5 xanchor 0.5
    
    
init python:
    def save_name_funct():
        global save_name
        save_name = "> Day {color=#00ff00}"+str(day)+"{/color} Hour {color=#00ff00}"+str(hour)+"{/color}\n> {color=#ff0000}"+str(players_alive)+"{/color} Players Alive"
    config.overlay_functions.append(save_name_funct)  
    
    
