################
#### Variables ####
################

init:
    #Positions
    $ mid = Position(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5)
    $ right = Position(xcenter=0.7)
    $ left = Position(xcenter=0.3)
    $ farright = Position(xcenter=0.8)
    $ farleft = Position(xcenter=0.2)
    $ mid_right = Position(xcenter=0.6)
    $ mid_left = Position(xcenter=0.4)

    $ center_pos = 0.5
    $ right_pos = 0.7
    $ left_pos =0.3
    $ farright_pos = 0.8
    $ farleft_pos = 0.2
    $ mid_right_pos = 0.6
    $ mid_left_pos = 0.4
    
    #Transitions
    $ quickdissolve = Dissolve(0.1)
    $ meddissolve = Dissolve(1.0)
    $ slowdissolve = Dissolve(3.0)
    $ intro_dissolve = Dissolve(5.0)
    $ sshake = Shake((0, 0, 0, 0), 0.75, dist=15)

################
#### IMAGES ####
################

init:
    #Static BG
    image static = Animation(im.Tile("map/bg1.jpg"),0.2,im.Tile("map/bg2.jpg"),0.2,im.Tile("map/bg3.jpg"),0.2,im.Tile("map/bg4.jpg"),0.2,im.Tile("map/bg5.jpg"),0.2)
    
    image splash_warning = "warning.png"
    image splash_logo = "hpbw.png"
    image splash_hand = "gui/hand.png"
    
    #Text  for credits
    image credit_text = renpy.ParameterizedText(ypos=0.85, xpos=0.05, xanchor=0.0, size=30, font="fonts/Commodore Angled v1.2.ttf")
    
    #Semi-black screen for GUI
    image half_black = "bg/black_screen.png"
    
    image tut_arrow = im.Flip("gui/tut_arrow.png",horizontal=True,vertical=True)
    
    image bg farm = "bg/farm.jpg"
    image bg farm2 = "bg/farm2.jpg"
    image bg canopy = "bg/canopy.jpg"
    image bg city = "bg/city_night002.jpg"
    image bg train = "bg/train.jpg"
    image girl1 = "char/28.png"
    image girl2 = "char/30.png"
    image girl3 = "char/27.png"
    image girl4 = "char/29.png"
    image bg city hall = "bg/old_clock.jpg"
    image bg farm3 = "bg/farm3.jpg"
    image bg train night = "bg/train_night.jpg"
    image smoke  = "bg/smoke.png"
    image cutscene = "bg/cutscene.png"
    
    image cabin = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/cabin_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/cabin_night.jpg",
        "True", "bg/cabin.jpg",)
    image trees = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/trees_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/trees_night.jpg",
        "True", "bg/trees.jpg",)
    image shack = ConditionSwitch(
        "hour < 9 and hour > 5", "bg/shack_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/shack_night.jpg",
        "True", "bg/shack.jpg",)
    image bathhouse = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/bathhouse_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/bathhouse_night.jpg",
        "True", "bg/bathhouse.jpg",)
    image bridge = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/bridge_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/bridge_night.jpg",
        "True", "bg/bridge.jpg",)
    image canopy = "bg/canopy.jpg"
    image cave = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/cave_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/cave_night.jpg",
        "True", "bg/cave.jpg",)
    image cave_int = "bg/cave_int.jpg"
    image cabins = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/cabins_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/cabins_night.jpg",
        "True", "bg/cabins.jpg",)
    image cliff = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/cliff_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/cliff_night.jpg",
        "True", "bg/cliff.jpg",)
    image cliff2 = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/cliff2_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/cliff2_night.jpg",
        "True", "bg/cliff2.jpg",)
    image coastline = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/coastline_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/coastline_night.jpg",
        "True", "bg/coastline.jpg",)
    image farm = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/farm_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/farm_night.jpg",
        "True", "bg/farm.jpg",)
    image farm2 = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/farm2_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/farm2_night.jpg",
        "True", "bg/farm2.jpg",)
    image farm3 = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/farm3_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/farm3_night.jpg",
        "True", "bg/farm3.jpg",)
    image forest = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/forest_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/forest_night.jpg",
        "True", "bg/forest.jpg",)
    image forest3 = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/forest3_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/forest3_night.jpg",
        "True", "bg/forest3.jpg",)
    image open_sea = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/open_sea_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/open_sea_night.jpg",
        "True", "bg/open_sea.jpg",)
    image gate = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/gate_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/gate_night.jpg",
        "True", "bg/gate.jpg",)
    image grass_path = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/grass_path_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/grass_path_night.jpg",
        "True", "bg/grass_path.jpg",)
    image grassland = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/grassland_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/grassland_night.jpg",
        "True", "bg/grassland.jpg",)
    image graveyard = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/graveyard_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/graveyard_night.jpg",
        "True", "bg/graveyard.jpg",)
    image graveyard2 = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/graveyard2_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/graveyard2_night.jpg",
        "True", "bg/graveyard2.jpg",)
    image ruins = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/ruins_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/ruins_night.jpg",
        "True", "bg/ruins.jpg",)
    image hospital = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/hospital_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/hospital_night.jpg",
        "True", "bg/hospital.jpg",)
    image lighthouse = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/lighthouse_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/lighthouse_night.jpg",
        "True", "bg/lighthouse.jpg",)
    image mansion = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/mansion_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/mansion_night.jpg",
        "True", "bg/mansion.jpg",)
    image old_clock = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/old_clock_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/old_clock_night.jpg",
        "True", "bg/old_clock.jpg",)
    image pier = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/pier_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/pier_night.jpg",
        "True", "bg/pier.jpg",)
    image sakura = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/sakura_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/sakura_night.jpg",
        "True", "bg/sakura.jpg",)
    image shrine = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/shrine_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/shrine_night.jpg",
        "True", "bg/shrine.jpg",)
    image shrine_little = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/shrine_little_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/shrine_little_night.jpg",
        "True", "bg/shrine_little.jpg",)
    image station = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/station_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/station_night.jpg",
        "True", "bg/station.jpg",)
    image teahouse = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/teahouse_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/teahouse_night.jpg",
        "True", "bg/teahouse.jpg",)
    image waterfall = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/waterfall_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/waterfall_night.jpg",
        "True", "bg/waterfall.jpg",)
    image waterfall_cave = "bg/waterfall_int.jpg"
    image ponds = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/ponds_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/ponds_night.jpg",
        "True", "bg/ponds.jpg",)
    image school = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/school_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/school_night.jpg",
        "True", "bg/school.jpg",)
    image corridor = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/corridor_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/corridor_night.jpg",
        "True", "bg/corridor.jpg",)
    image classroom = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/classroom_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/classroom_night.jpg",
        "True", "bg/classroom.jpg",)
    image teachers_room = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/teachers_room_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/teachers_room_night.jpg",
        "True", "bg/teachers_room.jpg",)
    image train_station = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/train_station_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/train_station_night.jpg",
        "True", "bg/train_station.jpg",)
    image old_kitchen = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/old_kitchen_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/old_kitchen_night.jpg",
        "True", "bg/old_kitchen.jpg",)
    image tea_house = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/tea_house_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/tea_house_night.jpg",
        "True", "bg/tea_house.jpg",)
    image old_room = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/old_room_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/old_room_night.jpg",
        "True", "bg/old_room.jpg",)
    image city_hall = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/city_hall_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/city_hall_night.jpg",
        "True", "bg/city_hall.jpg",)
    image lockers_ladies = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/lockers_ladies.jpg",
        "hour < 5 or hour >= 21", "bg/lockers_ladies_night.jpg",
        "True", "bg/lockers_ladies.jpg",)
    image lockers_men = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/lockers_men.jpg",
        "hour < 5 or hour >= 21", "bg/lockers_men_night.jpg",
        "True", "bg/lockers_men.jpg",)
    image showers = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/showers_night_on.jpg",
        "hour < 5 or hour >= 21", "bg/showers_night.jpg",
        "True", "bg/showers.jpg",)
    image lab = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/lab_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/lab_night.jpg",
        "True", "bg/lab.jpg",)
    image fireplace = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/fireplace_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/fireplace_night.jpg",
        "True", "bg/fireplace.jpg",)
    image bath = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/bath_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/bath_night.jpg",
        "True", "bg/bath.jpg",)
    image onsen = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/onsen_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/onsen_night.jpg",
        "True", "bg/onsen.jpg",)
    image foyer = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/foyer_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/foyer_night.jpg",
        "True", "bg/foyer.jpg",)
    image toilets = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/toilets_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/toilets_night.jpg",
        "True", "bg/toilets.jpg",)
    image shed = ConditionSwitch(
        "hour >= 5 and hour < 8", "bg/storage_dawn.jpg",
        "hour < 5 or hour >= 21", "bg/storage_night.jpg",
        "True", "bg/storage.jpg",)
    # image classroom = ConditionSwitch(
        # "hour >= 5 and hour < 8", "bg/classroom_dawn.jpg",
        # "hour < 5 or hour >= 21", "bg/classroom_night.jpg",
        # "True", "bg/classroom.jpg",)
    image locker = "bg/locker.png"
    image locker open = "bg/locker2.png"

    image bg helicopter sky = "bg/helicopter.jpg"
    image bg helicopter = "bg/helicopter2.jpg"

    image fancy room = "bg/fancy_room.jpg"
    image bg bar = "bg/bar.jpg"
    image bg restroom = "bg/bathroom.jpg"
    
    image blood0 = "bg/blood0.png"
    image blood1 = "bg/blood1.png"
    image blood2 = "bg/blood2.png"
    image blood3 = "bg/blood3.png"
    image blood4 = "bg/blood4.png"
    image blood5 = "bg/blood5.png"
    image blood6 = "bg/blood6.png"
    image blood7 = "bg/blood7.png"
    
    image glass_crack = "bg/crack.png"

    image Shinobu = "char/Shinobu.png"
    image Shinobu happy = "char/Shinobu_happy.png"
    image Shinobu angry = "char/Shinobu_angry.png"
    image Shinobu evil = "char/Shinobu_evil.png"
    image Shinobu sad = "char/Shinobu_sad.png"
    image Shinobu scared = "char/Shinobu_scared.png"
    image Jun = "char/Jun.png"
    image Jun scared = "char/Jun_scared.png"
    image Jun mad = "char/Jun_mad.png"
    image Jun surprised = "char/Jun_surprised.png"
    image Jun skeptical = "char/Jun_skeptical.png"
    image Jun sad = "char/Jun_sad.png"
    image Jun lookaway = "char/Jun_lookaway.png"
    image Jun angry = "char/Jun_angry.png"
    image Jun happy = "char/Jun_happy.png"
    image Tetsuo = "char/Tetsuo.png"
    image Tetsuo happy = "char/Tetsuo_happy.png"
    image Tetsuo scared = "char/Tetsuo_scared.png"
    image Tetsuo angry = "char/Tetsuo_angry.png"
    image Keitaro = "char/Keitaro.png"
    image Keitaro scared = "char/Keitaro_scared.png"
    image Keitaro angry = "char/Keitaro_angry.png"
    image Goro = "char/Goro.png"
    image Goro scared = "char/Goro.png"
    image Goro happy = "char/Goro.png"
    image Takeshi = "char/Takeshi.png"
    image Takeshi sad = "char/Takeshi_sad.png"
    image Takeshi angry = "char/Takeshi_angry.png"
    image Ikoma clean = "char/Ikoma.png"
    image Ikoma = "char/Ikoma_blood.png"
    image Ikoma coy = "char/Ikoma_coy.png"
    image Ikoma angry = "char/Ikoma_angry.png"
    image Yuki = "char/Yuki.png"
    image Yuki scared = "char/Yuki_scared.png"
    image Yuki sad = "char/Yuki_sad.png"
    image Yuki happy = "char/Yuki_happy.png"
    image Asai = "char/Asai.png"
    image Asai scared = "char/Asai_scared.png"
    image Asai angry = "char/Asai_angry.png"
    image Kenji = "char/Kenji.png"
    image Kenji scared = "char/Kenji_scared.png"
    image Kenji happy = "char/Kenji_happy.png"
    
    image Mari = "char/Mari.png"
    image Mari content = "char/Mari_content.png"
    image Mari happy = "char/Mari_happy.png"
    image Mari angry = "char/Mari_angry.png"
    image Mari scared = "char/Mari_scared.png"
    image Mari sad = "char/Mari_sad.png"
    image Mari yell = "char/Mari_yell.png"
    image Emi = "char/Emi.png"
    image Emi happy = "char/Emi_happy.png"
    image Emi scared = "char/Emi_scared.png"
    image Emi angry = "char/Emi_angry.png"
    image Yoriko = "char/Yoriko.png"
    image Yoriko scared = "char/Yoriko_scared.png"
    image Yoriko tired = "char/Yoriko_tired.png"
    image Yoriko angry = "char/Yoriko_angry.png"
    image Fumie = "char/Fumie.png"
    image Fumie happy = "char/Fumie_happy.png"
    image Fumie sad = "char/Fumie_sad.png"
    image Fumie angry = "char/Fumie_angry.png"
    image Fumie scared = "char/Fumie_scared.png"
    image Lucy = "char/Lucy.png"
    image Lucy scared = "char/Lucy_scared.png"
    image Lucy sad = "char/Lucy_sad.png"
    image Ai = "char/Ai.png"
    image Ai scared = "char/Ai_scared.png"
    image Ai sad = "char/Ai_sad.png"
    image Ai angry = "char/Ai_angry.png"
    image Ai yell = "char/Ai_yell.png"
    image Ai smile = "char/Ai_smile.png"
    image Ai evil = "char/Ai_evil.png"
    image Hitomo = "char/Hitomo.png"
    image Hitomo scared = "char/Hitomo_scared.png"
    image Hitomo happy = "char/Hitomo_happy.png"
    image Nanako = "char/Nanako.png"
    image Nanako smile = "char/Nanako_smile.png"
    image Nanako scared = "char/Nanako_scared.png"
    image Nanako angry = "char/Nanako_angry.png"
    image Nanako happy= "char/Nanako_happy.png"
    image Nanako sad= "char/Nanako_sad.png"
    
    image wife = "char/wife.png"
