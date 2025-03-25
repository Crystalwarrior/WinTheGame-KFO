######################################
###################################### TALKS #
######################################

## MARI
label Mari_talk:
    $ cutscene()
    $ talking = True
    
    call events_run_period
    if mari_hates_you or you in Mari.enemies or freeplay:
        show Mari scared
        mari "No! Please! Don't hurt me!"
        y none "Mari!?"
        mari "Don't come near me!"
        show screen health_enemy
        menu:
            "[[Attack]":
                $ battle_start(Mari,0,"You say nothing as you lunge for her.", "killed_mari", True)
            "[[Done]":
                $ Mari.move(runaway())
                hide Mari with dissolve
                "She runs away."
                jump grid_loc
    else:
        if mari_is_waiting:
            show Mari sad
            mari "You came back. I was so scared ..."
        else:
            show Mari
        $ enemy = Mari
        show screen health_enemy
        menu:
            "Change Weapon" if Mari in followers:
                show Mari
                y none "We need to change your weapon."
                mari "Oh. Okay. What should I trade it for?"
                $ wpn_replace_char = Mari
                call screen follower_wpn_replace
                $ new_wpn = _return
                if new_wpn is not False:
                    $ old_wpn = Mari.wpn
                    if old_wpn is not None:
                        $ old_wpn_name = old_wpn.fancy_name
                    $ new_wpn_name = new_wpn[0].fancy_name
                    $ Mari.wpn = new_wpn[0]
                    $ new_wpn[0].destroy(1)
                    if old_wpn is not None:
                        $ old_wpn.add()

                    if old_wpn is not None:
                        "She gives you her {color=#FFF}%(old_wpn_name)s{/color} for the {color=#FFF}%(new_wpn_name)s{/color}."
                    else:
                        "You give her the {color=#FFF}%(new_wpn_name)s{/color}."
                        
                else:
                    y none "Nevermind. Use what you have."
                    show Mari content
                    mari "I'm not even sure how to really do that ..."
            "Change Item" if Mari in followers:
                show Mari
                y none "Hold this for a moment."
                $ wpn_replace_char = Mari
                call screen follower_item_replace
                $ new_item = _return
                if new_item is not False:
                    $ old_item = Mari.item
                    if old_item is not None:
                        $ old_item_name = old_item[0].fancy_name
                        #unequip
                        if wpn is not fist and new_item[0].name == wpn.name:
                            $ wpn = fist
                        if armor is not None and new_item[0].name == armor.name:
                            $ armor = None
                    $ new_item_name = new_item[0].fancy_name
                    $ Mari.item = new_item
                    $ new_item[0].destroy("all")
                    if old_item is not None:
                        $ old_item[0].add(amt=old_item[1])
                        "You trade. She gives you her {color=#FFF}%(old_item_name)s{/color} for the {color=#FFF}%(new_item_name)s{/color}."
                    else:
                        "You give her the {color=#FFF}%(new_item_name)s{/color}."
                        
                else:
                    y none "Forget it."
                
            "Tell her to wait here" if not mari_is_waiting and Mari in followers:
                y none "You have to stay here while I go out."
                show Mari sad
                mari "You're going to leave me all alone?"
                y none "Don't worry, I'll be back for you."
                mari "Please ... hurry back."
                $ party.remove(Mari)
                $ mari_is_waiting = True
            "Follow me" if mari_is_waiting:
                y none "Okay, you can follow me again. I hope you're okay."
                show Mari content
                mari "I'm fine ... for the most part."
                $ mari_is_waiting = False
                $ party.append(Mari)
            "[[Attack]" if sanity <= 30 or lied_to_mari or Mari not in followers:
                $ wpn.get_sfx()
                show Mari scared
                if wpn == fist:
                    $ your_weapon = "your fists"
                else:
                    $ your_weapon = "your weapon"
                "You pull out %(your_weapon)s. Mari tenses since you are no doubt looking at her with eyes to kill."
                mari "S-Shin-n-nobu!?"
                $ battle_start(Mari,3,"You say nothing as you lunge for her.", "killed_mari", True)
            "[[Done]":
                $ talking = False
                hide screen health_enemy
                jump grid_loc
    jump Mari_talk
    
