######################################
###################################### FUNCTIONS #
######################################

init python:
    def add_health(num):
        global health
        renpy.sound.play("sfx/beep1.ogg",channel="system")
        if notify_y != .095:
            renpy.show_screen("beep_red")
        if num > 0:
            renpy.notify("Gaining Health ...")
            #store_say(None,"{color=#00db00}Gaining Health ...{/color}")
        else:
            renpy.notify("Losing Health ...")
            #store_say(None,"{color=#FF0000}Losing Health ...{/color}")
        health += num
        if health > 100:
            health = 100
        if health < 0:
            health = 0
        #calculatesanitysound()
        
    def add_sanity(num):
        global sanity
        renpy.sound.play("sfx/beep1.ogg",channel="system")
        if notify_y != .095:
            renpy.show_screen("beep_yellow")
        if num > 0:
            renpy.notify("Gaining Sanity ...")
            #store_say(None,"{color=#00db00}Gaining Sanity ...{/color}")
        else:
            renpy.notify("Losing Sanity ...")
            #store_say(None,"{color=#FF0000}Losing Sanity ...{/color}")
        renpy.sound.play("sfx/accent_weird.ogg",channel="system")
        sanity += num
        if sanity > 100:
            sanity = 100
        if sanity < 0:
            sanity = 0
        #calculatesanitysound()

    def add_health_sanity(num,num2):
        global health
        global sanity
        renpy.sound.play("sfx/beep1.ogg",channel="system")
        if notify_y != .095:
            renpy.show_screen("beep_yellow")
            renpy.show_screen("beep_red")
        if num > 0:
            renpy.notify("Gaining Health & Sanity ...")
            #store_say(None,"{color=#00db00}Gaining Health & Sanity ...{/color}")
        else:
            renpy.notify("Losing Health & Sanity ...")
            #store_say(None,"{color=#FF0000}Losing Health & Sanity ...{/color}")
        renpy.sound.play("sfx/accent_weird.ogg",channel="system")
        
        health += num
        sanity += num2
        
        if health > 100:
            health = 100
        if health < 0:
            health = 0
        if sanity > 100:
            sanity = 100
        if sanity < 0:
            sanity = 0
        #calculatesanitysound()
        
    #Sound that plays when you're lower on health or sanity
    def calculatesanitysound():
        #print "checking sanity"
        global sanity
        global health
        if sanity <= 20 or health <= 20:
            if sanity <= 20:
                renpy.show_screen("beep_yellow_continuous")
            if health <= 20:
                renpy.show_screen("beep_red_continuous")
            if persistent.sanity_sounds:
                renpy.music.play("sfx/sanity4.ogg", fadeout = 1.0, fadein = 5.0, channel="sanity", tight=True)
        elif sanity <= 40 or health <= 40:
            if sanity > 20:
                renpy.hide_screen("beep_yellow_continuous")
            if health > 20:
                renpy.hide_screen("beep_red_continuous")
            if persistent.sanity_sounds:
                renpy.music.play("sfx/sanity3.ogg", fadeout = 1.0, fadein = 1.0, channel="sanity")
        elif sanity <= 60 or health <= 60:
            if sanity > 20:
                renpy.hide_screen("beep_yellow_continuous")
            if health > 20:
                renpy.hide_screen("beep_red_continuous")
            if persistent.sanity_sounds:
                renpy.music.play("sfx/sanity2.ogg", fadeout = 1.0, fadein = 1.0, channel="sanity")
        elif sanity <= 80 or health <= 80:
            if sanity > 20:
                renpy.hide_screen("beep_yellow_continuous")
            if health > 20:
                renpy.hide_screen("beep_red_continuous")
            if persistent.sanity_sounds:
                renpy.music.play("sfx/sanity1.ogg", fadeout = 1.0, fadein = 1.0, channel="sanity")
        else:
            #print "stop sanity sound"
            if sanity > 20:
                renpy.hide_screen("beep_yellow_continuous")
            if health > 20:
                renpy.hide_screen("beep_red_continuous")
            if persistent.sanity_sounds:
                renpy.music.stop(fadeout=3.0,channel="sanity")
        if not persistent.sanity_sounds:
            renpy.music.stop(fadeout=0.0, channel="sanity")
            
    def party_add(name):
        global party
        global followers
        party.append(name)
        name.loc = loc
        renpy.notify(name.name+" travels with you now.")
        #store_say(None,"{color=#00db00}"+name.name+" travels with you now.")
            
        
    def party_remove(name):
        global party
        global followers
        if name in party:
            party.remove(name)
            if name in followers:
                renpy.notify(name.name+" leaves you.")
                #store_say(None,"{color=#FF0000}"+name.name+" left you.")
        
    def follower_add(name):
        global party
        global followers
        followers.append(name)
        name.loc = loc
        if name not in party:
            renpy.notify(name.name+" now follows you.")
            #store_say(None,"{color=#00db00}"+name.name+" now follows you.")
        
    def follower_remove(name):
        global party
        global followers
        if name in followers:
            followers.remove(name)
        renpy.notify(name.name+" is gone.")
        #store_say(None,"{color=#FF0000}"+name.name+" abandoned you.")
        if name in party:
            party_remove(name)
            
        
    
    def find_all_exits():
        for i in locations:
            if i.type == "grid":
                i.find_exits()

    def find_all_pop(): #Find population in locations
        for i in locations:
            i.pop = []
            for x in classmates:
                ppl_loc = x.loc
                if x.alive and x != you:
                    if ppl_loc.type == "room" and i.type == "room":
                        ppl_rm = ppl_loc
                        if ppl_rm == i:
                            ppl_rm.pop.append(x)
                            #ppl_loc.pop.append(x)
                    else:
                        ppl_rm = None
                        if ppl_loc == i:
                            ppl_loc.pop.append(x)
        # print "___LOC POPULATIONS___"
        # for i in locations:
            # print i.name
            # for x in i.pop:
                # print x.name
            # print "_______"