### HEALTH/SANITY BARS ###

image green_bar:
    "gui/sanity0.png"
    
image empty_bar:
    "gui/stat_bar_empty.png"

image green_bar_flash1:
    contains:
        "gui/sanity0.png"
    contains:
        "gui/sanity1.png"
        alpha 0 
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.0
        repeat
        
image green_bar_flash2:
    contains:
        "gui/sanity0.png"
    contains:
        "gui/sanity1.png"
        alpha 0 
        linear 0.75 alpha 1.0
        linear 0.75 alpha 0.0
        repeat
        
image green_bar_flash3:
    contains:
        "gui/sanity0.png"
    contains:
        "gui/sanity1.png"
        alpha 0 
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0.0
        repeat
        
image green_bar_flash4:
    contains:
        "gui/sanity0.png"
    contains:
        "gui/sanity1.png"
        alpha 0 
        linear 0.25 alpha 1.0
        linear 0.25 alpha 0.0
        repeat
        
image red_bar:
    "gui/health0.png"

image red_bar_flash1:
    contains:
        "gui/health0.png"
    contains:
        "gui/health1.png"
        alpha 0 
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.0
        repeat
        
image red_bar_flash2:
    contains:
        "gui/health0.png"
    contains:
        "gui/health1.png"
        alpha 0 
        linear 0.75 alpha 1.0
        linear 0.75 alpha 0.0
        repeat
        
