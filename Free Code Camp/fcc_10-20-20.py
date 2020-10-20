Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> dir(tk)
['ACTIVE', 'ALL', 'ANCHOR', 'ARC', 'BASELINE', 'BEVEL', 'BOTH', 'BOTTOM', 'BROWSE', 'BUTT', 'BaseWidget', 'BitmapImage', 'BooleanVar', 'Button', 'CASCADE', 'CENTER', 'CHAR', 'CHECKBUTTON', 'CHORD', 'COMMAND', 'CURRENT', 'CallWrapper', 'Canvas', 'Checkbutton', 'DISABLED', 'DOTBOX', 'DoubleVar', 'E', 'END', 'EW', 'EXCEPTION', 'EXTENDED', 'Entry', 'Event', 'EventType', 'FALSE', 'FIRST', 'FLAT', 'Frame', 'GROOVE', 'Grid', 'HIDDEN', 'HORIZONTAL', 'INSERT', 'INSIDE', 'Image', 'IntVar', 'LAST', 'LEFT', 'Label', 'LabelFrame', 'Listbox', 'MITER', 'MOVETO', 'MULTIPLE', 'Menu', 'Menubutton', 'Message', 'Misc', 'N', 'NE', 'NO', 'NONE', 'NORMAL', 'NS', 'NSEW', 'NUMERIC', 'NW', 'NoDefaultRoot', 'OFF', 'ON', 'OUTSIDE', 'OptionMenu', 'PAGES', 'PIESLICE', 'PROJECTING', 'Pack', 'PanedWindow', 'PhotoImage', 'Place', 'RADIOBUTTON', 'RAISED', 'READABLE', 'RIDGE', 'RIGHT', 'ROUND', 'Radiobutton', 'S', 'SCROLL', 'SE', 'SEL', 'SEL_FIRST', 'SEL_LAST', 'SEPARATOR', 'SINGLE', 'SOLID', 'SUNKEN', 'SW', 'Scale', 'Scrollbar', 'Spinbox', 'StringVar', 'TOP', 'TRUE', 'Tcl', 'TclError', 'TclVersion', 'Text', 'Tk', 'TkVersion', 'Toplevel', 'UNDERLINE', 'UNITS', 'VERTICAL', 'Variable', 'W', 'WORD', 'WRITABLE', 'Widget', 'Wm', 'X', 'XView', 'Y', 'YES', 'YView', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_cnfmerge', '_default_root', '_exit', '_flatten', '_join', '_magic_re', '_setit', '_space_re', '_splitdict', '_stringify', '_support_default_root', '_test', '_tkerror', '_tkinter', '_varnum', 'constants', 'enum', 'getboolean', 'getdouble', 'getint', 'image_names', 'image_types', 'mainloop', 're', 'sys', 'wantobjects']
>>> help(tk.TK)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    help(tk.TK)
AttributeError: module 'tkinter' has no attribute 'TK'
>>> help(tk.Tk)
Help on class Tk in module tkinter:

class Tk(Misc, Wm)
 |  Tk(screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None)
 |  
 |  Toplevel widget of Tk which represents mostly the main window
 |  of an application. It has an associated Tcl interpreter.
 |  
 |  Method resolution order:
 |      Tk
 |      Misc
 |      Wm
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __getattr__(self, attr)
 |      Delegate attribute access to the interpreter object
 |  
 |  __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None)
 |      Return a new Toplevel widget on screen SCREENNAME. A new Tcl interpreter will
 |      be created. BASENAME will be used for the identification of the profile file (see
 |      readprofile).
 |      It is constructed from sys.argv[0] without extensions if None is given. CLASSNAME
 |      is the name of the widget class.
 |  
 |  destroy(self)
 |      Destroy this and all descendants widgets. This will
 |      end the application of this Tcl interpreter.
 |  
 |  loadtk(self)
 |  
 |  readprofile(self, baseName, className)
 |      Internal function. It reads BASENAME.tcl and CLASSNAME.tcl into
 |      the Tcl Interpreter and calls exec on the contents of BASENAME.py and
 |      CLASSNAME.py if such a file exists in the home directory.
 |  
 |  report_callback_exception(self, exc, val, tb)
 |      Report callback exception on sys.stderr.
 |      
 |      Applications may want to override this internal function, and
 |      should when sys.stderr is None.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Misc:
 |  
 |  __getitem__ = cget(self, key)
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value)
 |  
 |  __str__(self)
 |      Return the window path name of this widget.
 |  
 |  after(self, ms, func=None, *args)
 |      Call function once after given time.
 |      
 |      MS specifies the time in milliseconds. FUNC gives the
 |      function which shall be called. Additional parameters
 |      are given as parameters to the function call.  Return
 |      identifier to cancel scheduling with after_cancel.
 |  
 |  after_cancel(self, id)
 |      Cancel scheduling of function identified with ID.
 |      
 |      Identifier returned by after or after_idle must be
 |      given as first parameter.
 |  
 |  after_idle(self, func, *args)
 |      Call FUNC once if the Tcl main loop has no event to
 |      process.
 |      
 |      Return an identifier to cancel the scheduling with
 |      after_cancel.
 |  
 |  anchor = grid_anchor(self, anchor=None)
 |  
 |  bbox = grid_bbox(self, column=None, row=None, col2=None, row2=None)
 |  
 |  bell(self, displayof=0)
 |      Ring a display's bell.
 |  
 |  bind(self, sequence=None, func=None, add=None)
 |      Bind to this widget at event SEQUENCE a call to function FUNC.
 |      
 |      SEQUENCE is a string of concatenated event
 |      patterns. An event pattern is of the form
 |      <MODIFIER-MODIFIER-TYPE-DETAIL> where MODIFIER is one
 |      of Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4,
 |      Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3,
 |      B3, Alt, Button4, B4, Double, Button5, B5 Triple,
 |      Mod1, M1. TYPE is one of Activate, Enter, Map,
 |      ButtonPress, Button, Expose, Motion, ButtonRelease
 |      FocusIn, MouseWheel, Circulate, FocusOut, Property,
 |      Colormap, Gravity Reparent, Configure, KeyPress, Key,
 |      Unmap, Deactivate, KeyRelease Visibility, Destroy,
 |      Leave and DETAIL is the button number for ButtonPress,
 |      ButtonRelease and DETAIL is the Keysym for KeyPress and
 |      KeyRelease. Examples are
 |      <Control-Button-1> for pressing Control and mouse button 1 or
 |      <Alt-A> for pressing A and the Alt key (KeyPress can be omitted).
 |      An event pattern can also be a virtual event of the form
 |      <<AString>> where AString can be arbitrary. This
 |      event can be generated by event_generate.
 |      If events are concatenated they must appear shortly
 |      after each other.
 |      
 |      FUNC will be called if the event sequence occurs with an
 |      instance of Event as argument. If the return value of FUNC is
 |      "break" no further bound function is invoked.
 |      
 |      An additional boolean parameter ADD specifies whether FUNC will
 |      be called additionally to the other bound function or whether
 |      it will replace the previous function.
 |      
 |      Bind will return an identifier to allow deletion of the bound function with
 |      unbind without memory leak.
 |      
 |      If FUNC or SEQUENCE is omitted the bound function or list
 |      of bound events are returned.
 |  
 |  bind_all(self, sequence=None, func=None, add=None)
 |      Bind to all widgets at an event SEQUENCE a call to function FUNC.
 |      An additional boolean parameter ADD specifies whether FUNC will
 |      be called additionally to the other bound function or whether
 |      it will replace the previous function. See bind for the return value.
 |  
 |  bind_class(self, className, sequence=None, func=None, add=None)
 |      Bind to widgets with bindtag CLASSNAME at event
 |      SEQUENCE a call of function FUNC. An additional
 |      boolean parameter ADD specifies whether FUNC will be
 |      called additionally to the other bound function or
 |      whether it will replace the previous function. See bind for
 |      the return value.
 |  
 |  bindtags(self, tagList=None)
 |      Set or get the list of bindtags for this widget.
 |      
 |      With no argument return the list of all bindtags associated with
 |      this widget. With a list of strings as argument the bindtags are
 |      set to this list. The bindtags determine in which order events are
 |      processed (see bind).
 |  
 |  cget(self, key)
 |      Return the resource value for a KEY given as string.
 |  
 |  clipboard_append(self, string, **kw)
 |      Append STRING to the Tk clipboard.
 |      
 |      A widget specified at the optional displayof keyword
 |      argument specifies the target display. The clipboard
 |      can be retrieved with selection_get.
 |  
 |  clipboard_clear(self, **kw)
 |      Clear the data in the Tk clipboard.
 |      
 |      A widget specified for the optional displayof keyword
 |      argument specifies the target display.
 |  
 |  clipboard_get(self, **kw)
 |      Retrieve data from the clipboard on window's display.
 |      
 |      The window keyword defaults to the root window of the Tkinter
 |      application.
 |      
 |      The type keyword specifies the form in which the data is
 |      to be returned and should be an atom name such as STRING
 |      or FILE_NAME.  Type defaults to STRING, except on X11, where the default
 |      is to try UTF8_STRING and fall back to STRING.
 |      
 |      This command is equivalent to:
 |      
 |      selection_get(CLIPBOARD)
 |  
 |  columnconfigure = grid_columnconfigure(self, index, cnf={}, **kw)
 |  
 |  config = configure(self, cnf=None, **kw)
 |  
 |  configure(self, cnf=None, **kw)
 |      Configure resources of a widget.
 |      
 |      The values for resources are specified as keyword
 |      arguments. To get an overview about
 |      the allowed keyword arguments call the method keys.
 |  
 |  deletecommand(self, name)
 |      Internal function.
 |      
 |      Delete the Tcl command provided in NAME.
 |  
 |  event_add(self, virtual, *sequences)
 |      Bind a virtual event VIRTUAL (of the form <<Name>>)
 |      to an event SEQUENCE such that the virtual event is triggered
 |      whenever SEQUENCE occurs.
 |  
 |  event_delete(self, virtual, *sequences)
 |      Unbind a virtual event VIRTUAL from SEQUENCE.
 |  
 |  event_generate(self, sequence, **kw)
 |      Generate an event SEQUENCE. Additional
 |      keyword arguments specify parameter of the event
 |      (e.g. x, y, rootx, rooty).
 |  
 |  event_info(self, virtual=None)
 |      Return a list of all virtual events or the information
 |      about the SEQUENCE bound to the virtual event VIRTUAL.
 |  
 |  focus = focus_set(self)
 |  
 |  focus_displayof(self)
 |      Return the widget which has currently the focus on the
 |      display where this widget is located.
 |      
 |      Return None if the application does not have the focus.
 |  
 |  focus_force(self)
 |      Direct input focus to this widget even if the
 |      application does not have the focus. Use with
 |      caution!
 |  
 |  focus_get(self)
 |      Return the widget which has currently the focus in the
 |      application.
 |      
 |      Use focus_displayof to allow working with several
 |      displays. Return None if application does not have
 |      the focus.
 |  
 |  focus_lastfor(self)
 |      Return the widget which would have the focus if top level
 |      for this widget gets the focus from the window manager.
 |  
 |  focus_set(self)
 |      Direct input focus to this widget.
 |      
 |      If the application currently does not have the focus
 |      this widget will get the focus if the application gets
 |      the focus through the window manager.
 |  
 |  getboolean(self, s)
 |      Return a boolean value for Tcl boolean values true and false given as parameter.
 |  
 |  getdouble(self, s)
 |  
 |  getint(self, s)
 |  
 |  getvar(self, name='PY_VAR')
 |      Return value of Tcl variable NAME.
 |  
 |  grab_current(self)
 |      Return widget which has currently the grab in this application
 |      or None.
 |  
 |  grab_release(self)
 |      Release grab for this widget if currently set.
 |  
 |  grab_set(self)
 |      Set grab for this widget.
 |      
 |      A grab directs all events to this and descendant
 |      widgets in the application.
 |  
 |  grab_set_global(self)
 |      Set global grab for this widget.
 |      
 |      A global grab directs all events to this and
 |      descendant widgets on the display. Use with caution -
 |      other applications do not get events anymore.
 |  
 |  grab_status(self)
 |      Return None, "local" or "global" if this widget has
 |      no, a local or a global grab.
 |  
 |  grid_anchor(self, anchor=None)
 |      The anchor value controls how to place the grid within the
 |      master when no row/column has any weight.
 |      
 |      The default anchor is nw.
 |  
 |  grid_bbox(self, column=None, row=None, col2=None, row2=None)
 |      Return a tuple of integer coordinates for the bounding
 |      box of this widget controlled by the geometry manager grid.
 |      
 |      If COLUMN, ROW is given the bounding box applies from
 |      the cell with row and column 0 to the specified
 |      cell. If COL2 and ROW2 are given the bounding box
 |      starts at that cell.
 |      
 |      The returned integers specify the offset of the upper left
 |      corner in the master widget and the width and height.
 |  
 |  grid_columnconfigure(self, index, cnf={}, **kw)
 |      Configure column INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the column),
 |      weight (how much does additional space propagate to this column)
 |      and pad (how much space to let additionally).
 |  
 |  grid_location(self, x, y)
 |      Return a tuple of column and row which identify the cell
 |      at which the pixel at position X and Y inside the master
 |      widget is located.
 |  
 |  grid_propagate(self, flag=['_noarg_'])
 |      Set or get the status for propagation of geometry information.
 |      
 |      A boolean argument specifies whether the geometry information
 |      of the slaves will determine the size of this widget. If no argument
 |      is given, the current setting will be returned.
 |  
 |  grid_rowconfigure(self, index, cnf={}, **kw)
 |      Configure row INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the row),
 |      weight (how much does additional space propagate to this row)
 |      and pad (how much space to let additionally).
 |  
 |  grid_size(self)
 |      Return a tuple of the number of column and rows in the grid.
 |  
 |  grid_slaves(self, row=None, column=None)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  image_names(self)
 |      Return a list of all existing image names.
 |  
 |  image_types(self)
 |      Return a list of all available image types (e.g. photo bitmap).
 |  
 |  keys(self)
 |      Return a list of all resource names of this widget.
 |  
 |  lift = tkraise(self, aboveThis=None)
 |  
 |  lower(self, belowThis=None)
 |      Lower this widget in the stacking order.
 |  
 |  mainloop(self, n=0)
 |      Call the mainloop of Tk.
 |  
 |  nametowidget(self, name)
 |      Return the Tkinter instance of a widget identified by
 |      its Tcl name NAME.
 |  
 |  option_add(self, pattern, value, priority=None)
 |      Set a VALUE (second parameter) for an option
 |      PATTERN (first parameter).
 |      
 |      An optional third parameter gives the numeric priority
 |      (defaults to 80).
 |  
 |  option_clear(self)
 |      Clear the option database.
 |      
 |      It will be reloaded if option_add is called.
 |  
 |  option_get(self, name, className)
 |      Return the value for an option NAME for this widget
 |      with CLASSNAME.
 |      
 |      Values with higher priority override lower values.
 |  
 |  option_readfile(self, fileName, priority=None)
 |      Read file FILENAME into the option database.
 |      
 |      An optional second parameter gives the numeric
 |      priority.
 |  
 |  pack_propagate(self, flag=['_noarg_'])
 |      Set or get the status for propagation of geometry information.
 |      
 |      A boolean argument specifies whether the geometry information
 |      of the slaves will determine the size of this widget. If no argument
 |      is given the current setting will be returned.
 |  
 |  pack_slaves(self)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  place_slaves(self)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  propagate = pack_propagate(self, flag=['_noarg_'])
 |  
 |  quit(self)
 |      Quit the Tcl interpreter. All widgets will be destroyed.
 |  
 |  register = _register(self, func, subst=None, needcleanup=1)
 |  
 |  rowconfigure = grid_rowconfigure(self, index, cnf={}, **kw)
 |  
 |  selection_clear(self, **kw)
 |      Clear the current X selection.
 |  
 |  selection_get(self, **kw)
 |      Return the contents of the current X selection.
 |      
 |      A keyword parameter selection specifies the name of
 |      the selection and defaults to PRIMARY.  A keyword
 |      parameter displayof specifies a widget on the display
 |      to use. A keyword parameter type specifies the form of data to be
 |      fetched, defaulting to STRING except on X11, where UTF8_STRING is tried
 |      before STRING.
 |  
 |  selection_handle(self, command, **kw)
 |      Specify a function COMMAND to call if the X
 |      selection owned by this widget is queried by another
 |      application.
 |      
 |      This function must return the contents of the
 |      selection. The function will be called with the
 |      arguments OFFSET and LENGTH which allows the chunking
 |      of very long selections. The following keyword
 |      parameters can be provided:
 |      selection - name of the selection (default PRIMARY),
 |      type - type of the selection (e.g. STRING, FILE_NAME).
 |  
 |  selection_own(self, **kw)
 |      Become owner of X selection.
 |      
 |      A keyword parameter selection specifies the name of
 |      the selection (default PRIMARY).
 |  
 |  selection_own_get(self, **kw)
 |      Return owner of X selection.
 |      
 |      The following keyword parameter can
 |      be provided:
 |      selection - name of the selection (default PRIMARY),
 |      type - type of the selection (e.g. STRING, FILE_NAME).
 |  
 |  send(self, interp, cmd, *args)
 |      Send Tcl command CMD to different interpreter INTERP to be executed.
 |  
 |  setvar(self, name='PY_VAR', value='1')
 |      Set Tcl variable NAME to VALUE.
 |  
 |  size = grid_size(self)
 |  
 |  slaves = pack_slaves(self)
 |  
 |  tk_bisque(self)
 |      Change the color scheme to light brown as used in Tk 3.6 and before.
 |  
 |  tk_focusFollowsMouse(self)
 |      The widget under mouse will get automatically focus. Can not
 |      be disabled easily.
 |  
 |  tk_focusNext(self)
 |      Return the next widget in the focus order which follows
 |      widget which has currently the focus.
 |      
 |      The focus order first goes to the next child, then to
 |      the children of the child recursively and then to the
 |      next sibling which is higher in the stacking order.  A
 |      widget is omitted if it has the takefocus resource set
 |      to 0.
 |  
 |  tk_focusPrev(self)
 |      Return previous widget in the focus order. See tk_focusNext for details.
 |  
 |  tk_setPalette(self, *args, **kw)
 |      Set a new color scheme for all widget elements.
 |      
 |      A single color as argument will cause that all colors of Tk
 |      widget elements are derived from this.
 |      Alternatively several keyword parameters and its associated
 |      colors can be given. The following keywords are valid:
 |      activeBackground, foreground, selectColor,
 |      activeForeground, highlightBackground, selectBackground,
 |      background, highlightColor, selectForeground,
 |      disabledForeground, insertBackground, troughColor.
 |  
 |  tk_strictMotif(self, boolean=None)
 |      Set Tcl internal variable, whether the look and feel
 |      should adhere to Motif.
 |      
 |      A parameter of 1 means adhere to Motif (e.g. no color
 |      change if mouse passes over slider).
 |      Returns the set value.
 |  
 |  tkraise(self, aboveThis=None)
 |      Raise this widget in the stacking order.
 |  
 |  unbind(self, sequence, funcid=None)
 |      Unbind for this widget for event SEQUENCE  the
 |      function identified with FUNCID.
 |  
 |  unbind_all(self, sequence)
 |      Unbind for all widgets for event SEQUENCE all functions.
 |  
 |  unbind_class(self, className, sequence)
 |      Unbind for all widgets with bindtag CLASSNAME for event SEQUENCE
 |      all functions.
 |  
 |  update(self)
 |      Enter event loop until all pending events have been processed by Tcl.
 |  
 |  update_idletasks(self)
 |      Enter event loop until all idle callbacks have been called. This
 |      will update the display of windows but not process events caused by
 |      the user.
 |  
 |  wait_variable(self, name='PY_VAR')
 |      Wait until the variable is modified.
 |      
 |      A parameter of type IntVar, StringVar, DoubleVar or
 |      BooleanVar must be given.
 |  
 |  wait_visibility(self, window=None)
 |      Wait until the visibility of a WIDGET changes
 |      (e.g. it appears).
 |      
 |      If no parameter is given self is used.
 |  
 |  wait_window(self, window=None)
 |      Wait until a WIDGET is destroyed.
 |      
 |      If no parameter is given self is used.
 |  
 |  waitvar = wait_variable(self, name='PY_VAR')
 |  
 |  winfo_atom(self, name, displayof=0)
 |      Return integer which represents atom NAME.
 |  
 |  winfo_atomname(self, id, displayof=0)
 |      Return name of atom with identifier ID.
 |  
 |  winfo_cells(self)
 |      Return number of cells in the colormap for this widget.
 |  
 |  winfo_children(self)
 |      Return a list of all widgets which are children of this widget.
 |  
 |  winfo_class(self)
 |      Return window class name of this widget.
 |  
 |  winfo_colormapfull(self)
 |      Return True if at the last color request the colormap was full.
 |  
 |  winfo_containing(self, rootX, rootY, displayof=0)
 |      Return the widget which is at the root coordinates ROOTX, ROOTY.
 |  
 |  winfo_depth(self)
 |      Return the number of bits per pixel.
 |  
 |  winfo_exists(self)
 |      Return true if this widget exists.
 |  
 |  winfo_fpixels(self, number)
 |      Return the number of pixels for the given distance NUMBER
 |      (e.g. "3c") as float.
 |  
 |  winfo_geometry(self)
 |      Return geometry string for this widget in the form "widthxheight+X+Y".
 |  
 |  winfo_height(self)
 |      Return height of this widget.
 |  
 |  winfo_id(self)
 |      Return identifier ID for this widget.
 |  
 |  winfo_interps(self, displayof=0)
 |      Return the name of all Tcl interpreters for this display.
 |  
 |  winfo_ismapped(self)
 |      Return true if this widget is mapped.
 |  
 |  winfo_manager(self)
 |      Return the window manager name for this widget.
 |  
 |  winfo_name(self)
 |      Return the name of this widget.
 |  
 |  winfo_parent(self)
 |      Return the name of the parent of this widget.
 |  
 |  winfo_pathname(self, id, displayof=0)
 |      Return the pathname of the widget given by ID.
 |  
 |  winfo_pixels(self, number)
 |      Rounded integer value of winfo_fpixels.
 |  
 |  winfo_pointerx(self)
 |      Return the x coordinate of the pointer on the root window.
 |  
 |  winfo_pointerxy(self)
 |      Return a tuple of x and y coordinates of the pointer on the root window.
 |  
 |  winfo_pointery(self)
 |      Return the y coordinate of the pointer on the root window.
 |  
 |  winfo_reqheight(self)
 |      Return requested height of this widget.
 |  
 |  winfo_reqwidth(self)
 |      Return requested width of this widget.
 |  
 |  winfo_rgb(self, color)
 |      Return tuple of decimal values for red, green, blue for
 |      COLOR in this widget.
 |  
 |  winfo_rootx(self)
 |      Return x coordinate of upper left corner of this widget on the
 |      root window.
 |  
 |  winfo_rooty(self)
 |      Return y coordinate of upper left corner of this widget on the
 |      root window.
 |  
 |  winfo_screen(self)
 |      Return the screen name of this widget.
 |  
 |  winfo_screencells(self)
 |      Return the number of the cells in the colormap of the screen
 |      of this widget.
 |  
 |  winfo_screendepth(self)
 |      Return the number of bits per pixel of the root window of the
 |      screen of this widget.
 |  
 |  winfo_screenheight(self)
 |      Return the number of pixels of the height of the screen of this widget
 |      in pixel.
 |  
 |  winfo_screenmmheight(self)
 |      Return the number of pixels of the height of the screen of
 |      this widget in mm.
 |  
 |  winfo_screenmmwidth(self)
 |      Return the number of pixels of the width of the screen of
 |      this widget in mm.
 |  
 |  winfo_screenvisual(self)
 |      Return one of the strings directcolor, grayscale, pseudocolor,
 |      staticcolor, staticgray, or truecolor for the default
 |      colormodel of this screen.
 |  
 |  winfo_screenwidth(self)
 |      Return the number of pixels of the width of the screen of
 |      this widget in pixel.
 |  
 |  winfo_server(self)
 |      Return information of the X-Server of the screen of this widget in
 |      the form "XmajorRminor vendor vendorVersion".
 |  
 |  winfo_toplevel(self)
 |      Return the toplevel widget of this widget.
 |  
 |  winfo_viewable(self)
 |      Return true if the widget and all its higher ancestors are mapped.
 |  
 |  winfo_visual(self)
 |      Return one of the strings directcolor, grayscale, pseudocolor,
 |      staticcolor, staticgray, or truecolor for the
 |      colormodel of this widget.
 |  
 |  winfo_visualid(self)
 |      Return the X identifier for the visual for this widget.
 |  
 |  winfo_visualsavailable(self, includeids=False)
 |      Return a list of all visuals available for the screen
 |      of this widget.
 |      
 |      Each item in the list consists of a visual name (see winfo_visual), a
 |      depth and if includeids is true is given also the X identifier.
 |  
 |  winfo_vrootheight(self)
 |      Return the height of the virtual root window associated with this
 |      widget in pixels. If there is no virtual root window return the
 |      height of the screen.
 |  
 |  winfo_vrootwidth(self)
 |      Return the width of the virtual root window associated with this
 |      widget in pixel. If there is no virtual root window return the
 |      width of the screen.
 |  
 |  winfo_vrootx(self)
 |      Return the x offset of the virtual root relative to the root
 |      window of the screen of this widget.
 |  
 |  winfo_vrooty(self)
 |      Return the y offset of the virtual root relative to the root
 |      window of the screen of this widget.
 |  
 |  winfo_width(self)
 |      Return the width of this widget.
 |  
 |  winfo_x(self)
 |      Return the x coordinate of the upper left corner of this widget
 |      in the parent.
 |  
 |  winfo_y(self)
 |      Return the y coordinate of the upper left corner of this widget
 |      in the parent.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Misc:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Wm:
 |  
 |  aspect = wm_aspect(self, minNumer=None, minDenom=None, maxNumer=None, maxDenom=None)
 |  
 |  attributes = wm_attributes(self, *args)
 |  
 |  client = wm_client(self, name=None)
 |  
 |  colormapwindows = wm_colormapwindows(self, *wlist)
 |  
 |  command = wm_command(self, value=None)
 |  
 |  deiconify = wm_deiconify(self)
 |  
 |  focusmodel = wm_focusmodel(self, model=None)
 |  
 |  forget = wm_forget(self, window)
 |  
 |  frame = wm_frame(self)
 |  
 |  geometry = wm_geometry(self, newGeometry=None)
 |  
 |  grid = wm_grid(self, baseWidth=None, baseHeight=None, widthInc=None, heightInc=None)
 |  
 |  group = wm_group(self, pathName=None)
 |  
 |  iconbitmap = wm_iconbitmap(self, bitmap=None, default=None)
 |  
 |  iconify = wm_iconify(self)
 |  
 |  iconmask = wm_iconmask(self, bitmap=None)
 |  
 |  iconname = wm_iconname(self, newName=None)
 |  
 |  iconphoto = wm_iconphoto(self, default=False, *args)
 |  
 |  iconposition = wm_iconposition(self, x=None, y=None)
 |  
 |  iconwindow = wm_iconwindow(self, pathName=None)
 |  
 |  manage = wm_manage(self, widget)
 |  
 |  maxsize = wm_maxsize(self, width=None, height=None)
 |  
 |  minsize = wm_minsize(self, width=None, height=None)
 |  
 |  overrideredirect = wm_overrideredirect(self, boolean=None)
 |  
 |  positionfrom = wm_positionfrom(self, who=None)
 |  
 |  protocol = wm_protocol(self, name=None, func=None)
 |  
 |  resizable = wm_resizable(self, width=None, height=None)
 |  
 |  sizefrom = wm_sizefrom(self, who=None)
 |  
 |  state = wm_state(self, newstate=None)
 |  
 |  title = wm_title(self, string=None)
 |  
 |  transient = wm_transient(self, master=None)
 |  
 |  withdraw = wm_withdraw(self)
 |  
 |  wm_aspect(self, minNumer=None, minDenom=None, maxNumer=None, maxDenom=None)
 |      Instruct the window manager to set the aspect ratio (width/height)
 |      of this widget to be between MINNUMER/MINDENOM and MAXNUMER/MAXDENOM. Return a tuple
 |      of the actual values if no argument is given.
 |  
 |  wm_attributes(self, *args)
 |      This subcommand returns or sets platform specific attributes
 |      
 |      The first form returns a list of the platform specific flags and
 |      their values. The second form returns the value for the specific
 |      option. The third form sets one or more of the values. The values
 |      are as follows:
 |      
 |      On Windows, -disabled gets or sets whether the window is in a
 |      disabled state. -toolwindow gets or sets the style of the window
 |      to toolwindow (as defined in the MSDN). -topmost gets or sets
 |      whether this is a topmost window (displays above all other
 |      windows).
 |      
 |      On Macintosh, XXXXX
 |      
 |      On Unix, there are currently no special attribute values.
 |  
 |  wm_client(self, name=None)
 |      Store NAME in WM_CLIENT_MACHINE property of this widget. Return
 |      current value.
 |  
 |  wm_colormapwindows(self, *wlist)
 |      Store list of window names (WLIST) into WM_COLORMAPWINDOWS property
 |      of this widget. This list contains windows whose colormaps differ from their
 |      parents. Return current list of widgets if WLIST is empty.
 |  
 |  wm_command(self, value=None)
 |      Store VALUE in WM_COMMAND property. It is the command
 |      which shall be used to invoke the application. Return current
 |      command if VALUE is None.
 |  
 |  wm_deiconify(self)
 |      Deiconify this widget. If it was never mapped it will not be mapped.
 |      On Windows it will raise this widget and give it the focus.
 |  
 |  wm_focusmodel(self, model=None)
 |      Set focus model to MODEL. "active" means that this widget will claim
 |      the focus itself, "passive" means that the window manager shall give
 |      the focus. Return current focus model if MODEL is None.
 |  
 |  wm_forget(self, window)
 |      The window will be unmapped from the screen and will no longer
 |      be managed by wm. toplevel windows will be treated like frame
 |      windows once they are no longer managed by wm, however, the menu
 |      option configuration will be remembered and the menus will return
 |      once the widget is managed again.
 |  
 |  wm_frame(self)
 |      Return identifier for decorative frame of this widget if present.
 |  
 |  wm_geometry(self, newGeometry=None)
 |      Set geometry to NEWGEOMETRY of the form =widthxheight+x+y. Return
 |      current value if None is given.
 |  
 |  wm_grid(self, baseWidth=None, baseHeight=None, widthInc=None, heightInc=None)
 |      Instruct the window manager that this widget shall only be
 |      resized on grid boundaries. WIDTHINC and HEIGHTINC are the width and
 |      height of a grid unit in pixels. BASEWIDTH and BASEHEIGHT are the
 |      number of grid units requested in Tk_GeometryRequest.
 |  
 |  wm_group(self, pathName=None)
 |      Set the group leader widgets for related widgets to PATHNAME. Return
 |      the group leader of this widget if None is given.
 |  
 |  wm_iconbitmap(self, bitmap=None, default=None)
 |      Set bitmap for the iconified widget to BITMAP. Return
 |      the bitmap if None is given.
 |      
 |      Under Windows, the DEFAULT parameter can be used to set the icon
 |      for the widget and any descendents that don't have an icon set
 |      explicitly.  DEFAULT can be the relative path to a .ico file
 |      (example: root.iconbitmap(default='myicon.ico') ).  See Tk
 |      documentation for more information.
 |  
 |  wm_iconify(self)
 |      Display widget as icon.
 |  
 |  wm_iconmask(self, bitmap=None)
 |      Set mask for the icon bitmap of this widget. Return the
 |      mask if None is given.
 |  
 |  wm_iconname(self, newName=None)
 |      Set the name of the icon for this widget. Return the name if
 |      None is given.
 |  
 |  wm_iconphoto(self, default=False, *args)
 |      Sets the titlebar icon for this window based on the named photo
 |      images passed through args. If default is True, this is applied to
 |      all future created toplevels as well.
 |      
 |      The data in the images is taken as a snapshot at the time of
 |      invocation. If the images are later changed, this is not reflected
 |      to the titlebar icons. Multiple images are accepted to allow
 |      different images sizes to be provided. The window manager may scale
 |      provided icons to an appropriate size.
 |      
 |      On Windows, the images are packed into a Windows icon structure.
 |      This will override an icon specified to wm_iconbitmap, and vice
 |      versa.
 |      
 |      On X, the images are arranged into the _NET_WM_ICON X property,
 |      which most modern window managers support. An icon specified by
 |      wm_iconbitmap may exist simultaneously.
 |      
 |      On Macintosh, this currently does nothing.
 |  
 |  wm_iconposition(self, x=None, y=None)
 |      Set the position of the icon of this widget to X and Y. Return
 |      a tuple of the current values of X and X if None is given.
 |  
 |  wm_iconwindow(self, pathName=None)
 |      Set widget PATHNAME to be displayed instead of icon. Return the current
 |      value if None is given.
 |  
 |  wm_manage(self, widget)
 |      The widget specified will become a stand alone top-level window.
 |      The window will be decorated with the window managers title bar,
 |      etc.
 |  
 |  wm_maxsize(self, width=None, height=None)
 |      Set max WIDTH and HEIGHT for this widget. If the window is gridded
 |      the values are given in grid units. Return the current values if None
 |      is given.
 |  
 |  wm_minsize(self, width=None, height=None)
 |      Set min WIDTH and HEIGHT for this widget. If the window is gridded
 |      the values are given in grid units. Return the current values if None
 |      is given.
 |  
 |  wm_overrideredirect(self, boolean=None)
 |      Instruct the window manager to ignore this widget
 |      if BOOLEAN is given with 1. Return the current value if None
 |      is given.
 |  
 |  wm_positionfrom(self, who=None)
 |      Instruct the window manager that the position of this widget shall
 |      be defined by the user if WHO is "user", and by its own policy if WHO is
 |      "program".
 |  
 |  wm_protocol(self, name=None, func=None)
 |      Bind function FUNC to command NAME for this widget.
 |      Return the function bound to NAME if None is given. NAME could be
 |      e.g. "WM_SAVE_YOURSELF" or "WM_DELETE_WINDOW".
 |  
 |  wm_resizable(self, width=None, height=None)
 |      Instruct the window manager whether this width can be resized
 |      in WIDTH or HEIGHT. Both values are boolean values.
 |  
 |  wm_sizefrom(self, who=None)
 |      Instruct the window manager that the size of this widget shall
 |      be defined by the user if WHO is "user", and by its own policy if WHO is
 |      "program".
 |  
 |  wm_state(self, newstate=None)
 |      Query or set the state of this widget as one of normal, icon,
 |      iconic (see wm_iconwindow), withdrawn, or zoomed (Windows only).
 |  
 |  wm_title(self, string=None)
 |      Set the title of this widget.
 |  
 |  wm_transient(self, master=None)
 |      Instruct the window manager that this widget is transient
 |      with regard to widget MASTER.
 |  
 |  wm_withdraw(self)
 |      Withdraw this widget from the screen such that it is unmapped
 |      and forgotten by the window manager. Re-draw it with wm_deiconify.

