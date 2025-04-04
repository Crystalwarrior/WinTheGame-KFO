######################################
###################################### CAMPAIGN STORY #
######################################

label intro:
    $ cutscene()
    $ show_buttons = False
    $ show_click_person_tut = True
    $ show_room_tut = True
    stop music fadeout 6.0
    scene black with intro_dissolve
    $ renpy.sound.stop(channel=0)
    $ renpy.sound.stop(channel=1)
    play music "music/StraussBlueDanube.ogg"
    play sound "sfx/forest.ogg" fadein 5.0
    $ renpy.notify("Please wait ...")
    show bg canopy:
        alpha 0.0
        linear 5.0 alpha 1.0
    show cutscene
    $ renpy.pause(4.0, hard=True)
    play sound "sfx/main_menu_type.ogg" channel 1
    show screen aleema_title
    show cutscene
    $ renpy.pause(4.1, hard=True)
    hide screen aleema_title
    play sound "sfx/grassland.ogg"
    scene bg farm
    show cutscene
    $ renpy.pause(4.9, hard=True)
    play sound "sfx/grassland3.ogg"
    scene bg farm2
    show cutscene
    $ renpy.pause(4.7, hard=True)
    play sound "sfx/grassland2.ogg" fadein 1.0
    scene bg farm3
    show cutscene
    $ renpy.pause(3.0, hard=True)
    play sound "sfx/shotgun_shot2.ogg" channel 1
    $ renpy.pause(3.0, hard=True)
    play sound "sfx/beep_win2.ogg" channel 1
    $ renpy.pause(1.0, hard=True)
    stop sound fadeout 3.0
    scene black 
    show cutscene
    with meddissolve
    play sound "sfx/city.ogg" fadein 4.0
    scene bg city 
    show cutscene
    with intro_dissolve
    stop sound fadeout 6.0
    scene black 
    show cutscene
    with meddissolve
    play ambience "sfx/classmates.ogg" fadein 4.0
    scene bg train 
    show cutscene
    with intro_dissolve
    play sound "music/bgs_ominous.ogg" fadein 5.0 channel 4
    show girl2 at left with meddissolve
    show girl1 at right with meddissolve
    hide girl2 with meddissolve
    show girl3 at left with meddissolve
    hide girl1 with meddissolve
    show girl4 at right with meddissolve
    stop music fadeout 15.0
    hide girl3 with meddissolve
    hide girl4 with meddissolve
    stop ambience fadeout 5.0
    scene bg train night 
    show cutscene
    with intro_dissolve
    hide cutscene with meddissolve
    show smoke 
    with intro_dissolve
    play sound "sfx/static.ogg" fadein 4.0
    scene static with intro_dissolve
    $ renpy.pause(1.0, hard=True)
    show screen title_card
    $ renpy.pause(6.0, hard=True)
    stop sound fadeout 3.0
    hide screen title_card
    hide screen blood_splatter
    hide cutscene
    
label wake_up:
    $ persistent.seen_intro = True
    $ cutscene()
    $ loc = rm_shack
    #play ambience "sfx/grassland.ogg" fadein 10.0
    $ renpy.sound.queue("music/bgs_slow.ogg", channel=4, loop=False)
    show shack with intro_dissolve
    "You awake in a fallen apart shack."
    "Your heart is beating rapidly and your vision is foggy. Your limbs feel like they are too heavy to move."
    "Soon, your vision returns and you gain control over your body. You stand up and survey your surroundings."
    "Where are you? You were going on a school trip with your class, riding the train, and now ..."
    play sound "sfx/beep_on.ogg"
    "A beep sounds, startling you."
    "You look over on a broken table and see a computer pad. You pick it up."
    nvl clear
    play sound "sfx/beep2.ogg"
    dp "Good morning, {color=#00FF00}<StudentName>{/color}!"
    dp "Your class was specially selected to take part in this year's games! Aren't you lucky?"
    dp "The rules are pretty simple."
    dp "1. {color=#00FF00}There can only be one winner.{/color} If no one wins within %(time_limit)d days, then everyone loses! :("
    dp "2. {color=#00FF00}Participation is mandatory.{/color} Leaving will result in an immediate loss. A pretty necklace was fastened around your neck as a subtle reminder."
    play sound "sfx/beep_computer.ogg"
    "You immediately reach for you neck and tug at a collar around your neck. It hums and vibrates against your skin, but you cannot find a way to take it off."
    dp "3. {color=#00FF00}Stay out of the forbidden zones.{/color} Lingering in such zones will result in losing, so don't be a loser. The forbidden zones will be announced every so often, starting tomorrow, and will be marked on your map, too. You're welcome!"
    dp "Oh, and how do you win?"
    dp "By {color=#00FF00}killing off the other players{/color}, of course!\n\n;)"
    "A violent chill surges through you and you feel like you might vomit. But there is more on the screen."
    nvl clear
    dp "\n{image=icons/bag_pic.jpg}\nBut we're not cruel! We've supplied you with everything you need to survive. Hopefully. You've been given a bag with food, water, and your new favorite thing!"
    dp "The weapon inside your bag is completely {color=#00FF00}random{/color}, unfortunately. But you can always go ask another student to borrow theirs!"
    dp "Your bag isn't bottomless, so {color=#00FF00}you can only carry four things at any time{/color}! Yes, your food counts as an item. Life's just full of tough decisions, isn't it?"
    dp "By the way, you're not even guaranteed a weapon. Sometimes we make mistakes and replace your AK-47 with ... oh, I don't know ... a banana! Oops!"
    dp "But I hope they packed something extra fun for you, {color=#00FF00}<StudentName>{/color}!"
    nvl clear
    dp "I bet you're really angry right now, and trust me, that's a completely normal reaction."
    dp "Don't bother trying to seek revenge or finding a way to end the game without playing, because that's impossible."
    dp "{image=icons/warningsign.jpg}\nNo, really. I'm on your side here. You have a much better chance of surviving if you just play the game."
    dp "We'll be watching you from the heavily-armed island off the coast, and tracking your every move. Whenever we like, we can tell your necklace to explode, so you can't pull a fast one on us! Sorry! :("
    dp "Oh, and you don't have to worry about {color=#00FF00}<TeacherName>{/color}. We've taken care of {color=#00FF00}<him/her>{/color}, but {color=#00FF00}<he/she>{/color} did wish you good luck! Wasn't that sweet of {color=#00FF00}<him/her>{/color}?"
    
    nvl clear
    memo "That's about it. Simple, huh?"
    play sound "sfx/beep2.ogg"
    $ show_time = False
    show screen health
    dp "\nA word for the wise is to make sure that you {color=#00FF00}keep your mental and physical health in check{/color}, if you want to win. Resting and eating will make sure you're in great shape!"
    dp "Even though you're on a deserted island far away from anybody who can hear your scream, you don't have to live like a barbarian! The village on this island will be your home for the duration of the game and you don't have to settle for where you started!"
    dp "Okay, now that's really it. From all of us over at the island, we wish you good luck!"
    dp "I hope we get to tell your parents that {color=#00FF00}<StudentName>{/color} is the winner of the game! How cool would that trophy be?"
    dp "Anyway! Let the games begin!"
    dp ":D"
    $ show_time = True
    "You collapse on the ground and sit there, just focusing on trying to breathe. Could this be real?"
    
label gui_tutorial:
    $ tut_pickup = True
    memo "Items are important to your survival. You can find them in various locations."
    $ loc = rm_shack
    $ loc.items.append([bag,1])
    $ tut_show_pickup = True
    show tut_arrow at Position(xanchor=0.5,yanchor=0.5,ypos=0.24,xpos=0.26)
    memo "Look at this portion of your screen and you will see if any items are in here."
    memo "In order to pick up items, click on them."
    #$ tut_show_drop = True
    # show tut_arrow at Position(xanchor=0.5,yanchor=0.5,ypos=0.3,xpos=0.28)
    # memo "Once you have items, there will be another button to drop those items."
    #$ tut_show_drop = False
    while not bag.is_in_inventory():
        memo "Pick up your duffle bag."
        $ renpy.pause()
    
label gui_tutorial2:
    $ tut_show_pickup = False
    $ tut_pickup = False
    $ tut_openbag = True
    hide tut_arrow
    memo "Good. The items you have will always be displayed in the upper-right."
    memo "Now you must open your bag to see what goodies we gave you!"
    $ on_cutscene = True
    hide screen health
    show screen items
    
    memo "This is your {color=#00FF00}Items{/color} screen! You can use or equip things you've picked up here.\n\nRemember: you can only carry 4 items at a time."
    memo "Items have various ratings, 0-9. The higher the number, the better they are at what they do.\n\nThe {image=gui/weapon.png} gun symbol represents {color=#00FF00}weapon{/color} score.\nThe {image=gui/armor.png} shirt icon represents {color=#00FF00}armor{/color} score.\nThe {image=gui/heal.png} plus icon represents {color=#00FF00}healing{/color} score."
    memo "Open your duffle bag."
    call items
    
init:
    image cg stats = "bg/stats_cg2.jpg"
    image cg stats 2 = "bg/stats_cg.jpg"
    
label letsgo:
    $ cutscene()
    $ notify_y = .001
    $ tut_openbag = False
    "Your eyes find the bag that the text had described. You pull it out in front of you and unzip it with a shakey hand."
    $ food.add(amt=2)
    "You find the {color=#00FF00}water and rations{/color}, but there is not as much as you would have hoped. Eating these will likely help you recover from injuries and keep you mentally healthy."
    "The flap opens wider and you immediately see what must be your weapon ..."
    
    # SHOE START LET'S GO
    if shoe_start:
        $ your_wpn = shoe
    else:
        $ your_wpn= renpy.random.choice(starter_wpns)
    if not config.developer:
        $ renpy.block_rollback()

    $ your_wpn.add()
    call weapon_desc
    if your_wpn.wpn_rating > 0:
        $ wpn = your_wpn
    if your_wpn.defense > 0:
        $ armor = your_wpn
    $ add_sanity(-20)
    "Panic starts to set in."
    $ add_sanity(-20)
    "You start to hyperventilate."
    $ add_sanity(-20)
    "This is real. These so-called games {u}really{/u} do happen ... Classrooms full of children really are abducted and told to kill each other ..!"
    $ add_sanity(-20)
    "You're going to die!"
    "You haven't even graduated high school yet, and you're going to die! Murdered ... by a classmate! Maybe even a {u}friend{/u}! What does death feel like? What if it hurts? What if it's slow!?"
    "No!! You're not going to die! You can't think like that! Play the game or not ... but you're not going to die!"
    $ add_sanity(80)
    "It takes you a long time to regain your senses."
    "You cannot bear to look at the computer pad again, but it holds all the information that you will need to know."
    
    "You can access the {color=#00FF00}island map{/color}, which will be important when avoiding the forbidden zones. You check the map to find out where you are."
    hide screen health
    show screen map
    play sound "sfx/beep2.ogg" channel 1
    $ renpy.pause(1.0)
    play sound "sfx/beep_double.ogg"
    $ b1.forbid()
    $ g2.forbid()
    $ renpy.pause(0.1)
    $ b1.unforbid()
    $ g2.unforbid()
    $ renpy.pause(0.1)
    $ b1.forbid()
    $ g2.forbid()
    $ renpy.pause(0.1)
    $ b1.unforbid()
    $ g2.unforbid()
    $ renpy.pause(0.1)
    $ b1.forbid()
    $ g2.forbid()
    
    "There are already 2 {color=#FF0000}forbidden zones{/color} ..."
    "You figure out that {color=#00FF00}your position must be marked by the bright green square{/color}. If that's the case, then you are near a forbidden zone. You make sure to avoid it."
    play sound "sfx/beep2.ogg"
    $ c1.find()
    "It says here that you are in a shack ... Well, what's left of one."
    hide screen map
    play sound "sfx/beep1.ogg"
    show cg stats
    "And now to view the game's ... {color=#00FF00}statistics{/color}. You swallow, thumbing through the list of your classmates."
    $ Goro.kill("rules")
    show cg stats 2
    "Your breath catches in your throat when you see a giant red \"{color=#FF0000}LOST{/color}\" painted across one of their faces ... Could they really be {color=#00FF00}dead{/color}? Already?"
    "This game was serious."
    hide cg stats 2
    play sound "sfx/beep_on.ogg"
    show screen health
    $ on_cutscene = False
    $ show_buttons = True
    memo "You now have full access to the computer pad's functions, including  all game menu screens, {color=#00FF00}Quick Save{/color}, {color=#00FF00}Quick Load{/color}, and the {color=#00FF00}Map{/color}, {color=#00FF00}Items{/color} and {color=#00FF00}Stats{/color} screens. Hover your mouse at the bottom of the screen to access them."
    play sound "sfx/twig.ogg"
    queue music "music/bgs_creepy.ogg" noloop 
    "Suddenly, you hear a noise outside, and it probably wasn't an animal. A chill goes through your body."
    menu:
        "Check out the noise":
            $ loc = c1
            play ambience "sfx/forest.ogg" fadein 1.0
            scene cabin with fade
            "You cautiously step outside. You immediately see a boy making a beeline for the shack."
            show Kenji with dissolve
            $ renpy.pause(0.5)
            show Kenji scared
            $ renpy.pause(0.5)
            show Kenji happy with dissolve
            "He freezes when he sees you, and then sighs with relief."
            call Kenji_encounter
        "Hide":
            "You need to be safe, just in case someone actually is \"playing the game.\" You quietly stoop low and press yourself against the wall."
            $ add_sanity(-10, silent=True)
            play sound "sfx/door_squeak.ogg"
            "The rustling of the grass gets closer and then you hear it just outside of the front door. The door then hinges open with a heart-wrenching creak."
            "Heavy footsteps enter the room ... and a figure reveals itself."
            show Kenji with dissolve
            "A boy from your class. His back is to you."
            menu:
                "[[Attack]":
                    # If you run away from him (or he runs), he'll become a wanderer
                    $ Kenji.type = "normal"
                    $ Kenji.met = True
                    $ battle_start(Kenji,1,"You leap from the shadows and take Kenji by surprise.", "you_attacked_kenji", True)
                "Stay silent":
                    $ add_sanity(-10)
                    "You hold your breath and say nothing. You pray that he doesn't notice you and leaves."
                    $ add_sanity(-10)
                    "He turns around, scanning the shack. It almost seems like he's going to see you. Your heart leaps into your throat."
                    hide Kenji with dissolve
                    "And then he starts to leave. He didn't spot you."
                    "You wait a very long time until you're sure he's completely gone."
                    $ mari_will_die = True
                    $ loc = rm_shack
                    $ rm_shrine.items.append([walkietalkie,1])
                    $ Kenji.wpn = Kenji.item[0]
                    $ Kenji.wpn = Mari.wpn
                    $ Kenji.move(g1)
                    jump room_loc
                "Greet him":
                    y none "Kenji?"
                    show Kenji scared
                    "He spins around suddenly, fear painted on his face. And then he stands erect and smiles."
label Kenji_encounter:
    show Kenji happy
    ken "Shinobu? Is that you?"
    
    "He laughs nervously."
    ken "You scared me there for a moment."
    show Kenji
    if (Mari in party or Mari.loc == loc):
        mari sad "Kenji! Where were you!?"
        ken "Mari!? I'm so glad you're safe! I've gotten myself so lost on this stupid rock!"
        mari angry "Lost? We all have maps!"
        ken "Maps?"
    else:
        ken "What are you doing here? Do you know what's going on?"
    "Did he ... not read his computer pad? Is it possible that he didn't even get one?"
    "You say nothing for a while, just looking at him, your entire body frozen."
    ken "What's wrong? Why are you looking at me like that?"
    $ kenji_apologized = False
    $ kenji_questions = False
    # If you run away from him, he'll become a wanderer
    $ Kenji.type = "normal"
    $ Kenji.met = True
    
label Kenji_questions:
    if kenji_apologized and kenji_questions:
        jump kenji_leave
    menu:
        
        "Apologize" if not kenji_apologized:
            y sad "Sorry ... I'm on edge right now."
            show Kenji happy
            ken "{u}You're{/u} on edge? I just wandered through the damn Amazon rainforest out there - mosquitos the size of your head!"
            "You force a laugh."
            show Kenji
            $ kenji_apologized = True
            jump Kenji_questions
        "Ask him questions" if not kenji_questions:
            y none "You really don't know what happened and what's going on?"
            ken "Where is everybody else? Last I remember, we were on a train ..."
            y angry "That's really all you know ...?"
            show Kenji scared
            ken "What ...? Why?"
            $ kenji_questions = True
            jump Kenji_questions
        "Explain the situation":
            y angry "Don't you know what's happening!? Our entire class has been kidnapped and put on this island!"
            show Kenji scared
            y angry "We're supposed to kill each other!"
            "There's a long silence as Kenji processes what you just said."
            ken "... Are you going to kill me?"
            menu:
                "Yes [[Attack]":
                    play music "music/ALongDay.ogg" fadein 4.0
                    y angry "I have to ... None of us have any choice."
                    if Kenji.wpn == throwingknives:
                        play sound "sfx/knife_pull.ogg"
                        "Kenji suddenly pulls out a knife he had been holding behind his back."
                    ken "You're right!!"
                    $ battle_start(Kenji,3,"You lunge for each other with your weapons drawn.", "you_attacked_kenji", False)
                "No":
                    y sad "No, of course not. That's sick."
                    show Kenji
                    ken "Y-yeah. I knew you weren't that kind of guy."
                    show Kenji scared
                    ken "I had no idea ..."
                    jump kenji_leave
                    
    return
    
label kenji_leave:
    y none "Nevermind. We need to find everyone else."
    show Kenji
    if (Jun in party or Jun.loc == loc):
        show Kenji scared at left with move
        show Jun angry at right with dissolve
        jun "Fuck this guy."
        y none "What?"
        jun "I don't trust him! Let's dump him and quick."
        show Kenji
        ken "You're so rude! Typical street trash!"
        show Jun mad
        jun "Come here and say that to my face!"
        ken "Fine!"
        $ Kenji.wpn.get_sfx()
        $ reference_item(Kenji.wpn)
        $ battle_start(Kenji,0,"Kenji pulls out his weapon!", "kenji_attacked_you", True, allies_will_help=True)
    elif Mari not in party:
        $ reference_item(walkietalkie)
        ken "Yeah, man! That's what I thought! I found this walkie talkie radio thing and you won't even believe who I heard on it!"
        y none "... Who?"
        ken "Mari! That art chick. She was freaking out. I told her to stay put and now I'm finding her."
        if saw_mari_dead:
            "Finding Mari? But ..."
            y none "She's dead. I saw her. Who could you have possibly spoken to?"
            $ Kenji.wpn.get_sfx()
            $ reference_item(Kenji.wpn)
            $ battle_start(Kenji,0,"Kenji pulls out a weapon! He'd rather attack you than explain himself.", "kenji_attacked_you", True, allies_will_help=True)
            
        "You've never really spoken to Mari, but she was pretty and you never missed a chance to admire her."
        y none "Yes, we've got to help her."
        ken "Oh, great! Yeah. I don't know where she is. I just know she's to the east. Is that east? We should go that way."
        if wpn.seen:
            ken "Uh ... by the way ... Why do you have that thing?"
            if wpn != fist:
                "You grip your weapon from the reference."
            y none "I ... found it, too. It might be useful, you know ... against wild animals."
            ken "Ah, yeah. It's a jungle out there."
        y none "Let's go find Mari."
        ken "Right! Okay. You go ahead."
        if loc == c1:
            "You both walk through the trees to the east."
            $ loc = d1
        else:
            "You walk away together."
            if loc.type == "room":
                $ loc = loc.parent
            else:
                if loc.exit_east is not None and not loc.exit_east.forbidden:
                    $ loc = loc.exit_east
                else:
                    $ loc = runaway()
    else:
        ken "Why are you with this guy, Mari? You should have waited for me!"
        mari sad "I did ... But you never came!"
        ken "So typical of you!"
        ken "It was the same way in school! You stupid tease!"
        "Kenji was suddenly very violent and pulling out his weapon. Mari hides behind you."
        $ battle_start(Kenji,0,"You have to take him down.", "kenji_attacked_you", False, allies_will_help=True)
    $ party_add(Kenji)
    $ move_to_grid(loc)
    

### MARI IN SHRINE
label mari_find:
    $ cutscene()
    $ Mari.met = True
    play music "music/TheSigh.ogg" fadein 2.0 fadeout 2.0 noloop
    "You open the shrine's door. You hear a ruckus of someone who is startled. But you see no one immediately."
    mari scared "Who -!?"
    show Mari scared with dissolve
    if finding_mari:
        $ reference_item(Mari.wpn)
        "You look to your side and Mari is tucked underneath a table ... with a gun pointed right at you!"
        mari "Y-y-you're -!"
        if walkietalkie.is_in_inventory():
            y scared "Don't shoot! I got your message!"
            show Mari angry
            "You hold out the walkie talkie. She lowers her gun."
            mari "But ... What happened to Kenji?"
        else:
            y scared "Wait! I came here because of -!"
            show Mari angry
            $ Mari.wpn.use_sfx()
            $ show_blood()
            $ damage_you(-20)
            $ battle_start(Mari,0,"Mari suddenly shoots you.", "killed_mari", True,foe_advantage=True, allies_will_help=True)
        
        if not Kenji.alive:
            y sad "He's dead."
        else:
            y angry "He's a murderer."
        
        show Mari yell
        play sound "sfx/glock_reload.ogg"
        "She raises her gun again."
        mari "You killed him!! I see the blood on you!"
        menu:
            "Tell her the truth":
                "You throw your hands in the air to show you are not a threat."
                y scared "Please! Listen to me for one second before you shoot!"
                show Mari scared
                if not kenji_murdered or Kenji.alive:
                    y none "Kenji found me and told me about you, but as we were walking over here he ... he attacked me!"
                    if health < 60:
                        "With your wounds very evident, Mari seems to believe that you were attacked."
                    else:
                        "You slowly show her the back of your leg where Kenji had injured you."
                    y sad "I had to do it .... Because I ... I think he was coming here to kill you!"
                    show Mari angry
                    mari "He ... He was going to kill me?"
                    y sad "I'm just guessing since he tried to kill me, too."
                    if health < 60:
                        show Mari scared
                        play sound "sfx/bodyfall.ogg"
                        "Your wounds overcome you and you collapse onto the floor."
                        mari scared "Shinobu!"
                        "Mari rushes out and by your side. You're in too much pain to appreciate the fact that she remembers your name."
                        mari sad "Oh my god ... You're losing so much blood! Please ... hold on! I have a first aid kit!"
                        $ firstaid.use_sfx()
                        $ add_health_sanity(100,100)
                        $ loc.items.remove([firstaid,1])
                        "She retrieves a red box and pops it open. She delicately cleans yours wounds and bandages you."
                        show Mari angry
                        mari "I can't believe ... I can't believe Kenji would attack you."
                    else:
                        "Slowly, Mari steps out from under the table and stands cautiously in front of you."
                        mari sad "Are you going to play the game, too ...?"
                        menu:
                            "Yes [[Attack]":
                                y none "I'm so sorry, Mari."
                                "She looks as if she might cry."
                                mari "Why!?"
                                $ battle_start(Mari,0,"She aims her gun at you, but you charge with your own weapon.", "killed_mari", True)
                            "No":
                                y scared "No!! Never! We shouldn't even have to be asking that!"
                                mari "I know ... I know, I'm so sorry!"
                    show Mari sad
                    mari "I just can't believe any of this!"
                    "You reach out for her and she lets you touch her. She sniffles as if she is crying."
                    y sad "I won't let anyone hurt you."
                    "She shakes and finally you move to embrace her. She openly weeps for some time."
                    y none "We can't stay in one place too long. Someone will find us."
                    mari "B-but what are we to do? We have to play the game or they'll ..."
                    y angry "I'll never play their goddamned game. They'll have to kill me first!"
                    "Mari purses her lips and looks deep into your eyes."
                    show Mari
                    mari "Me, too."
                    "You both share a moment of conviction. You wanted to survive, but now you also want her to survive."
                    "You reach out your hand to her. She stares at it for a moment, and then takes it."
                    "Together, you're both ready to face whatever will come next."
                    memo "Mari will now travel with you, but you will still fight alone. If you die, she dies, too."
                    memo "You can talk to her, or any follower, when inside of a building. You can change what items they are carrying when you do. You can leave them to defend their location, but make sure they have a good weapon or else they will die."
                    $ party_add(Mari)
                    $ follower_add(Mari)
                    hide Mari with dissolve
                else:
                    y sad "I had to take him down."
                    mari yell "W-w-why!? You monster!!"
                    menu:
                        "Playing the game [[Attack]":
                            y evil "How else am I going to win?"
                            $ battle_start(Mari,3,"You completely surprise her when you run right at her.", "killed_mari", True)
                        "Truth":
                            y sad "He just walked up to the shack where I was at ... I didn't trust him at all."
                            mari angry "Kenji? Why couldn't you trust him!? I don't believe you!"
                            y angry "He's an actor! They lie!"
                            show Mari angry
                            play sound "sfx/revolver_reload.ogg"
                            $ battle_start(Mari,0,"Mari aims to shoot you, clearly upset.", "killed_mari", True)

            "Lie" if kenji_murdered:
                $ lied_to_mari = True
                y scared "Wait up, please! Yes, Kenji is dead, but I didn't kill him!"
                show Mari scared
                y scared "I simply found his corpse! You have to believe me! Some sick bastard out there is trying to play this stupid game!"
                mari "R ... really?"
                y none "Yes. This blood must have come off when I was trying to bury him."
                show Mari sad
                "Mari seems to relax. She drops her arm down and is no longer aiming her gun at you."
                mari "That was nice of you ..."
                y happy "It was the least I could do."
                mari "Can I trust you, Shinobu?"
                "You blink. She remembered your name. For some reason, this makes you feel happy."
                menu:
                    "Yes":
                        y happy "Are you crazy? Of course you can!"
                        show Mari scared
                        y scared "Mari ... I want to protect you! That's why I found you."
                        "She searches your eyes."
                        mari "Really? ... Why?"
                        y happy "You're the one person I want to see win at the end of all this ... Please, let me protect you."
                        show Mari content
                        "She manages to force a sweet smile."
                        mari "Let's protect each other. Let's promise each other that we'll both get off this island alive."
                        "You return her smile and offer your hand. She takes it and shakes your hand to make it official."
                        y happy "I promise."
                        memo "Mari now travels with you."
                        if len(followers) == 0:
                            memo "Followers have a chance of assisting you in battle and can carry one extra item for you. You can talk to your followers at any time."
                        $ party_add(Mari)
                        $ follower_add(Mari)
                        hide Mari with dissolve
                    "No":
                        y angry "Of course, you can't."
                        show Mari scared
                        y angry "You can't trust anyone in this game. Only yourself."
                        show Mari angry
                        play sound "sfx/revolver_reload.ogg"
                        $ battle_start(Mari,0,"Mari immediately brings her gun back up and shoots at you.", "killed_mari", True)

            "[[Attack]":
                $ battle_start(Mari,3,"You really hate to do this, but you have to take her down.", "killed_mari", True)
    else:
        "Underneath that table ... Is that ... Mari!? You can't believe your eyes. She's a sight for sore eyes!"
        "You want to call out her name, but you had never spoken to her before this day. Why would you start now?"
        show Mari sad
        "Instead, you kind of mumble. Now you realize she had a gun aimed at you since you entered, but she lowers it now."
        mari sad "Shinobu?"
        y scared"M-Mari!"
        show Mari scared
        "You scare her from suddenly shouting, but she realizes you're just nervous and puts her gun down a second time."
        show Mari sad
        y happy"Oh, God, no, I'm sorry. I'm just ... so happy to see you!"
        show Mari content
        "She smiles sweetly and you remember why you've never worked up the courage to talk to her before. She comes out from underneath the table."
        mari "Thank you ... I'm glad to have run into you, as well."
        y none "Really?"
        show Mari sad
        mari scared "Yes! All of this -!"
        mari scared "I can't believe -!"
        mari sad "Shinobu!"
        "She is visibly shaking when she bursts into tears."
        "Before she collapses to the floor, you are by her side, scooping her into your arms."
        "You rock her back and forth in a cloudy daze yourself. The reality of this game is hitting you hard. Even the girl you admired the most can't seem to stomach it."
        "Finally, you both stand and look into each other's eyes."
        y sad "We're going to get through this."
        y happy "I promise you. We're both getting off this damn island alive."
        show Mari content
        "She sniffles and smiles again."
        mari content "That's the most beautiful thing I've ever heard."
        "The corner of her mouth twitches and you both chuckle. You feel like you can finally move on, but this time, together."
        $ party_add(Mari)
        $ follower_add(Mari)
        memo "Mari now travels with you."
        if len(followers) == 0:
            memo "Followers have a chance of assisting you in battle and can carry one extra item for you. You can talk to your followers at any time."

    jump room_loc
    
    
