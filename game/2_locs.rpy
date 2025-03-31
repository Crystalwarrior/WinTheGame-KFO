######################################
###################################### LOCATIONS #
######################################

label game_init_locs:
    python:
        ##################
        ## INSTRUCTIONS ##
        ##################
        ## There are 2 types of locations, "grid" and "room". Grid is the general square of land that the map is divided into. Rooms can be inside of grids, or inside other rooms.
        ## The map system requires that you have a map of the entire game location and that it can be divided into squares.
        
        #Size of map grid
        grid_x = 7 #columns (letters)
        grid_y = 4 #rows (numbers)
        
        ##"GRID"
        # Letter - the grid letter, as written in quotations
        # Number - the grid number, as an integer
        # X - X position of the top left corner of the grid square on overall map image
        # Y - Y position of the top left corner of the grid square on overall map image
        # BG image - defined as an image somewhere else, name only
        # Ambience - a background sound specfic to this location; * in "sfx/*.ogg" (Required)
        # Landmark - name of a landmark in this grid, if it exists (optional)
        # Landmark X -  X postion of the landmark image on the overall map (required if there's a landmark)
        # Landmark Y - Y postion of the landmark image on the overall map (required if there's a landmark)
        # Items - list of items in this location (default: []  empty)

        ##"ROOM"
        # Name - What the player will see on the "Enter _____" button
        # Parent Location - where you can find this room. This is usually a grid location, but you can place rooms inside of room by setting the parent to a room that's previously defined
        # BG image - defined as an image somewhere else, name only
        # Ambience - a background sound specfic to this location; * in "sfx/*.ogg" (default: the sound of the parent, volume reduced)
        # Items - list of items in this location (default: []  empty)
        # Visibility - # between 1 and 10 that describes how obvious and attractive the room is to outsiders. The higher the number, the more likely a student will go into it. (default = 5)
        # Can Sleep? - Can the player sleep here? (default: False)
        # Enter SFX - Sound for entering this room; * in "sfx/*.ogg" (default is a door opening)    
        # Exit SFX  - Sound for leaving this room; * in "sfx/*.ogg" (default is a door closing)    
        # Exit Location  - Use this if, for some reason, you want the player to end up at a certain location when they exit instead of their technical parent location

        
        a1 = location( #GRID
            "a", #Letter
            1, #Number
            93, #X
            96, #Y
            "bathhouse", #BG image
            "grassland", #ambience in sfx/ folder
            landmark="bathhouse", #I plan for this location to have a bathhouse that will be noted in the map screen
            landmark_x=130, #X pos of the bathhouse marker
            landmark_y=150  #Y pos of the bathhouse marker
            )
        
        rm_bathhouse = room(# ROOM
            "Bathhouse", #Name
            a1, #Parent loc
            "onsen", #BG image
            visibility = 9 #Visibility ... it's very visible and the AI will gravitate towards it
            )
        
        rm_lockers = room("Lockers",rm_bathhouse, "lockers_ladies",ambience="room_tone1",item_list=[[key_copper,1]], visibility = 7, can_sleep=True, enter_sound="door_slide", exit_sound="door_slide2") #room
        rm_showers = room("Wash Area",rm_lockers, "showers",ambience="dripping",item_list=[[firstaid,1]], visibility = 5, enter_sound="door_slide", exit_sound="door_slide2") #room
        a2 = location("a",2,93,197, "bridge","grassland",landmark="bridge",landmark_x=130,landmark_y=205,item_list=[])
        a3 = location("a",3,93,298, "station","grassland",landmark="station",landmark_x=140,landmark_y=350,item_list=[[lantern,1]])
        rm_station= room("Station",a3, "train_station",item_list=[[gas,1]], visibility = 7, can_sleep=True) #room
        a4 = location("a",4,93,400,"trees","ocean",item_list=[])
        
        b1 = location("b",1,194,96,"graveyard","grassland",item_list=[])
        b2 = location("b",2,194,197, "grassland","grassland2",item_list=[[stick,1]])
        b3 = location("b",3,194,298,"farm","grassland4",landmark="farm",landmark_x=205,landmark_y=330,item_list=[])
        rm_shed = room("Shed",b3, "shed",item_list=[[trap,1],[shotgun_sawed,1]]) #room
        b4 = location("b",4,194,400, "school","grassland",landmark="school",landmark_x=197,landmark_y=415,item_list=[])
        rm_corridor = room("School",b4, "corridor",item_list=[], visibility = 7) #room
        rm_classroom = room("Classroom",rm_corridor, "classroom",item_list=[[helmet,1]], visibility = 6) #room
        rm_teacher = room("Teachers' Room",rm_classroom, "teachers_room", item_list=[[cigarettes,1]], visibility = 4, can_sleep=True, dump_loc=rm_corridor) #room
        
        c1 = location("c",1,295,96, "cabin","forest",landmark="shack",landmark_x=310,landmark_y=115,item_list=[])
        rm_shack = room("Shack",c1, "shack",item_list=[], visibility = 6, can_sleep=True) #room
        c2 = location("c",2,295,197,"forest","forest",item_list=[[wood,1]])
        c3 = location("c",3,295,298, "old_clock","grassland",landmark="cityhall",landmark_x=310,landmark_y=350,item_list=[[rope,1]])
        rm_city_hall = room("City Hall",c3, "city_hall",item_list=[[paper,1],[matches,1]], visibility = 8, can_sleep=True) #room
        c4 = location("c",4,295,400,"pier","ocean", landmark="pier",landmark_x=340,landmark_y=430,item_list=[])
        
        d1 = location("d",1,396,96, "cliff","ocean",item_list=[])
        d2 = location("d",2,396,197, "waterfall","waterfall",landmark="waterfall",landmark_x=400,landmark_y=210,item_list=[])
        d3 = location("d",3,396,298,"farm2","grassland4",landmark="house1",landmark_x=425,landmark_y=335,item_list=[])
        rm_house = room("Old House",d3, "old_kitchen",item_list=[[wood,1]], visibility = 6, can_sleep=True) #room
        d4 = location("d",4,396,400,"ruins","grassland",item_list=[[wood,1]])      
        d5 = location("d",5,396,500,"gate","grassland",landmark="gate",landmark_x=440,landmark_y=510,item_list=[])
        
        e1 = location("e",1,498,96, "cliff2","ocean_cliff",item_list=[])
        e2 = location("e",2,496,197,"forest3","grassland2",item_list=[])
        e3 = location("e",3,496,298,"cabins","forest", landmark="cabins",landmark_x=535,landmark_y=350,item_list=[])
        rm_cabin = room("Cabin",e3, "old_room",item_list=[[radio,1],[food,2],[key_silver,1]], visibility = 7, can_sleep=True) #room
        e4 = location("e",4,499,400,"ponds","ocean",landmark="lighthouse",landmark_x=510,landmark_y=455,item_list=[])
        rm_lighthouse = room("Lighthouse",e4, "lighthouse",item_list=[[lantern,1],[wood,1]], visibility = 3, enter_sound="swim", exit_sound="swim_out", can_sleep=True) #room
        e5 = location("e",5,499,500,"mansion","grassland",landmark="backgate",landmark_x=497,landmark_y=525,item_list=[])
        
        f1 = location("f",1,599,96,"teahouse","grassland3",landmark="shrine",landmark_x=640,landmark_y=150,item_list=[])
        rm_shrine = room("Shrine",f1, "shrine","grassland3",item_list=[[firstaid,1]],can_sleep=True) #room
        f2 = location("f",2,599,197,"graveyard2","grassland",landmark="graveyard",landmark_x=605,landmark_y=250,item_list=[])
        f3 = location("f",3,599,298,"cave","grassland",landmark="cave",landmark_x=635,landmark_y=330,item_list=[])
        rm_cave = room("Cave",f3, "cave_int","cave",item_list=[[dynamite,2],[wood,1]], visibility = 3, enter_sound="walk_gravel", exit_sound="walk_gravel") #room
        f4 = location("f",4,599,400,"farm3","ocean",landmark="house2",landmark_x=610,landmark_y=425,item_list=[])
        rm_house2 = room("House",f4, "fireplace",item_list=[[wood,1],[food,1]], visibility = 7, can_sleep=True) #room
        rm_tea = room("Tea House",rm_house2, "tea_house",ambience="room_tone1",item_list=[[food,1]], can_sleep=True) #room
        
        g1 = location("g",1,701,97,"sakura","ocean_cliff",item_list=[])
        g2 = location("g",2,701,197,"grass_path","grassland2",item_list=[])
        g3 = location("g",3,701,298,"hospital","grassland",landmark="hospital",landmark_x=700,landmark_y=350,item_list=[])
        rm_hospital = room("Hospital",g3, "lab","room_tone1",item_list=[[firstaid,1]], visibility = 8, can_sleep=True) #room
        g4 = location("g",4,701,400,"shrine_little","grassland2",landmark="shrine",landmark_x=690,landmark_y=405,item_list=[])
        
        #Locked Locations
        rm_cabin.keys = [key_copper]
        rm_cabin.key_phrase = "The copper door knob won't turn, as if it is locked. Maybe you can find a key."
        rm_cabin.key_use_phrase = "You easily unlock the door with the copper key. The door requires some effort to push, but you get inside."
        rm_shed.keys = [key_silver]
        rm_shed.key_phrase = "The doors won't open. There is a silver-plated hole for a key to fit on one of them."
        rm_shed.key_use_phrase = "The silver key works in unlocking the doors. The shed is open to you."
        rm_cave.keys = [lantern,lighter]
        rm_cave.key_phrase = "It's too dark. You'll need a source of light to go any further."
        rm_cave.key_use_phrase = "You raise your lantern and continue."
        
        
        #Map grid
        #Just make a matrix like your map grid, with brackets for each row
        grid = [
        [a1,b1,c1,d1,e1,f1,g1],
        [a2,b2,c2,d2,e2,f2,g2],
        [a3,b3,c3,d3,e3,f3,g3],
        [a4,b4,c4,d4,e4,f4,g4],]
        
        #Shoreline
        ## For events that require you to be near the coast or a cliff (this isn't automated because just because you're in a zone on the coast doesn't mean the location in the BG is)
        # Cliffs allow you to jump to your death for optional suicide (requires low sanity)
        # Shores will let the campaign know if you can go into an ocean safely (useful if the map is an island)
        b1.cliff = True
        d1.cliff = True
        e1.cliff = True
        g1.cliff = True
        a2.cliff = True
        a4.shore = True
        c4.shore = True
        d4.shore = True
        e4.shore = True
        f4.shore = True
        g4.shore = True
        d5.shore = True
        e5.shore = True
        
        #Forest
        # For wood chopping activities. If True, allows you to chop wood if you have an axe.
        c1.forest = True
        c2.forest = True
        e2.forest = True
        e3.forest = True
        
        #mini-map coordinates
        a1.minimap_x = 25
        a1.minimap_y = 26
        a2.minimap_x = 25
        a2.minimap_y = 54
        a3.minimap_x = 25
        a3.minimap_y = 82
        a4.minimap_x = 25
        a4.minimap_y = 110
        
        b1.minimap_x = 54
        b1.minimap_y = 26
        b2.minimap_x = 54
        b2.minimap_y = 54
        b3.minimap_x = 54
        b3.minimap_y = 82
        b4.minimap_x = 54
        b4.minimap_y = 110
        
        c1.minimap_x = 81
        c1.minimap_y = 26
        c2.minimap_x = 81
        c2.minimap_y = 54
        c3.minimap_x = 81
        c3.minimap_y = 82
        c4.minimap_x = 81
        c4.minimap_y = 110
        
        d1.minimap_x = 109
        d1.minimap_y = 26
        d2.minimap_x = 109
        d2.minimap_y = 54
        d3.minimap_x = 109
        d3.minimap_y = 82
        d4.minimap_x = 109
        d4.minimap_y = 110
        d5.minimap_x = 109
        d5.minimap_y = 138
        
        e1.minimap_x = 137
        e1.minimap_y = 26
        e2.minimap_x = 137
        e2.minimap_y = 54
        e3.minimap_x = 137
        e3.minimap_y = 82
        e4.minimap_x = 137
        e4.minimap_y = 110
        e5.minimap_x = 137
        e5.minimap_y = 138
        
        f1.minimap_x = 165
        f1.minimap_y = 26
        f2.minimap_x = 165
        f2.minimap_y = 54
        f3.minimap_x = 165
        f3.minimap_y = 82
        f4.minimap_x = 165
        f4.minimap_y = 110
        
        g1.minimap_x = 193
        g1.minimap_y = 26
        g2.minimap_x = 193
        g2.minimap_y = 54
        g3.minimap_x = 193
        g3.minimap_y = 82
        g4.minimap_x = 193
        g4.minimap_y = 110

    return