image red_bar_flash3:
    contains:
        "gui/health0.png"
    contains:
        "gui/health1.png"
        alpha 0 
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0.0
        repeat
        
image red_bar_flash4:
    contains:
        "gui/health0.png"
    contains:
        "gui/health1.png"
        alpha 0 
        linear 0.25 alpha 1.0
        linear 0.25 alpha 0.0
        repeat
        
### BLOOD ###
init python:
    def show_blood():
        global rand_blood
        renpy.sound.play("sfx/blood1.ogg",channel="system2")
        num = renpy.random.randint(0,7)
        rand_blood = "bg/blood%d.png"%num
        renpy.show_screen("blood")

screen blood:
    add rand_blood at _splatter_transform
    timer 2.25 action Hide('blood')
    
screen blood1:
    add "blood1" at _splatter_transform
    timer 3.0 action Hide('blood1')
    
screen blood2:
    add "blood2" at _splatter_transform
    timer 3.0 action Hide('blood2')
    
screen blood3:
    add "blood3" at _splatter_transform
    timer 3.0 action Hide('blood3')
    
screen blood4:
    add "blood4" at _splatter_transform
    timer 3.0 action Hide('blood4')
    
screen blood5:
    add "blood5" at _splatter_transform
    timer 3.0 action Hide('blood5')
    