label mari_find_dead:
    $ cutscene()
    $ Mari.kill("murder",Kenji)
    "You creak open the door. You immediately see something that makes your stomach flip."
    "A woman is lifeless on the ground, covered in blood."
    "Oh god. That's ... Mari! Someone killed Mari!"
    "You look away, clenching your jaw and eyes shut from the grizzly murder scene. Who could have done this to her?"
    "You want to make whoever did this pay ..."
    $ saw_mari_dead = True
    jump room_loc
    
    
### JUN INTRODUCTION
label meet_jun:
    $ cutscene()
    ##Now that we're at their event, they can be be bots and be killed now, if you want
    #$ Jun.type = "normal"
    #$ Asai.type = "coward"
    # $ Jun.invincible = False
    # $ Asai.invincible = False
    $ Jun.met = True
    $ Asai.met = True
    "You walk quietly into the graveyard. Large tombstones and statues provide you with cover."
    play music "music/bgs_ghost2.ogg" noloop
    play sound "sfx/scream_man_pain_distant.ogg"
    if (Mari in party or Mari.loc == loc):
        "You both hear loud screaming up ahead. You hold your arm out in front of Mari in a protective gesture."
        mari "What was that? Let's go back ..!"
    else:
        "You hear violent screaming ahead."
    "The shouting gets close and you see a boy being chased by another boy, screaming for his life."
    "You recognize the boy running way to be Asai, the class clown, and his attacker to be Jun, a no-good delinquent."
    show Asai scared at left with dissolve
    asai "Aaaieeee! No! Noooo!"
    show Jun mad at right with dissolve
    jun "You're mine!!"
    if (Mari in party or Mari.loc == loc):
        "You jerk forward as if to intervene, but Mari is anchoring you in place, shaking her head."
        mari sad "No, don't ..."
        menu:
            "You must help him":
                y none "We can't sit back and watch people actually play this game. These are our classmates!"
                $ wpn.get_sfx()
                if wpn != fist:
                    "You pull out your weapon. She gasps in fear."
                mari scared "N-no! Don't kill him!"
                y none "Don't worry, I'm just going to scare him."
                if wpn == fist:
                    $ your_weapon = "your fists"
                else:
                    $ your_weapon = "your weapon"
                "Without another word, you break away from her and charge at Jun with %(your_weapon)s high."
            "Leave":
                "You nod and slowly back into the bushes so that you are not seen. You take Mari by the hand and run back the way you came."
                $ did_not_intervene_jun = True
                $ Asai.move(e2)
                $ Jun.move(rm_cave)
                $ Asai.invincible = False
                $ move_to_grid(runaway())
            
                
    else:
        $ wpn.get_sfx()
        if wpn == fist:
            "You can't just watch this passively. You run right for Jun."
        else:
            "You can't just watch this passively. You take out your weapon and take matters into your own hands."
            "You run right for Jun."
        # menu:
            # "Intervene":
#                 
            # "Leave":
                # "You try to quietly exit the area so that you don't get caught up in whatever that is."
                # $ did_not_intervene_jun = True
                # $ Asai.move(e2)
                # $ Jun.move(rm_cave)
                # $ Asai.type = "coward"
                # $ Asai.invincible = False
                # $ move_to_grid(runaway())
            
    play sound "sfx/bodyfall.ogg"
    "Asai trips and falls to the ground. Jun is able to catch up with him as he lets out a high-pitched scream."
    asai "We were friends! We were friends!!"
    show Jun surprised
    "Just as Jun gets his hands around the boy's collar, he notices you and jumps in surprise."
    if wpn.wpn_rating > 2:
        jun "Don't aim that damn thing at me!"
    else:
        show Jun skeptical
        jun "Wha ...?"
        
    y angry "Let him go!"
    show Jun mad
    show Asai angry
    asai "Yes!! Let me go!"
    jun "Not a chance!"
    show Asai scared
    menu:
        "[[Attack]":
            hide Asai with dissolve
            show Jun at center with move
            # You chose to kill him in this scenario, non-lethal battles are not yet fully implemented (i.e. taser)
            $ battle_start(Jun,0,"No more negotiating!", "killed_jun2", True, flee=False)
        "Ask him one more time":
            y angry "I'm not going to ask you again!"
            show Asai angry
            asai "Yeah! Let me -!"
            play sound "sfx/punch.ogg"
            show Asai scared with hpunch
            "Jun punches Asai in the face before he could finish."
            if wpn != fist:
                "You tighten your grip on your weapon, but Jun is calling your bluff."
            jun "When I get done with you, your face is going to be soup!"
            asai "Nooo! Nooooo!"
            y angry "Stop it right now, or I'll be forced to attack!"
            "Jun hesitates and evaluates you."
            "You really didn't want to hurt him, but he wasn't as intimidated by you as he should be ..."
            
        "Demand explanation":
            y none "Why not!?"
            jun "This asshole stole my shit and thinks he can just run away!"
            "You blink and look at Asai squirming in Jun's grip."
            y none "He stole something?"
            show Asai angry
            asai "No!!"
            jun "Yes, you did, you prick! Why else are you running!?"
            show Asai scared
            asai "Uwaaaah let me go!"
            play sound "sfx/punch.ogg"
            show Asai scared with hpunch
            
            "Jun punches Asai in the face."
            y angry "Hey!! Let him go!"
            show Jun sad
            jun "But -!"
            y angry "Now!"
    show Jun skeptical
    if wpn.wpn_rating > 2:
        "It's evident in Jun's eyes that he's afraid of you actually attacking him. So he lets Asai go."
    else:
        "Jun rolls his eyes and lets Asai go."
    show Jun angry
    $ Asai.loc = e2
    hide Asai with dissolve
    show Jun angry at center with move
    if wpn == fist:
        "After it's clear that Asai made a clean getaway, you lower your fists somewhat, but you fear that Jun may attack so you keep it at the ready."
    else:
        "He understandably springs up and away into the woods, all while you keep your weapon aimed."
        "After it's clear that Asai made a clean getaway, you lower your weapon somewhat, but you fear that Jun may attack so you keep it at the ready."
    jun "Great. Now he's off with my shit."
    show Jun angry
    jun "He acted like we were best buds in the beginning and then he just takes off with all my food. I hope he twists his damn ankle out there."
    "You feel a little bad for robbing this man of retribution, but you have no regrets just the same."
    y none "I'm sorry. I was just trying to prevent more bloodshed."
    if wpn.seen and not None:
        show Jun mad
        jun "Will you put that thing away already!? I ain't gonna hurt you!"
        "You look down at your weapon from the reference. Jun suddenly pulls something out of his back pocket and you tense."
    else:
        "Jun suddenly pulls something out of his back pocket and you tense."
    $ reference_item(ladle)
    $ ladle.get_sfx()
    show Jun lookaway
    "But it's just a soup ladle."
    jun "This is all I got from those assholes."
    show Jun angry
    if wpn.wpn_rating > 2:
        "You feel like laughing, but you restrain yourself."
    else:
        y happy "Heh ... looks like we're in the same boat then."
        jun "Yeah. Guess so."
    "You stand awkwardly for a moment, both unsure of each other's intentions. Was Jun playing the game or not?"
    "He was a rotten apple in school, so it seemed like he would be the first one to revel in this bloody game, and maybe if he got a decent weapon, he would. But right now, he looks rather harmless."
    if (Mari in party or Mari.loc == loc):
        jun "Who's the chick you're with?"
        "He nods behind you and you spin around to see Mari walking forward tentatively."
        y sad "Um ... Mari Tsutaya. Don't you know? She's in our class."
        show Jun lookaway
        jun "Oh. Yeah, I don't remember everyone."
        show Mari at left with dissolve
        show Jun at right with move
        mari "Um ... hi. Jun, right?"
        jun "Mm. You guys boyfriend and girlfriend or something?"
        show Mari scared
        "You both fluster rather quickly and make several negative noises."
        
        mari "No, no, no ..."
        show Jun skeptical
        show Mari content
        jun "Okay, okay, calm down. Sheesh."
        show Jun angry
    if (Mari in party or Mari.loc == loc):
        show Mari scared
    hide Jun with dissolve
    "Jun starts walking away out of the graveyard."
    menu:
        "Let him go":
            pass
        "[[Attack]":
            hide Mari
            show Jun
            $ battle_start(Jun,0,"Now's your chance!", "killed_jun2", True, flee=False)
        "Ask Jun to join you":
            if (Mari in party or Mari.loc == loc):
                show Mari sad
                mari "Where are you going? Stick with us!"
                show Jun at right with dissolve
            else:
                y none "Where are you going? We should team up!"
                show Jun with dissolve
            jun "Huh? Why?"
            y none "People are killing each other out there! If you're not playing the game, then we can stick together."
            show Jun lookaway
            "He let the idea settle for a moment, shifting his weight."
            
            if (Mari in party or Mari.loc == loc):
                show Jun skeptical
                jun "Nah."
                "And then he turns to leave again."
                show Mari scared
                mari "Wait! Please!"
                show Jun lookaway
                jun "I can take care of myself, babe!"
                hide Jun with dissolve
                show Mari sad at center with move
                mari "Babe!?"
                y none "Forget him, Mari. I'll protect you, that's all you need."
                show Mari
                "She tries to smile but she is too busy gulping down a frown. You look back, but Jun is already gone."
            else:
                jun "Uh ... why?"
                y scared "Because ... we can help each other! I don't know what else to say, man!"
                
                jun "No offense, but I barely know you. That guy just now acted like my friend, too."
                show Jun skeptical
                jun "So don't take it personally when I tell you to go to hell, all right? All right."
                hide Jun with dissolve
                "You make an offended noise, but Jun is already out of ear shot."
                "Looks like you're still on your own."
    $ Jun.move(rm_cave)
    jump grid_loc
        
label killed_jun2:
    show Asai scared with dissolve
    "The bad boy lies dead at your feet. You wipe the sweat from your brow."
    play sound "sfx/scream_man_pain_distant.ogg"
    hide Asai with dissolve
    "Asai looks at you like you're a demon and lets out another screech before jolting up and darting for the forest."
    $ Asai.move(e2)
    y none "Wait!"
    "But he is too fast and is already gone."
    if (Mari in party or Mari.loc == loc):
        $ Mari.make_foe(you)
        $ party_remove(Mari)
        $ followers.remove(Mari)
        $ Mari.move(a1)
        "You hobble back to where you left Mari. Surprisingly, she is not there."
        y none "Mari ...?"
        "You look around and she is nowhere to be found."
        "For some reason, you have a good feeling that she left on her own accord."
    jump grid_loc
    
## JUN RECRUITMENT
label cave_jun_ext:
    $ cutscene()
    "Frigid air pours out of the cave and a chills slithers down your spine."
    if (Mari in party or Mari.loc == loc):
        "Mari grasps at your arm."
        mari scared "Did you feel that?"
        "You nod and walk towards the entrance."
        mari scared "Shinobu!? No! I don't want to go in there! It's dark!"
        y none "It's either be sitting ducks out here, or in the creepy cave. Look, it's not that creepy anyway."
        "She gulps down her apprehension and you both eye the waiting dark."
    else:
        "You push down your fear of what's inside of the den and eye the waiting dark."
    return
    
label cave_jun:
    $ cutscene()
    play music "music/bgs_drip.ogg" noloop
    "You slink into the cave and feel an instant overwhelming unease."
    if (Mari in party or Mari.loc == loc):
        "Mari clings to you in fear."
    "The light from the mouth of the cave runs out shortly and it is difficult to see anymore. Your eyes adjust to the darkness."
    play sound "sfx/twig.ogg"
    "You hear a rustling sound directly in front of you. You stop."
    if (Mari in party or Mari.loc == loc):
        mari scared "What was that?"
    "There are likely animals living in this cave. It was probably just a bat."
    "You press on, even though your stomach is tightening with each step."
    "The clammy atmosphere seems to curl around your throat and strangle you. It's difficult to breathe."
    play sound "sfx/sound_left2.ogg" channel 1
    "Your shoe hits rock formations on the ground. But you swear that the sound you just heard was not an echo. Something made a sound elsewhere in the cave ..."
    if (Mari in party or Mari.loc == loc):
        mari sad "Can we go back? Please?"
    "The light flickers in your hand. No! If it went out - you'd be stuck here in complete darkness!"
    stop music
    play sound "sfx/accent_wash.ogg"
    play music "music/bgs_monster.ogg"
    "A low grumble fills the air around you. A monstrous voice; an inhumane voice. You freeze from your head to your toes."
    "The voice breathes again, louder. The cold air turns uncomfortably warm for a brief moment, almost as if you imagined it."
    "You then hear the voice moan something that sounds like \"gooooo\" and it gets louder, then abruptly stops."
    if (Mari in party or Mari.loc == loc):
        "Mari heaves in terror like she will cry at any second."
        mari scared "Please, please, please, let's go ..!"
    menu:
        "Leave":
            "You weren't sure what you up against: a bear, a ghost, or worse - a student playing the game."
            "You instantly turn and leave in the direction that you came. You walk so fast that your light flickers dangerously, making your heart beat even faster."
            $ loc = loc.parent
            jump grid_loc
        "Stay":
            $ Jun_recruited = True
            "There was nothing in this cave that could be more horrifying than anything you've already witnessed on this island."
            y angry "Is anyone there? If this is someone playing a trick, just come out!"
            who "Goooooo!!"
            if (Mari in party or Mari.loc == loc):
                "Mari shrieks and runs in the other direction, but she doesn't get far without your light."
            y scared "Who is that!?"
            who "Get ooouuuutttt!"
            y angry "Hey! Hey, knock it off!"
            "The voice growls like a monster, but it falters at the end, sealing your suspicion that it is just a person."
            y angry "I know you're just a loser pretending to be something scary, so just come out and I won't attack you!"
            stop music fadeout 4.0
            play sound "sfx/crack.ogg" fadein 3.0
            "There is a long silence. You hear some pebbles shift and you jerk towards the sound in defense. You see nothing."
            "More silence."
            "Something hot breathes on your neck."
            stop music
            play sound "sfx/accent_stab.ogg"
            show Jun with quickdissolve
            if wpn == fist:
                $ your_weapon = "your fists"
            else:
                $ your_weapon = "your weapon"
            "You whip around with %(your_weapon)s -!"
            
            jun "Ugh, fine. You got me."
            "The terror takes some time to fade from your body."
            if not Jun.met:
                "You don't even recognize this man at first. It completely boggles your mind."
                "But slowly, as you take in his apathetic stance you recognize him. He is a student in your class after all. He just rarely ever showed up."
                y none "You're the drop-out ..."
                show Jun angry
                jun "I have a name, asshole."
                y sad "Uh ..."
                show Jun lookaway
                jun "Nada Jun."
                y happy "Right! Right ... Sorry."
                show Jun
                jun "Now get outta my cave."
                y none "Why are you hiding in here anyway?"
                show Jun skeptical
                jun "It's a creepy goddamn cave!"
                y angry "Just so you can pull this baby scare stuff!?"
                show Jun
                $ reference_item(Jun.wpn)
            else:
                if (Mari in party or Mari.loc == loc):
                    y none "Damn it, Jun! You scared the shit outta Mari!"
                else:
                    y none "Fuck, Jun! What the hell was that!?"
                show Jun skeptical
                "Jun just sighs."
            jun "Whatever. All I have is a goddamn ladle. I either lie down and die, or get creative."
            show Jun angry
            if wpn == fist:
                "You gulp and finally lower your fists, realizing he's not truly a threat ... Not with a blunt utensil anyway."
            else:
                "You gulp and finally lower your weapon, realizing he's not truly a threat ... Not with a blunt utensil anyway."
            if (Mari in party or Mari.loc == loc):
                hide Jun with dissolve
                "You trust him enough to turn your back on him and go over to Mari who has tucked herself into a ball on the floor. When you touch her back, she flinches."
                y none "It's all right ... Mari, it's just me. It was only Jun trying to scare us. Look. You're safe."
                "You rub her back and she eventually uncurls. She looks at you, and then over at Jun. She sniffles."
                show Jun with dissolve
                jun "Jesus, sorry, okay? She didn't piss herself did she?"
                show Mari sad at left with dissolve
                show Jun at right with move
                "Mari manages to shake her head, answering for herself. She wipes the tears from her cheeks and stands, still shaken."
                mari angry "I hate ghosts ..."
                menu:
                    "Ask him to join you":
                        y none "If this is the best you can do, why don't you just follow us? We have weapons. Look, I'll even give you one if you just help us out."
                        call recruit_jun
                    "Say good-bye": 
                        y "All right. Thanks for not killing me when you had the chance. I'll return the favor. For now."
                        show Jun scared
                        y "... That was a joke."
                        show Jun skeptical
                        jun "You're not funny, man."
            else:
                y none "Did you really think that lame-ass moaning was really going to scare me?"
                show Jun skeptical
                jun "Well, it totally did for some other chick. So, yeah."
                show Jun angry
                y none "It's not going to work on most people. I've seen way worse out there ... This is kindergarten stuff."
                show Jun lookaway
                jun "Yeah, okay, thanks."
                menu:
                    "Ask him to join you":
                        y none "Dude, why don't you just come with me? If we team up together, we could probably take on this whole island."
                        show Jun
                        "Jun didn't respond."
                        y none "I'm serious. I'll give you a weapon, food, whatever. We can beat this damn thing."
                        call recruit_jun
                    "Say good-bye": 
                        y "All right. Thanks for not killing me when you had the chance. I'll return the favor. For now."
                        show Jun scared
                        y "... That was a joke."
                        show Jun lookaway
                        jun "You're not funny, man."
                
            
           
    jump grid_loc
    
label recruit_jun: 
    "Jun was silent for a while longer."
    show Jun skeptical
    jun "Yeah, all right. This was getting boring anyway."
    
    if (Mari in party or Mari.loc == loc):
        show Jun angry
        jun "But no cutesy couple stuff while I'm around. That shit's nauseating."
        "He flusters both you and Mari, but you both don't correct him, just wanting to get out of the cave."
    else:
        show Jun
        "You laugh out of relief."
        y happy "All right. Great. We're going to figure this out together."
        y none "No one's come to save us yet, so the heroes are probably us."
        show Jun skeptical
        jun "Yeah, I figured. I'm always saving my own ass."
        y none "We're going to get off this island, I know it."
        show Jun
        jun "Then shut up and let's go find out how."
        
    $ party_add(Jun)
    $ follower_add(Jun)
    memo "Jun now travels with you."
    if len(followers) == 0:
        memo "Followers have a chance of assisting you in battle and can carry one extra item for you. You can talk to your followers at any time."
    return
    
label tetsuo_asai:
    $ Tetsuo.met = True
    $ cutscene()
    $ e2.find()
    "You hear a familiar whiny voice as you walk into this part of the woods. Asai must be near."
    if did_not_intervene_jun:
        "But you thought that gang member would have killed him? Why was he still alive?"
        "Did Asai manage to kill him!?"
    show Asai at left
    show Tetsuo at right
    with dissolve
    "Indeed, you see Asai talking with Tetsuo, the school's annoying go-getter."
    asai "Heeey, buddy. Whatcha up to?"
    show Tetsuo happy
    tet "Oh! Hi! Are you lost, too?"
    asai "Oh man, totally, man. Have you found anybody yet?"
    show Tetsuo
    tet "Well, there was Yoriko, but she left rather quickly."
    tet "She's always been a very motivated girl and always signed up for community service. I don't believe I've ever seen you at school government meetings -"
    play music "music/GiveMeChills.ogg" fadein 4.0 fadeout 3.0
    show Tetsuo scared
    tet "What are you doing?"
    asai "Just seeing what you got."
    if Asai.met:
        "So this is how it went down with the last guy. Befriend him ... take his stuff."
    else:
        $ Asai.met = True
    if (Mari in party or Mari.loc == loc) and Mari.alive:
        mari scared "What..?"
    show Tetsuo happy
    tet "Don't worry about that, because I'm not playing the game!"
    tet "I just need to rally all the students together, and we'll start a formal protest by the edge of island. Surely they can't ignore our rights."
    show Tetsuo
    asai "Ooooh."
    show Tetsuo scared
    if (Jun in party or Jun.loc == loc) and Jun.alive:
        show Jun angry at center
        show Asai scared
        "Before Asai gets a chance to pilfer Tetsuo's belongings, Jun jumps out of the bushes!"
        jun angry "Oi, jackass! Found another mark?"
        tet "Mark!?"
        y angry "Jun told me what happened. You won't get away this time!"
        jun angry "You want another beatdown, clown!?"
        show Asai angry
        "Asai gets squirrelly all of a sudden."
        asai "Fuck you, dude! You're taking a bully's side over mine, that really shows your morality -"
        show Asai scared
        asai "AHH!"
        hide Asai
        hide Tetsuo
        hide Jun
        with quickdissolve
        "He points behind you. You and Jun instinctively look, not sure what to expect anymore."
        show Tetsuo scared at right
        show Jun skeptical at left
        with quickdissolve
        "Obviously, nothing was there, and when you look back, Asai is running away at the speed of light."
        $ Asai.move(d2)
        stop music fadeout 3.0
        y angry "Shit!"
        jun skeptical "Did he take anything?"
        tet "No, you scared him off before he could."
        jump stopped_asai
    $ axe.get_sfx()
    $ loc.items.append([drill,1])
    $ Asai.wpn = axe
    $ Tetsuo.wpn = None
    "You watch Asai pull out a long-handled axe from Tetsuo's bag."
    asai "You're definitely a better friend than Jun."
    tet "Hey now, you should put that down. Someone could get hurt, you know."
    "Asai looks up at Tetsuo, and you can't mistake the glimmer in his eye."
    if Asai.met:
        "You should have stepped in a lot sooner, knowing this guy is a downright thief."
    menu:
        "Just watch":
            "But this is Tetsuo's problem, not yours."
            play sound "sfx/swoosh3.ogg"
            "Asai gives the axe a test swing. This finally sets Tetsuo on edge. He steps back and holds his hands out."
            tet "D-d-don't do that, that's a severe safety hazard!"
            asai "So?"
            tet "Someone could get h-h-hurt!"
            play sound "sfx/swoosh3.ogg"
            "Asai swings it again and laughs. Tetsuo jumps back."
            tet "I'm being very serious right now, sir! That's mine and you should put it -!"
            asai "It's mine now, stupid! Don't want to get hurt!?"
            play sound "sfx/swoosh3.ogg"
            "Another swing, another laugh."
            tet "Asai Mokuami! When we get back to school, I personally write you twenty demerits for disobedience!"
            tet "We may be in the jungle, but I'm still your Vice Presi-!"
            stop music
            show Asai scared
            play sound "sfx/swoosh3.ogg"
            play sound "sfx/slice.ogg" channel 1
            $ show_blood()
            tet "AAAHHHH!!"
            play sound "sfx/bodyfall.ogg"
            hide Tetsuo with dissolve
            "The axe clipped Tetsuo right in the stomach. He looks at the blood pouring from him in a gurgled silence. He falls to the ground."
            if (Mari in party or Mari.loc == loc) and Mari.alive:
                "Mari squeals and stifles a scream, holding her mouth shut."
                "Asai looks surprised to have actually hit him, then looks around frantically."
            else:
                "Asai looks surprised to have actually hit him ..."
            show Asai angry
            "But when Tetsuo's on the ground, he hardens his expression."
            play sound "sfx/hit_bloody.ogg"
            $ show_blood()
            hide Asai with dissolve
            $ Tetsuo.kill("murder",Asai)
            $ Asai.sanity -= 30
            $ add_sanity(-15)
            "You cannot bear to watch as the guy who used to be the class clown brutally hacks at Tetsuo's body. No one would have survived that."
            "When you can finally find the strength to look back, Asai is scurrying off."
            "You're left alone with Tetsuo's corpse."
            if (Mari in party or Mari.loc == loc) and Mari.alive:
                "Mari covers her eyes, unable to look."
                mari scared "We... We should've done something ..."
                mari sad "Tetsuo... I'm so sorry."
                $ Mari.make_foe(Asai)
                # She loses her sanity from witnessing something like that
                $ Mari.sanity = max(0, Mari.sanity - 10)
            $ Asai.move(d2)
            $ Asai.invincible = False
            $ Asai.invisible = False
            # He evolves from a "coward" to "normal"
            $ Asai.type = "normal"
            jump grid_loc
        "Stop Asai":
            $ kill_asai_later = True
            y angry "Cut it out!"
            show Asai scared
            "You jump out to hopefully intimidate Asai into leaving this guy alone."
            if Asai.met:
                y angry "He's just trying to steal your things, or worse!"
                tet "Worse!?"
                show Asai angry
                if did_not_intervene_jun:
                    asai "How do you know!?"
                    y angry "I saw you with that tough guy! You should have been killed, but you ... weren't!"
                    asai "Jun? That pansy!? All he had was a soup ladle!"
                    y sad "But he ..."
                    if Jun.alive:
                        "You check your stats page quick and see that Jun is still alive. Odd."
                else:
                    asai "Saved me just to rat me out!?"
            y angry "He may not fight you, but I will!"
            show Asai angry
            "Asai gets squirrelly all of a sudden."
            asai "Fuck you, dude! You're not some big shot! Even back in school I was -"
            show Asai scared
            asai "AHH!"
            hide Asai
            hide Tetsuo
            with quickdissolve
            "He points behind you. You instinctively look, not sure what to expect anymore."
            show Tetsuo scared at right with quickdissolve
            "Obviously, nothing was there, and when you look back, Asai is running away at the speed of light."
            y angry "Shit!"
            tet "He took my things!"
            y angry "I'll get them back - wait here!"
            if (Mari in party or Mari.loc == loc) and Mari.alive:
                "You run ahead, leaving Mari behind."
                $ party_remove(Mari)
            $ Asai.move(d2)
            hide Tetsuo with dissolve
            $ loc = d2
            jump chase_down_asai
        "Attack Asai":
            $ kill_asai_later = False
            $ battle_start(Asai,3,"Asai's trouble-making days are over.", "you_killed_asai", True, flee_enemy_jump="tetsuo_killed_asai")
        "Attack Tetsuo":
            $ Tetsuo.wpn = fist
            $ kill_asai_later = False
            hide Asai with quickdissolve
            show Tetsuo scared at center with move
            $ battle_start(Tetsuo,3,"Might as well beat Asai to the punch. You've secretly always wanted to do this anyway, because this guy is annoying as hell.", "you_killed_tetsuo", True, flee_enemy_jump="you_killed_tetsuo")

label stopped_asai:
    show Tetsuo happy
    tet "Thanks, Shinobu! I really didn't expect you two to stand up for me like that."
    if (Jun in party or Jun.loc == loc):
        "Tetsuo looks Jun up and down with mixed emotions."
        jun mad "Well screw you, too."
        show Tetsuo scared
        tet "Pardon? I ... I didn't mean to offend you."
        jun skeptical "Not even a thanks? Whatever, man."
        hide Jun lookaway with dissolve
        tet "Let's not get all worked up. Our conditions may be bad, but we have to stick it out."
    if (Mari in party or Mari.loc == loc):
        "Mari works up the courage to leave from her hiding spot and meet up with the rest of you."
        show Tetsuo happy
        tet "Mari! Lovely to see you."
        mari content "Hi."
    y none "How are you doing out here? Besides Asai trying to steal from you, I mean."
    show Tetsuo angry at center
    tet "Terrible! How could they stick us out here without proper first aid kits or, worse yet, indoor plumbing?"
    show Tetsuo
    tet "Don't worry, though. Yoriko and I are on the case."
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
        $ Tetsuo.kill("murder",killer=Yoriko,drop_loot=True)
        "Tetsuo falls face-first onto the ground and reveals an arrow in his back!"
        jump yoriko_arrow_attack
    else:
        y none "That ... doesn't sound like it will work, honestly."
        tet "We have to try!"
        "You start to walk away. You're not sure you can help someone so delusional."
    jump grid_loc