######################################
############# GAME CODE ############# 
######################################

init python:
    def move_to_grid(newloc): #move you to a grid loc
        global loc
        global this_is_a_new_loc
        global party
        global music_steps
        global fz_ticker
        global day
        global hour
        global fz_start_day
        global fz_start_hour
        global show_report
        if loc.type == "room":
            if loc.exit_sfx is None: #play sound of leaving the room, default is a door sound
                renpy.sound.play("sfx/door_close.ogg", channel="system2")
            else:
                renpy.sound.play("sfx/"+loc.exit_sfx+".ogg", channel="system2")
        else:
            renpy.sound.play("sfx/walk.ogg", channel="system2")
        renpy.scene()
        renpy.show("black")
        renpy.transition(dissolve)
        renpy.pause(0.5)
        if moving_boat and not (Mari in party or Mari.loc == loc) and not (Jun in party or Jun.loc == loc):
            add_time(3) #Super extra time for moving the boat alone because friendship rules
        elif moving_boat:
            add_time(2) #Extra time for moving the boat because it's heavy and stuff
        else:
            add_time(1) #Advance time 1 hour for traveling to a new grid location

        loc = newloc
        for x in classmates:
            if x == you:
                x.loc = newloc #moves your avatar
        for i in party:
            i.loc = newloc #Sets your party member's loc
        if not newloc.found:
            this_is_a_new_loc = True #in case you want events when you first discover someplace
            
        music_steps += 1
        if music_steps > 5:
            music_steps = 0
            ambient_music()

        renpy.jump("grid_loc")
        
    def move_to_room(newloc): #move you to a room
        global loc
        global this_is_a_new_loc
        global party
        renpy.scene()
        renpy.show("black")
        renpy.transition(dissolve)
        renpy.pause(0.5)
        loc = newloc
        for x in classmates:
            if x == you:
                x.loc = newloc
        for i in party:
            i.loc = newloc
        if not newloc.found:
            this_is_a_new_loc = True
        renpy.jump("room_loc")
        
    def ambient_music():
        global ambient_music_tracks
        play_this_song = renpy.random.choice(ambient_music_tracks)
        renpy.music.queue(play_this_song, loop=False, clear_queue=True, fadein=6.0)
        