#     
    ### ADD TIME ###
    def add_time(num,do_ai=True):
        global day
        global hour
        global fz_start_day
        global fz_start_hour
        global show_report
        global fz_ticker
        global fz_reports
        counter = 0
        while counter < num:
            hour += 1
            renpy.sound.play("sfx/beep1.ogg",channel="system")
            renpy.show_screen("beep_green")
            renpy.pause(1.0)
            
            if hour > 23:
                hour -= 24
                day += 1
            if hour < 0:
                hour = 0
                
            if day == fz_start_day and hour == fz_start_hour:
                show_report = True
            elif fz_reports and day >= fz_start_day and hour >= fz_start_hour:
                fz_ticker += 1
                if fz_ticker >= fz_period:
                    fz_ticker = 0
                    show_report = True
                
            if do_ai:
                #print "___MOVE AI___"
                move_ai() #move players around grid
                #print "***FINDING POPS..."
                find_all_pop() #tally population in each area
                #print "___BOT ACTIONS___"
                attack_ai() #trigger bot actions
            counter += 1
            
    def move_ai(ai_move=True):
        global day
        global hour
        global trap_set
        global trap_caught_person
        for i in classmates:
            trapped = False
            moved = False
            
            if i.loc == trap_loc and trap_set and i != you and i.alive and i not in party:
                trapped = True
                trap_caught_person = i
                trap_set = False
            
            if i.route is not None and not trapped:
                for x in i.route:
                    if x[0] == day and x[1] == hour:
                        i.loc = x[2]
                        moved = True
                
            if not moved and not trapped:
                if i.alive and i != you and i not in party:
                    #print i.name,", Sanity:",i.sanity
                    
                    this_place = i.loc
                    people_here = this_place.pop
                    friend_here = False
                    
                    #chance to move based on archetype
                    #print "***FINDING MOVE CHANCE ..."
                    if i.type == "hostile":
                        move_chance = renpy.random.randint(1,3)
                    elif i.type == "normal":
                        if len(people_here) > 1: #if they're not alone
                            for x in people_here:
                                if x in i.friends:
                                    
                                    friend_here = True
                        if friend_here:
                            move_chance = renpy.random.randint(1,30)#lower chance to move because they're with friends
                        else:
                            move_chance = renpy.random.randint(1,6)
                    elif i.type == "coward":
                        move_chance = renpy.random.randint(1,12)
                    else: #don't ever move
                        move_chance = 0
    
                    if i.loc.zone.forbidden: #move if in forbidden zone
                        move_chance = 1
    
                    # Test if we are trapped. If all the exits are forbidden zones, we're screwed!
                    surrounded = len(i.loc.zone.exits)
                    for x in i.loc.zone.exits:
                        if x.forbidden:
                            surrounded -= 1
                    trapped = surrounded <= 0

                    if move_chance == 1:
                        #print "***MOVING ..."
                        if i.loc.room is not None and not i.loc.zone.forbidden and i.sanity >= 15 and i.health >= 15: # Chance to move to a loc's room
                            room_chance = i.loc.room.visibility * 10
                            num = renpy.random.randint(0,100)
                            if num < room_chance and i.loc.room.keys is None or i.loc.room.keys is not None and i.item in i.loc.room.keys:
                                i.loc = i.loc.room

                        if not i.loc.type == "room" or i.loc.zone.forbidden:
                            if i.loc.zone.forbidden:
                                i.loc = i.loc.zone
                            places_to_go = []
                            if i.sanity <= 15 or i.health <= 15: #must pass sanity check to avoid kill zones
                                #print "***INSANE, WILL MOVE TO FZs"
                                places_to_go = i.loc.exits
                            else:
                                #print "***SANE, AVOIDING FZs"
                                for x in i.loc.exits: #check if there are forbidden zones around
                                    if not x.forbidden: 
                                        places_to_go.append(x)
                        
                            if len(places_to_go) > 0: #check if they're not trapped
                                rand_exit = renpy.random.choice(places_to_go) #random exit
                                i.loc = rand_exit
                            else:
                                stay_effects(i,True) #don't move, trapped
                    else:
                        stay_effects(i,trapped) #don't move

                    # Their final loc is a forbidden zone. RIP in peace
                    if i.loc.zone.forbidden:
                        i.kill("rules")

    def stay_effects(i,trapped):
        if trapped:
            #being trapped makes you go crazy
            i.sanity -= 15
            #print "- trapped and lost sanity (", i.sanity,")"

            # Make them wander around
            if i.type != "normal" and i.type != "coward" and i.type != "hostile":
                i.type = "normal"
            return
        friend_here = False
        if len(i.loc.pop) > 1: #if they're not alone
            for x in i.loc.pop:
                if x in i.friends:
                    friend_here = True
        if not friend_here:
            #chance to lose sanity
            num = renpy.random.randint(0,100)
            if num < 25:
                i.sanity -= 5
            elif num > 50:
                # recover sanity instead, people die in forbidden zones too frequently
                i.sanity += 1
        else:
            # we're with a friend! Keep recovering sanity.
            i.sanity += 1
   
    def attack_ai():
        for i in locations:
            if len(i.pop) > 0:
                for x in range(0,len(i.pop)):
                    if x != (len(i.pop)-1):
                        guy1 = i.pop[x]
                        guy2 = i.pop[x+1]
                        #print "*",guy1.name," vs ",guy2.name
                        
                        if guy1 in party or guy2 in party or guy1.invisible or guy2.invisible:
                            #Make sure party members aren't tangled up in this, or invisible people
                            pass
                        else:
                            guy1_attacks = True
                            guy2_attacks = True
            
                            # Are they friends? (both required to not attack)
                            if guy2 in guy1.friends and guy1.type != "hostile":
                                if guy1.sanity > 50:
                                    guy1_attacks = False
                                    #print "- ",guy1.name, " considers ",guy2.name," a friend"
                                else:
                                    num = renpy.random.randint(0,100)
                                    if num > 20:
                                        guy1_attacks = False
                                    
                            
                            if guy1 in guy2.friends and guy2.type != "hostile":
                                if guy2.sanity > 50:
                                    guy2_attacks = False
                                    #print "- ",guy2.name, " considers ",guy1.name," a friend"
                                else:
                                    num = renpy.random.randint(0,100)
                                    if num > 20:
                                        guy2_attacks = False
             
                            if guy1_attacks or guy2_attacks:
                                #print "- SHOWDOWN!"
                                showdown(guy1,guy2)
                                break
                                attack_ai()
                                
                        
    # AI BATTLE
    def showdown(guy1, guy2):
        ##find attacker 1's battle rating##
        if guy1.invincible:
            guy1_rating = 999
        else:
            if guy1.wpn is not None:
                guy1_wpn = guy1.wpn
                guy1_range = guy1_wpn.wpn_range
            else:
                #if no weapon, fights with hands
                guy1_wpn = fist
                guy1_range = "melee"
                
            #give bonus for secondary item or weapon
            if guy1.item is not None:
                guy1_bonus = (guy1.item[0].wpn_rating/2) + guy1.item[0].defense
            else:
                guy1_bonus = 0
    
            guy1_rating = guy1_wpn.wpn_rating + guy1_bonus
            
            #Give weapon range bonus
            if guy1_range == "ranged" or guy1_range == "both":
                guy1_rating += 1
            elif guy1_range == "explosive":
                guy1_rating -= 1
                
            #Give personality bonus
            if guy1.type == "hostile":
                guy1_rating += 1
            elif guy1.type == "coward":
                guy1_rating -= 1
            
        #print "-- ",guy1.name," rating: ",guy1_rating
        
        ##find attacker 2's battle rating##
        if guy2.invincible:
            guy2_rating = 999
        else:
            if guy2.wpn is not None:
                guy2_wpn = guy2.wpn
                guy2_range = guy2_wpn.wpn_range
            else:
                #if no weapon, fights with hands
                guy2_wpn = fist
                guy2_range = "melee"
                
            #give bonus for secondary item or weapon
            if guy2.item is not None:
                guy2_bonus = (guy2.item[0].wpn_rating/2) + guy2.item[0].defense
            else:
                guy2_bonus = 0
    
            guy2_rating = guy2_wpn.wpn_rating + guy2_bonus
            
            #Give weapon range bonus
            if guy2_range == "ranged" or guy2_range == "both":
                guy2_rating += 1
            elif guy2_range == "explosive":
                guy2_rating -= 1
                
            #Give personality bonus
            if guy2.type == "hostile":
                guy2_rating += 1
            elif guy2.type == "coward":
                guy2_rating -= 1
                
        if guy1.health < guy2.health:
            guy2_rating += 1
        elif guy1.health > guy2.health:
            guy1_rating += 1
            
        #print "-- ",guy2.name," rating: ",guy2_rating
            
        if guy1_rating > guy2_rating:
            guy2.kill("murder",guy1)
            guy1_killed = False
            #print guy1.name," KILLS ",guy2.name,"!"
        elif guy2_rating > guy1_rating:
            guy1.kill("murder",guy2)
            guy1_killed = True
            #print guy2.name," KILLS ",guy1.name,"!"
        else:
            #they're matched, so it's random
            num = renpy.random.randint(0,100)
            if num > 50:
                guy2.kill("murder",guy1)
                guy1_killed = False
                #print guy1.name," KILLS ",guy2.name,"!"
            else:
                guy1.kill("murder",guy2)
                guy1_killed = True
                #print guy2.name," KILLS ",guy1.name,"!"
                
        if guy1_killed:
            ##What the winner does with the victim's stuff
            guy2.sanity -= 10
            guy2.health -= 10
            #Trade weapons if the victim's is better
            if guy1.wpn.wpn_rating > guy2.wpn.wpn_rating and guy1.wpn is not fist:
                guy2_oldwpn = guy2.wpn
                guy2.wpn = guy1.wpn
                if guy2.item is None: #Keep both weapons if slot available
                    #print "Takes new weapon, keeps old one"
                    guy2.item = [guy2_oldwpn,1]
                else:
                    #print "Dumps old weapon"
                    guy2_oldwpn.drop(char=guy1) #Otherwise, dump it
            elif guy2.item is None and guy1.wpn is not fist:
                #print "Takes victim's weapon,",guy1.wpn.name
                guy2.item = [guy1.wpn,1]
            elif guy1.wpn is not None and guy1.wpn is not fist:
                #print "Leaves victim's weapon"
                guy1.wpn.drop(char=guy1) #Leave victim's stuff
                
            #Take victim's items
            if guy2.item is None and guy1.item is not None:
                #print "Takes victim's stuff"
                guy2.item = [guy1.item,1]
            elif guy1.item is not None:
                #print "Abadons victim's things"
                guy1.item[0].drop(char=guy1) #Or abandon it
                
            #if guy2.item is None:
                #print guy2.name," now has ",guy2.wpn.name,"&",guy2.item.name
            #else:
                #print guy2.name," now has ",guy2.wpn.name
        else:
            #Same if other way around
            guy1.sanity -= 10
            guy1.health -= 10
            if guy2.wpn.wpn_rating > guy1.wpn.wpn_rating and guy2.wpn is not fist:
                guy1_oldwpn = guy1.wpn
                guy1.wpn = guy2.wpn
                if guy1.item is None:
                    #print "Takes new weapon, keeps old one"
                    guy1.item = [guy1_oldwpn,1]
                else:
                    #print "Dumps old weapon"
                    guy1_oldwpn.drop(char=guy2)
            elif guy1.item is None and guy2.wpn is not fist:
                #print "Takes victim's weapon,",guy2.wpn.name
                guy1.item = [guy2.wpn,1]
            elif guy2.wpn is not None and guy2.wpn is not fist:
                #print "Leaves victim's weapon"
                guy2.wpn.drop(char=guy2)
                
            if guy1.item is None and guy2.item is not None:
                #print "Takes victim's stuff"
                guy1.item = [guy2.item,1]
            elif guy2.item is not None:
                #print "Abadons victim's things"
                guy2.item[0].drop(char=guy2)
#                 
            # if guy1.item is not None:
                # #print guy1.name," now has ",guy1.wpn.name,"&",guy1.item.name
            # else:
                # #print guy1.name," now has ",guy1.wpn.name
                
    


    
    
######################################
###################################### SCREENS #
######################################

##############
## OVERLAY ##
##############
init:
    $ item_picked = None
    $ item_picked_amt = 1
    $ item_to_drop = None
    $ minimap = False
    
