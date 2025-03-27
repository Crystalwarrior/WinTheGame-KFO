######################################
###################################### BATTLE ENGINE #
######################################
init:
    $ ever_battled = True
    $ battle_grid = [None,None,"foe",None,None,None,None,"you",None,None]
    $ f_place = 0
    $ y_place = 9
    $ battle_selection = False
    $ slat_range = []
    $ battle_moving = False
    $ battle_attacking = False
    $ y_move_count = 0
    $ f_move_count = 0
    $ enemy_time = False
    $ show_attack_slat = False
    $ show_attack_slat2 = False
    $ f_attacking = False
    $ f_moving = False     
    $ f_fleeing = False
    $ f_waiting = False
    $ f_flee_successful = False
    $ show_moving_slat = False
    $ battle_missed = False
    $ throwing = False
    $ just_murdered_someone = False
    $ battling = False
    $ battle_wpn_broken = False

label new_battle_intro:
    $ cutscene()
    $ battle_selection = False
    $ slat_range = []
    $ battle_moving = False
    $ battle_attacking = False
    $ y_move_count = 0
    $ f_move_count = 0
    $ enemy_time = False
    $ show_attack_slat = False
    $ show_attack_slat2 = False
    $ f_attacking = False
    $ f_moving = False     
    $ f_fleeing = False
    $ f_flee_successful = False
    $ show_moving_slat = False
    
    hide screen battle_start
    hide screen battle_start2
    

    
screen new_battle:
    add battle_static2
    #Show slats
    hbox:
        xalign 0.5 yalign 0.45 spacing -125
        $ slat_y = 0
        for i in range(0,len(battle_grid)):
                
            if i in slat_range and battle_moving and battle_grid[i] != "foe":
                imagebutton idle "battle/slat_green.png" hover "battle/slat_green2.png" action Return(i) ypos slat_y
            elif i in slat_range and battle_attacking:
                imagebutton idle "battle/slat_green.png" hover "battle/slat_red2.png" action Return(i) ypos slat_y
            elif i in slat_range and (show_moving_slat or f_moving):
                add "battle/slat_green.png" ypos slat_y
            # elif i in slat_range and show_attack_slat2 and not enemy_time:
                # add "battle/slat_green.png" ypos slat_y
            elif i in slat_range and (f_attacking or battle_attacking or show_attack_slat2):
                add "battle/slat_red.png" ypos slat_y
            elif i in slat_range and show_attack_slat:
                add "battle/slat_red.png" ypos slat_y
            else:
                add "battle/slat.png" ypos slat_y
            $ slat_y += 20
        
    #Show the little figure guy
    hbox:
        xalign 0.5 yalign 0.35 spacing -125
        $ slat_y = 0
        for i in battle_grid:
            if i == "foe":
                if show_attack_slat and not battle_missed:
                    add "battle/guy_red2.png" ypos slat_y
                else:   
                    add "battle/guy_red.png" ypos slat_y
            elif i == "you":
                if f_attacking and not battle_missed:
                    add "battle/guy2.png" ypos slat_y
                else:
                    add "battle/guy.png" ypos slat_y
            else:
                add "battle/guy_none.png" ypos slat_y
            $ slat_y += 20
        
    #Show your HP over guy fig
    hbox:
        xalign 0.5 yalign 0.2 spacing -125
        $ slat_y = 0
        for i in battle_grid:
            if i == "foe":
                vbox:
                    
                    if f_fleeing:
                        add "battle/flee.png" ypos slat_y xalign 0.5
                    elif f_waiting:
                        add "battle/talk.png" ypos slat_y xalign 0.5
                    elif f_moving:
                        add "battle/move.png" ypos slat_y xalign 0.5
                    elif f_attacking:
                        add "battle/attack.png" ypos slat_y xalign 0.5
                    else:
                        null height 19
                    text (enemy.name) ypos slat_y xalign 0.5
                    hbox:
                        null width 40
                        bar range 100 value enemy.health left_bar Frame("gui/bar_full_red.png",5,5) right_bar Frame("gui/bar_empty.png",5,5) thumb None xmaximum 105 ypos slat_y ymaximum 10
                        null width 40
            elif i == "you":
                vbox:
                    null height 19
                    text "You" ypos slat_y xalign 0.5
                    hbox:
                        null width 40
                        bar range 100 value health left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5) thumb None xmaximum 105 ypos slat_y ymaximum 10
                        null width 40
            else:
                null width 185
            $ slat_y += 20
    if battle_attacking:
        if persistent.autoattack:
            text "Your weapon is out of range." size 18 xalign 0.5 ypos 0.95
        else:
            text "Select who to shoot within your weapon's range." size 18 xalign 0.5 ypos 0.95
        textbutton "Cancel" xalign 0.5 ypos 0.88 action Return("cancel")
    if battle_moving:
        text "Select where to move." size 18 xalign 0.5 ypos 0.95
        textbutton "Cancel" xalign 0.5 ypos 0.88 action Return("cancel")

    