label killed_mari:
    if (Mari in party or Mari.loc == loc):
        $ follower_remove(Mari)
    "You can't help but feel a pang of regret looking down on Mari's corpse."
    "She was just alive ... breathing and beautiful ... and now she is not."
    if wpn == fist:
        $your_weapon = "fists"
    else:
        $your_weapon = "your weapon"
    "You clean %(your_weapon)s and put it away. This game was going to be taxing in every way possible."
    jump grid_loc
    
## JUN
label Jun_talk:
    $ cutscene()
    call events_run_period
    if jun_is_waiting and not talking:
        show Jun skeptical
        jun "Finally. I was starting to get cabin fever."
        $ talking = True
    else:
        $ talking = True
        show Jun
        if not Jun in followers:
            if jun_hates_you or freeplay:
                show Jun scared
                jun "Shit! Go away!"
                "Jun breaks for it."
                menu:
                    "Try to catch him [[Attack]":
                        $ num = renpy.random.randint(0,100)
                        if num <= 25:
                            $ battle_start(Jun,2,"But you catch him!", "killed_jun", True)
                    "Leave him alone":
                        pass
                hide Jun with dissolve
                "He manages to get away!"
                $ rand_loc = runaway()
                $ Jun.move(rand_loc)
                jump grid_loc
            else:
                jun "Leave me alone, man."
    $enemy = Jun
    show screen health_enemy
    menu:
        "Change Weapon" if Jun in followers:
            show Jun
            y none "Give me your weapon."
            show Jun skeptical
            if Jun.wpn == ladle:
                jun "About time. This only-a-spoon thing is getting ridiculous."
            else:
                jun "Get real. Oh. You mean to trade?"
            $ wpn_replace_char = Jun
            call screen follower_wpn_replace
            $ new_wpn = _return
            if new_wpn is not False:
                $ old_wpn = Jun.wpn
                if old_wpn is not None:
                    $ old_wpn_name = old_wpn.fancy_name
                $ new_wpn_name = new_wpn[0].fancy_name
                $ Jun.wpn = new_wpn[0]
                $ new_wpn[0].destroy(1)
                if old_wpn is not None:
                    $ old_wpn.add()

                if old_wpn is not None:
                    "He gives you his {color=#FFF}%(old_wpn_name)s{/color} for the {color=#FFF}%(new_wpn_name)s{/color}."
                else:
                    "You give him the {color=#FFF}%(new_wpn_name)s{/color}."
                if new_wpn[0] == ladle or new_wpn[0] == potlid or new_wpn[0] == shoe or new_wpn[0] == stick:
                    show Jun angry
                    jun "You goddamned bastard."
                    y none "I don't have anything else!"
                    "He grumbles."     
            else:
                y none "Nevermind. Use what you have."
                show Jun
                jun "Uh ... 'kay."
        "Change Item" if Jun in followers:
            show Jun
            y none "Hold this for a moment."
            $ wpn_replace_char = Jun
            call screen follower_item_replace
            $ new_item = _return
            if new_item is not False:
                $ old_item = Jun.item
                if old_item is not None:
                    $ old_item_name = old_item[0].fancy_name
                    #unequip
                    if wpn is not fist and new_item[0].name == wpn.name:
                        $ wpn = fist
                    if armor is not None and new_item[0].name == armor.name:
                        $ armor = None
                $ new_item_name = new_item[0].fancy_name
                $ Jun.item = new_item
                $ new_item[0].destroy("all")
                if old_item is not None:
                    $ old_item[0].add(amt=old_item[1])
                    "He gives you his {color=#FFF}%(old_item_name)s{/color} for the {color=#FFF}%(new_item_name)s{/color}."
                else:
                    "You give him the {color=#FFF}%(new_item_name)s{/color}."
            else:
                y none "Forget it."
        "Tell him to wait here" if not jun_is_waiting and Jun in followers:
            y none "Wait here."
            show Jun
            jun "I got your back. Take me with you."
            y none "No, I have to do something alone. Trust me, okay?"
            show Jun lookaway
            jun "Uh ... Fine. I'll hold the fort, I guess."
            $ party.remove(Jun)
            $ jun_is_waiting = True
        "Follow me" if jun_is_waiting and Jun in followers:
            y none "Okay, let's go."
            show Jun
            jun "Cool."
            $ jun_is_waiting = False
            $ party.append(Jun)
        "[[Attack]" if sanity <= 30 or Jun not in followers:
            $ wpn.get_sfx()
            if wpn != fist:
                "You pull out your weapon."
            show Jun scared
            jun "What the hell, man!?"
            y none "Shut up and die."
            show Jun mad
            if Jun in followers:
                jun "I knew this was gonna happen! Fuck you - I trusted you!"
            $ battle_start(Jun,3,"You knew he was all bark and no bite.", "killed_jun", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
    jump Jun_talk
    
label killed_jun:
    if (Jun in party or Jun.loc == loc):
        $ follower_remove(Jun)
    "Jun tries to fight the inevitable, but can't. He collapses and bleeds out."
    jump grid_loc
    
    

label Hitomo_talk:
    $ cutscene()
    show Hitomo
    if you in Hitomo.enemies:
        show Hitomo scared
        hit "Ahh!!"
        menu:
            "[[Attack]":
                $ battle_start(Hitomo,0,"Might as well.", "murdered_hitomo", True)
            "[[Done]":
                pass
    elif not freeplay:
        if you_can_cross_bridge:
            if saved_hitomo:
                hit "Thank you for saving me ... I'm sorry I freaked."
                y "It's okay."
            else:
                hit "Hi."
            $ enemy = Hitomo
            show screen health_enemy
            menu:
                "[[Attack]":
                    $ battle_start(Hitomo,0,"Might as well.", "murdered_hitomo", True)
                "[[Done]":
                    $ talking = False
                    hide screen health_enemy
                    jump grid_loc
        else:
            show Hitomo
            hit "Go away! I'm warning you!"
            y none "You're not going to let us cross, are you?"
            hit "No!!"
            $ enemy = Hitomo
            show screen health_enemy
            menu:
                "[[Attack]":
                    $ battle_start(Hitomo,0,"She brought you to this.", "murdered_hitomo", True)
                "Bribe her":
                    if cigarettes.is_in_inventory() or radio.is_in_inventory() or walkietalkie.is_in_inventory():
                        menu:
                            "Give Cigarettes" if cigarettes.is_in_inventory():
                                show Hitomo scared
                                hit "Cigarettes!? I don't smoke! Eww!"
                                "She doesn't take them."
                            "Give Radio" if radio.is_in_inventory():
                                hit "Is that ... a radio? Does it get music?"
                                y none "It might."
                                "She reaches for it, but you pull it back."
                                y none "If I give this to you, you have to let us through."
                                hit "Um ... all right ... Just ... don't tell Nana that I let you across. And don't kill her. Uh, please?"
                                show Hitomo happy
                                "You give Hitomo the radio and she lets you cross the bridge."
                                $ radio.destroy("all")
                                $ Hitomo.item = [radio,1]
                                $ you_can_cross_bridge = True
                            "Give Walkie Talkie" if walkietalkie.is_in_inventory():
                                y none "I have a two way radio here. I think you need it more than me."
                                show Hitomo happy
                                hit "Whoa! You mean I could talk to Nana with this?"
                                y none "Yes, but she has to have the other one."
                                $ walkietalkie.destroy("all")
                                $ Hitomo.item = [walkietalkie,1]
                                y none "Here, I'll give you this one. I'll go give her the other one, okay?"
                                hit "So cool ... thanks!"
                                $ you_can_cross_bridge = True
                            "[[Done]":
                                pass
                    else:
                        "You probably don't have anything she wants."
                    jump grid_loc
                "[[Done]":
                    jump grid_loc
    else:
        $ enemy = Hitomo
        show screen health_enemy
        menu:
            "[[Attack]":
                $ battle_start(Hitomo,0,"Might as well.", "murdered_hitomo", True)
            "[[Done]":
                $ talking = False
                hide screen health_enemy
                jump grid_loc
    
label murdered_hitomo:
    $ murdered = "Hitomo"
    if Nanako.loc == loc and Nanako.alive:
        show Nanako scared
        nana "Oh my god! He's a psycho! I knew it! You're fucking psycho!"
        $ Nanako.move("rand")
        "Nanako flees. She doesn't appear to have a weapon."
    if Lucy.loc == loc and Lucy.alive:
        show Lucy scared
        lucy "How could you!?"
        $ battle_start(Lucy,3,"She raises her bow for revenge.", "murdered_lucy", True)
    call murder_follower_reaction
    jump grid_loc
    
## NANAKO            
label Nanako_talk:
    $ cutscene()
    show Nanako
    if not freeplay:
        if you in Nanako.enemies:
            show Nanako angry
            "Nanako spits at your feet."
            $ battle_start(Nanako,0,"You don't care.", "murdered_nanako", True)
        elif you in Nanako.friends:
            show Nanako sad
            nana "I don't want you around here. I want to be alone."
        elif Nanako.loc == Yuki.loc:
            show Nanako happy
            nana "Isn't he cute? Yuki came all the way here to find me!"
            y none "Maybe he's lying, so he can kill you ..."
            show Nanako angry
            nana "This is why I hate you."
        elif Nanako.loc == rm_lockers:
            show Nanako angry
            nana "Why are you here? Get out!"
    $ enemy = Nanako
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Nanako,3,"Nanako glares at you and stands her ground, even though her death is inevitable.", "murdered_nanako", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
            
label murdered_nanako:
    "Her precious vest couldn't save her."
    if Lucy.loc == loc and Lucy.alive:
        show Lucy scared
        lucy "How could you!?"
        $ battle_start(Lucy,3,"She raises her bow for revenge.", "murdered_lucy", True)
    if Hitomo.loc == loc and Hitomo.alive:
        show Hitomo scared
        hit "N-n-n-nanako!? Sh-sh-sh-shinobu!?"
        $ battle_start(Hitomo,0,"She doesn't know why you attacked, but she doesn't hesitate to defend herself.", "murdered_hitomo", True)
    $ murdered = "Nanako"
    call murder_follower_reaction
    jump grid_loc
    
    
## LUCY            
label Lucy_talk:
    $ cutscene()
    show Lucy
    if you in Lucy.enemies or freeplay:
        $ battle_start(Lucy,3,"Lucy screams.", "murdered_lucy", True)
    elif Nanako.loc == Yuki.loc:
        lucy "Yuki showed up! Did you see him?"
        y none "Yep."
        lucy "Such a dreamboat ..."
    elif Nanako.loc == Lucy.loc:
        show Lucy sad
        lucy "Nana probably doesn't want you here. You should leave."
    $ enemy = Lucy
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Lucy,3,"Lucy gasps just from that look in your eye.", "murdered_lucy", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
            
label murdered_lucy:
    $ murdered = "Lucy"
    if Nanako.loc == loc and Nanako.alive:
        show Nanako scared
        nana "Oh my god! He's a psycho! I knew it! You're fucking psycho!"
        $ Nanako.move("rand")
        "Nanako flees. She doesn't appear to have a weapon."
    if Hitomo.loc == loc and Hitomo.alive:
        show Hitomo scared
        hit "N-n-n-nanako!? Sh-sh-sh-shinobu!?"
        $ battle_start(Hitomo,0,"She doesn't know why you attacked, but she doesn't hesitate to defend herself.", "murdered_hitomo", True)
    call murder_follower_reaction
    jump grid_loc
    
    
## FUMIE            
label Fumie_talk:
    $ cutscene()
    show Fumie
    if not freeplay:
        if you in Fumie.enemies:
            show Fumie angry
            fum "Kei is going to kick your ass! Kei! Kei!!"
            $ battle_start(Fumie,0,"Fumie can't be saved now.", "murdered_fumie", True)
        elif Kei.met and Kei.alive:
            fum "Welcome to the secret pact!"
            y none "Uh, thanks."
        elif not Kei.alive:
            show Fumie sad
            fum "Kei ... sweet Kei ..."
    $ enemy = Fumie
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Fumie,3,"Fumie barely has time to react.", "murdered_fumie", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
            
label murdered_fumie:
    $ murdered = "Fumie"
    call murder_follower_reaction
    jump grid_loc
    
    
## TETSUO            
label Tetsuo_talk:
    $ cutscene()
    show Tetsuo
    if you in Tetsuo.enemies:
        tet "P-p-please!"
        $ battle_start(Tetsuo,2,"He's annoying just to look at.", "murdered_tetsuo", True)
    $ enemy = Tetsuo
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Tetsuo,3,"He's annoying just to look at.", "murdered_tetsuo", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
            
label murdered_tetsuo:
    $ murdered = "Tetsuo"
    call murder_follower_reaction
    jump grid_loc
    
    
## KEI            
label Keitaro_talk:
    $ cutscene()
    show Keitaro
    if you in Kei.enemies:
        show Keitaro scared
        kei "You again!?"
        $ battle_start(Kei,0,"You never liked him anyway.", "murdered_kei", True)
    $ enemy = Kei
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Kei,3,"You never liked him anyway.", "murdered_kei", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
    jump Keitaro_talk
            
label murdered_kei:
    $ murdered = "Keitaro"
    call murder_follower_reaction
    jump grid_loc
    
    
## TAKESHI            
label Takeshi_talk:
    $ cutscene()
    show Takeshi
    if you in Takeshi.enemies:
        show Takeshi sad
        tak "Give up, won't you?"
        $ battle_start(Takeshi,0,"Let's see how tough this guy is!", "murdered_takeshi", True)
    $ enemy = Takeshi
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Takeshi,3,"Let's see how tough this guy is!", "murdered_takeshi", True)
        "About hacking" if ask_takeshi:
            call takeshi_collar_help
        "Technology" if takeshi_gps:
            call takeshi_gps_give
        "Seen Boat" if not takeshi_boat_truth and not takeshi_boat_lied:
            tak "Have you found a boat yet?"
            call takeshi_boat_chat
            hide screen health_enemy
            jump grid_loc
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
    jump Takeshi_talk
            
