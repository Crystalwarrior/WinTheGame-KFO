label weapon_desc:
    if your_wpn.name == "axe":
        "You pull out a two-handed axe. The edge is quite sharp, but you would need to be close to use it."
    elif your_wpn.name == "bat":
        "You pull out a baseball bat. You frown, thinking that this is all you have to protect yourself. But it is better than nothing."
    elif your_wpn.name == "binoculars":
        "You pull out a pair of binoculars ... and then search the bag for anything more. There is nothing. What are you supposed to do with these?"
    elif your_wpn.name == "bow":
        "You pull out a long and complicated-looking bow and arrows. You've never shot a bow before in your life, but it looks like you will have to learn."
    elif your_wpn.name == "bulletproof":
        "You pull out a heavy garment and recognize it to be a bulletproof vest. Though this will come in handy, you're upset that it's all they gave you."
    elif your_wpn.name == "chainsaw":
        "You pull out a heavy duty chainsaw, frightening to even look at. It could be quite dangerous, but it is also very loud."
    elif your_wpn.name == "grenades":
        "You pull out an assortment of hand grenades with their pins tightly locked into the safe position. These would only be useful at range so you don't hurt yourself."
    elif your_wpn.name == "knife":
        "You pull out what looks like a kitchen knife. It is larger than a pocket knife, but you would still need to be very close for it to be any use."
    elif your_wpn.name == "ladle":
        "You pull out ... a soup ladle!? You frantically search the bag but there is nothing left. This is really your so-called \"weapon!\" You're suddenly very scared for your life."
    elif your_wpn.name == "pistol" or your_wpn.name == "glock" or your_wpn.name == "bayonet":
        "You pull out a small hand gun and ammunition. The weight and quality of it make you shiver. You've never owned a gun before."
        if your_wpn.name == "bayonet":
            "A knife is attached to the front of the gun ... it may be useful in melee combat as well. You're not sure how much damage it can do, though ..."
    # elif your_wpn.name == "poison":
        # "You pull out two bottles. You're confused until you read the labels and find out that they are poisonous ... They will be no use unless someone ingests them."
    elif your_wpn.name == "shoe":
        "... A shoe? They gave you a {u}shoe{/u} to defend yourself!? You feel almost as if you might cry."
    elif your_wpn.name == "shotgun" or your_wpn.name == "shotgun_sawed" or your_wpn.name == "shotgun_pump":
        "You pull out a shotgun and ammunition. You suddenly feel dangerous with it in your hands. Maybe you could really win this game?"
    elif your_wpn.name == "sickle":
        "You pull out a long harvesting tool. It's blade is sharp, and so it could be deadly. Still, it will be no match for a gun."
    elif your_wpn.name == "sniperrifle":
        "You pull out a long and complicated gun, and you recognize the scope and bi-pod, meaning it is a sniper rifle. You pray that you have good aim to make good use of it."
    elif your_wpn.name == "sword":
        "You pull out a flawless katana from the bag, but even though it is beautiful, it will not be a match for any gun. Still, your weapon could have been a lot worse."
    elif your_wpn.name == "taser":
        "You pull out a handheld taser. You click it on and jump at the loud, electric bolts that leap from the prongs. You're not sure if it could kill anyone, but it could incapacitate someone."
    elif your_wpn.name == "walkietalkie":
        "You pull out a single walkie talkie radio from the bag. After searching, you realize this is all you have to defend yourself! They didn't even give you a pair to make it useful!"
    elif your_wpn.name == "hook":
        "You pull out a sharp grappling hook tied to a rope. Climbing is not a priority; staying alive is. Maybe you can swing it around and do some damage."
    elif your_wpn.name == "screwdriver":
        "At the bottom of the bag you find a simple screwdriver. You curse as you realize this is your \"weapon.\" How are you supposed to defend yourself with this?"
    elif your_wpn.name == "potlid":
        "Inside of your bag you find ... a pot lid, and nothing else. You want to laugh, you are so distraught. Perhaps you can use it as a shield for now."
    elif your_wpn.name == "camouflage":
        "You pull out a long, ugly mess of green and brown cloth. You then realize it to be a camouflage suit ... it's not a weapon, but it would be useful to become invisible while outdoors."
    elif your_wpn.name == "uzi":
        "You pull out a large gun and recognize it from the movies to be an Uzi submachine gun. This will be deadly, but the question is, do you want it to be?"
    elif your_wpn.name == "bbgun":
        "Your heart beats when you pull out something that looks like a shotgun ... but many parts are plastic. The ammunition reveals it to be only a BB gun; designed specifically not to kill."
    elif your_wpn.name == "revolver":
        "You pull out a long, old-timey revolver. You wonder if it even works, but for now you'll have to trust that it does."
    elif your_wpn.name == "ak47":
        "You pull out a brand new AK-47 rifle. You're very glad that it isn't a banana."
    elif your_wpn.name == "slingshot":
        "You pull out a dangling string attached to a handle ... a slingshot? It doesn't come with ammunition, so you must use rocks. But how much damage can a rock really do?"
    else:
        $ sayit = your_wpn.fancy_name
        "You pull out a %(sayit)s."
    return

######################################
###################################### EVENTS #
######################################
init:
    #Framework events (editable in script.rpy)
    $ event("time_limit_fail", "day > time_limit", event.only(), event.once(), priority=1) #death by time limit
    $ event("forbidden_zone_fail", "loc.forbidden", event.only(), event.once(), priority=1) #death by forbidden zone
    $ event("won_game", "players_alive == 1", event.only(), event.once(), priority=1) #you win the game
    
    #Campaign events
    $ event("kenji_attacks_you", "Kenji in party and not freeplay", event.once(), priority=100)
    $ event("shrine_find", "loc == f1 and finding_mari and not freeplay", event.only(), event.once(), priority=100)
    $ event("mari_find", "loc == rm_shrine and not Mari.met and not mari_will_die and not freeplay", event.only(), event.once(), priority=100)
    $ event("mari_find_dead", "loc == rm_shrine and mari_will_die and not freeplay", event.once(), priority=50)
    $ event("meet_jun", "Jun.loc == Asai.loc and not Jun.met and not Asai.met and loc == Asai.loc and not freeplay", event.once(), priority=25)
    $ event("cave_jun_ext", "loc == f3 and Jun.loc == rm_cave and not freeplay", event.once(), priority=100)
    $ event("cave_jun", "loc == rm_cave and Jun.loc == rm_cave and not Jun_recruited and not freeplay", event.only(),priority=100)
    $ event("tetsuo_asai", "loc == e2 and Asai.loc == e2 and Tetsuo.loc == e2 and Asai.alive and Tetsuo.alive and not freeplay", event.only(), event.once(), priority=25)
    $ event("bathhouse_ai", "loc == a1 and bath_save_mari and not freeplay or loc == a1 and Ai.alive and Ai.loc == rm_showers and not freeplay", event.only(), event.once(), priority=1)
    $ event("bath_no_ai", "loc == rm_bathhouse and not Nanako.met and not bath_save_mari and not freeplay", event.only(), event.once(), priority=50)
    $ event("school_emi_intro", "loc == rm_corridor and Emi.alive and not freeplay", event.only(), event.once(), priority=50)
    $ event("ikoma_emi", "loc == Ikoma.loc and loc == Emi.loc and Ikoma.alive and Emi.alive and not freeplay", event.only(), event.once(), priority=50)
    $ event("Kenji_talk", "loc == Kenji.loc and Kenji.alive and you in Kenji.enemies and not freeplay", event.only(), event.once(), priority=50)
    
    $ event("bathhouse_nanako_yuki", "Nanako.loc == loc and Yuki.loc == loc and not freeplay", event.only(), event.once(), priority=50)
    $ event("yuki_waiting", "loc == Yuki.loc and Yuki.alive and yuki_lied and not freeplay", event.only(), event.once(), priority=50)
    
    $ event("gps_hospital", "gps_story and loc == g3 and Takeshi.alive and not freeplay", event.only(), event.once(), priority=50)
    $ event("boat_missing", "loc == rm_shed and takeshi_boat_truth and seen_boat and not freeplay", event.only(), event.once(), priority=50)
    $ event("takkeifum_boat_death", "boat_missing and loc.zone.shore and not loc.forbidden and not freeplay", event.only(), event.once(), priority=50)
    $ event("takeshi_boat_lie", "loc == rm_shed and takeshi_boat_lied and seen_boat and not freeplay", event.only(), event.once(), priority=100)
    $ event("ai_revenge_kill", "Ai.alive and dealt_ai == \"tied\"", event.once(), priority=100)
    
    
    # $ event("", "loc == ", event.only(), event.once(), priority=50)
    

    #Variables
    $ freeplay = False
    $ this_is_a_new_loc = False
    $ finding_mari = False
    $ saw_mari_dead = False
    $ kenji_murdered = False
    $ lied_to_mari = False
    $ mari_is_waiting = False
    $ jun_is_waiting = False
    $ mari_will_die = False
    $ dealt_ai = ""
    $ murdered = None
    $ mari_here = False
    $ jun_here = False
    $ mari_hates_you = False
    $ jun_hates_you = False
    $ did_not_intervene_jun = False
    $ you_can_cross_bridge = False
    $ bath_save_mari = False
    $ hitomo_dead= False
    $ moving_boat = False
    $ answered_yuki = False
    $ mari_knows_yuki_lie = False
    $ mari_knows_emi_kill = False
    $ seen_boat = False
    $ ask_takeshi = False
    $ takeshi_gps = False
    $ takeshi_boat_lied = False
    $ takeshi_boat_truth = False
    $ gps_story = False
    $ boat_coast_loc = None
    $ boat_missing = False
    $ Jun_recruited = False
    $ saved_hitomo = False
    