screen blood6:
    add "blood6" at _splatter_transform
    timer 3.0 action Hide('blood6')
    
screen blood7:
    add "blood7" at _splatter_transform
    timer 3.0 action Hide('blood7')
    
screen blood0:
    add "blood0" at _splatter_transform
    timer 3.0 action Hide('blood0')
        
transform _splatter_transform:
    xpos 0 ypos 0
    on show:
        alpha 0
        0.25
        linear .25 alpha 1.0
    on hide:
        linear 2.0 alpha 0.0
        
screen blood_splatter:
    add "bg/blood0.png"
        
##################################
######### TYPE EFFECTS ###########
##################################
# could be an easier way of doing this, but oh well

screen title_card:
    window:
        background Animation(im.Tile("map/bg1.jpg"),0.2,im.Tile("map/bg2.jpg"),0.2,im.Tile("map/bg3.jpg"),0.2,)
    add "winthegame_title" xpos 68 ypos 330
    timer 0.001 action Play("system","sfx/main_menu_type.ogg")
    timer 3.0 action Play("system","sfx/blood3.ogg")
    timer 3.0 action Show("blood_splatter")

image winthegame_title:
    contains:
        "gui/letters/blank.png"
        0.5
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/w.png"
    contains:
        xpos 43
        "gui/letters/blank.png"
        0.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/i.png"
    contains:
        xpos 86
        "gui/letters/blank.png"
        0.7
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/n.png"
    contains:
        ypos 44
        "gui/letters/blank.png"
        0.9
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/t.png"
    contains:
        xpos 43 ypos 44
        "gui/letters/blank.png"
        1.0
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/h.png"
    contains:
        xpos 86 ypos 44
        "gui/letters/blank.png"
        1.1
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos 135 ypos 10
        "gui/letters/blank.png"
        1.3
        "gui/letters/big_caret.png"
        0.1
        "gui/letters/g_big.png"
    contains:   
        xpos (135+82) ypos 10
        "gui/letters/blank.png"
        1.4
        "gui/letters/big_caret.png"
        0.1
        "gui/letters/a_big.png"
    contains:
        xpos ((135+82)+82) ypos 10
        "gui/letters/blank.png"
        1.5
        "gui/letters/big_caret.png"
        0.1
        "gui/letters/m_big.png"
    contains:
        xpos (((135+82)+82)+82) ypos 10
        "gui/letters/blank.png"
        1.7
        "gui/letters/big_caret.png"
        0.1
        "gui/letters/e_big.png"
    contains:
        xpos ((((135+82)+82)+82)+70) ypos 10
        "gui/letters/blank.png"
        1.7
        block:
            "gui/letters/big_caret.png"
            1.0
            "gui/letters/blank.png"
            0.5
            repeat