screen health:
    zorder 90
    if show_black_gradient:
        add "gui/black_gradient.png" xalign 0.0 yalign 0.0
    vbox:
        xpos 5 ypos 5
        hbox:
            $ full_bar_graphic = ConditionSwitch(
                "health <= 20", "red_bar_flash4",
                "health <= 40", "red_bar_flash3",
                "health <= 60", "red_bar_flash2",
                "health <= 80", "red_bar_flash1",
                "True", "red_bar",)
            bar:
                value health+5
                range 100
                left_bar full_bar_graphic
                right_bar "empty_bar"
                thumb None
                xmaximum 125
            text "Health" ypos 4 xpos -63 xanchor 0.5 size 14
        hbox:
            #xpos -60
            $ full_bar_graphic = ConditionSwitch(
                "sanity <= 20", "green_bar_flash4",
                "sanity <= 40", "green_bar_flash3",
                "sanity <= 60", "green_bar_flash2",
                "sanity <= 80", "green_bar_flash1",
                "True", "green_bar",)
            bar:
                value sanity+5
                range 100
                left_bar full_bar_graphic
                right_bar "empty_bar"
                thumb None
                xmaximum 125
            text "Sanity" ypos 4 xpos -63 xanchor 0.5 size 14
            
        if show_time:
            frame:
                ypos 5
                xpos 0.325 xanchor 0.5
                has vbox
                $ show_time = str(hour)
                if hour < 10:
                    $ show_time = "0"+show_time
                
                $ datetime = "{color=#FFF}%d{/color}d.{color=#FFF}%s{/color}00h"%(day, show_time)
                text datetime size 16 color "#3a843a"
                hbox:
                    ypos 2
                    if wpn is not None and wpn.wpn_rating > 0:
                            $ show_wpn = "{color=#00ff00}"+str(wpn.wpn_rating)+"{/color}"
                    else:
                        $ show_wpn = "{color=#398339}0{/color}"
                    if armor is not None and armor.defense > 0:
                            $ show_armor = "{color=#00ff00}"+str(armor.defense)+"{/color}"
                    else:
                        $ show_armor = "{color=#398339}0{/color}"
                    add "gui/weapon.png"
                    text show_wpn ypos -1 size 16
                    add "gui/armor.png"
                    text show_armor ypos -1 size 16
        
        hbox ypos 5 xpos -2:                                              
            if minimap:                                     
                imagebutton idle "gui/overlay_items1.png" hover "gui/overlay_items3.png" action SetVariable("minimap",False) xalign 1.0
            else:
                imagebutton idle "gui/overlay_items4.png" hover "gui/overlay_items2.png" action SetVariable("minimap",True) xalign 1.0
                
            if minimap:
                imagebutton idle "gui/overlay_map4.png" hover "gui/overlay_map2.png" action SetVariable("minimap",False) xalign 1.0
            else:
                imagebutton idle "gui/overlay_map1.png" hover "gui/overlay_map3.png" action SetVariable("minimap",True) xalign 1.0
            
            
    hbox: # display items
        ypos 5 xpos 800
        xanchor 1.0
                
            
        if not minimap:
            for i in inventory:
                $ itm = i[0]
                $ itm_amt = i[1]
                vbox:
                    
                    frame:
                        xminimum 120
                        xmaximum 155
                        $ showing_item = im.FactorScale("icons/"+itm.name+".jpg", .5, .5)
                        $ showing_item2 = im.MatrixColor((im.FactorScale("icons/"+itm.name+".jpg", .5, .5)),im.matrix.brightness(0.25))
                        if itm_amt > 1:
                            $ howmuchtoshow = "%s (%d)"%(itm.fancy_name, itm_amt)
                        else:
                            $ howmuchtoshow = itm.fancy_name
                            
                        if itm.broken:
                            if itm.type == "gun":
                                $ howmuchtoshow += "\n{size=9}{color=#FF0000}(NO AMMO){/color}{/size}"
                            elif itm.type == "filled":
                                $ howmuchtoshow += "\n{size=9}{color=#FF0000}(EMPTY){/color}{/size}"
                            elif weapon_range="melee":
                                $ howmuchtoshow += "\n{size=9}{color=#FF0000}(NO POWER){/color}{/size}"
                            else:
                                $ howmuchtoshow += "\n{size=9}{color=#FF0000}(BROKEN){/color}{/size}"
                        elif wpn == itm or armor == itm:
                                $ howmuchtoshow += "\n{size=7}{color=#00ff00}(EQUIPPED){/color}{/size}"
                        vbox:
                            xpos 0.5 xanchor 0.5
                            imagebutton idle showing_item hover showing_item2 xpos 0.5 xanchor 0.5 xalign 0.5 clicked ui.callsinnewcontext("items")
                            text howmuchtoshow xpos 0.5 xanchor 0.5 size 12 layout "subtitle" text_align 0.5
                    if itm.uses > 0 and not itm.broken:
                            $ num_bullets = itm.uses - itm.use_count
                            if itm == wpn or itm == armor or itm.broken or len(itm.name) > 11:
                                $ bullet_y = -47
                            else:
                                $ bullet_y = -40
                            hbox xpos 0.32 ypos bullet_y:
                                for i in range(0,num_bullets):
                                    if itm.type == "gun":
                                        add "gui/bullet.png"  
                                    elif itm.type == "fuel":
                                        add "gui/fuel.png"
                                    else:
                                        add "gui/battery.png"  
                       
        else:
            null width 245
        null width 5

    if show_time:
        add "gui/light0.png" xpos 87 ypos 93
        add "gui/light0.png" xpos 99 ypos 93
        add "gui/light0.png" xpos 111 ypos 93
        
    vbox:
        ypos 5 xpos 135
        if len(loc.bodies) > 0:
            text "{u}BODIES:{/u}" size 15 color "#FFF"
            for i in loc.bodies:
                frame:
                    has hbox
                    add (im.MatrixColor(im.FactorScale("char/"+i.portrait+".jpg", .3, .3),im.matrix.tint(1,0,0))) yalign 0.5
                    null width 5
                    $ fancy_show_name = i.name+"\n"+i.last_name
                    text fancy_show_name size 10 color "#d3ffd3" yalign 0.5
    if show_drop_stuff or tut_show_pickup:       
        vbox:
            ypos 375 xpos 145
            if len(loc.items) > 0:
                text "{u}ITEMS:{/u}" size 15 color "#FFF"
                hbox:
                    for i in loc.items:
                        vbox:
                            if show_drop_stuff or tut_show_pickup or tut_show_drop:
                                imagebutton idle (im.FactorScale("icons/"+i[0].name+".jpg", .5, .5)) hover (im.MatrixColor((im.FactorScale("icons/"+i[0].name+".jpg", .5, .5)),im.matrix.brightness(0.25))) action [SetVariable("item_picked", i[0]),Jump("item_loc_selection")]
                            else:
                                add (im.FactorScale("icons/"+i[0].name+".jpg", .5, .5))
                            
                            if i[1] == 1:
                                $ fancy_show_name = ""
                            else:
                                $ fancy_show_name ="%d"% i[1]
                            
                            text fancy_show_name size 10 ypos -15
                        
    if minimap:
        frame xpos 555:
            add "map/grid_mini.png"
        for i in locations:
            if loc.zone == i:
                add "map/minimap_indicator.png" xpos (i.minimap_x+566) ypos (i.minimap_y+10)
        for i in locations:
            if i.type == "room" and len(i.keys) > 0 and i.found and i != rm_cave:# don't want the cave to have a mini-map icon
                add "map/minimap_lock.png" xpos (i.zone.minimap_x+566) ypos (i.zone.minimap_y+10)
                
                
                
#######################   
### OVERLAY EXTRAS ###
########################

#Notification text that comes up whenever you get something, lose health, etc.
screen notify:
    zorder 100
    text message at _notify_transform size 15 color "#00fc00" outlines [(2, "#000", 0, 0)] text_align 0.0 xalign 0.0 yalign 0.0
    timer 2.25 action Hide('notify')

transform _notify_transform:
    xpos .5 ypos notify_y xanchor 0.5
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
        
screen beep_green:
    zorder 100
    add "gui/light1.png" xpos 111 ypos 93 at _beep_transform
    timer 0.5 action Hide('beep_green')
    
screen beep_yellow:
    zorder 100
    add "gui/light3.png" xpos 99 ypos 93 at _beep_transform
    timer 0.5 action Hide('beep_yellow')
    
screen beep_yellow_continuous:
    zorder 100
    add "gui/light3.png" xpos 99 ypos 93 at _beep_transform_repeat
    
screen beep_red:
    zorder 100
    add "gui/light2.png" xpos 87 ypos 93 at _beep_transform
    timer 0.5 action Hide('beep_red')

screen beep_red_continuous:
    zorder 100
    add "gui/light2.png" xpos 87 ypos 93 at _beep_transform_repeat
    
transform _beep_transform:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .25 alpha 0.0
        
transform _beep_transform_repeat:
    on show:
        alpha 0
        linear .25 alpha 1.0
        0.5
        linear .25 alpha 0.0
        repeat
        
    on hide:
        linear .5 alpha 0.0
        

#############
#### MAP ####
#############

label map:
    call screen map
    return
    
screen map:
    window:
        background Animation( im.Tile("map/bg1.jpg"),0.2,im.Tile("map/bg2.jpg"),0.2,im.Tile("map/bg3.jpg"),0.2,)
    add "map/grid.png"
    
    if not on_cutscene:
        textbutton "Exit" xanchor 1.0 yanchor 1.0 xpos 0.99 ypos 0.99 action Return() xminimum 150

    for i in locations:

        if i.type == "grid":
            $ top_cor_x = i.x
            $ top_cor_y = i.y
        else:
            python:
                parent = i.parent
                while parent.type == "room":
                    parent = parent.parent
            $ top_cor_x = parent.x
            $ top_cor_y = parent.y
                    
        if i.type == "grid" and i.found and i.landmark is not None:
            $ show_landmark = "map/"+i.landmark+".png" 
            add show_landmark xpos i.place_x ypos i.place_y
        if not i.found and i.type == "grid" and i.number != 5:
            add "map/fog.png" xpos i.x ypos i.y
        if i.type == "grid" and i.forbidden:
            add "map/x.png" xpos i.x ypos i.y
        if loc.zone == i:
            add "map/border.png" xpos i.x ypos i.y
        if (show_gps or gps.is_in_inventory()) and i.type == "grid":
            hbox:
                xpos (top_cor_x+2) ypos (top_cor_y+2)
                python:
                    #print i.name
                    loc_pop = []
                    loc_pop += i.pop
                    for moar in locations:
                        if moar.zone == i:
                            loc_pop += moar.pop
                        # if moar.type == "room":
                            # while moar.parent.type == "room":
                                # moar = moar.parent
                            # if moar.parent == i:
                                # loc_pop +=moar.pop
                    loc_pop = list(set(loc_pop))
                grid 4 4:#most is 16, otherwise game crashes
                    $count = 0
                    for z in loc_pop:
                        if z.loc.type == "room":
                            $ face_to_show = im.MatrixColor(im.FactorScale("char/"+z.portrait+".jpg", .25, .25),im.matrix.opacity(0.5))
                        else:
                            $ face_to_show = im.FactorScale("char/"+z.portrait+".jpg", .25, .25)
                        if z.alive:
                            $count += 1
                            add face_to_show
                            
                    if count != 16:
                        for moar in range(0,(16-count)):
                            null
        elif binoculars.is_in_inventory() and loc.type != "room":
            if i in loc.exits or i==loc:
                hbox:
                    xpos (top_cor_x+2) ypos (top_cor_y+2)
                    for z in i.pop:
                        if z.loc.type != "room" and not z.hidden:
                            $ face_to_show = im.FactorScale("char/"+z.portrait+".jpg", .25, .25)
                            if z.alive:
                                add face_to_show
        # else:
            # hbox:
                # xpos (top_cor_x+2) ypos (top_cor_y+2)
                # for z in i.pop:
                    # if z in followers and z.alive:
                        # if z.loc.type == "room":
                            # $ face_to_show = im.MatrixColor(im.FactorScale("char/"+z.portrait+".jpg", .25, .25),im.matrix.opacity(0.5))
                        # else:
                            # $ face_to_show = im.FactorScale("char/"+z.portrait+".jpg", .25, .25)
                        # add face_to_show
            
            
                        
###############
#### STATS ####
###############
                        
label stats:
    call screen stats
    return
    