########################
######## EVENTS ########
########################

label kenji_attacks_you:
    
    stop music fadeout 3.0
    $ party.remove(Kenji)
    "Your forced banter dies down. Kenji appears to be struggling in matching your pace, obviously not used to outdoor activities."
    if loc == d1:
        "The trees thin and you can see the ocean as you press east. It is a very steep fall off of the cliff to the ragged rocks below."
    $ damage_you(-20)
    $ show_blood()
    stop music
    play music "music/AngryOpheliasSong.ogg" fadein 3.0
    "Suddenly, you feel a sharp pain in your lower leg."
    
    "You look and see a silver knife sticking out of the back of your leg!"
    $ reference_item(Kenji.wpn)
    show Kenji scared with dissolve
    "You immediately look at Kenji and see him holding other knives!"
    y scared "Kenji!?"
    if (Mari in party or Mari.loc == loc):
        mari yell "No! How could you!?"
    "He's playing the game! He lied all along! He ... was probably going to kill Mari if he found her!"
    play sound "sfx/backstab.ogg"
    "You rip out the knife and flail it away. Your wound is incredibly painful and already bleeding profusely. But you have no choice now."
    ken "I'm not going to lose, man ... I ain't gonna die on this damn island!"
    $ Kenji.type = "normal"
    $ Kenji.met = True
    $ Kenji.make_foe(you)
    $ battle_start(Kenji,0,"Kenji lunges for you with his knives aimed to kill!", "kenji_attacked_you", False)
    
    return

label you_attacked_kenji:
    $ kenji_murdered = True
    "Kenji's lifeless body slumps to the ground. You just stare at it and the blood."
    "You killed him. You are really playing the game."
    play sound "sfx/static_loop.ogg" channel 1 fadein 1.0
    "The walkie talkie in your hand crackles and you look down at it. Does it actually work? And more importantly, could you reach someone else with it?"
    if Mari not in party and Mari.alive and you not in Mari.enemies:
        call mari_radio
        stop sound channel 1
        "You put away the radio, sure you've heard enough. You're not sure you can even trust her."
    else:
        stop sound channel 1
        if (Mari in party or Mari.loc == loc):
            mari "I have the other one."
            y none "Oh. Good."
        "You put the radio away, doubting that it's of any use now."
    jump grid_loc
    
    
label kenji_attacked_you:
    if (Jun in party or Jun.loc == loc):
        jun mad "I knew we couldn't trust this bastard!"
    elif (Mari in party or Mari.loc == loc):
        "Mari wipes tears from her eyes."
        mari sad "He was such a sweet guy in school ..."
    else:
        "Kenji had completely transformed. He was nothing like you knew him in school."
    "How many more classmates were ready to play this sick game? How many were going to try to murder you?"
    if Mari not in party and Mari.alive and you not in Mari.enemies:
        play sound "sfx/static_loop.ogg" channel 1 fadein 1.0 loop
        "You stand in silence for a long time, but the walkie talkie crackles and you are reminded of Mari."
        "Is what Kenji said true? Did he really talk to her? Was she really to the east?"
        call mari_radio
        y none "I'm coming for you! Stay where you are!"
        stop sound channel 1
        "Kenji said she was to the east ... If you don't reach her, someone else might. Someone playing the game."
    jump grid_loc
    
label mari_radio:
    play sound "sfx/walkietalkie.ogg"
    "You press the talk button on the radio."
    y sad "Hello? Um ... anyone there?"
    "There's a long silence, and then suddenly the radio crackles to life again."
    play sound "sfx/walkietalkie.ogg"
    who "K-K-Kenji? Is that you?"
    "That's definitely Mari's voice."
    "You don't want to scare her by telling her how you got the walkie talkie, so you pretend you are him."
    play sound "sfx/walkietalkie.ogg"
    y none "Where are you?"
    play sound "sfx/walkietalkie.ogg"
    mari "Like I said I'm in ... I'm in a shrine or something. I'm scared, please ... please come soon!"
    $ finding_mari = True
    return
    
label shrine_find:
    "You stumble upon an old, but beautiful hut. This must be the shrine, and where you will find Mari."
    return
    

    
    
##########################
## CHAR INTRODUCTIONS ##
##########################
init:
    $ event("find_mari", "Mari.loc == loc and Mari.alive and not Mari.met and not Mari.hidden and not freeplay", event.once(), priority=75)
    $ event("find_jun", "Jun.loc == loc and Jun.alive and not Jun.met and not Jun.hidden and not freeplay", event.once(), priority=75)
    $ event("find_emi", "Emi.loc == loc and Emi.alive and not Emi.met and not Emi.hidden and not freeplay", event.once(), priority=75)
    $ event("find_goro", "Goro.loc == loc and Goro.alive and not Goro.met and not Goro.hidden and not freeplay", event.once(), priority=75)
    $ event("find_tetsuo", "Tetsuo.loc == loc and Tetsuo.alive and not Tetsuo.met and not Tetsuo.hidden and not freeplay", event.once(), priority=75)
    $ event("find_fumie", "Fumie.loc == loc and Fumie.alive and not Fumie.met and not Fumie.hidden and not freeplay", event.once(), priority=75)
    $ event("find_kei", "Kei.loc == loc and Kei.alive and not Kei.met and not Kei.hidden and not freeplay", event.once(), priority=75)
    $ event("find_takeshi", "Takeshi.loc == loc and Takeshi.alive and not Takeshi.met and not Takeshi.hidden and not freeplay", event.once(), priority=75)
    $ event("find_yuki", "Yuki.loc == loc and Yuki.alive and not Yuki.met and not Yuki.hidden and not freeplay", event.once(), priority=75)
    $ event("find_nanako", "Nanako.loc == loc and Nanako.alive and not Nanako.met and not Nanako.hidden and not freeplay", event.once(), priority=75)
    $ event("find_kenji", "Kenji.loc == loc and Kenji.alive and not Kenji.met and not Kenji.hidden and Kenji not in party and not freeplay", event.once(), priority=75)
    $ event("find_lucy", "Lucy.loc == loc and Lucy.alive and not Lucy.met and not Lucy.hidden and not freeplay", event.once(), priority=75)
    $ event("find_ikoma", "Ikoma.loc == loc and Ikoma.alive and not Ikoma.met and not Ikoma.hidden", event.once(), priority=75)
    $ event("ikoma_scene", "Ikoma.loc == loc and Ikoma.alive and Ikoma.met and not Ikoma.hidden", event.only(), priority=75)
    $ event("find_ai", "Ai.loc == loc and Ai.alive and not Ai.met and not Ai.hidden and not freeplay", event.once(), priority=75)
    $ event("find_hitomo", "Hitomo.loc == loc and Hitomo.alive and not Hitomo.met and not freeplay", event.once(), priority=75)
    $ event("Hitomo_talk", "Hitomo.loc == loc and Hitomo.alive and Hitomo.met and not Hitomo.hidden and not freeplay", event.once(), priority=75)
    $ event("find_asai", "Asai.loc == loc and Asai.alive and not Asai.met and not Asai.hidden and not freeplay", event.once(), priority=75)
    $ event("find_yoriko", "Yoriko.loc == loc and Yoriko.alive and not Yoriko.met and Yoriko.hidden and not freeplay", event.once(), priority=75)
    $ event("yoriko_arrows", "Yoriko.loc == loc and Yoriko.alive and Yoriko.hidden and Yoriko.met and not freeplay", event.only(), priority=80)     
    $people_to_show = []
    $ event("deathmatch_handler", "freeplay and len(loc.pop) > 0", event.solo(), priority=15)
