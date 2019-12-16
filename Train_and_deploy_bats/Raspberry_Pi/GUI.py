# cd /home/pi/Desktop/deploy_classifier/
# python GUI.py
import os
import time as t
import random as rd
import math 
import gi
import os.path
import re

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf, GLib

class ButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ultrasonic Classifier")
        self.set_border_width(10)
        self.set_default_size(800, 480)
        
        hp1 = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        hp2 = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        hp3 = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        vp1 = Gtk.Paned.new(Gtk.Orientation.VERTICAL)
        vp2 = Gtk.Paned.new(Gtk.Orientation.VERTICAL)

        grid_01 = Gtk.Grid()
        grid_02 = Gtk.Grid()
        grid_03 = Gtk.Grid()
        grid_03.set_column_homogeneous(True)
        grid_03.set_column_spacing(20)
        grid_04 = Gtk.Grid()
        grid_04.set_column_homogeneous(True)
        grid_04.set_column_spacing(10)
        
######################################################################       
        hbox = Gtk.Box(spacing=6)
        hbox.set_orientation(Gtk.Orientation.VERTICAL)

        buttonZ1 = Gtk.RadioButton.new_with_label_from_widget(None, "Record some live audio")
        buttonZ1.connect("toggled", self.on_button_toggled, "1")
        hbox.pack_start(buttonZ1, False, False, 0)

        buttonZ2 = Gtk.RadioButton.new_with_label_from_widget(buttonZ1, "Process a batch of old recordings")
        buttonZ2.connect("toggled", self.on_button_toggled, "1")
        hbox.pack_start(buttonZ2, False, False, 0)

        buttonZ3 = Gtk.RadioButton.new_with_label_from_widget(buttonZ1, "Button 3")
        buttonZ3.connect("toggled", self.on_button_toggled, "1")
        hbox.pack_start(buttonZ3, False, False, 0)
        
        buttonZ4 = Gtk.RadioButton.new_with_label_from_widget(buttonZ1, "Button 4")
        buttonZ4.connect("toggled", self.on_button_toggled, "1")
        hbox.pack_start(buttonZ4, False, False, 0)
#######################################################################

        button1 = Gtk.Button.new_with_label("Play discovery roger audio")
        button1.connect("clicked", self.on_click_me_clicked)

        button2 = Gtk.Button.new_with_mnemonic("_Run Classifier")
        button2.connect("clicked", self.on_open_clicked)

        button3 = Gtk.Button.new_with_mnemonic("_Close")
        button3.connect("clicked", self.on_close_clicked)
        
        button4 = Gtk.Button.new_with_mnemonic("_Ignore")
        button4.connect("clicked", self.on_close_clicked)
        
        button5 = Gtk.Button.new_with_mnemonic("_Threshold")
        
        button6 = Gtk.Button.new_with_mnemonic("_Something Else")
        button6.connect("clicked", self.on_close_clicked)

        button7 = Gtk.Button.new_with_label("Play disc rog audio")
        button7.connect("clicked", self.on_click_me_clicked)
        
        button8 = Gtk.Button.new_with_label("Play disc rog audio")
        button8.connect("clicked", self.on_click_me_clicked)
        
        adjustment = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
        self.spinbutton_01 = Gtk.SpinButton()
        self.spinbutton_01.set_adjustment(adjustment)

        # a label
        self.label = Gtk.Label()
        self.label.set_text("Choose a threshold value ! ")
        self.spinbutton_01.connect("value-changed", self.spin_selected)
  
        check_numeric_01 = Gtk.CheckButton("Numeric")
        check_numeric_01.connect("toggled", self.on_numeric_toggled)

        check_ifvalid_01 = Gtk.CheckButton("If Valid")
        check_ifvalid_01.connect("toggled", self.on_ifvalid_toggled)
        
        checkbutton_01 = Gtk.CheckButton("Click me!")
        checkbutton_01.connect("toggled", self.on_ifvalid_toggled)
        
        grid_01.add(button1)
        grid_01.attach(button2, 1, 0, 2, 1)
        grid_01.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid_01.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid_01.attach(button5, 1, 2, 1, 1)
        grid_01.attach(self.label, 0, 5, 2, 1)
        grid_01.attach_next_to(self.spinbutton_01, button5, Gtk.PositionType.RIGHT, 1, 1)
        
        grid_02.add(button7)
        grid_02.attach(button8, 0, 1, 1, 1)
        grid_02.attach(check_numeric_01, 0, 3, 1, 1)
        grid_02.attach(check_ifvalid_01, 0, 4, 1, 1)
        grid_02.attach(checkbutton_01, 0, 5, 1, 1)

##########################################################################
        hp1.add1(hbox)
        hp1.add2(grid_01)
        hp1.set_position(300)   # Only max of 2 panes alloed.