label murdered_takeshi:
    $ murdered = "Takeshi"
    call murder_follower_reaction
    jump grid_loc
    
    
## KENJI            
label Kenji_talk:
    $ cutscene()
    show Kenji
    if you in Kenji.enemies or freeplay:
        show Kenji scared
        y none "Kenji?"
        ken "I'm not losing! Definitely not to you!"
        # He attacked you first so Jun and Mari are not gonna like this guy
        $ Jun.make_foe(Kenji)
        $ Mari.make_foe(Kenji)
        $ battle_start(Kenji,0,"You never trusted this guy.", "murdered_kenji", True)
    $ enemy = Kenji
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Kenji,3,"You never trusted this guy.", "murdered_kenji", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
            
label murdered_kenji:
    $ murdered = "Kenji"
    call murder_follower_reaction
    jump grid_loc
    
    
## AI            
label Ai_talk:
    $ cutscene()
    show Ai
    if you in Ai.enemies or freeplay:
        show Ai smile
        $ battle_start(Ai,0,"Ai smiles at you.", "murdered_ai", True)
    $ enemy = Ai
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Ai,3,"Ai is expecting you.", "murdered_ai", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
            
label murdered_ai:
    $ murdered = "Ai"
    call murder_follower_reaction
    jump grid_loc
    
    
