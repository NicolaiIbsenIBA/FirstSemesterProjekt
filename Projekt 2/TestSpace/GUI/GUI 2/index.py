import customtkinter as c
import my_queries as mq
import my_names as mn
import structure
import home as h
import login as l
import classes as cl

master = c.CTk(fg_color=mn.primary_grey)
master.title("NextText CALC")
master.geometry("800x800")
master.iconbitmap("Assets/IBA_icon_ico.ico")
master._set_appearance_mode("system")
# Header
structure.header_frame(master)

### Body start
scrollable_frame = c.CTkScrollableFrame(master,
                                        bg_color=mn.primary_grey,
                                        fg_color=mn.primary_grey,)
### Body start

l.login_content(scrollable_frame, mn.my_list)


### Body end
scrollable_frame.pack(expand=True, fill="both") 
### Body end

# Footer
structure.footer_frame(master)

master.mainloop()