##########################################################################       
        
        button9 = Gtk.Button.new_with_label("Play disc rog audio")
        button9.connect("clicked", self.on_click_me_clicked)

        button10 = Gtk.Button.new_with_label("STOP")
        button10.connect("clicked", self.on_click_me_clicked)
        color = Gdk.Color(40000, 0, 0)
        button10.modify_bg(Gtk.StateType.PRELIGHT, color)
        button10.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(65000, 0, 0)) # Red, Green, Blue, max 65535
        
        button11 = Gtk.Button.new_with_label("RECORD")
        button11.connect("clicked", self.on_click_me_clicked)
        color = Gdk.Color(0, 40000, 0)
        button11.modify_bg(Gtk.StateType.PRELIGHT, color)
        button11.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0, 50000, 0)) # Red, Green, Blue, max 65535
        
        button12 = Gtk.Button.new_with_label("Play audio")
        button12.connect("clicked", self.on_click_me_clicked)
        
        
        button13 = Gtk.Button.new_with_label("Play audio")
        button13.connect("clicked", self.on_click_me_clicked)
        
        button14 = Gtk.Button.new_with_label("Play audio")
        button14.connect("clicked", self.on_click_me_clicked)
        
        button15 = Gtk.Button.new_with_label("Play audio")
        button15.connect("clicked", self.on_click_me_clicked)

        media_box = Gtk.EventBox()
        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file("/home/pi/Desktop/GUI/goatlogo70high.jpg")
        image.set_from_pixbuf(pixbuf)
        media_box.add(image)
        media_box.connect("button_press_event",self.hello1)
        
        start_media_box = Gtk.EventBox()
        start_image = Gtk.Image()
        pixbuf_start = GdkPixbuf.Pixbuf.new_from_file_at_size("/home/pi/Desktop/GUI/start_250.png", 100, 100)
        start_image.set_from_pixbuf(pixbuf_start)
        start_media_box.add(start_image)
        start_media_box.connect("button_press_event",self.start)  # Starts the window of results in app.
        # start_media_box.connect("button_press_event",self.record_and_classify)
        # record_and_calssify does not connect until 'stop' is pressed! Not useful!!!!
        
        stop_media_box = Gtk.EventBox()
        stop_image = Gtk.Image()
        pixbuf_stop = GdkPixbuf.Pixbuf.new_from_file_at_size("/home/pi/Desktop/GUI/stop_250.png", 100, 100)
        stop_image.set_from_pixbuf(pixbuf_stop)
        stop_media_box.add(stop_image)
        stop_media_box.connect("button_press_event",self.stop)

        grid_03.add(media_box)
        
        grid_04.add(start_media_box)                         # Record
        grid_04.attach(stop_media_box, 1, 0, 1, 1)           # Stop
        
        grid_05 = Gtk.Grid()

        box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box1.set_homogeneous(False)

        self.label1 = Gtk.Label()
        self.label1.set_width_chars(60)
        box1.pack_start(self.label1, True, True, 0)
        
        # self.activitybar = Gtk.ProgressBar()
        # self.timeout_id = GLib.timeout_add(50, self.on_timeout_pulse, None)
        # self.activity_mode = True
        # box1.pack_start(self.activitybar, True, True, 0)
        
        self.label2 = Gtk.Label()
        self.label2.set_width_chars(60)
        box1.pack_start(self.label2, True, True, 0)

        grid_05.add(box1)

#########################################################################   
        hp3.add1(grid_02)                          # Some random checkboxes
        hp3.add2(grid_05)                          # Display text file
        hp3.set_position(200)
##########################################################################
        hp2.add1(grid_03)                          # Goat logo
        hp2.add2(grid_04)                          # Record / Stop recording.
        #hp2.set_position(310)   
##########################################################################    
        vp1.add1(hp1)                              # Check boxes and buttons
        vp1.add2(hp3)                              # Some random checkboxes and text box.
        vp1.set_position(120)
##########################################################################  
        vp2.add1(vp1) 
        vp2.set_position(360)
        vp2.add2(hp2)                             # Got logo and recording controls.
##########################################################################
        self.add(vp2)
