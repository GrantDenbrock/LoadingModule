# def loop_through_frame_text(self):
#     """
#     loops through the text elements in the frames specified in parameters.
#     """
#     sys.stdout.write(' ')
#     while True:
#         if self.exit:
#             sys.stdout.write('\b' * self.frame_longest_string)
#             sys.stdout.write('\b')
#             break
#         for text in self.frame_load_steps:
#             time.sleep(0.5)
#             sys.stdout.write('\b' * self.frame_longest_string + text)
#             sys.stdout.flush()
#
# def play_frames(self):
#     """
#     Loops through the frames defined in the path_to_frames parameter.
#     If none were provided, this will loop through an empty list...printing nothing.
#     :return:
#     """
#     list_of_text_strings, longest_string = self.get_text_from_frames()
#     self.loop_through_frame_text(list_of_text_strings, longest_string)
#
# def node_load(self):
#     """
#     Loops a loader that looks like npm.
#     :return:
#     """
#     sys.stdout.write(' ')
#     while True:
#         if self.exit:
#             sys.stdout.write('\b')
#             break
#         for text in self.node_steps:
#             time.sleep(0.5)
#             sys.stdout.write('\b' + f'{self.color}' + text + '\033[0m')
#             sys.stdout.flush()
#
# def spin_load(self):
#     """
#     Loops a loader that looks like the standard spinning cursor.
#     :return:
#     """
#     sys.stdout.write(' ')
#     while True:
#         if self.exit:
#             sys.stdout.write('\b')
#             break
#         for text in self.spin_load_steps:
#             time.sleep(0.5)
#             sys.stdout.write('\b' + f'{self.color}' + text + '\033[0m')
#             sys.stdout.flush()
#
# def custom_load(self):
#     """
#     Loops a loader that uses characters defined in the custom_load_steps parameter.
#
#     :return:
#     """
#     longest_string = len(max(self.custom_load_steps, key=len))
#     sys.stdout.write(' ')
#     while True:
#         if self.exit:
#             sys.stdout.flush()
#             sys.stdout.write('\b'*longest_string + "\n\n")
#             print("")
#             break
#         for text in self.custom_load_steps:
#             time.sleep(0.5)
#             sys.stdout.write('\b'*longest_string + f'{self.color}' + text + '\033[0m')
#             sys.stdout.flush()


git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/GrantDenbrock/LoadingModule.git
git push -u origin main