## YUKI            
label Yuki_talk:
    $ cutscene()
    show Yuki
    if not freeplay:
        if you in Yuki.enemies:
            show Yuki scared
            yuki "No! No, please!"
            $ battle_start(Yuki,0,"Yuki flails around.", "murdered_yuki", True)
        else:
            if not answered_yuki:
                yuki "Back again? Tell me if you see Nanako."
            elif yuki_lied:
                show Yuki sad
                yuki "I haven't seen her at all ..."
            elif Nanako.loc == Yuki.loc:
                yuki "I told Nanako everything. It doesn't matter what happens now, I'm happy."
    $ enemy = Yuki
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Yuki,3,"Yuki flails around once he realizes what you're doing.", "murdered_yuki", True)
        "Seen Nanako" if not answered_yuki:
            yuki "Have you seen Nanako?"
            menu:
                "Yes" if Nanako.met:
                    $ answered_yuki = True
                    y none "Actually, I have. She's way north in a bathhouse in A1."
                    show Yuki happy
                    yuki "Really? ... Really!?"
                    yuki "That's ... great news!"
                    "Yuki is overjoyed and takes out his datapad to look at the map."
                    if Hitomo.alive:
                        y none "Be careful when you go up there, Hitomo likes to act the bridge troll."
                        yuki "Pardon?"
                        y none "Hitomo is blocking the way, but I suppose she'd let someone like you pass ..."
                        yuki "No doubt about that. Hitomo and I are close friends."
                        y none "... Of couse you are."
                    yuki "Thank you so much."
                    "Yuki runs away with a quick wave."
                    $ Yuki.move(Nanako.loc) #Teleport him to Nanako
                    $ Yuki.type = "fixed"
        
                "Yes [[Lie]" if not Nanako.met:
                    $ answered_yuki = True
                    $ yuki_lied = True
                    y happy "Yeah, totally."
                    y none "I saw her walking around A4."
                    yuki "Thank you! Thank -"
                    show Yuki sad
                    yuki "A4? Are you sure?"
                    y none "Pretty sure. Why?"
                    yuki "Maybe ... No, it's nothing."
                    yuki "All right, bye."
                    hide Yuki with dissolve
                    "Yuki scratches his head and leaves."
                    $ Yuki.move(a4) #Teleport
                    if (Mari in party or Mari.loc == loc):
                        mari "Why did you lie to him?"
                        y none "I forgot."
                        mari "No, you didn't."
                        y none "Fine, I never liked him, okay?"
                        "Mari frowns at you, but you don't care."
                        $ mari_knows_yuki_lie = False
                "No":
                    y none "'fraid not."
                    show Yuki sad
                    yuki "Oh. That's not at all what I was hoping you'd say."
                    yuki "Well ... Thanks for not killing me. See you."
                    if Nanako.met:
                        if (Mari in party or Mari.loc == loc):
                            mari "Why did you lie to him?"
                            y none "I forgot."
                            mari "No, you didn't."
                            y angry "Fine, I never liked him, okay?"
                            "Mari frowns at you, but you don't care."
                            $ mari_knows_yuki_lie = False
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
    jump grid_loc
            