init:
    $ movement_keys = False
        
label move_north:
    $ movement_keys = False
    $ move_to_grid(north_loc)
    
label move_north2:
    $ movement_keys = False
    if sanity >= 40:
        "That way leads to a {color=#FF0000}forbidden zone{/color} and would mean certain death."
    else:
        "Are you sure? That way leads to a {color=#FF0000}forbidden zone{/color}."
        menu:
            "Yes, go":
                $ move_to_grid(north_loc)
            "No, don't go":
                pass
    $ movement_keys = True
    return
    
label move_south:
    $ movement_keys = False
    $ move_to_grid(south_loc)
    
label move_south2:
    $ movement_keys = False
    if sanity >= 40:
        "That way leads to a {color=#FF0000}forbidden zone{/color} and would mean certain death."
    else:
        "Are you sure? That way leads to a {color=#FF0000}forbidden zone{/color}."
        menu:
            "Yes, go":
                $ move_to_grid(south_loc)
            "No, don't go":
                pass    
    return
    
label move_east:
    $ movement_keys = False
    $ move_to_grid(east_loc)
    
label move_east2:
    $ movement_keys = False
    if sanity >= 40:
        "That way leads to a {color=#FF0000}forbidden zone{/color} and would mean certain death."
    else:
        "Are you sure? That way leads to a {color=#FF0000}forbidden zone{/color}."
        menu:
            "Yes, go":
                $ move_to_grid(east_loc)
            "No, don't go":
                pass    
    $ movement_keys = True
    return
    
