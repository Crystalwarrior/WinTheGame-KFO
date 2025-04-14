######################################
###################################### ITEMS #
######################################
label game_init_items:
    python:
        ##################
        ## INSTRUCTIONS ##
        ##################
        ###Values you can define: 
        #Name - call name for its portrait ("icons/*.jpg") "REQUIRED)
        #Fancy Name - formal name that's displayed to the player (REQUIRED)
        #Get SFX - sound effect played when you pick up the item (REQUIRED) - must be in the "sfx/" folder and .ogg
        #Use SFX - sound effect player when you use (consume or attack with) the item (REQUIRED) - must be in the "sfx/" folder and .ogg
        #Drop SFX - sound when you discard the item (REQUIRED) - must be in the "sfx/" folder and .ogg
        #Description - info displayed on item screen (REQUIRED)
        #Type - your custom item tag for grouping general types of item for reference later (if you need to check if the player specifically has a "gun" and not just a ranged weapon)
        #Wpn Rating - # from 0-9  (9 meaning 'extremely deadly')
        #Wpn Range - Can be either "ranged" (can shoot from a distance), "melee" (needs to be close up), or "both". 'None' is default.
        #Defence Rating - # from 0-9 (9 meaning 'extremely protective')
        #Heal Rating - # from 0-9 (9 meaning 'restores all of your health')
        #Sanity Heal Rating - # from 0-9 (9 meaning 'restores all of your sanity')
        #Conspicuous? - Will other players notice that you have a threatening weapon? (Say False if you can conceal your weapon or it is not threatening at all.) 'False' is default.
        # Amount to add - How many of the item should be added when you first find them?
        
        #AID
        food = items(
            "food",  #Name
            "Food", #Fancy Name
            "Bottled water and freeze-dried food in silver packets. Consuming these would restore your health and a little sanity.",  #Description
            "plastic2", #Get SFX
            "bite", #Use SFX
            "drop1", #Drop SFX
            heal_rating=5, #Heal Rating
            sanity_rating=2, #Sanity Rating
            type="food" #Type (optional, just for grouping similar items)
            )
        food.amount_to_add = 2 ## Amount to add
        
        cigarettes = items("cigarettes", "Cigarettes","A pack of cigarettes. The seal is broken, some are missing, and the rest a little bloody, but otherwise intact and usable.","plastic", "smoking", "drop3",sanity_rating=4,type="filled")
        cigarettes.uses = 1
        cigarettes.broken_message = "Cigarette box is now empty."
        lighter = items("lighter", "Lighter","A metal pocket lighter, probably used for lighting cigarettes.","lighter", "lighter", "drop3")
        megaphone = items("megaphone", "Megaphone","A portable bull horn that will amplify and direct the speaker's voice over long distances. It also has a siren and pitch adjuster.", "radio", "walkietalkie", "drop2")
        laptop = items("laptop", "Laptop","A modern laptop computer with top-of-the-line features. No internet access, however.", "beep_on", "beep_computer", "drop1",sanity_rating=9)
        laptop.uses = 1
        laptop.broken_message = "Laptop has run out of battery life."
        key_copper = items("key", "Copper Key","A copper key. No indicator what it is used for.", "keys", "plastic2", "drop_small")
        key_silver = items("key", "Silver Key","A silver key. No indicator what it is used for.", "keys", "plastic2", "drop_small")
        gas = items("gas", "Gasoline","A canister of gasoline. Many things require gasoline to run, but it is also known for being highly flammable.", "metal5", "plastic_crush.ogg", "splash")
        binoculars = items("binoculars", "Binoculars","A pair of telescopes that allow the viewer to see across long distances. These appear to be small duty, as if for a hobbyist on a budget.", "plastic2", "plastic", "drop1", True)
        firstaid = items("firstaid", "First Aid Kit","A case of supplies to help with common injuries, but will not save lives. Inside are band-aids, rubbing alcohol, cotton swabs, guaze, and medical tape.","firstaid_get", "firstaid", "drop1",heal_rating=6,sanity_rating=4)
        medkit = items("medkit", "Medical Kit","Professional grade equipment to mend the wounded, including tourniquets, morphine, antibacterial supplements, and more.", "firstaid_get", "firstaid", "drop1",heal_rating=9,sanity_rating=6)
        gps = items("gps", "GPS Tracker","A global positioning system that was specifically designed for this island and game in mind. With this, the map will show who is in what zone.", "plastic", "beep_many", "drop1")
        meat = items("meat", "Raw Meat","Slab of raw meat. It could be used as food, but must be cooked first.", "blood3", "bite", "blood3", )
        cooked_meat = items("meat_cooked", "Cooked Meat","Burnt meat that you tried to cook with a stove you didn't know how to operate. Eating it will be healthy.", "blood3", "bite", "blood3",heal_rating=6,sanity_rating=5, type="food")
        
        bag = items("bag", "Duffle Bag","Canvas bag that your datapad told you about. You should open it.", "bag_get", "bag", "plastic2", )
        
        #GUNS
        bbgun = items("bbgun", "BB Gun","An air gun that is known for being a child's introduction to rifles. It shoots plastic BBs that can hurt or break the skin, but only lethal in specific situations.", "bbgun_reload", "bbgun_shot", "drop1", weapon_range="ranged", weapon_rating=4, battle_range=6, conspicuous=True, type="gun")
        revolver = items("revolver", "Revolver","A firearm with a rotating cylinder. You must cock the hammer before each shot.", "revolver_reload", "revolver_shot", "drop2", weapon_range="ranged", weapon_rating=6, battle_range=6, conspicuous=True, type="gun")
        pistol = items("pistol", "M9 Pistol","A handgun, where the barrel is integral with the chamber. Its range is approximately 100 feet.", "gun_reload", "pistol_shot", "drop1", weapon_range="ranged", weapon_rating=6, battle_range=6, conspicuous=True, type="gun")
        glock = items("glock", "Glock Pistol","Semi-automatic pistol often referred to as a \"plastic gun\" due to its polymer frame.", "gun_reload", "glock_shot", "drop1", weapon_range="ranged", weapon_rating=7, battle_range=7, conspicuous=True, type="gun")
        bayonet = items("bayonet", "Bayonet Gun","A handgun with a knife-like blade stick out of the front of it, allowing the user a last line of defense in melee situations.", "gun_reload", "gun_shot", "drop1", weapon_range="both", weapon_rating=7, battle_range=7, conspicuous=True, type="gun")
        uzi = items("uzi", "Uzi Pistol","A submachine gun with the magazine located in the hand grip. It can clock 600 rounds per minute.", "gun_reload", "uzi_shoot", "drop2", weapon_range="ranged", weapon_rating=9, battle_range=8, conspicuous=True, type="gun")
        ak47 = items("ak47", "AK-47 Rifle","When you absolutely must kill everything in the room.","rifle_reload", "ak47_shot", "drop2", weapon_range="ranged", weapon_rating=9, conspicuous=True, type="gun")
        rifle = items("sniperrifle", "Sniper Rifle","A firearm to give the shooter the best possible accuracy in long-range shots. It needs some prepartion, however.", "rifle_reload", "sniper_shot", "drop2", weapon_range="ranged", weapon_rating=8, conspicuous=True, type="gun")
        shotgun = items("shotgun", "Shotgun","A firearm meant to be fired from the shoulder. When fired, the ammo scatters in all directions.", "shotgun_pump", "shotgun_shot2", "drop2", weapon_range="ranged", weapon_rating=8, battle_range=8, conspicuous=True, type="gun")
        shotgun_sawed = items("shotgun_sawed", "Sawed-Off Shotgun","Shotgun with a shortened barrel. Range is shorter but wider, and the gun better concealed.", "shotgun_pump", "shotgun_shot1", "drop2", weapon_range="ranged", weapon_rating=9, conspicuous=True, type="gun")
        shotgun_pump = items("shotgun_pump", "Pump-Action Shotgun","Shotgun with a slide feature that quickly expels spent shells and chambers new ones.", "shotgun_pump", "shotgun_shot3", "drop2", weapon_range="ranged", weapon_rating=9, conspicuous=True, type="gun")
        derringer = items("derringer", "Derringer","Pocket pistol that is notorious easy to hide but usually only contains a single shot.", "revolver_reload", "revolver_shot", "drop2", weapon_range="ranged", weapon_rating=5, battle_range=6, conspicuous=True, type="gun")
        tommy = items("tommy", "Tommy Gun","A submachine gun popularized by American gangsters. Its magazine is notably large.", "gun_reload", "uzi_shoot", "drop2", weapon_range="ranged", weapon_rating=9, conspicuous=True, type="gun")
        machinegun = items("machinegun", "Machine Gun","Light, fully automatic weapon that only needs to be told where to shoot, and it shoots.", "rifle_reload", "uzi_shoot", "drop2", weapon_range="ranged", weapon_rating=9, conspicuous=True, type="gun")
        
        
        
        #MELEE
        
        shoe = items("shoe", "Shoe","The right shoe of a pair of leather footwear.", "plastic2", "plastic", "drop3", weapon_range="melee", weapon_rating=1)
        ladle = items("ladle", "Soup Ladle","A large curved spoon designed to scoop liquids out of a deep pot, normally only found in professional kitchens.", "metal_pull", "metal2", "bat_drop", weapon_range="melee", weapon_rating=1)
        stick = items("stick", "Stick","A sharp and pointy stick.", "bat", "plastic", "drop1", weapon_range="melee", weapon_rating=2)
        screwdriver = items("screwdriver", "Screwdriver","A simple Phillips-head screwdriver that you could find in any toolbox.", "metal_pull", "plastic", "bat_drop", weapon_range="melee", weapon_rating=2)
        taser = items("taser", "Stun Gun","A self-defense item intentionally designed to stun, not kill. Expect electric bolts of up to 900,000 volts to surge through your victims.", "taser", "taser", "drop1", weapon_range="melee", weapon_rating=3)
        drill = items("drill", "Power Drill","A power tool meant to screw in bolts, but the tip spins dangerously fast. If contact is made with it, serious wounds could occur.", "drill", "drill_use", "drop2", weapon_range="melee", weapon_rating=4)
        drill.uses = 5
        bat = items("bat", "Baseball Bat","This is a standard issue aluminum baseball bat. Bats are known for reaching speeds of 110mph, making them deadly if swung at the right place.", "bat", "bat_hit", "bat_drop", weapon_range="melee", weapon_rating=5, battle_range=2, conspicuous=True)
        knife = items("knife", "Knife","A 10\" long kitchen knife usually for cooking preparation. The paper-thin blade will shear anything it touches and it can even puncture cans.", "knife_pull", "slice_blood", "drop1", weapon_range="melee", weapon_rating=5, conspicuous=True)
        axe = items("axe", "Axe","A firefighter's axe meant for breaking down doors. The metal head allows the user to have a very heavy, thus very deadly, swing.", "metal_drag", "slice", "bat_drop", weapon_range="melee", weapon_rating=6, battle_range=2, conspicuous=True)
        sickle = items("sickle", "Sickle","A sharp farming tool meant to help harvest crops. Surprisingly light-weight, this tool has a long, curved blade that will be difficult to avoid.", "metal_drag", "slice", "drop1", weapon_range="melee", weapon_rating=7, battle_range=2, conspicuous=True)
        sword = items("sword", "Sword","Ancient sword as used by the samurai. Swift, precise strokes will bring your enemy down, but don't forget to take it out of the sheath.", "sword_pull", "sword", "sword_drop", weapon_range="melee", weapon_rating=8, battle_range=2, conspicuous=True)
        hook = items("hook", "Hook","A grappling hook typically used for vertical climbs, attached to a good length of rope. The hooks are very sharp.", "metal1", "hook_attack", "drop1", weapon_range="both", weapon_rating=3, battle_range=3, conspicuous=True)
        chainsaw = items("chainsaw", "Chainsaw","A gasoline-powered gardening tool that instills fear at the very sound of it. No limb will survive it if contact is made.", "metal_drag", "chainsaw_short", "drop2", weapon_range="melee", battle_range=2, weapon_rating=9, conspicuous=True,type="fuel")
        chainsaw.uses = 5
        chainsaw.broken_message = "Chainsaw has run out of gas."
        
        #RANGED
        slingshot = items("slingshot", "Slingshot","Wishbone-shaped plastic with an elastic band stretch between the sprongs. No ammo was found.", "slingshot", "slingshot_hit", "drop1",weapon_range="ranged", weapon_rating=2, battle_range=4, conspicuous=True)
        bow = items("bow", "Hunting Bow","A long bow and a quiver of high grade arrows. It takes a lot of strength to pull back the bow string.", "plastic2", "bow_shot", "drop2", weapon_range="ranged", weapon_rating=7, battle_range=6, conspicuous=True)
        crossbow = items("crossbow", "Crossbow","A bow and bolt apparatus that you can hold like a gun. It takes less effort to shoot than a normal bow.", "plastic2", "bow_shot", "drop2", weapon_range="ranged", weapon_rating=7, battle_range=6, conspicuous=True)
        flamethrower = items("flamethrower", "Flamethrower","Throws flames. Things die.", "chain_fence", "flamethrower", "drop2", weapon_range="ranged", weapon_rating=9, battle_range=4, conspicuous=True,type="fuel")
        flamethrower.uses = 5
        flamethrower.broken_message = "Flamethrower is out of fuel."
        grenades = items("grenades", "Grenades","Typically used only in the military because of its deadly blast. Pull the pin and throw!", "glass", "grenade", "drop1", weapon_range="ranged", weapon_rating=7, battle_range=8, conspicuous=True, type = "explosive")
        grenades.amount_to_add = 3
        dynamite = items("dynamite", "Dynamite","Light the end of the fuse and run away as fast as you can.", "plastic", "explosion", "drop1", weapon_range="ranged", weapon_rating=9, conspicuous=True, type = "explosive")
        dynamite.amount_to_add = 2
        throwingknives = items("throwingknives", "Throwing Knives","Aerodynamic silver blades that were meant to be thrown, but they can be wielded as regular knives.", "metal_pull", "hook_attack", "sword_drop",weapon_range="both", weapon_rating=3, battle_range=7, conspicuous=True)
        
        #MISC
        #poison = items("poison", "Poison","Bottles of liquid not meant for human consumption. Very large warnings labels about their lethality.", "glass", "plastic", "glass_break", type="food")
        #poison.amount_to_add = 2
        walkietalkie = items("walkietalkie", "Walkie Talkie","A handheld single channel two-way radio. With a pair, you could give one to a teammate to keep in contact while separated.", "radio", "walkietalkie", "drop1",sanity_rating=2)
        walkietalkie.uses = 2
        walkietalkie.broken_message = "Walkie Talkie batteries have died."
        rope = items("rope", "Rope","Farming rope that is frayed from old age, but it still looks strong enough to withstand heavy loads.", "rope", "rope_climb", "drop1")
        radio = items("radio", "Radio","A radio that can be powered by batteries, but the signal does not last long. Only the emergency broadcast station can be heard. But that's better than nothing.", "radio", "radio_tune", "drop1", sanity_rating = 6)
        radio.uses = 1
        radio.broken_message = "Radio batteries have died."
        trap = items("trap", "Bear Trap","A large bear trap. Hide under leaves for best effect. Warning: trap can cause loss of limb and life if used inappropriately.", "metal_jingle", "sword", "drop1")
        fist = items("punch", "Fist Punch","Your fist.", "swoosh", "punch", "drop1", weapon_rating=0,weapon_range="melee")
        wood = items("wood", "Wood","Planks of wood. Can be used to start a fire. They breathe and bend, making them flexible and perfect for carpentry.", "bat", "bat_hit", "bat_drop")
        lantern = items("lantern", "Lantern","A kerosene lamp that still has fuel in it. It was lit when you found it.", "glass", "plastic", "glass_break")
        paper = items("paper", "Paper","A sheet of clean paper and an accompanying pen.", "plastic", "writing", "drop_small")
        matches = items("matches", "Matches","Small boxes of matches, totaling well over 100 in number. They will help you set things on fire.", "plastic", "plastic2", "drop_small")
        boat = items("boat", "Boat","An old boat.", "bat", "bat_hit", "bat_drop")
    
        #CLOTHES
        potlid = items("potlid", "Pot Lid","The top of a stainless steel pot with a wide handle perfect to conform to your hand. You can use it as a shield or as a battering weapon.", "metal1", "metal3", "drop1", weapon_rating=1,defense_rating=2,type="armor")
        helmet = items("helmet", "Sports Helmet","A sports helmet that you typically find in a little league game, not professional grade. It will only protect your head, but that is the most important part of the body.", "plastic2", "plastic", "drop3", defense_rating=3,type="armor")
        camo = items("camouflage","Ghillie Suit","An outfit of camouflage meant to look like bushy vegetation that will help you disappear out in the wilderness if you stay completely still.", "clothes", "clothes", "drop3", defense_rating=1,type="armor")
        bodyarmor = items("bodyarmor", "Body Armor","Military-grade protective gear that relies on heavy fabric to shield the wearer from projectiles.", "clothes", "hit1", "drop3", defense_rating=9,type="armor")
        bulletproof = items("bulletproof", "Bulletproof Vest","A heavy lead kevlar vest meant to keep bullets from piercing your body. It will only cover your torso and will not make you invincible.", "clothes", "hit1", "drop3", defense_rating=6,type="armor")
 
    return
    