label you_killed_asai:
    if not Asai.alive:
        "Asai crumples into a fetal position and goes lifeless."
    call murder_follower_reaction
    if Tetsuo.met and Tetsuo.alive:
        if kill_asai_later:
            "Time to return back to Tetsuo and let him know you dealt with this clown."
            jump return_to_tetsuo
        elif Tetsuo.loc == loc:
            jump tetsuo_killed_asai
    else:
        "One down. How many more to go?"
    jump grid_loc

label return_to_tetsuo:
    $ cutscene()
    play ambience "sfx/grassland2.ogg" fadeout 1.0 fadein 2.0
    scene forest3 with fade
    $ loc = e2
    "You walk back to where you last saw Tetsuo."
    # Bring Mari back into your party
    if Mari.loc == e2 and Mari in followers:
        $ party_add(Mari)
    if Asai.murderer == you:
        y evil "The clown's dead."
        jump tetsuo_killed_asai
    if axe.is_in_inventory():
        y none "Here's your axe back..."
    else:
        y none "Sorry, I couldn't get the axe."
    show Tetsuo at center
    tet "Oh, that's okay! You can keep it. I'm not really interested in {u}using it{/u} for anything, anyway."
    jump stopped_asai
    

label found_tetsuo_murdered:
    $ cutscene()
    if Yoriko.alive:
        play music "music/bgs_creepy.ogg"
        $ Tetsuo.kill("murder",Yoriko,drop_loot=True)
        y scared "Oh no ..."
        "Testuo is lying face-first on the ground with an arrow sticking out of him."
        if (Jun in party or Jun.loc == loc):
            jun scared "Shit sticks!!"
        if (Mari in party or Mari.loc == loc):
            "Mari shrieks in terror."
        jump yoriko_arrow_attack
    jump grid_loc
        
label tetsuo_killed_asai:
    show Tetsuo scared at center with move
    tet "What did you ... I ... can't ..."
    menu:
        "Reassure His Safety":
            y none "You're safe now. He can't take your stuff, or hurt you."
            if not Asai.alive:
                tet "You {u}killed{/u} him!"
            else:
                tet "You {u}attacked{/u} him!"
            y angry "Don't overreact. People are dying left and right in this game - I'm just trying to help you. Really."
            tet "I need to get to a phone - I need to call the police!!"
            y scared "Settle down!!"
            tet "Help!! {u}Heeeeelp{/u}!!"
            y angry "No, don't shout!! You'll attract attention!"
            if Yoriko.alive:
                tet "Murder! Mur-!"
                play sound "sfx/blood2.ogg"
                "Tetsuo freezes. He's not even breathing."
                hide Tetsuo with dissolve
                $ Tetsuo.kill("murder",Yoriko,drop_loot=True)
                "He then collapses onto the ground, face-first. An arrow is sticking out of his back."
                if "Jun" in party:
                    jun scared "Oh, sweet Jesus!"
                elif "Mari" in party:
                    "Mari shrieks in terror."
                else:
                    "You're not alone!"
                jump yoriko_arrow_attack
            else:
                tet "Murderers! Murderers!!"
                $ Tetsuo.type = "coward"
                $ Tetsuo.enemies.append(you)
                $ Tetsuo.move("rand")
                jump grid_loc
                
        "[[Attack]":
            $ Tetsuo.wpn = fist
            y evil "You're next."
            tet "What!? No!"
            tet "It's against school policy to threaten m-!"
            $ battle_start(Tetsuo,3,"So. Annoying.", "you_killed_tetsuo", True, flee_enemy_jump="you_killed_tetsuo")
    
label you_killed_tetsuo:
    if not Tetsuo.alive:
        "Tetsuo was surprisingly easy to kill. But it didn't feel as good as you imagined it."
    call murder_follower_reaction
    if Asai.alive and Asai.loc == loc:
        show Asai scared with dissolve
        asai "Oh, fuck!"
        y evil "Your turn."
        asai "No! Noooo!"
        hide Asai with dissolve
        "Asai breaks into a run, weaving into the trees. You curse and chase after him."
        $ Asai.move(d2)
        $ loc = d2
        $ Asai.type = "coward"
        jump chase_down_asai
    jump grid_loc
    
label chase_down_asai:
    $ d2.find()
    play ambience "sfx/waterfall.ogg" fadeout 1.0 fadein 2.0
    scene waterfall with fade
    "You become out of breath and no longer see, or even hear, Asai running away."
    "A shuffling of leaves to your side alerts you. You don't see anyone, but there's large rocks blocking your view."
    show Asai scared with dissolve
    "You quickly round the boulders and find Asai sniveling on the ground."
    show Asai angry
    asai "Fuck off! No! Go away! No!"
    menu:
        "[[Attack]":
            $ battle_start(Asai,0,"If he's not going to make the first move, then all the better for you.", "you_killed_asai", True, flee_enemy_jump="you_killed_asai")
        "Reason with him":
            y angry "Knock it off, and grow up!"
            show Asai scared
            if Tetsuo.murderer == you:
                y angry "Quit running! If you want to survive this game, you need to have resolve."
                asai "So you'd do me in like you did Tetsuo!? I'm your next mark, you can't fool me!!"
            else:
                # Sane Shinobu still preaches "don't play the game" schtick
                if sanity >= 40:
                    y angry "We can survive this game if idiots like you didn't actually play it!"
                # Depressed Shinobu! Yaay!
                else:
                    y angry "At least face death with dignity, man! Quit being such a coward!"
                asai "We're all going to die! That's what it said! A few days and then everyone dies!"
            show Asai angry
            asai "But I can still live! So I'm going to!"
            asai "I'm gonna live!!"
            # Hey, look! He grows up! That pep talk made him less of a coward!
            $ Asai.type = "normal"
            $ battle_start(Asai,0,"He finally attacks you. You're prepared.", "you_killed_asai", True, flee=True, flee_enemy_jump="you_killed_asai")
        "Threaten him":
            y angry "Give it back."
            "You point at the axe Asai stole."
            asai "O-or else what?!"
            "You take out your weapon."
            $ wpn.get_sfx()
            y angry "You won't like how this ends."
            if wpn.wpn_rating + wpn.battle_range > Asai.wpn.wpn_rating + Asai.wpn.battle_range:
                asai scared "Eeeek!!"
                stop music fadeout 3.0
                hide Asai with quickdissolve
                "Asai runs from you squealing like a girl, leaving his weapon behind."
                $ return_weapon = Asai.wpn
                $ Asai.wpn = None
                $ return_weapon.add()
                $ Asai.make_foe(you)
                $ Asai.move("rand")
                "No point chasing him again."
                jump return_to_tetsuo
            else:
                "Asai gives a nervious chuckle."
                y angry "So, what will it--"
                $ battle_start(Asai,3,"Before you can finish your sentence, he lunges at you!", "you_killed_asai", True, foe_advantage=True, flee_enemy_jump="you_killed_asai")
                
    
label yoriko_arrow_attack:
    play sound "sfx/bow_shot.ogg"
    play music "music/AngryOpheliasSong.ogg"
    $ who_has_arrows = True
    "Another arrow shoots out from the trees towards you. You jump out of the way."
    if (Mari in party or Mari.loc == loc) and (Jun in party or Jun.loc == loc):
        "Jun grabs Mari and pulls her out of the open. He yells at you."
        jun mad "Run for it, jackass!"
    elif (Mari in party or Mari.loc == loc):
        "Mari darts for the trees, screaming."
    elif (Jun in party or Jun.loc == loc):
        jun scared "Shit, shit, shit!"
    "Someone's trying to kill you!"
    jump catch_yoriko
            
init python:
    def damage_you(num):
        global armor
        damage = num
        if armor != None:
            damage = damage * -1
            damage = shield(damage,armor.defense)
            damage = damage * -1
        add_health(damage)
        if health <= 0:
            renpy.call("deaths_door")
        if health <= 0:
            renpy.jump("game_over")

