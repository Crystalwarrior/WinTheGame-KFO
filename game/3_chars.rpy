######################################
###################################### CHARACTERS #
######################################
label game_init_chars:
    python:
        ##################
        ## INSTRUCTIONS ##
        ##################
        #Values: 
        #name - first name
        #last name - self explanatory
        #gender - "Male" or "Female"
        #Club - fluff text about their favorite after school activity
        #desc - What it says in their profile on Stats screen
        #attitude - options: "normal", "coward" (moves less, sucks in battle), "hostile" (moves more, advantage in battle), "fixed" (never moves)
        #portrait name - name of the portrait image in the "char/" folder, must be .png
        #weapon - Weapon they're holding (say None for nothing)
        #item - Item they're holding (say None for nothing)
        #talking name - the variable for their Character() call name, so we can speak as them. You'll need to define this somewhere else first.
        #death phrase - what they say when they're killed
        #death sound - sound they make when they're killed
        #death sprite - name of the image that shows when they die
        #attacking sprite - name of the image that shows when they're attacking you
        #starting location - Where you want the character to start on the map (grid location or room location variables only)
        
        
        Shinobu = char("Shinobu", "Okita", "Male","Baseball (Manager)","An average student, but very driven.","fixed","boy12", None, None, None, "You've lost the game.", "scream_boy1", "Shinobu", "Shinobu", loc) #Created a character for the player character for technical reasons, but you will never "meet" him
        
        Emi = char(
            "Emi", #Name
            "Fukumitsu", #Last name
            "Female", #Gender
            "Literature", #After school club
            "Shy bookworm, president of chess club.", #Profile tidbit
            "fixed", #Her attitude, she's "fixed" because she's a recluse in the school and will refuse to leave
            "girl2", # portrait "char/girl2.png"
            bayonet, # her weapon
            None, # her item (it's None because she isn't carrying anything)
            emi, #talking name
            "Noooo!", #Death phrase
            "scream_girl3", #Death sound
            "Emi scared", #death sprite
            "Emi angry", #attacking sprite
            rm_classroom #Starting location (Emi's in a room - the classroom)
            )
        Emi.sanity =  50 #Emi starts off with half her sanity, for story purposes
        
        Goro = char("Goro", "Ryusaki", "Male","Anime","Shifty-eyed boy who always sat by himself.","hostile","boy8", None , None, gor, "Foolish mortal!", "scream_boy5", "Goro scared", "Goro scared",g2)
        Mari = char("Mari", "Tsutaya", "Female","Art","Avid painter, quiet, and good student.","fixed","girl1", revolver, walkietalkie, mari, "I ... forgive you ...", "scream_girl1", "Mari scared", "Mari angry",rm_shrine)
        Tetsuo = char("Tetsuo", "Maruyama", "Male","Student Council (Vice President)","Go-getter. Very active in school.","coward","boy11", axe, None, tet, "You ... You really are trying to kill me!", "scream_boy16", "Tetsuo scared", "Tetsuo scared",e2)
        Fumie = char("Fumie", "Sugihara", "Female","Volleyball","Best friends with just about everyone.","coward","girl16", hook, None, fum, "I don't wanna die!! I ... I ...", "scream_girl4", "Fumie scared", "Fumie angry",g3)
        Kei = char("Keitaro", "Tayama", "Male","Baseball","Star player of the school's baseball team.","normal","boy13", pistol, None, kei, "I can't believe this ... You asshole!", "scream_boy7", "Keitaro angry", "Keitaro scared",f4)
        Takeshi = char("Takeshi", "Uehara", "Male","Kendo","Popular boy with a famous family.","normal","boy3", sword, laptop, tak, "Beaten by a pansy ... ugh.", "scream_boy1", "Takeshi sad", "Takeshi angry",d4)
        Nanako = char("Nanako", "Maeda", "Female","Homemaking","Popular girl known for her fashion sense.","fixed","girl18", None, bulletproof, nana, "This isn't how I was supposed to go ...", "scream_girl8", "Nanako scared", "Nanako angry",rm_bathhouse)
        Kenji = char("Kenji", "Sakai", "Male","Drama (President)","Friendly boy with high ambitions.","hostile","boy5", throwingknives, walkietalkie, ken, "N-n-nooo! I thought ... we were friends ..!", "scream_boy17", "Kenji scared", "Kenji happy", b1)
        Lucy = char("Lucy", "Kanagaki", "Female","Homemaking","Mixed girl with an obsession for boy idols.","normal","girl6", bow, None, lucy, "I see a light ... Shall I go ... towards ... it?", "scream_girl1", "Lucy scared", "Lucy sad",rm_bathhouse)
        Ikoma = char("Ikoma", "Kazutoshi", "Male","Chess","Know-it-all that was constantly bullied.","hostile","boy15", ak47, bodyarmor, iko, "You'll all pay! You'll all rot in hell! Hahahaha!", "scream_boy2", "Ikoma angry", "Ikoma angry",a4)
        Ai = char("Ai", "Watabe", "Female","Volleyball","Early bloomer with an attitude.","hostile","girl7", chainsaw, None, ai, "I'll kill you! I'll kill you!! You're dead!! You're - aaaggh!", "scream_girl6", "Ai yell", "Ai evil",b2)
        Yuki = char("Yuki", "Hishida", "Male","n/a","Quiet boy, popular with all the girls.","coward","boy14", derringer, food, yuki, "Glerggh! Okay! I give up ..!", "scream_boy13", "Yuki scared", "Yuki scared",rm_city_hall) #shotgun_pump
        Hitomo = char("Hitomo", "Gakusha", "Female","Band (Trumpet)","Small-voiced but loyal.","fixed","girl4", glock, None, hit, "Aieeeee!", "scream_girl7", "Hitomo scared", "Hitomo scared",a2)
        Asai = char("Asai", "Mokuami", "Male","Kendo","Loud class clown and known moocher.","fixed","boy17", drill, food, asai, "Arrrgggh!", "scream_boy10", "Asai scared", "Asai scared",f2)
        Yoriko = char("Yoriko", "Hida", "Female","Literature","Strict class president with high honors.","hostile","girl5", crossbow, camo,yor, "You ... win.", "scream_girl5", "Yoriko angry", "Yoriko scared",e3)
        Jun = char("Jun", "Nada", "Male","n/a","Delinquent who always skipped school.","fixed","boy9", ladle, None, jun, "Ugggh!", "scream_boy15", "Jun mad", "Jun scared",f2)

        
        you = Shinobu #Your player character, REQUIRED!
        
        
        ###########Friendships (they will not kill their friends while sane or unprovoked, if they're not hostile)
        Jun.friends = [Asai, Kei]
        Tetsuo.friends = classmates #friends with everyone
        Kei.friends = [you, Takeshi, Kenji, Asai, Yuki, Mari, Emi, Yoriko, Fumie, Lucy, Ai, Hitomo, Nanako]
        Takeshi.friends = [you, Kei, Kenji, Asai, Yuki, Mari, Emi, Yoriko, Fumie, Lucy, Ai, Hitomo, Nanako]
        Ikoma.friends = [] #Friends with no one
        Yuki.friends = classmates
        Goro.friends = [Emi, Yoriko, Ai, Nanako, Lucy, Fumie, Mari, Hitomo]
        Asai.friends = [Takeshi,Yuki,Jun,Kenji,Fumie,Nanako,Hitomo]
        Kenji.friends = [Takeshi, Kei, Nanako, Fumie]
        Mari.friends = classmates
        Fumie.friends = classmates
        Emi.friends = [Yoriko, Goro, Ikoma, Yuki]
        Yoriko.friends = [Emi, Goro, Ikoma, Yuki]
        Lucy.friends = [Nanako, Hitomo, Ai, Fumie, Mari]
        Ai.friends = [Fumie, Mari, Lucy, Yoriko, Emi, Kei]
        Hitomo.friends = [Mari, Yoriko,Fumie,Lucy, Nanako]
        Nanako.friends = [Lucy, Hitomo, Ai, Fumie, Mari, Kei, Takeshi, Yuki, Tetsuo]
        
        ###########Enemies (will absolutely attack on sight)
        Ikoma.enemies = classmates #will try to kill everyone
        Emi.enemies = [Nanako,Lucy,Ai,Hitomo]
        Yoriko.enemies = [Ai, Asai,Takeshi]
        Nanako.enemies = [Goro,Jun]
        
        ############################
        ### SPECIAL CHAR STATES ###
        ############################
        # For story purposes, there are 3 special flags a char can have: Hidden, Invisible, and Invincible
        
        #Hidden
        ##You will not see these characters if they're in the same location as you. (But that doesn't necessarily render them passive.)
        Yoriko.hidden = True
        
        #Invisible
        ### Sorry for the confusing name, but this means they're invisible to the AI, not you. Meaning, they won't get tangled up in any off-screen battles. Good idea for chars that are required for cutscenes. They will show up on screen, but hostile AI chars will overlook them.
        for i in classmates:
            i.invisible = True ##This code makes them ALL invisible at start. You can then change their invisible status when their required cutscenes are done. I am doing this becauase I want you to try and meet all the campaign chars before they start randomly killing each other off.
        
        #Invincible
        ## The "god mode" for chars. They will win any AI battle against other players, except for the player character
        Shinobu.invincible = True
        Ikoma.invincible = True

        total_players,players_alive = len(classmates),len(classmates) #Determines player size, REQUIRED!
        
        

        #########################
        ### Character move routes ###
        #########################
        ## Day, Hour, Location (gaps in directions will cause them to immediately jump to a location, no matter where they are, if that's not what you want, define every hour of every day)
        Ai.route = [
        [1,6,b2], #day 1, hour 6, zone B2, etc...
        [1,7,b3],
        [1,8,a3],
        ]
        Kei.route = [
        [2,7,g3], 
        ]
        Fumie.route = [
        [2,7,g3], 
        ]
        
        
    return
        
