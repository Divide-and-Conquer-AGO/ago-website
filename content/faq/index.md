---
title: "F.A.Q"
toc: "true"
description: "Frequently asked questions about AGO"
---

--------------------------------

## Frequently Asked Questions

## Game Mechanics

#### What are minor settlements?
Minor settlements function essentially the same as normal settlements with the following caveats. You cannot construct culture buildings, roads, ports, mines or farms in minor settlements however they do share the benefits of these building types if they are built in the main settlement of that region. They share the culture and hidden resources of the major settlement in the region.

#### Why are all the banners on the map full?
It's a new mechanic to encourage more use of spies and scouting. If you want to turn it off, you can turn if off by toggling the 'Hide Army Info' setting.

#### How can I automatically sort my armies?
Select an army and press CTRL+Z. You can change this in the shortcuts menu.

#### How can I enable surround sound?
Go to the Sound settings in-game and select EAX4 as your sound provider

#### How can I enable DXVK rendering mode?
Enable it in the launcher, make sure to read the tooltip.

#### What is DXVK rendering mode?
DXVK is a set of software libraries that translates DirectX API calls to Vulkan API calls. Depending on your hardware, especially if your GPU is not very modern or you use an AMD card, this mode can help boost performance. Please note that the game is still generally CPU bound and this setting will not help with that.

#### How can I enable automatic Freecam integration??
Enable it in the launcher.

#### How can I contribute to the mod?
We have a generally pretty open contribution model so if you have some skills you think are useful, please reach out and we can try and get you set up.

## Game Issues

#### Requirements
- [Steam copy of Total War: MEDIEVAL II – Definitive Edition](https://store.steampowered.com/app/4700/Total_War_MEDIEVAL_II__Definitive_Edition/)
- 4GB+ Memory
- Disk versions patched to at least version 1.5 with the Kingdoms expansion should work but we can't guarantee it as there are many different disk versions of the game. You can redeem your CD key on Steam for a full, free copy of the Definitive edition.

####  Pirated copies of Medieval 2
The mod is known to cause issues with pirated copies of Medieval 2 and is likely to crash, do not ask for support if you have a pirated copy as we do not know or particularly care why it doesn't work. We have no idea how to fix it so it is just a waste of everyones time.

#### Anti Virus is triggered
The [Engine Overhaul Project](https://github.com/youneuoy/M2TWEOP-library) and [AGO Launcher](https://github.com/Divide-and-Conquer-AGO/ago-launcher) often get detected as a Trojan by Windows Defender or 3rd party anti-virus. To be able to play with it enabled you need to make an exclusion to the mod folder. The reason it gets detected is because it works by modifying the memory of another program when you run it (Medieval 2), which is similar to what some malicious programs would do to other programs you don't want it to happen to.

**Windows Defender - Adding an exclusion**
- Go to Start > Settings > Update & Security > Windows Security > Virus & threat protection.
- Under Virus & threat protection settings, select Manage settings, and then under Exclusions, select Add or remove exclusions.
- Select Add an exclusion, and then select the mod folder (e.g `E:/Steam/steamapps/common/Medieval II Total War/mods/ago_beta/` or whatever your mod folder is).
- If `M2TWEOP_GUI.exe` or `AGO_Launcher.exe` got deleted then consult [Restore quarantined files in Microsoft Defender Antivirus](https://learn.microsoft.com/en-us/defender-endpoint/restore-quarantined-files-microsoft-defender-antivirus)

**Norton 360, Bitdefender, and McAfee - Adding an exclusion**
- Seek help online

**Additional Troubleshooting Steps**
- Set `AGO_Launcher.exe` to run as admin
- Set `M2TWOP_GUI.exe` to run as admin

#### The mod won't start
* Re-apply LAA to your medieval2/kingdoms.exe (Run `tools/Large Address Aware/Large_Address_Aware.exe`)
* Set the medieval2/kingdoms.exe to run as admin
* Restart your PC
* For Steam versions make sure you are logged in to steam
* Make sure your mod folder name does not contain spaces
* If you are using Reshade, first delete d3d9.dll in the game folder, then copy d3d9.dll of Reshade to the game folder, then rename it to dxgi.dll and only then launch the mod

**If you are still having issues**
* If you are using submods or have modified your game make sure to mention this
* Post a screenshot of your mod folder with the *full* path showing at the top 
* Provide a save if you are consistently crashing in the same place
* Describe in detail what you have done already to attempt to solve the problem
* Describe in detail what is happening/what you are doing when you encounter the issue
* Write what Windows version you are using (Windows 11 is known to cause issues with Medieval 2)

#### Game crashes with a "Pure virtual function call" message
This is a rare medieval 2 bug that can happen if a faction gets destroyed. There is no fix other then making sure the faction doesn't die and trying at a later point.

#### Game freezes with windows loading icon
It is likely a faction is going horde (Ar-Adunaim). You have to wait it out, don't click on anything to make it stop responding, be warned it can take up to 10 minutes or more for some people for a faction to go horde.

#### d3dx9_43.dll and XINPUT1_3.dll were not found
Install Directx from this link: https://drive.google.com/file/d/1Do4Uu5j_7xX5Jw8IqNuSjMMnnATPsDTa/view?usp=sharing and restart your PC.

#### Vanilla starts when trying to start the mod
Open TATW.cfg and change the path after mod= to point to what you called your mod folder, also make sure your Steam launch options are empty!

#### Resolution issues
If your game is not running in the right resolution then check the settings for resolution in the launcher or via TATW.cfg. You can edit this with notepad, having your taskbar at the top of the screen bugs out borderless window.

#### Game returns to main menu when clicking 'Grand Campaign'
Run FullCleaner.bat in the mod folder.

#### Mod used to work but suddenly starts crashing at startup or loading any saves/battles
Check you still have M2TWEOP_GUI.exe and AGO_Launcher.exe in your mod folder (your anti-virus may have deleted them). Make sure to restart your PC also.

#### Launcher doens't open
Make sure to run the launcher as an adminstrator (Right Click -> Run as admin) or (Right click -> Properties -> Run this program as adminstrator)