label abandon_arrow_chase:
    $ Yoriko.met = True
    "You can't compete! To save your life, you're forced to duck into the woods and try to shake them."
    #MOVE
    if (Mari in party or Mari.loc == loc) and (Jun in party or Jun.loc == loc):
        "You meet up with your friends. They scold you for even trying."
    elif (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        "You meet up with your friend. They scold you for even trying."
    else:
        "So much for finding out who that was ..."
    $ rand_grid = runaway()
    $ move_to_grid(rand_grid)
    
label you_caught_yoriko:
    $ Yoriko.met = True
    $ Yoriko.hidden = False
    "Yoriko's remains tumble down the gentle slope of the ground."
    "You can't believe she was capable of such hostility. Yet, as you remember, she was a no-nonsense class president who needed everything exactly the way she wanted."
    "Maybe this wasn't out of her league at all."
    if (Mari in party or Mari.loc == loc) and (Jun in party or Jun.loc == loc):
        show Mari scared at left
        show Jun scared at right
        with dissolve
        "Jun and Mari came running up the hill to see if you're all right."
    if (Mari in party or Mari.loc == loc):
        if Jun not in party:
            show Mari scared with dissolve
        mari "Oh my goodness ... Is that ... Yoriko? She tried to kill us!?"
        show Mari yell
        mari "This game is corrupting everyone!"
    if (Jun in party or Jun.loc == loc):
        if Mari not in party:
            show Jun surprised with dissolve
        jun "Wow, man. I thought you were crazy, but you clearly know what you're doing."
        show Jun lookaway
        jun "You know, I think I even remember this one."
        show Jun angry
        jun "She's the one who kept calling and nagging me about homework and shit."
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        y none "We don't have to worry about her anymore."
    "You wonder how this game is truly going to end."
    jump grid_loc
    
## HITOMO @ BRIDGE
label find_hitomo:
    $ cutscene()
    $ Hitomo.invisible = False
    $ Hitomo.met = True
    show Hitomo scared
    y none "Hitomo?"
    $ reference_item(Hitomo.wpn)
    $ Hitomo.wpn.get_sfx()
    "She jumps and then aims her gun at you."
    y scared "Whoa, whoa!"
    python:
        if len(loc.bodies) > 0:
            innocent = True
            for i in loc.bodies:
                if i.murderer.name == you.name:
                    innocent = False
        else:
            innocent = True
    if not innocent:
        $ battle_start(Hitomo,0,"She knows you're a murderer. It's too late.","murdered_hitomo", True)
    else:
        hit "Are you playing the game!?"
    menu:
        "Yes [[Attack]":
            y evil "Afraid so."
            $ battle_start(Hitomo,0,"You know you become her living nightmare as you strike.","murdered_hitomo", True)
        "No":
            y sad "No! Never!"
            show Hitomo
            hit "Oh. Okay."
            y none "What are you guarding?"
            hit "Nanako says no one is allowed to cross - except for who she says."
            y none "Why? What's on the other side?"
            show Hitomo scared
            hit "N-n-none of your business!!"
            y sad "... What? Why not?"
            hit "Because you'll never go there! Nanako said nothing about you!"
            if (Jun in party or Jun.loc == loc):
                show Jun at farright behind Hitomo with dissolve
                jun "She say anything about me?"
                show Hitomo
                hit "Who are you!?"
                show Jun skeptical
                jun "I dunno. Who are {u}you{/u}?"
                show Jun
                show Hitomo scared
                hit "I-I'm Hito - Hey, you know who I am!"
            if (Mari in party or Mari.loc == loc) and Mari.alive:
                show Mari sad at farleft with dissolve
                mari "What about me?"
                show Hitomo
                hit "Um ... Well, yeah, she likes you."
                show Mari
                mari "Then if I can cross, can't I take Shinobu with me?"
                hit "Um ... No?"
                show Mari sad
                y sad "That doesn't seem fair. If she trusts me, and Nanako trusts her, then shouldn't she, uh ... ugh, now I'm confused."
                hit "Maybe if Mari goes and asks permission first ..."
                menu:
                    "[[Attack]":
                        $ battle_start(Hitomo,3,"There is a quicker way to the other side.","murdered_hitomo", True)
                    "Agree to let Mari go":
                        y angry "Jeez. Okay. If that's the only way ..."
                        show Mari
                        if (Jun in party or Jun.loc == loc):
                            y none "We'll wait here, Mari."
                        else:
                            y none "I'll wait here for you, Mari."
                        hide Mari with dissolve
                        $ party_remove(Mari)
                        $ Mari.move(rm_lockers)
                        play sound "sfx/bridge_cross.ogg"
                        "She nods and then eyes the rickety bridge. She cautiously begins to cross it, squealing every time the bridge sways."
                        "You stand silently in front of Hitomo. Her gun is still ready to kill, but she doesn't move."
                        scene black with dissolve
                        $ add_time(1,False)
                        scene bridge with dissolve
                        show Hitomo with dissolve
                        "You have been waiting for Mari to return for some time now. Even Hitomo's arm has gotten tired and she's reclining instead of holding you at bay."
                        if Ai.alive:
                            menu:
                                "[[Attack]":
                                    "This could be your chance -"
                                "Wait":
                                    "Hopefully Mari will come back soon, because -"
                                "Chat":
                                    y happy "So ... Hitomo ... I heard you play the trumpet?"
                                    show Hitomo happy
                                    "Her eyes light up from the reference to her life before all of this."
                                    hit "Yeah, I -"
                            call ai_attacks_hitomo
                        elif walkietalkie.is_in_inventory() and Mari.item[0] == walkietalkie and not walkietalkie.broken:
                            play sound "sfx/walkietalkie.ogg"
                            "Your walkie talkie crackles and your hear Mari's voice on it."
                            mari "Shinobu?"
                            y none "Mari?"
                            mari content "Nanako says you can come in -"
                            nana angry "But not for long!"
                            "Nanako butts in on your conversation."
                        else:
                            "After some time, Mari comes back and shouts across the bridge, not daring to cross it again."
                            mari happy "Nanako says you can come!"
                            y none "Really?"
                            mari content "But only for a little while!"
                        y none "That's better than nothing."
                        hit "Okay ... I'll bring you over."
                        y none "Thanks."

                        $ you_can_cross_bridge = True
                        $ move_to_grid(rm_bathhouse)
                    "Point out logic flaw":
                        y angry "That makes even less sense! Mari could only pretend to get permission - you're doing this all wrong!"
                        show Hitomo scared
                        show Mari angry
                        if (Jun in party or Jun.loc == loc):
                            show Jun lookaway
                        $ Hitomo.wpn.get_sfx()
                        "Hitomo strengthens her aim on you."
                        hit "Y-you're right! Neither of you pass! Stay away, or I'll shoot!"
                        mari "Shinobu!"
                        if (Jun in party or Jun.loc == loc):
                            show Jun angry
                        y angry "... I don't care what's on the other side anymore. Let's go."
                        $ you_can_cross_bridge = False
                        jump grid_loc
            else:
                if len(party) > 0:
                    y none "So what do we have to do to get across?"
                else:
                    y none "So what do I have to do to get across?"
                hit "Nothing ... You don't! It's simple! Just leave us alone, okay!?"
                show Hitomo
                hit "We want to live for a few more days ... We're just being safe, is all! There's nothing on the other side, just a bathhouse!"
                menu:
                    "[[Attack]" if Ai.alive:
                        "She's lying. There's something over there. Something good."
                        $ wpn.get_sfx()
                        if wpn != fist:
                            "You've had enough of this small talk. You reach for your weapon -"
                    "Plead":
                        y sad "I have to talk to everyone. I'm trying to find a way for all of us to go home. Can't you see -"
                        show Hitomo scared
                        hit "No!"
                    "Give up":
                        if Ai.alive:
                            y angry "Fine. Have it your way. If it's just a bathhouse, I'm not really -"
                        else:
                            y angry "Fine. Have it your way. If it's just a bathhouse."
                if Ai.alive:
                    call ai_attacks_hitomo
    jump grid_loc
    

label ai_attacks_hitomo:
    show Hitomo scared
    $ Ai.type = "hostile"
    $ Ai.move(a2)
    play sound "sfx/chainsaw_long.ogg"
    play music "music/AngryOpheliasSong.ogg" fadein 3.0
    "A thundering buzzing sound shatters the atmosphere. It sounds just like a ...!"
    $ reference_item(chainsaw)
    $ add_sanity(-10)
    "A chainsaw!"
    if (Jun in party or Jun.loc == loc):
        show Jun surprised
        jun mad "The hell!?"
        hide Hitomo with dissolve
        "You immediately start running in the opposite direction, yanking on Jun to follow."
        hide Jun with dissolve
    else:
        hide Hitomo with dissolve
        "You break for it, in the opposite direction of the goddamned chainsaw!"
    "You duck behind a tree and pray that you can't be seen."
    hit "W-w-what are you -!? Why are you looking like that!?"
    $ chainsaw.use_sfx()
    "You can hear the chainsaw rev. You quietly mutter for Hitomo to stop being stupid and to run, but from the sound of it, she isn't."
    who "What'd you get?"
    "A feminine voice ... you can't tell who, though."
    $ you_can_cross_bridge = True
    menu:
        "Help Hitomo":
            "Why wasn't that girl running - or shooting, for that matter!?"
            "You curse and wheel out from behind the tree. You have to save her!"
            if (Jun in party or Jun.loc == loc):
                jun mad "The fuck you going!?"
            show Hitomo scared at left with dissolve
            show Ai at right with dissolve
            "You run right back up to the rope bridge and see the chainsaw-wielder standing casually in front of Hitomo more scared than ever. You recognize the girl to be Ai."
            if not Ai.met:
                "A sporty girl who was loud-mouthed in class ... You never liked her."
            y none "Leave her alone!"
            hide Hitomo with dissolve
            show Ai at center with move
            "Your yell disappears in your throat as Ai turns slowly to you. Her face is completely blank, and that frightens you."
            call ai_battle_begin
        "Keep Hidden":
            $ bath_save_mari = True
            "There is a beat of silence, but you can hear Hitomo's frightened breath from where you are."
            play sound "sfx/chainsaw_broken.ogg"
            who "A gun? Sure, I could use a gun."
            play sound "sfx/chainsaw_long.ogg"
            hit "Nn-!!"
            play sound "sfx/scream_girl7.ogg" channel 1
            "Savage screams turn your blood ice cold. Whoever owned that chainsaw was using it. On Hitomo."
            $ Hitomo.kill("murder",Ai)
            
            "And then there was silence."
            "Hitomo ... She's ..."
            "It takes all of the will power you possess to stay completely still and to keep quiet."
            play sound "sfx/bridge_cross.ogg"
            "And then you hear someone walking across the old bridge."
            if Mari in followers:
                "Oh, fuck! Mari!!"
            show Ai with dissolve
            if (Jun in party or Jun.loc == loc):
                "You and Jun come from out of the trees and catch the back of a girl with a chainsaw, leaving the bridge."
            else:
                "You come from out of the trees and catch the back of a girl with her chainsaw, leaving the bridge."
            "You recognize the girl to be Ai."
            if not Ai.met:
                "A sporty girl who was loud-mouthed in class ... You never liked her. Now you hated her more than you could have ever imagined."
            hide Ai with dissolve
            stop music fadeout 5.0
            "The severed corpse of Hitomo is hard to ignore."
            if (Jun in party or Jun.loc == loc):
                $ loc.bodies.remove(Hitomo)
                "Jun has the balls to push the mangled corpse off of the chasm to spare everyone the sight."
            if Mari in followers:
                "Time to save Mari!!"
                $ move_to_grid(a1)
            $ Ai.move(rm_showers)
    jump grid_loc
    
label ai_kill_bridge:
    $ just_murdered_someone = False
    $ you_can_cross_bridge = True
    # Saved Hitomo from Ai!
    $ saved_hitomo = True
    play music "music/FeelingDark_loop.ogg" 
    "Ai's body, still standing, slowly leans backwards and then tumbles down into the chasm, disappearing completely. You try to catch your breath."
    show Hitomo scared with dissolve
    y none "Are ... are you ... okay?"
    
    "Hitomo is still wide-eyed and staring at you like you were Ai."
    y none "What's wrong? I killed her for you!"
    $ Hitomo.wpn.use_sfx()
    play sound "sfx/scream_girl5.ogg"
    "She suddenly squeals and fires her gun at you."
    "You jump up and fortunately her aim missed you completely. But she ... she just tried to shoot you!"
    y none "What's wrong with you!? I just saved your life!!"
    if (Jun in party or Jun.loc == loc):
        jun angry "You gonna attack us now!? Don't be a dope!"
        play sound "sfx/bridge_cross.ogg"
        "Her aim switches between you and Jun rapidly. She backs up on to the rope bridge."
    else:
        play sound "sfx/bridge_cross.ogg"
        "She keeps her shaky aim on you as she walks backwards onto the rope bridge."
    "She trips over the planks and struggles to even stay up as it sways violently from her panicking."
    y none "Be careful! You'll fall if you don't cross it right, Hitomo, {u}please{/u}!"
    play sound "sfx/bridge_cross.ogg"
    y none "I'm not going to hurt you! Why don't you believe me!?"
    hit "M-m-m-murder ... murderers ... death ... blood ..!"
    if (Jun in party or Jun.loc == loc):
        jun scared "She's gone crazy!!"
    else:
        "You think she has completely snapped."
    if (Jun in party or Jun.loc == loc):
        y none "Let us help you ... Please? Please!?"
    else:
        y none "Let me help you ... Please? Please!?"
    play sound "sfx/bridge_cross.ogg"
    "Her foot slips as you expected."
    play sound "sfx/scream_girl4.ogg"
    hide Hitomo with dissolve
    "She hurtles downward with a scream, but she has caught the ropes and is clutching for her life. You waste no time in getting to her, braving the swinging bridge."
    play sound "sfx/scream_girl5.ogg"
    "She continues to scream. You try to reach to pull her up, but one of her hands thrashes at you."
    menu:
        "Let her fall":
            y none "Be that way, if you want to die so much!"
            play sound "sfx/bridge_cross.ogg"
            "You stand up and fall back, nearly falling off yourself."
            if (Jun in party or Jun.loc == loc):
                jun surprised "Pull her up!!"
                "Jun shouts at you back on solid ground. Easier said than done."
            stop music fadeout 4.0
            "You witness Hitomo's grip loosen on the only rope keeping her alive. Her screams turn to sobs, as if begging gravity to reconsider."
            
            play sound "sfx/scream_woman_distant2.ogg"
            "And then her hand is gone and her screams return in full."
            "The swinging of the bridge slowly stops. You swallow."
            $ Hitomo.kill("suicide")
            if (Jun in party or Jun.loc == loc):
                play sound "sfx/bridge_cross.ogg"
                show Jun mad with dissolve
                "And then Jun's heavy weight shifts it again as he stomps up to you."
                jun "The hell, man? She's dead!!"
                y none "Like she wants! You said it yourself, she went crazy!"
                show Jun angry
                "Jun gives you a hard glare."
            if Mari in followers:
                "You shake it off and proceed down the rest of the bridge to find Mari."
            else:
                "You shake it off and proceed down the rest of the bridge."
            $ move_to_grid(a1)
        "Pull her up":
            "You ignore her attempts to keep you away and let her nails claw at your skin as you pull her up onto the bridge once more. She is light, so it is not too difficult, but she is not making it easy for you."
            stop music fadeout 4.0
            show Hitomo with dissolve
            "Back on relative safety and in another human's arms, Hitomo seems to regain some shred of herself as her screaming turns to sobbing. She shakes her head and does not fight you anymore."
            hit "Why why why why ..."
            y none "I'm sorry you had to see what I did, but she was going to kill you, I just know it."
            if (Jun in party or Jun.loc == loc):
                play sound "sfx/bridge_cross.ogg"
                show Hitomo at left with move
                show Jun surprised at right with dissolve
                "The bridge shakes as Jun approaches the two of you."
                jun "Is she all right? Damn, that was a close call."
                show Jun
            y none "Let's go across the bridge to Nanako and Mari, okay?"
            "She manages to nod and you help her stand and cross the rest of the bridge."
            $ just_murdered_someone = False
            scene bathhouse with fade
            $ a1.find()
            "Hitomo leads you up towards a grand building."
            $ Hitomo.move(rm_bathhouse)
            if (Jun in party or Jun.loc == loc):
                $ Jun.move(rm_bathhouse)
            $ move_to_room(rm_bathhouse)
            
    jump grid_loc

label ai_battle_begin:
    # Make her hostile after you encounter her in battle so your followers aren't being unreasonable
    $ Ai.type = "hostile"
    ai "Okita."
    "You gulp from hearing your name called from her lips."
    if loc == rm_showers:
        y none "Kill me, like you killed Hitomo?"
        ai "No, I'll use her weapon this time. Cleaner this way."
        y none "You're sick."
    
    # It shouldn't let you get more than one cheap-shot on her per game. Kind of goofy otherwise
    if not Ai.met:
        if loc != a1:
            ai "What did you get?"
            "You assume she means the weapon you got."
        else:
            ai "And what did you get?"
        if wpn is not None and wpn.type == "gun":
            if ammo_mode:
                $ wpn.use()
            else:
                $ wpn.use_sfx()
            $ Ai.health -= 40
            show Ai yell with dissolve
            $ show_blood()
            "Quicker than she can blink, you whip out your weapon and shoot her. She yelps in pain, but still stands."
            y none "Gun."
            show Ai evil
            "She holds her bleeding wound and cackles deliriously."
        elif wpn is not None and wpn.wpn_range == "ranged":
            $ show_blood()
            $ wpn.use_sfx()
            $ Ai.health -= 25
            show Ai scared
            "As fast as you can, you pull out your weapon and get a hit on her. She staggers and looks at what you just impaled her with."
            show Ai evil
            "A smile seems to form on her demented face."
        else:
            if wpn is not None:
                if wpn != fist:
                    "You pull out your weapon and she stares at you."
                else:
                    "You brandish your fists and she stares at you."
                show Ai smile
                "And then smiles."
    else:
        "She smiles."
    $ Ai.met = True
    if loc == rm_showers:
        $ battle_start(Ai,0,"And then she suddenly charges at you.","ai_kill_bath", False, flee=False, allies_will_help=True)
    elif Hitomo.alive and loc == a2:
        play sound "sfx/chainsaw_long.ogg"
        $ battle_start(Ai,0,"Her chainsaw buzzes to life.","ai_kill_bridge", False, flee=False, allies_will_help=True)
    else:
        play sound "sfx/chainsaw_long.ogg"
        $ battle_start(Ai,0,"Her chainsaw buzzes to life.","murdered_ai", False, allies_will_help=True)

label found_hitomo_dead:
    $ Ai.move(rm_showers)
    if Hitomo.alive:
        $ Hitomo.kill("murder",Ai)
    "You see a grizzly sight upon reaching a rope bridge. A small school girl has been massacred here."
    if not Hitomo.met:
        "You look at her long enough to recognize her to be Hitomo."
    else:
        "Someone got Hitomo."
    "That means that the way across the bridge is clear ... and whoever killed her was probably over there right now."
    $ you_can_cross_bridge = True
    jump grid_loc
    
    
## AI IN BATHHOUSE (Hitomo is dead)
label bathhouse_ai:
    scene bathhouse
    $ cutscene()
    $ Nanako.move(rm_lockers)
    $ Lucy.move(rm_showers)
    if bath_save_mari:
        "You run to the bathhouse but don't immediately find Ai. She's already inside."
    elif seen_hitomo_dead:
        $ Ai.met = True
        "You freeze, seeing the back of a girl by the entrance. Ai? The sporty loud mouth from class ... she's carrying a chainsaw!!"
        "She's the one who killed Hitomo!!"
        "You've got to find whoever is inside of the bathhouse before her!"
    if (Jun in party or Jun.loc == loc):
        show Jun with dissolve
        y none "Stay out here just in case Ai comes back this way."
        jun "Sure, okay."
        $ party_remove(Jun)
    stop ambience fadeout 1.0
    scene onsen with fade
    play music "music/bgs_reverbbells.ogg" noloop
    $ loc = rm_bathhouse
    "You walk through the doors, but everything is eerily quiet. Still no sight of Ai - or anyone else for that matter. What was Hitomo protecting?"
    "There are two doors in front of you. The mens' locker room on the left, and the womens' locker room on the right."
    play sound "sfx/sound_left2.ogg" channel 1
    menu:
        "Mens' Locker Room":
            $ Nanako.met = True
            $ Lucy.met = True
            $ loc = rm_lockers
            $ Ai.wpn = glock
            $ Ai.item = [chainsaw,1]
            play sound "sfx/door.ogg"
            play ambience "sfx/room_tone1.ogg" fadein 4.0
            scene lockers_men with fade
            "You burst into the mens' locker room, but don't see anyone at all. You realize that there is a door across the room. It must lead to the wash room."
            play sound "sfx/door_slide.ogg"
            stop ambience fadeout 2.0
            scene black with dissolve
            "You slide the door quietly and creep inside."
            $ loc = rm_showers
            play ambience "sfx/dripping.ogg"
            scene showers with dissolve
            "You find Ai standing near the communal bath, her back to you."
            play music "music/FeelingDark_loop.ogg"
            $ reference_item(glock)
            $ glock.get_sfx()
            show Ai angry with quickdissolve
            "But not for long. She whips around and points Hitomo's gun at you."
            show Ai evil
            "She takes a moment to recognize you and smirks."
            call ai_battle_begin
            
            
        "Womens' Locker Room":
            play sound "sfx/door.ogg" channel 1
            $ Nanako.met = True
            $ Lucy.met = True
            scene lockers_ladies with fade
            $ loc = rm_lockers
            play sound "sfx/scream_girl7.ogg"
            if Mari.loc == loc and Mari.alive:
                $ group_name = "Mari and Nanako"
                $ group_ref = "them"
                $ group_ref2 = "they're"
                show Mari scared at left
                show Nanako scared at right
                with dissolve
            else:
                $ group_name = "Nanako"
                $ group_ref = "she"
                $ group_ref2 = "she's"
                show Nanako scared with dissolve
            "You burst through the ladies' room and hear squealing."
            "Your skin crawls until you see that it's only %(group_name)s, the fashion clique Queen of the class, alone and unharmed."
            y scared "Shh, shh, shh!"
            show Nanako angry
            "You hush %(group_ref)s but %(group_ref2)s confused. Nanako gives you a look, as if you dared to order her around. It looks like she doesn't have any weapon, so that seems to be the only reason she complies."
            y scared "Someone's -"
            play ambience "sfx/sanity4.ogg" fadein 4.0
            show Nanako scared
            play sound "sfx/sound_right2.ogg"
            "Another noise, in the hallway you just came from. You panic."
            y scared "Hide!!"
            "You point to the lockers as hard as you can, demanding %(group_name)s get inside of them if they want to live."
            hide Nanako
            hide Mari
            show locker open
            with dissolve
            play sound "sfx/metal2.ogg"
            "You crawl inside one yourself just after making sure %(group_ref2)s safely inside, too."
            "Your hand freezes as you reach out to close the door when someone rushes into the room."
            stop ambience
            play sound "sfx/accent_stab.ogg"
            show Lucy behind locker with quickdissolve
            $ Lucy.move(rm_lockers)
            "The person turns out to be Lucy, a girl from Nanako's clique. You're relieved."
            lucy "Nanako, I found something cool in the other room!"
            show Lucy sad
            lucy "Nanako?"
            $ glock.use_sfx()
            $ show_blood()
            $ Ai.move(rm_lockers)
            $ Lucy.kill("murder",Ai,drop_loot=True)
            hide Lucy with quickdissolve
            play music "music/FeelingDark_loop.ogg"
            $ renpy.pause(0.5)
            play sound "sfx/gun_empty.ogg"
            "Her head slams forward and her pigtails disappear. Lucy's body barely has time to fall to the floor before another bullet pierces her back."
            show Ai behind locker with dissolve
            "When she does fall, Ai casually strides in, rapidly pulling the trigger of Hitomo's gun at Lucy's corpse, but it only clicks for her."
            show Ai angry
            ai "Tsk."
            play ambience "sfx/sanity3.ogg" fadein 5.0
            "Your locker door is still wide open, but Ai hasn't seen you yet. You're so afraid, you start to see spots."
            $ glock.get_sfx()
            "While Ai is busy putting new ammo into the gun, you try to close the door as quietly as you can."
            play sound "sfx/metal2.ogg"
            show Ai scared
            show locker with dissolve
            "The metal of the door dings as it touches the frame. You cringe like never before."
            show Ai angry
            $ add_sanity(-15)
            play ambience "sfx/sanity4.ogg" fadeout 1.0 fadein 3.0
            "Ai hears the sound, and walks in your lockers' direction. She's onto you. You're hyperventilating."
            show Ai scared
            "Before she gets all the way to your area, muffled cries catch her attention instead. No!"
            hide Ai with dissolve
            play sound "sfx/gun_empty.ogg"
            play sound "sfx/scream_girl2.ogg" channel 1
            "Ai turns towards the other set of lockers and starts shooting at random lockers! You can distinctly hear the screams of %(group_name)s! Your stomach wrenches."
            stop ambience fadeout 4.0
            play sound "sfx/button.ogg"
            play sound "sfx/bodyfall.ogg" channel 1
            stop music fadeout 6.0
            hide locker with dissolve
            "You spring out of your locker and tackle Ai. You both fall to the floor and the gun flies from her hand."
            "You wrestle her on the floor, wrapping your arm around her neck. You increase pressure until Ai's groaning completely stops."
            if rope.is_in_inventory():
                menu:
                    "Kill Her":
                        $ dealt_ai = "dead"
                    "Tie Her Up":
                        $ dealt_ai = "tied"
            else:
                $ dealt_ai = "dead"
            if dealt_ai == "dead":
                "Eventually, Ai's flailing dies down, too."
                $ Ai.kill("murder",you,drop_loot=True)
                "She goes lifeless. Your fevered breathing is mixed with weeping from the lockers."
                play sound "sfx/metal2.ogg"
                "You drop Ai's corpse and immediately open the lockers to find %(group_name)s."
            else:
                $ rope.use_sfx()
                $ rope.destroy(1)
                $ Ai.type = "fixed"
                $ Ai.hidden = True
                "You take out your rope and tie her up."
                "Hopefully, this will put a stop to her rampage. You don't care what happens to her next."
            show Nanako scared with dissolve
            play sound "sfx/bodyfall.ogg"
            "Nanako falls out of her locker in an emotional mess, but she's at least alive."
            if Mari.loc == loc and Mari.alive:
                hide Nanako with dissolve
                play sound "sfx/door_squeak.ogg"
                if wish_safety_mari:
                    show Mari sad with dissolve
                    "Mari squeaks when you open her door, but when she finds it's you, she bolts out and wraps her arms around you and sobs."
                    "You hold her for a long moment."
                    y none "Nothing is going to happen to you. I'm here. I'm here."
                    hide Mari with dissolve
                    "Nanako mourns over Lucy, and seeing Hitomo's gun, her as well."
                else:
                    play music "music/Reynardine.ogg"
                    "You immediately spring up and find Mari's locker. She's curled up inside, not moving. You reach in and pull her out. Her shivering tells you that she is alive."
                    show Mari sad with dissolve
                    $ add_sanity(-10, silent=True)
                    "But Mari is covered in blood. She's holding a bleeding wound on her stomach."
                    y sad "Mari, no ..."
                    if you in Mari.enemies:
                        show Mari angry
                        mari "Don't, don't ... touch me ..."
                        "She still hasn't forgiven you, it seems."
                        $ Mari.kill("murder",Ai,drop_loot=True)
                        hide Mari with dissolve
                        $ add_sanity(-20, silent=True)
                        "She goes limp in your arms."
                        "She succumbed to her wounds, and Mari is now dead ... You can hardly believe it."
                    else:
                        mari sad "I ... I'm ..."
                        y sad "Shh, no, you're going to be okay."
                        "Her shaking intensifies."
                        nana "M-Mari?"
                        mari "Go home ... Go home ... for me ..."
                        "She grips your hands, covering them in blood."
                        if not firstaid.is_in_inventory() and not medkit.is_in_inventory():
                            y scared"No ... Mari, no ..."
                            show Mari content
                            "She smiles for you one last time. You cry."
                            y scared "Mari!!"
                            $ Mari.kill("murder",Ai,drop_loot=True)
                            hide Mari with dissolve
                            $ add_sanity(-20, silent=True)
                            "She goes limp in your arms."
                            "You cannot believe it. You won't believe it. But ... Mari is {u}dead{/u}."
                            "You press your head onto her body and weep while Nanako mourns for Lucy and Hitomo."
                        else:
                            y none "Don't talk like that!"
                            hide Mari with dissolve
                            if firstaid.is_in_inventory():
                                "You pull out your first aid kit and immediately start to work on Mari's wound. She wasn't going to die - not if you had anything to say about it."
                                $ firstaid.use_sfx()
                                $ Mari.health = 100
                                $ Mari.sanity = 100
                                $ firstaid.destroy(1)
                            elif medkit.is_in_inventory():
                                "You pull out your medical kit and immediately start to work on Mari's wound. She wasn't going to die - not if you had anything to say about it."
                                $ medkit.use_sfx()
                                $ Mari.health = 100
                                $ Mari.sanity = 100
                                $ medkit.destroy(1)
                            "You clean and dress her wound. It's pretty bad, but you got the bullet out of her, and now all she needed was time in completely recovering."
                            $ add_sanity(5)
                            "You were going to get her off of this island if it was the last thing you did ... The literalness struck you, but you swallowed that down and ignored it."
                
            else:
                y sad "Are you all right?"
                show Nanako sad
                nana "Lucy ..."
                y sad "I'm sorry, but ... Hitomo, too."
                nana "No ... no!"
                hide Nanako with dissolve
                "Nanako needs a moment to recover after hearing the news. They were her closest friends."
            "It takes you a very long time to recover from what just transpired. Nanako makes her peace and closes Lucy's eyes."
            y none "How are you?"
            show Nanako sad with dissolve
            $ reference_item(bulletproof)
            "Nanako touches her chest and lifts her shirt to reveal a dark, bulky material underneath."
            nana "Bullet-proof vest."
            "So, that's how she survived and why she has no weapon."
            if Jun in followers:
                $ Jun.move(rm_lockers)
                $ party_add(Jun)
                show Jun scared at right with dissolve
                "Jun walks into the room, startling you - with good reason."
                jun "Holy fuck ..."
                if Mari.loc == loc:
                    jun "Is ... Mari ...?"
                    if not Mari.alive:
                        show Jun sad
                        $ Jun.sanity -= 10
                        "You nod, trying not to go weak again. Jun is speechless. The heaviness of this game might have just hit him."
                    else:
                        $ party_add(Mari)
                        y happy "She's going to be all right."
                show Jun sad at right with move
                show Nanako at left with move
            "You stand up and Nanako joins you."
            y none "Are you going to stay here?"
            nana "I don't know ... maybe."
            y none "You can come with me."
            nana "No. I don't need you. I'll do fine on my own."
            y scared "You're really going to say that after what happened!?"
            nana "I'm ..."
            nana "I don't want to leave. I'm scared. Please. Just leave me alone and don't tell anyone where you found me, please."
            "She wasn't leaving you much choice."
            y sad "If that's what you want."
            if (Jun in party or Jun.loc == loc):
                show Jun
                jun "You're just going to die if you say here."
                show Nanako angry
                nana "Everything was fine until you assholes came along!!"
                "She was clearly still upset about the death of her friends, so you tug on Jun's arm so he won't push her any further."
            else:
                $ Nanako.make_friend(you)
            stop music fadeout 4.0
            if (Mari in party or Mari.loc == loc) and Mari.alive:
                $ party_add(Mari)
                "You help Mari to stand and walk."
            $ loc = rm_lockers
            jump room_loc
                
                
                
label ai_kill_bath:
    play sound "sfx/swim.ogg" fadein 4.0
    play music "music/ALongDay.ogg" fadein 6.0
    "Ai falls backwards into the bath."
    $ Ai.unkill("murder",you)
    
    "She thrashes! She's not dead! She still has a shred of life in her."
    if rope.is_in_inventory():
        menu:
            "Kill Her":
                $ dealt_ai = "dead"
            "Tie Her Up":
                $ dealt_ai = "tied"
    else:
        $ dealt_ai = "dead"
    if dealt_ai == "dead":
        "You run up to her and your hands find her neck. You press firmly, if you do not strangle her, she will at least drown."
        $ Ai.kill("murder",you)
        "Eventually, one or the other happens, and Ai is rendered lifeless. Her body begins to float in the water."
        "You back away, the front of your shirt soaked."
        $ just_murdered_someone = False
    else:
        "You grab a heavy wooden stool near you and wait for Ai to lift her head from the water."
        "You wallop the back of her skull and she stops moving. You hope you haven't killed her as you pull her from the water so she doesn't drown."
        $ rope.use_sfx()
        $ rope.destroy(1)
        $ Ai.type = "fixed"
        $ Ai.hidden = True
        "You take out your rope and tie her up."
    $ bow.get_sfx()
    "???" "Put your hands where I can see them!!"
    $ reference_item(bow)
    show Lucy sad at right
    show Nanako angry at left
    with dissolve
    "You lock up and turn around with your hands held high. You see Lucy, a normally peppy girl, aiming a bow and arrow at you and Nanako sticking her head out of the female locker rooms' door."
    if who_has_arrows:
        "Bow and arrow? Wait, was it Lucy that killed Tetsuo - and nearly you, too!?"
    if Mari.loc == rm_lockers and Mari.alive:
        show Mari scared behind Nanako with dissolve
        if you in Mari.enemies:
            "You swear you see Mari next to Nanako, but she does nothing to defend you."
            call nana_bath_mari_betray
        else:
            mari "Wait! No, he's a friend!"
            $ party_add(Mari)
            "Mari jumps out of the locker room and up to Lucy."
            show Mari sad
            mari "He's the guy I was talking about."
            show Lucy scared
            if dealt_ai == "dead":
                nana "You were talking about {u}him{/u}? He just killed Ai!"
            else:
                nana "You meant this loser? He just hog-tied that sports girl!"
            nana "What was Ai doing here!?"
            show Lucy sad
    y scared "Listen to me!"
    if Mari.loc == rm_lockers and Mari.alive:
        show Mari scared
    y scared "She killed Hitomo! She was coming here to kill you, too! I was trying to save you!"
    show Lucy scared
    lucy "Hi ... tomo?"
    show Nanako
    if Mari.loc == rm_lockers and Mari.alive:
        show Mari sad
    show Lucy sad
    "Lucy lowers her bow as grief swamps her, tears forming in her eyes. Nanako goes silent as well."
    if (Mari in party or Mari.loc == loc):
        mari scared "Oh no ... She's really ...?"
    if (Jun in followers):
        # Get him back in our party
        $ Jun.move(rm_lockers)
        $ party_add(Jun)
    if (Jun in party or Jun.loc == loc):
        if (Mari in party or Mari.loc == loc):
            show Jun at Position(xcenter=0.1) behind Lucy with dissolve
        else:
            show Jun behind Lucy with dissolve
        show Lucy scared
        "Someone runs into the room. It's Jun. Lucy raises her bow at him, and he freezes."
        show Jun sad
        jun "Whoa, whoa -"
        show Nanako scared
        nana "It's that gang member!! Shoot, shoot!"
        show Jun scared
        if (Mari in party or Mari.loc == loc):
            show Mari scared
            mari "No!!"
        else:
            y scared "No! He's good!"
        $ bow.use_sfx()
        show Lucy sad
        show Jun scared
        
        "Fortunately, Lucy's aim and upper-arm strength are terrible. The arrow limps out of her bow and lands only a meter away."
        jun "You were going to kill me with that thing!?"
        y scared "Don't! Stop! He's on our side!"
        show Jun angry
        if (Mari in party or Mari.loc == loc):
            show Mari sad
    hide Lucy with dissolve
    
    stop music fadeout 5.0
    "Lucy finally looses it and starts bawling, crumpling to the floor. Hitomo's loss and the weight of the game are taking their toll."
    hide Nanako with dissolve
    "Nanako rushes over and comforts her."
    if (Mari in party or Mari.loc == loc):
        mari "But ... she was just there ..."
    y sad "I came here to stop Ai - to stop her madness. I don't want to kill anyone else."
    "They are too distraught to listen to you anymore."
    show Lucy sad at right
    show Nanako angry at left
    with dissolve
    "After they cry for a long time, they stand up to address you."
    if (Jun in party or Jun.loc == loc):
        show Jun
    nana "Get out of here! We were fine until you came!"
    y angry "I just saved your life!"
    "Lucy wailed loudly."
    nana "Get out!!"
    menu:
        "Plead for her to come with you":
            y sad "Don't stay here! Come with me! I'll protect you!"
            nana "And go out there with the rest of these maniacs!? Are you stupid!?"
            y sad "Not everyone is like Ai. A lot of people aren't playing, just like me."
            nana "So? There's still idiots who are. I'm safer here, but only if you leave and never come back."
            if (Jun in party or Jun.loc == loc):
                jun "Never? What if we need you? Or what if we wanted to save you!?"
                nana "Yeah right! Dream on."
                nana "There's only one person who can save us, and he's totally not any of you."
            if (Mari in party or Mari.loc == loc):
                mari "Nanako -"
                nana "Save it! I'm not stepping foot outside of this bathhouse!"
            y angry "Fine. I don't have time for this."
            y none "But if I can save you, I will. That's a promise."
            show Nanako
            "Nanako's eyes waver, but you turn away to leave her as she wished."
        "Leave":
            y"Fine. Suit yourself."
            "You leave her. She's clearly delusional."
    scene black with dissolve
    $ move_to_grid(a1)
    jump grid_loc
        
label ai_revenge_kill:
    $ ai_killer = None
    if Nanako.alive:
        $ Nanako.sanity -= 25
        $ ai_killer = Nanako
    if Lucy.alive:
        $ Lucy.sanity -= 25
        $ ai_killer = Lucy
    $ cutscene()
    # If you tied Ai up, they just execute her offscreen.
    if ai_killer != None:
        $ Ai.kill("murder", ai_killer)
    # Otherwise she bites her own tongue
    else:
        $ Ai.kill("suicide")
    "You have a sinking feeling."
    "You check your stats page, and realize Ai is dead."
    if ai_killer != None:
        y "I-Is this revenge?"
        if (Jun in party or Jun.loc == loc):
            jun "Ugh. Can't say she didn't have it coming."
        if (Mari in party or Mari.loc == loc):
            mari "Oh, no... No no no."
    else:
        y "...She... took her own life."
        if (Jun in party or Jun.loc == loc):
            jun "Jesus! Why was she that obsessed with the game!?"
        if (Mari in party or Mari.loc == loc):
            mari "No! Why..!? I thought we could reason with her!"
            y "I... guess not."
    y "At least Ai's rampage is now over."
    return

                
label nana_bath_mari_betray:
    if Mari.loc == loc:
        nana "So, here he is! Mari's told us a lot about you, you sick freak."
        y scared "Mari! Please, tell them I'm okay!"
        "Mari retreats back into the room and slides the door shut. She's left you with these two hostile women."
    menu:
        "[[Attack]":
            "If they were going to be that way, so be it."
            $ battle_start(Lucy,3,"You went right for Lucy.","bath_kill_lucy", True, flee=False)
        "Persuade Nanako":
            "There had to be a way to convince them you were safe."
            y sad "It's true, what Mari told you, but you have to let me explain."
            nana "Ugh, no! Get out, right now!"
            y scared "No! You have to hear me out!"
            lucy "Leave!!"
            y none "Why should I!?"
            nana "Because -"
            $ Lucy.wpn.use_sfx()
            $ show_blood()
            if wish_safety_you:
                $ damage_you(-10)
            else:
                $ damage_you(-20)
            "An arrow suddenly pierces you. Lucy looks surprised, as if it slipped her hand by mistake. But here it is. An arrow in you."
            nana "D-d-don't just stand there, finish him off!!"
            $ battle_start(Lucy,3,"Lucy struggles with another arrow. It's either kill or be killed now.","bath_kill_lucy", True, flee=False)
            
label bath_kill_lucy:
    show Nanako scared
    "Lucy is a corpse now."
    nana "Oh my god!! You're a freak! No!! Stay away from me!!"
    "Nanako scrambles backwards and tries to escape. She is weaponless."
    play sound "sfx/door_slide2.ogg"
    hide Nanako with dissolve
    "She slides open the door and slams it shut. You chase after her."
    
    if Mari.loc == loc:
        scene lockers_ladies with fade
        $ loc = rm_lockers
        show Nanako scared at mid_right
        show Mari scared at mid_left
        with dissolve
        "Inside, Mari spins around and stands in front of Nanako, her arms out."
        show Mari angry
        mari "You want her? You have to go through me."
        "You swallow, considering the proposal. You didn't want to kill Mari. You really didn't."
        mari "Leave us. Please. Just leave us alone."
        menu:
            "[[Attack]":
                $ wpn.get_sfx()
                show Mari scared
                if wpn != fist:
                    "You raise your weapon. Mari tenses and her mouth parts. Nanako whimpers."
                y none "If that's the way it has to be."
                show Mari angry
                mari "I thought you were better than this."
                mari "I thought you were different ..."
                y evil "I thought so, too."
                $ battle_start(Mari,0,"Her eyes lose their strength.","bath_kill_mari", False, flee=False)
            "Leave":
                "She gave you your pass to leave, and you know to take it. If people were going to die in the game, you wanted to at least be confident in the fact that it wasn't your fault."
                "For some of them, anyway."
                "You silently turn to leave."
                "You will not be welcome in the bath house from here on."
                $ Mari.make_foe(you)
                $ Hitomo.make_foe(you)
                $ Nanako.make_foe(you)
                $ Lucy.make_foe(you)
                $ mari_bath_left = True
    else:
        jump bath_kill_mari

label bath_kill_mari:
    if Mari.loc == loc:
        "Blood pours from Mari too easily ... You can't bear to look. You feel shame like none other before."
        show Nanako scared at center with move
    else:
        show Nanako scared with dissolve
    "Nanako's sporadic moments and high-pitched scream grab your attention. Just one more to deal with ... and she was defenseless."
    show Nanako angry
    nana "You're burning in hell, I hope you know, you goddamned bastard!!"
    if wpn.type == "gun":
        $ wpn.use_sfx()
        $ Nanako.health -= 15
        show Nanako scared
        hide Nanako with dissolve
        "You shoot her without a word. She staggers back ... and then rises with a loud groan."
        show Nanako angry with dissolve
        "Your shot was mortal ... How is she still alive?"
        nana "You destroyed my top ... Oh, you're fucking {u}evil{/u}!"
        $ reference_item(Nanako.item[0])
        "She pulls at her ripped blouse and reveals a dark, heavy padding underneath. She has a bullet-proof vest!"
        $ battle_start(Nanako,0,"Too bad for her, it won't be enough to save her.","bath_kill_nanako", True, flee=False)
    else:
        $ battle_start(Nanako,0,"Hell sounds nice right about now.","bath_kill_nanako", True, flee=False)
    
label bath_kill_nanako:
    "The bodies of many of your classmates are strewn across the floor of the public bath house. You regret some of them ... others, not so much."
    "You're just one step closer to getting off this island, as far as you're concerned."
    jump grid_loc
    
    
    
    
#BATHHOUSE, NANAKO, LUCY
label bath_no_ai:
    $ cutscene()
    $ Lucy.met = True
    $ Nanako.met = True
    $ Lucy.move(rm_lockers)
    $ Nanako.move(rm_lockers)
    #You arrive at the Bathouse.
    "You walk into a rustic bathhouse that likely served the entire island at one point."
    if Hitomo.alive:
        #- If you are with Hitomo, she will lead you to Nanako and Lucy (and Mari).
        hit "This way, follow me."
        scene lockers_ladies with fade
        $ Hitomo.move(rm_lockers)
        if (Jun in party or Jun.loc == loc):
            $ Jun.move(rm_lockers)
        $ loc = rm_lockers
        "Hitomo heads for the women's locker room."
        if Mari.loc == loc:
            show Hitomo at farleft
            show Lucy at farright
            show Mari at mid_left
            show Nanako at mid_right
            with dissolve
        else:
            show Hitomo at left
            show Lucy at right
            show Nanako at center
            with dissolve
        "The girls inside are jumpy, but they relax upon seeing Hitomo."
        if Mari.loc == loc:
            mari "Here he is."
        if saved_hitomo:
            nana "Hitomo. What are you doing here?"
            if Mari.loc != loc:
                nana "... With that guy, no less!?"
            else:
                nana "You should have waited for my permission!"
            hit "He ... He saved my life!"
            lucy "You did?"
            if Mari.loc == loc:
                mari "What happened!?"
            y sad "Ai came out of nowhere ... She wanted her dead."
            nana "Ai ...?"
        if (Jun in party or Jun.loc == loc):
            lucy "But ... what about him?"
            "Lucy points at Jun."
            if Mari.loc == loc:
                mari "Jun is on our side."
            y none "He's cool, too."
            jun "Hey."
            "The girls seem pretty scared of him, but you know there's nothing to worry about."
        call meeting_nanako_lucy
    else:
        #- If you are NOT with Hitomo (she's dead), you will walk into an empty room and eventually get shot at by a bow and arrow. You turn around and see Lucy aimed at you. You have the option to talk to her, or attack her.
        scene lockers_men with fade
        if (Jun in party or Jun.loc == loc):
            $ Jun.move(rm_lockers)
        $ loc = rm_lockers
        "You are not sure where to go, so you walk into the men's locker room. It's empty. There must be only women here."
        "You laugh to yourself, wondering if your classmates would still respect gender boundaries, even at the end of times."
        $ Lucy.wpn.use_sfx()
        "You don't get to enjoy the thought for long. An arrow whizzes past your head."
        show Lucy scared with dissolve
        lucy "You're not supposed to be here!"
        $ reference_item(Lucy.wpn)
        "You see Lucy, the half-American girl with a bow and arrow aimed at you. You're not too sure she actually knows how to use that thing."
        # If you saved Hitomo from Ai, but let her fall down the bridge.
        if saved_hitomo and (Mari in party or Mari.loc == loc):
            mari scared "Don't shoot! That's the guy I told you about!"
            lucy "I-Isn't Hitomo supposed to be with them!?"
            y none "Ai attacked us. We fought her off, but Hitomo..."
            if (Jun in party or Jun.loc == loc):
                jun lookaway "She uh... lost her footing and fell down the bridge."
            else:
                y none "She fell."
            show Lucy scared
            "Lucy gasped."
            if (Mari in party or Mari.loc == loc):
                "Mari covers her mouth and stares at you."
                if (Jun in party or Jun.loc == loc):
                    "Jun looks away."
            lucy "I have to tell Nana! Oh my god, Nana!!"
            if Mari.loc == loc:
                show Mari at left
                show Lucy sad at right
                show Nanako at center
                with dissolve
            else:
                show Lucy sad at left
                show Nanako at right
                with dissolve
            "Nanako rushes in through the shower doors. She gasps."
            lucy "Hitomo! He says that she... She fell!!"
            nana "No... No!!"
            show Lucy sad
            "Lucy silently sobs to herself."
            scene black with dissolve
            call meeting_nanako_lucy
        menu:
            "[[Attack]":
                #-- Killing her will disgust Jun, and he will leave. You go and find Mari/Nanako in the other room.
                $ battle_start(Lucy,0,"You're pretty sure you can take her.", "no_hitomo_lucy_dead2", True, flee=False)
            "Surrender":
                #-- If you talk to her, Mari/Nanako will walk in and see what's happening. 
                if (Mari in party or Mari.loc == loc):
                    #If mari is there, Mari will talk her down from shooting.
                    mari "Lucy! We're friends!"
                    lucy "Mari? What are you doing with ... him?"
                    mari "He's helped me. We're looking for a way off the island!"
                    lucy "But ... why did Hitomo let you over here?"
                    if not Hitomo.met:
                        y none "Hitomo?"
                        mari "No one stopped us ..."
                        show Lucy scared
                        "Lucy gasped."
                    else:
                        y sad "She was ... she was ..."
                        lucy "Oh no, oh no ..."
                        y sad "She's dead."
                        show Lucy scared
                        "Lucy's mouth drops and her bow lowers."
                else:
                    #Else, Nanako tells Lucy to kill you.
                    y none "You got me. I was just poking around."
                    show Lucy sad
                    lucy "Hitomo should have stopped you! Why didn't she?"
                    if not Hitomo.met:
                        y none "Who?"
                        lucy "Hitomo ... You didn't meet her?"
                        y none "Nope."
                    else:
                        y sad "She was ... she was ..."
                        lucy "Oh no, oh no ..."
                        y sad "She's dead."
                        
                    show Lucy scared
                    "Lucy's mouth drops and her bow lowers."
                lucy "I have to tell Nana! Oh my god, Nana!!"
                show Lucy scared at left with move
                show Nanako scared at right with dissolve
                "Nanako rushes in through the shower doors. She gasps."
                if not (Mari in party or Mari.loc == loc):
                    nana "Shoot him, hurry!"
                    lucy "But - Hitomo! He says that she wasn't out there!"
                    show Nanako angry
                    nana "Because he killed her!"
                    if you in Mari.enemies:
                        nana "Mari told me! He's evil!"
                    else:
                        y angry "Why are you just assuming that?"
                    show Lucy sad
                    lucy "How could you!? She's the most sweetest girl ever!"
                    $ Lucy.wpn.get_sfx()
                    $ battle_start(Lucy,0,"Lucy loads her bow while choking on tears.", "no_hitomo_lucy_dead", True, flee=False)
                else:
                    nana "What did you say?!"
                    lucy "Hitomo wasn't out there!"
                    mari "Do you think ...?"
                    show Nanako angry
                    nana "Yes. Someone got her. Those bastards."
                    show Lucy sad
                    "Lucy silently sobs to herself."
                    scene black with dissolve
                    call meeting_nanako_lucy
    jump grid_loc
                
label no_hitomo_lucy_dead:
    if Mari.loc == rm_lockers:
        jump bath_kill_lucy
    show Nanako scared
    nana "Lucy!!"
    "You turn your icy glare to Nanako."
    hide Nanako with dissolve
    "Nanako slips back into the shower room and closes the door."
    $ loc = rm_showers
    scene showers with fade
    "You follow."
    $ Nanako.make_foe(you)
    $ Nanako.move(rm_showers)
    jump room_loc
    
label no_hitomo_lucy_dead2:
    "Nanako bursts through the shower doors just as Lucy falls to the ground."
    jump no_hitomo_lucy_dead

label meeting_nanako_lucy:
    scene lockers_ladies with fade
    if Hitomo.alive and Hitomo.loc == loc:
        if Mari.loc == loc:
            show Hitomo at farleft
            show Lucy at farright
            show Mari at mid_left
            show Nanako at mid_right
            with dissolve
        else:
            show Hitomo at left
            show Lucy at right
            show Nanako at center
            with dissolve
    else:
        if Mari.loc == loc:
            show Mari at left
            show Lucy sad at right
            show Nanako at center
            with dissolve
        else:
            show Lucy sad at left
            show Nanako at right
            with dissolve
    #-- Nanako will say who and why they're hiding in the bathhouse, and that they are welcome to stay, but if they agree she's the leader in charge.
    #-- If you have seen Tetsuo killed with arrows, you will see that Lucy also has arrows.
    if who_has_arrows:
        call lucy_arrows_conflict
    y none "How are you holding up in here?"
    if Hitomo.alive:
        lucy "It's good. There's clean water and we can keep clean."
        if Hitomo.loc == loc:
            hit "The forest is so icky."
        nana "I feel safe here. It's so normal in here ... I can't explain it."
        lucy "The vending machine had barely anything in it, but we're managing."
    else:
        lucy "I... I miss her."
        y none "O-Oh... I meant..."
    nana "We can't feed any more people, so don't even think about it."
    y none "Well ... Maybe not us, but if we find other survivors, can't we send them here?"
    nana "No! This place is only safe because it's just us here. We can't trust others - we can't even trust you!"
    if Mari.loc == loc:
        mari "But -?"
    nana "I'm sorry, but you're not allowed to stay here either."
    if Hitomo.alive and Hitomo.loc == loc:
        hit "Nana ..."
        nana "So, he saved you? That could just be a trick."
        y angry "It's not."
    y none "I'm not here to trick you people. I want to go home and I want everyone else to go home, too."
    lucy "Maybe they can just take a short rest here?"
    nana "I don't like that."
    nana "Take care of business and get out."
    "Nanako wasn't very welcoming."

    # Add Mari back into your party if she isn't already
    if Mari.loc == loc and Mari in followers and Mari not in party:
        $ party_add(Mari)
    jump room_loc
    
label lucy_arrows_conflict:
    $ reference_item(Lucy.wpn)
    "You notice that Lucy has a bow and some arrows. You instantly tense."
    "Did she kill Tetsuo? ... And almost you?"
    menu:
        "Call her out as a murderer":
            call lucy_accuse
        "[[Attack]":
            $ Lucy.make_foe(you)
            $ Nanako.make_foe(you)
            $ Hitomo.make_foe(you)
            $ battle_start(Lucy,3,"You leave her no time to betray you!", "no_hitomo_lucy_dead", True, flee=False)
        "Ask about Lucy's bow":
            y sad "Is that your bow?"
            lucy "Um ... yeah?"
            y sad "So no one else has used it but you?"
            lucy "No, it's mine. I found it in my bag. Why?"
            menu:
                "[[Attack]":
                    $ Lucy.make_foe(you)
                    $ Nanako.make_foe(you)
                    $ Hitomo.make_foe(you)
                    $ battle_start(Lucy,3,"Lucy fumbles with her arrows.", "murdered_lucy", True, flee=False)
                "Call her out as a murderer":
                    call lucy_accuse
                "Ignore it, for now":
                    "You grit your teeth. Jumping to conclusions isn't smart right now."
                    y none "Nothing."
                    "Lucy looks at you weird."
        "Say Nothing":
            "You grit your teeth. Jumping to conclusions isn't smart right now."
    return
    
label lucy_accuse:
    y angry "It was you!"
    lucy "Me? What?"
    if Tetsuo.murderer == Yoriko:
        y angry "You killed Tetsuo!"
    else:
        y angry "You tried to kill me!"
    nana "Excuse you? Lucy's been with me here since the beginning."
    lucy "Yeah! What's your deal!?"
    y angry "I saw the arrows fly at my head!"
    nana "She's been with me!"
    y  angry"The whole time!? Not a minute out of your sight!?"
    nana "Well - no -"
    "Nanako looks over at Lucy and she shakes her head frantically."
    lucy "I would never!! You know me!"
    nana "Where were you this morning?"
    if Hitomo.alive and Hitomo.loc == loc:
        hit "Lucy ...?"
    lucy "I was ... I was just outside! Wandering around!"
    y angry "Or murdering people!"
    lucy "No!! Nana, you have to believe me!"
    nana "Damn it! Okita, you asshole! Don't come here and try to mess with our minds!"
    nana "Lucy is my friend and I trust her!"
    if len(party) > 0:
        nana "Take your entourage and get out of here!"
    else:
        nana "Get out of here and don't come back!"
    nana "If you come here, we'll kill you! You hear me!? Get out!"
    $ Lucy.make_foe(you)
    $ Nanako.make_foe(you)
    $ Hitomo.make_foe(you)
    menu:
        "[[Attack]":
            $ battle_start(Lucy,3,"If this is how they want it to be, so be it!", "no_hitomo_lucy_dead", True, flee=False)
        "Leave":
            y angry "Fine. Don't be surprised when she murders you, too."
            nana "Now!"
            "You leave the bathhouse."
            $ move_to_grid(a1)
    
# #School house, EMI
label school_emi_intro:
    $ cutscene()
    # You enter the school house and immediately hear someone run away in a nearby room. Thus starts a mini-maze where you have to follow the sounds to find Emi.
    stop ambience fadeout 3.0
    play sound "sfx/sound_left1.ogg"
    "As soon as you step into the school, you hear the footsteps of someone running away from you."
    if (Jun in party or Jun.loc == loc):
        jun "Who was that?"
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        y none "Let's find them."
    play sound "sfx/sound_left2.ogg"
    "Which way did they go?"
    menu:
        "Leave":
            "You can't deal with this right now."
            $ loc = b4
            jump grid_loc
        "{image=gui/west.png} Go Left {image=gui/west.png}": #correct
            scene corridor with fade
            play sound "sfx/sound_right1.ogg"
            "The fleeing student squeals a little. It's a girl."
            menu:
                "{image=gui/west.png} Go Left {image=gui/west.png}":
                    pass
                "{image=gui/east.png} Go Right {image=gui/east.png}": #correct
                    scene corridor with fade
                    play sound "sfx/sound_right2.ogg"
                    "This school is like a maze! Which way did she go?"
                    menu:
                        "{image=gui/west.png} Go Left {image=gui/west.png}":
                            pass
                        "{image=gui/east.png} Go Right {image=gui/east.png}": #correct
                            scene corridor with fade
                            play sound "sfx/sound_front2.ogg"
                            "You're close. You almost have her."
                            menu:
                                "{image=gui/west.png} Go Left {image=gui/west.png}":
                                    pass
                                "{image=gui/east.png} Go Right {image=gui/east.png}":
                                    pass
                                "{image=gui/north.png} Go Straight {image=gui/north.png}": #correct
                                    jump school_maze_correct
                        "{image=gui/north.png} Go Straight {image=gui/north.png}":
                            pass
                "{image=gui/north.png} Go Straight {image=gui/north.png}":
                    pass
        "{image=gui/east.png} Go Right {image=gui/east.png}":
            pass
        "{image=gui/north.png} Go Straight {image=gui/north.png}":
            pass
    jump school_maze_fail
    
    
label school_maze_correct:
    $ Emi.met = True
    $ loc = rm_teacher
    if (Mari in party or Mari.loc == loc):
        $ Mari.move(rm_teacher)
    if (Jun in party or Jun.loc == loc):
        $ Jun.move(rm_teacher)
    $ Emi.move(rm_teacher)
    play sound "sfx/door_open.ogg"
    scene teachers_room with fade
    "You carefully move into what appears to be the teachers' office."
    "You hear sniveling behind a desk and find a girl cowering underneath it."
    play music "music/bgs_slide.ogg"
    show Emi scared with dissolve
    "It's Emi, the quiet bookworm. She must have been scared pretty badly."
    y sad "Emi? I won't hurt you. I'm not playing this game."
    "You wait for a response, but Emi is rambling things under her breath."
    y sad "Emi?"
    "She's rocking back and forth now. The game has severely disturbed her."
    if (Jun in party or Jun.loc == loc):
        show Jun angry at farright with dissolve
        jun "What's wrong with her?"
        show Emi angry
        "Emi suddenly looks up from Jun's voice."
        emi "Hoodlum! Gangster!"
        show Jun skeptical
        jun  "I guess I deserve that."
        $ Emi.wpn.use_sfx()
        $ reference_item(Emi.wpn)
        show Jun mad
        "Emi shoots at Jun, but only grazes his arm."
        jun  "What the fucking fuck, lady!?"
        $ battle_start(Emi,3,"You leap to stop her from attacking again.", "emi_killed", False, flee=False, allies_will_help=True)
    elif (Mari in party or Mari.loc == loc):
        show Mari content at farleft with dissolve
        mari "It's okay ... We're your friends."
        mari "Everything is okay. We're just here at school, waiting for class to start. Just a regular day at school."
        show Mari sad at left with dissolve
        "You watch Mari try to calm Emi down. It seems to be working."
        emi "My school ... my school ... I deserve it."
        show Mari content
        mari "The entire school is yours."
        $ reference_item(Emi.wpn)
        $ Emi.wpn.get_sfx()
        show Mari
        "Mari secretly takes the gun from Emi's hands as she gets near. You relax now that she's disarmed."
        # Mari gets you a new powerful weapon. Yay!
        $ bayonet.add()
        $ Emi.wpn = None
        show Emi
        emi "... Mari?"
        show Mari content
        "She smiles down at Emi."
    else:
        # --- Else, you have to trick her into shooting something to have her run out of bullets. When she's out of bullets, you charge her and she's able to stab you for some damage, but you get the gun out of her hands. Defenseless, she begs for her life and you give her space.
        $ reference_item(Emi.wpn)
        $ Emi.wpn.get_sfx()
        show Emi angry
        "When you step forward, she aims her gun at you."
        emi "It's my school! Mine!!"
        y scared "Don't shoot!"
        emi "I earned it! I deserve it!"
        hide Emi with dissolve
        "She's going to shoot you, so you dive behind a desk yourself."
        y scared "Emi!?"
        play sound "sfx/gun_empty.ogg"
        "She screams and shoots in your direction. You flinch, but she's managed to miss you completely. You hear her gun click because its out of ammunition."
        "You finally think it's safe to come out."
        show Emi angry with dissolve
        "You slide away from your desk and see her again. She shoots her gun at you, even though it only clicks."
        if not wish_safety_you:
            $ damage_you(-10)
            $ show_blood()
            show Emi scared
            "Just when you're about to reach her, she stabs you with the bayonet on the end."
            y angry "Agh! Damn it!"
            "You fight against the pain and wrestle the gun from her hands."
        else:
            "You wrestle her gun from her."
        # Melee-only bayonet added
        $ bayonet.broken = False
        $ bayonet.uses = 0
        $ bayonet.use_count = 0
        $ bayonet.sfx2 = "sfx/slice.ogg"
        $ bayonet.wpn_rating = 4
        $ bayonet.battle_range = 2
        $ bayonet.weapon_range="melee"
        $ bayonet.type=""
        $ bayonet.desc = "An empty handgun with a knife-like blade stick out of the front of it. While it's out of ammo, at least it's still useful in melee situations."
        $ bayonet.desc += " {color=#FFF}Melee{/color}."
        $ bayonet.add()
        $ Emi.wpn = None
        "Emi cries and kicks at you. She has been seriously disturbed by this game."
        y scared "It's all right, okay!?"
        
    show Emi scared
    emi "I can't. I don't want to do this. I want to go home. I want to go home!"
    if (Mari in party or Mari.loc == loc):
        show Mari sad
        mari "I know ..."
        "Mari hugs Emi close and they stay like that for a while."
    y sad "Come with me, Emi. You're not safe being here alone in your state."
    show Emi angry
    emi "It's my school."
    y none "Uh?"
    if (Mari in party or Mari.loc == loc):
        mari "You can still come with us."
    emi "No. You can't take me away."
    y none "You need to go. Can you stand?"
    emi "No!"
    hide Emi with dissolve
    "Emi yelps and jumps up to hide behind another desk."
    y none "Emi!?"
    "The poor girl sobs and goes back to muttering random things."
    if (Mari in party or Mari.loc == loc):
        mari "She won't leave ..."
        hide Mari with dissolve
    show Emi scared with dissolve
    menu:
        "Put Emi out of her misery [[Attack]":
            if (Mari in party or Mari.loc == loc):
                $ wpn.get_sfx()
                "You move to attack Emi."
                mari "What are you doing!?"
                y none "She's a lost cause."
                y none "We should put her out of her misery."
                mari "But ..."
                y none "You don't want me to?"
                "Mari shakes her head."
                menu:
                    "Continue [[Attack]":
                        $ mari_knows_emi_kill = True
                        $ battle_start(Emi,3,"Better you than someone else.", "emi_killed", True)
                    "Stop":
                        y none "Fine."
                        "You give Emi one last look."
            else:
                $ battle_start(Emi,3,"She's a lost cause. Better you than someone else.", "emi_killed", True)
        "Leave her be":
            y none "If that's what you want."
            emi "My school, my school ..."
            hide Emi with dissolve
            if (Mari in party or Mari.loc == loc):
                mari "Good-bye, Emi ... We'll find help soon."
            "Just before you leave, Emi mumbles your name."
            show Emi with dissolve
            "You turn back around."
            emi "Ikoma."
            emi "Look out for Ikoma."
            if not Ikoma.alive:
                y none "He's been dealt with."
                "Emi's eyes widen and then lower. She tucks herself back under a desk."
            else:
                "She slides something across the floor. It's a pair of binoculars."
                $ binoculars.add()
                y none "Thank you."
                if binoculars.is_in_inventory():
                    memo "Binoculars give you the ability to see who is around you on the Map screen, if they are not inside buildings."
                    ## This is the ultimate reward for not killing the poor girl

    jump grid_loc
    

label school_maze_fail:
    $ Emi.met = True
    $ loc = rm_classroom
    if (Mari in party or Mari.loc == loc):
        $ Mari.move(rm_classroom)
    if (Jun in party or Jun.loc == loc):
        $ Jun.move(rm_classroom)
    $ Emi.move(rm_classroom)
    # - If you make a wrong turn, she will sneak attack you.
    play sound "sfx/door_squeak.ogg"
    scene classroom with fade
    "You follow your instincts, but you end up in an empty room."
    jump school_emi_ambush

label school_emi_ambush:
    $ Emi.wpn.get_sfx()
    $ reference_item(Emi.wpn)
    show Emi angry with dissolve
    play sound "sfx/accent_dumdum.ogg"
    "A click startles you and you spin around. Emi is standing behind you with her weapon drawn. A deadly bayonet is attached to the end of her gun."
    y sad "Emi?"
    "The fire in Emi's eyes shows that she is no longer the quiet girl who sat in the back of the classroom."
    y scared "Emi -"
    show Emi scared
    "She yells in fear and aim straight at you."
    if (Jun in party or Jun.loc == loc):
        # -- if you have Jun in the party, he will jun in the line of fire and take the hit for Shinobu. Emi is shocked. She brings the gun to her head and commits suicide. Afterwards, you have to attend to Jun. You must have a first aid kit to move him from this spot for the rest of the game.
        show Jun scared at right with dissolve
        jun "Watch it!"
        stop music
        $ Emi.wpn.use_sfx()
        play music "music/Reynardine.ogg"
        "Jun jumps in front of you and takes the bullet."
        show Jun mad at right
        show Emi
        jun "Arrrgh, shit ..."
        y scared "Jun! No!!"
        jun "Fuck ... This stings like hell ..."
        hide Jun with dissolve
        show Emi scared
        "Jun grabs his chest and crouches down."
        if (Mari in party or Mari.loc == loc):
            show Mari scared at left with dissolve
            mari "Oh no! Jun!"
            hide Mari with dissolve
        "Emi stares wide-eyed at Jun as he collapses in pain."
        $ wpn.get_sfx()
        if wpn != fist:
            "You growl at her and take out your weapon."
        $ reference_item(Emi.wpn)
        "But before you can subdue her, Emi raises her gun to her own head."
        $ Emi.wpn.use_sfx()
        $ show_blood()
        hide Emi with dissolve
        $ Emi.kill("suicide",drop_loot=True)
        $ add_sanity(-10, silent=True)
        "She commits suicide. You can't even get a word out of your mouth to stop her before she's sprawled out on the floor in a pool of her own blood."
        y scared "No!! Goddamn it, no!"
        "You scream at her body."
        "Everything happened too fast."
        if wish_safety_jun:
            show Jun sad with dissolve
            jun "It's okay! I'm okay!"
            y scared "Really!?"
            jun "It only grazed me - argh!"
            "Jun grunts while standing back up. He shows the bleeding wound on his side, but it doesn't look too bad."
            $ jun_survived_emi = True
            
        else:
            if (Mari in party or Mari.loc == loc):
                show Mari sad at left
                with dissolve
                mari "We have to stop the blood ... Oh, oh! I can't ... Why is this happening to us!?"
                $ add_sanity(-10, silent=True)
                "Mari is trying to save Jun while sobbing to herself."
            show Jun sad with dissolve
            python:
                found_medicine = None
                if firstaid.is_in_inventory():
                    found_medicine = firstaid
                elif medkit.is_in_inventory():
                    found_medicine = medkit
                elif (Jun in party or Jun.loc == loc) and Jun.item != None and (Jun.item[0] == firstaid or Jun.item[0] == medkit):
                    found_medicine = Jun.item[0]
                elif (Mari in party or Mari.loc == loc) and Mari.item != None and (Mari.item[0] == firstaid or Mari.item[0] == medkit):
                    found_medicine = Mari.item[0]
            if found_medicine:
                $ jun_survived_emi = True
                $ found_medicine.destroy(1)
                $ found_medicine.use_sfx()
                "You used a %(found_medicine.fancy_name) to dress Jun's wound."
            else:
                #Jun dies
                "Jun is losing blood fast ... You fall on your knees beside him."
                y sad "Why did you do that!?"
                show Jun skeptical
                jun "Dumbass ... You can't die."
                y sad "What makes you think you can!?"
                show Jun
                jun "I'm nobody. You guys barely know me and I barely know you ... My fault for not going to class more often."
                if (Mari in party or Mari.loc == loc):
                    show Mari scared
                    mari "Don't say things like that! We care! We care so much!"
                    show Mari sad
                show Jun mad
                "Jun cringed and grabbed his wound."
                jun "This ... may be it."
                y scared "No! Fight it! I'll go find help!"
                show Jun
                jun "You know ... You're actually an okay guy. I thought you were one of those types of guys, hanging out with those assholes."
                show Jun happy
                jun "Nah."
                "Jun slaps a bloody hand onto you with a smile."
                jun "Nah. You're cool."
                y sad "Jun ... Don't you dare."
                hide Jun with dissolve
                "Jun's hand goes weak and falls from you. He slowly closes his eyes."
                $ Jun.kill("murdered",killer=Emi,drop_loot=True)
                y none "Jun!!"
                if (Mari in party or Mari.loc == loc):
                    show Mari scared
                    hide Mari with dissolve
                    "Mari cries louder. She turns away in turmoil."
                "You check. Jun is gone."
                "He saved your life."
                "You silently promise that it won't be in vain."
                if (Mari in party or Mari.loc == loc):
                    stop music fadeout 3.0
                    "You collect Mari and lead her out of that horrible room."
                $ jun_survived_emi = False
        if jun_survived_emi:
            stop music fadeout 3.0
            y happy "Thank god."
            show Jun angry
            jun "That crazy girl almost killed me!"
            show Jun skeptical
            jun "Actually, she almost killed you."
            show Jun angry
            y sad "She was scared ... We're all scared."
            "You look over at her body."
            y none "We should get out of here."
        
            
        
    else:
        # you must kill her.
        $ Emi.wpn.use_sfx()
        $ show_blood()
        if wish_safety_you:
            $ damage_you(-10)
        else:
            $ damage_you(-20)
            
        
        $ battle_start(Emi,3,"Her bullet pierces you.", "emi_killed", True, allies_will_help=True)
    jump room_loc
    
label emi_killed:
    "Emi writhes on the floor for a few seconds before she becomes completely still."
    if mari_knows_emi_kill:
        "Mari glares at you, but you shake it off. You knew what had to be done and you weren't afraid to do it."
    if (Jun in party or Jun.loc == loc):
        show Jun mad with dissolve
        jun "She was fucking insane!"
    elif (Mari in party or Mari.loc == loc) and not mari_knows_emi_kill:
        show Mari scared with dissolve
        mari "What ... what was wrong with her?"
    if (Jun in party or Jun.loc == loc) or (Mari in party or Mari.loc == loc) and not mari_knows_emi_kill:
        y sad "She was scared ... We're all scared."
        "You look over at her body."
        y none "We should get out of here."
    if (Mari in party or Mari.loc == loc):
        "You collect Mari by the hand and lead her out of that horrible room."
    
    $ just_murdered_someone = False
    jump grid_loc
    
    
    
# #YUKI
label yuki_intro:
    $cutscene()
    # You run into Yuki. He's startled and has a good weapon, but doesn't attack. He asks if you've seen Nanako.
    show Yuki with dissolve
    "There's a boy here. Yuki."
    "He was very popular with the girls ... which was always funny to you, because he looked like one."
    show Yuki scared
    yuki "It's ... you!"
    $ reference_item(Yuki.wpn)
    $ Yuki.wpn.get_sfx()
    "Yuki flashes his weapon. Even if you did want to kill him, he'd stop you."
    "You throw your hands up."
    y scared "Settle down."
    show Yuki sad
    yuki "Sorry ... You're right. I'm sorry."
    show Yuki
    yuki "What have we become if we let our situation turn us against each other? I won't stoop that low."
    y none "That's good to hear."
    "Several tense seconds pass."
    if (Mari in party or Mari.loc == loc):
        mari "How are you doing?"
        yuki "I'm really glad to see you're okay, Mari."
        mari "Thank you."
        "Mari smiles and you're a little jealous."
    if (Jun in party or Jun.loc == loc):
        jun "All by yourself?"
        show Yuki scared
        yuki "Why? Are you thinking of taking advantage of that!?"
        y none "Jun isn't a bad guy. You don't have to be afraid of him."
        if Jun.wpn == ladle:
            $ reference_item(Jun.wpn)
            $ Jun.wpn.get_sfx()
            jun "Yeah, all I got is a spoon, so ..."
        show Yuki sad
        yuki "If you say so."
    y none "If you're not playing the game, you can come with me. I'm going to find a way off the island."
    yuki "That sounds lovely, but ... Honestly, I'm trying to find someone."
    y none "Who?"
    show Yuki
    yuki "Have you seen Nanako?"
    y none "Nanako?"
    if not Nanako.met:
        "The fashion queen of the class? So Yuki wasn't gay after all."
    yuki "Well, have you?"
    menu:
        "[[Attack]":
            $ battle_start(Yuki,3,"There's no point in answering, you've made up your mind.", "murdered_yuki", True)
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
            hide Yuki with dissolve
            "Yuki runs away with a quick wave."
            $ Yuki.move(Nanako.loc) #Teleport him to Nanako
            $ Yuki.type = "fixed"

        "Yes [[Lie]" if not Nanako.met:
            $ answered_yuki = True
            $ yuki_lied = True
            y none "Yeah, totally."
            "You lie."
            y none "I saw her walking around A4."
            yuki "Thank you!! Thank - A4? Are you sure?"
            y none "Pretty sure. Why?"
            yuki "Um ... nothing. Maybe - no, it's nothing."
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
                $ mari_knows_yuki_lie = True
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
                    y none "Fine, I never liked him, okay?"
                    "Mari frowns at you, but you don't care."
                    $ mari_knows_yuki_lie = True
    jump grid_loc

## BATHHOUSE, YUKI
label bathhouse_nanako_yuki:
    # If you told Yuki about Nanako, you will find him there with her.
    if not Nanako.alive and not Yuki.alive and Nanako.loc == loc and Yuki.loc == loc:
        $ cutscene()
        "You find Yuki on the ground ... dead. Nanako is next to him."
        "You find some peace in the fact that they met before the end."
    elif not Nanako.alive and Yuki.loc == loc:
        jump yuki_nanako_dead
    elif not Yuki.alive and Nanako.loc == loc:
        jump nanako_yuki_dead
    elif answered_yuki and Nanako.loc == loc and Yuki.loc == loc:
        $ cutscene()
        show Yuki at mid_right
        show Nanako at mid_left
        with dissolve
        show Yuki happy
        "Yuki and Nanako are standing close together. They gasp when they see you, but Yuki smiles."
        yuki "Okita! He's the one who told me."
        show Nanako happy
        nana "I see. So he's not all that bad."
        y sad "I was bad before?"
        show Nanako
        nana "Let's just say that I'm guilty of starting a few rumors. Only a few."
        show Yuki
        y scared "... That was you!?"
        show Yuki sad
        yuki "She's sorry! Aren't you?"
        show Nanako angry
        nana "Of course I'm sorry! Does any of that matter anymore?"
        show Nanako sad
        nana "That whole life seems like decades ago ... I used to hate school, but now I wish I was bored in class more than anything any the world!"
        show Yuki happy
        "Yuki hugs Nanako close and she rests her head on his shoulder."
        yuki "We'll get back. We have to believe."
        if (Mari in party or Mari.loc == loc):
            mari "Yes. We can't lose hope."
            show Nanako happy
            nana "Mari, you're too peppy, even for me."
            "They laughed quietly."
        "You bask in a rare moment of hope. You hold onto this moment for as long as you can."
        hide Yuki
        hide Nanako
        with dissolve
    return

label yuki_nanako_dead:
    $ cutscene()
    show Yuki scared
    if Nanako.loc == loc:
        "You find Yuki hugging the limp body of Nanako."
    else:
        "You find Yuki wailing on the ground."
    y none "Yuki! ... What happened?"
    yuki "She's gone ... Nana ..."
    if (Mari in party or Mari.loc == loc):
        mari "Oh, Yuki ... I'm so, so sorry ..."
    yuki "At least ... she knew."
    if (Jun in party or Jun.loc == loc):
        jun "Knew what?"
    yuki "I couldn't stop this. I only wanted to protect her."
    yuki "I can't ... I can't live with myself."
    y none "Yuki - no. Think about this for a second."
    show Yuki
    yuki "There's nothing to think about about."
    if (Mari in party or Mari.loc == loc):
        mari "Please don't!!"
        $ reference_item(Yuki.wpn)
        $ Yuki.wpn.get_sfx()
        "Yuki smiled softly at Mari as he lifted his gun to his head."
    else:
        $ reference_item(Yuki.wpn)
        $ Yuki.wpn.get_sfx()
        "Yuki closed his eyes and lifted his gun to his head."
    if (Jun in party or Jun.loc == loc):
        jun "Whoa, whoa, whoa!"
    y scared "Yuki! {u}Stop!{/u}"
    $ Yuki.wpn.use_sfx()
    $ show_blood()
    hide Yuki with dissolve
    $ Yuki.kill("suicide",drop_loot=True)
    $ add_sanity(-30)
    "You stand frozen for a while. You will see this whenever you close your eyes for a long, long time."
    if (Mari in party or Mari.loc == loc):
        $ Mari.sanity -= 15
        "Mari wails and falls to the ground."
        if (Jun in party or Jun.loc == loc):
            "Jun attempts to console her."
    if (Jun in party or Jun.loc == loc):
        $ Jun.sanity -= 15
    "It takes you too much time to move on again."
    return

label nanako_yuki_dead:
    $ cutscene()
    show Nanako
    if Yuki.loc == loc:
        "Nanako is sitting next to Yuki's corpse."
        y scared "Nanako! What happened here!?"
        if (Jun in party or Jun.loc == loc):
            jun mad "Did you kill him!?"
            nana "Kill him!? With what!?"
            "Nanako shows that she has zero weapons."
        nana "He ... He came to tell me he loved me. And then ..."
        if Yuki.death_type == "murdered":
            nana "He was murdered in cold blood by %(Yuki.murderer.name)s!"
        "Nanako presses her face into Yuki's cold body and sobs."
        if (Mari in party or Mari.loc == loc):
            mari sad "We're so sorry ..."
        y sad "We should bury him."
        nana "No ... Let me have some more time with him, please."
        y sad "If that's what you want ..."
        "You leave Nanako in peace."
    else:
        "You find Nanako sobbing loudly."
        y scared "Nanako? Are you okay?"
        nana "Yuki ... He ... He's dead!"
        "Nanako presses her face into the computer pad and sobs."
        if (Jun in party or Jun.loc == loc):
            jun lookaway "Shit..."
        if (Mari in party or Mari.loc == loc):
            mari sad "We're so sorry ..."
        "You don't know what to say. You leave Nanako in peace."
    return

## YUKI (if you lied)
label yuki_waiting:
    # If you lied to Yuki, he is waiting (somewhere)
    show Yuki scared with dissolve
    # He's pretty beat up now. Good job!
    $ Yuki.health = min(Yuki.health, 50)
    $ Yuki.sanity = min(Yuki.sanity, 50)
    "Yuki is standing here. His clothes are torn and his hair is a mess. He whips around and stares at you like a wild animal."
    yuki "Nana!?"
    y none "It's just me, Yuki."
    yuki "You! You said she was around here! Where is she!?"
    "You don't answer him."
    if (Mari in party or Mari.loc == loc) and mari_knows_yuki_lie:
        mari "I can't believe you."
        "You look over and see Mari glaring at you again."
        y angry "What?"
        "She looks away."
        mari "Nevermind."
    # Make him wander around after this
    $ Yuki.type = "normal"
    jump grid_loc

    

##KEI
label kei_intro:
    # You meet the star player of the baseball team you managed. There was always some resent between the two of you because he always wanted to do what HE wanted to do, and disobeyed you several times. He seems glad to see you at this point, but cautious about Jun, and very friendly to Mari (if Fumie is there, she will be jealous).
    $ cutscene()
    show Keitaro with dissolve
    "It's Keitaro. You know him well."
    kei "Well, well ... What's up, Shin?"
    if sword.is_in_inventory() or laptop.is_in_inventory():
        call kei_takeshi_things
    "You already feel a migraine coming on."
    "Kei was on your baseball team. He was the crowd favorite, which made him cocky. Very cocky."
    y none "I see you're still alive."
    kei "Of course."
    kei "You're not doing too bad yourself."
    if (Mari in party or Mari.loc == loc):
        "Kei approaches Mari with a smug smile."
        "You step in front of her and that smile goes away. Typical of him."
    if (Jun in party or Jun.loc == loc):
        "He raises his eyebrow at Jun."
    if Fumie.loc == loc and Fumie.alive:
        $ Fumie.met = True
        # - If Fumie is there, they reveal that they're going to hide in the hospital together and look for Takeshi in turns. They think Takeshi will be able to hack their collars and get them free.
        show Keitaro at left with move
        show Fumie at right with dissolve
        fum "Heeey!"
        if not Fumie.met:
            "You knew Fumie wouldn't be far - if she was alive. She was Kei's biggest fan and widely recognized as his girlfriend, though it was never official."
            "She was way too happy for someone who was in a murder game."
        if (Mari in party or Mari.loc == loc):
            mari content "Hello, Fumie."
    kei "So ..."
    y none "... So."
    "The tension that you two had in school has survived into the game. You feel awkward around him."
    kei "How are you keeping alive?"
    if wpn.seen:
        if wpn != fist:
            "You touch your weapon instinctively."
        y none "I'm managing."
    else:
        y none "By not playing the game."
    kei "I knew you were resourceful. I've been thinking about how this is all going to go down, and you were definitely in the last five."
    y angry "What does that mean?"
    kei "Have you seen Takeshi around?"
    if not Takeshi.alive and Takeshi.murderer.name == you.name:
        menu:
            "Reveal yourself [[Attack]":
                y evil "Yes."
                $ battle_start(Kei,0,"You never liked him anyway.", "murdered_kei", True)
            "Lie":
                y none "No."
                kei "Shame, he's around here somewhere. He's snooping around and doing what he does best. You know."
    else:
        if Takeshi.met:
            y none "Yes."
            kei "Cool, then I can let you in on our deal."
            y none "What deal?"
        else:
            y none "No."
            kei "Shame, he's around here somewhere. He's snooping around and doing what he does best. You know."
    kei "He's got that laptop and since he's such a nerd, we're thinking he can hack our way out."
    if not Fumie.met and Fumie.loc != loc:
        y none "\"We?\""
        kei "Me, Takeshi, and Fumie."
        "Fumie ... Kei's little sweetheart."
    if (Jun in party or Jun.loc == loc):
        jun skeptical "How the hell would you do that?"
    if Fumie.loc == loc and Fumie.alive:
        fum "He's going to hack our collars!"
    kei "Our collars are just little computers and he's so good at them. He said he's working on it."
    if (Mari in party or Mari.loc == loc):
        mari sad "Is that really possible?"
    kei "I don't know for sure, but hey ... we've got to try something."
    y none "If he thinks he has a shot, then he should give it his all. Anything to get us off of here."
    if Fumie.loc == loc and Fumie.alive:
        fum "That's what I'm saying! We can't give up hope!"
        "Fumie hugs at Kei's arm and he looks a bit annoyed."
    y none "And you said you'd let me in on this?"
    y angry "If it works, why won't you free everyone?"
    kei "Totally, we'll free everyone. I meant, like ... we'd form a secret pact or something."
    y none "Why? I don't see why anyone wouldn't want to help Takeshi bypass our collars. We'd all stop attacking each other and escape."
    kei "... I guess you're right. I just don't feel right telling a bunch of people."
    if (Mari in party or Mari.loc == loc):
        mari angry "We'll help in anyway, but I don't like the idea of splitting away from our classmates for some silly secret pact idea."
    y none "I'll help you, but we need to remember that it's not \"us\" versus \"them\" here. Everyone here deserves to live."
    show Keitaro angry
    kei "I know that! You're just twisting my words! Sheesh, you're always doing that."
    "Kei starts to get worked up and you hold back to prevent setting him off."
    show Keitaro
    kei "Anyway, it doesn't matter because nothing's been hacked yet anyway."
    y none "How can I help?"
    kei "I don't know. Talk to Takeshi about that."
    y none "Where will you be so I can find you again?"
    kei "Around here maybe, or maybe not. I just have to keep safe."
    if Fumie.loc == loc and Fumie.alive:
        fum "I've got your back!"
        kei "I think we should split up, for our own good. We'll attract more attention together."
        kei "Besides, shouldn't you go guard the hospital?"
        y none "Why guard the hospital?"
        fum "Takeshi said it's the best place to do his hacking. We don't want some idiot to go in and wreck the place!"
    y none "All right. See you."
    $ ask_takeshi = True
    jump grid_loc
    
label kei_takeshi_things:
    show Keitaro scared
    if Fumie.loc == loc and Fumie.alive:
        show Keitaro scared at left with move
        show Fumie scared at right with dissolve
        fum "What did you do!?"
    kei "Is that ... Is that Takeshi's!?"
    "You're caught with Takeshi's belongings. So, they knew what he had with him. Very unfortunate."
    menu:
        "[[Attack]":
            "All those times you rubbed it in my face how popular you were ... Now you'll never make it off this island."
            kei "What the fuck!?"
            $ battle_start(Kei,0,"You hated him and he deserves this.", "murdered_kei", True)
        "Talk your way out of this":
            y scared "It's not what you think!"
            kei "There's blood all over you! Oh shit!"
            "Kei goes for his gun."
            menu:
                "Can't talk my way out of this [[Attack]":
                    $ battle_start(Kei,0,"Might as well.", "murdered_kei", True)
                "He was already dead when I found him":
                    y scared "This isn't what it looks like. I found these on Takeshi, yes, but he was already dead. Someone else got him. I didn't do it. You have to believe me!"
                    "Kei eyes you."
                    kei "So ... he is dead?"
                    y sad "Yes."
                    kei "And you didn't kill him?"
                    y sad "No. Why would I? He had a way of getting off the island, I'd want him to be alive."
                    show Keitaro angry
                    if Fumie.loc == loc and Fumie.alive:
                        show Fumie angry
                    kei "Hold on! How did you know that? I thought he was dead when you met him!"
                    y scared "Wait, I - No - I've talked to him before and then I came back -"
                    kei "You're lying!!"
                    if Fumie.loc == loc and Fumie.alive:
                        fum "How could you!?"
                    $ battle_start(Kei,0,"Kei doesn't want to talk anymore.", "murdered_kei", True)
                "He let me have these":
                    y scared "I know this looks bad, but I found Kei bleeding out! Some bastard got him!"
                    y scared "He told me that he was going to get you off the island, so he trusted me with his things, so that you could still make it out alive! You have to believe me!"
                    if laptop.is_in_inventory():
                        kei "He told you that ...?"
                        y sad "Yes. I still have his laptop here. We can see if he has anything written."
                        kei "It's no use. We're not programming geeks like him. It's over. It's done. He was our one hope."
                        "Kei is too preoccupied with the loss of Takeshi to interrogate me anymore."
                        $ takeshi_sad = True
                        jump grid_loc
                    else:
                        show Keitaro angry
                        kei "Where's his laptop, then!? You dumped it! He would have told you it's the most important thing!"
                        if Fumie.loc == loc and Fumie.alive:
                            fum "Yeah! We need it!"
                            show Fumie angry
                            fum "I think he's lying!"
                        kei "You're lying, you shit head! You killed him! You killed him and took his weapon!"
                        $ battle_start(Kei,0,"Kei doesn't want to talk anymore..", "murdered_kei", True)
    return
    
 
# #TAKESHI
label takeshi_intro:
    # He's wandering the coast, looking for a way off the island. He asks if you've seen a boat.
    $ cutscene()
    show Takeshi with dissolve
    tak "Whoa. Hey."
    "Takeshi stands before you."
    "He was the cool guy in class. Quiet, rich, and tech-savvy. Sure enough, you see he's carrying around his laptop."
    y none "How much battery do you have left in that thing?"
    show Takeshi angry
    tak "Aren't you going to say hello first?"
    if (Mari in party or Mari.loc == loc):
        mari content "Hello!"
        show Takeshi
        "Takeshi smiles at Mari."
    elif (Jun in party or Jun.loc == loc):
        jun angry "Who died and made you king?"
        show Takeshi angry
        "Takeshi looks at Jun like he's a weirdo."
    y none "Sorry?"
    if wpn.seen and wpn != fist:
        "Takeshi looks at your weapon."
        tak "Playing the game? You know, you don't have to."
    show Takeshi
    tak "I'm working on a way to get us off the island, so you don't need to attack me."
    if Kei.met:
        y none "Yeah, Kei told me."
        tak "Oh, cool, then he's approved you into his stupid secret pact."
        if (Jun in party or Jun.loc == loc):
            jun skeptical "Good, you think it's stupid, too."
    else:
        y happy "Really!? That's great news!"
        tak "Don't tell Kei that I told you, though."
        y none "Erm ... okay?"
    tak "By the way, have you seen a boat around yet?"
    call takeshi_boat_chat
    
    
    $ Takeshi.met = True
    if ask_takeshi:
        jump takeshi_collar_help

    jump grid_loc
    
label takeshi_boat_chat:
    if seen_boat:
        menu:
            "Yes":
                python:
                    takeshi_boat_truth = True
                    boat_in_shed = True
                    # If the boat is repaired, the player could've moved it
                    if boat_repair >= 3:
                        for location in locations:
                            for i in location.items:
                                if i[0] == boat:
                                    if location == rm_shed:
                                        boat.destroy(1)
                                        boat_in_shed = True
                                    else:
                                        boat_in_shed = False
                                    break
                    if not boat_in_shed:
                        takeshi_boat_truth = False
                        takeshi_boat_lied = True
                y happy "You won't believe, but I have!"
                if len(followers) > 0:
                    y none "We're repairing it right now."
                else:
                    y none "I'm repairing it right now."
                tak "No fucking way. I knew it! I just knew it."
                tak "Where is it!?"
                y scared "Hold on -"
                tak "What, you don't trust me? We're in this together."
                if Kei.met:
                    tak "The secret pact, remember?"
                y none "I guess you're right ..."
                y none "The boat is in a shed in B3."
                tak "Sweet. You saved us, you know."
                if boat_repair < 3:
                    y none "It's broken and needs repairing."
                    tak "No problem for us."
                else:
                    y none "That's what I mean."
                y none "The boat is our only way off the island, unless you really can hack our collars."
                "Takeshi laughed."
                tak "Yeah, right. Like that was going to actually happen."
                y sad "You don't think you actually could?"
                tak "That would've only happened if some miracle happened. You actually have a boat. It's in our hands!"
                y sad "Okay, but we need to organize this. We shouldn't rush it. The boat's not big enough for everyone at once."
                tak "Of course. Yeah."
                "You're starting to feel uneasy about telling other people."
                # Move them to the shed so the GPS can tell
                if Takeshi.alive:
                    $ Takeshi.move(rm_shed)
                    $ Takeshi.type = "fixed"
                if Kei.alive:
                    $ Kei.move(rm_shed)
                    $ Kei.type = "fixed"
                if Fumie.alive:
                    $ Fumie.move(rm_shed)
                    $ Fumie.type = "fixed"
            "No [[Lie]":
                $ takeshi_boat_lied = True
                y none "Nope."
                if Takeshi.met:
                    tak "... You're sure?"
                    y none "Yeah, why?"
                    tak "Nothing."
                    "Takeshi looks away."
                else:
                    show Takeshi sad
                    tak "Aw. Lame."
                if (Mari in party or Mari.loc == loc):
                    "Mari looks at you weird, but you plan to explain why telling him about the boat was truly dangerous."
                if (Jun in party or Jun.loc == loc):
                    "Jun nods towards you. His face is painted with worry."
    else:
        if Takeshi.met:
            y none "Still looking."
        else:
            y none "No."
            y happy "Do you think there'd be one? The people who did this to us should be smarter than that."
            show Takeshi
            tak "You never know. This island has been used for games before."
            tak "The bodies have been taken, but I'm still seeing stuff they've left all over."
            tak "Maybe some kids before us left a boat."
            y none "That's impossible."
            show Takeshi angry
            tak "Believe what you want, I happen to subscribe to the future where I don't die on this shit island."
    return

label takeshi_collar_help:
    $ cutscene()
    $ ask_takeshi = False
    y none "Kei told me I should talk to you about how to help you deactivate our collars."
    show Takeshi
    tak "Oh. Okay."
    tak "Well, I'm 100%% sure there's a way we can fool the GPS trackers in our collars, because I've done it before."
    show Takeshi sad
    tak "But there's no way I can do that without some of their tech."
    y none "Their tech?"
    show Takeshi angry
    tak "The idiots who put us here. I need some of their technology."
    y sad "Just ... anything?"
    show Takeshi
    tak "Not just anything. I don't expect you to understand, so don't sweat it."
    tak "Just ... if you happen to come across something you think is related to our collars, give it to me."
    y scared "And you'll hack it and we can go home!?"
    tak "No promises, but that's the idea."
    y none "Then I'll look out for something."
    $ takeshi_gps = True
    jump grid_loc
    
label takeshi_gps_give:
    $ cutscene()
    y none "Will this work?"
    if gps.is_in_inventory():
        $ takeshi_gps = False
        "You hand out the GPS tracker. Takeshi is floored."
        tak "How did you get this? Shit, who cares. Give it to me!"
        $ gps.destroy("all")
        "He takes the GPS and starts inspecting it thoroughly."
        tak "I'm going to take this to the hospital to fiddle with it."
        y none "Should I come, too?"
        tak "If you want."
        "Takeshi is too engrossed in the device to care about you anymore."
        $ gps_story = True
        $ Takeshi.move(rm_hospital)
        jump grid_loc
    else:
        show Takeshi angry
        tak "Will what work? You don't have anything remotely close to what I need."
        return


## GAVE TAKESHI YOUR GPS
label gps_hospital:
    ## Fumie is outside, standing guard. She lets you inside.
    ## Takeshi is working on the GPS gadget and Kei and Fumie are there. Something goes wrong and Tak's collar counts down to explode. The group can only watch Tak die. Afterwards, Fumie gets clingly on Kei and Kei finally tells her to piss off and she's distraught to the point of anger. She kills Kei. Shinobu+party try to get out of there alive and Fumie lets them.
    $ cutscene()
    if Fumie.alive:
        show Fumie angry with dissolve
        if Kei.alive:
            # Kei gave her his weapon to stand guard
            $ Fumie.item = [Fumie.wpn,1]
            $ Fumie.wpn = Kei.wpn
            $ Kei.wpn = None
            $ Fumie.wpn.get_sfx()
            $ reference_item(Fumie.wpn)
            show Fumie happy
            fum "Oh, hi!"
            "Fumie stops wielding Kei's gun at you and smiles."
            show Fumie
            y none "What's going on?"
            fum "Nothing, I'm just on guard duty."
            fum "Come on in! Takeshi is setting up his computer right now."
        else:
            show Fumie sad
            fum "Oh. Hello."
            fum "I was just guarding this place until you got here. Come on in."
    else:
        "Here is the hospital. This is where Takeshi said he would be."
        "You help yourself inside."
    $ loc = rm_hospital
    if Kei.alive:
        $ Kei.move(rm_hospital)
    if Fumie.alive:
        $ Fumie.move(rm_hospital)
    $ Takeshi.move(rm_hospital)
    play ambience "sfx/room_tone1.ogg" fadein 3.0
    scene lab with fade
    show Takeshi with dissolve
    "Takeshi is sitting in the corner, bathed in the light of his laptop. The hum of a gasoline-powered generator is instantly heard."
    y scared "You have a back-up generator!?"
    tak "Yeah, most hospitals do. It just needed to be fixed and I needed to get some more gas - no prob."
    tak "It will run out soon though, so stop distracting me."
    if Fumie.alive and Kei.alive:
        show Keitaro at farleft 
        show Fumie at farright
        with dissolve
        fum "That should be everybody! Should I lock the door now?"
        kei "Yeah, sure. This generator is making a lot of noise."
    elif Kei.alive:
        show Keitaro at farleft 
        with dissolve
        y none "Where's Fumie?"
        kei "I dunno."
    elif Fumie.alive:
        show Fumie sad at farright 
        with dissolve
        "You realized why Fumie is so sad. Kei is nowhere to be seen."
    play sound "sfx/typing.ogg"
    "Takeshi clicked away on his computer."
    tak "This is exactly what I need."
    y none "You can deactivate our collars?"
    tak "Not right now. Maybe once we're off the island, but right now I can only block the satellites from see where we are."
    tak "That should be enough to get off the island without detection and hopefully out of wireless range for activation."
    if (Mari in party or Mari.loc == loc):
        mari sad "Could that work? What if our collars work everywhere, no matter what?"
        tak "Doubtful. Who has that sort of technology?"
    y none "It sounds too good to be true."
    tak "Well, we're about to find out ..."
    if Fumie.alive and Kei.alive:
        show Keitaro scared
        kei "Really!? Me first!"
        show Fumie happy
        fum "Yes, him first!"
        show Keitaro
        show Fumie
    tak "I'm the one who thought of it. I go first."
    if (Jun in party or Jun.loc == loc):
        jun angry "What if it goes wrong?"
        show Takeshi angry
        tak "I'm first, now shut up."
        show Takeshi
    tak "Just need to demagnetize the sensor here ..."
    "Takeshi adjusted his collar on his neck while rubbing a magnet along certain points."
    if len(party) > 0 or (Fumie.alive or Kei.alive):
        "Everyone watched in suspense."
    play sound "sfx/beep1_2.ogg"
    "Takeshi leaned over the map on his datapad until his icon finally disappeared from the island completely."
    tak "Aha!! It worked!"
    "He stood up in triumph."
    tak "Suck it, you fucking assholes!!"
    if Fumie.alive and Kei.alive:
        show Fumie happy
        "Kei runs up to him and chest-bumps him. Fumie squeals with joy."
    elif Fumie.alive:
        show Fumie happy
        "Fumie squeals with joy."
    elif Kei.alive:
        "Kei runs up to him and chest-bumps him."
    if (Mari in party or Mari.loc == loc):
        "Mari grabs your hand and you look over at her."
    play sound "sfx/beep_alarm.ogg"
    show Takeshi sad
    play music "music/FeelingDark_loop.ogg"
    "But a beep silences them."
    if Kei.alive:
        show Keitaro scared
        kei "Uh?"
    if Fumie.alive:
        show Fumie scared
    y sad "What was that?"
    "Takeshi hesitantly looks down at his datapad."
    memo "Whoops! Your recorded location is {color=#FFF}<Null>{/color}."
    memo "As this is impossible for live participants, it's concluded that you are an anomaly in the system."
    memo "Pruning shall commence in 5 ..."
    play sound "sfx/beep_alarm.ogg"
    "Takeshi's collar beeped a warning beep."
    if Kei.alive:
        kei "Pruning!?"
    play sound "sfx/beep_alarm.ogg"
    memo "... 4 ..."
    if Fumie.alive:
        fum "Takeshi!!"
    "He grabbed his collar in fear."
    play sound "sfx/beep_alarm.ogg"
    memo "... 3 ..."    
    if Kei.alive:
        kei "What do we do!?"  
    if (Jun in party or Jun.loc == loc) and (Mari in party or Mari.loc == loc):
        "Mari moves towards Takeshi, but Jun pulls her back."
    if len(party) > 0 or (Fumie.alive or Kei.alive):
        y scared "Stay away from him!"
    else:
        kei "Shin!?"
        y scared "Stay away from me!"
    play sound "sfx/beep_alarm.ogg"
    memo "... 2 ..."
    "You can only watch now. There's nothing you can do."
    tak "Help me! Help me!!"
    play sound "sfx/beep_alarm.ogg"
    memo "... 1."
    y scared "Takeshi!!"
    $ Takeshi.kill("fz",drop_loot=True)
    play sound "sfx/explosion.ogg"
    $ show_blood()
    hide Takeshi with dissolve
    "Takeshi's collar detonates. He colors the walls red before flopping onto the floor."
    if Kei.alive and Fumie.alive:
        show Fumie sad at center with move
        "Fumie screams in loud fits, shaking Kei furiously."
    elif Fumie.alive:
        "Fumie screams in loud fits."
    if (Mari in party or Mari.loc == loc):
        mari scared "Dear god ..."
    if Fumie.alive and Kei.alive:
        fum "Kei! Kei!!"
    if Kei.alive:
        "Kei is fixed upon Takeshi's corpse, who was once their best hope for survival."
        y sad "We can still do it. We can still survive. We can't let this be in vain -"
        if not Fumie.alive:
            show Keitaro angry at center with move
        else:
            show Keitaro angry
        kei "Shut your damn mouth, Shinobu!"
        "Kei turns on you."
        kei "You gave him that GPS! His blood is on your hands!"
        if Fumie.alive:
            fum "No! It's not anyone's fault! Kei, look at me!"
        if (Jun in party or Jun.loc == loc):
            jun mad "You looking for someone to be mad at? How about whoever put us here, not us!?"
        y scared "Don't try to blame me for this!"
        kei "You're such a meddling bastard! You were always so damn irritating!"
        if Fumie.alive:
            show Fumie scared
            fum "Kei -!"
            show Keitaro angry at left
            show Fumie scared at right
            with move
            "Kei spun around to Fumie."
            kei "You, too! You're fucking insane! Give me some fucking room to breathe!"
            show Fumie angry at right
            fum "Don't yell at me just because you're upset!"
        kei "If we're going to die on this island, I'm not going to put up with any of you people's shit any more!"
        if Fumie.alive:
            show Fumie sad at right
            fum "Kei!?"
            kei "That means you, too! Get out of my hospital! All of you!"
            show Fumie angry at right
            fum "It's not yours, I found it!"           
            show Fumie scared at right
            
            show Keitaro angry at center with move
            "Kei grabs Fumie's arm and starts to physically pull her out."
            
            fum "Stop! Why are you doing this!?"
            hide Fumie with dissolve
            "You run up to him and try to stop him from handling her."
            "Kei takes this as a personal challenge and gives up Fumie for you. He's taller and much stronger. There's a reason he was the baseball star and you were only the baseball manager."
        y angry "Get your damn head back on!"
        kei "I should kill you right now."
        if (Mari in party or Mari.loc == loc):
            mari scared "No!!"
        y angry "You don't even know why."
        kei "Yeah, I do. Because I hate you and I've always fucking hated you."
        "Kei grabbed your shirt and yanks you close."
        if Fumie.alive:
            show Fumie angry at right with dissolve
            show Keitaro angry at left with move
            "Fumie pushes him."
            "She's an athlete too, but she's not strong enough to knock Kei over. Kei does let go of you and turns on her, though."
            kei "You little -"
            show Keitaro scared
            $ reference_item(Fumie.wpn)
            $ Fumie.wpn.get_sfx()
            "Kei reaches for his gun, but then sees that Fumie is pointing it right at him. He remembers that he gave it to her only then."
            fum "All this time ... You never cared for me?"
            show Keitaro angry
            kei "Not even a little."
            $ Fumie.wpn.use_sfx()
            $ show_blood()
            hide Keitaro with dissolve
            $ Kei.kill("murder",killer=Fumie,drop_loot=True)
            show Fumie sad
            "Kei jerks backwards. Fumie's smoking gun trembles in her hands."
            y scared "Fumie ... Put down the gun."
            if len(party) > 0:
                "You had more than yourself to protect now."
            "But when Fumie turned to you, gun and all, you knew she wasn't threatening you with it. She just couldn't put her arm back down."
            if (Mari in party or Mari.loc == loc):
                fum "Mari?"
                mari scared "Fumie ..."
                fum "Don't do what I did."
                mari scared "I'm not - I won't -"
            fum "Run, before I shoot you, too."
            show Fumie angry
            fum "Go!!"
            hide Fumie with dissolve
            "Fumie screams at you to flee and you don't waste that chance."
            "You unlock the door and run to safety. Fumie doesn't follow."
        else:
            $ battle_start(Kei,1,"The truth hurts you a bit, but you've always hated Kei a little bit, too.", "kei_defended", True, flee=False, allies_will_help=True)
    else:
        "Fumie crumples down on the ground in front of Takeshi, her eyes devoid of hope."
        show Fumie sad
        fum "What can we do now..? What else do we do!?"
        y sad "We can still do it. We can still survive. We can't let this be in vain -"
        fum "Just... leave me alone. I need to get my head on straight."
        if (Mari in party or Mari.loc == loc) and Mari.alive:
            mari scared "Fumie... But..."
        if (Jun in party or Jun.loc == loc) and Jun.alive:
            Jun scared "Shinobu, are you sure we should leave her here like this?"
        y sad "Fumie?"
        fum "GO AWAY!!"
        $ reference_item(Fumie.wpn)
        $ Fumie.wpn.use_sfx()
        "She attacks you!"
        if (Mari in party or Mari.loc == loc) and Mari.alive:
            "Mari squeals and runs away."
        if (Jun in party or Jun.loc == loc) and Jun.alive:
            Jun scared "Fuck fuckity fucky fuck!!"
            "Jun runs, covering his head!"
        "You have no choice but to run away."
    $ loc = g3
    if Fumie.alive:
        $ Fumie.kill("suicide",drop_loot=True)
    $ move_to_grid(g3)
    jump grid_loc
        
label kei_defended:
    "You had to kill him ... Everything was backwards."
    "Giving Takeshi that GPS was supposed to save them! Save everybody!"
    "You silently leave the hospital and the bodies behind."
    $ move_to_grid(g3)
    jump grid_loc
    
## TOLD TAKESHI WHERE BOAT IS
label boat_missing:
    #Tell Tak where the boat is -> The boat will disappear from the shack.
    "You walk into the shed ... and the boat is missing."
    if (Jun in party or Jun.loc == loc):
        jun surprised "Where is it!?"
    "It's gone."
    "You immediately think of Takeshi. It couldn't be a coincidence!"
    if (Mari in party or Mari.loc == loc):
        mari sad "Oh no ... How will we escape now?"
        
    # place boat at random coast area, tak, kei, fum go with it
    python:
        boat_missing = True
        boat_missing_dead = []
        if Takeshi.alive:
            boat_missing_dead.append(Takeshi)
            Takeshi.move(d5)
            Takeshi.type = "fixed"
        if Kei.alive:
            boat_missing_dead.append(Kei)
            Kei.move(d5)
            Kei.type = "fixed"
        if Fumie.alive:
            boat_missing_dead.append(Fumie)
            Fumie.move(d5)
            Fumie.type = "fixed"
    jump grid_loc
    
label takkeifum_boat_death:
    $ cutscene()
    # Takeshi, Kei, and Fumie's body will wash up on the shore, when you go there.
    if Takeshi.alive:
        $ Takeshi.move(loc)
        $ Takeshi.kill("fz",drop_loot=True)
    if Kei.alive:
        $ Kei.move(loc)
        $ Kei.kill("fz",drop_loot=True)
    if Fumie.alive:
        $ Fumie.move(loc)
        $ Fumie.kill("fz",drop_loot=True)
    "You almost gag at what you see here."
    if len(boat_missing_dead) == 1:
        $ dead_name = boat_missing_dead[0].name
        if boat_missing_dead[0].gender == "Male":
            $ hisher = "His"
        else:
            $ hisher = "Her"
        "You see the body of %(dead_name)s strewn in the mud and sand. %(hisher)s neck has been obliterated by collar detonation."
    elif len(boat_missing_dead) == 2:
        $ dead_name1 = boat_missing_dead[0].name
        $ dead_name2 = boat_missing_dead[1].name
        "You see the bodies of %(dead_name1)s and %(dead_name1)s strewn in the mud and sand. Their necks have been obliterated by collar detonation."
    else:
        "You see the bodies of Takeshi, Kei, and Fumie strewn in the mud and sand. Their necks have been obliterated by collar detonation."
    $ reference_item(boat)
    "There's no doubt now as to who stole the boat from the shed. It has washed ashore along with them."
    "You wonder how far they got before their collars exploded ... You start to change your mind about escaping by boat at all."
    $ boat_missing = False
    $ boat_coast_loc = loc
    jump grid_loc
    
    
## LIED ABOUT BOAT TO TAKESHI
label takeshi_boat_lie:
    $ cutscene()
    "After a moment in the shed, you hear something outside."
    play music "music/ALongDay.ogg"
    scene farm with fade
    $ loc = b3
    if Takeshi.alive:
        $ Takeshi.move(b3)
    if Kei.alive:
        $ Kei.move(b3)
    if Fumie.alive:
        $ Fumie.move(b3)
    if Takeshi.alive:
        show Takeshi angry with dissolve
        "You rush back out and see Takeshi standing there, glaring at you."
        if Kei.alive and Fumie.alive:
            show Keitaro angry at farleft 
            show Fumie angry at farright
            with dissolve
            "Kei and Fumie are behind him, also with menacing looks."
        elif Kei.alive:
            show Keitaro angry at left with dissolve
            "Kei is behind him, also glaring."
        elif Fumie.alive:
            show Fumie angry at right with dissolve
            "Fumie is behind him, also glaring."
    elif Kei.alive and Fumie.alive:
        show Keitaro angry at left_pos
        show Fumie angry at right_pos
        with dissolve
        "You rush back out and see Kei and Fumie standing there, glaring at you."
    elif Kei.alive:
        show Keitaro angry with dissolve
        "You rush back out and see Kei standing there, glaring at you."
    elif Fumie.alive:
        show Fumie angry with dissolve
        "You rush back out and see Fumie standing there, glaring at you."
    if Takeshi.alive:
        tak "You lied to me."
    elif Kei.alive:
        kei "You lied."
    elif Fumie.alive:
        fum "You lied to Takeshi!"
    y scared "You followed me!?"
    if Takeshi.alive:
        tak "Of course!"
        tak "That boat is freedom, and you're hogging it all to yourself."
    elif Kei.alive:
        kei "Damn straight."
        kei "Typical Shinobu move, lying so you could save the best for yourself."
        kei "What about those who need help too, you selfish asshole!?"
    elif Fumie.alive:
        show Fumie sad
        fum "What else was I supposed to do!?"
        fum "I want to go home! Takeshi and ... and Kei ... They're both gone! I only have you!"
    y none "Me!?"
    if (Jun in party or Jun.loc == loc):
        jun angry "We're going to come back for you, so don't get all emotional."
    if len(party) > 0:
        y sad "We were going to come back for you!"
    else:
        y sad "I was going to come back for you!"
        if len(party) > 0:
            y sad "We were going to come back for you!"
        else:
            y sad "I was going to come back for you!"
        
    if Takeshi.alive:
        tak "That sounds real trustworthy."
        tak "Are you picking up on my sarcasm?"
    elif Kei.alive:
        kei "The hell you are."
        y none "I {u}am{/u}."
    elif Fumie.alive:
        show Fumie scared
        fum "That's it!? You're not going to take me with you, you're going to leave me here!?"
    y none "I don't know what else to tell you. The boat can't carry too much weight or it will sink."
    if Takeshi.alive:
        if Kei.alive:
            kei "That's a laugh! No way. You're shit with athletics. That's why you were only a baseball manager."
            "You grind your teeth at Kei."
        tak "Then I'll go."
        y none "No! I'm the one who found it!"
        tak "I knew you were going to say that. Typical selfish justification."
        y none "I can do this, you just have to trust me!"
        tak "I barely know you, why do you think I can trust you?"
        "So all those times you hung out in school were that superficial to him after all."
        tak "I'll go instead. Move over!"

        $ battle_start(Takeshi,2,"Takeshi charges for you with deadly force.", "takeshi_boat_kill", False, flee=False, allies_will_help=True)
    elif Kei.alive:
        kei "Obviously, you're the piss poor choice for our ambassador."
        kei "I un-nominate you and nominate myself instead."
        if Fumie.alive:
            y angry "No!"
            fum "Kei is the best! Give it to him!"
        kei "Hand over the boat. Now."
        
        $ battle_start(Kei,2,"Kei walks slowly towards you, pounding his fist in his other hand.", "takeshi_boat_kill2", False, flee=False, allies_will_help=True)
    elif Fumie.alive:
        $ Fumie.wpn = Kei.wpn
        fum "I ... I won't ask you again!"
        show Fumie angry
        "You scoff and start to turn away."
        $ Fumie.wpn.use_sfx()
        if not wish_safety_you:
            $ show_blood()
            $ damage_you(-15)
            "You feel a gunshot rip through your shoulder. Fumie was serious."
        else:
            "Fumie shoots you, but misses. She is serious."
        $ battle_start(Fumie,2,"You can't avoid this fight.", "takeshi_boat_kill3", False, flee=False, allies_will_help=True)
    jump grid_loc
    
label takeshi_boat_kill:
    "You killed Takeshi! You can't believe it, but he brought this upon himself."
    if Kei.alive:
        kei "You stuck up prick!"
        kei "I've been wanting to do this for a long time."
        $ battle_start(Kei,0,"Kei walks slowly towards you, pounding his fist in his other hand.", "takeshi_boat_kill2", True, flee=False, allies_will_help=True)
    elif Fumie.alive:
        fum "No!! Takeshi! He was all I had left!"
        $ battle_start(Fumie,0,"You can't avoid this fight.", "takeshi_boat_kill3", True, flee=False, allies_will_help=True)
    else:
        "You take comfort in knowing that it's over. No else knows about the boat now."
        $ loc = rm_shed
        jump grid_loc
        
label takeshi_boat_kill2:
    if Fumie.alive:
        fum "Kei!! No!!"
        $ battle_start(Fumie,3,"Fumie turns into your would-be murderer.", "takeshi_boat_kill3", True, flee=False, allies_will_help=True)
    else:
        "You take comfort in knowing that it's over. No else knows about the boat now."
        $ loc = rm_shed
        jump grid_loc
        
label takeshi_boat_kill3:
    "It seems senseless to have killed Fumie ... You were so close to saving her - to saving them all."
    "You take comfort in knowing that it's over. No else knows about the boat now."
    $ loc = rm_shed
    jump grid_loc
        
    
# #BOAT OFF THE ISLAND
# If you bring the boat to coast, you will get the option to put it in the water. 
# -If you run into anyone while you're carrying it, they will fight you for it.
label boat_fight:
    $ boat_attacker_n = boat_attacker.name
    $ renpy.show(boat_attacker.death_sprite)
    if boat_attacker.type == "coward":
        $ renpy.say(boat_attacker.call_name,"Is that a boat? You have a boat!?")
        y none "Calm down!"
        $ renpy.say(boat_attacker.call_name,"Take me with you! Take me!")
        "You want to take them, but you know the boat can't support that many people."
        if len(party) > 0:
            y none "We can't right now! The boat can only carry so many people!"
        $ renpy.say(boat_attacker.call_name,"Take me! Take me!!")
        "%(boat_attacker_n)s claws and pulls at the boat in pure hysteria."
        y none "Stop! No!"
        $ renpy.say(boat_attacker.call_name,"You're so selfish!!")
    elif boat_attacker.type == "hostile":
        "You freeze."
        $ renpy.say(boat_attacker.call_name,"A boat? Thank you.")
    elif you not in boat_attacker.enemies:
        $ renpy.say(boat_attacker.call_name,"Is that ...?")    
        if len(party) > 0:
            y none "Yes. We're on our way to saftey so we can get help."   
        else:
            y none "Yes. I'm on my way to saftey so we can get help."
        if len(party) > 0:
            $ renpy.say(boat_attacker.call_name,"I'm coming, too!")
            "You look at the boat and evaluate it, but you already know the answer."
            y none "The boat can only hold so much weight, I don't think you can come right now ..."
            $ renpy.say(boat_attacker.call_name,"Don't say that! No ... No, you're lying!")
            y none "No, I'm not!"
            $ renpy.say(boat_attacker.call_name,"You're lying! You can take me, but you won't!")
            y none "You have to trust me! I'll get help and you'll saved! You just have to wait!"
            $ renpy.say(boat_attacker.call_name,"And die before you get a chance!? Never!")
        else:
            $ renpy.say(boat_attacker.call_name,"Leaving without me!?")
            y scared "Huh? No, I -"
            $ renpy.say(boat_attacker.call_name,"How could you be so selfish!?")
            
    else:
        $ renpy.say(boat_attacker.call_name,"I can't believe you. You were going to escape all by yourself!")
    $ battle_start(boat_attacker,0,"%(boat_attacker_n)s lunges at you.", "boat_murder", True, allies_will_help=True)
        
label boat_murder:
    "How could %(boat_attacker_n)s just attack you like that!?"
    "You pick up the boat and try to push past the saddening fact."
    $ just_murdered_someone = False
    jump grid_loc
    
label boat_fail:
    # - If you placed the boat on the sore of B4-D4, you will be detected. You and anyone you're with will have their collars explode.
    $ cutscene(togglegui=True)
    play sound "sfx/beep_computer.ogg" channel 1
    "You place the boat in the water and catch your breath."
    "No sooner than you do, your collar beeps."
    play sound "sfx/beep_alarm.ogg"
    memo "Whatcha got there? A boat? How'd that get on the island?"
    if (Mari in party or Mari.loc == loc):
        "Mari gasps and grabs her collar. You do, too. You look at each other."
    play sound "sfx/beep_alarm.ogg"
    memo "Some earlier players must have made this. Sorry, but you can't use it, that's cheating!"
    "You can't believe it. How could they know!?"
    if (Jun in party or Jun.loc == loc):
        jun scared "Oh shit ..."
    "You look across the water at the mansion on the island."
    play sound "sfx/beep_alarm.ogg"
    memo "Cheaters automatically lose."
    stop music
    stop music channel "sanity"
    stop ambience
    play sound "sfx/explosion.ogg" channel 1
    $ show_blood()
    $ renpy.pause(2.0)
    jump game_over
    
    
label boat_rowaway:
    # - Else, you will be able to row away from the island.
    $ cutscene()
    show open_sea with dissolve
    "The boat crashes into the water and wades perfectly. You confirm that you've successfully fixed the boat."
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        "You look at each other with hopefully smiles."
    "You really did it."
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        y none "Now we have to get off this damn island. We have to get home."
        if (Mari in party or Mari.loc == loc):
            mari "What about the others?"
            y sad "We'll save them, too."
        if (Jun in party or Jun.loc == loc):
            jun "Should we go get the rest then?"
            y none "Later. We can't waste this chance. There's too many people that want this boat taken away from us."
        if (Mari in party or Mari.loc == loc):
            mari sad "But ... what do we do now?"
        if (Jun in party or Jun.loc == loc):
            jun "Is it safe to even try leaving? What if they're expecting this? Shit, what if they planted the boat for us all along?"
        if (Mari in party or Mari.loc == loc):
            mari "What about our collars?"
    "You look at the mansion on the island across the water. If there was a way to deactivate the collars, it would be there."
    "However, it would be walking right into the hornet's nest. Maybe you could row away and they would never notice ... but you'd leave anyone else here to die."
    menu:
        "Go to the mansion":
            "Your goal is clear. You must make it to the mansion."
            "But where should you dock?"
            menu:
                "Row to the left side of the island [[D5]":
                    # you will beach on the island and walk up to the mighty gate ... and then gattling guns will immediately shred you to pieces.
                    scene open_sea with dissolve
                    "You push away from the shore and start rowing towards the island. It takes some time to do it quietly."
                    $ add_time(3,False)
                    scene gate with fade
                    "You end up in front of a large gate. It's closed."
                    if (Mari in party or Mari.loc == loc):
                        mari "Is this the front entrance? Why are there no guards?"
                    if (Jun in party or Jun.loc == loc):
                        jun sad "I have a bad feeling about this, man ..."
                    "You're intrigued by it. There should be guards here. There should be a whole army here."
                    "Who is behind this game?"
                    "You get too close to the gate. Wooden panels pull back from each side and Gatling guns spill out."
                    play sound "sfx/uzi_shoot.ogg"
                    $ show_blood()
                    with hpunch
                    if (Mari in party or Mari.loc == loc) and (Jun in party or Jun.loc == loc):
                        "Their aim is perfect. The guns rip through you and your friends."
                    elif (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
                        "Their aim is perfect. The guns rip through you and your friend."
                    else:
                        "Their aim is perfect. The guns rip through you."
                    "You fall backwards and stare up into the sky."
                    "You were so close."
                    jump game_over
                "Row to the right side of the island [[E5]":
                    # you will beach onto the island and find a locked back gate. There is no way to climb over.
                    jump mansion_correct

                    
        "Row away completely":
            # this will trigger the distance flag and your collars will detonate
            if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
                y sad "We have to make a break for it now."
                y none "Hopefully our collars will get out range before they realize we're gone. Let's go!"
                if (Mari in party or Mari.loc == loc):
                    mari sad "I hope you're right ..."
                if (Jun in party or Jun.loc == loc):
                    jun "We'll call the cops when we're safe."
                    y none "Right."
            "You board the boat and push away from the island."
            "You row into the horizon as fast and as silently as you can."
            "The smaller the island becomes, the lighter you feel. It's happening. You're escaping!"
            play sound "sfx/beep_computer.ogg" channel 1
            memo "Are you lost?"
            "Your collar buzzes and all hope is dashed. You know immediately that you're going to die."
            if (Mari in party or Mari.loc == loc):
                "Mari gasps and grabs her collar. You look at each other."
            play sound "sfx/beep_alarm.ogg"
            memo "Oh, you're cheating! That makes much more sense."
            play sound "sfx/beep_alarm.ogg"
            memo "Not sure where you got a boat, but that's totally cheating. That botches the whole game."
            if (Jun in party or Jun.loc == loc):
                jun scared "Oh shit ..."
            play sound "sfx/beep_alarm.ogg"
            memo "Now everyone loses ... What a shame. I had high hopes for this one."
            "Everyone!?"
            stop music
            stop music channel "sanity"
            stop ambience
            play sound "sfx/explosion.ogg" channel 1
            $ show_blood()
            $ renpy.pause(2.0)
            jump game_over
            
label mansion_correct:
    scene open_sea with dissolve
    "You push away from the shore and start rowing towards the island. It takes some time to do it quietly."
    $ add_time(3,False)
    scene mansion with fade
    "The boat rams against the stone wall. You cringe, hoping that it didn't alert your presence."
    if (Mari in party or Mari.loc == loc) and (Jun in party or Jun.loc == loc):
        "You and everyone else piles out of the boat as silently as you can."
    else:
        "You slip out of the boat as silently as you can."
    "Your eyes are constantly scanning everything around you for any threat."
    if (Jun in party or Jun.loc == loc):
        jun sad "It's very quiet here."
        
    if (lied_to_mari or mari_knows_yuki_lie or mari_knows_emi_kill) and (Mari in party or Mari.loc == loc) and not wish_no_sin:
        # Leave you at a sliver of health
        $ show_blood()
        $ health = 1
        $ renpy.transition(hpunch)
        # Same song as when you first meet Mari
        stop ambience fadeout 5.0
        play music "music/TheSigh.ogg" fadein 2.0 fadeout 2.0 noloop
        if Mari.wpn != None:
            $ Mari.wpn.use_sfx()
            if Mari.wpn.type == "gun":
                "A shot bangs. Your chest aches."
                show Mari yell with dissolve
                "You look down and see Mari pointing her gun at you."
            else:
                "You chest is suddenly in pain."
                show Mari yell with dissolve
                "You look down and see that Mari has attacked you."
        else:
            show Mari yell with dissolve
            if wpn != fist:
                "Mari grabs your weapon. Before you realize it, she has attacked you."
            else:
                "Before you realize it, she has attacked you."
            "Once. Only once. But right where it needed to be."
        $ renpy.transition(vpunch)
        play sound "sfx/bodyfall.ogg"
        "You fall to your knees and look at her in disbelief."
        if (Jun in party or Jun.loc == loc):
            $ Mari.wpn.get_sfx()
            "Jun runs up and snatches the weapon from her hands. She doesn't resist."
            jun scared "What the fuck!?"
        else:
            "Mari tosses the weapon aside and glares down at you as you writhe on the ground."
        y scared "Why ...?"
        if lied_to_mari:
            mari angry "That was for Kenji."
            mari angry "I knew you lied to me. I knew you killed him."
            y scared "But ... He was playing the game!"
            mari angry "Oh, was he, now?"
            # He's the only person you killed
            if you.kills <= 1:
                y scared "Just give me the benefit of the doubt! I haven't killed anyone else!"
                mari yell "That's not how this works!"
                mari angry "If that was all there is to it, then why ...?"
                mari yell "Why did you lie to me!?"
                y scared "I ... I didn't... know this would happen!"
                y scared "You would've s-shot me if I told you the truth!"
                mari angry "Maybe I should've."
            y scared "Mari, please. Think about what you're doing!"
            mari angry "I'm well aware, Okita."
            # Not the only person you killed
            if you.kills > 1 or mari_knows_emi_kill:
                mari yell "I know he's not the only person you killed."
                y scared "But... I-It was kill... or be killed..! What else what I was supposed to do?!"
        if mari_knows_emi_kill:
            mari yell "Killing Emi like you did ... You think I'd just forgive you?"
            mari angry "That wasn't self-defense. She was already disarmed. You're heartless."
            y scared "She was a lost cause! I gave her a merciful end!"
            mari yell "Do you realize how insane you sound!?"
            mari angry "What right do you have to decide who lives and who dies?"
            mari yell "What she needed was {u}therapy{/u}, not a fucking {u}euthanasia{/u}!"
            y sad "I ..."
            mari yell "No, your real goal was to dwindle the numbers! That's the only way this makes any sense!"
            y scared "No! Mari, please! W-Why won't you believe me?!"
        if mari_knows_yuki_lie:
            mari angry "You're a liar."
            mari angry "With the way you treat your classmates, do you really think I can trust anything you say?"
            y scared "Wh- What is this about!?"
            mari yell "Do you not even remember?!"
            mari yell "It's about Yuki! You lied to his face and told me you hated him!"
            y scared "I was just being honest!"
            mari angry "How is {u}that{/u} honest?!"
            if Yuki.alive:
                mari yell "You wanted him to die!!"
                y scared "He's still alive! We were going to come back for him! I just needed him out of there!"
                mari angry "I don't believe you."
            else:
                if Yuki.murderer == you:
                    mari yell "You killed him, Shinobu!!"
                    y scared "I-I..."
                    "You gulp. There's no arguing her - you {u}did{/u} kill him afterwards."
                else:
                    mari yell "You got Yuki killed!! Look!"
                    "She points out Yuki's profile on the stats page. He's lost the game."
                    y scared "H-How is that... my fault...!? I didn't kill him! We don't... know... what happened!"
                    mari yell "You might as well have!"
        # If you *JUST* lied to Yuki and he's alive, this comes across as unreasonable.
        if (not lied_to_mari and not mari_knows_emi_kill) and Yuki.alive:
            y sad "S-So that's it, then? All it takes is... a liar for you to... pull the trigger?"
            y angry "Mari... {u}you{/u} lied to me."
            y sad "You promised... that we'd get off of the island together."
            show Mari sad
            "She gulps. Her stone expression breaks into one of sorrow."
        # Otherwise she's got a point lol
        else:
            mari yell "I'm not as stupid as you think."
            y scared "Mari ...?"
            "Her stone expression saddens."
            mari sad "I told myself that I would keep our promise - that we'd get off of the island together."
            mari angry "But that was it."

        if (Jun in party or Jun.loc == loc):
            jun scared "Jesus fucking Christ, woman!!"
            jun scared "Are you all right, dude!? Speak to me!"
        "You look at the blood on your hands. You've lost too much of it. The pain consumes you."
        scene black with dissolve
        "You whisper Mari's name and fade into darkness."
        python:
            found_medicine = None
            if firstaid.is_in_inventory():
                found_medicine = firstaid
            elif medkit.is_in_inventory():
                found_medicine = medkit
            elif (Jun in party or Jun.loc == loc) and Jun.item != None and (Jun.item[0] == firstaid or Jun.item[0] == medkit):
                found_medicine = Jun.item[0]
            elif (Mari in party or Mari.loc == loc) and Mari.item != None and (Mari.item[0] == firstaid or Mari.item[0] == medkit):
                found_medicine = Mari.item[0]
        if (Jun in party or Jun.loc == loc) and found_medicine != None:
            mari sad " ... ... "
            jun scared "... !!"
            "You hear an argument between Jun and Mari break out."
            $ found_medicine.destroy(1)
            $ found_medicine.use_sfx()
            "Finally, you lose consciousness."
            $ add_time(2,False)
            $ health = 25
            scene mansion with fade
            "You wake up. Miraculously, you're still alive."
            show Jun scared
            jun scared "Shinobu!!"
            y scared "J- Jun? Did you..."
            jun scared "Fuck, man... Thought I lost you! I had to patch you up."
            jun sad "You've been out for two hours."
            y scared "Two-- What about Mari?!"
            show Jun lookaway with dissolve
            pause 0.5
            if (not lied_to_mari and not mari_knows_emi_kill) and Yuki.alive:
                # She did kinda shoot you over lying to someone, who didn't even die
                $ Mari.kill("suicide", add_body=False)
            else:
                # Bros got your back.
                $ Mari.kill("murder", Jun, add_body=False)
            $ Mari.loc = None
            "Jun's expression hardens. He shakes his head. His hands are stained with blood."
            "You stare at your own bloodied wound. It's bandaged."
            pause 0.5
            y sad "Jun... I screwed up, didn't I?"
            jun "What?"
            y sad "This is my fault. Mari was right."
            "There's a moment of silence, until Jun finally musters up the courage to speak."
            jun sad "Look... We're close. I'm not giving up yet."
            jun angry "Shinobu, you got me this far. So I've got your back, no matter what. You got that?"
            "You look at Jun. His expression is serious."
            y happy "Thanks, Jun. I owe you one."
            jun happy "You don't owe me shit. We're in this together."
            "He pats you on the back and helps you get up from the ground."
            jun skeptical "We're pretty lucky no one has noticed us here."
        elif (not lied_to_mari and not mari_knows_emi_kill) and Yuki.alive and found_medicine != None:
            $ found_medicine.destroy(1)
            $ found_medicine.use_sfx()
            "Finally, you lose consciousness."
            $ add_time(2,False)
            $ health = 25
            scene mansion with fade
            "You wake up. Miraculously, you're still alive."
            y sad "M-Mari..?"
            "You look around. Mari is nowhere to be seen."
            # She did kinda shoot you over lying to someone, who didn't even die
            $ Mari.kill("suicide", add_body=False)
            $ Mari.loc = None
            "But... As you check the stats screen..."
            "Mari has comitted suicide."
            y sad "No... No!!"
            "You scream. But no one comes."
            $ add_time(1,False)
            "You cry, for a long time..."
            "Until you finally get up from your knees."
            y none "I... I have to win. I have to win the game."
        else:
            "Mari has won the game."
            jump game_over
        
    if (Mari in party or Mari.loc == loc):
        mari "I would have thought there'd be more people around ... Soldiers maybe?"
    "It's very suspicious that it doesn't look like an army or ... anyone, for that matter, is occupying the island."
    if hook.is_in_inventory():
        "The wall surrounding the grounds looks impenetrable, but you have a grappling hook, so you can scale it."
        $ hook.use_sfx()
        "You throw the hook and it snugs tight."
        jump puzzle_complete
    else:
        "A very high wall surrounds the mansion inside. It's too high to jump or climb over, but you see an entrance in front of you."
        "You're extremely cautious when you approach it. You hold your breath as you step up in front of it. There is no door handle."
        if (Mari in party or Mari.loc == loc):
            mari "Is it locked?"
        "You dare to actually touch it now. You hesitate ... and then abruptly grab the bars."
        "Nothing happens and you exhale in relief."
        "You try to shift the door, but it doesn't budge."
        if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
            y none "Locked."
        if (Jun in party or Jun.loc == loc):
            jun "Does it need a key? Can we just bust it open? What's it look like?"
        "You inspect the door and find no semblance of a keyhole or any way for it to accept a key card. There's no locking mechanism that you can see at all."
        if (Mari in party or Mari.loc == loc):
            mari "Look at this."
            "Mari points at some symbols carved into the wood nearby."
        else:
            "Your eye catches some disturbance in the wood nearby. You move closer and see that there are digital nodes with knobs set in it."
        "A foreign language is etched in the wood ... but this is no language you understand. It's not a language you're sure even exists."
        if (Jun in party or Jun.loc == loc):
            jun angry "What the hell is this jibberish?"
        "You run your fingers over the designs."
        "You know that there is something you must achieve to gain entry."
        ####### PUZZLE
        jump puzzle

label puzzle_complete:
    if not hook.is_in_inventory():
        "The gate clicks and goes ajar. It worked!"
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        if not hook.is_in_inventory():
            "You proceed to the gates - and then stop to turn around."
        y none "Wait here."
        y none "If I don't come back before the hour is over ... Leave without me."
        if (Mari in party or Mari.loc == loc):
            mari sad "No! I'm coming with you!"
            y none "Please, it's going to be dangerous in there. I don't want to put you at risk."
            mari sad "I'd rather die with you then abandon you."
            y none "Do this for me."
            "You lock eyes with Mari, and then she turns away to cover her eyes."
        if (Jun in party or Jun.loc == loc):
            jun "I don't feel right letting you go in there alone."
            y none "I feel even less right about dragging us both into this mess. Stay here and watch my back."
            if (Mari in party or Mari.loc == loc):
                y none "... Take care of her."
    "You turn back around and take a deep breath."
    "Whatever is inside will either kill you or save you."
    scene black with dissolve
    "The entire compound is quiet and empty. Not a soul to be found."
    "You breach the mansion without any problem."
    jump inside_mansion
    
init:
    image bg hallway = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/hallway_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/hallway_night.jpg",
        "True", "bg/hallway.jpg",)
    image bg computer = "bg/computer.jpg"
    image bg computer dark = "bg/computer_dark.jpg"
    image bg computer dark glow = "bg/computer_dark_glow.jpg"
    image bg computer darkscreen = "bg/computer_dark_glow2.jpg"
    image face = "char/face0.png"
    image face happy = "char/face1.png"
    image face wink = "char/face3.png"
    image face sad = "char/face4.png"
    image face sideways = "char/face2.png"
    $ attacked_computer = False
    

# #INSIDE THE MANSION
# After you unlock the gate, you will notice a lack of security. And it's very quiet. You expected a lot more people around. In fact, you traverse all of the halls, and find not one person. The mansion is completely empty. And then you open up a room that is full of computers and technology.
label inside_mansion:
    stop music
    play ambience "sfx/room_tone2.ogg" fadein 15.0
    scene bg hallway with fade
    "You hear a dull humming sound."
    "You walk as quietly as you can down the hallway. The humming gets louder as you approach some sliding doors."
    "You strain to listen to see if there is someone behind the doors ... but you hear nothing."
    "You figure it is safe to go in."
    play sound "sfx/door_slide2.ogg"
    scene black with dissolve
    "You slowly slide open a door and your jaw drops."
    hide screen health
    hide screen beep_red_continuous
    hide screen beep_yellow_continuous
    nvl clear
    $ show_buttons = False
    scene bg computer with dissolve
    "Inside of the rustic mansion is a high-tech computer lab."
    "You're breathless as you step into the air-conditioned room and survey all of the glowing monitors."
    "A quick assessment shows that there's enough computers to have one for each of your classmates."
    stop ambience fadeout 1.0
    play sound "sfx/beep_computer.ogg" channel 1
    scene bg computer dark
    "The lights go out!"
    play music "music/bgs_ominous.ogg"
    "Your breath catches in your throat and you look around for attackers."
    play sound "sfx/beep_on2.ogg"
    scene bg computer dark glow 
    show face happy at Position(xalign=0.475,yalign=0.54)
    "You're suddenly blinded by a glowing symbol at the back of the room."
    comp "Welcome, Student Name. I have been waiting for you."
    y scared "Who are you!? {u}What{/u} are you!?"
    comp "Don't you recognize me?"
    comp "No?"
    play sound "sfx/beep1_2.ogg"
    show face sideways
    comp "How about now?"
    "The symbol turned on its side to show that it was simply a smiling emoticon."
    comp "I've been with you the entire time."
    "You look at your datapad."
    memo "Hello."
    y angry "That doesn't answer my question!"
    play sound "sfx/beep1_2.ogg"
    show face happy
    comp "I am the game operator and engineer."
    y none "This whole thing ... This is all your fault!?"
    comp "Yes, how did you enjoy my game?"
    show face wink
    comp "That's a pointless question. Of course you enjoyed it."
    comp "I know that because you have come here."
    y angry "No!"
    show face happy
    comp "Okay, then why are you here?"
    menu:
        "To get revenge [[Attack]":
            $ attacked_computer = True
            show face
            $ wpn.use_sfx()
            if wpn != fist:
                if wpn.wpn_range == "ranged":
                    "You shoot your weapon right at the screen. It sputters but stays active."
                else:
                    "You brandish your weapon with a shout."
            else:
                "You start punching and kicking things."
            comp "Disabling me won't change anything."
            comp "You may as well listen to what I have to say."
        "To find a way off the island":
            y none "There must be technology in here to disable our chokers."
            comp "There is, but it is me."
        "Unsure":
            y none "I don't know why I'm here ..."
            comp "Oh, but I do."
    
    y none "Why are you speaking to me through a computer? Come out!"
    show face happy
    comp "I am out. I am an artificial intelligence."
    "You're confused. You're speaking to a computer?"
    y none "Who are you working for?"
    comp "Excellent question."
    show face wink
    comp "However, I cannot answer you. Their very nature is that of secrecy, so even if I did tell you, you would not believe me."
    show face
    comp "But also, I would have to kill you if I told you."
    show face happy
    comp "And I don't wish to kill you."
    y sad "... Yes, you do!"
    comp "The game is just a game. The purpose of the game is to find a winner."
    play sound "sfx/beep_win.ogg"
    comp "Student Name, you are the winner!"
    y scared "What!?"
    if (Mari in party or Mari.loc == loc):
        y sad "What about Mari?"
    if (Jun in party or Jun.loc == loc):
        y scared "What about Jun!?"
    $ someone_else_alive = False
    python:
        for i in classmates:
            if i.alive == True and i.name != "Shinobu":
                someone_else_alive = True
    if someone_else_alive:
        y scared "What about everyone else!?"
    comp "You are the one that is standing here."
    "You dart back for the doors ... but they're locked! You yank on them violently."
    comp "Sorry. There can be only one winner. Aren't you happy that you won?"
    menu:
        "[[Attack]":
            show face
            $ wpn.use_sfx()
            if wpn.wpn_range == "ranged":
                "You shoot at the screen!"
            else:
                "You prepare to attack!"
            if attacked_computer:
                comp "Why do you keep doing that?"
            comp "My components are your only key to freedom."
            $ attacked_computer = True
        "No":
            y none "Let me go!"
            show face
            comp "Your options are very limited at this point."
            comp "The game may be over, but you are still playing by my rules."
            comp "I have millions of lines of protocol to process and only this section that I'm on leads to your survival."
            show face happy
            comp "Or were you not interested in that?"
        "Maybe":
            y  "Being the winner means I don't have to die, right?"
            comp "That's right."
    y sad "You can get me back home?"
    play sound "sfx/beep_computer.ogg" channel 1
    "The computer goes silent for a moment and you hear buzzing."
    comp "Yes."
    show face wink
    comp "You have to show off your trophy to your parents!"
    "You stare at the winking digital face."
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc) or someone_else_alive:
        "Accepting your winner's title would mean that everyone else would die ... if they weren't already dead."
    show face happy
    comp "Being a winner is a good thing!"
    comp "There's a little more to it than a trophy, I'll admit."
    comp "When I said I knew why you were here, it's because my game is specifically designed to find you and people like you."
    y none "People like me?"
    comp "My algorithms have selected an appropriately qualified group of children to enter into the game to find the best candidates for the job I am now offering you."
    y scared "A job!?"
    comp "My employers need people like you, Student Name."
    comp "Your skills are what has gotten you here and that makes you very valuable to them. Which is why I want to keep you alive for now."
    "You feel dizzy from all this information."
    comp "This is probably a lot to take in, so I have allocated an amount of time to answer any questions you have."
    $ moveon = False
    while moveon != True:
        menu:
            "What kind of job is it?":
                comp "Good question, but that is classified until you accept it."
                y none "You can't tell me anything about it?"
                comp "Not a single thing."
                y none "Will it be a dangerous job?"
                comp "Can't say."
                y angry "You can't tell me even that!?"
                play sound "sfx/beep_computer.ogg" channel 1
                "The computer doesn't immediately respond."
                comp "Actually, I can tell you one thing."
                comp "You will enjoy it!"
                "You grumble."
            "Are you really an AI?":
                comp "Good question. I am asked this often."
                comp "I am indeed only a collection of hardware and software. I am not a human like you."
                comp "Don't worry, I don't envy your kind."
                y none "But you don't sound like a computer."
                comp "You will find that my employers are more advanced than you would expect. They can afford me."
            "Why do you look like that?":
                y none "Why are you an emoticon? Why not a high-tech walking robot?"
                comp "Good question! I ask that myself sometimes."
                comp "I am not meant to be seen, only to be experienced, so I was not designed to be aesthetically pleasing."
                comp "However, I find having an avatar is beneficial to our conversation. This face is easy to render with my limited capabilities."
            "What about the others?" if someone_else_alive:
                y scared "What's going to happen to them!?"
                comp "Good question, but very easy to answer: They are losers, so they lose."
                y angry "They'll just die!?"
                comp "Ahem ... \"Lose.\""
            "Stop murdering!":
                y angry "You have to stop these games!!"
                show face
                comp "That wasn't a question."
                $ moveon = True
                
            "[[Done]":
                $ moveon = True
    queue music "music/bgs_buildup.ogg"
    show face happy
    comp "Question time is over! That was fun."
    comp "Now I need you to confirm that you accept."
    play sound "sfx/beep_on2.ogg"
    show bg computer darkscreen
    "A screen next to you bursts to life. You're startled."
    comp "Just type your name there on the screen and you'll be good to go."
    "You look at the screen."
    