init:
    #CHARACTER CALLS (All chars inherit from "narrator")
    $ narrator = Character(None, color="#fff", ctc=Animation("gui/caret0.png",0.5,"gui/caret1.png",0.7), ctc_position="nestled", callback=callback, who_prefix="{color=#00CC00}[[{/color}", who_suffix="{color=#00CC00}]{/color}",who_bold=False, kind=adv)
    $ y = Character('Shinobu', kind=narrator, who_prefix="{color=#d3ffd3}[[{/color}", who_suffix="{color=#d3ffd3}]{/color}",image="Shinobu", window_left_padding = 150) #PC, y = you
    $ who = Character('???', kind=narrator, window_left_padding = 150,image="blank_side") # for unknown characters
    $ ken = Character('Kenji', kind=narrator, window_left_padding = 150,image="Kenji")
    $ mari = Character('Mari', kind=narrator, window_left_padding = 150,image="Mari")
    $ jun = Character('Jun', kind=narrator, window_left_padding = 150,image="Jun")
    $ emi = Character('Emi', kind=narrator, window_left_padding = 150,image="Emi")
    $ kei = Character('Kei', kind=narrator, window_left_padding = 150,image="Keitaro")
    $ fum = Character('Fumie', kind=narrator, window_left_padding = 150,image="Fumie")
    $ gor = Character('Goro', kind=narrator, window_left_padding = 150,image="blank_side")
    $ ai = Character('Ai', kind=narrator, window_left_padding = 150,image="Ai")
    $ tak = Character('Takeshi', kind=narrator, window_left_padding = 150,image="Takeshi")
    $ nana = Character('Nanako', kind=narrator, window_left_padding = 150,image="Nanako")
    $ iko = Character('Ikoma', kind=narrator, window_left_padding = 150,image="Ikoma")
    $ hit = Character('Hitomo', kind=narrator, window_left_padding = 150,image="Hitomo")
    $ yuki = Character('Yuki', kind=narrator, window_left_padding = 150,image="Yuki")
    $ asai = Character('Asai', kind=narrator, window_left_padding = 150,image="Asai")
    $ yor = Character('Yoriko', kind=narrator, window_left_padding = 150,image="Yoriko")
    $ tet= Character('Tetsuo', kind=narrator, window_left_padding = 150,image="Tetsuo")
    $ lucy= Character('Lucy', kind=narrator, window_left_padding = 150,image="Lucy")
    $ child= Character('Child', kind=narrator,image="blank_side")
    
    image side Shinobu = im.FactorScale("char/side/side_shin.jpg", .9, .9)
    image side Shinobu none  = im.FactorScale("char/side/side_shin.jpg", .9, .9)   
    image side Shinobu happy = im.FactorScale("char/side/side_shin_happy.jpg", .9, .9)    
    image side Shinobu angry = im.FactorScale("char/side/side_shin_angry.jpg", .9, .9)
    image side Shinobu sad = im.FactorScale("char/side/side_shin_sad.jpg", .9, .9)
    image side Shinobu evil = im.FactorScale("char/side/side_shin_evil.jpg", .9, .9)
    image side Shinobu scared = im.FactorScale("char/side/side_shin_scared.jpg", .9, .9)
    
    image side Kenji = im.FactorScale("char/side/side_kenji.jpg", .9, .9)
    image side Kenji happy = im.FactorScale("char/side/side_kenji_happy.jpg", .9, .9)
    image side Kenji scared = im.FactorScale("char/side/side_kenji_scared.jpg", .9, .9)
    
    image side Mari = im.FactorScale("char/side/side_mari.jpg", .9, .9)
    image side Mari happy = im.FactorScale("char/side/side_mari_happy.jpg", .9, .9)
    image side Mari content = im.FactorScale("char/side/side_mari_content.jpg", .9, .9)
    image side Mari angry = im.FactorScale("char/side/side_mari_angry.jpg", .9, .9)
    image side Mari yell = im.FactorScale("char/side/side_mari_yell.jpg", .9, .9)
    image side Mari sad = im.FactorScale("char/side/side_mari_sad.jpg", .9, .9)
    image side Mari scared = im.FactorScale("char/side/side_mari_scared.jpg", .9, .9)
    image side Mari happy = im.FactorScale("char/side/side_mari_happy.jpg", .9, .9)
    
    image side Jun = im.FactorScale("char/side/side_jun.jpg", .9, .9)
    image side Jun happy = im.FactorScale("char/side/side_jun_happy.jpg", .9, .9)     
    image side Jun sad = im.FactorScale("char/side/side_jun_sad.jpg", .9, .9)
    image side Jun angry = im.FactorScale("char/side/side_jun_angry.jpg", .9, .9)
    image side Jun mad = im.FactorScale("char/side/side_jun_mad.jpg", .9, .9)
    image side Jun surprised = im.FactorScale("char/side/side_jun_surprised.jpg", .9, .9)
    image side Jun lookaway = im.FactorScale("char/side/side_jun_lookaway.jpg", .9, .9)
    image side Jun skeptical = im.FactorScale("char/side/side_jun_skeptical.jpg", .9, .9)
    image side Jun scared = im.FactorScale("char/side/side_jun_scared.jpg", .9, .9)
    
    image side Emi = im.FactorScale("char/side/side_emi.jpg", .9, .9)  
    image side Emi happy = im.FactorScale("char/side/side_emi_happy.jpg", .9, .9)  
    image side Emi scared = im.FactorScale("char/side/side_emi_scared.jpg", .9, .9)  
    image side Emi angry = im.FactorScale("char/side/side_emi_angry.jpg", .9, .9)  
    
    image side Keitaro = im.FactorScale("char/side/side_kei.jpg", .9, .9)   
    image side Keitaro angry = im.FactorScale("char/side/side_kei_angry.jpg", .9, .9)  
    image side Keitaro scared = im.FactorScale("char/side/side_kei_scared.jpg", .9, .9)
    
    image side Fumie = im.FactorScale("char/side/side_fumie.jpg", .9, .9)
    image side Fumie happy = im.FactorScale("char/side/side_fumie_happy.jpg", .9, .9)
    image side Fumie angry = im.FactorScale("char/side/side_fumie_angry.jpg", .9, .9)
    image side Fumie sad = im.FactorScale("char/side/side_fumie_sad.jpg", .9, .9)
    image side Fumie scared = im.FactorScale("char/side/side_fumie_scared.jpg", .9, .9)
    
    image side Ai = im.FactorScale("char/side/side_ai.jpg", .9, .9)
    image side Ai evil = im.FactorScale("char/side/side_ai_evil.jpg", .9, .9)
    image side Ai smile = im.FactorScale("char/side/side_ai_smile.jpg", .9, .9)
    image side Ai angry = im.FactorScale("char/side/side_ai_angry.jpg", .9, .9)
    image side Ai yell = im.FactorScale("char/side/side_ai_yell.jpg", .9, .9)
    image side Ai sad = im.FactorScale("char/side/side_ai_sad.jpg", .9, .9)
    image side Ai scared = im.FactorScale("char/side/side_ai_scared.jpg", .9, .9)
    
    image side Takeshi = im.FactorScale("char/side/side_tak.jpg", .9, .9)
    image side Takeshi angry = im.FactorScale("char/side/side_tak_angry.jpg", .9, .9)
    image side Takeshi sad = im.FactorScale("char/side/side_tak_sad.jpg", .9, .9)
    image side Takeshi tired = im.FactorScale("char/side/side_tak_tired.jpg", .9, .9)
    
    image side Nanako = im.FactorScale("char/side/side_nana.jpg", .9, .9)
    image side Nanako scared = im.FactorScale("char/side/side_nana_scared.jpg", .9, .9)
    image side Nanako angry = im.FactorScale("char/side/side_nana_angry.jpg", .9, .9)
    image side Nanako happy = im.FactorScale("char/side/side_nana_happy.jpg", .9, .9)
    image side Nanako sad = im.FactorScale("char/side/side_nana_sad.jpg", .9, .9)
    image side Nanako smile = im.FactorScale("char/side/side_nana_smile.jpg", .9, .9)
    
    image side Ikoma = im.FactorScale("char/side/side_iko.jpg", .9, .9)
    
    image side Yuki = im.FactorScale("char/side/side_yuki.jpg", .9, .9)
    image side Yuki scared = im.FactorScale("char/side/side_yuki_scared.jpg", .9, .9)
    image side Yuki angry = im.FactorScale("char/side/side_yuki_angry.jpg", .9, .9)
    image side Yuki happy = im.FactorScale("char/side/side_yuki_happy.jpg", .9, .9)
    image side Yuki sad = im.FactorScale("char/side/side_yuki_sad.jpg", .9, .9)
    
    image side Asai = im.FactorScale("char/side/side_asai.jpg", .9, .9)
    image side Asai scared = im.FactorScale("char/side/side_asai_scared.jpg", .9, .9)
    image side Asai angry = im.FactorScale("char/side/side_asai_angry.jpg", .9, .9)
    
    image side Yoriko = im.FactorScale("char/side/side_yor.jpg", .9, .9)
    image side Yoriko scared = im.FactorScale("char/side/side_yor_scared.jpg", .9, .9)
    image side Yoriko angry = im.FactorScale("char/side/side_yor_angry.jpg", .9, .9)
    image side Yoriko tired = im.FactorScale("char/side/side_yor_tired.jpg", .9, .9)
    
    image side Tetsuo = im.FactorScale("char/side/side_tet.jpg", .9, .9)
    image side Tetsuo scared = im.FactorScale("char/side/side_tet_scared.jpg", .9, .9)
    image side Tetsuo angry = im.FactorScale("char/side/side_tet_angry.jpg", .9, .9)
    image side Tetsuo happy = im.FactorScale("char/side/side_tet_happy.jpg", .9, .9)
    
    image side Lucy = im.FactorScale("char/side/side_lucy.jpg", .9, .9)
    image side Lucy scared = im.FactorScale("char/side/side_lucy_scared.jpg", .9, .9)
    image side Lucy sad = im.FactorScale("char/side/side_lucy_sad.jpg", .9, .9)
    
    image side Hitomo = im.FactorScale("char/side/side_hit.jpg", .9, .9)
    image side Hitomo scared = im.FactorScale("char/side/side_hit_scared.jpg", .9, .9)
    image side Hitomo happy = im.FactorScale("char/side/side_hit_happy.jpg", .9, .9)
    
    image side blank_side = im.FactorScale("char/blank.jpg", .9, .9)
    
    #Data pad characters
    $ comp = Character('Computer', kind=narrator)#image="blank_side", window_left_padding = 150)
    $ dp = NVLCharacter(None, kind=nvl, callback=callback_digi, ctc=Animation("gui/caret0.png",0.5,"gui/caret1.png",0.7))
    $ memo = Character(None, kind=narrator, callback=callback_digi, ctc=Animation("gui/caret0.png",0.5,"gui/caret1.png",0.7), window_xpos=0.5, window_ypos=0.5,window_xanchor=0.5,window_yanchor=0.5,window_background=Frame("gui/static.png",15,15), what_xalign=0.5, what_yalign=0.5, window_ymaximum=50,   window_yminimum=35, window_xpadding =15, window_top_padding=10, window_bottom_padding=15, window_xmargin =50,window_ymargin =0,)
    $ memo2 = Character(None, kind=narrator, callback=callback_digi, ctc=Animation("gui/caret0.png",0.5,"gui/caret1.png",0.7), window_xpos=0.5, window_ypos=0.89,window_xanchor=0.5,window_yanchor=0.5,window_background=Frame("gui/static.png",15,15), what_xalign=0.5, what_yalign=0.5, window_ymaximum=50,   window_yminimum=35, window_xpadding =15, window_top_padding=10, window_bottom_padding=15, window_xmargin =50,window_ymargin =0,)
    