label move_west:
    $ movement_keys = False
    $ move_to_grid(west_loc)
    
label move_west2:
    $ movement_keys = False
    if sanity >= 40:
        "That way leads to a {color=#FF0000}forbidden zone{/color} and would mean certain death."
    else:
        "Are you sure? That way leads to a {color=#FF0000}forbidden zone{/color}."
        menu:
            "Yes, go":
                $ move_to_grid(west_loc)
            "No, don't go":
                pass    
    $ movement_keys = True
    return
    
label enter_room:
    $ movement_keys = False
    $ room_here.find()
    if room_here.keys != []:
        python:    
            have_key = False
            for x in inventory:
                if x[0] in room_here.keys:
                    have_key = True
            if have_key:
                renpy.say(None,room_here.key_use_phrase)
                if room_here != rm_cave: #everything but the cave stays unlocked
                    for x in inventory:
                        if x[0] in room_here.keys:
                            x[0].destroy(1)
                    room_here.keys = []
                move_to_room(room_here)
            else:
                renpy.say(None,room_here.key_phrase)
        jump grid_loc
    if room_here.enter_sfx is None: #play sound of leaving the room, default is a door sound
        play sound "sfx/door_open.ogg" channel "system2"
    else:
        $ renpy.sound.play("sfx/"+room_here.enter_sfx+".ogg", channel="system2")
    $ move_to_room(room_here)
    
label exit_room:
    $ loc.dump()
    
label error_sound:
    play sound "sfx/beep_double2.ogg"
    if loc.type == "grid":
        jump grid_loc
    else:
        jump room_loc
    

    
##############
## GRID LOC ##
##############
#This is the base for every grid location. It gets its unique values from the information you supplied in the locations definitions.
        
