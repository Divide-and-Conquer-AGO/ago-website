# 3.2 Changelog

<!-- ### Battle Mechanics
- Fixed pike units instantly drawing their secondary weapons when a single soldier is engaged upon. They now switch to secondaries on a per soldier basis once the balance of threat of enemies to friendlies in their rear gets over 0
- Soldiers at the rear of pike units will now push forward and clump up less when given attack orders
- Fixed units with the 'prec' attribute such as Corsair Raiders from freezing up and behaving strangely whena attacked in certain circumstances -->

### Allegiance of Old
- Added a new alliance support system for Elven factions.
- Elven realms (High Elves, Lórien, Woodland Realm) can now maintain long-term alliances with key Free Peoples factions.
- Allied factions include:
  - **Rangers (Dúnedain)** – Northern allies tied to Imladris, representing the remnants of Arnor.
  - **Khazad-dûm** – Dwarven allies whose strength reflects the restoration of Moria.
  - **Rohan** – Cavalry-focused kingdom aligned with Lórien.
  - **Anduin Vale** – Woodmen and Éothéod factions connected to both Lórien and the Woodland Realm.
  - **Dale** – Northern Men allied closely with the Woodland Realm.

- Each alliance is tied to specific Elven capitals:
  - **Imladris (Rivendell)** supports Rangers and Khazad-dûm.
  - **Caras Galadhon (Lórien)** supports Rohan and partially Anduin.
  - **Thranduil’s Halls (Woodland Realm)** supports Dale and partially Anduin.

- Alliances require:
  - Active diplomatic alliance
  - Control of key Elven strongholds
  - Allied factions holding critical settlements and maintaining sufficient territory

- Allied factions will periodically provide:
  - Gold contributions
  - Reinforcement armies based on their culture and military identity

- Alliances progress through tiers (Low → Medium → High), improving:
  - Quality and size of reinforcements
  - Amount of financial aid

- The **Anduin Vale** alliance is shared between Lórien and the Woodland Realm, with support depending on which capital is controlled.

- Aid frequency depends on the current alliance tier:
  - **Low Tier** — infrequent support with smaller armies
  - **Medium Tier** — more regular reinforcements and larger aid shipments
  - **High Tier** — frequent elite reinforcements and substantial financial support

- Alliances can weaken or break if:
  - Key settlements are lost
  - Allied factions decline in power
  - Strategic capitals fall

- Added faction-specific reinforcement pools to reflect each ally’s unique military style.

- Added new events, UI elements, and notifications to track alliance status, growth, and aid deliveries.

- Encourages cooperative gameplay, protecting and strengthening allied kingdoms rather than conquering them.

## Elven/Dwarven Stat Overhaul

## Dwarves
- Increased armour across the board
- Slightly nerfed defense skill and melee damage

## Elves
- All elven units get “Relentless” animations
- Increase all attack and defensive stats
- Melee damage greatly increased
- Missile damage greatly increased
- Armour (around 9-20)
- Defense skill (around 9-20)
- Shield (around 7-10)
- Smaller unit size (generally 80-100)
- Terrain Effects/Bonuses improved greatly
- Increase Movement Speed
- Increase Unit Mass
- Add AP Arrows

The Following Units gets ap arrows
- Rivendell Rangers
- GilGalads Company
- Elderinwe Thurudir
- Tawar Areiniyr
- Aredhirith
- Elbereths Sentinels
- Berio I Thoronaid
- Galadhrim Chosen
- Berio I Ngelaidh
- Gurveleg
- Elderinwe Rocthinim
- Elladans’s Bodyguard
- Greenwood Rangers

## Angmar
- Overhaul entire Angmar faction (Thank you Armolitskiy)
- New starting conditions
- Entirely new roster and units
- Split barracks (Orcs/Angmarin/Hillmen)