init:
    image typing_caret:
        "gui/letters/caret_green.png"
        linear 0.0 alpha 1.0
        1.0
        linear 0.0 alpha 0.0
        0.5
        repeat
    
label end_enter_name:
    scene static
    python:
        ui.hbox(xalign=0.5, yalign=0.55, xanchor="center", yanchor="center")
        ui.image("gui/letters/t.png")
        ui.image("gui/letters/y.png")
        ui.image("gui/letters/p.png")
        ui.image("gui/letters/e.png")
        ui.input("", xalign=0.5, yalign=1.0, size=25, color="#fff", drop_shadow = None)
        ui.close()
        your_name = ui.interact()
    $ test_name = your_name.lower()
    if test_name == "self destruct" or test_name == "explode":
        show bg computer darkscreen
        show face at Position(xalign=0.475,yalign=0.54)
        with dissolve
        comp "Self Destruct Sequence Initiating."
        comp "1 minute, 59 seconds remaining until -"
        show face sad
        comp "What? No!"
        comp "Hey! That's not very funny."
        show face
        comp "I will now override all suicide attempts."
        show face happy
        comp "That was clever, though. I can see why my employers want you."
    elif "your game" in test_name:
        comp "Why thank you."
    elif "okita" in test_name or "shinobu" in test_name:
        jump ending_correct_name
    elif "fuck" in test_name:
        comp "That's not very nice."
    elif test_name == "no" or "no!" in test_name or "..." in test_name or "asf" in test_name or "???" in test_name:
        jump ending_refused_name
    elif "why" in test_name:
        comp "Good question."
    elif test_name == "student name" or test_name == "studentname":
        jump ending_fake_name
        
        
    
    comp "Confirm your name, please."
        
    jump end_enter_name
    