image winthegame:
    contains:
        "gui/letters/blank.png"
        0.5
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/w.png"
    contains:
        xpos 43
        "gui/letters/blank.png"
        0.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/i.png"
    contains:
        xpos 86
        "gui/letters/blank.png"
        0.7
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/n.png"
    contains:
        xpos 129
        "gui/letters/blank.png"
        0.8
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/space.png"
    contains:
        xpos 156
        "gui/letters/blank.png"
        0.9
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/t.png"
    contains:
        xpos 199
        "gui/letters/blank.png"
        1.0
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/h.png"
    contains:
        xpos 242
        "gui/letters/blank.png"
        1.1
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos 285
        "gui/letters/blank.png"
        1.2
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/space.png"
    contains:
        xpos 312
        "gui/letters/blank.png"
        1.3
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/g.png"
    contains:
        xpos 355
        "gui/letters/blank.png"
        1.4
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/a.png"
    contains:
        xpos 398
        "gui/letters/blank.png"
        1.5
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/m.png"
    contains:
        xpos 441
        "gui/letters/blank.png"
        1.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos 484
        "gui/letters/blank.png"
        1.7
        block:
            "gui/letters/caret_green.png"
            1.0
            "gui/letters/blank.png"
            0.5
            repeat
            
screen aleema_title:
    add "hb_presents" xpos 10 ypos 0.825
        