>>> 
================ RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ================
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> win
<tkinter.Tk object .>
>>> dir(win)
['_Misc__winfo_getint', '_Misc__winfo_parseitem', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bind', '_configure', '_displayof', '_getboolean', '_getconfigure', '_getconfigure1', '_getdoubles', '_getints', '_grid_configure', '_gridconvvalue', '_last_child_ids', '_loadtk', '_nametowidget', '_noarg_', '_options', '_register', '_report_exception', '_root', '_subst_format', '_subst_format_str', '_substitute', '_tclCommands', '_tkloaded', '_w', '_windowingsystem', 'after', 'after_cancel', 'after_idle', 'anchor', 'aspect', 'attributes', 'bbox', 'bell', 'bind', 'bind_all', 'bind_class', 'bindtags', 'cget', 'children', 'client', 'clipboard_append', 'clipboard_clear', 'clipboard_get', 'colormapwindows', 'columnconfigure', 'command', 'config', 'configure', 'deiconify', 'deletecommand', 'destroy', 'event_add', 'event_delete', 'event_generate', 'event_info', 'focus', 'focus_displayof', 'focus_force', 'focus_get', 'focus_lastfor', 'focus_set', 'focusmodel', 'forget', 'frame', 'geometry', 'getboolean', 'getdouble', 'getint', 'getvar', 'grab_current', 'grab_release', 'grab_set', 'grab_set_global', 'grab_status', 'grid', 'grid_anchor', 'grid_bbox', 'grid_columnconfigure', 'grid_location', 'grid_propagate', 'grid_rowconfigure', 'grid_size', 'grid_slaves', 'group', 'iconbitmap', 'iconify', 'iconmask', 'iconname', 'iconphoto', 'iconposition', 'iconwindow', 'image_names', 'image_types', 'keys', 'lift', 'loadtk', 'lower', 'mainloop', 'manage', 'master', 'maxsize', 'minsize', 'nametowidget', 'option_add', 'option_clear', 'option_get', 'option_readfile', 'overrideredirect', 'pack_propagate', 'pack_slaves', 'place_slaves', 'positionfrom', 'propagate', 'protocol', 'quit', 'readprofile', 'register', 'report_callback_exception', 'resizable', 'rowconfigure', 'selection_clear', 'selection_get', 'selection_handle', 'selection_own', 'selection_own_get', 'send', 'setvar', 'size', 'sizefrom', 'slaves', 'state', 'title', 'tk', 'tk_bisque', 'tk_focusFollowsMouse', 'tk_focusNext', 'tk_focusPrev', 'tk_setPalette', 'tk_strictMotif', 'tkraise', 'transient', 'unbind', 'unbind_all', 'unbind_class', 'update', 'update_idletasks', 'wait_variable', 'wait_visibility', 'wait_window', 'waitvar', 'winfo_atom', 'winfo_atomname', 'winfo_cells', 'winfo_children', 'winfo_class', 'winfo_colormapfull', 'winfo_containing', 'winfo_depth', 'winfo_exists', 'winfo_fpixels', 'winfo_geometry', 'winfo_height', 'winfo_id', 'winfo_interps', 'winfo_ismapped', 'winfo_manager', 'winfo_name', 'winfo_parent', 'winfo_pathname', 'winfo_pixels', 'winfo_pointerx', 'winfo_pointerxy', 'winfo_pointery', 'winfo_reqheight', 'winfo_reqwidth', 'winfo_rgb', 'winfo_rootx', 'winfo_rooty', 'winfo_screen', 'winfo_screencells', 'winfo_screendepth', 'winfo_screenheight', 'winfo_screenmmheight', 'winfo_screenmmwidth', 'winfo_screenvisual', 'winfo_screenwidth', 'winfo_server', 'winfo_toplevel', 'winfo_viewable', 'winfo_visual', 'winfo_visualid', 'winfo_visualsavailable', 'winfo_vrootheight', 'winfo_vrootwidth', 'winfo_vrootx', 'winfo_vrooty', 'winfo_width', 'winfo_x', 'winfo_y', 'withdraw', 'wm_aspect', 'wm_attributes', 'wm_client', 'wm_colormapwindows', 'wm_command', 'wm_deiconify', 'wm_focusmodel', 'wm_forget', 'wm_frame', 'wm_geometry', 'wm_grid', 'wm_group', 'wm_iconbitmap', 'wm_iconify', 'wm_iconmask', 'wm_iconname', 'wm_iconphoto', 'wm_iconposition', 'wm_iconwindow', 'wm_manage', 'wm_maxsize', 'wm_minsize', 'wm_overrideredirect', 'wm_positionfrom', 'wm_protocol', 'wm_resizable', 'wm_sizefrom', 'wm_state', 'wm_title', 'wm_transient', 'wm_withdraw']
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> help(win.mainloop)
Help on method mainloop in module tkinter:

mainloop(n=0) method of tkinter.Tk instance
    Call the mainloop of Tk.

>>> dir(win)
['_Misc__winfo_getint', '_Misc__winfo_parseitem', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bind', '_configure', '_displayof', '_getboolean', '_getconfigure', '_getconfigure1', '_getdoubles', '_getints', '_grid_configure', '_gridconvvalue', '_last_child_ids', '_loadtk', '_nametowidget', '_noarg_', '_options', '_register', '_report_exception', '_root', '_subst_format', '_subst_format_str', '_substitute', '_tclCommands', '_tkloaded', '_w', '_windowingsystem', 'after', 'after_cancel', 'after_idle', 'anchor', 'aspect', 'attributes', 'bbox', 'bell', 'bind', 'bind_all', 'bind_class', 'bindtags', 'cget', 'children', 'client', 'clipboard_append', 'clipboard_clear', 'clipboard_get', 'colormapwindows', 'columnconfigure', 'command', 'config', 'configure', 'deiconify', 'deletecommand', 'destroy', 'event_add', 'event_delete', 'event_generate', 'event_info', 'focus', 'focus_displayof', 'focus_force', 'focus_get', 'focus_lastfor', 'focus_set', 'focusmodel', 'forget', 'frame', 'geometry', 'getboolean', 'getdouble', 'getint', 'getvar', 'grab_current', 'grab_release', 'grab_set', 'grab_set_global', 'grab_status', 'grid', 'grid_anchor', 'grid_bbox', 'grid_columnconfigure', 'grid_location', 'grid_propagate', 'grid_rowconfigure', 'grid_size', 'grid_slaves', 'group', 'iconbitmap', 'iconify', 'iconmask', 'iconname', 'iconphoto', 'iconposition', 'iconwindow', 'image_names', 'image_types', 'keys', 'lift', 'loadtk', 'lower', 'mainloop', 'manage', 'master', 'maxsize', 'minsize', 'nametowidget', 'option_add', 'option_clear', 'option_get', 'option_readfile', 'overrideredirect', 'pack_propagate', 'pack_slaves', 'place_slaves', 'positionfrom', 'propagate', 'protocol', 'quit', 'readprofile', 'register', 'report_callback_exception', 'resizable', 'rowconfigure', 'selection_clear', 'selection_get', 'selection_handle', 'selection_own', 'selection_own_get', 'send', 'setvar', 'size', 'sizefrom', 'slaves', 'state', 'title', 'tk', 'tk_bisque', 'tk_focusFollowsMouse', 'tk_focusNext', 'tk_focusPrev', 'tk_setPalette', 'tk_strictMotif', 'tkraise', 'transient', 'unbind', 'unbind_all', 'unbind_class', 'update', 'update_idletasks', 'wait_variable', 'wait_visibility', 'wait_window', 'waitvar', 'winfo_atom', 'winfo_atomname', 'winfo_cells', 'winfo_children', 'winfo_class', 'winfo_colormapfull', 'winfo_containing', 'winfo_depth', 'winfo_exists', 'winfo_fpixels', 'winfo_geometry', 'winfo_height', 'winfo_id', 'winfo_interps', 'winfo_ismapped', 'winfo_manager', 'winfo_name', 'winfo_parent', 'winfo_pathname', 'winfo_pixels', 'winfo_pointerx', 'winfo_pointerxy', 'winfo_pointery', 'winfo_reqheight', 'winfo_reqwidth', 'winfo_rgb', 'winfo_rootx', 'winfo_rooty', 'winfo_screen', 'winfo_screencells', 'winfo_screendepth', 'winfo_screenheight', 'winfo_screenmmheight', 'winfo_screenmmwidth', 'winfo_screenvisual', 'winfo_screenwidth', 'winfo_server', 'winfo_toplevel', 'winfo_viewable', 'winfo_visual', 'winfo_visualid', 'winfo_visualsavailable', 'winfo_vrootheight', 'winfo_vrootwidth', 'winfo_vrootx', 'winfo_vrooty', 'winfo_width', 'winfo_x', 'winfo_y', 'withdraw', 'wm_aspect', 'wm_attributes', 'wm_client', 'wm_colormapwindows', 'wm_command', 'wm_deiconify', 'wm_focusmodel', 'wm_forget', 'wm_frame', 'wm_geometry', 'wm_grid', 'wm_group', 'wm_iconbitmap', 'wm_iconify', 'wm_iconmask', 'wm_iconname', 'wm_iconphoto', 'wm_iconposition', 'wm_iconwindow', 'wm_manage', 'wm_maxsize', 'wm_minsize', 'wm_overrideredirect', 'wm_positionfrom', 'wm_protocol', 'wm_resizable', 'wm_sizefrom', 'wm_state', 'wm_title', 'wm_transient', 'wm_withdraw']
>>> help(win.title)
Help on method wm_title in module tkinter:

wm_title(string=None) method of tkinter.Tk instance
    Set the title of this widget.

>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
Set the title of this widget.= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py

= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> help(win.configure)
Help on method configure in module tkinter:

configure(cnf=None, **kw) method of tkinter.Tk instance
    Configure resources of a widget.
    
    The values for resources are specified as keyword
    arguments. To get an overview about
    the allowed keyword arguments call the method keys.

>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 1236, in <module>
    win.configure(width=300,height=300,backgroud='red')
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\lib\tkinter\__init__.py", line 1637, in configure
    return self._configure('configure', cnf, kw)
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\lib\tkinter\__init__.py", line 1627, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-backgroud"
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 1240, in <module>
    label = ttk.label(win,text="Hello World")
AttributeError: module 'tkinter.ttk' has no attribute 'label'
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 1240, in <module>
    label = ttk.label(win,text="Hello World")
AttributeError: module 'tkinter.ttk' has no attribute 'label'
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 1240, in <module>
    label = tk.label(win,text="Hello World")
AttributeError: module 'tkinter' has no attribute 'label'
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\python_basics_2020.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\python_basics_2020.py

= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\python_basics_2020.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\python_basics_2020.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py

= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\python_basics_2020.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py

= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 1249, in <module>
    text = tk.StingVar()
AttributeError: module 'tkinter' has no attribute 'StingVar'
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 1279, in <lambda>
    button_6 = ttk.Button(win,text='6',command=lambda:press(6))
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 1255, in press
    text.set(expr)
NameError: name 'text' is not defined
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> help(eval)
Help on built-in function eval in module builtins:

eval(source, globals=None, locals=None, /)
    Evaluate the given source in the context of globals and locals.
    
    The source may be a string representing a Python expression
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.

>>> '6' * 1
'6'
>>> '6' * 6
'666666'
>>> '6' + '3'
'63'
>>> eval('6+3')
9
>>> ttl = eval('6+3')
>>> ttl
9
>>> type(ttl)
<class 'int'>
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> 