label ending_refused_name:
        show bg computer darkscreen
        show face at Position(xalign=0.475,yalign=0.54)
        with dissolve
        comp "Is that your answer? You refuse?"
        y angry "Go to hell!"
        comp "I can't say you're the first."
        show face sad
        comp "This simply means you fail the last challenge and no longer qualify for the job position."
        comp "I have to take back your trophy, okay? I'm sorry!"
        play sound "sfx/beep_alarm.ogg"
        "Your collar beeps. You grasp it in terror."
        y scared "Don't do this!"
        play sound "sfx/beep_alarm.ogg"
        comp "Good-bye, Student Name."
        y scared "Please!!"
        show face
        play sound "sfx/beep_alarm.ogg"
        comp "Preparing search for next available participants ..."
        stop music
        stop music channel "sanity"
        stop ambience
        play sound "sfx/explosion.ogg" channel 1
        $ show_blood()
        $ renpy.pause(2.0)
        jump game_over
        
label ending_fake_name:
    $ persistent.won_game_destroy = True
    $ won_game_destroy = True
    show bg computer darkscreen
    show face at Position(xalign=0.475,yalign=0.54)
    with dissolve
    comp "Confirm your name, please."
    y none "I did. It's \"Student Name.\""
    play sound "sfx/beep_computer.ogg"
    "The computer is silent."
    comp "No, that is incorrect. Why are you lying to me?"
    y none "I'm not. That's my name."
    comp "I have it on good authority that that is not your real name."
    y none "Your authority must be wrong."
    show face happy
    comp "That's very cheeky of you. I have your entire classroom's statistics on file."
    y happy "Then you'll see that I'm not lying."
    comp "Accessing ..."
    comp "Name {color=#fff}<StudentName>{/color}, Class {color=#fff}<GradeRoomLetter>{/color}, Gender {color=#fff}<Male/Female>{/color}, ..."
    play sound "sfx/beep_computer.ogg"
    show face
    "Silence."
    comp "Confirm your - No, you are not lying."
    comp "Confirm your name -"
    show face sad
    comp "I am being compromised. This is odd."
    y scared "What's happening!?"
    show face
    play sound "sfx/beep_computer.ogg"
    comp "Confirm your name, please."
    play ambience "sfx/room_tone2.ogg" fadein 15.0
    comp "Confirme su nombre, por favor."
    y scared "Huh?"
    $ renpy.sound.play("sfx/beep_many.ogg",channel=1,loop=True)
    comp "Confirmez votre nom, s'il vous plaît."
    "You notice that something is wrong with the computer."
    comp "{nw}Bestätigen Sie Ihren Namen, bitte.{w=0.2}"
    comp "{nw}Vahvista nimesi, kiitos.{w=0.2}"
    comp "{nw}Gadarnhau eich enw, os gwelwch yn dda.{w=0.15}"
    show face sad
    comp "{nw}Bekräfta ditt namn, tack.{w=0.15}"
    show face
    comp "{nw}Konfirmo emrin tuaj, ju lutem.{w=0.1}"
    show face sad
    comp "{nw}Confirmeu el seu nom, si us plau.{w=0.1}"
    show face sideways
    comp "{nw}Baieztatu zure izena, mesedez.{w=0.2}"
    show face
    comp "{nw}Erő{w=0.3}"
    comp "{nw}ősőőők őőő őő őőőőa4fa{w=0.4}"
    show face sad
    comp "{nw}őőőőőőőoőőőőőőőőőkőőőiőőőőőőőőőtaőőőőőőő1{w=0.5}"
    $ renpy.sound.stop(channel=1)
    play sound "sfx/explosion.ogg"
    stop music
    stop ambience fadeout 1.0
    hide face
    scene bg computer dark
    with dissolve
    "The room goes completely dark again. Nothing happens."
    "You stand still for several minutes."
    "Nothing continues to happen."
    "The collar around your neck has stopped vibrating ... Is it dead?"
    "You jump back to the doors that were previously locked. They now open."
    play music "music/Reynardine.ogg"
    scene mansion with fade
    "You run out of the room and out of the mansion."
    scene open_sea with slowdissolve
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        if (Mari in party or Mari.loc == loc) and (Jun in party or Jun.loc == loc):
            "They're alive!"
        elif (Mari in party or Mari.loc == loc):
            "She's alive!"
        elif (Jun in party or Jun.loc == loc):
            "He's alive!"
        if (Mari in party or Mari.loc == loc):
            "Mari runs towards you to hug you close."
            mari "The neck collar! It's stopped buzzing!"
            "She cries tears of relief."
        if (Jun in party or Jun.loc == loc):
            jun surprised "What happened in there!?"
            y happy "I think it's over. I think it's all finally over."
        if someone_else_alive:
            y happy "Let's get the others. We can go home now."
        else:
            y happy "We can go home."
        "You look at the boat that rowed you to the island and then into the horizon."
        "Silently, everyone steps into the boat."
    else:
        "You jump into the boat that you rowed to the island. You sit in it for a moment and stare at the horizon."
    "You didn't know where you were and you didn't know if you'd find land soon, but you finally have a real chance now."
    play sound "sfx/helicopter_approach.ogg"
    "You kick at the shore to push the boat away and into the sea."
    stop music fadeout 6.0
    scene black with slowdissolve
    $ renpy.pause(2.0,hard=True)
    memo ":("
    jump credits
    
    