label new_battle: #This is a giant loop
    python:
        for i in range(0,len(battle_grid)): #Find where you and foe are in battlefield
            if battle_grid[i] == "you":
                y_place = i
            if battle_grid[i] == "foe":
                f_place = i
                
    if f_advantage: #Does enemy have advantage, as determined by the battle stats? They'll go first.
        $ f_advantage = False
        call battle_enemy_turn
                
    if battle_moving or battle_attacking: #Moving or attacking?
        call screen new_battle #Select a slat
        $ slat = _return
        if slat == "cancel":
            pass
        elif battle_grid[slat] != "foe" and battle_attacking and not persistent.autoattack:
            show screen new_battle
            $ show_buttons = False
            play sound "sfx/beep_double.ogg"
            $ battle_attacking = False
            memo2 "Empty. Select another grid square."
            $ battle_attacking = True
            $ show_buttons = True
            jump new_battle
        elif battle_grid[slat] == "foe" and battle_attacking and not persistent.autoattack:
            show screen new_battle
            $ battle_attacking = False
            $ show_attack_slat = True
            $slat_range = [f_place]
            $renpy.pause(0.5)
            $ y_move_count = 0
            call battle_your_turn
            $ show_attack_slat = False
            call battle_enemy_turn
            $ battle_missed = False
            jump new_battle
        elif battle_moving:
            show screen new_battle
            $ battle_moving = False
            python:
                show_moving_slat = True
                target_slat = slat
                slat_range = [slat]
                renpy.pause(0.2)
                while y_place != target_slat:
                    renpy.sound.play("sfx/beep2.ogg")
                    if battle_grid[y_place] != "foe":
                        battle_grid[y_place] = None
                    if slat < y_place:
                        y_place -= 1
                    else:
                        y_place += 1
                    if battle_grid[y_place] != "foe":
                        battle_grid[y_place] = "you"
                    renpy.pause(0.2)
                show_moving_slat = False
            
            # $ battle_grid[y_place] = None
            # $ battle_grid[slat] = "you"
            $ y_move_count += 1
            if y_move_count > 1:
                $ y_move_count = 0
                call battle_enemy_turn
        $ slat_range = []
        $ battle_moving = False
        $ battle_attacking = False
        jump new_battle
    else:
        $slat_range = []
    show screen new_battle
    $ explosives = []
    python:
        for i in inventory:
            if i[0].type == "explosive":
                explosives.append(i[0])
    $ do_something_stupid = False
    $ num = renpy.random.randint(0,100)
    if sanity <= 50 and num <= 25:
        $ do_something_stupid = True
    elif sanity <= 25 and num <= 50:
        $ do_something_stupid = True
        
    if not persistent.ever_battled: #Battle Tutorial
        $ persistent.ever_battled = True
        $ renpy.notify("You've started your first skirmish!")
        show screen new_battle
        $ renpy.pause(1.0,hard=True)
        #hide screen health_enemy2
        memo2 "{color=#00fc00}Goal:{/color} Deplete enemy's health.\n{color=#FF0000}Warning:{/color} Do not allow your opponent to deplete your own health."
        memo2 "You may attack once per turn. You may move once and attack or move twice.\nYou may not attack and then move!"
        memo2 "{color=#FFFFFF}MELEE{/color} weapons require you to be next to your opponent. {color=#FFFFFF}RANGED{/color} weapons can attack from far away, but their accuracy lowers."
        memo2 "You can heal yourself or equip new weapons in the {color=#FFFFFF}ITEMS{/color} screen. You can {color=#FFFFFF}FLEE{/color} battle if you reach either end of the grid. Some battles you cannot run from."
        #show screen health_enemy2
        
    menu:
        "{image=gui/bullseye.png} Attack":
            if wpn.uses == 0 or (wpn.wpn_range !="both" and wpn.uses >0 and wpn.use_count < wpn.uses) or wpn.wpn_range == "both":
                if do_something_stupid:
                    $ num = renpy.random.randint(0,100)
                    if num < 50:
                        memo2 "{color=00FF00}(Low Sanity){/color} You cackle delirously."
                    elif sanity <= 25:
                        memo2 "{color=00FF00}(Low Sanity){/color} You dance a merry jig."
                    else:
                        memo2 "{color=00FF00}(Low Sanity){/color} You're distracted. Is someone behind you!?"
                    call battle_enemy_turn
                else:
                    python:
                        slat_range = []
                        if wpn.battle_range != 0:
                            slat_range = range(10)
                            remove_slat_range = range(10)
                            for x in range(1,(wpn.battle_range+1)):
                                if (y_place-x) in remove_slat_range:
                                    remove_slat_range.remove(y_place-x)
                                if (y_place+x) in remove_slat_range:
                                    remove_slat_range.remove(y_place+x)
                            for x in remove_slat_range:
                                if x in slat_range:
                                    slat_range.remove(x)
                        elif wpn.wpn_range == "ranged" or (wpn.wpn_range == "both" and wpn.uses > 0 and wpn.use_count < wpn.uses):
                            slat_range = range(10)
                            slat_range.remove(y_place)
                            # if wpn.wpn_range != "both":
                                # if y_place != 0:
                                    # slat_range.remove(y_place-1)
                                # if y_place != 9:
                                    # slat_range.remove(y_place+1)
                        else:
                            if y_place != 0:
                                slat_range.append(y_place-1)
                            if y_place != 9:
                                slat_range.append(y_place+1)
                                    
                    if persistent.autoattack:
                        if f_place in slat_range:
                            $ show_attack_slat2 = True
                            $renpy.pause(0.5)
                            $ show_attack_slat2 = False
                            $ show_attack_slat = True
                            $slat_range = [f_place]
                            $renpy.pause(0.5)
                            $ y_move_count = 0
                            call battle_your_turn
                            $ show_attack_slat = False
                            call battle_enemy_turn
                            $ battle_missed =  False
                        else:
                            show screen new_battle
                            $ show_buttons = False
                            $ show_attack_slat2 = True
                            play sound "sfx/beep_double.ogg"
                            memo2 "Weapon out of range."
                            $ show_attack_slat2 = False
                            $ show_buttons = True
                            jump new_battle
                    else:
                        $ battle_attacking = True
                        jump new_battle
            else:
                if wpn.type == "gun":
                    memo2 "You are out of ammo."
                elif wpn.type == "fuel":
                    memo2 "Your weapon is out of fuel."
                else:
                    memo2 "Your weapon is broken."
                $ renpy.restart_interaction()
        "{image=gui/boom.png} Throw{image=gui/caret0.png}{image=gui/caret0.png}" if len(explosives) > 0:
            $ throwing = True
            python:
                slat_range = range(10)
                slat_range.remove(y_place)
                if clamp(y_place+1,0,9) in slat_range:
                    slat_range.remove(clamp(y_place+1,0,9))
                if clamp(y_place+2,0,9) in slat_range:
                    slat_range.remove(clamp(y_place+2,0,9))
                if clamp(y_place-1,0,9) in slat_range:
                    slat_range.remove(clamp(y_place-1,0,9))
                if clamp(y_place-2,0,9) in slat_range:
                    slat_range.remove(clamp(y_place-2,0,9))
                if clamp(y_place+3,0,9) in slat_range:
                    slat_range.remove(clamp(y_place+3,0,9))
                if clamp(y_place-3,0,9) in slat_range:
                    slat_range.remove(clamp(y_place-3,0,9))
            if len(explosives) == 1:
                $ explosive_thrown = explosives[0]  
                $ battle_attacking = True
            else:
                call screen explosive_inventory
                $ item_to_add = _return
                if item_to_add != 0:
                    $ explosive_thrown = item_to_add
                    $ battle_attacking = True
                else:
                    $ throwing = False
            
                    
            if persistent.autoattack:
                $ battle_attacking = False
                if f_place in slat_range:
                    $ show_attack_slat2 = True
                    $renpy.pause(0.5)
                    $ show_attack_slat2 = False
                    $ show_attack_slat = True
                    $slat_range = [f_place]
                    $renpy.pause(0.5)
                    $ y_move_count = 0
                    call battle_your_turn
                    $ show_attack_slat = False
                    call battle_enemy_turn
                else:
                    $ throwing = False
                    show screen new_battle
                    $ show_buttons = False
                    $ show_attack_slat2 = True
                    play sound "sfx/beep_double.ogg"
                    memo2 "Weapon out of range."
                    $ show_attack_slat2 = False
                    $ show_buttons = True
                    jump new_battle
            else:
                jump new_battle
        "{image=gui/move.png} Move{image=gui/caret0.png}{image=gui/caret0.png}{image=gui/caret0.png}":
            $ battle_moving = True
            $ slat_range = []
            
            $ slat_range.append(clamp(y_place+1,0,9))
            $ slat_range.append(clamp(y_place+2,0,9))
            $ slat_range.append(clamp(y_place-1,0,9))
            $ slat_range.append(clamp(y_place-2,0,9))
            python:
                while f_place in slat_range:
                    slat_range.remove(f_place)
                while y_place in slat_range:
                    slat_range.remove(y_place)
                slat_range = list(set(slat_range))
            jump new_battle
         # "{image=gui/boom.png} Item{image=gui/caret0.png}{image=gui/caret0.png}{image=gui/caret0.png}":
        "{image=gui/wait.png} Wait{image=gui/caret0.png}{image=gui/caret0.png}{image=gui/caret0.png}":
            call battle_enemy_turn
        "Flee" if (y_place == 0 or y_place == 9) and can_flee:
            $ show_buttons = False
            $ chance = renpy.random.randint(0,100)
            if chance > 33:
                play sound "sfx/beep_good.ogg"
                memo2 "You successfully escape!"
                hide screen new_battle
                hide screen health_enemy2
                with dissolve
                
                $ show_buttons = True
                $ loc = runaway()
                $ move_to_grid(loc)
            else:
                play sound "sfx/beep_double.ogg"
                memo2 "You try to escape, but fail!"
                $ show_buttons = True
                call battle_enemy_turn

    #Determine if battle is over
    if enemy.health <= 0:
        $ enemy.health = 0
        $ battle_end()
    elif health <= 0 and not cannot_die:
        $ health = 0
        jump game_over
    else:
        jump new_battle
        