screen stats:
    window:
        background Animation( im.Tile("map/bg1.jpg"),0.2,im.Tile("map/bg2.jpg"),0.2,im.Tile("map/bg3.jpg"),0.2,)

    vbox:
        ypos 15 xpos 0.5 xanchor 0.5
        add "map/players.png"
        bar:
            value players_alive
            range total_players
            left_bar "map/players_full.png"
            right_bar "map/players_empty.png"
            thumb None
            xmaximum 227
            ymaximum 34
        $player_score = "%d / %d"%(players_alive,total_players)
        text player_score xpos 0.5 xanchor 0.5 ypos -29 drop_shadow None outlines [(2,"#000",0,0)] size 16
        
    side "c r":
        area (50, 90, 700, 455)
        
        viewport id "vp":
            draggable True
            mousewheel True
            vbox:
                for i in classmates:
                    frame:
                        xmargin 5
                        xpadding 7
                        background Frame("map/line_box.png",5,5)
                        xfill True
                        has hbox
                        if i.alive:
                            $ portrait_name = "char/"+i.portrait+".jpg"
                        else:
                            $ portrait_name = LiveComposite((100,100),
                                (0,0),"char/"+i.portrait+".jpg",
                                (0,0),"map/lost.png",)
                        $ full_name = i.name+" "+i.last_name
                        $ full_gender = "Gender: {color=#fff}"+i.gender+"{/color}"
                        $ full_club = "Club: {color=#fff}%s{/color}"%i.club
                        $ full_desc = "{i}"+i.desc+"{/i}"
                        if not i.alive:
                            if i.death_type == "murder":
                                $ their_killer = i.murderer
                                $ their_killer = their_killer.name+" "+ their_killer.last_name
                                # The game's characters never actually acknowledge who killed who.
                                # So this information is purely meta
                                $ murder_info = ">Killed by [[REDACTED]"#+their_killer
                            elif i.death_type == "suicide":
                                $ murder_info = ">Suicide"
                            else:
                                $ murder_info = ">Forbidden Zone"
                                
                            if i.kills > 0:
                                $ murder_info += " >Kills [[{color=#FFF}"+str(i.kills)+"{/color}]"
                        elif i == you:
                            $ murder_info = ">Kills [[{color=#FFF}"+str(i.kills)+"{/color}]"
                            
                                
                        add portrait_name
                        null width 5
                        vbox:
                            hbox:
                                xfill True xmaximum 600
                                vbox:
                                    text full_name size 20 color "#00fa00"
                                    text full_gender size 16
                                    text full_club size 16
                                hbox:
                                    
                                    null width 5
                                if ((show_gps or gps.is_in_inventory()) and show_p_inv) or show_p_inv_always:
                                    hbox:
                                        xalign 1.0
                                        if i.wpn is not None:
                                            add (im.FactorScale("icons/"+i.wpn.name+".jpg", .5, .5)) xalign 1.0
                                        if i.item is not None:
                                            add (im.FactorScale("icons/"+i.item[0].name+".jpg", .5, .5)) xalign 1.0
                            text full_desc
                            if not i.alive or i == you:
                                null height 5
                                text murder_info color "#FF0000" size 16
                        

        vbar value YScrollValue("vp")

    if not on_cutscene:
        textbutton "Exit" xanchor 1.0 yanchor 1.0 xpos 0.99 ypos 0.99 action Return() xminimum 150

###################
#### INVENTORY ###
##################

screen items:
    window:
        background Animation( im.Tile("map/bg1.jpg"),0.2,im.Tile("map/bg2.jpg"),0.2,im.Tile("map/bg3.jpg"),0.2,)
    add "map/items.png" ypos 6 xpos 0.5 xanchor 0.5
    
    grid 2 2:
        xpos 0.5 xanchor 0.5 ypos 40
        spacing 10
        $ count = 0
        for i in inventory:
            $ itm = i[0]
            $ itm_amt = i[1]
            $ count += 1
            $ item_name = itm.name
            if itm.uses == 0:
                $ item_quantity = "Quantity: "+str(itm_amt)
            elif itm.type == "gun":
                $ ammo_left = itm.uses - itm.use_count
                if ammo_left <= 3:
                    $ item_quantity = "Ammo Left: {color=#ff0000}"+str(ammo_left)+"{/color}"
                else:
                    $ item_quantity = "Ammo Left: {color=#00FF00}"+str(ammo_left)+"{/color}"
            else:
                $ fuel_left = itm.uses - itm.use_count
                $ item_quantity = "Uses Left: {color=#00ed00}"+str(fuel_left)+"{/color}"
            $ fancy_item_name = itm.fancy_name
            $ item_desc = itm.desc
            $ item_wpn_rating = str(itm.wpn_rating)
            $ item_def_rating = str(itm.defense)
            $ item_heal_rating = str(itm.healing)
            $ item_sane_rating = str(itm.sanity)
            # if i.wpn_rating > 0 and wpn == i or i.defense > 0 and armor == i:
                # $ whattoshow = LiveComposite((100,100),
                    # (0,0),"icons/"+item_name+".jpg",
                    # (0,0),"icons/redborder.png",
                    # )
            $ whattoshow = "icons/"+item_name+".jpg"
                
            $ allowed_to_act = persistent.always_act or not (battling and not battle_selection) or health > 0
            
            frame:
                xpadding 10
                xminimum 390
                background Frame("map/line_box.png",5,5)
                has hbox
                vbox:
                    add whattoshow xalign 0.5 xanchor 0.5
                    null height 5
                    hbox:
                        add "gui/weapon.png"
                        if item_wpn_rating != "0":
                            text item_wpn_rating ypos -1 color "#fff" size 16
                        else:
                            text item_wpn_rating ypos -1 color "#398339" size 16
                        add "gui/armor.png"
                        if item_def_rating != "0":
                            text item_def_rating ypos -1 color "#fff" size 16
                        else:
                            text item_def_rating ypos -1 color "#398339" size 16
                        add "gui/heal.png"
                        if item_heal_rating != "0":
                            text item_heal_rating ypos -1 color "#fff" size 16
                        else:
                            text item_heal_rating ypos -1 color "#398339" size 16
                    vbox:
                        xalign 0.5 ypos 5
                        if (wpn != itm and armor != itm) and (itm.wpn_rating > 0 or itm.defense > 0) and itm.type != "explosive" and not itm.broken:
                            if allowed_to_act:
                                textbutton "EQUIP" text_style "small_button_text" style "small_button" action [Return("equip"),SetVariable("item_to_show",itm)]
                            else:
                                textbutton "EQUIP" text_style "small_button_text" style "small_button"
                        elif wpn == itm or armor == itm:
                            if allowed_to_act:
                                textbutton "EQUIPPED" text_style "unequip_button_text" style "unequip_button" action [Return("unequip"),SetVariable("item_to_show",itm)]
                            else:
                                textbutton "EQUIPPED" text_style "unequip_button_text" style "unequip_button"
                        else:
                            textbutton "EQUIP" text_style "small_button_text" style "small_button"
                        
                        if not allowed_to_act:
                            # Disable the button during enemy turn
                            textbutton "USE" text_style "small_button_text" style "small_button"
                        elif itm == trap:
                            textbutton "SET" text_style "small_button_text" style "small_button" action [Return("use"),SetVariable("item_to_show",itm)]
                        elif itm == bag:
                            textbutton "OPEN" text_style "small_button_text" style "small_button" action [Return("use"),SetVariable("item_to_show",itm)]
                        elif itm.healing > 0 and not itm.broken or itm.sanity > 0 and not itm.broken or itm == gas:
                            textbutton "USE" text_style "small_button_text" style "small_button" action [Return("use"),SetVariable("item_to_show",itm)]
                        else:
                            textbutton "USE" text_style "small_button_text" style "small_button"
                        
                        if show_drop_stuff and allowed_to_act:
                            textbutton "DROP" text_style "small_button_text" style "small_button" action [Return("drop"),SetVariable("item_to_show",itm)]
                        else:
                            textbutton "DROP" text_style "small_button_text" style "small_button"
                        null height 5
                        
                null width 5
                vbox:
                    text fancy_item_name size 19 color "#00fa00" layout "subtitle"
                    hbox:
                        text item_quantity size 16
                        if itm.broken:
                            text ("{size=10}{color=#FF0000}(Broken){/color}{/size}") xpos 70 ypos 5
                    null height 3
                    add "gui/hr.png"
                    null height 2
                    text item_desc xmaximum 260 size 15 color "#d2fed2"

        for i in range(count,4):
            frame:
                xpadding 10
                xminimum 390
                yminimum 226
                background Frame("map/line_box.png",5,5)
                null
    hbox:
        xpos 17 ypos 555
        xanchor 0.0 yanchor 1.0
        
        for i in followers:
            if i in party:
                $ follower_portrait = im.FactorScale("char/"+i.portrait+".jpg", .5, .5)
            else:
                $ follower_portrait = im.MatrixColor(im.FactorScale("char/"+i.portrait+".jpg", .5, .5),im.matrix.opacity(0.5))
            add follower_portrait
            null width 5
                
    hbox:
        xpos 15 ypos 585
        xanchor 0.0 yanchor 1.0
        
        hbox:
            bar:
                value health+5
                range 100
                left_bar Frame("gui/bar_full_red.png",5,5)
                right_bar Frame("gui/bar_empty.png",5,5)
                thumb None
                xmaximum 125
            text "Health" ypos 4 xpos -63 xanchor 0.5 size 14
        hbox:
            xpos -60
            bar:
                value sanity+5
                range 100
                left_bar Frame("gui/bar_full.png",5,5)
                right_bar Frame("gui/bar_empty.png",5,5)
                thumb None
                xmaximum 125
            text "Sanity" ypos 4 xpos -63 xanchor 0.5 size 14
        hbox:
            xpos -115
            ypos 5
            xanchor 0.0
            text "Your Ratings:" ypos -2 size 16
            null width 2
            if wpn is not None:
                $ show_wpn = "{color=#FFF}"+str(wpn.wpn_rating)+"{/color}"
            else:
                $ show_wpn = "{color=#398339}0{/color}"
            if armor is not None:
                $ show_armor = "{color=#FFF}"+str(armor.defense)+"{/color}"
            else:
                $ show_armor = "{color=#398339}0{/color}"
            add "gui/weapon.png"
            text show_wpn ypos -1 size 16
            add "gui/armor.png"
            text show_armor ypos -1 size 16
    if not on_cutscene:
        textbutton "Exit" xanchor 1.0 yanchor 1.0 xpos 0.99 ypos 0.99 action Return() xminimum 150

    