**Slaving**
- Angmar generals can get the "Slavedriver" trait
- Certain units such as Thralls now replenish faster based on the % of slave culture present in the settlement
- Angmar's slave market provides additional income based on the % of slaves in the settlement

**New Scripts**
- Once the Witch-king of Angmar has returned and the Dark Lord Sauron has the One Ring, you can summon plagues across Middle-earth to cripple other factions and destroy their populations.
- Ally with Gundabad to gain the ability to recruit Snow-Orcs from your orc barracks or conquer Mt. Gundabad to recieve much more.
- Capture historical Numenorean settlements such as Fornost, Annuminas and Ost Sul to receive custom Black Numenorean generals and reinforcements from Mordor.
- Conquer Eriador and herald the return of the Witch-king to his rightful domain in Angmar. Capture Fornost, Imladris, and hold Carn Dûm. Like other Nazgûl, he will respawn after 15 turns if killed.

**Settlements**
- Rename Athilin to Imlad Nin (wet valley) and rework the terrain around it accordingly
- Rename Nocvha Rhaglaw to Rhaglaw and make it the home of the Rhudaur remnants. 
- Change Barchaleg into a castle and move some if it's infrastructure into Rhaglaw
- Add a new landmark building, the "Hallowed Halls of Rhuduar" to Cameth Brin

## Rohan
- Update Eomer's custom portrait
- Update the Glittering Caves script with new building UI, a custom Guard of the Caves general upon upgrading the caves, the ability to gain points with Khazad-Dum, -g for the fact that EL can accept the rings, Dwarven Labourer recruitment and updated event text
- Removed Eomer as a general at game start for the Rohan player. He now respawns when Theoden is renewed. Theoden now has a chance to renew that scales based off - settlements owned and battles won rather than spawning at a fixed turn.
- Update Rohan's event pictures
- Give Rohan a load of custom bodyguards and make player Rohan have significantly smaller armies at game start
- Added Rohan elite Bannerman (Thank you Lerynian)
- Make the negative effects of the "Deceived by Grima" far more severe
- Give Night Fighter to Eomer

## Erebor
- Added 5 new units
  - **Gimli's Company** (Re-statted King's Axes)
  - **Dain's Royal Guard**  (Re-statted Axeguard of Erebor)
  - **Thorin's Retinue** (Re-statted Sons of the Fallen)
  - **Gloin's Company** (Re-statted King's Warriors)
  - **Trollbane Ballista** (Cheap, single unit ballista intended for dealing with monster units)
- Adjusted Dwarven Grudges effects and adjusted some garrisons in Gundabad.  
- Reduce Erebor generals starting command
- Thank you "a rainy day" for most of these changes and Bregathel for the writing for the new units!

## Anduin
- Add new unit models for Eotheod Longbowmen, Eotheod Horse Archers, Eotheod Footmen and Eotheod Cavalry (Thank you Jayzinski)
- Update Eotheod unit stats to account for new models
- Add honey to Rhosgobel
- Add an apiary to Beorns Hall

## Khazad-Dum
- Added new unit models for Legion Shieldguard, Deeping Guard and Hammerguard
- Added new unit models for First Legion and Zentih Guard
- Added new unit models for Balin's Guard, Khazad-Dum Guardians and Reclaimers
- Added new unit models for Dragonslayers
- Added new projectile models for some Dwarven units

## Lorien
**Units**
- Gurdhinen and Gurveleg can only be recruited in Castle “Town Hall”
- Gurdhinen can only be recruited in Castle “T2+ Town Hall”
- Gurdhinen get AP throwing knives as primary weapon, secondary double-bladed
- Gurveleg can only be recruited in Castle “T3+ Town Hall”
- Gurveleg can only be recruited in “Forest” region
- Gurveleg gets dual swords as secondary
- Increase Gurveleg arrow's range, accuracy, and ammo
- Change Yavanna’s Chosen weapon to 2H spear (with halberd animation)
- Remove spear wall ability (Galadhrim Guard and Yavanna’s Chosen)
- **New Unit:** Galadhrim Guardians
  - Spear & Shield Infantry