######################################
###################################### BATTLE ENGINE #
######################################
                
init python:
    ########## BATTLE START ##########
    def battle_start(foe,positioning,opener,ending,play_music, flee = True,foe_advantage=False):
        global enemy 
        global advantage
        global battle_won
        global your_atk
        global your_def
        global your_wpn
        global their_def
        global enemy_wpn
        global enemy_atk
        global enemy_def
        global battle_message
        global battle_end_jump
        global battle_grid
        global ever_battled
        global can_flee
        global f_advantage
        global ever_battled
        global battling
        global trap_caught_person
        battling = True
        can_flee = flee
        f_advantage = foe_advantage
        battle_message = opener
        battle_end_jump = ending
        enemy = foe

        # Battling the trapped person will release them
        if trap_caught_person == enemy:
            trap_caught_person = None
        advantage = adv
        battle_won = False
        if enemy.wpn is None:
            enemy.wpn = fist
        enemy_wpn = enemy.wpn
        enemy_atk = enemy_wpn.wpn_rating
        enemy_def = enemy_wpn.defense
        enemy.make_foe(you)
        if positioning == 1:
            battle_grid = [None,None,None,None,"foe","you",None,None,None,None]
        elif positioning == 2:
            battle_grid = ["foe",None,None,None,None,None,None,None,None,"you"]
        elif positioning == 3:
            battle_grid = [None,None,None,"foe",None,None,"you",None,None,None]
        else:
            battle_grid = [None,None,"foe",None,None,None,None,"you",None,None]
        if wpn is None:
            your_wpn = fist
        else:
            your_wpn = wpn
        
        your_atk = your_wpn.wpn_rating
        if armor is None:
            your_def = 0
        else:
            your_def = armor.defense
        their_def = 0
        if enemy.wpn != None:
            if enemy.wpn.defense > their_def:
                their_def = enemy.wpn.defense
        if enemy.item != None:
            if enemy.item[0].defense > their_def:
                their_def = enemy.item[0].defense
        if play_music:
            renpy.music.stop(fadeout=2.0)  
        if not freeplay:
            renpy.show(enemy.death_sprite)
        renpy.say(None,battle_message)
        renpy.hide_screen("health_enemy")
        if play_music:
            tracks = [
                "music/ResonantBlip.ogg",
                "music/ResonantBlipBSide.ogg",
                "music/ResonantBlipCSide.ogg",
                "music/ResonantBlipDSide.ogg"
            ]
            # Default combat track
            track = tracks[0]
            # Play B-side on lower sanity or when you're a mass murderer
            if sanity <= 60 or you.kills > 2:
                track = tracks[1]
            # Play C-side after your 6th kill
            if you.kills > 6:
                track = tracks[2]
            # Play D-side after your 8th kill!!
            if you.kills > 8:
                track = tracks[3]
            # Mix things up when it becomes routine after your 10th kill.
            if you.kills > 10:
                # Randomize!
                track = tracks[renpy.random.randint(0, 3)]
            renpy.music.play(track,fadein=2.0, fadeout=1.0)

        renpy.sound.play("sfx/accent_battle.ogg",channel="system2")
        renpy.show_screen("battle_start")
        renpy.pause(2.5, hard=True)
        #renpy.scene()
        #renpy.show("battle_static")
        renpy.transition(dissolve)
        renpy.show_screen("health_enemy2")
        renpy.pause(0.5)
        renpy.jump("new_battle_intro")
        
    ########## BATTLE END ##########
    def battle_end():
        global battle_end_jump
        global enemy
        global can_flee
        global f_advantage
        global just_murdered_someone
        global murdered
        global battling
        battling = False
        murdered = enemy.name
        if enemy.type != "hostile" and not f_advantage:
            just_murdered_someone = True
        can_flee = True
        f_advantage = False
        config.skipping = False
        enemy.death_sfx()
        renpy.show(enemy.death_sprite)
        renpy.music.stop(fadeout=3.0)
        renpy.hide_screen("health_enemy2")
        renpy.hide_screen("new_battle")
        renpy.transition(dissolve)
        add_sanity(-30)
        renpy.notify("You've taken a human life.")
        enemy_call = enemy.call_name
        enemy_phrase = enemy.death_phrase
        renpy.say(enemy_call, enemy_phrase)
        enemy_name = enemy.name+" "+enemy.last_name
        enemy.kill("murder",you)
        renpy.sound.play("sfx/bodyfall.ogg",channel=1)
        renpy.hide(enemy.death_sprite)
        renpy.transition(dissolve)
        renpy.sound.play("sfx/gameover.ogg")
        renpy.show_screen("beep_red")
        renpy.say(memo,"{color=#FFF}"+enemy_name+"{/color} has {color=#FF0000}lost the game{/color}.")
        if enemy.wpn is not None and enemy.wpn is not fist:
            loot_wpn = enemy.wpn
            loot_to_say = "You take "+enemy.name+"'s weapon."
            loot_wpn.add()
            if loot_wpn.is_in_inventory():
                renpy.say(None, loot_to_say)
        if enemy.item is not None:       
            loot_item = enemy.item
            loot_to_say = "You find something on "+enemy.name+"."
            loot_item[0].add(amt=loot_item[1])
            if loot_item[0].is_in_inventory():
                renpy.say(None, loot_to_say)
        if enemy.gender == "Male":
            e_him = "him"
            e_his = "his"
            e_he = "he"
        else:
            e_him = "her"
            e_his = "her"
            e_he = "she"
        ## Various reactions to murdering people, depending on the number
        if you.kills == 1:
            renpy.say(None, "You took a life. What have you done?")
            renpy.say(None, "You ... killed them!")
            renpy.say(None, "But it was either kill or be killed ...")
        elif you.kills == 2:
            renpy.say(None, "You choke on nothing and look at your hands. You did this. You!")
            renpy.say(None, "Another classmate dies at your hands. Did they really deserve this?")
            renpy.say(None, "What will happen to you if you keep killing?")
        elif you.kills == 3:
            renpy.say(None, "You took another life ... Are you really doing this!? These were your {u}friends{/u}!")
            renpy.say(None, "You close your eyes tight and take many deep breaths.")
        elif you.kills == 4:
            renpy.say(None, "You scream and tears form in your eyes.")
            renpy.say(None, "This shouldn't be happening.")
        elif you.kills == 5:
            renpy.say(None, "Blood. So much blood ...")
        elif you.kills == 6:
            renpy.say(None, "You're starting to realize that you might be dead inside. Looking at their corpse does nothing to you. Not anymore.")
        elif you.kills == 7:
            renpy.say(None, "There's a sort of sweetness to this pain of watching your friends die.")
        elif you.kills == 8:
            renpy.say(None, "You smile. You know it's wrong, but you do it anyway.")
        elif you.kills > 8:
            renpy.say(None, "You cackle deliriously.")
        
        if battle_end_jump is not None:
            renpy.jump(battle_end_jump)
        else:
            renpy.jump("grid_loc")
        
    #generate a damage amount
    def gen_atk(rating):
        global sanity
        num = renpy.random.randint(0,10) #randomness
        
        damage = (rating*8) #base damage
        
        #Change damage based on sanity
        if sanity < 25:
            damage -= 30
        elif sanity < 35:
            damage -= 25
        elif sanity < 50:
            damage -= 20
        elif sanity < 65:
            damage -= 15
        elif sanity < 75:
            damage -= 10
        elif sanity < 85:
            damage -= 5
            
        # minimum damage
        if damage < 0:
            damage = 0
        damage += num
        return damage
        
    #generate how much damage to buffer
    def shield(dam,dfn):
        if dfn == 1:
            percent = 0.1
        elif dfn == 2:
            percent = 0.15
        elif dfn == 3:
            percent = 0.25
        elif dfn == 4:
            percent = 0.33
        elif dfn == 5:
            percent = 0.4
        elif dfn == 6:
            percent = 0.5
        elif dfn == 7:
            percent = 0.6
        elif dfn == 8:
            percent = 0.7
        elif dfn == 9:
            percent = 0.75
        else:
            percent = 0
            
        dam = dam - (dam * percent)
        return dam
        
    def get_enemy_range():
        global enemy_wpn_range
        global enemy_walk_range
        slat_range = []
        for i in range(0,len(battle_grid)):
            if battle_grid[i] == "you":
                y_place = i
            if battle_grid[i] == "foe":
                f_place = i
        #Enemy Attacking Range
        enemy_wpn_range = []
        if enemy.wpn.battle_range != 0:
            enemy_wpn_range = range(10)
            remove_enemy_wpn_range = range(10)
            for x in range(1,(enemy.wpn.battle_range+1)):
                if (f_place-x) in remove_enemy_wpn_range:
                    remove_enemy_wpn_range.remove(f_place-x)
                if (f_place+x) in remove_enemy_wpn_range:
                    remove_enemy_wpn_range.remove(f_place+x)
            for x in remove_enemy_wpn_range:
                if x in enemy_wpn_range:
                    enemy_wpn_range.remove(x)
        elif enemy.wpn.wpn_range == "melee":
            if f_place != 0:
                enemy_wpn_range.append(f_place-1)
            if f_place != 9:
                enemy_wpn_range.append(f_place+1)
        else:
            enemy_wpn_range = range(10)
            # if enemy.wpn.wpn_range != "both":
                # if f_place != 0:
                    # enemy_wpn_range.remove(f_place-1)
                # if f_place != 9:
                    # enemy_wpn_range.remove(f_place+1)
        if f_place in enemy_wpn_range:
            enemy_wpn_range.remove(f_place)
        
        #print "enemy_wpn_range",enemy_wpn_range
        #Enemy Walking Range
        enemy_walk_range = []
        
        #Default 1 forward, 1 backwards
        enemy_walk_range.append(clamp(f_place+1,0,9))
        enemy_walk_range.append(clamp(f_place-1,0,9))
        
        if enemy.type == "coward":
            #Cowards get +2 in opposite direction of you
            if y_place > f_place:
                enemy_walk_range.append(clamp(f_place-2,0,9))
                enemy_walk_range.append(clamp(f_place-3,0,9))
            else:
                enemy_walk_range.append(clamp(f_place+2,0,9))
                enemy_walk_range.append(clamp(f_place+3,0,9))
        elif enemy.type == "hostile":
            #Hostiles get +2 in the direction of you
            if y_place > f_place and f_place !=9:
                enemy_walk_range.append(clamp(f_place+2,0,9))
                enemy_walk_range.append(clamp(f_place+3,0,9))
            elif f_place != 0:
                enemy_walk_range.append(clamp(f_place-2,0,9))
                enemy_walk_range.append(clamp(f_place-3,0,9))
        else:
            #Normal gets 2 forward, 2 back
            enemy_walk_range.append(clamp(f_place+2,0,9))
            enemy_walk_range.append(clamp(f_place-2,0,9))
                
        while f_place in enemy_walk_range:
            enemy_walk_range.remove(f_place)
        while y_place in enemy_walk_range:
            enemy_walk_range.remove(y_place)
        enemy_walk_range = list(set(enemy_walk_range))
        #print "enemy_walk_range",enemy_walk_range
        #print "enemy.wpn.wpn_range",enemy.wpn.wpn_range
        
    def get_fig_range():
        global battle_grid
        for i in range(0,len(battle_grid)):
            if battle_grid[i] == "you":
                y_place = i
            if battle_grid[i] == "foe":
                f_place = i
        
        if f_place > y_place:
            difference = f_place - y_place
        else:
            difference = y_place - f_place
        return difference
        
    def get_accuracy(weapon):
        difference = get_fig_range()
        if difference == 1:
            chance = 100
        elif difference == 2:
            if weapon.wpn_range == "melee":
                chance = 75
            else:
                chance = 90
        elif difference == 3:
            if weapon.wpn_range == "melee":
                chance = 50
            else:
                chance = 80
        elif difference == 4:
            chance = 70
        elif difference == 5:
            chance = 60
        elif difference == 6:
            chance = 50
        elif difference == 7:
            chance = 45
        elif difference == 8:
            chance = 33
        elif difference == 9:
            chance = 25
        else:
            chance = 100
        return chance
        
    def clamp(n, minn, maxn):
        return max(min(maxn, n), minn)