label items:
    $ notify_y = .095
    call screen items
    if _return == "use":
        if item_to_show == trap:
            $ trap_set = True
            $ trap_loc = loc
            $ trap_time = [day,hour]
            $ needs_to_be = [ (trap_time[0] + trap_required_time[0]), (trap_time[1] + trap_required_time[1]) ]
            python:
                while needs_to_be[1] > 23:
                    needs_to_be[1] -= 24
                    needs_to_be[0] += 1
            $ item_to_show.drop()
            $ renpy.notify("Setting trap ...")
            $ trap.use_sfx()
        elif item_to_show == gas:
            $ fuel_found = False
            python:
                for x in inventory:
                    if x[0].type == "fuel" and x[0].use_count > 0:
                        fuel_found = True
                        renpy.notify("Refilling weapon ...")
                        gas.use_sfx()
                        renpy.pause(1.0)
                        x[0].restore_use()
            if fuel_found:
                $ gas.destroy()
            else:
                memo "You don't have anything that needs gas."
        elif item_to_show == bag and tut_openbag:
            $ item_to_show.consume()
            $ renpy.notify("Opening bag ...")
            $ bag.use_sfx()
            show screen items
            $ renpy.pause(1.0,hard=True)
            hide screen items
            show screen health
            jump letsgo
        elif item_to_show.uses > 0:
            $ item_to_show.use()
        else:
            $ item_to_show.consume()
        jump items
    elif _return == "equip":
        $ item_to_show.equip()
        jump items
    elif _return == "unequip":
        $ item_to_show.unequip()
        jump items
    elif _return == "drop":
        $ item_to_show.drop("all")
        # update the grid location
        jump items
    else:
        if show_drop_stuff:
            jump grid_loc
    $ notify_y = .001
    return
    
label equip_wpn:     
    $ item_to_show.equip()
    if battling:
        return
    else:
        jump grid_loc
    
    
label use_item:    
    if item_to_show == trap:
        $ trap_set = True
        $ trap_loc = loc
        $ trap_time = [day,hour]
        $ needs_to_be = [ (trap_time[0] + trap_required_time[0]), (trap_time[1] + trap_required_time[1]) ]
        python:
            while needs_to_be[1] > 23:
               needs_to_be[1] -= 24
               needs_to_be[0] += 1
        $ item_to_show.drop()
        $ renpy.notify("Setting trap ...")
        $ trap.use_sfx()
    elif item_to_show == gas:
        $ fuel_found = False
        python:
            for x in inventory:
                if x[0].type == "fuel" and x[0].use_count > 0:
                    fuel_found = True
                    renpy.notify("Refilling weapon ...")
                    gas.use_sfx()
                    renpy.pause(1.0)
                    x[0].restore_use()
        if fuel_found:
            $ gas.destroy()
        else:
            memo "You don't have anything that needs gas."
    elif item_to_show == bag and tut_openbag:
        $ item_to_show.consume()
        $ renpy.notify("Opening bag ...")
        $ bag.use_sfx()
        show screen items
        $ renpy.pause(1.0,hard=True)
        hide screen items
        show screen health
        jump letsgo
    elif item_to_show.uses > 0:
        $ item_to_show.use()
    else:
        $ item_to_show.consume()
    if battling:
        return
    else:
        jump grid_loc
    

######################
#### ITEM POP-UPS ####
######################

label item_loc_selection:
    jump selection_one
    # if len(loc.items) == 1:
        # jump selection_one
    # else:
        # jump selection_many
        
label selection_one:
    if item_picked == trap and trap_set:
        call bear_trap_info
    else:
        python:
            if len(loc.items) > 0:
                for i in loc.items:
                    if i[0].name == item_picked.name:
                        item_picked_amt = i[1]
        $ item_picked.add(amt=item_picked_amt,silent=True,pickup=True)
    if item_picked == bag and tut_pickup:
        jump gui_tutorial2
    else:
        jump grid_loc
        
# label selection_many:
    # $ item_quantity = 0
    # call screen loc_inventory
    # $ item_to_add = _return
    # if item_to_add != 0:
        # if item_to_add == trap and trap_set:
            # call bear_trap_info
        # else:
            # $ item_to_add.add(item_quantity,True)
            # python:
                # for x in loc.items:
                    # if item_to_add == x[0]:
                        # x[1] = 0
    # if itm == bag and tut_pickup:
        # jump gui_tutorial2
    # elif len(loc.items) > 0 and item_to_add != 0:
        # jump selection_many
    # else:
        # jump grid_loc

label item_drop_selection:
    # call screen item_drop_select
    # $ item_to_drop = _return
    # if item_to_drop != 0:
    $ item_to_drop.drop()
    # if len(inventory) > 0 and item_to_drop != 0:
        # jump item_drop_selection
    # else:
    if battling:
        return
    else:
        jump grid_loc

screen loc_inventory:
    modal True
    zorder 100
    add "half_black"
    vbox:
        xpos .5 ypos .5
        xanchor 0.5 yanchor 0.5
        spacing 5
        text "{color=#FFF}{u}Pick Up Items{/u}{/color}" xpos 0.5 xanchor 0.5 size 22
        text "Choose which items you would like to pick up." xpos 0.5 xanchor 0.5 size 18 text_align 0.5
        null height 3
        frame:
            xpos .5 ypos .5
            xanchor 0.5 yanchor 0.5
            xpadding 15 ypadding 15
            $numitems = len(loc.items)
            $rows_to_make = numitems / 4
            $leftover = numitems % 4
            if leftover > 0:
                $rows_to_make += 1
            $squares_left = (4 * rows_to_make) - numitems
            
            grid 4 rows_to_make:
                spacing 4
                for i in range(0,numitems):
                    $ itm = loc.items[i][1]
                    $ itm_amt = loc.items[i][2]
                    
                    $ whattoshow = im.FactorScale("icons/"+itm.name+".jpg", .5, .5)
                    $ whattoshow_hover = im.FactorScale(im.MatrixColor("icons/"+itm.name+".jpg",im.matrix.brightness(0.25)), .5, .5)
                    if itm_amt > 1:
                        $ howmuchtoshow = "%s (%d)"%(itm.fancy_name, itm_amt)
                    else:
                        $ howmuchtoshow = itm.fancy_name
                    vbox:
                        xalign 0.5
                        imagebutton idle whattoshow hover whattoshow_hover action [SetVariable("item_quantity",itm_amt),Return(itm)] xalign 0.5
                        text howmuchtoshow  xalign 0.5 size 12
                for i in range(0,squares_left):
                    vbox:
                        xalign 0.5
                        add im.FactorScale(im.MatrixColor("icons/blank.jpg",im.matrix.opacity(0.5)), .5, .5)  xalign 0.5
                        text "" xalign 0.5 size 12
                

        textbutton "Cancel" xminimum 100 action Return(0) xpos 0.5 xanchor 0.5
        
screen explosive_inventory:
    modal True
    zorder 100
    add "half_black"
    vbox:
        xpos .5 ypos .5
        xanchor 0.5 yanchor 0.5
        spacing 5
        text "{color=#FFF}{u}Throw Explosive{/u}{/color}" xpos 0.5 xanchor 0.5 size 22
        text "Choose which explosive you want to throw.\nIt will destroy itself on impact." xpos 0.5 xanchor 0.5 size 18 text_align 0.5
        null height 3
        frame:
            xpos .5 ypos .5
            xanchor 0.5 yanchor 0.5
            xpadding 15 ypadding 15
            $numitems = len(explosives)
            $rows_to_make = numitems / 4
            $leftover = numitems % 4
            if leftover > 0:
                $rows_to_make += 1
            $squares_left = (4 * rows_to_make) - numitems
            
            grid 4 rows_to_make:
                spacing 4
                for i in range(0,numitems):
                    $ itm = explosives[i]
                    $ itm_amt =itm.amount
                    $ whattoshow = im.FactorScale("icons/"+itm.name+".jpg", .5, .5)
                    $ whattoshow_hover = im.FactorScale(im.MatrixColor("icons/"+itm.name+".jpg",im.matrix.brightness(0.25)), .5, .5)
                    if itm_amt > 1:
                        $ howmuchtoshow = "%s (%d)"%(itm.fancy_name, itm_amt)
                    else:
                        $ howmuchtoshow = itm.fancy_name
                    vbox:
                        xalign 0.5
                        imagebutton idle whattoshow hover whattoshow_hover action Return(itm) xalign 0.5
                        text howmuchtoshow  xalign 0.5 size 12
                for i in range(0,squares_left):
                    vbox:
                        xalign 0.5
                        add im.FactorScale(im.MatrixColor("icons/blank.jpg",im.matrix.opacity(0.5)), .5, .5)  xalign 0.5
                        text "" xalign 0.5 size 12
                

        textbutton "Cancel" xminimum 100 action Return(0) xpos 0.5 xanchor 0.5

transform _item_transform:
    xpos .5 ypos .5
    xanchor 0.5 yanchor 0.5
    on show:
        alpha 0
        linear .5 alpha 1.0
    on hide:
        linear .5 alpha 0.0
        
#When you get a new items
screen item_new:
    tag item
    zorder 100
    $ whattoshow = "icons/"+item_name+".jpg"
    if item_quantity > 1:
        $ howmuchtoshow = "%s (%d)"%(fancy_item_name, item_amt)
    else:
        $ howmuchtoshow = fancy_item_name
    vbox:
        xpos .9 ypos .3
        xanchor 0.5 yanchor 0.5
        frame:
            xpos .5 ypos .5
            xanchor 0.5 yanchor 0.5
            has vbox
            add whattoshow at _item_transform
            text howmuchtoshow xpos 0.5 xanchor 0.5 size 12
        text "NEW" xpos 0.5 xanchor 0.5 size 22 ypos -80
    timer 5.0 action Hide('item_new')
    
