# GameInterfacePOC
Quick MMO project with Griff

NOTE ON USING GIT: I'm not sure how to get it to delete compiled files on your
local copy since we're ignoring .pyc files in git.  The reason this will be 
potentially important: if we delete a file, the compiled copy will remain.
That might end up getting imported by something running.  Basically, just
clean up your own compiled files every once in a while

Run the index.py script in Game dir (vscode ctrl+shift+b, or debug with f5)
 - Move with arrow keys, spawn enemies with enter and move with WASD.  
 - Abilities will be used with the number keys, shift+number will level up
 - Tab will attempt to target nearest enemy, will not target out of range

¯\_(ツ)_/¯ <=====3