- **New Unit:** Lorien Dyrith (Lowest tier unit)
  - Primary: Bow
  - Secondary: 2H spear (with halberd animation)
  - Lorien Dyrith can only be recruited in Castle & City “Town Hall”
  - Lorien Dyrith can only be recruited in T1 & T2 “Town Hall”
- **New Unique Bodyguard Unit:** Berio I Thoronaid
  - Bodyguard of Celeborn
  - Copy of Berio I Ngelaidh but slightly stronger
- **New Unique Bodyguard Unit:** Silvan Edtauryn
  - Bodyguard of Haldir, Rumil, and Orophin (Starting)
- **New Unique Bodyguard Unit:** Galadhrim Chosen
  - Bodyguard of Haldir, Rumil, and Orophin (Upgraded)
- All Lorien archer units gain +1 to +2 extra missile damage compare to other elven archers
- All Lorien archer units gain shield piercing arrows
- Add a custom Yavanna's Chosen general for Lorien when they form the union

**Building**
- Add Minor Settlement:(in Caras Galadhon region)
  - Sarnol
    - Castle
- Add Landmark Building in Sarnol:
  - Cerin Amroth
    - Free upkeep: +1
    - Population Growth: +1%

**Player Starting Position**
- Caras Galadhon and Sarnol
- Limhir becomes rebel at the start
- Spawn Goblin army near Khazad Dum to delay KD steamrolling Dol Guldur

**AI Auto-expansion**
- Caras Galadhon, Sarnol, and Limhir

**Improved AI Garrison**
- Caras Galadhon and Sarnol

**Script**
- Allegiance of Old

## Woodland Realm
**Units**
- Added new unit models for Aredhirith and the Elvenkings units
- Thranduil’s BG gets ap
- Woodland Wardens & Hin e-Daur can only be recruited in Castle “Town Hall”
- Woodland Wardens can only be recruited in Castle “T2+ Town Hall”
- Hin e-Daur can only be recruited in Castle “T3+ Town Hall”
- Hin e-Daur can only be recruited in “Mirkwood” region
- **New Unit:** “Woodland Tirnas” (Lowest tier unit)
  - Primary: Bow; Secondary: 1h axe
  - Woodland Tirnas can only be recruited in Castle & City “Town Hall”
  - Woodland Tirnas can only be recruited in T1 & T2 “Town Hall”
- **New Unique Bodyguard Unit:** Pilin i-Thewair
  - Bodyguard of Legolas (Starting)
  - Copy of Woodland Sentinels but slightly stronger
- **Unique Bodyguard Unit:** Greenwood Rangers
  - Bodyguard of Legolas (Upgraded)
  - AP arrows with 1h sword

**Building**
- Add Landmark Building (in Taur Philin)
  - The Forest Gate of Mirkwood
    - Free upkeep +1
  - The Elf-path
    - Population Growth +1%
    - Trade Bonus

**Player Starting Position**
- Thranduil’s Halls and Taur Philin

**AI Auto-expansion**
- Thranduil’s Halls, Taur Philin and Emyn-nu-Fuin

**Improved AI Garrison**
- Thranduil’s Halls, Taur Philin

**Script**
- Allegiance of Old
- Legolas can now upgrade his bodyguard unit

## High Elves
- Add 1 armour level to HE generic BGs and adjust Lindar BG upgrade look
- Adjusted Amanyar unit cards
- Add Galdor Company unit
- Allow HE military buildings to stack 2 units for most units
- Move Mirdain faction overview info to its own fancy new tab
- Add small Mirdain event with the excavations
- Make HE mirdain script less random
- Update Glorfindel starting BG
- Improved AI garrisons in Mithlond, Harlond, Forlond