screen item_replace_prompt:
    tag item
    modal True
    zorder 100
    add "half_black"
    $ whattoshow = "icons/"+item_name+".jpg"
    if item_quantity > 1:
        $ howmuchtoshow = "%s (%d)"%(fancy_item_name, item_quantity)
    else:
        $ howmuchtoshow = fancy_item_name
    vbox:
        xpos .5 ypos .5
        xanchor 0.5 yanchor 0.5
        text "{color=#FFF}{u}You have more than 4 items!{/u}{/color}" xpos 0.5 xanchor 0.5 size 22
        text "Do you wish to swap an item for the one below?" xpos 0.5 xanchor 0.5 size 18
        null height 3
        frame:
            xpos .5 ypos .5
            xanchor 0.5 yanchor 0.5
            has vbox
            add whattoshow at _item_transform
            text howmuchtoshow xpos 0.5 xanchor 0.5 size 12
        hbox:
            xpos 0.5 xanchor 0.5
            textbutton "Yes" xminimum 100 action [SetVariable("swap",True),Return(True)]
            textbutton "No" xminimum 100 action [SetVariable("swap", False),Return(False)]

            
#Trade one of your items out for another
screen item_replace:
    tag item
    modal True
    zorder 100
    add "half_black"
    vbox:
        xpos .5 ypos .5
        xanchor 0.5 yanchor 0.5
        $ promptshow = "Select which item to drop for {color=#FFF}"+fancy_item_name+"{/color}."
        text promptshow xpos 0.5 xanchor 0.5 size 22 layout "subtitle"
        null height 3
        hbox:
            xpos .5 ypos .5
            xanchor 0.5 yanchor 0.5
            for i in inventory:
                $ itm = i[0]
                if itm != boat:
                    $ itm_amt = i[1]
                    $ whattoshow = "icons/"+itm.name+".jpg"
                    $ whattoshow_hover = im.MatrixColor("icons/"+itm.name+".jpg",im.matrix.brightness(0.25))
                    if itm_amt > 1:
                        $ howmuchtoshow = "%s (%d)"%(itm.fancy_name, itm_amt)
                    else:
                        $ howmuchtoshow = itm.fancy_name
                    frame:
                        xpos .5 ypos .5
                        xanchor 0.5 yanchor 0.5
                        has vbox
                        imagebutton idle whattoshow hover whattoshow_hover action [SetVariable("discarded",i),Return(True)] xcenter 0.5
                        text howmuchtoshow xpos 0.5 xanchor 0.5 size 12
        null height 3
        textbutton "Cancel" xminimum 100 action [SetVariable("discarded","cancel"),Return(True)] xpos 0.5 xanchor 0.5
        
screen item_drop_select:
    tag item
    modal True
    zorder 100
    add "half_black"
    vbox:
        xpos .5 ypos .5
        xanchor 0.5 yanchor 0.5
        text "{color=#FFF}{u}Drop Items{/u}{/color}" xpos 0.5 xanchor 0.5 size 22
        text "Select which item to drop." xpos 0.5 xanchor 0.5 size 18 layout "subtitle"
        null height 3
        hbox:
            xpos .5 ypos .5
            xanchor 0.5 yanchor 0.5
            for i in inventory:
                $ itm = i[0]
                $ itm_amt = i[1]
                $ whattoshow = "icons/"+itm.name+".jpg"
                $ whattoshow_hover = im.MatrixColor("icons/"+itm.name+".jpg",im.matrix.brightness(0.25))
                if itm_amt > 1:
                    $ howmuchtoshow = "%s (%d)"%(itm.fancy_name, itm_amt)
                else:
                    $ howmuchtoshow = itm.fancy_name
                frame:
                    xpos .5 ypos .5
                    xanchor 0.5 yanchor 0.5
                    has vbox
                    imagebutton idle whattoshow hover whattoshow_hover action Return(i) xcenter 0.5
                    text howmuchtoshow xpos 0.5 xanchor 0.5 size 12
        null height 3
        textbutton "Cancel" xminimum 100 action Return(0) xpos 0.5 xanchor 0.5
        
#Trade a follower's weapon out
screen follower_wpn_replace:
    tag item
    modal True
    zorder 100
    add "half_black"
    vbox:
        xpos .5 ypos .25
        xanchor 0.5 yanchor 0.0  
        $ char_name = wpn_replace_char.name
        $ wpn_name = wpn_replace_char.wpn
        $ wpn_name = wpn_name.fancy_name
        $ promptshow = "Select which weapon you want to give {color=#FFF}%s{/color}."%char_name
        #$ prompt_sub = "She currently has a {color=#FFF}%s{/color} equipped."%wpn_name
        text promptshow xpos 0.5 xanchor 0.5 size 22 layout "subtitle"
        text "You cannot trade equipped weapons." xpos 0.5 xanchor 0.5 size 15
        null height 3
        hbox:
            xpos .5 ypos .5
            xanchor 0.5 yanchor 0.5
            $ counter = 0
            for i in inventory:
                $ itm = i[0]
                $ itm_amt = i[1]
                if itm.wpn_rating > 0 and wpn != i and itm.type != "explosive":
                    $ counter += 1
                    $ whattoshow = "icons/"+itm.name+".jpg"
                    $ whattoshow_hover = im.MatrixColor("icons/"+itm.name+".jpg",im.matrix.brightness(0.25))
                    if itm_amt > 1:
                        $ howmuchtoshow = "%s x %d"%(itm.fancy_name, itm_amt)
                    else:
                        $ howmuchtoshow = itm.fancy_name
                    frame:
                        xpos .5 ypos .5
                        xanchor 0.5 yanchor 0.5
                        has vbox
                        imagebutton idle whattoshow hover whattoshow_hover action Return(i) xcenter 0.5
                        text howmuchtoshow xpos 0.5 xanchor 0.5 size 12
            if counter == 0:
                vbox:
                    frame:
                        xpos .5 ypos .5
                        xanchor 0.5 yanchor 0.5
                        add (im.MatrixColor("icons/blank.jpg",im.matrix.opacity(0.25)))
                    text "NO ITEMS\nAVAILABLE" ypos -72 text_align 0.5 size 13 xalign 0.5
                
                
        null height 3
        if counter == 0:
            textbutton "Cancel" xminimum 100 action Return(False) xpos 0.5 xanchor 0.5 ypos -20
        else:
            textbutton "Cancel" xminimum 100 action Return(False) xpos 0.5 xanchor 0.5
        null height 5
        add "gui/trade.png" xcenter 0.5
        null height 65
        frame:
            xpos .5
            xanchor 0.5 yanchor 0.5
            has vbox
            $ wpn_name = wpn_replace_char.wpn
            $ whattoshow2 = "icons/"+wpn_name.name+".jpg"
            $ howmuchtoshow2 = wpn_name.fancy_name
            add whattoshow2 xcenter 0.5
            text howmuchtoshow2 xpos 0.5 xanchor 0.5 size 12
        hbox:
            ypos -104
            xpos .46
            xanchor 0.5 yanchor 0.5
            add "gui/weapon.png"
            $ show_wpn = "{color=#FFF}"+str(wpn_name.wpn_rating)+"{/color}"
            text show_wpn
            
            
#Trade a follower's item (free extra pockets!)
screen follower_item_replace:
    tag item
    modal True
    zorder 100
    add "half_black"
    vbox:
        xpos .5 ypos .25
        xanchor 0.5 yanchor 0.0  
        $ char_name = wpn_replace_char.name
        $ item_name = wpn_replace_char.item
        if item_name != None:
            $ item_name = item_name[0].fancy_name
        $ promptshow = "Select which item you want to give {color=#FFF}%s{/color}."%char_name
        #$ prompt_sub = "She currently has a {color=#FFF}%s{/color} equipped."%item_name
        text promptshow xpos 0.5 xanchor 0.5 size 22 layout "subtitle"
        text "You cannot trade broken items." xpos 0.5 xanchor 0.5 size 15
        null height 3
        hbox:
            xpos .5 ypos .5
            xanchor 0.5 yanchor 0.5
            $ counter = 0
            # Allow you to trade for Nothing
            frame:
                xpos .5 ypos .5
                xanchor 0.5 yanchor 0.5
                has vbox
                imagebutton idle "icons/blank.jpg" hover im.MatrixColor("icons/blank.jpg",im.matrix.brightness(0.25)) action Return("nothing") xcenter 0.5
                text "Nothing" xpos 0.5 xanchor 0.5 size 12
            for i in inventory:
                $ itm = i[0]
                $ itm_amt = i[1]
                if not itm.broken and itm != boat: #and i != wpn and i != armor and itm.amount == 1 and itm.type != "explosive":
                    $ counter += 1
                    $ whattoshow = "icons/"+itm.name+".jpg"
                    $ whattoshow_hover = im.MatrixColor("icons/"+itm.name+".jpg",im.matrix.brightness(0.25))
                    if itm_amt > 1:
                        $ howmuchtoshow = "%s x %d"%(itm.fancy_name, itm_amt)
                    else:
                        $ howmuchtoshow = itm.fancy_name
                    frame:
                        xpos .5 ypos .5
                        xanchor 0.5 yanchor 0.5
                        has vbox
                        imagebutton idle whattoshow hover whattoshow_hover action Return(i) xcenter 0.5
                        text howmuchtoshow xpos 0.5 xanchor 0.5 size 12
            if counter == 0:
                vbox:
                    frame:
                        xpos .5 ypos .5
                        xanchor 0.5 yanchor 0.5
                        add (im.MatrixColor("icons/blank.jpg",im.matrix.opacity(0.25)))
                    text "NO ITEMS\nAVAILABLE" ypos -72 text_align 0.5 size 13 xalign 0.5
                
                
        null height 3
        if counter == 0:
            textbutton "Cancel" xminimum 100 action Return(False) xpos 0.5 xanchor 0.5 ypos -20
        else:
            textbutton "Cancel" xminimum 100 action Return(False) xpos 0.5 xanchor 0.5
        null height 5
        add "gui/trade.png" xcenter 0.5
        null height 65
        frame:
            xpos .5
            xanchor 0.5 yanchor 0.5
            has vbox
            $ item_name = wpn_replace_char.item
            if wpn_replace_char.item != None:
                $ whattoshow2 = "icons/"+item_name[0].name+".jpg"
                $ howmuchtoshow2 = item_name[0].fancy_name
                add whattoshow2 xcenter 0.5
                text howmuchtoshow2 xpos 0.5 xanchor 0.5 size 12
            else:
                null height 100 width 100
        if item_name is not None:
            if item_name[0].wpn_rating > 0 or item_name[0].defense > 0 or item_name[0].healing > 0:
                hbox:
                    ypos -104
                    xpos .46
                    xanchor 0.5 yanchor 0.5
                    if item_name[0].wpn_rating > 0:
                        add "gui/weapon.png"
                        $ show_wpn = "{color=#FFF}"+str(item_name[0].wpn_rating)+"{/color}"
                        text show_wpn
                    if item_name[0].defense > 0:
                        add "gui/armor.png"
                        $ show_wpn = "{color=#FFF}"+str(item_name[0].armor_rating)+"{/color}"
                        text show_wpn
                    if item_name[0].defense > 0:
                        add "gui/heal.png"
                        $ show_wpn = "{color=#FFF}"+str(item_name[0].healing)+"{/color}"
                        text show_wpn

