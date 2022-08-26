from DisplayLoop import *
import threading

# --- initialize the animation loop ---
# if you want it to use frames...
path_to_frames = './frames/LoadingWheel/'  # frames should go in a directory and be organized in a way that, when sorted, come back in alphabetical order.

loop = DisplayLoop(path_to_frames)  # Note that color arg is optional...

loop.exit = False # built-in exit condition. Should be False to start the looping. True when you are ready to exit.
# ---  ---

# --- start the looping in another thread... ---
t = threading.Thread(target=loop.render_loader, args=("frames",))  # args can be in "custom", "node", "spin_load", "frames".

t.start()

# running code where we are displaying loading in the meantime...
time.sleep(3)

# at the end of that code, finish the loading animation:
loop.exit = True
# ---  ---


# now your code is finished. TODO It seems like the terminal cursor needs to be bumped off still which is annoying...
print("\n")  # bump it...
print("finished.")

# 5 lines of code to implement a loader! not too bad... IG 6 if you count the fact that you need to add a bumper ;)

# TODO make this a decorator that I can apply to other functions instead of bookending the code with the thread.