label murdered_yuki:
    $ murdered = "Yuki"
    call murder_follower_reaction
    jump grid_loc
    
    
## ASAI            
label Asai_talk:
    $ cutscene()
    show Asai
    if not freeplay:
        if you in Asai.enemies:
            show Asai angry
            asai "Screw off!"
        elif did_not_intervene_jun:
            show Asai angry
            asai "I finally got away from that jerk, no thanks to you!"
            y none "I didn't want to get involved."
            asai "Whatever!"
        else:
            asai "Hey, hey. Did you get anything good?"
            y angry "Leave me alone. I know how you work."
            show Asai angry
            asai "Whatever!"
        if (Jun in party or Jun.loc == loc):
            jun "Hey, you little shit."
            show Asai scared
            asai "Why'd you bring him!?"
            y none "Play nice. Please."
            jun "You're lucky. You hear me? You're lucky."
            show Asai angry
            asai "Pfft."
    $ enemy = Asai
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Asai,3,"Asai screeches as you advance.", "murdered_asai", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
            
label murdered_asai:
    $ murdered = "Asai"
    call murder_follower_reaction
    jump grid_loc
    
    
## YORIKO            
label Yoriko_talk:
    $ cutscene()
    show Yoriko
    if you in Yoriko.enemies or freeplay:
        show Yoriko angry
        yor "How did you find me?"
        $ battle_start(Yoriko,2,"Yoriko flips her ponytail over her shoulder as you prepare to attack.", "murdered_yoriko", True)
    $ enemy = Yoriko
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Yoriko,3,"Yoriko flips her ponytail over her shoulder as you prepare to attack.", "murdered_yoriko", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
            