label battle_enemy_turn:
    #ENEMEY ATTACK
    $ slat_range = []
    show screen new_battle
    $ renpy.pause(0.5)
    python:
        if True:
            for p_attacker in party:
                if enemy.type != "hostile" and (enemy in party or enemy not in p_attacker.enemies):
                    num = renpy.random.randint(0,100)
                    # 40% chance for the party member to scold you
                    if num <= 40:
                        helper_phrases = ["Shinobu!?", "What are you doing!?", "Stop!", "Don't hurt them!"]
                        helper_phrase = renpy.random.choice(helper_phrases)
                        renpy.say(p_attacker.call_name, helper_phrase)
                    continue
                num = renpy.random.randint(0,100)
                # 25% chance for each party member to help out, but only if your enemy isn't on death's door
                if num <= 25 and enemy.health > 5:
                    #print "party member attacks!"
                    p_attacker_n = p_attacker.name
                    enemy_name  = enemy.name
                    helper_phrases = ["Shinobu!", "Watch out!", "I have your back!","Let me help!","Get away from him!"]
                    helper_phrase = renpy.random.choice(helper_phrases)
                    renpy.say(p_attacker.call_name, helper_phrase)
                    
                    damage = gen_atk(p_attacker.wpn.wpn_rating)
                    damage = shield(damage,their_def)
                    p_attacker.wpn.use_sfx()
                    reference_item(p_attacker.wpn)
                    renpy.pause(0.25)
                    show_blood()
                    if enemy.gender == "Male":
                        num = renpy.random.randint(1,4)
                        rand_hitsfx = "sfx/hit_boy%d.ogg"%num
                    else:
                        num = renpy.random.randint(1,5)
                        rand_hitsfx = "sfx/hit_girl%d.ogg"%num
                    enemy.health -= damage
                    renpy.sound.play(rand_hitsfx, channel="system")
                    renpy.say(memo2,"%(p_attacker_n)s attacks %(enemy_name)s for {color=#FF0000}%(damage)d{/color} points of damage!")
                    renpy.pause(0.5)
                    if enemy.health <= 0:
                        enemy.health = 1
                        # Party members don't fight to kill
                        break
    $ enemy_time = True
    $ f_move_count = 0
    $ f_attacking = False
    $ f_fleeing = False
    $ f_moving = False
    $ f_waiting = False
    $ retreated_already = False
    $ advanced_already = False
    python:
        ### ENEMY AI
        while f_move_count < 2:
            
            get_enemy_range()
            
            f_moving = False
            f_waiting = False
            distance = get_fig_range()
            #Decide if AI will retreat
            retreat = False
            if wpn.wpn_range == "melee" and distance < 2 and enemy.wpn.wpn_range != "melee": # and enemy.type != "hostile":
                #print "scared of melee weapon"
                num = renpy.random.randint(0,100)
                if num <= 66:
                    #print "retreating!"
                    retreat = True
            if enemy.type == "normal" or enemy.type == "fixed":
                if enemy.health <= 10:
                    # Always retreat when on death's door
                    retreat = True
                elif enemy.health <= 25:
                    num = renpy.random.randint(0,100)
                    if num < 75:
                        #print "retreating!"
                        retreat = True
                elif enemy.health <= 50:
                    num = renpy.random.randint(0,100)
                    if num < 50:
                        #print "retreating!"
                        retreat = True
            elif enemy.type == "coward":
                if enemy.health <= 50:
                    #print "coward is retreating"
                    retreat = True
                    
            if retreat and not can_flee:
                #print "can't retreat, silly!"
                num = renpy.random.randint(0,100)
                if num < 50:
                    #print "so we won't"
                    retreat = False
                    
            if y_place in enemy_wpn_range and not retreat:
                num = renpy.random.randint(0,100)
                
                
                
                #Random chance to move
                if num <= 33 and distance > 1:
                    f_moving = True
                else:
                    f_attacking = True
                    f_move_count = 2
            else:
                f_moving = True
 
            if f_moving or retreat:
                # Lower sanity makes them more likely to stop retreating
                num = renpy.random.randint(0,100)
                if enemy.sanity < 50 and num > enemy.sanity:
                    retreat = False
                    if y_place in enemy_wpn_range:
                        f_attacking = True
                    else:
                        f_moving = True
                
                #Walk closer or flee
                if f_place == 0 or f_place == 9:
                    #Going to flee?
                    f_fleeing = False
                    if enemy.type == "coward" and can_flee:
                        f_fleeing = True
                    elif enemy.type != "hostile":
                        #print "not a hostile"
                        num = renpy.random.randint(0,100)
                        if num < 50 and y_place in enemy_wpn_range or not can_flee:
                            #print "won't flee, attack!"
                            f_fleeing = False
                            f_moving = False
                            retreat = False
                            if y_place in enemy_wpn_range:
                                f_attacking = True
                            else:
                                num = renpy.random.randint(0,100)
                                f_attacking = False
                                if num < 50:
                                    f_waiting = True
                                    f_move_count = 2
                                else:
                                    f_moving = True
                                    f_waiting = False
                                    f_move_count += 1
                            
                        else:
                            #print "will flee!"
                            f_fleeing = True
                            f_attacking = False
                        
                if f_fleeing:
                    #print "checking flee success"
                    f_move_count = 2
                    renpy.sound.play("sfx/beep2.ogg")
                    renpy.pause(0.5)
                    num = renpy.random.randint(0,100)
                    if num < 35:
                        f_flee_successful = True
                    else:
                        f_flee_successful = False
                elif f_moving:
                    if not retreat and not retreated_already:
                        # MOVE CLOSER TO YOU
                        # determine danger zone that AI will avoid venturing past
                        
                        slat_range = enemy_walk_range
                        renpy.pause(0.2)
                        danger_zone = y_place
                        advanced_already = True
                        if wpn.wpn_range == "melee" and enemy.wpn.wpn_range != "melee":
                            if wpn.battle_range == 0:
                                zone_add = 1
                            else:
                                zone_add = wpn.battle_range
                            if f_place < y_place:
                                danger_zone -= zone_add
                            else:
                                danger_zone += zone_add
                        #print "danger_zone",danger_zone
                        if f_place < y_place:
                            move_spot = 0
                            for i in enemy_walk_range:
                                if i > move_spot and not i >= danger_zone:
                                    move_spot = i
                        else:
                            move_spot = 9
                            for i in enemy_walk_range:
                                if i < move_spot and not i <= danger_zone:
                                    move_spot = i
                    elif not advanced_already:
                        # MOVE AWAY FROM YOU (RETREAT)
                        slat_range = enemy_walk_range
                        renpy.pause(0.2)
                        retreated_already = True
                        if f_place < y_place:
                            move_spot = 9
                            for i in enemy_walk_range:
                                if i < move_spot:
                                    move_spot = i
                        else:
                            move_spot = 0
                            for i in enemy_walk_range:
                                if i > move_spot:
                                    move_spot = i
                    else:
                        slat_range = []
                        f_waiting = True
                        f_move_count = 2
                        break
                        
                        
                    #print "moving to ...",move_spot
                    target_slat = move_spot
                    slat_range = [move_spot]
                    renpy.sound.play("sfx/beep2.ogg")
                    renpy.pause(0.2)
                    while f_place != target_slat:
                        renpy.sound.play("sfx/beep2.ogg")
                        if battle_grid[f_place] != "you":
                            battle_grid[f_place] = None
                        if move_spot < f_place:
                            f_place -= 1
                        else:
                            f_place += 1
                        if battle_grid[f_place] != "you":
                            battle_grid[f_place] = "foe"
                        renpy.pause(0.2)

                    f_moving = False
                    f_move_count += 1
        
    if f_waiting:
        python:
            renpy.pause(0.5)
            enemy_call = enemy.call_name
            rand_sayings = ["Leave me alone!", "Go away!", "Stop it!!", "You won't get away with this!", "I can't believe you!","Shinobu!?","I don't want to die!"]
            random_saying = renpy.random.choice(rand_sayings)
            renpy.say(enemy_call, random_saying)
        $ f_waiting = False
    elif f_attacking:
        python:
            #print "attacking ..."
            slat_range = enemy_wpn_range
            renpy.pause(0.5)
            slat_range = [y_place]
            renpy.sound.play("sfx/beep2.ogg")
            renpy.pause(0.5)
        $ enemy_atk_face = enemy.atk_sprite
        $renpy.show(enemy_atk_face)
        $ num = renpy.random.randint(0,100)
        
        $ chance = get_accuracy(enemy.wpn)           
        if enemy.type == "hostile":
            $ chance += 10
        elif enemy.type == "coward":
            $ chance -= 5
        $ enemy_wpn.use_sfx()
        $ e_name = enemy.name
        if num <= chance:
            $ damage = gen_atk(enemy_atk)
            
            $ damage = shield(damage,your_def)
            $renpy.transition(hpunch)
            $ num_damage = damage * -1
            $ add_health(num_damage)
            memo2 "%(e_name)s inflicts {color=#FF0000}%(damage)d{/color} points of damage on you."
        else:
            $ battle_missed = True
            play sound "sfx/beep_on.ogg"
            memo2 "%(e_name)s attacked but missed you!"
        $ f_attacking = False
        $renpy.show(enemy.death_sprite)
    if f_fleeing:
        $ e_name = enemy.name
        if f_flee_successful:
            play sound "sfx/flee.ogg" channel 1
            $renpy.hide(enemy.name)
            $renpy.transition(dissolve)
            $ renpy.pause(0.4)
            python:
                for i in range(0,len(battle_grid)):
                    if battle_grid[i] == "foe":
                        battle_grid[i] = None
        else:
            memo2 "%(e_name)s tries to flee, but can't get away!"
        $ f_fleeing = False
        $ f_moving = False
            
    
    $ enemy_time = False
    if f_flee_successful:
        $ enemy.make_foe(you)
        $ enemy.move("rand")
        play sound "sfx/beep_double2.ogg"
        memo2 "%(e_name)s flees to the %(escape_plan)s!"
        $ enemy.type = "normal"
        $ enemy.invisible = False
        $ enemy.hidden = False
        $ murdered = enemy.name
        $ enemy.sanity -= 25
        play sound "sfx/accent_wash.ogg"
        hide screen health_enemy2
        hide screen new_battle
        with dissolve
        call murder_follower_reaction
        $ renpy.pause(0.5)
        jump grid_loc                            
    elif enemy.health <= 0:
        $ enemy.health = 0
        $ battle_end()
    elif health <= 0 and not cannot_die:
        $ health = 0
        jump game_over
    $ f_waiting = False
    $ f_attacking = False
    $ f_moving = False
    return
                