label grid_loc:
    $ uncutscene()
    $ calculatesanitysound()
    if loc.type == "room": #just in case here by mistake
        jump room_loc
    $ find_all_pop()
    show screen health
    hide screen health_enemy     
    hide screen health_enemy2
    $ loc.find() #find this place if you haven't already
    $ loc_bg = loc.bg #custom bg for this loc
    $ loc_sound = "sfx/"+loc.sfx+".ogg" #custom ambience for this loc
    $renpy.scene()
    $renpy.show(loc_bg)
    #$ renpy.transition(dissolve)
    $ renpy.music.set_volume(1.0, 0, channel="ambience")
    $renpy.music.play(loc_sound,channel="ambience", fadeout=1.0,fadein=1.0)
    
    python: #Find out if there are non-party members at the loc
        strangers_here = False
        strangers = []
        for x in loc.pop:
            if x.alive and x != you and x not in followers:
                strangers.append(x)
                strangers_here = True

    #People around you react to murder
    if just_murdered_someone:
        $ just_murdered_someone = False
        if len(party) > 0:
            call murder_follower_reaction
        if strangers_here:
            "Those around you are horrified by what they've seen."
            python:
                for i in strangers:
                    # i.make_foe(you)
                    i.move("rand")
                    renpy.say(None,"%s goes %s."%(i.name,escape_plan))
                        
    if trap_caught_person != None and trap_loc == loc:
        jump trap_fight
             
    #If someone's here while you're carrying the boat
    if moving_boat and strangers_here:
        $ boat_attacker = strangers[0]
        jump boat_fight

    #Forbidden Zone Reports Trigger
    if show_report:
        $ show_report = False
        $ time_for_fz()
        
    
    
    if persistent.show_click_person_tut:
        $ persistent.show_click_person_tut = False
        memo "You can now move freely around the island.\nWell, almost freely."
        memo "You may encounter other players while moving around. Simply click on them to interact with them. Unless they're dead."
        memo "Use the menu buttons to move around, east, west, north, and south, or use {color=#00ff00}W{/color}, {color=#00ff00}A{/color}, {color=#00ff00}S{/color}, {color=#00ff00}D{/color} on your keyboard. Press {color=#00ff00}E{/color} to enter rooms, {color=#00ff00}Q{/color} to exit."
        memo "Go get 'em, slugger. ;)"

    #Are there items here?
    if len(loc.items) > 0:
        $ there_are_items = True
        $ items_here = loc.items
    else:
        $ there_are_items = False
        
    #Are there bodies here?
    if len(loc.bodies) > 0:
        $ there_are_bodies = True
        $ bodies_here = loc.bodies
    else:
        $ there_are_bodies = False
    
    #Is there a room here?
    $ room_here = None
    python:
        for i in locations:
            if i.type == "room":
                if i.parent == loc:
                    if loc == d2:
                        if found_waterfall:
                            room_here = i
                    else:
                        room_here = i
    if room_here is not None:
         $ room_name = room_here.name
         $ room_name = room_name.title()

    # DETERMINING THE EXITS
    #North
    if loc.exit_north is not None:
        if loc.exit_north == a1 and not you_can_cross_bridge and Hitomo.alive and Hitomo.loc == loc: #special condition for the bridge sequence
            $ show_north = False
        else:
            $ show_north = True
            $ north_loc = loc.exit_north
            if loc.exit_north == a1:
                $ north_exit = "Across Bridge [[North]"
            else:
                $ north_exit = "North"
    else:
        $ show_north = False
    #South
    if loc.exit_south is not None:
        $ show_south = True
        $ south_loc = loc.exit_south
        $ south_exit = "South"
    else:
        $ show_south = False
    #East
    if loc.exit_east is not None:
        $ show_east = True
        $ east_loc = loc.exit_east
        $ east_exit = "East"
    else:
        $ show_east = False
    #West
    if loc.exit_west is not None:
        $ show_west = True
        $ west_loc = loc.exit_west
        $ west_exit = "West"
    else:
        $ show_west = False
        
    #Check if there are events to show, REQUIRED!
    call events_run_period 
    
    if this_is_a_new_loc: #Turn off the "new loc" flag
        $ this_is_a_new_loc = False

    call events_run_period #CHECK FOR EVENTS, again, after showing who's here
    $ show_drop_stuff = True
    $ movement_keys = True
    call say_people_here #Showing and announcing who is in the location
    menu:# This is where we show the menu options
        "Put Boat In Water" if moving_boat and loc.shore:
            $ movement_keys = False
            jump boat_in_water
        "Get Boat" if loc == boat_coast_loc:
            $ movement_keys = False
            menu:
                "Move it somewhere else":
                    call shed_boat_move
                "Push boat out to sea":
                    jump boat_in_water
        "Commit Suicide" if sanity < 25 and loc.cliff:
            $ movement_keys = False
            "You walk towards the steep cliff. You look down and see sweet relief."
            if (Jun in party or Jun.loc == loc):
                jun sad "... What are you doing?"
            if (Mari in party or Mari.loc == loc):
                # Mari will jump with you if her sanity is also low
                if Mari.sanity <= 50:
                    "You look over at Mari but you can see that she was already so incredibly sad. Nothing you do now could make her any sadder."
                    "She walks closer to you and holds out her hand."
                    "You take it."
                # Otherwise, she'll actually *save* you and make you reconsider.
                else:
                    mari scared "S-Shinobu!"
                    "She walks closer to you and holds out her hand."
                    "You take it."
                    mari "Please... Don't do this."
                    "She looks at you straight in the eyes."
                    $ add_sanity(20)
                    "You feel relieved. Perhaps there's a point to keep on living, at least for a while longer."
                    "You walk away from the cliff with Mari."
                    if (Jun in party or Jun.loc == loc):
                        jun sad "Jeez, man! You two scared the crap out of me!"
                        jun "I thought you were gonna jump or somethin'..."
                        $ add_sanity(10)
                        "You chuckle at how bluntly he put it."
                    # You spooked the heck out of Mari. She's gonna jump with you next time.
                    $ Mari.sanity = max(0, Mari.sanity - 50)
                    jump grid_loc
            "You look out at the ocean. There was a home somewhere across that water. A home you will never see again."
            if (Jun in party or Jun.loc == loc):
                y none "Good bye."
                jun scared "Good - what!?"
            "You step forwards and plummet straight down."
            if (Mari in party or Mari.loc == loc) and Mari.sanity <= 50:
                "Mari is right beside you."
            scene black with dissolve
            $ show_blood()
            jump game_over
                
        "Enter %(room_name)s" if room_here is not None:
            call enter_room
        "Retrieve Bear Trap" if trap_set and trap_loc == loc:
            $ movement_keys = False
            call bear_trap_info
        "Make Wish" if loc == g4 and not made_wish:
            $ movement_keys = False
            jump wish_tree
        "Chop Wood [[3 hours]" if axe.is_in_inventory() and loc.forest:
            $ movement_keys = False
            play sound "sfx/hammer.ogg"
            "You take your axe and harvest the best-looking wood in the area."
            $ add_time(3)
            $ wood.add()
        "Wait in Camouflage" if armor == camo:
            $ movement_keys = False
            "You blend into the surroundings."
            call screen wait_prompt
            $ amount = _return
            if amount != 0:
                $ wait(amount)
            else:
                pass
        "{image=gui/north.png} Go  %(north_exit)s {image=gui/north.png}" if show_north and not north_loc.forbidden or show_north and sanity <= 20:
            call move_north
        "{image=gui/north.png} {color=#FF0000}Go %(north_exit)s{/color} {image=gui/north.png}" if show_north and north_loc.forbidden and sanity > 20:
            call move_north2
        "{image=gui/east.png} Go %(east_exit)s {image=gui/east.png}" if show_east and not east_loc.forbidden or show_east and sanity <= 20:
            call move_east
        "{image=gui/east.png} {color=#FF0000}Go %(east_exit)s{/color} {image=gui/east.png}" if show_east and east_loc.forbidden and sanity > 20:
            call move_east2
        "{image=gui/west.png} Go  %(west_exit)s {image=gui/west.png}" if show_west and not west_loc.forbidden or show_west and sanity <= 20:
            call move_west
        "{image=gui/west.png} {color=#FF0000}Go %(west_exit)s{/color} {image=gui/west.png}" if show_west and west_loc.forbidden and sanity > 20:
            call move_west2
        "{image=gui/south.png} Go  %(south_exit)s {image=gui/south.png}" if show_south and not south_loc.forbidden or show_south and sanity <= 20:
            call move_south
        "{image=gui/south.png} {color=#FF0000}Go %(south_exit)s{/color} {image=gui/south.png}" if show_south and south_loc.forbidden and sanity > 20:
            call move_south2
    $ show_people_here = False
    jump grid_loc
    