label murdered_yoriko:
    $ murdered = "Yoriko"
    call murder_follower_reaction
    jump grid_loc
    
    
## EMI            
label Emi_talk:
    $ cutscene()
    show Emi
    if you in Emi.enemies or freeplay:
        $ battle_start(Emi,3,"Emi squeals but goes for her weapon.", "murdered_emi", True)
    $ enemy = Emi
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Emi,3,"Emi looks scared stiff.", "murdered_emi", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
            
label murdered_emi:
    $ murdered = "Emi"
    call murder_follower_reaction
    jump grid_loc
    
## IKOMA
label Ikoma_talk:
    $ cutscene()
    jump ikoma_scene
    
label ikoma_scene:
    $ cutscene()
    # If you run into Ikoma at any time, he will cavalierly attack you. You'll have the option to run or fight him.
    play music "music/AngryOpheliasSong.ogg"
    show Ikoma with dissolve
    "Ikoma is here!! He sees you!"
    $ enemy = Ikoma
    show screen health_enemy
    menu:
        "[[Attack]":
            if (Mari in party or Mari.loc == loc):
                mari "Shinobu, no!!"
            elif (Jun in party or Jun.loc == loc):
                jun "Are you crazy!?"
            $ battle_start(Ikoma,2,"Ikoma welcomes you.", "killed_ikoma", False)
        "Flee":
            "You run as fast as you can away from him!"
            $ Ikoma.wpn.use_sfx()
            "You hear Ikoma laugh and spray bullets in your direction."
            if not wish_safety_you:
                $ show_blood()
                $ damage_you(-20)
                "You're hit! But you still manage to get away."
            $ loc = runaway()
            scene black with dissolve
            $ move_to_grid(loc)
            jump grid_loc
            
