import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import time



# define global variables
interval = 150
count = 0
status = True
score = 0
total_stops = 0
success_stops = 0
stop = True



def draw(canvas):
    text = format(count)
    canvas.draw_text( text, (80, 125), 42, "white")
    canvas.draw_text(str(success_stops) + '/' + str(total_stops), (190,30), 24, "pink")
    #canvas.draw_text(text, (190,30), 24, "pink")
    
    



def Start():
    timer.start()

    

    
def Stop():
    global total_stops, success_stops, stop
    #if stop == False :
    if count % 10 == 0 and count != 0 :
        success_stops += 1
        total_stops += 1
    elif count != 0 :
        total_stops += 1
    stopped = True
    timer.stop()
    
    
    
def Reset():
    global count, success_stops, total_stops
    count = 0
    stop = True
    total_stops = 0
    success_stops = 0
    timer.stop()


def tick():
    global count
    count += 1
        


frame = simplegui.create_frame("Stopwatch game", 250, 250)
frame.set_canvas_background('green')
        
        
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)


frame.start()
Reset()