init -2 python:
    ## CHARACTER OBJECT ##
    class char(store.object):
        def __init__(self,n1,n2,i1,i2,i3,i4,i5,weapon,item,i6,i7,sfx1,sprite,sprite2,start):
            global classmates
            self.name = n1
            self.last_name = n2
            self.health = 100
            self.sanity = 100
            self.wpn = weapon
            if item != None:
                self.item = [item,item.amount_to_add]
            else:
                self.item = None
            self.alive = True
            self.gender = i1
            self.club = i2
            self.desc = i3
            self.type = i4 #normal (will fight if attacked), coward (will run away), hostile (will always attack), traitor (will attack if given chance)
            self.portrait = i5
            self.call_name = i6
            self.death_phrase = i7
            #self.hit_sound = sfx2
            self.die_sound = sfx1
            self.death_sprite = sprite
            self.atk_sprite = sprite2
            self.loc = start
            if self not in classmates:
                classmates.append(self)
            self.friends = [] #People they will not kill unless attacked first
            self.enemies = [] #People they will try to kill on sight
            self.invincible = False #Wins every bot fight
            self.invisible = False #Cannot be seen by AI (no bot fights)
            self.hidden = False #Cannot be seen by player
            self.death_type = None
            self.murderer = None
            self.kills = 0
            self.met = False
            self.route = []
            self.order = None
            self.murder_wpn = None
            self.seen_corpse = False
            
        def move(self,newloc):
            global escape_plan
            global loc
            if newloc == "rand":
                randexit = runaway()
                self.loc = randexit
                if loc.type == "grid":
                    if loc.exit_north is not None and loc.exit_north.name == randexit.name:
                        escape_plan = "north"
                    if loc.exit_east is not None and loc.exit_east.name == randexit.name:
                        escape_plan = "east"
                    if loc.exit_west is not None and loc.exit_west.name == randexit.name:
                        escape_plan = "west"
                    if loc.exit_south is not None and loc.exit_south.name == randexit.name:
                        escape_plan = "south"
                else:
                    escape_plan = "outside"
            else:
               self.loc = newloc
            find_all_pop()
            
        def make_foe(self,foe):
            for i in self.friends:
                if i == foe:
                    self.friends.remove(foe)
            self.enemies.append(foe)
            self.enemies = list(set(self.enemies))
            
        def make_friend(self,friend):
            for i in self.enemies:
                if i == friend:
                    self.enemies.remove(friend)
            self.friends.append(friend)
            self.friends = list(set(self.friends))

        def kill(self,type,killer=None):
            global players_alive
            global death_list
            self.alive = False
            players_alive -= 1
            loc_to_add = self.loc
            if self not in loc_to_add.bodies:
                loc_to_add.bodies.append(self)
            loc_to_add.bodies = list(set(loc_to_add.bodies)) #remove duplicate bodies
            self.death_type = type #"Murder" (must supply "killer"), Suicide, or else FZ death
            if type == "murder":
                self.murderer = killer
                killer.kills += 1
                self.murder_wpn = killer.wpn
            #self.loc = None
            if self in party:
                party_remove(self)
            death_list.append(self)
            death_list = list(set(death_list))
            find_all_pop()
            
        def unkill(self,type,killer=None):
            global players_alive
            global death_list
            self.alive = True
            players_alive += 1
            loc_to_add = self.loc
            if self in loc_to_add.bodies:
                loc_to_add.bodies.remove(self)
            loc_to_add.bodies = list(set(loc_to_add.bodies)) #remove duplicate bodies
            self.death_type = type
            if type == "murder":
                self.murderer = None
                killer.kills -= 1
                self.murder_wpn = None
            #self.loc = None
            if self in followers:
                party_add(self)
            if self in death_list:
                death_list.remove(self)
            find_all_pop()

        def death_sfx(self):
            renpy.sound.play("sfx/"+self.die_sound+".ogg", channel=1)
        