image aleema_presents:
    contains:
        "gui/letters/blank.png"
        0.5
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/a.png"
    contains:
        xpos 43
        "gui/letters/blank.png"
        0.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/l.png"
    contains:
        xpos 86
        "gui/letters/blank.png"
        0.7
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos 129
        "gui/letters/blank.png"
        0.8
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos 172
        "gui/letters/blank.png"
        0.9
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/m.png"
    contains:
        xpos 215
        "gui/letters/blank.png"
        1.0
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/a.png"
    contains:
        xpos 258
        "gui/letters/blank.png"
        1.1
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/space.png"
    contains:
        xpos 285
        "gui/letters/blank.png"
        1.2
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/p.png"
    contains:
        xpos 328
        "gui/letters/blank.png"
        1.3
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/r.png"
    contains:
        xpos 371
        "gui/letters/blank.png"
        1.4
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos 414
        "gui/letters/blank.png"
        1.5
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/s.png"
    contains:
        xpos 457
        "gui/letters/blank.png"
        1.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos (457+43)
        "gui/letters/blank.png"
        1.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/n.png"
    contains:
        xpos ((457+43)+43)
        "gui/letters/blank.png"
        1.7
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/t.png"
    contains:
        xpos (((457+43)+43)+43)
        "gui/letters/blank.png"
        1.8
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/s.png"
    contains:
        xpos ((((457+43)+43)+43)+43)
        "gui/letters/blank.png"
        1.9
        block:
            "gui/letters/caret_green.png"
            1.0
            "gui/letters/blank.png"
            0.5
            repeat

image hb_presents:
    contains:
        "gui/letters/blank.png"
        0.5
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/h.png"
    contains:
        xpos 43
        "gui/letters/blank.png"
        0.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/a.png"
    contains:
        xpos 86
        "gui/letters/blank.png"
        0.7
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/p.png"
    contains:
        xpos 129
        "gui/letters/blank.png"
        0.8
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/p.png"
    contains:
        xpos 172
        "gui/letters/blank.png"
        0.9
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/y.png"
    contains:
        xpos 215
        "gui/letters/blank.png"
        1.0
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/b.png"
    contains:
        xpos 258
        "gui/letters/blank.png"
        1.1
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/space.png"
    contains:
        xpos 285
        "gui/letters/blank.png"
        1.2
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/p.png"
    contains:
        xpos 328
        "gui/letters/blank.png"
        1.3
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/r.png"
    contains:
        xpos 371
        "gui/letters/blank.png"
        1.4
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos 414
        "gui/letters/blank.png"
        1.5
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/s.png"
    contains:
        xpos 457
        "gui/letters/blank.png"
        1.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos (457+43)
        "gui/letters/blank.png"
        1.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/n.png"
    contains:
        xpos ((457+43)+43)
        "gui/letters/blank.png"
        1.7
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/t.png"
    contains:
        xpos (((457+43)+43)+43)
        "gui/letters/blank.png"
        1.8
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/s.png"
    contains:
        xpos ((((457+43)+43)+43)+43)
        "gui/letters/blank.png"
        1.9
        block:
            "gui/letters/caret_green.png"
            1.0
            "gui/letters/blank.png"
            0.5
            repeat
            
            
image target_locked:
    contains:
        "gui/letters/blank.png"
        0.5
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/t.png"
    contains:
        xpos 43
        "gui/letters/blank.png"
        0.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/a.png"
    contains:
        xpos 86
        "gui/letters/blank.png"
        0.7
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/r.png"
    contains:
        xpos 129
        "gui/letters/blank.png"
        0.8
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/g.png"
    contains:
        xpos 172
        "gui/letters/blank.png"
        0.9
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos 215
        "gui/letters/blank.png"
        1.0
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/t.png"
    contains:
        xpos 258
        "gui/letters/blank.png"
        1.1
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/space.png"
    contains:
        xpos 285
        "gui/letters/blank.png"
        1.2
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/l.png"
    contains:
        xpos 328
        "gui/letters/blank.png"
        1.3
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/o.png"
    contains:
        xpos 371
        "gui/letters/blank.png"
        1.4
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/c.png"
    contains:
        xpos 414
        "gui/letters/blank.png"
        1.5
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/k.png"
    contains:
        xpos 457
        "gui/letters/blank.png"
        1.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos (457+43)
        "gui/letters/blank.png"
        1.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/d.png"
    contains:
        xpos ((457+43)+43)
        "gui/letters/blank.png"
        1.7
        block:
            "gui/letters/caret_green.png"
            1.0
            "gui/letters/blank.png"
            0.5
            repeat
            