#Show an item on screen while in a cutscene (not acquiring)
screen item_show:
    tag item
    zorder 100
    $ whattoshow = "icons/"+item_name+".jpg"
    vbox:
        xpos .25 ypos .5
        xanchor 0.5 yanchor 0.5
        null height 3
        frame:
            xpos .5 ypos .5
            xanchor 0.5 yanchor 0.5
            add whattoshow at _item_transform
    timer 4.0 action Hide('item_show')
    
init python:
    def reference_item(name):
        global item_name
        item_name = name.name
        renpy.show_screen("item_show")
    


########################
#### QUICK BUTTONS ####
########################

label _quick_save:
    $ renpy.sound.play("sfx/beep1.mp3", channel="system")
    $ renpy.notify("Saving ...")
    #$ renpy.pause(1.0)
    $ renpy.save('quicksave', _('Quick Save'))

    return

label _quick_load:
    call screen load_confrim
    $ do_load = _return
    if do_load:
        $ renpy.sound.play("sfx/beep_stutter.ogg", channel="system")
        $ renpy.notify("Loading ...")
        $ renpy.pause(0.25)
        $ renpy.load('quicksave')
    else:
        return
    
screen load_confrim:
    frame xalign 0.5 yalign 0.5:
        has vbox:
            text "Are you sure you want to {color=#00FF00}quick load{/color}?\n{size=-5}Your progress will be lost.{/size}" text_align 0.5 xalign 0.5
            hbox spacing 30  xalign 0.5:
                textbutton "Yes" action Return(True) xminimum 150 xalign 0.5
                textbutton "No" action Return(False) xminimum 150 xalign 0.5
                

init python:
    def quick_save():
        renpy.sound.play("sfx/beep_stutter.ogg", channel="system")
        renpy.notify("Saving ...")
        renpy.save('quicksave', _('Quick Save'))

    def toggle_skipping():
        config.skipping = not config.skipping
        renpy.restart_interaction()
        
    config.default_afm_enable = False
    config.default_afm_time = 10

    _preferences.afm_enable = False
    
    if not persistent.set_afm:
        _preferences.afm_time = 25 # Or something. 
        persistent.set_afm = True
    
    def toggle_auto():
       _preferences.afm_enable = not _preferences.afm_enable
       renpy.restart_interaction()
    
    show_buttons = True

    def button_game_menu():
        #This is the old school way to do it. Please use Screens for your own quick menu!
        if show_buttons:
            
            if renpy.variant("small"):
                ui.hbox(xpos=0.5, ypos=1.01, xanchor='center', yanchor='bottom')
                ui.imagebutton(im.MatrixColor("gui/q_save1.png",im.matrix.opacity(1.0)),"gui/q_save2.png", clicked=quick_save, xanchor='right', xalign=1.0)
                ui.imagebutton(im.MatrixColor("gui/q_load1.png",im.matrix.opacity(1.0)),"gui/q_load2.png", clicked=ui.callsinnewcontext("_quick_load"), xanchor='right', xalign=1.0)
                ui.imagebutton(im.MatrixColor("gui/q_prefs1.png",im.matrix.opacity(1.0)),"gui/q_prefs2.png", clicked=ui.callsinnewcontext("_game_menu_preferences"), xanchor='right', xalign=1.0)
                if config.skipping:
                    ui.imagebutton("gui/q_skip2.png","gui/q_skip2.png", clicked=toggle_skipping, xanchor='right', xalign=1.0)
                else:
                    ui.imagebutton(im.MatrixColor("gui/q_skip1.png",im.matrix.opacity(1.0)),"gui/q_skip2.png", clicked=toggle_skipping, xanchor='right', xalign=1.0)
                if _preferences.afm_enable:
                    ui.imagebutton("gui/q_auto2.png","gui/q_auto2.png", clicked=toggle_auto, xanchor='right', xalign=0.99)
                else:
                    ui.imagebutton(im.MatrixColor("gui/q_auto1.png",im.matrix.opacity(1.0)),"gui/q_auto2.png", clicked=toggle_auto, xanchor='right', xalign=0.99)
                ui.imagebutton(im.MatrixColor("gui/q_map1.png",im.matrix.opacity(1.0)),"gui/q_map2.png", clicked=ui.callsinnewcontext("map"), xanchor='right', xalign=1.0)
                
                ui.imagebutton(im.MatrixColor("gui/q_items1.png",im.matrix.opacity(1.0)),"gui/q_items2.png", clicked=ui.callsinnewcontext("items"), xanchor='right', xalign=1.0)
                ui.imagebutton(im.MatrixColor("gui/q_stats1.png",im.matrix.opacity(1.0)),"gui/q_stats2.png", clicked=ui.callsinnewcontext("stats"), xanchor='right', xalign=1.0)
                
                ui.close()
            else:
                ui.hbox(xpos=0.5, ypos=1.01, xanchor='center', yanchor='bottom')
                ui.imagebutton(im.MatrixColor("gui/q_save1.png",im.matrix.opacity(1.0)),"gui/q_save2.png", clicked=quick_save, xanchor='right', xalign=1.0)
                ui.imagebutton(im.MatrixColor("gui/q_load1.png",im.matrix.opacity(1.0)),"gui/q_load2.png", clicked=ui.callsinnewcontext("_quick_load"), xanchor='right', xalign=1.0)
                ui.imagebutton(im.MatrixColor("gui/q_prefs1.png",im.matrix.opacity(1.0)),"gui/q_prefs2.png", clicked=ui.callsinnewcontext("_game_menu_preferences"), xanchor='right', xalign=1.0)
                if config.skipping:
                    ui.imagebutton("gui/q_skip2.png","gui/q_skip2.png", clicked=toggle_skipping, xanchor='right', xalign=1.0)
                else:
                    ui.imagebutton(im.MatrixColor("gui/q_skip1.png",im.matrix.opacity(1.0)),"gui/q_skip2.png", clicked=toggle_skipping, xanchor='right', xalign=1.0)
                if _preferences.afm_enable:
                    ui.imagebutton("gui/q_auto2.png","gui/q_auto2.png", clicked=toggle_auto, xanchor='right', xalign=0.99)
                else:
                    ui.imagebutton(im.MatrixColor("gui/q_auto1.png",im.matrix.opacity(1.0)),"gui/q_auto2.png", clicked=toggle_auto, xanchor='right', xalign=0.99)
                ui.imagebutton(im.MatrixColor("gui/q_map1.png",im.matrix.opacity(1.0)),"gui/q_map2.png", clicked=ui.callsinnewcontext("map"), xanchor='right', xalign=1.0)
                
                ui.imagebutton(im.MatrixColor("gui/q_items1.png",im.matrix.opacity(1.0)),"gui/q_items2.png", clicked=ui.callsinnewcontext("items"), xanchor='right', xalign=1.0)
                ui.imagebutton(im.MatrixColor("gui/q_stats1.png",im.matrix.opacity(1.0)),"gui/q_stats2.png", clicked=ui.callsinnewcontext("stats"), xanchor='right', xalign=1.0)
                
                ui.close()
                


    config.window_overlay_functions.append(button_game_menu)
    

################
# DEATH'S DOOR #
################

label deaths_door:
    python:
        config.skipping = False
        config.allow_skipping = False
        has_healing_items = False
        for i in inventory:
            if i[0].healing > 0:
                has_healing_items = True
                break
    memo2 "{color=#FF0000}You're on death's door!{/color} This is your last opportunity to save yourself{w=1}{nw}"
    # Pause in text to give you indication this is timed
    if health <= 0:
        extend ".{w=1}{nw}"
    if health <= 0:
        extend ".{w=1}{nw}"
    if health <= 0:
        extend ".{w=1}{nw}"
    if health <= 0:
        extend ".{w=1}{nw}"
    if health <= 0:
        extend ".{w=1}"
    # If you spam click, you still get a chance
    if health <= 0:
        $ renpy.pause(2.0, hard=True)
    # If you continue being a gremlin, now you've done it to yourself.
    $ config.allow_skipping = True
    if health <= 0:
        jump game_over
    return


###################
### WAIT / SLEEP ###
###################

