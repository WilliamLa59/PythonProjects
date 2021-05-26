# RiotAutoLogin
A simple python script that will automatically log you into a specified riot account if you have multiple 

If you run the script try not to tab into a different window, as the script assumes that the riot client is already selected.
Feel free to make changes to the sleep timer. 8 seconds is what I find the most consistent.

## This script requires pynput 

	Use the command "pip install pynput" in cmd to install 

### Minor edits to the script must be made to properly login to riot account

## "applocation" needs the absolute path of the game client you want to launch. You'll also need to replace any "\\" with a "//"
	
	"G:\Riot Games\LoL\LeagueClient.exe" becomes ---> "G://Riot Games//LoL//LeagueClient.exe"
For league you can point to "LeagueClient.exe" straight in the league install directory.

For a game like valorant where the client points to the actual Riot client before launching the game you'll need to do a few steps 
	
	1. Create a shortcut of the VALORANT.exe located in your valorant install directory
	2. Right click on the shortcut and go to properties
	3. Add the following launch options to the "Target" textfield. Do not replace whats already in the textfield as the path of the client should already be there
	   --launch-product=valorant --launch-patchline=live
	4. Hit apply and set the "applocation" to the path of the newly created shortcut

## "username" needs the username of the account you want to sign in as

## "password" needs the password of the account you want to sign in as