label deathmatch_handler:
    $cutscene()
    python:
        print "loc.pop",loc.pop      
        if freeplay and not story_mode:
            student_attack = False
            student_flees = False
            if len(loc.pop) > 0:
                for i in loc.pop:
                    if i.alive:
                        student_attacker = i
                        if i.type == "hostile":
                            student_attack = True
                        elif i.type == "normal":
                            num = renpy.random.randint(0,100)
                            if num > 50:
                                student_attack = True
                        else:
                            student_flees = True
                if student_attack:
                    battle_start(student_attacker,0,"%s sees you and attacks!"%(student_attacker.name),"grid_loc", True)
                elif student_flees:
                    student_attacker.move("rand")
                    renpy.say(None,"%s sees you and flees %s!"%(student_attacker.name,escape_plan))
                    find_all_pop()
                    renpy.jump("grid_loc")
    
    
label say_people_here:
    #Is someone here?
    $ show_people_here = True
    python:
        people_here = []
        people_to_show = []
        # print "people here:"
        for i in loc.pop:
            if i.loc == loc and i.alive:
                people_here.append(i)
                if not i.hidden:
                    people_to_show.append(i)


        #Show them! Up to 7 people in one screen.
        if show_drop_stuff:
            if len(people_to_show) == 1:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=center_pos,clicked=ui.jumps(people_to_show[0].name+"_talk"), focus_mask=True)
            elif len(people_to_show) == 2:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=left_pos,clicked=ui.jumps(people_to_show[0].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=right_pos,clicked=ui.jumps(people_to_show[1].name+"_talk"), focus_mask=True)
            elif len(people_to_show) == 3:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos,clicked=ui.jumps(people_to_show[0].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=center_pos,clicked=ui.jumps(people_to_show[1].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[2].name),im.MatrixColor("char/"+people_to_show[2].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farright_pos,clicked=ui.jumps(people_to_show[2].name+"_talk"), focus_mask=True)
            elif len(people_to_show) == 4:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos,clicked=ui.jumps(people_to_show[0].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_left_pos,clicked=ui.jumps(people_to_show[1].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[2].name),im.MatrixColor("char/"+people_to_show[2].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_right_pos,clicked=ui.jumps(people_to_show[2].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[3].name),im.MatrixColor("char/"+people_to_show[3].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farright_pos,clicked=ui.jumps(people_to_show[3].name+"_talk"), focus_mask=True)
            elif len(people_to_show) == 5:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos,clicked=ui.jumps(people_to_show[0].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_left_pos,clicked=ui.jumps(people_to_show[1].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[2].name),im.MatrixColor("char/"+people_to_show[2].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=center_pos,clicked=ui.jumps(people_to_show[2].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[3].name),im.MatrixColor("char/"+people_to_show[3].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_right_pos,clicked=ui.jumps(people_to_show[3].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[4].name),im.MatrixColor("char/"+people_to_show[4].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farright_pos,clicked=ui.jumps(people_to_show[4].name+"_talk"), focus_mask=True)
            elif len(people_to_show) == 6:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos,clicked=ui.jumps(people_to_show[0].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=left_pos,clicked=ui.jumps(people_to_show[1].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[2].name),im.MatrixColor("char/"+people_to_show[2].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_left_pos,clicked=ui.jumps(people_to_show[2].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[3].name),im.MatrixColor("char/"+people_to_show[3].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=center_pos,clicked=ui.jumps(people_to_show[3].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[4].name),im.MatrixColor("char/"+people_to_show[4].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_right_pos,clicked=ui.jumps(people_to_show[4].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[5].name),im.MatrixColor("char/"+people_to_show[5].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farright_pos,clicked=ui.jumps(people_to_show[5].name+"_talk"), focus_mask=True)
            elif len(people_to_show) == 7:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos,clicked=ui.jumps(people_to_show[0].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=left_pos,clicked=ui.jumps(people_to_show[1].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[2].name),im.MatrixColor("char/"+people_to_show[2].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_left_pos,clicked=ui.jumps(people_to_show[2].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[3].name),im.MatrixColor("char/"+people_to_show[3].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=center_pos,clicked=ui.jumps(people_to_show[3].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[4].name),im.MatrixColor("char/"+people_to_show[4].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_right_pos,clicked=ui.jumps(people_to_show[4].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[5].name),im.MatrixColor("char/"+people_to_show[5].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=right_pos,clicked=ui.jumps(people_to_show[5].name+"_talk"), focus_mask=True)
                ui.imagebutton((people_to_show[6].name),im.MatrixColor("char/"+people_to_show[6].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farright_pos,clicked=ui.jumps(people_to_show[6].name+"_talk"), focus_mask=True)
            else:
                ui.hbox(xmaximum = 800)
                for i in people_to_show:
                    ui.imagebutton((i.name),im.MatrixColor("char/"+i.name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos,clicked=ui.jumps(i.name+"_talk"), focus_mask=True)
                ui.close()
        else:
            if len(people_to_show) == 1:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=center_pos, focus_mask=True)
            elif len(people_to_show) == 2:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=left_pos, focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=right_pos, focus_mask=True)
            elif len(people_to_show) == 3:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos, focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=center_pos, focus_mask=True)
                ui.imagebutton((people_to_show[2].name),im.MatrixColor("char/"+people_to_show[2].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farright_pos, focus_mask=True)
            elif len(people_to_show) == 4:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos, focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_left_pos, focus_mask=True)
                ui.imagebutton((people_to_show[2].name),im.MatrixColor("char/"+people_to_show[2].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_right_pos, focus_mask=True)
                ui.imagebutton((people_to_show[3].name),im.MatrixColor("char/"+people_to_show[3].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farright_pos, focus_mask=True)
            elif len(people_to_show) == 5:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos, focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_left_pos, focus_mask=True)
                ui.imagebutton((people_to_show[2].name),im.MatrixColor("char/"+people_to_show[2].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=center_pos, focus_mask=True)
                ui.imagebutton((people_to_show[3].name),im.MatrixColor("char/"+people_to_show[3].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_right_pos, focus_mask=True)
                ui.imagebutton((people_to_show[4].name),im.MatrixColor("char/"+people_to_show[4].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farright_pos, focus_mask=True)
            elif len(people_to_show) == 6:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos, focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=left_pos, focus_mask=True)
                ui.imagebutton((people_to_show[2].name),im.MatrixColor("char/"+people_to_show[2].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_left_pos, focus_mask=True)
                ui.imagebutton((people_to_show[3].name),im.MatrixColor("char/"+people_to_show[3].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=center_pos, focus_mask=True)
                ui.imagebutton((people_to_show[4].name),im.MatrixColor("char/"+people_to_show[4].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_right_pos, focus_mask=True)
                ui.imagebutton((people_to_show[5].name),im.MatrixColor("char/"+people_to_show[5].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farright_pos, focus_mask=True)
            elif len(people_to_show) == 7:
                ui.imagebutton((people_to_show[0].name),im.MatrixColor("char/"+people_to_show[0].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos, focus_mask=True)
                ui.imagebutton((people_to_show[1].name),im.MatrixColor("char/"+people_to_show[1].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=left_pos, focus_mask=True)
                ui.imagebutton((people_to_show[2].name),im.MatrixColor("char/"+people_to_show[2].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_left_pos, focus_mask=True)
                ui.imagebutton((people_to_show[3].name),im.MatrixColor("char/"+people_to_show[3].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=center_pos, focus_mask=True)
                ui.imagebutton((people_to_show[4].name),im.MatrixColor("char/"+people_to_show[4].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=mid_right_pos, focus_mask=True)
                ui.imagebutton((people_to_show[5].name),im.MatrixColor("char/"+people_to_show[5].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=right_pos, focus_mask=True)
                ui.imagebutton((people_to_show[6].name),im.MatrixColor("char/"+people_to_show[6].name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farright_pos, focus_mask=True)
            else:
                ui.hbox(xmaximum = 800)
                for i in people_to_show:
                    ui.imagebutton((i.name),im.MatrixColor("char/"+i.name+".png",im.matrix.brightness(0.1)),yalign=1.0,xcenter=farleft_pos, focus_mask=True)
                ui.close()
            
    return
    
    
label find_mari:
    $ Mari.met = True
    jump mari_find
    
label find_jun:
    $ Jun.met = True
    "Jun introduction."
    return

label find_emi:
    $ Emi.met = True
    jump school_emi_ambush
    
label find_goro:
    $ Goro.met = True
    "Goro introduction."
    return
    
label find_tetsuo:
    $ cutscene()
    $ Tetsuo.met = True
    show Tetsuo with dissolve
    "You find Tetsuo, a typical over-achiever and Vice President of the student council. A little too peppy for your tastes."
    show Tetsuo happy
    tet "Hey, Shin! You lost, too?"
    y none "Not really. How are you doing out here?"
    show Tetsuo angry
    tet "Terrible! How could they stick us out here without proper first aid kits or, worse yet, indoor plumbing?"
    show Tetsuo
    tet "Don't worry, though. Yoriko and I are on the case."
    if (Mari in party or Mari.loc == loc):
        show Tetsuo happy
        tet "Mari! Lovely to see you."
        mari content "Hi."
    if (Jun in party or Jun.loc == loc):
        show Tetsuo angry
        tet "I see you have ... found some company."
        "Tetsuo looks Jun up and down with disgust."
        jun skeptical "Well screw you, too."
        show Tetsuo scared
        tet "Pardon? I ... I didn't mean to offend you."
        show Tetsuo
        tet "Let's not get all worked up. Our conditions may be bad, but we have to stick it out."
    tet "We should gather all the students and start a formal protest. What do you think?"
    if Yoriko.alive:
        $ Yoriko.move(loc)
        y none "I don't think -"
        play sound "sfx/bow_shot.ogg"
        show Tetsuo scared
        "A thwack sound interrupts you. Tetsuo's eyes go wide."
        if (Mari in party or Mari.loc == loc):
            mari scared "What's wrong!?"
        play sound "sfx/bodyfall.ogg"
        hide Tetsuo with dissolve
        $ Tetsuo.kill("murder",killer=Yoriko)
        "Tetsuo falls face-first onto the ground and reveals an arrow in his back!"
        jump yoriko_arrow_attack
    else:
        y none "That ... doesn't sound like it will work, honestly."
        tet "We have to try!"
        "You start to walk away. You're not sure you can help someone so delusional."
    jump grid_loc

    
label find_fumie:
    $ cutscene()
    $ Fumie.met = True
    if Kei.alive:
        show Fumie with dissolve
        "Fumie is here. She looks unusually happy, considering the situation."
        fum "Hey, Shin!"
        if (Jun in party or Jun.loc == loc):
            jun lookaway "She's freaking me out."
        y sad "Uh, hi. You're not ... dangerous, are you?"
        fum "No, silly. I'm just happy because I know a secret."
        y none "What secret?"
        fum "I can't tell you. Duh."
        fum "Kei can tell you, though. Go talk to him."
        if not Kei.met:
            "Ugh ... Kei."
            "At least you know he's alive."
        else:
            y none "I already did."
            show Fumie sad
            fum "Hmm ... Then maybe I can't tell you after all."
            y none "You're talking about his \"secret pact\"?"
            show Fumie happy
            fum "Oh!! Yes! So you're included then?"
            y none "I guess, but ... whatever."
            "This wasn't worth discussing."
    else:
        show Fumie scared with dissolve
        "Fumie is here. She looks devastated."
        y none "What's wrong with you?"
        "She flips out, startled that you're there."
        fum "Sh ... Shin!?"
        y sad "I won't hurt you."
        fum "He's dead ... He's dead!"
        y none "Who is?"
        fum "Kei!!"
        if Kei.met:
            y scared "What, how!?"
            fum "I don't know! I wasn't there!"
        else:
            "You knew she was close to him."
            
        "Fumie sobs openly."
        if (Mari in party or Mari.loc == loc):
            "Mari tries to console her, but Fumie pushes her away."
        "It looks like Fumie will be inconsolable."
    jump grid_loc
    
label find_kei:
    $ Kei.met = True
    jump kei_intro
    
label find_takeshi:
    jump takeshi_intro
    
label find_nanako:
    $ Nanako.met = True
    "Nanako is here. She was the undisputed queen of the classroom and envy of all the school girls."
    return
    
label find_kenji:
    $ cutscene()
    $ Kenji.met = True
    show Kenji with dissolve
    "It's Kenji again ..."
    "He sees you, so you can't avoid him."
    y none "Hey."
    show Kenji scared
    ken "Oh!"
    if (Jun in party or Jun.loc == loc):
        jun skeptical "I dunno about this guy ..."
    jump Kenji_encounter
    
label find_lucy:
    $ cutscene()
    $ Lucy.met = True
    show Lucy with dissolve
    "It's Lucy. She's that half-American girl who's always squealing and giggling with Nanako and Hitomo."
    show Lucy sad
    lucy "Um ... Shinobu?"
    y none "It's all right. I won't hurt you."
    show Lucy
    lucy "Oh good!"
    return
    
init python:
    def runaway():
        global sanity
        global loc
        if loc.type == "room":
            rand_exit = loc.parent
        else:
            rand_exit = renpy.random.choice(loc.exits)
            if rand_exit.forbidden and sanity >= 50:
                for i in loc.exits:
                    if not i.forbidden:
                        rand_exit = i
                        return rand_exit
        return rand_exit
        
    gui_is_off = False
    def cutscene(togglegui=False):
        global gui_is_off
        global show_drop_stuff
        global movement_keys
        movement_keys = False
        #global on_cutscene
        show_drop_stuff = False
        #on_cutscene = True
        if togglegui:
            gui_is_off = True
            config.skipping = False
            renpy.hide_screen("health")
            renpy.hide_screen("beep_red_continuous")
            renpy.hide_screen("beep_yellow_continuous")
        
    def uncutscene():
        global gui_is_off
        global show_drop_stuff
        global movement_keys
        movement_keys = True
        #global on_cutscene
        show_drop_stuff = True
        #on_cutscene = False
        renpy.music.stop(fadeout=3.0)
        if gui_is_off:
            renpy.hide_screen("health")
            renpy.hide_screen("beep_red_continuous")
            renpy.hide_screen("beep_yellow_continuous")
                    
## IKOMA
label find_ikoma:
    $ cutscene()
    $ Ikoma.met = True
    $ Ikoma.type = "hostile"
    "You see a boy walking swiftly but calmly in your direction."
    y none "Who ...?"
    show Ikoma clean with dissolve
    "As he gets closer, you recognize it is ... Hmm. You think his name was Ikoma."
    "He was always obnoxious, but he was also horribly bullied ... You remember how you turned your head away every time and now you are swamped with shame."
    play music "music/AngryOpheliasSong.ogg"
    show Ikoma with dissolve
    "You quickly realize, however, that Ikoma has not forgotten those times. He has not forgotten anything and he wants revenge."
    if Mari in party or Mari.loc == loc:
        mari scared "Ikoma? Ikoma!?"
    if Jun in party or Jun.loc == loc:
        jun "Who's that?"
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        y scared "Run!!"
    $ Ikoma.wpn.get_sfx()
    $ reference_item(Ikoma.wpn)
    "Ikoma grins with intent! He slips off a deadly automatic gun from his back!"
    menu:
        "[[Attack]":
            $ battle_start(Ikoma,2,"Ikoma welcomes you.", "killed_ikoma", False)
        "Flee":
            "You move as fast as your legs can take you."
            $ loc = runaway()
            $ move_to_grid(loc)
            stop music fadeout 4.0
            scene black with dissolve
            "That was close."
    jump grid_loc
    
label ikoma_emi:
    $ Ikoma.met = True
    $ Ikoma.type = "hostile"
    $ Emi.met = True
    $ cutscene()
    show Ikoma at left
    show Emi at right
    with dissolve
    "Ikoma and Emi are here together."
    if not Emi.met:
        "Emi was a quiet bookworm that you barely knew. You studied together once."
    if Ikoma.met:
        y scared "Emi! Look out!!"
        show Emi scared
        "Emi looks at you with confusion."
    else:
        "Ikoma was always obnoxious, but he was also horribly bullied ... You remember how you turned your head away every time and now you are swamped with shame."
    $ reference_item(Ikoma.wpn)
    $ Ikoma.wpn.get_sfx()
    show Emi scared
    "Ikoma points his gun at you."
    y scared "Run, Emi! Run!"
    show Emi angry
    "Emi pushes Ikoma's gun away."
    emi "What are you doing!?"
    show Ikoma coy
    iko "Killing them."
    emi "Why!?"
    iko "I'm going to go home."
    show Emi scared
    emi "But ..."
    show Ikoma
    iko "I wanted to be nice and save you for last, but oh well."
    $ Ikoma.wpn.use_sfx()
    $ Emi.kill("murder",killer=Ikoma)
    $ show_blood()
    hide Emi with dissolve
    "Ikoma shoots Emi point blank."
    
    $ battle_start(Ikoma,0,"Then he shoots you.", "killed_ikoma", False)

label find_ai:
    $ cutscene()
    $ Ai.met = True
    show Ai with dissolve
    "The loud-mouthed sports girl of the class is standing ahead of you."
    show Ai evil
    "She spots you and she smiles."
    $ reference_item(Ai.wpn)
    play music "music/AngryOpheliasSong.ogg"
    "She turns and reveals that she's holding a bloody chainsaw."
    if (Mari in party or Mari.loc == loc):
        mari scared "Oh my god!"
    elif (Jun in party or Jun.loc == loc):
        jun scared "Sweet baby Jesus!"
    jump ai_battle_begin
    
label find_yuki:
    $ Yuki.met = True
    jump yuki_intro
    
label find_asai:
    $ cutscene()
    $ Asai.met = True
    show Asai with dissolve
    "It's that weasly clown, Asai."
    y none "What are you doing?"
    show Asai angry
    asai "None of your business!"
    return
    
label find_yoriko:
    $ cutscene()
    $ Yoriko.met = True
    if Tetsuo.alive and Tetsuo.loc == loc:
        if not Tetsuo.met:
            jump find_tetsuo
        else:
            show Tetsuo with dissolve
            tet "You're back! Did you change your mind about that protest?"
            y none "Well, I -"
            play sound "sfx/bow_shot.ogg"
            show Tetsuo scared
            "A thwack sound interrupts you. Tetsuo's eyes go wide."
            if (Mari in party or Mari.loc == loc):
                mari scared "What's wrong!?"
            play sound "sfx/bodyfall.ogg"
            hide Tetsuo with dissolve
            $ Tetsuo.kill("murder",killer=Yoriko)
            "Tetsuo falls face-first onto the ground and reveals an arrow in his back!"
            jump yoriko_arrow_attack
    else:
        $ Yoriko.wpn.use_sfx()
        $renpy.scene()
        $renpy.show(loc_bg)
        $ renpy.transition(dissolve)
        "Something shoots right past your head. An arrow?"
        jump yoriko_arrow_attack
    

label yoriko_arrows:
    $ cutscene()
    $ Yoriko.wpn.use_sfx()
    play music "music/AngryOpheliasSong.ogg"
    $renpy.scene()
    $renpy.show(loc_bg)
    $ renpy.transition(dissolve)
    $ num = renpy.random.randint(0,100)
    if num < 60 and not wish_safety_you:
        $ show_blood()
        $ damage_you(-20)
        "An arrow grazes you! The arrow attacker is back!"
    else:
        "An arrow nearly hits you! The arrow attacker is back!"
    jump catch_yoriko
    
label catch_yoriko:
    menu:
        "Run Away":
            "You'd only get yourself killed trying to run after this person! They have too many advantages! You decide to be smart and run into the woods."
            if (Mari in party or Mari.loc == loc) and (Jun in party or Jun.loc == loc):
                "You meet up with your friends."
            elif (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
                "You meet up with your friend."
            $ rand_grid = runaway()
            $ move_to_grid(rand_grid)
        "Catch Person":
            "You charge towards where the arrows came from. You have to catch them!"
            if (Mari in party or Mari.loc == loc):
                mari scared "Shinobu! No!!"
            play sound "sfx/bow_shot.ogg"
            $ num = renpy.random.randint(0,100)
            if num < 60 and not wish_safety_you:
                $ show_blood()
                $ damage_you(-20)
                "An arrow launches from nowhere once again. This time it grazes you!"
            else:
                "You manage to gain distance without being hit!"
            menu:
                "Run Away":
                    jump abandon_arrow_chase
                "Keep Going":
                    "You need to find and stop this person! You dash forwards and catch the sight of a girl's skirt."
                    play sound "sfx/bow_shot.ogg"
                    $ num = renpy.random.randint(0,100)
                    if num < 60 and not wish_safety_you:
                        $ show_blood()
                        $ damage_you(-20)
                        "But another arrow shoots out and wounds you."
                    else:
                        "They miss you! You gain considerable ground."
                    menu:
                        "Run Away":
                            jump abandon_arrow_chase
                        "Keep Going":
                            "Now you're just mad!!"
                            "You shout incoherently and charge ahead, full speed!"
                            play sound "sfx/bow_shot.ogg"
                            $ show_blood()
                            if wish_safety_you:
                                $ damage_you(-10)
                            else:
                                $ damage_you(-20)
                            "Another arrow hits you straight in the chest. You stumble back, but the adrenaline helps you recover."
                            show Yoriko scared with dissolve
                            "Behind a tree, you find a girl trying to load another bolt into her crossbow. She gasps seeing you."
                            "You yank the bolt from your chest and growl at her."
                            y angry "Yoriko, you bitch!"
                            show Yoriko angry
                            yor "Bite me!"
                            $ Yoriko.type = "hostile"
                            $ reference_item(Yoriko.wpn)
                            $ who_has_arrows = False
                            $ battle_start(Yoriko,2,"She picks up her freshly loaded crossbow.", "you_caught_yoriko", False)
        "Shoot Back" if (wpn.type == "gun" or wpn.wpn_range == "ranged"):
            $ Yoriko.health -= renpy.random.randint(10, wpn.wpn_rating*4)
            if ammo_mode:
                $wpn.use()
            else:
                $ wpn.use_sfx()
            if wpn.type == "gun":
                "You take out your gun and spray bullets into the trees where the arrows came from."
            else:
                "You use your weapon to shoot into the trees where the arrows came from."
            if Yoriko.health <= 0:
                $ Yoriko.death_sfx()
                $ renpy.music.stop(fadeout=2.0)
                $ renpy.sound.play("sfx/bodyfall.ogg",channel=1)
                $ Yoriko.kill("murder",you)
                jump you_caught_yoriko
            else:
                "You hear running. You must have scared them!"
                "You sprint towards the area in hopes of catching them. Instead, you only see the glimpse of a girl's skirt before she disappears entirely. You failed to catch her."
                stop music fadeout 3.0
                if (Mari in party or Mari.loc == loc) and (Jun in party or Jun.loc == loc):
                    "You go back and tell your friends that you've scared off the person."
                elif (Mari in party or Mari.loc == loc):
                    "You go back and find Mari. She's relieved to see you and gives you a hug. And then scolds you for running off in the first place."
                elif (Jun in party or Jun.loc == loc):
                    "You go back and tell Jun what you saw."
                $ Yoriko.met = True
                $ Yoriko.type = "hostile"
                $ Yoriko.loc = runaway()
                jump grid_loc
    jump abandon_arrow_chase
        
########################
## LOC INTRODUCTIONS ##
########################

init:
    $ event("a1_first", "loc == a1 and not freeplay", event.once(), priority=10) #bathouse
    $ event("a2_first", "loc == a2 and not freeplay", event.once(), priority=10) #bridge
    $ event("a3_first", "loc == a3 and not freeplay", event.once(), priority=10) #train station
    $ event("b1_first", "loc == b1 and not freeplay", event.once(), priority=10) #graveyard
    $ event("b3_first", "loc == b3 and not freeplay", event.once(), priority=10) #farm
    $ event("shed_first", "loc == rm_shed and not freeplay", event.once(), priority=10) #shed
    $ event("b4_first", "loc == b4 and not freeplay", event.once(), priority=10) #school
    $ event("c1_first", "loc == c1 and not freeplay", event.once(), priority=10) #shack
    $ event("c3_first", "loc == c3 and not freeplay", event.once(), priority=10) #city hall
    $ event("c4_first", "loc == c4 and not freeplay", event.once(), priority=10) #pier
    $ event("d2_first", "loc == d2 and not freeplay", event.once(), priority=10) #waterfall
    $ event("waterfall_discover", "loc == d2 and (Jun in party or Jun.loc == loc) and not freeplay", event.once(), priority=125)
    $ event("d3_first", "loc == d3 and not freeplay", event.once(), priority=10) #old houses 1
    $ event("d4_first", "loc == d4 and not freeplay", event.once(), priority=10) #ruins
    $ event("e3_first", "loc == e3 and not freeplay", event.once(), priority=10) #cabin
    $ event("e4_first", "loc == e4 and not freeplay", event.once(), priority=10) #lighthouse
    $ event("f1_first", "loc == f1 and not finding_mari and not freeplay", event.once(), priority=10) #shrine
    $ event("f2_first", "loc == f2 and not freeplay", event.once(), priority=10) #graveyard
    $ event("f3_first", "loc == f3 and not freeplay", event.once(), priority=10) #cave
    $ event("f4_first", "loc == f4 and not freeplay", event.once(), priority=10) #old houses 2
    $ event("g1_first", "loc == g1 and not freeplay", event.once(), priority=10) #tree
    $ event("g3_first", "loc == g3 and not freeplay", event.once(), priority=10) #hospital
    $ event("g4_first", "loc == g4 and not freeplay", event.once(), priority=10) #little shrine
    
label a1_first:
    $ cutscene()
    "A huge building stands before you. It looks like a communal bathhouse."
    return
    
label a2_first:
    $ cutscene()
    "You stumble across a long, dangerous-looking bridge. The chasm below it is too deep to find another way to cross."
    if Hitomo.loc == a2 and Hitomo.alive:
        show Hitomo with dissolve
        "Hitomo, a timid girl you know from class, seems to be standing guard in front of it ..."
    else:
        "You're sure you could cross the bridge safely, however."
    return
    
label a3_first:
    $ cutscene()
    "You find a building after following some train tracks, which must be a train station. There are no trains to be found, however, and the tracks break up and disappear shortly."
    return
    
label b1_first:
    $ cutscene()
    "There is a simple cemetery here."
    return
    
label b3_first:
    $ cutscene()
    "Various fields and shacks litter the landscape. This island must have once relied heavily on farming."
    "There is a promising looking shack in one of the fields. It may be a small storage shed of some sort."
    return
    
label trap_fight:
    $ cutscene()
    play music "music/FeelingDark_loop.ogg"
    $ trapped_n = trap_caught_person.name
    $ trap_set = False
    "The bear trap has caught someone!!"
    $ renpy.show(trap_caught_person.death_sprite)
    "%(trapped_n)s writhes in the trap and cannot escape. You approach."
    $ trap_caught_person.health -= 30 #Wounded

    # Special trap interactions
    if trap_caught_person == Ikoma:
        "The monster notices you."
        show Ikoma
        "He pries the trap off and gives you a wry smile."
        $ battle_start(trap_caught_person,0,"%(trapped_n)s cackles like a maniac and charges at you!", "killed_ikoma", True)
    elif trap_caught_person == Ai:
        ai "Okita."
        show Ai angry
        ai "You're not playing fair."
        show Ai evil
        "She pries the trap from her bloodied leg and cackles deliriously!"
        $ battle_start(trap_caught_person,0,"%(trapped_n)s charges at you!", "murdered_ai", True)
    elif trap_caught_person.type == "coward":
        $ renpy.say(trap_caught_person.call_name,"Shinobu! Help me! I'm stuck!")
    elif trap_caught_person.type == "hostile":
        $ renpy.say(trap_caught_person.call_name,"You did this? Clever.")
        $ renpy.say(trap_caught_person.call_name,"Too bad it won't save you.")
        $ battle_start(trap_caught_person,0,"%(trapped_n)s pries the trap off and attacks against all odds.", "trap_murder", True)
    elif you in trap_caught_person.enemies:
        $ renpy.say(trap_caught_person.call_name,"You monster!! Let me go!")
    else:
        $ renpy.say(trap_caught_person.call_name,"I'm hurt! Help me, please! Get it off me!")
    menu:
        "Kill %(trapped_n)s":
            $ wpn.use_sfx()
            $ show_blood()
            if wpn.wpn_range == "ranged" or wpn.wpn_range == "both":
                $ trap_caught_person.kill("murder",you)
                $ renpy.hide(trap_caught_person.death_sprite)
                "You easily kill %(trapped_n)s from afar."
            else:
                
                $ trap_caught_person.health -= 20
                $ battle_start(trap_caught_person,1,"You get close and get a good hit in before %(trapped_n)s starts to fight back.", "trap_murder", True)
        "Let %(trapped_n)s go":
            "Your conscience gets a hold of you and you can't go through with anything."
            $ trap.use_sfx()
            "You help %(trapped_n)s get the bear trap off."
            $ renpy.say(trap_caught_person.call_name,"Thank you ... for a moment there, I thought you were going to kill me.")
            y none "Well, I -"
            $ renpy.hide(trap_caught_person.death_sprite)
            "%(trapped_n)s runs off, obviously still afraid of you."
            $ Yuki.loc = runaway()
    $ trap_caught_person = None
    jump grid_loc
    
label trap_murder:
    $ cutscene()
    $ trap_caught_person = None
    "The trap worked to your advantage."
    if sanity <= 40:
        menu:
            "Harvest meat":
                "You stare at the corpse before you."
                "Your stomach is growling, as it has been for a long while."
                "The body is still warm and ... inviting."
                "You shouldn't waste perfectly meat. Not when your survival is on the line."
                $ meat.add()
                "You carve what you can from the fresh kill and you are so numb that you feel no remorse. No guilt. This is perfectly natural."
            "Leave body alone":
                pass
    "You roll the corpse face-down so you don't have to look at it."
    if sanity > 40:
        "You feel as though you might throw up."
    jump grid_loc
    
label shed_first:
    $ cutscene()
    $ seen_boat = True
    $ boat_repair = 0
    "Inside of the shed is nothing but empty crates and dust. You do uncover a bear trap, but you've never used one before."
    $ reference_item(boat)
    "You push some boxes out of the way to reveal a small boat. It looks ancient, and perhaps not even sea-worthy, but the very sight of it sends tremendous hope through you."
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        y none "Do you have any idea what this means?"
    if (Mari in party or Mari.loc == loc):
        "Mari suddenly hugs you."
        mari content "I knew it ... I knew it!"
    if (Jun in party or Jun.loc == loc):
        jun surprised "Crap me a sandwich - that's really a goddamned boat!"
        jun happy "We can get off this island now!"
    "You might actually be able to escape this wretched game. This is unbelievable."
    "You pull at the boat to move it and find that it has major holes in it. Three, to be exact."
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        y none "We need to find some way to patch these. We'll have to look for extra wood on the island."
        if (Jun in party or Jun.loc == loc):
            jun "We should keep the thing here until we need it. Hide it again so no one else gets the same idea."
        elif (Mari in party or Mari.loc == loc):
            mari "If we take it out ... someone else might find this and use it for themselves. We should put it back for now ..."
    else:
        "In order to get the boat repaired, you need to find perfect scraps of wood somewhere on the island."
        "You decide to keep the boat hidden in the shed so that no one else takes it."
    if Takeshi.met and Takeshi.alive:
        "You're unsure if you should tell Takeshi about the boat. On one hand, if there's a chance to get off the island, everyone should know so they stop killing each other."
        "On the other hand ... telling people about the boat may lead to more killing. No one is in their rational mind anymore."
    jump grid_loc
    
label shed_repair:
    $ cutscene()
    if wood.is_in_inventory():
        $ boat_repair += 1
        $ wood.destroy(1)
        play sound "sfx/hammer.ogg"
        scene black with dissolve
        $ add_time(1)
        scene shed with dissolve
        
        if boat_repair == 1:
            "You spend an hour attempting to patch the boat, but you manage to do it."
            "Two more holes remain."
        elif boat_repair == 2:
            "After much sweat and effort, you get the wood to work the way you need it to."
            "Just one more hole."
        else:
            "You did it! The boat is completely fixed! Well, on dry land anyway."
            if (Mari in party or Mari.loc == loc):
                mari happy "Yay! This is it! This is really it!"
            if (Jun in party or Jun.loc == loc):
                jun skeptical "This better work. I don't know if I could handle the disappointment."
                y none "Let's find out - the hard way."
            "You can now move the boat out of the shed when you are ready to use it."
            if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
                "You're sure, however, that if you come across anyone while you're moving it to the shore, they may try to kill you for it. But it's a risk you're willing to take."
            else:
                "Unfortunately, the boat is too big for just yourself to carry. You'll need at least one other person to help you move it to the shore ..."
    else:
        "You'll need wood to fix the boat, but you don't have any with you."
    return
    
label shed_boat_move:
    $ cutscene()
    if not boat.is_in_inventory():
        $ boat.add()
    if boat.is_in_inventory():
        if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
            y none "Okay, ready? We make our break now."
            if (Mari in party or Mari.loc == loc):
                if lied_to_mari:
                    mari "I'm ready."
                else:
                    mari content "I'll follow you anywhere."
            if (Jun in party or Jun.loc == loc):
                jun "Let's ditch this mother. I'm done here. Really fucking done."
            if loc == rm_shed:
                "You pick up the boat with help and try to weasel it out of the shed."
            scene farm with fade
            "You walk as quietly as you can so you don't attract attention. If you don't run into any trouble, you only need to pick out where to unload the boat from here."
            $ loc = b3
            
            $ moving_boat = True
            $ move_to_grid(b3)
            jump grid_loc
        elif Mari in followers or Jun in followers:
            "The boat is too big for just you. You'll need at least one other person to help you move it."
        else:
            "It's incredibly heavy with just one person. Moving it will be extra difficult, but you have no choice now."
            $ moving_boat = True
    else:
        memo "You need to make room for the boat. Lighten your load a little and try again."
    return
    
label boat_in_water:
    $ cutscene()
    if loc == b4 or loc == c4 or loc ==d4:
        jump boat_fail
    else:
        jump boat_rowaway
    
label b4_first:
    $ cutscene()
    "A large building is in this area. Signs indicate that it is a school. It must have once taught children of all ages on the island."
    return
    
label c1_first:
    $ cutscene()
    "You're standing in front of an old shack that seems to have collapsed or been set on fire ... or both."
    return
    
label c3_first:
    $ cutscene()
    "There is a building here with a large clock in a spire. This must have been an iconic building for the islanders that once lived here. Signs indicate that it is indeed the village center."
    return
    
label c4_first:
    $ cutscene()
    "A strikingly modern pier takes up this section of the coast. It must have been built recently, perhaps whoever put you on this island in the first place ..."
    "You don't see any boats in the harbor."
    return
    
label d2_first:
    $ cutscene()
    "The sound of rushing water leads you to a waterfall. It looks beautiful, but you cannot take the time to appreciate it with so much else on your mind."
    return
    
label waterfall_discover:
    $ cutscene()
    scene waterfall
    show Jun surprised
    with dissolve
    $ found_waterfall = True
    jun "Whoa, cool."
    show Jun
    jun "We should check behind the waterfall to see if there's treasure. You know, like the movies."
    y none "It's probably just solid rock ..."
    show Jun lookaway
    jun "Aw, c'mon. Aren't you even a little interested?"
    if (Mari in party or Mari.loc == loc):
        mari happy "I'm interested! Let's find out."
    show Jun
    y none "All right ..."
    play sound "sfx/swim.ogg"
    hide Jun with dissolve
    "You jump into the lake and swim towards and dive under the beating fall."
    scene black with dissolve
    "You expect to crash into the cliff face, but you keep swimming."
    scene waterfall_cave with dissolve
    "You end up in a little alcove in the rock. That guy was right! Even though you are soaked, you found a valuable hiding place."
    "You are probably the only people to have considered looking past the waterfall, and will be relatively safe when inside."
    play sound "sfx/swim_out.ogg"
    scene waterfall 
    show Jun
    with fade
    "You swim out and tell him that."
    show Jun happy
    jun "Ah hah! Who's clever? I'm clever."
    $ rm_waterfall = room("Waterfall",d2, "waterfall_cave",None,[[wood,1]],False,1, "swim", "swim_out") #New room!
    jump grid_loc
    
    
    
label d3_first:
    $ cutscene()
    "Some very old houses are built alongside rice paddies. The fields look barren, but one of the houses looks intact."
    return
    
label d4_first:
    $ cutscene()
    "You slosh around in the wet ruins of some tall building. It looks like there was never a building here, but instead, the framework of a new building that never got finished."
    return
    
label e3_first:
    $ cutscene()
    "Several rustic cabins are lined up in a row. Most all of them are trashed and useless, but there is one of interest. You can see its contents are pristine from the window."
    return
    
label e4_first:
    $ cutscene()
    "The coast looks newly sunken, so there is no beach. You see a lighthouse on a nearby small island. You could swim to it if you wanted."
    return
    
label f1_first:
    $ cutscene()
    "A rustic, ornate building sits here. From the exterior, you guess that inside may be a shrine to Buddha."
    return
    
label f2_first:
    $ cutscene()
    "An extensive cemetery stretches through most of the area."
    return
    
label f3_first:
    $ cutscene()
    "A quick search of the rocky terrain reveals a large hole as if it were the mouth to a cave."
    return
    
label f4_first:
    $ cutscene()
    "A cluster of old houses make up this coastal neighborhood. One home seems to be in better shape than the rest."
    return
    
label g1_first:
    $ cutscene()
    "A beautiful sakura tree is in bloom and standing bravely against the wind."
    return
    
label g3_first:
    $ cutscene()
    "This modern-looking building appears to be the island hospital."
    return
    
label g4_first:
    $ cutscene()
    "You find small arrangements of religious structures and artifacts. Several hopes and prayers are written on sheets of paper, tied to a tree."
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        if (Mari in party or Mari.loc == loc):
            mari happy "A wish tree!"
            "Mari runs up to the tree and inspects the wishes already tied to it. Her smile goes away as she reads each of them."
            mari sad "We're not the first class to be stuck in this game ..."
        if (Jun in party or Jun.loc == loc):
            jun "They're all different, but they all say pretty much the same thing ..."
            jun sad "\"Give me the strength to win.\" \"I want to hug my mother one last time.\""
        if (Mari in party or Mari.loc == loc):
               mari sad "\"I wish I could live.\""
        "You share a silence."
    else:
        "You walk up to the spiritual tree and inspect the wishes tied to its limbs."
        "\"Please let Namaki and I get off this island alive.\" \"Tell my family I loved them.\" \"I wish for a gun.\""
        "These were all written by students, just like you, playing the same game." 
    return
    
label wish_tree:
    $ cutscene()
    if paper.is_in_inventory():
        $ made_wish = True
        $ paper.destroy("all")
        "You take out the paper you were carrying. You're going to see if this tree works."
        menu:
            "Wish to be absolved of sin":
                $ wish_no_sin = True
                "Your hands are stained and your thoughts impure. This is not how you want to live."
                "You pray for your sins to be erased, and hang the sentiment on one of the tree's limbs."
            "Wish for Mari's safety" if (Mari in party or Mari.loc == loc):
                $ wish_safety_mari = True
                "There is nothing you want more right now than Mari's well-being. It supersedes even your own."
                "You write down your wish in secret and hang it on the tree without her seeing."
            "Wish for Jun's safety" if (Jun in party or Jun.loc == loc):
                $ wish_safety_jun = True
                "No matter how much you want to live, you have to look out for others as well. Jun deserved peace as much as you."
                "Out of pure selflessness, you wish for Jun's well being over your own and hang the wish on the tree."
            "Wish for your safety":
                $ wish_safety_you = True
                "No matter what, you had to get out of this game alive. It would be nice if others could survive as well, but just in case ..."
                "You write your hope for survival with no shame and hang it guilt-free on the tree."
        "Only time will tell if miracles do come true."
    else:
        "You need something to write on first."
    jump grid_loc
    
############################ CHEAT CODES
    
    
init python hide:
     config.keymap['screenshot'].remove('s')
     config.keymap['screenshot'].append('K_PRINT')
    
     def cheat_overlay():
         if show_drop_stuff: #only when not in cutscene
             ui.keymap(K_F1=ui.jumps("cheat_code")) 
         else:
             ui.keymap(K_F1=None) 
         if config.developer:
             ui.keymap(K_F2=ui.jumps("start")) 
         if not config.developer:
             ui.keymap(K_F5=renpy.curried_call_in_new_context("_quick_save")) 
             ui.keymap(K_F9=renpy.curried_call_in_new_context("_quick_load"))
         if movement_keys:
            if show_north and not north_loc.forbidden or show_north and sanity <= 20:
                ui.keymap(K_w=ui.jumps("move_north"))
            elif show_north and north_loc.forbidden and sanity > 20:
                ui.keymap(K_w=ui.jumps("move_north2"))
            else:
                ui.keymap(K_d=ui.jumps("error_sound"))
            if show_west and not west_loc.forbidden or show_west and sanity <= 20:
                ui.keymap(K_a=ui.jumps("move_west"))  
            elif show_west and west_loc.forbidden and sanity > 20:
                ui.keymap(K_a=ui.jumps("move_west2"))
            else:
                ui.keymap(K_d=ui.jumps("error_sound"))
            if show_south and not south_loc.forbidden or show_south and sanity <= 20:
                ui.keymap(K_s=ui.jumps("move_south"))
            elif show_south and south_loc.forbidden and sanity > 20:
                ui.keymap(K_s=ui.jumps("move_south2"))
            else:
                ui.keymap(K_d=ui.jumps("error_sound"))
            if show_east and not east_loc.forbidden or show_east and sanity <= 20:
                ui.keymap(K_d=ui.jumps("move_east"))
            elif show_east and east_loc.forbidden and sanity > 20:
                ui.keymap(K_d=ui.jumps("move_east2"))
            else:
                ui.keymap(K_d=ui.jumps("error_sound"))
                
            if room_here is not None:      
                ui.keymap(K_e=ui.jumps("enter_room"))
            else:
                ui.keymap(K_e=ui.jumps("error_sound"))
            if loc.type == "room":
                ui.keymap(K_q=ui.jumps("exit_room"))
            else:
                ui.keymap(K_q=ui.jumps("error_sound"))
                
     config.overlay_functions.append(cheat_overlay)
     
     
# This is called in a new context when the cheat code is entered.
label cheat_code:
    $ movement_keys = False
    $ cheat = renpy.input("Enter cheat code:", length=25)
    
    $ cheat = cheat.lower()
    if cheat == "restore":
        $ add_health_sanity(100,100)
    elif cheat == "lose health":
        $ add_health(-50)
    elif cheat == "lose sanity":
        $ add_sanity(-50)
    elif cheat == "easy mode":
        if wpn is not None and wpn != fist:
            $ wpn.destroy("all")
        $ ak47.add()
        $ ak47.equip()
    elif cheat == "hard mode":
        if wpn is not None and wpn != fist:
            $ wpn.destroy("all")
        $ shoe.add()
        $ shoe.equip()
    elif cheat == "god mode":
        $ cannot_die = not cannot_die
        play sound "sfx/beep_good.ogg"
    elif cheat == "print locations":
        $ printlocs = "Locations: "
        python:
            for i in locations:
                printlocs += i.name +", "
        "%(printlocs)s"
    elif cheat == "toggle gps":
        play sound "sfx/beep_good.ogg"
        $ show_gps = not show_gps
    elif cheat == "find all":
        play sound "sfx/beep_good.ogg"
        python:
            for i in locations:
                i.found = True
    elif cheat == "met all":
        play sound "sfx/beep_good.ogg"
        python:
            for i in classmates:
                i.met = True
    elif cheat == "dev plz":
        $ config.developer = not config.developer
    elif cheat[:4] == "jump" or cheat[:6] == "revive" or cheat[:4] == "kill" or cheat[:3] == "get":
        $ cheat = cheat.split(' ', 1 )
        $ cheat_job = cheat[0]
        $ cheat_value = cheat[1]
        python:
            if cheat_job == "jump":
                for i in locations:
                    if i.name.lower()  == cheat_value:
                        renpy.sound.play("sfx/beep_good.ogg")
                        move_to_grid(i)
            elif cheat_job == "revive":
                if cheat_value == "all":
                    for i in classmates:
                        if not i.alive:
                            i.unkill(i.death_type,i.murderer)
                            renpy.sound.play("sfx/beep_good.ogg")
                else:
                    for i in classmates:
                        if i.name.lower() == cheat_value:
                            i.unkill(i.death_type,i.murderer)
                            renpy.sound.play("sfx/beep_good.ogg")
            elif cheat_job == "kill":
                if cheat_value == "all":
                    for i in classmates:
                        if i.alive and i != you:
                            i.kill("suicide")
                            renpy.sound.play("sfx/accent_wash.ogg")
                else:
                    for i in classmates:
                        #print i.name
                        if i.name.lower() == cheat_value:
                            i.kill("suicide")
                            renpy.sound.play("sfx/accent_wash.ogg")
            
            elif cheat_job == "get":
                for i in all_items:
                    if i.name.lower() == cheat_value:
                        i.add()
                    
    jump grid_loc
