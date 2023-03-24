# Import necessary modules
from psychopy import visual, event, core
import random
import psychopy.iohub as io
from psychopy.hardware import keyboard

# Set up the window
win = visual.Window([1366, 768], fullscr=True, allowGUI=True, monitor='testMonitor', units='deg')

# Define the gratings
grating1 = visual.GratingStim(win, tex='sin', mask='gauss', size=10, pos=(-5, 0), sf=0, ori=0)
grating2 = visual.GratingStim(win, tex='sin', mask='gauss', size=10, pos=(5, 0), sf=0, ori=0)

# Define the user input mapping
user_input = {'d': 45, 'h': 0, 'v': 90, 'q': None}

# Define the parameters
sp_list = [3, 5, 7.5, 10, 15, 20, 24, 30, 36, 40]
orientation_list = [90, 45, 0]


# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Start the trial loop
for i, sp in enumerate(sp_list):
    # Randomly choose the orientation of the gratings
    orientation1 = random.choice(orientation_list)
    orientation2 = random.choice(orientation_list)

    # Set the orientation of the gratings
    grating1.ori = orientation1
    grating2.ori = orientation2

    # Display grating1 for 3 seconds and get user input
    grating1.sf = sp
    print(sp)
    grating1.contrast = 1
    trial_clock = core.Clock()
    while trial_clock.getTime() < 3.0:
        grating1.draw()
        win.flip()

        # Get user input
        keys = event.waitKeys(keyList=['d', 'h', 'v'])
        if keys:
            if user_input[keys[0]] == orientation1:
                break
#    win.flip()
    # Display grating2 for 3 seconds and get user input
    grating2.sf = sp
    print(sp)
    grating2.contrast = 1
    trial_clock = core.Clock()
    while trial_clock.getTime() < 3.0:
#        grating1.draw()
        grating2.draw()
        win.flip()

        # Get user input
        keys = event.waitKeys(keyList=['d', 'h', 'v','q'])
        if keys:
            if user_input[keys[0]] == orientation2:
                break
            elif user_input[keys[0]] == 'q':
                core.quit()

    # Check user input and adjust contrast accordingly
   
    if not keys or user_input.get(keys[0]) != orientation1 or user_input.get(keys[0]) != orientation2:
        c = 1
        while True:
            c -= 0.1
            if c <= 0:
                break
            grating1.contrast = max(0.0, min(c, 1.0))
            grating2.contrast = max(0.0, min(c, 1.0))
#            grating1.contrast = c
#            grating2.contrast = c
            grating1.draw()
            grating2.draw()
            win.flip()
            keys = event.getKeys(keyList=['d', 'h', 'v','q'])
            if keys:
                if user_input[keys[0]] == orientation1 and user_input[keys[0]] == orientation2:
                    break
                elif user_input[keys[0]] == 'q':
                    core.quit()
                    
    # check for quit (typically the Esc key)
    if defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # Display the current sp and c values
    if i == len(sp_list)-1:
        sp_text = visual.TextStim(win, text=f'Current sp: {sp}, Current c: {c:.1f}', pos=(0, 0))
        sp_text.draw()
        win.flip()
        core.wait(2)

# End the experiment
#win.close()
#core.quit()
core.wait(0)
#core.quit()