## Northern Dunedain
- Eldarion custom portrait/biography/bodyguard
- Add new custom bodyguard units Eradan's Company and Dunedain Troll-slayers for Eradan and Elegost respectively (Thank you Maverick for the models and High King -or writing/ideas)
- Update Rangers unit cards
- Swap Troll-men Warriors in RK Barracks for Muhad Beastmasters
- Update RK event pics
- Rebalance Steelbow units
- No lil bitch gobbo peace out strats

## Dale
- Add Dalian Byrdest and Lake-town Wardens as recruitable general's bodyguard units for Dale

## Ar-Adunaim
- Add 20 new custom traitorous AA generals (Thank you Juoppo!)
- Add some units to T3 AA Warrior's Guild
- AA units stats rebalance
- Give AA some pop/culture growth in ports/merchants wharf buildings
- Update NumenoreanRace trait desc to make it clear they aren't actual "Black Numenoreans"
- Fixed some inconsistencies in Conscription Camp

## Dunland
- Add random Dunland event that gives them the oppurtunity to learn how to breed wargs or keep their ancestral ways
- Updated Dunland's unit cards
- Make Skreulingir relentless

## Bree
- Update Bree Dwarvern commander strat model to use a modified version of the Ered Luin strat model instead of a KD model
- Updated some Bree Custom Commander portraits and some of Dunland/Bree's general portrait pool (Thank you Harn!)

## Gondor/DA
- Add new Sea Hunting building line for Dol Amroth/Gondor
- Adjusted how some Gondorian units behave in autoresolve
- Move Gondor RK script to Lua (and hopefully fix the few bugs there)
- AI Gondor/Dunedain can form RK under extreme circumstances 
  - Denethor is dead, Minas Tirith is held, Aragorn is alive, Boromir and Faramir are alive etc.

## Mordor
- Make Mordor more defensive if the player is Harad/Khand/Rhun
- Adjusted how some Mordor units behave in autoresolve
- DG keep old bodyguards during Mordor merge
- Nerfed Nazgul in auto-resolve
- Give Minas Morgul a barracks at game start
- Make the Black Gate and Minas Morguls's initial Men of the East recruit pools a bit more random and dependant on if the player is one of those factions

## Harad
- Harad black ships in Umbar
- Add "The Twelve" - a super rare one time use mercenary unit of twelve men that can appear in Harad. Thank you Resident Arnorposter for the kitbash.
- Remove Gimilkhad and Gimilzor from Harad name list*
- Give Harad a less Arabic name pool

## Dorwinion
- Adjust Dorwinion Shieldbearer/Retainer stats slightly
- Nerf Leofthiuda Far-Riders armour
- Adjusted Justiciar upkeep

## Dol Guldur
- Added new unit models for two of the Goblin units

## Battlemaps
- Add DaC V5 Lorien battlemap
- Update clear weather lighting colors to better match skybox

## Scripts/Mechanics
- Trading settlements via diplomacy now spawns in a random army for the new owner instead of random mercerenaries or often nothing at all
- 1% Chance to spawn a random general everytime a pit fight is held (Orcs/Isengard only)
- Recruitable ethnic/racial/cultural bodyguard units
- Added the ability to gain hero abilities from buildings. Supports 17 different hero abilities.
- Add 5 new hero abilities. "Curse" (For Wights, with 4 different sound effects), "Drums" (For Orcs with 4 different sound effects), "Focus" (Generic), "Blizzard" -/Dwarves), "House of Telcontar" (Elessar/Eldarion)
- Allow the custom naming of individual's alias
- Add a new UI where you can see all the governor/military effects and what trait/ancillary is giving them that effect