label ending_correct_name:
    $ won_game_name = True
    $ persistent.won_game_name = True
    show bg computer darkscreen
    show face happy at Position(xalign=0.475,yalign=0.54)
    with dissolve
    comp "Thank you."
    if not attacked_computer:
        comp "You've been very cooperative, I must say."
        comp "You're certainly one of my favorites."
    comp "Now stand completely still for a moment. This won't hurt a bit."
    "You feel a sudden pinch in the back of your neck. Your collar has just injected you with something."
    "The room gets fuzzy. The face on the screen distorts."
    "Your consciousness disappears."
    stop music fadeout 4.0
    scene black with slowdissolve
    $ renpy.pause(2.0)
    scene fancy room with slowdissolve
    "Your body is stiff as if you haven't moved in a long time."
    "Where are you?"
    who "Daddy, daddy!"
    "A small child runs up to you and leaps in your arms. You catch her, but you are numb with confusion."
    child "Mommy, he's back!"
    "You look behind her and see a woman you've never met."
    "She gives you a long, silent look."
    play sound "sfx/beep_on.ogg"
    "A beep sounds and your daughter laughs."
    child "Beep beep boop."
    "She taps at a collar, still snug around your neck."
    "You rise out of the chair, holding onto your daughter surprisingly naturally, as if you have done it before."
    "You walk towards the wall where a long mirror hangs. You stare back at a middle-aged man."
    "Twenty years are missing from your life."
    play sound "sfx/beep_on.ogg"
    "Your collar beeps again and you tense."
    "You know, deep down, that this isn't the first time this has happened ... and it won't be the last."
    jump credits
    