##########################################################################

    def on_timeout_pulse(self, user_data):
        if self.activity_mode:
            self.activitybar.pulse()
        # As this is a timeout function, return True so that it
        # continues to get called
        return True
        
    def record_and_classify(self, button, event):
        print("\"Open\" button was clicked")
        file = "/home/pi/Desktop/deploy_classifier/bash_app"
        os.system("bash " + file)

    def stop(self, widget, event):            # Stop image.
        print("stop")
        stopFile = "/home/pi/Desktop/deploy_classifier/helpers/stop.txt"
        startFile = "/home/pi/Desktop/deploy_classifier/helpers/start.txt"
        f= open(stopFile, "w+")
        if os.path.isfile(startFile):
            os.remove(startFile)
            print("start file removed")
        print("stop file created !!")
        f.close() 

    def start(self, widget, event):    # Start box rather than image.
        stopFile = "/home/pi/Desktop/deploy_classifier/helpers/stop.txt"
        startFile = "/home/pi/Desktop/deploy_classifier/helpers/start.txt"
        f= open(startFile, "w+")     # Create the file start.txt
        if os.path.isfile(stopFile):
            os.remove(stopFile)
            print("stop file removed")
        print("start file created !!")
        a = 0
        while a==0:
            if os.path.isfile(stopFile):
                print("stopFile detected !!!!")
                a = 1
            else:                                      # There exists no stopFile.
                file = '/home/pi/Desktop/deploy_classifier/Final_result_copy.txt'
                if os.path.isfile(file):
                    # print ("File exists")
                    # readText = open(file).read()
                    # text = re.sub('\ |\"|\.|\!|\/|\;|\:', '', readText)
                    # print (text)
                    newText = ""
                    line2 = ""
                    line3 = ""
                    zzz = ""
                    lines = 0
                    with open(file) as fp:
                        # for i, l in enumerate(fp):
                            # pass
                            # lines = lines + 1
                        # print(lines)
                        line = fp.readline()
                        cnt = 1
                        while line :
                            line = fp.readline()
                            line2 = re.sub('\ |\"|\!|\/|\;|\:', '', line)
                            if cnt < 7:
                                # strs = "foo\tbar\t\tspam"
                                zzz = re.split(r'\t+', line2)
                                # print(zzz)
                                # print(zzz.pop(0))
                                line3 = zzz.pop(0) + " = " + zzz.pop(1)
                                # print(line3)
                                # print(cnt)
                                # print("Line {}: {}".format(cnt, line.strip()))
                                
                                newText = newText + line3
                            cnt += 1
                    batTime = "12:32"
                    text = batTime + "\n" + newText
                    # text = re.sub('\ |\"|\!|\/|\;|\:', '', newText)
                    
                else:
                    # print ("File not exist")
                    text = "Waiting for data ......"
                waittime=1
                num=rd.randint(1,60)
                text2 = ""
                for i in range(num):
                    text2 = text2 + "*"
                self.label1.set_text(text2)
                self.label2.set_text(text)
                while Gtk.events_pending():
                    Gtk.main_iteration()
                t.sleep(waittime)

    def updateTime(self):
        timeStr = self.getTime()
        print(timeStr)
        #self.set_text(timeStr)
        return GLib.SOURCE_CONTINUE

    def getTime(self):
        return time.strftime("%c")

    # callback function: the signal of the spinbutton is used to change the text of the label
    def spin_selected(self, event):
        self.label.set_text("Threshold value selected is: " + str(self.spinbutton_01.get_value_as_int()) + ".")


    def on_click_me_clicked(self, button):
        print("\"Click me\" button was clicked")
        file = "/home/pi/Desktop/deploy_classifier/alert_sounds/Go_for_Deploy.wav"
        os.system("aplay " + file)

    def on_open_clicked(self, button):
        print("\"Open\" button was clicked")
        file = "/home/pi/Desktop/deploy_classifier/bash_app"
        os.system("bash " + file)

    def on_close_clicked(self, button):
        print("Stopping application")
        os.system(exit)
        #os.system(return [n])
        
    #def on_close_clicked(self, button):
        #print("Closing application")
        #Gtk.main_quit()

    def on_numeric_toggled(self, button):
        self.spinbutton_01.set_numeric(button.get_active())
        print("Numeric")

    def on_ifvalid_toggled(self, button):
        if button.get_active():
            policy = Gtk.SpinButtonUpdatePolicy.IF_VALID
            print("Validated")
        else:
            policy = Gtk.SpinButtonUpdatePolicy.ALWAYS
        self.spinbutton_01.set_update_policy(policy)
        
    def on_spinbutton_01_value_changed(self, spinbutton):
        # print spinbutton_01.get_value_as_int()
        print("Nothing")
        
    def hello1(self, widget, event):
        print("clicked label 1")
        
    def test(self):
        Gtk.Window.__init__(self, title="RadioButton Demo")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button1 = Gtk.RadioButton.new_with_label_from_widget(None, "Button 1")
        button1.connect("toggled", self.on_button_toggled, "1")
        hbox.pack_start(button1, False, False, 0)

        button2 = Gtk.RadioButton.new_from_widget(button1)
        button2.set_label("Button 2")
        button2.connect("toggled", self.on_button_toggled, "2")
        hbox.pack_start(button2, False, False, 0)

        button3 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1,
            "B_utton 3")
        button3.connect("toggled", self.on_button_toggled, "3")
        hbox.pack_start(button3, False, False, 0)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)
        
    def set_style_text(self, checkbutton):
        start, end = textbuffer.get_bounds()

        if checkbuttonColor.get_active():
            textbuffer.apply_tag(texttagColor, start, end)
        else:
            textbuffer.remove_tag(texttagColor, start, end)
            
    def set_wrap_mode(self, radiobutton, wrap_mode):
        textview.set_wrap_mode(wrap_mode)
        
def test88():
    print("test88")
    return 1

# test88()
    
win = ButtonWindow()
win.set_position(Gtk.WindowPosition.CENTER)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