## Recruitable Bodyguards
- Make Rhun's ethnic bodyguards recruitable from the Khan's Tent (Availability based on progress through the Unite the Clans script)
- Make Leofthiuda Bodyguard and Kugath Chieftains recruitable generals from the Dorwinion Military Academy
- Skin-changers can now be recruited from the Apiary building line, Sons of Marwhini can be recruited from the Barracks line if you have an alliance with Rohan, -can be recruited from the Barracks line in Mirkwood and Stoor Council can be recruited in Fenholm.
- Make Dunland's ethnic bodyguards recruitable from various buildings
- Make Ered Luin ethnic bodyguards recruitable from Thorin's Halls (Grimborn Bodyguards can be recruited from Skorgrim's Halls in Buzra Dum also)

## Armour Upgrades
- Add a bunch of new armour tier names and fix Bree getting T5 Armour/Arnor visuals from merc path
- Dunland and Enedwaith can get highest tier of armour if they side with Saruman
- Angmar can get highest tier of armour if the Witch-king returns and an additional tier if they keep the One Ring
- Rhun can all get highest tier of armour if they keep the One Ring
- Mordor, DG and Goblins can all get highest tier of armour if Sauron claims the One Ring
- Gondor, Dol Amroth and AA can all get highest tier of armour upgrade for keeping the One Ring
- Harad gets armour upgrades from Unite the Tribes script and the Haradwaith script
- Enable Isengard to get tier 5 armour by finding the One Ring
- Khand can get the highest tier of armour if they stay loyal to Sauron
- Anduin can get the highest tier of armour if Mirkwood and the roads are safe
- Dorwinion gets Tier 5 armour from siding with Sauron