label bear_trap_info:
    
    if trap_caught_person != None:
        jump trap_fight
    elif day >= needs_to_be[0] and hour >= needs_to_be[1] and trap_caught_person == None:
        "Your trap has captured a deer."
        $ meat.add()
        "You scavange raw meat. It will need to be cooked before you can eat it."
        $ trap_set = False
        $ trap_loc = None
    else:
        play sound "sfx/beep_double.ogg"
        memo "This trap is set and waiting. Come back later when it has sprung."
    return
    
###############
## ROOM LOC ##
###############
#Same as grid_loc, but this is specific to rooms
    
label room_loc:
    $ uncutscene()
    $ calculatesanitysound()
    if loc.type == "grid": #just in case here by mistake
        jump grid_loc
    show screen health
    hide screen health_enemy     
    hide screen health_enemy2
    $ find_all_pop()
    $ loc.find()
    $ loc_bg = loc.bg
    if loc.sfx is not None:
        $ loc_sound = "sfx/"+loc.sfx+".ogg"
    elif loc.parent.type =="grid":
        $ renpy.music.set_volume(0.25, .5, channel="ambience")
        $ loc_sound = "sfx/"+loc.parent.sfx+".ogg"
    $renpy.scene()
    $renpy.show(loc_bg)

    $ renpy.music.play(loc_sound,channel="ambience", fadeout=1.0,fadein=1.0)
    python: #Find out if there are non-party members at the loc
        strangers_here = False
        strangers = []
        for x in loc.pop:
            if x.alive and x != you and x not in followers:
                strangers.append(x)
                strangers_here = True
    
    #People around you react to murder
    if just_murdered_someone:
        $ just_murdered_someone = False
        if len(party) > 0:
            call murder_follower_reaction
        if strangers_here:
            "Those around you are horrified by what they've seen."
            python:
                for i in strangers:
                    # i.make_foe(you)
                    i.move("rand")
                    renpy.say(None,"%s goes %s."%(i.name,escape_plan))
                        
    #If someone's here while you're carrying the boat
    if moving_boat and strangers_here:
        $ boat_attacker = strangers[0]
        jump boat_fight
  
    #Forbidden Zone Reports Trigger
    if show_report:
        $ show_report = False
        $ time_for_fz()
        
    #Are there items here?
    if len(loc.items) > 0:
        $ there_are_items = True
        $ items_here = loc.items
    else:
        $ there_are_items = False
        
    #Are there bodies here?
    if len(loc.bodies) > 0:
        $ there_are_bodies = True
        $ bodies_here = loc.bodies
    else:
        $ there_are_bodies = False
    
    #Is there a room here?
    $ room_here = None
    python:
        for i in locations:
            if i.type == "room":
                if i.parent == loc:
                    room_here = i
    if room_here is not None:
         $ room_name = room_here.name
         $ room_name = room_name.title()
        
    call events_run_period #CHECK FOR EVENTS

    $ show_north = False
    $ show_south = False
    $ show_east = False
    $ show_west = False
    
    if persistent.show_room_tut:
        $ persistent.show_room_tut = False
        memo "You're inside of a room right now. You can wait or sleep (sometimes) in rooms you find."
        memo "{color=#FFFFFF}Sleeping{/color} restores your health, but you'll be very vulnerable. Unless you find a good hiding spot, that is.\n\n{color=#FFFFFF}Waiting{/color} keeps you on your toes so you can be prepared for anyone looking for you, but that's a bit harsh on your sanity."
        memo "Anyway. To go outside, you have to hit the \"Exit\" button at the bottom of the list."
                    
    call events_run_period #CHECK FOR EVENTS, again, after showing who's here
    $ show_drop_stuff = True
    $ movement_keys = True

    call say_people_here #Showing and announcing who is in the location
    menu:     
        "Repair Boat" if loc == rm_shed and boat_repair < 3 and not boat_missing:
            call shed_repair
            
        "Move Boat" if loc == rm_shed and boat_repair > 2 and not boat_missing and not boat.is_in_inventory():
            call shed_boat_move
            
        
            
        "Enter %(room_name)s" if room_here is not None:
            if room_here.enter_sfx is None: #play sound of leaving the room, default is a door sound
                play sound "sfx/door_open.ogg" channel "system2"
            else:
                $ renpy.sound.play("sfx/"+room_here.enter_sfx+".ogg", channel="system2")
            $ move_to_room(room_here)
        "Use Stove" if loc == rm_house or loc == rm_house2:
            call using_stove

        "{image=gui/wait.png} Wait":
            call screen wait_prompt
            $ amount = _return
            if amount != 0:
                $ wait(amount)
            else:
                pass
        "{image=gui/sleep.png} Rest" if loc.can_sleep:
            if strangers_here:
                "Can't sleep with strangers around."
            else:
                call screen sleep_prompt
                $ amount = _return
                if amount != 0:
                    $ sleep(amount)
                else:
                    pass
        "{image=gui/exit.png} Exit":
            call exit_room
    $ show_people_here = False
    jump room_loc
                