init -2 python:
    ## ITEM OBJECT ##
    class items(store.object):
        def __init__(self,n1,n2,info,sfx1,sfx2,sfx3,type = None, weapon_rating=0, weapon_range=None, battle_range=0, defense_rating=0, heal_rating=0, sanity_rating=0, conspicuous=False, can_stack = True):
            global all_items
            self.name = n1
            self.fancy_name = n2
            self.amount =  0
            self.amount_to_add =  1
            self.wpn_rating = weapon_rating #0 for not a weapon
            self.wpn_range = weapon_range #melee, ranged, both, None
            self.defense = defense_rating #0 if no defense
            self.healing = heal_rating #0 if does not heal upon use
            self.sanity = sanity_rating #0 is does nothing for mental health upon use
            if self.healing > 0 or self.sanity > 0:
                self.can_use = True
            else:
                self.can_use = False
            self.sfx1 = sfx1
            self.sfx2 = sfx2
            self.sfx3 = sfx3
            self.seen = conspicuous
            self.desc = info
            self.type = type
            
            self.can_stack = can_stack #Can the item stack in your inventory?
            
            self.uses = 0 # 0= unlimited
            self.use_count = 0
            self.broken = False
            self.broken_message = self.fancy_name+" can no longer be used."
            
            self.battle_range = battle_range
            
            if self not in all_items:
                all_items.append(self)
            
            if self.wpn_range == "melee":
                self.desc += " {color=#FFF}Melee{/color}."
            elif self.wpn_range == "ranged":
                self.desc += " {color=#FFF}Ranged{/color}."
            elif self.wpn_range == "both":
                self.desc += " {color=#FFF}Melee & Ranged{/color}."
            elif self.wpn_range == "explosive":
                self.desc += " {color=#FFF}Explosive{/color}."
            elif self.wpn_range == "armor":
                self.desc += " {color=#FFF}Armor{/color}."

        def get_sfx(self):
            renpy.sound.play("sfx/"+self.sfx1+".ogg", channel=1)
        def use_sfx(self):
            renpy.sound.play("sfx/"+self.sfx2+".ogg", channel=1)
        def drop_sfx(self):
            renpy.sound.play("sfx/"+self.sfx3+".ogg", channel=1)
            
        def use(self, use_sound=True):
            global wpn
            global armor
            global sanity
            if not self.broken and self.uses > 0:
                self.use_count += 1
                if use_sound:
                    self.use_sfx()
                if self.healing > 0:
                    num = renpy.random.randint(0,10)
                    heal_amt = (self.healing * 7) + num
                    #health += heal_amt
                    add_health(heal_amt)
                if self.sanity > 0:
                    num = renpy.random.randint(0,10)
                    sane_amt = (self.sanity * 5) + num
                    sanity += sane_amt
                    add_sanity(sane_amt)
                if self.use_count >= self.uses:
                    self.broken = True
                    if self.type != "gun":
                        renpy.notify(self.broken_message)
                    else:
                        renpy.notify("You're out of ammo!")
                        if self == bayonet: #change to a melee weapon
                            self.broken = False
                            self.uses = 0
                            self.use_count = 0
                            self.sfx2 = "sfx/slice.ogg"
                            self.wpn_rating = 4
                            self.battle_range = 2
                            self.weapon_range="melee"
                            self.type=""
                            self.desc = "An empty handgun with a knife-like blade stick out of the front of it. While it's out of ammo, at least it's still useful in melee situations."
                            self.desc += " {color=#FFF}Melee{/color}."
                    if armor == self:
                        armor = None
                    if wpn == self:
                        wpn = fist
                        
        def is_in_inventory(self):
            global inventory
            for i in inventory:
                if i[0].name == self.name:
                    return True
            return False
        
        def restore_use(self):
            self.broken = False
            self.use_count = 0
            renpy.notify(self.fancy_name+" is fully functional again!")
            self.get_sfx()
            
        def consume(self):
            global health
            global sanity
            self.use_sfx()
            self.destroy(1,True)
            if self.healing > 0 and self.sanity > 0:
                num = renpy.random.randint(0,10)
                heal_amt = (self.healing * 7) + num
                num = renpy.random.randint(0,10)
                sane_amt = (self.sanity * 5) + num
                sanity += sane_amt
                add_health_sanity(heal_amt,sane_amt)
            elif self.healing > 0:
                num = renpy.random.randint(0,10)
                heal_amt = (self.healing * 7) + num
                #health += heal_amt
                add_health(heal_amt)
            elif self.sanity > 0:
                num = renpy.random.randint(0,10)
                sane_amt = (self.sanity * 5) + num
                sanity += sane_amt
                add_sanity(sane_amt)
                
        def equip(self):
            global wpn
            global armor
            self.get_sfx()
            renpy.sound.play("sfx/beep1.ogg",channel="system")
            if notify_y != .095:
                renpy.show_screen("beep_green")
            if self.wpn_rating > 0:
                wpn = self
            if self.defense > 0:
                armor = self
                
        def unequip(self):
            global wpn
            global armor
            self.drop_sfx()
            renpy.sound.play("sfx/beep1.ogg",channel="system")
            if notify_y != .095:
                renpy.show_screen("beep_green")
            if self.wpn_rating > 0:
                wpn = fist
            if self.defense > 0:
                armor = None
            
                
        def add(self,amt=1,silent=False,pickup=False,from_floor=True):
            global item_name
            global item_quantity
            global fancy_item_name
            global item_amt
            global discarded
            item_name = self.name
            fancy_item_name = self.fancy_name
            if amt == 0:
                amt = self.amount_to_add
            renpy.block_rollback()
            if len(inventory) >= inven_max and not self.is_in_inventory() or len(inventory) >= inven_max and not self.can_stack:
                #print "[inventory full]"
                renpy.sound.play("sfx/beep_double.ogg", channel="system")
                renpy.call_screen("item_replace_prompt")
                if swap:
                    renpy.call_screen("item_replace")
                    if discarded == "cancel" and not pickup:
                        discarded = self
                    elif discarded == "cancel":
                        pass
                    else:
                        discarded = discarded[0]
                        self.get_sfx()
                        inventory.append([self,amt])
                        renpy.notify("Adding "+self.fancy_name+" ...")
                        #store_say(None,"{color=#00db00}Adding "+self.fancy_name+" ...{/color}")
                        if not silent:
                            renpy.sound.play("sfx/beep_good.ogg", channel="system")
                            renpy.show_screen("item_new")
                        # Take item out of location inventory
                        if from_floor:
                            for i in loc.items:
                                if i[0] == self:
                                    i[1] -= amt
                                    if i[1] <= 0:
                                        loc.items.remove(i)
                                    break
                    if discarded != "cancel":
                        discarded.drop("all")
                elif not pickup:
                    self.drop(amt)
                        
            else:
                #print "[inventory not full]"
                renpy.notify("Adding "+self.fancy_name+" ...")
                #store_say(None,"{color=#00db00}Adding "+self.fancy_name+" ...{/color}")
                self.get_sfx()
                if not self.is_in_inventory():
                    inventory.append([self,amt])
                else:
                    for i in inventory:
                        if i[0] == self:
                            i[1] += amt
                            break
                            
                if not silent:
                    renpy.sound.play("sfx/beep_good.ogg", channel="system")
                    renpy.show_screen("item_new")
                if from_floor:
                    for i in loc.items:
                        if i[0] == self:
                            i[1] -= amt
                            if i[1] <= 0:
                                loc.items.remove(i)
                            break
                
            
        def drop(self, num=1,char="you"):
            global wpn
            global loc
            global armor
            global inventory
            if num == "all":
                found = False
                for i in inventory:
                    if i[0].name == self.name:
                        num = i[1]
                        found = True
                        break
                if not found:
                    num = 1
            #print "removing!",self.name,num
            if char == "you":
                self.drop_sfx()
                renpy.sound.play("sfx/beep_double.ogg", channel="system")
                renpy.notify("Dropping "+self.fancy_name+" ...")
                #store_say(None,"{color=#FF0000}Removing "+self.fancy_name+" ...{/color}")
                for i in inventory:
                    if i[0] == self:
                        if i[1] - num <= 0:
                            inventory.remove(i)
                        else:
                            i[1] -= num
                        break
                if self == wpn:
                    wpn = fist
                elif self == armor:
                    armor = None
                    
            #Drop items into location inventory
            already_there = False
            if char == "you":
                loc_to_drop = loc
            else:
                loc_to_drop = char.loc
            for i in loc.items:
                if i[0] == self:
                    i[1] += num
                    already_there = True
            if not already_there:
                loc_to_drop.items.append([self,num])
                
        def destroy(self, num, consume=False):
            global wpn
            global armor
            if self == wpn:
                wpn = fist
            elif self == armor:
                armor = None
            renpy.sound.play("sfx/beep_double.ogg", channel="system")
            if not consume:
                self.drop_sfx()
                renpy.notify("Removing "+self.fancy_name+" ...")
                #store_say(None,"{color=#FF0000}Removing "+self.fancy_name+" ...{/color}")
            else:
                renpy.notify("Consuming "+self.fancy_name+" ...")
                #store_say(None,"{color=#00db00}Consuming "+self.fancy_name+" ...{/color}")

            # IF ONLY THE ITEM JUST HAD A LOC ATTRIBUTE
            if num == "all":
                for i in inventory:
                    if i[0] == self:
                        inventory.remove(i)
                        return
                for char in classmates:
                    if char.item != None and char.item[0] == self:
                        char.item = None
                        return
                    if char.wpn != None and char.wpn == self:
                        char.wpn = None
                        return
                for i in loc.items:
                    if i[0] == self:
                        loc.items.remove(i)
                        return
            else:
                for i in inventory:
                    if i[0] == self:
                        i[1] -= num
                        if i[1] <= 0:
                            inventory.remove(i)
                        return
                for char in classmates:
                    if char.item != None and char.item[0] == self:
                        char.item[1] -= num
                        if char.item[1] <= 0:
                            char.item = None
                        return
                    # NPC weapons can't stack
                    if char.wpn != None and char.wpn == self:
                        char.wpn = None
                        return
                for i in loc.items:
                    if i[0] == self:
                        i[1] -= num
                        if i[1] <= 0:
                            loc.items.remove(i)
                        return
                