label battle_your_turn:
    python:
        for i in range(0,len(battle_grid)):
            if battle_grid[i] == "you":
                y_place = i
            if battle_grid[i] == "foe":
                f_place = i
    #YOUR ATTACK
    show screen new_battle
    if throwing:
        $ battle_wpn_broken = False
        $ num = 0
        $ chance = 100
    else:
        $ battle_wpn_broken = False
        $ wpn.use_sfx()
        $ num = renpy.random.randint(0,100)
        $ chance = get_accuracy(wpn) 
        if sanity >= 75: #the more insane you are, the less your accuracy
            $ chance += 10
        elif sanity >= 50:
            $ chance += 5
        elif sanity < 50:
            $ chance -= 5
        elif sanity <= 25:
            $ chance -= 10
    if num <= chance:
        if throwing:
            $ explosive_thrown.destroy(1)
            $ explosive_thrown.use_sfx()
            $ damage = gen_atk(explosive_thrown.wpn_rating)
            $ throwing = False
        else:
            $ damage = gen_atk(wpn.wpn_rating)
        $ damage = shield(damage,their_def)
        $ renpy.pause(0.25)
        $ show_blood()
        if enemy.gender == "Male":
            $ num = renpy.random.randint(1,4)
            $ rand_hitsfx = "sfx/hit_boy%d.ogg"%num
        else:
            $ num = renpy.random.randint(1,5)
            $ rand_hitsfx = "sfx/hit_girl%d.ogg"%num
        play sound (rand_hitsfx) channel "system"
        $ enemy.health -= damage
        memo2 "You do {color=#FF0000}%(damage)d{/color} points of damage."

        # SPECIAL non-lethal taser check
        if enemy.health > 0 and wpn.name == "taser":
            $ chance = renpy.random.randint(0,100)
            # The lower your enemy health is, the higher chance of incapacitation
            if chance > enemy.health:
                jump enemy_incapacitated
    else:
        play sound "sfx/beep_double2.ogg"
        $ battle_missed = True
        memo2 "You miss!"
    if wpn.uses > 0:
        $ wpn.use(use_sound=False)
    if battle_wpn_broken:
        play sound "sfx/beep_double2.ogg"
        if wpn.type == "gun":
            memo2 "You ran out of ammo!"
        elif wpn.type == "fuel":
            memo2 "You ran out of fuel! Your weapon is useless!"
        else:
            memo2 "Your weapon breaks!"
    if enemy.health <= 0:
        $ enemy.health = 0
        $ battle_end()
    elif health <= 0 and not cannot_die:
        $ health = 0
        jump game_over
    return######################################


label enemy_incapacitated:
    $ renpy.music.stop(fadeout=3.0)
    play sound "sfx/beep_good.ogg"
    memo2 "You have incapacitated your opponent!"
    if can_flee:
        memo2 "With them down on the ground, you may now {color=#00FF00}flee{/color} or {color=#FF0000}execute{/color} them."
        menu:
            "{image=gui/bullseye.png} {color=#FF0000}Execute{/color}":
                $ enemy.health = 0
                $ show_blood()
                memo2 "You finish off your opponent."
            "Flee":
                hide screen new_battle
                hide screen health_enemy2
                with dissolve
                
                $ show_buttons = True
                $ loc = runaway()
                $ move_to_grid(loc)
    else:
        memo2 "You have no choice but to {color=#FF0000}execute{/color} them."
        $ enemy.health = 0
        $ show_blood()
        memo2 "You finish off your opponent."
    if enemy.health <= 0:
        $ enemy.health = 0
        $ battle_end()