label using_stove:
    if meat.is_in_inventory():
        if wood.is_in_inventory():       
            $ wood.use_sfx()
            play sound "sfx/cook.ogg"
            $ wood.consume()
            $ renpy.pause(1.0)
            $ meat.destroy(1)
            $ renpy.pause(1.0)
            $ cooked_meat.add()
            "You cook the meat, maybe a bit too much, and it now looks edible."
        else:
            memo "You need wood to start a fire."
    else:
        memo "You have nothing to cook."
    return
    

    
init -2 python:
    ## LOCATIONS ##
    class location(store.object):
        def __init__(self,n1,n2, coor1, coor2,bg_name,ambience,landmark=None, landmark_x =0, landmark_y =0,item_list=[]):
            global locations
            self.type = "grid"
            self.letter = n1
            self.number = n2
            self.name = n1+str(n2)
            self.found = False
            self.forbidden = False
            self.landmark = landmark
            self.items = item_list
            self.bodies = []
            self.bg = bg_name
            self.sfx = ambience
            #top-left corner of grid
            self.x = coor1
            self.y = coor2
            #top-left corner of landmark
            self.place_x = landmark_x
            self.place_y = landmark_y
            self.exits = []
            self.exit_north = None
            self.exit_south = None
            self.exit_east = None
            self.exit_west = None
            locations.append(self)
            self.pop = []
            
            self.minimap_x = 0    
            self.minimap_y = 0
                
            self.room = None
            self.zone = self
            self.shore = False #on the coast?
            self.cliff = False #has a steep cliff (you can jump off of)?
            self.forest = False #has wood to chop
            
        def forbid(self):
            self.forbidden = True
            if self.room is not None:
                self.room.forbidden = True
            
        def unforbid(self):
            self.forbidden = False
            if self.room is not None:
                self.room.forbidden = False
            
        def find(self):
            self.found = True
            #self.find_exits()
            
        def find_exits(self):
            global grid_y
            global grid_x
            loc_x = 0
            loc_y = 0
            
            for i in range(0,grid_y):
                for x in range(0,grid_x):
                    if grid[i][x] == self:
                        loc_x = x
                        loc_y = i
            if loc_y != 0:
                new_exit = grid[(loc_y-1)][loc_x]
                self.exits.append(new_exit)
                self.exit_north = new_exit
            if loc_y != (grid_y-1):
                new_exit = grid[(loc_y+1)][loc_x]
                self.exits.append(new_exit)
                self.exit_south = new_exit
            if loc_x != 0:
                new_exit = grid[loc_y][(loc_x-1)]
                self.exits.append(new_exit)
                self.exit_west = new_exit
            if loc_x != (grid_x-1):
                new_exit = grid[loc_y][(loc_x+1)]
                self.exits.append(new_exit)
                self.exit_east = new_exit
                
    ## ROOM ##
    class room(store.object):
        def __init__(self,place,parent,bg_name,ambience=None,item_list=[],visibility=5,can_sleep=False,enter_sound=None, exit_sound=None, dump_loc=None):
            global locations
            self.type = "room"
            self.parent = parent
            self.found = False
            self.name = place
            self.items = item_list
            self.bodies = []
            self.bg = bg_name
            self.sfx = ambience
            if dump_loc is None:
                self.exit = parent
            else:
                self.exit = dump_loc
            self.can_sleep = can_sleep
            self.visibility = visibility #1-10 (hidden vs. attractive)
            
            for i in range(0, len(locations)):
                if locations[i] == self.parent:
                    locations.insert((i+1),self)
            #locations.append(self)
 
            self.forbidden = False
            self.pop = []
            self.enter_sfx = enter_sound
            self.exit_sfx = exit_sound
            
            self.parent.room = self
            
            self.keys = []
            self.room = None
            self.zone = parent
            if self.zone.type == "room":
                while self.zone.type == "room":
                    self.zone = self.zone.parent
                    
            
        def find(self):
            self.found = True

        def dump(self):
            global loc
            global this_is_a_new_loc
            global party
            exit = self.exit
            if exit.type == "grid":
                newloc = exit
                if loc.exit_sfx is None: #play sound of leaving the room, default is a door sound
                    renpy.sound.play("sfx/door_close.ogg", channel="system2")
                else:
                    renpy.sound.play("sfx/"+loc.exit_sfx+".ogg", channel="system2")
                renpy.scene()
                renpy.show("black")
                renpy.transition(dissolve)
                renpy.pause(0.5)
                loc = newloc
                for i in party:
                    i.loc = newloc
                renpy.jump("grid_loc")
                move_to_grid(self.exit)
            else:
                move_to_room(self.exit)