init python:
    #SLEEP
    def sleep(num):
        global health
        global sanity
        for i in range(0,num):
            add_time(1)
            # Your sanity heals quicker with more party members
            sanity_recover = 2 + len(party)*2

            if health < 100 or sanity < 100:
                add_health_sanity(10,sanity_recover)

            # Your party members will regain sanity, too.
            for ally in party:
                # At a lower rate
                ally.sanity += sanity_recover
                if ally.sanity > 100:
                    ally.sanity = 100

            renpy.pause(0.5)
            interrupt_sleep = False
            for x in classmates:
                #must only be able to sleep in rooms for this to work
                if x.loc == loc.parent and x.alive and not x in followers and x != you:
                    interrupt_sleep = True
                    interrupter = x
                    break

            if show_report or interrupt_sleep:
                if i <= 1:
                    hur = "an hour"
                else:
                    hur = str(i)+" hours"
                renpy.say(None, "You rest for "+hur+" before you are awoken.")
                
                if interrupt_sleep:
                    interrupter.move(loc)
                    renpy.show(interrupter.name)
                    advantage = True
                    if Jun in followers and Jun.loc == loc:
                        renpy.say(Jun.call_name, "Who the heck!?")
                        advantage = False
                    if Mari in followers and Mari.loc == loc:
                        renpy.say(Mari.call_name, "S-Someone's here!")
                        advantage = False
                    if interrupter.type == "hostile":
                        battle_start(interrupter,1,interrupter.name+" has found you!", "grid_loc", True, foe_advantage=advantage, allies_will_help=True)
                    elif interrupter.type == "coward":
                        renpy.say(None,interrupter.name+" stumbles inside, screams upon seeing you, and flees back out!")
                        interrupter.move("rand")
                    else:
                        renpy.say(None,interrupter.name+" stumbles inside, surprised to see anyone in here!")
                        if you in interrupter.enemies:
                            battle_start(interrupter,1,interrupter.name+" takes the opportunity to get rid of you!", "grid_loc", True, foe_advantage=advantage, allies_will_help=True)
                        elif interrupter.met:
                            renpy.jump(interrupter.name+"_talk")
                        else:
                            renpy.jump(interrupter.name+"_intro")
                else:
                    renpy.jump("grid_loc")
                    
                    
        if num == 1:
            hur = "an hour"
        else:
            hur = str(num)+" hours"
        renpy.say(None, "You slept for %s."%hur)
        
    #WAIT
    def wait(num):
        for i in range(0,num):
            add_time(1)
            add_sanity(-5)
            renpy.pause(0.5)
            interrupt_wait = False
            for x in classmates:
                #must only be able to sleep in rooms for this to work
                if x.alive and x.loc == loc and x != you and not x in followers:
                    interrupt_wait = True
                    interrupter = x
                    break
            if show_report or interrupt_wait:
                if num < 2:
                    hur = "an hour"
                else:
                    hur = str(i)+" hours"
                renpy.say(None, "You wait for "+hur+" until you hear something.")
                if interrupt_wait:
                    interrupter.move(loc)
                    renpy.show(interrupter.name)
                    if armor == camo:
                        renpy.say(None,"Sneak attacking "+interrupter.name+" would be easy.")
                    else:
                        renpy.say(None,interrupter.name+" doesn't realize you're here.")
                    camo_menu = [
                        ("[[Attack]","attack"),
                        ("Ignore","ignore"),
                        ]
                    result = renpy.display_menu(camo_menu )
                    if result == "attack":
                        wpn.use_sfx()
                        if armor == camo:
                            interrupter.health -= 20
                            battle_start(interrupter,1,"You successfully sneak attack!", "grid_loc", True)
                        else:
                            interrupter.health -= 10
                            battle_start(interrupter,1,"You leap from the shadows!", "grid_loc", True)
                    else:
                        if interrupter.met:
                            renpy.jump(interrupter.name+"_talk")
                        else:
                            renpy.jump(interrupter.name+"_intro")
                else:
                    renpy.jump("grid_loc")
        if num == 1:
            hur = "an hour"
        else:
            hur = str(num)+" hours"
        renpy.say(None, "You wait for %s."%hur)
    

screen sleep_prompt:
    tag sleep
    modal True
    zorder 100
    add "half_black"
    vbox:
        xpos .5 ypos .6
        xanchor 0.5 yanchor 0.5
        text "{color=#FFF}{u}How long do you wish to sleep?{/u}{/color}" xpos 0.5 xanchor 0.5 size 22
        text "This will recover health and sanity,\nbut you will be open to attack." xpos 0.5 xanchor 0.5 size 15 text_align 0.5
        null height 3
        frame:
            xpos .5 ypos .5
            xanchor 0.5 yanchor 0.5
            has vbox
            hbox:
                textbutton "1h" xminimum 50 action Return(1)
                textbutton "2h" xminimum 50 action Return(2)
                textbutton "3h" xminimum 50 action Return(3)
                textbutton "4h" xminimum 50 action Return(4)
            hbox:
                textbutton "5h" xminimum 50 action Return(5)
                textbutton "6h" xminimum 50 action Return(6)
                textbutton "7h" xminimum 50 action Return(7)
                textbutton "8h" xminimum 50 action Return(8)

        textbutton "Cancel" xminimum 100 action Return(0) xpos 0.5 xanchor 0.5
        
screen wait_prompt:
    tag sleep
    modal True
    zorder 100
    add "half_black"
    vbox:
        xpos .5 ypos .6
        xanchor 0.5 yanchor 0.5
        text "{color=#FFF}{u}How long do you wish to wait?{/u}{/color}" xpos 0.5 xanchor 0.5 size 22
        text "You will lose a small amount of sanity for each hour you wait." xpos 0.5 xanchor 0.5 size 15 text_align 0.5
        null height 3
        frame:
            xpos .5 ypos .5
            xanchor 0.5 yanchor 0.5
            has vbox
            hbox:
                textbutton "1h" xminimum 50 action Return(1)
                textbutton "2h" xminimum 50 action Return(2)
                textbutton "3h" xminimum 50 action Return(3)
                textbutton "4h" xminimum 50 action Return(4)
            hbox:
                textbutton "5h" xminimum 50 action Return(5)
                textbutton "6h" xminimum 50 action Return(6)
                textbutton "7h" xminimum 50 action Return(7)
                textbutton "8h" xminimum 50 action Return(8)

        textbutton "Cancel" xminimum 100 action Return(0) xpos 0.5 xanchor 0.5


################
#### BATTLE ####
################
init:
    $ battle_static = Animation(im.Tile(im.MatrixColor("map/bg1.jpg",im.matrix.opacity(0.5))),0.2, im.Tile(im.MatrixColor("map/bg2.jpg",im.matrix.opacity(0.5))),0.2, im.Tile(im.MatrixColor("map/bg3.jpg",im.matrix.opacity(0.5))),0.2,)
    $ battle_static2 = Animation(im.Tile(im.MatrixColor("map/bg1.jpg",im.matrix.opacity(0.75))),0.2, im.Tile(im.MatrixColor("map/bg2.jpg",im.matrix.opacity(0.75))),0.2, im.Tile(im.MatrixColor("map/bg3.jpg",im.matrix.opacity(0.75))),0.2,)
#Opening graphic for battle
screen battle_start:
    add battle_static at _beep_transform
    add "gui/scanline_h.png" at _scan_h
    add "gui/scanline_v.png" at _scan_v
    vbox:
        xpos 0.61 ypos 0.5
        xanchor 0.5# yanchor 0.5
        add "target_locked" at _beep_transform xpos 25
    timer 2.5 action Hide('battle_start')
    timer 2.5 action Show('battle_start2')
    
screen battle_start2:
    add battle_static
    add battle_static2 at _fade_transform
    timer 0.5 action Hide('battle_start2')
    timer 0.5 action Show('new_battle')
    
transform _fade_transform:
    on show:
        alpha 0
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0
 
transform _scan_h:
    #xpos 0.5 ypos 0.5 xanchor 0.0 yanchor 0.5
    on show:
        alpha 0
        0.25
        alpha 1.0
        ypos 0.0
        linear 0.75 ypos 1.0
    on hide:
        linear 1.0 alpha 0.0
        
transform _scan_v:
    #xpos 0.5 ypos 0.5 xanchor 0.0 yanchor 0.5
    on show:
        alpha 0
        0.25
        alpha 1.0
        xpos 0.0
        linear 0.75 xpos 1.0
    on hide:
        linear 1.0 alpha 0.0
        
# Enemy overlay
screen health_enemy:
    zorder 90
    vbox:
        xpos 5 ypos 375
        text (enemy.name)
        
        hbox:
            $ full_bar_graphic = ConditionSwitch(
                "enemy.health <= 20", "red_bar_flash4",
                "enemy.health <= 40", "red_bar_flash3",
                "enemy.health <= 60", "red_bar_flash2",
                "enemy.health <= 80", "red_bar_flash1",
                "True", "red_bar",)
            bar:
                value enemy.health+5
                range 100
                left_bar full_bar_graphic
                right_bar "empty_bar"
                thumb None
                xmaximum 125
            text "Health" ypos 4 xpos -63 xanchor 0.5 size 14
        hbox:
            #xpos -60
            $ full_bar_graphic = ConditionSwitch(
                "enemy.sanity <= 20", "green_bar_flash4",
                "enemy.sanity <= 40", "green_bar_flash3",
                "enemy.sanity <= 60", "green_bar_flash2",
                "enemy.sanity <= 80", "green_bar_flash1",
                "True", "green_bar",)
            bar:
                value enemy.sanity+5
                range 100
                left_bar full_bar_graphic
                right_bar "empty_bar"
                thumb None
                xmaximum 125
            text "Sanity" ypos 4 xpos -63 xanchor 0.5 size 14
            
        frame:
            xpos  775
            ypos -90
            xanchor 1.0
            has hbox
            if enemy.wpn != None:
                $ enemy_wpn_img = im.FactorScale("icons/"+enemy.wpn.name+".jpg", .75, .75)
                #$ enemy_wpn_img = "icons/"+enemy_wpn.name+".jpg"
                add enemy_wpn_img
            if enemy.item is not None:
                $ enemy_itm_img = im.FactorScale("icons/"+enemy.item[0].name+".jpg", .75, .75)
                add enemy_itm_img
        if enemy.item is not None:
            if enemy.item[1] > 1:
                text "%d"%enemy.item[1] xpos  750 ypos -120
                
                
screen health_enemy2:
    zorder 90
    vbox:
        xpos 5 ypos 305
        text (enemy.name)
        
        hbox:
            $ full_bar_graphic = ConditionSwitch(
                "enemy.health <= 20", "red_bar_flash4",
                "enemy.health <= 40", "red_bar_flash3",
                "enemy.health <= 60", "red_bar_flash2",
                "enemy.health <= 80", "red_bar_flash1",
                "True", "red_bar",)
            bar:
                value enemy.health+5
                range 100
                left_bar full_bar_graphic
                right_bar "empty_bar"
                thumb None
                xmaximum 125
            text "Health" ypos 4 xpos -63 xanchor 0.5 size 14
        hbox:
            #xpos -60
            $ full_bar_graphic = ConditionSwitch(
                "enemy.sanity <= 20", "green_bar_flash4",
                "enemy.sanity <= 40", "green_bar_flash3",
                "enemy.sanity <= 60", "green_bar_flash2",
                "enemy.sanity <= 80", "green_bar_flash1",
                "True", "green_bar",)
            bar:
                value enemy.sanity+5
                range 100
                left_bar full_bar_graphic
                right_bar "empty_bar"
                thumb None
                xmaximum 125
            text "Sanity" ypos 4 xpos -63 xanchor 0.5 size 14
        frame:
            ypos 5
            has hbox
            $ enemy_wpn_img = im.FactorScale("icons/"+enemy.wpn.name+".jpg", .75, .75)
            add enemy_wpn_img
            if enemy.item is not None:
                $ enemy_itm_img = im.FactorScale("icons/"+enemy.item[0].name+".jpg", .75, .75)
                add enemy_itm_img
            
        