## UI/Text 
- Adjusted nearly every single faction colour to feel more "Lord of the Rings" and parseable at a glance on the map. Also added a config option to revert to old colours if necessary.
- Add new culture specific Half Scroll banner images for the "Details" and "Attributes" tabs
- Removed stupid Chinese dragon on Rhun banners and replaced it with a more Persian symbol
- Display a "Red Book" instead of a "Green Book" in minor settlements so that players know if they are a minor settlement. Also, explain what a minor settlement is in -iption of the red book.
- Update faction selection screen starting regions/colours
- Stylize and polish the Spy Network menu a bit and add custom tooltip colours for each faction (#73)
- Improve faction descriptions on faction selection screen
- Update Gundabad temple descriptions
- Add "Bonus damage vs. creatures and chariots" and "Splitshot Arrows" to effect text
- Show exact terrain boni/mali in unit descriptions
- Add Twin Hall of the Twofold King text for Dunland
- Update campaign menu faction descriptions
- Add information about how you can recruit your various bodyguard units in the faction overviews
- Add an upgrade section in the character detail panel for characters that can recieve upgrades
- Fixed the problem where when paused you can't see stats before starting battle
- Witch-Realm/King -> Witch-realm/king
- Updated settlement overview icons/pips
- Changed middle-earth -> Middle-earth
- Capitalized race names like elf -> Elf, hobbit -> Hobbit etc.

## Guilds
- Make Thieves Guild give a lot more spies
- Add the ability to Invest (10,000 gold = 12.5% progress) or Banish (reset progress to 0) guilds in each settlement
- Make rarer guilds more readily available 

## Sounds
- Add support for the Copyright Free Sound pack and add the ability to easily customize it
- Add a new battle announcer voice for Orc factions (Thank you Wii-san!)
- Give Rohan generals for Gondor a Rohan voice and vice versa
- Add missing voicelines for new general units
- Guild tab now shows where the Tier 3 building is located and is a bit more streamlined
- Give Nazgul custom selection sounds in batttle

## Traits/Ancillaries
- Added a new Pit Champion trait for Orc factions
- Added a Nomad trait for Good Khand
- Old age trait now triggers more at higher ages
- Rename the Winter trait names
- Remove/adjust some neglible traits/anc effects
- Added some new healing ancillaries for Elves
  - Healer, Antidote of Lothlórien, Healing Vial of Mirkwood, Athelas of Imladris, Henbane of Lindon

## Hero Abilities

## Performance
- Delete a bunch of unused strat models
- Speed up Lua dev environment

## Misc.
- Reduce size and cost of Brandatudnas units to better reflect their in-game description
- Nerf foreign spy conversion rate a bit
- Make evil dwarves hate humans a bit more
- Make Spy Network and Slow Motion keys rebindable. Add a new AGO/WASD themed keyset
- If a character has dread it can't degrade now
- Make sure factions set their capital to their capital (e.g Dale will always be the capital of Dale if they control it)
- Make it random who the White Council picks to destroy the ring (Elrond, Gandalf, Aragorn, Celeborn, Cirdan) instead of usually just choosing Elrond
- Give Guardians of Enedwaith shield piercing
- War Maidens can now screech to buff/debuff friendly/enemy morale
- Make Trebuchet better against walls
- Added a notification telling you when a Palantir is ready to be used again
- Reduce morale of Farmhand Pikemen and all siege
- Update some swamp textures to be more parseable
- Grant AA access to T3 Warrior's Guild (Thank you DVM for the building description)
- Remove "light_spear" from a few halberd units
- Buff Dragonswrath unit stats/reduce size
- AA, Khand, Rhun and Harad all get a better public health bonus from Public Fountains/Baths to compensate for their lack of pop growth buildings
- Adjust recruit morale bonus effects from buildings
- Update Haradwaith/Forodwaith region colors to blend better with the map
- No Cameth Brin for AI HE
- Add Fountain Guard and Varyando Evendim to the T2 Waystation
- Add Avari to T2 WR Waystation
- Update the skybox so it actually fits the battlemap correctly
- Remove Longbeard Phalanx/Longbeard race trait combo
- Make area around Anuben embarkeable
- Remove control DA option
- Disable the ability to retry/ignore Lua errors
- Optimized some Goblin models for better performance

## Bugfixes
- Fixed AI taking control over the player's armies in certain circumstances
- Fix being neutral with rebels in Shattered Alliances
- Fix Lua exception when starting a historical/scenario battle
- Fix Anfalas BG upkeep
- Update units using crappy vanilla horses to use the new Marka ones
- Fix Arnor units coming from Ranger Guild without Arnor
- Slightly buff the garrison units in Minas Morgul
- Fix "First Commander First Commander"
- Gave axethrower units the "thrown" attribute like they should have
- Fixed Dunedain Pikemen's sprites
- Reduce anti-cav bonus for some lower tier units
- Make Mumak general bald
- Give all avari units free upkeep
- Add missing coast hidden resource to a few regions
- Fix Gondor merge not working for AI
- Rhun leader can't become Inquisitor!
- Correctly update faction relations/ring sides when RK vassalizes Khand/Rhun/Harad
- Exclude Treebeard from certain historic events
- Fix AA Captains missing weapon
- Fix weird map generation around a river in Enedwaith
- Fixed AI Dorwinion relentlessly spamming Kantors all over the map
- Fixed AI Dorwinion forceably building a Kantor in your lands
- Fix issues with the Dwarven Grudges trait 
- Fix some instances of spawned characters being in the family tree when they shouldnt
- Fix some issues with rebel factions in Harondor
- Fix dodgy shadows on Mumakil
- Fix Trollmen Champions missing weapons
- Fix bug with Eorl's Horn not being correctly transferred to EL faction leader
- Fix Dorwinion wrong starting chars wrong strat models
- Fix Lua error related to spawning the ring
- Fix some issues with RK recruitment (Thank you ohno)
- Fix Amrothian Squires in Waystation
- Fix double Avari fort crash (maybe)
- Fix Rebuilt Dome of the Stars global bonus not doing anything
- Fix some boat pathfinding issues around Dol Vorn and a black spot of land near Gundbad
- Fix road generation near Celoniach
- Fix missing floating banners for Arnor and routing banners
- Fix Aragorn's quest tab bugging out
- Prevent ring respawning after going to Grey Havens