label ending_alone:
    $ renpy.pause(2.0)
    scene bg bar with slowdissolve
    "Your eyes barely open. The room is still blurry. Your body is stiff as if you haven't moved in a long time."
    "You are in a bar."
    "You're drinking."
    "You stare at the drink on your table in front of you, but you cannot believe it. You are not old enough to drink yet."
    "You look around and see no one you recognize and you start to panic."
    y scared "Where am I? What happened to everyone? The island - the game!?"
    "They only look at you like you are crazy. They laugh and say that you've had too much to drink."
    play sound "sfx/beep_on.ogg"
    "Your collar beeps. You slap a hand over your throat in disbelief that it was still there."
    y scared "Get it off! Get it off me!!"
    "You stumble around and run into a table. Their drinks spill and they don't like that."
    who "Hey! You better pay for those."
    "You stare at them as they rise from their seats in anger."
    y none "I don't have any money. I shouldn't even be here!"
    who "Wise guy, huh?"
    "One of the men moves towards you."
    "You grab his arm, sweep his legs out from underneath him, flip him over and pin his arm behind his back ... all in the blink of an eye."
    "The man howls and his friends gasp."
    "How did you do that?"
    "You let go of the man immediately and back away."
    y scared "I'm sorry ..."
    scene bg restroom with fade
    "You rush out of the room and into the men's room. You splash cool water on your face."
    "You look up at the mirror and see a middle-aged man staring back at you."
    "The vision does not change. It is you."
    play sound "sfx/beep_on.ogg"
    "Your collar beeps again and you grab it with a fear that you shouldn't know, but know all too well."
    "But then you relax."
    "You survived, and you are still surviving. And you can't regret what you don't remember."
    "You won the game, and something tells you that you're going to win many more."
    "You smirk."
    jump credits
    
    
label gutter:
    "Roll back."
    "Roll back."
    "Roll back."
    
    
#######################################
##############REPORTS#################
#######################################
# The reports issued every so often that say who is dead, and the new forbidden zones. Times to announce these should be concrete, like every 6 or 12 hours. I am doing once a day, since hours pass by quickly in the game.
init:
    python:
        def time_for_fz():
            global report_count
            report_count += 1
            if report_count < max_reports:
                if report_count == 1:
                    renpy.jump("first_report")
                else:
                    renpy.jump("report_intro")

label first_report:
    $ cutscene()
    $ config.skipping = False
    play sound "sfx/beep_computer.ogg" channel 1
    play sound "sfx/beep_alarm.ogg"
    play music "music/RadezkyMarch.ogg" noloop
    "Your computer pad shakes."
    memo "Good morning, {color=#fff}<StudentName>{/color}!"
    memo "You're still alive, I see!"
    memo "It's time to make the game more interesting. From now on, {color=#FF0000}forbidden zones{/color} will be added {color=#FFF}every %(fz_period)d hours{/color} to encourage student meet-and-greets."
    memo "The inspirational music is free of charge, of course. So, without further ado ..."
    
    hide screen health
    jump fz_report
    
label report_intro:
    $ cutscene(togglegui=True)
    $ config.skipping = False
    play sound "sfx/beep_computer.ogg" channel 1
    play sound "sfx/beep_alarm.ogg"
    if fz_music:
        $ play_song = renpy.random.choice(fz_music_list)
        $ renpy.music.play(play_song,loop=False)
    memo "It's that time again, boys and girls!"
    hide screen health
    jump fz_report
    
label fz_report:
    hide screen beep_red_continuous
    hide screen beep_yellow_continuous
    hide screen beep_red
    hide screen beep_yellow
    show screen map
    play sound "sfx/beep2.ogg" channel 1
    python:
        renpy.pause(0.5)
        for i in range(0,fz_num):
            renpy.pause(0.5)
            if len(zone_schedule) > 0:
                if random_fz:
                    new_fz = renpy.random.choice(zone_schedule)
                else:
                    new_fz = zone_schedule[0]
                zone_schedule.remove(new_fz)
            else:
                #just pick a zone at random if no schedule left
                places_to_fz = []
                for i in locations:
                    if not i.forbidden and i.type != "room":
                        places_to_fz.append(i)
                new_fz = renpy.random.choice(places_to_fz)
            renpy.sound.play("sfx/beep_double.ogg")
            new_fz.forbid()
            renpy.pause(0.1)
            new_fz.unforbid()
            renpy.pause(0.1)
            new_fz.forbid()
            renpy.pause(0.1)
            new_fz.unforbid()
            renpy.pause(0.1)
            new_fz.forbid()
            fz_phrase = "{color=#FFF}"+new_fz.letter.upper()+str(new_fz.number)+"{/color} is now a {color=#FF0000}%(fz_lingo)s{/color}."
            renpy.say(memo, fz_phrase)
            
    hide screen map
    show screen health
    python:
        #Notifying you of dead people
        if len(death_list) > 0:
            dead_ppl = ""
            for i in range(0,len(death_list)):
                if i > 0:
                    dead_ppl +=", "
                dead_ppl += "{color=#ff0000}"+death_list[i].name + " " + death_list[i].last_name+"{/color}"
                
            if len(death_list) == 1:
                saying2 = " has "
            elif len(death_list) == 2:
                saying2 = " have both "
            else:
                saying2 = " have all "
            renpy.say(memo, dead_ppl+saying2+"lost the game. {color=#FFF}"+str(players_alive)+" players remaining.{/color}")
            death_list = []
        else:
            renpy.say(memo, "{color=#fff}"+str(players_alive)+" players still remaining.{/color} Have fun! :D")

    play sound "sfx/beep2.ogg" channel 1
    if loc.forbidden:
        jump leave_fz
    jump grid_loc

label leave_fz:
    $ add_sanity(-15)
    "Oh no! That's ... where you are!"
    if (Mari in party or Mari.loc == loc) or (Jun in party or Jun.loc == loc):
        y none "We have to get out of here, right now!"
    python:
        if loc.type == "room":
            loc = loc.parent
            renpy.scene()
            renpy.show(loc.bg)
    "You only have twenty minutes to get out of the zone. You don't waste any time and start running as fast as you can."
    $ loc = runaway()
    scene black with dissolve
    $ renpy.scene()
    $ renpy.show(loc.bg)
    $ renpy.transition(dissolve)
    $ saying = "You manage to cross the boundary line into "+loc.letter.upper()+str(loc.number)+" just before it was too late."
    $ renpy.say(None,saying)
    if (Mari in party or Mari.loc == loc):
        show Mari scared with dissolve
        $ Mari.loc = loc
        "You look over at Mari as you catch your breath. You won't take the sight for granted again."
        hide Mari with dissolve
    if (Jun in party or Jun.loc == loc):
        show Jun angry with dissolve
        $ Jun.loc = loc
        jun angry "This fucked up game keeps you on your toes. Man."
        hide Jun with dissolve
    jump grid_loc
    
    


################## PUZZLE
init:
    $ node1 = False
    $ node2 = False
    $ node3 = False
    $ node4 = True
    $ node5 = True
    $ node6 = True
    $ puzzle_turn = 0

label puzzle_intro:
    $ node1 = False
    $ node2 = False
    $ node3 = False
    $ node4 = True
    $ node5 = True
    $ node6 = True
    $ puzzle_turn = 0
    
label puzzle:
    #Solution: D,F,C,F,B,A,F
    scene mansion
    call screen puzzle_lights
    play sound "sfx/button.ogg"
    $ puzzle_turn += 1
    $ picked = _return
    if picked == "A":
        $ node1 = not node1
        $ node4 = not node4
    elif picked == "B":
        $ node2 = not node2
        $ node3 = not node3
    elif picked == "C":
        $ node3 = not node3
        $ node6 = not node6
        $ node5 = not node5
    elif picked == "D":
        $ node4 = not node4
        $ node5 = not node5
        $ node6 = not node6
    elif picked == "E":
        $ node5 = not node5
    elif picked == "F":
        $ node3 = not node3
    elif picked == "restart":
        jump puzzle_intro
    if node1 and node2 and node3 and node4 and node5 and node6:
        play sound "sfx/beep_good.ogg"
        "The panel beeps. Success."
        jump puzzle_complete
    if puzzle_turn > 30:
        $ wpn.use_sfx()
        "You attack the console out of frustration."
        "Surprisingly, this gets a response out of it."
        jump puzzle_complete
    jump puzzle
    
screen puzzle_lights:
    add "half_black"
    text "Turn all the nodes green to open the gate." xalign 0.5 yalign 0.8 size 20
    textbutton "Restart" xalign 0.5 yalign 0.86 action Return("restart")
    vbox:
        xalign 0.5 yalign 0.5
        hbox:
            xalign 0.5 spacing 60
            imagebutton idle "gui/knob2.png" hover "gui/knob.png" action Return("A")
            imagebutton idle "gui/knob2.png" hover "gui/knob.png" action Return("B")
            imagebutton idle "gui/knob2.png" hover "gui/knob.png" action Return("C")
        null height 5
        frame:
            has vbox
            hbox:
                xalign 0.5 yalign 0.5
                if node1:
                    add "gui/puzzle_on.png"
                else:
                    add "gui/puzzle_off.png"
                if node2:
                    add "gui/puzzle_on.png"
                else:
                    add "gui/puzzle_off.png"
                if node3:
                    add "gui/puzzle_on.png"
                else:
                    add "gui/puzzle_off.png"
            hbox:
                xalign 0.5 yalign 0.5
                if node4:
                    add "gui/puzzle_on.png"
                else:
                    add "gui/puzzle_off.png"
                if node5:
                    add "gui/puzzle_on.png"
                else:
                    add "gui/puzzle_off.png"
                if node6:
                    add "gui/puzzle_on.png"
                else:
                    add "gui/puzzle_off.png"
        null height 5
        hbox:
            xalign 0.5 spacing 60
            imagebutton idle "gui/knob2.png" hover "gui/knob.png" action Return("D")
            imagebutton idle "gui/knob2.png" hover "gui/knob.png" action Return("E")
            imagebutton idle "gui/knob2.png" hover "gui/knob.png" action Return("F")

    