image game_over:
    contains:
        "gui/letters/blank.png"
        0.5
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/g.png"
    contains:
        xpos 43
        "gui/letters/blank.png"
        0.6
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/a.png"
    contains:
        xpos 86
        "gui/letters/blank.png"
        0.7
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/m.png"
    contains:
        xpos 129
        "gui/letters/blank.png"
        0.8
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos 172
        "gui/letters/blank.png"
        0.9
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/space.png"
    contains:
        xpos (172+27)
        "gui/letters/blank.png"
        1.0
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/o.png"
    contains:
        xpos ((172+27)+43)
        "gui/letters/blank.png"
        1.1
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/v.png"
    contains:
        xpos (((172+27)+43)+43)
        "gui/letters/blank.png"
        1.2
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/e.png"
    contains:
        xpos ((((172+27)+43)+43)+43)
        "gui/letters/blank.png"
        1.3
        "gui/letters/caret_green.png"
        0.1
        "gui/letters/r.png"
    contains:
        xpos (((((172+27)+43)+43)+43)+43)
        "gui/letters/blank.png"
        1.4
        block:
            "gui/letters/caret_green.png"
            1.0
            "gui/letters/blank.png"
            0.5
            repeat
            
image credits_montage:
    alpha 0 xanchor 0.0 yanchor 0.0
    xpos 0.7 ypos 0.0
    "gui/credits/mari.png"
    linear 4.0 xpos 0.5 alpha 1.0
    linear 3.0 xpos 0.3 alpha 0.0
    xpos 0.7 ypos 0.0
    "gui/credits/jun.png"
    linear 4.0 xpos 0.5 alpha 1.0
    linear 3.0 xpos 0.3 alpha 0.0
    xpos 0.6 ypos 0.0
    "gui/credits/hitomo_lucy.png"
    linear 4.0 xpos 0.4 alpha 1.0
    linear 3.0 xpos 0.2 alpha 0.0
    xpos 0.7 ypos 0.0
    "gui/credits/yoriko.png"
    linear 4.0 xpos 0.5 alpha 1.0
    linear 3.0 xpos 0.3 alpha 0.0
    xpos 0.7 ypos 0.0
    "gui/credits/fumie_kei.png"
    linear 4.0 xpos 0.5 alpha 1.0
    linear 3.0 xpos 0.3 alpha 0.0
    xpos 0.7 ypos 0.0
    "gui/credits/kenji.png"
    linear 4.0 xpos 0.5 alpha 1.0
    linear 3.0 xpos 0.3 alpha 0.0
    xpos 0.7 ypos 0.0
    
    
    "gui/credits/takeshi.png"
    linear 4.0 xpos 0.5 alpha 1.0
    linear 3.0 xpos 0.3 alpha 0.0
    xpos 0.7 ypos 0.0
    "gui/credits/ikoma.png"
    linear 4.0 xpos 0.5 alpha 1.0
    linear 3.0 xpos 0.3 alpha 0.0
    xpos 0.7 ypos 0.0
    "gui/credits/yuki_nanako.png"
    linear 4.0 xpos 0.5 alpha 1.0
    linear 3.0 xpos 0.3 alpha 0.0
    xpos 0.7 ypos 0.0
    "gui/credits/ai.png"
    linear 4.0 xpos 0.5 alpha 1.0
    linear 3.0 xpos 0.3 alpha 0.0
    xpos 0.6 ypos 0.0
    "gui/credits/asai_tetsuo.png"
    linear 3.0 xpos 0.4 alpha 1.0
    linear 2.0 xpos 0.2 alpha 0.0
    xpos 0.7 ypos 0.0
    "gui/credits/emi.png"
    linear 4.0 xpos 0.5 alpha 1.0
    linear 3.0 xpos 0.3 alpha 0.0
    xpos 0.7 ypos 0.0
