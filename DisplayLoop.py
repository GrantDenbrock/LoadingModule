import os
import time
import sys


class DisplayLoop:
    """
    Displays frames of text one after the other on the command line. Useful for "loading" type of animations.

    Usage:
    from DisplayLoop import *
    loop = DisplayLoop()
    loop.exit = False # init condition
    thread = threading.Thread(target=loop.<method>) # choose a method
    thread.start()

    <code to execute while loop of text is displayed>

    loop.exit = True # exit condition to stop your display loop
    """

    # colors/fonts to choose from to render your loader.
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[96m'

    def __init__(self, path_to_frames=None, custom_load_steps=None, color=OKCYAN):
        if path_to_frames == None:
            path_to_frames = ""
        if custom_load_steps == None:
            custom_load_steps = []
        self.exit = None
        self.path_to_frames = path_to_frames
        self.color = color
        self.frame_load_steps = []
        self.frame_longest_string = 0
        self.node_steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.spin_load_steps = ["|", "/", "-"]
        self.custom_load_steps = custom_load_steps

    def get_text_from_frames(self):
        """
        Iterates through the sorted() list of frames specified in the path_to_frames parameter
        and generates a list of text elements for the display loop to loop over.

        Also returns the longest string in the list so when we clear the terminal
        we get all the text that was there before the next frame is displayed.

        :return: text_strings, longest_string
        """

        for file in sorted(os.listdir(self.path_to_frames)):
            f = os.path.join(self.path_to_frames, file)
            with open(f, 'r') as fin:
                self.frame_load_steps.append(f'{self.color}' + fin.read() + '\033[0m')
        self.frame_longest_string = len(max(self.frame_load_steps, key=len))

    def render_loader(self, loader):
        # figure out what loader we want to render i.e. what text we are looping over...
        if str.lower(loader) == "custom":
            loading_text = self.custom_load_steps # already defined in params
        if str.lower(loader) == "node":
            loading_text = self.node_steps # already defined
        if str.lower(loader) == "spin_load":
            loading_text = self.spin_load_steps # already defined
        if str.lower(loader) == "frames":
            self.get_text_from_frames()
            loading_text = self.frame_load_steps
        longest_string = len(max(loading_text, key=len))

        sys.stdout.write(' ')
        while True:
            if self.exit:
                sys.stdout.flush()
                sys.stdout.write('\b' * longest_string + "\n\n")
                print("")
                break
            for text in loading_text:
                time.sleep(0.5)
                sys.stdout.write('\b' * longest_string + f'{self.color}' + text + '\033[0m')
                sys.stdout.flush()