label killed_ikoma:
    "The monster has finally been slain."
    play sound "sfx/beep_computer.ogg"
    "You pant as you look over Ikoma's corpse. A beeping sound catches you attention, but it's not like the sound your collar makes."
    "You look through Ikoma's clothing."
    $ gps.add()
    "You find a ... GPS? It's functional. You're amazed."
    if gps.is_in_inventory():
        memo "With the GPS, you can see where every player is on the island at all times."
    else:
        "Frankly, you're surprised that Ikoma hasn't killed much more people."
    jump grid_loc
    
## GORO            
label Goro_talk:
    $ cutscene()
    show Goro
    if you in Goro.enemies:
        show Goro scared
        goro "Waaah!"
    $ enemy = Goro
    show screen health_enemy
    menu:
        "[[Attack]":
            $ battle_start(Goro,3,"You attack him.", "murdered_goro", True)
        "[[Done]":
            $ talking = False
            hide screen health_enemy
            jump grid_loc
            
label murdered_goro:
    $ murdered = "Goro"
    call murder_follower_reaction
    jump grid_loc
    
label murder_follower_reaction:
    python:
        for i in classmates:
            if i.name == murdered:
                murdered_i = i

    # Check if mari/jun are here, and if they considered your attacker an enemy or not.
    $ mari_here = Mari.alive and (Mari in party or Mari.loc == loc) and murdered_i not in Mari.enemies
    $ jun_here = Jun.alive and (Jun in party or Jun.loc == loc) and murdered_i not in Jun.enemies
    # your party only has a negative reaction if they're not hostile, or they're not an enemy to them
    if murdered_i.type != "hostile" and (mari_here or jun_here):
        if wish_no_sin:
            if jun_here:
                show Jun scared with dissolve
                jun "... Shit..."
            if mari_here:
                show Mari scared with dissolve
                mari "W-Why..!?"
            y none "I... I had to."
            y none "Trust me, if I didn't do that, we'd be screwed!"
            if mari_here:
                show Mari scared with dissolve
                mari "Shinobu... I'm not so sure."
                mari "They weren't even hostile..."
            if jun_here:
                show Jun mad
                jun "You god damn... How can I even--"
                jun "Whatever, man. You've shown what you're capable of, and I'd rather be on your side."
            "It's a blessing they decided not to question you."
            "Don't push your luck."
            $ wish_no_sin = False
            $ murdered = None
            $ just_murdered_someone = False
            return
        else:
            if (mari_here and not f_flee_successful) or (jun_here and not f_flee_successful):
                "%(murdered)s never stood a chance against you."
            elif (mari_here and f_flee_successful) or (jun_here and f_flee_successful):
                "%(murdered)s had escaped, but it was clear what you were trying to do."
            if mari_here and jun_here:
                show Mari scared at farleft
                show Jun scared at farright
                with dissolve
                "Mari and Jun stare at you in horror."
            elif mari_here:
                show Mari scared with dissolve
                "Mari stares at you in horror."
            elif jun_here:
                show Jun scared with dissolve
                "Jun stares at you in horror."
            if jun_here:
                jun scared "Sweet Jesus Christ, man!!"
            if mari_here:
                mari scared "Don't hurt me!!"
                hide Mari with dissolve
                $ party_remove(Mari)
                $ follower_remove(Mari)
                $ Mari.move(rm_lockers)
                $ Mari.invisible = False
                $ Mari.type = "fixed"
                $ Mari.make_foe(you)
                # Since the girls can be in the locker room, too, they're going to jump in Mari's defense
                $ Lucy.make_foe(you)
                $ Nanako.make_foe(you)
                $ Hitomo.make_foe(you)
                $ mari_hates_you = True
                if loc == a2:
                    play sound "sfx/bridge_cross.ogg"
                    "Mari takes off running across the bridge, fleeing from you."
                else:
                    "Mari takes off running, fleeing from you. She's too fast for you and you won't be able to catch up."
            if mari_here or jun_here:
                y scared "Hold on, now! %(murdered)s was just an obstacle!"
            if jun_here:
                show Jun mad
                jun "That's what you say!? %(murdered)s was a damn person! You're sick! Just plain sick!"
                jun "I'm outta here. Stay the fuck away from me."
                $ party_remove(Jun)
                $ follower_remove(Jun)
                $ rand_loc = runaway()
                $ Jun.move(rand_loc)
                $ Jun.type = "normal"
                $ Jun.invisible = False
                $ Jun.make_foe(you)
                $ jun_hates_you = True
                hide Jun with dissolve
                "Jun swiftly backs away until he's far enough to make a run for it. You don't see which way he goes."
    # Argue in self defense to signal your followers don't like you killing people, and to inform about the fleeing mechanic
    elif not self_defense_argument and not murdered_i.alive:
        # Enemy status doesn't matter in this branch
        $ mari_here = Mari.alive and (Mari in party or Mari.loc == loc)
        $ jun_here = Jun.alive and (Jun in party or Jun.loc == loc)
        if mari_here and jun_here:
            show Mari scared at farleft
            show Jun scared at farright
            with dissolve
            "Mari and Jun stare at %(murdered)s in horror."
        elif mari_here:
            show Mari scared with dissolve
            "Mari stares at %(murdered)s in horror."
        elif jun_here:
            show Jun scared with dissolve
            "Jun stares at %(murdered)s in horror."
        if jun_here:
            jun sad "Screw this game, man."
        if mari_here:
            mari sad "Are we... bad people?"
        y scared "I-It had to be done... %(murdered)s attacked me, first."
        if jun_here:
            show Jun mad
            jun "God-- I get it, okay?!"
            jun "But fleeing was an option! I wish we just ran!"
        if mari_here:
            show Mari scared
            mari scared "We should've ran..."
        y scared "Then we'd just be hunted down! You saw how %(murdered)s was!"
        if jun_here:
            show Jun mad
            jun "... Fucking psychos."
        if mari_here:
            show Mari scared
            mari "I want to go home..."
        if jun_here:
            show Jun mad
            jun "So much for \"not playing the game\"."
        memo "In most battles, you can run to the edge of the screen to unlock the \"Flee\" option. However, some special combat encounters are unavoidable and are kill or be killed."
        $ self_defense_argument = True
    $ murdered = None
    $ just_murdered_someone = False
    return
