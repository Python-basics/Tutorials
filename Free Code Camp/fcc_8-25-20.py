Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> help(open)
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.

>>> 
=========== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ==========
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 910, in <module>
    f = open('test_1.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'test_1.txt'
>>> 
=========== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ==========
>>> dir(f)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
>>> help(f)
Help on TextIOWrapper object:

class TextIOWrapper(_TextIOBase)
 |  TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)
 |  
 |  Character and line based layer over a BufferedIOBase object, buffer.
 |  
 |  encoding gives the name of the encoding that the stream will be
 |  decoded or encoded with. It defaults to locale.getpreferredencoding(False).
 |  
 |  errors determines the strictness of encoding and decoding (see
 |  help(codecs.Codec) or the documentation for codecs.register) and
 |  defaults to "strict".
 |  
 |  newline controls how line endings are handled. It can be None, '',
 |  '\n', '\r', and '\r\n'.  It works as follows:
 |  
 |  * On input, if newline is None, universal newlines mode is
 |    enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
 |    these are translated into '\n' before being returned to the
 |    caller. If it is '', universal newline mode is enabled, but line
 |    endings are returned to the caller untranslated. If it has any of
 |    the other legal values, input lines are only terminated by the given
 |    string, and the line ending is returned to the caller untranslated.
 |  
 |  * On output, if newline is None, any '\n' characters written are
 |    translated to the system default line separator, os.linesep. If
 |    newline is '' or '\n', no translation takes place. If newline is any
 |    of the other legal values, any '\n' characters written are translated
 |    to the given string.
 |  
 |  If line_buffering is True, a call to flush is implied when a call to
 |  write contains a newline character.
 |  
 |  Method resolution order:
 |      TextIOWrapper
 |      _TextIOBase
 |      _IOBase
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  close(self, /)
 |      Flush and close the IO object.
 |      
 |      This method has no effect if the file is already closed.
 |  
 |  detach(self, /)
 |      Separate the underlying buffer from the TextIOBase and return it.
 |      
 |      After the underlying buffer has been detached, the TextIO is in an
 |      unusable state.
 |  
 |  fileno(self, /)
 |      Returns underlying file descriptor if one exists.
 |      
 |      OSError is raised if the IO object does not use a file descriptor.
 |  
 |  flush(self, /)
 |      Flush write buffers, if applicable.
 |      
 |      This is not implemented for read-only and non-blocking streams.
 |  
 |  isatty(self, /)
 |      Return whether this is an 'interactive' stream.
 |      
 |      Return False if it can't be determined.
 |  
 |  read(self, size=-1, /)
 |      Read at most n characters from stream.
 |      
 |      Read from underlying buffer until we have n characters or we hit EOF.
 |      If n is negative or omitted, read until EOF.
 |  
 |  readable(self, /)
 |      Return whether object was opened for reading.
 |      
 |      If False, read() will raise OSError.
 |  
 |  readline(self, size=-1, /)
 |      Read until newline or EOF.
 |      
 |      Returns an empty string if EOF is hit immediately.
 |  
 |  reconfigure(self, /, *, encoding=None, errors=None, newline=None, line_buffering=None, write_through=None)
 |      Reconfigure the text stream with new parameters.
 |      
 |      This also does an implicit stream flush.
 |  
 |  seek(self, cookie, whence=0, /)
 |      Change stream position.
 |      
 |      Change the stream position to the given byte offset. The offset is
 |      interpreted relative to the position indicated by whence.  Values
 |      for whence are:
 |      
 |      * 0 -- start of stream (the default); offset should be zero or positive
 |      * 1 -- current stream position; offset may be negative
 |      * 2 -- end of stream; offset is usually negative
 |      
 |      Return the new absolute position.
 |  
 |  seekable(self, /)
 |      Return whether object supports random access.
 |      
 |      If False, seek(), tell() and truncate() will raise OSError.
 |      This method may need to do a test seek().
 |  
 |  tell(self, /)
 |      Return current stream position.
 |  
 |  truncate(self, pos=None, /)
 |      Truncate file to size bytes.
 |      
 |      File pointer is left unchanged.  Size defaults to the current IO
 |      position as reported by tell().  Returns the new size.
 |  
 |  writable(self, /)
 |      Return whether object was opened for writing.
 |      
 |      If False, write() will raise OSError.
 |  
 |  write(self, text, /)
 |      Write string to stream.
 |      Returns the number of characters written (which is always equal to
 |      the length of the string).
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  buffer
 |  
 |  closed
 |  
 |  encoding
 |      Encoding of the text stream.
 |      
 |      Subclasses should override.
 |  
 |  errors
 |      The error setting of the decoder or encoder.
 |      
 |      Subclasses should override.
 |  
 |  line_buffering
 |  
 |  name
 |  
 |  newlines
 |      Line endings translated so far.
 |      
 |      Only line endings translated during reading are considered.
 |      
 |      Subclasses should override.
 |  
 |  write_through
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from _IOBase:
 |  
 |  __del__(...)
 |  
 |  __enter__(...)
 |  
 |  __exit__(...)
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  readlines(self, hint=-1, /)
 |      Return a list of lines from the stream.
 |      
 |      hint can be specified to control the number of lines read: no more
 |      lines will be read if the total size (in bytes/characters) of all
 |      lines so far exceeds hint.
 |  
 |  writelines(self, lines, /)
 |      Write a list of lines to stream.
 |      
 |      Line separators are not added, so it is usual for each of the
 |      lines provided to have a line separator at the end.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from _IOBase:
 |  
 |  __dict__

>>> f.closed
False
>>> f.close()
>>> f.closed
True
>>> dir(f)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
>>> help(f.write)
Help on built-in function write:

write(text, /) method of _io.TextIOWrapper instance
    Write string to stream.
    Returns the number of characters written (which is always equal to
    the length of the string).

>>> 
=========== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ==========
>>> f.write('hello')
5
>>> f.close()
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
>>> f
<_io.TextIOWrapper name='test_1.txt' mode='r' encoding='cp1252'>
>>> dir(f)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
>>> f.read()
'hello'
>>> f.close()
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
Hi how are you?
>>> help(open)
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.

>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Hi how are you?
>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: bread
>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: milk
>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: bread
>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: milk
>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: eggs
>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: bread
>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: milk
>>> '\n'
'\n'
>>> new_line = '\n'
>>> print()

>>> print(new_line)


>>> print('\t')
	
>>> print('\t hello')
	 hello
>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: eggs
Enter item: butter
Enter item: 
======================================= RESTART: Shell ======================================
>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: jelly
Enter item: lettuce
Enter item: EXIT
>>> help(open)
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.

>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: LIST

Enter item: grapes
Enter item: EXIT
>>> file
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    file
NameError: name 'file' is not defined
>>> f = open('shopping_list.txt')
>>> dir(f)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
>>> help(f.seek)
Help on built-in function seek:

seek(cookie, whence=0, /) method of _io.TextIOWrapper instance
    Change stream position.
    
    Change the stream position to the given byte offset. The offset is
    interpreted relative to the position indicated by whence.  Values
    for whence are:
    
    * 0 -- start of stream (the default); offset should be zero or positive
    * 1 -- current stream position; offset may be negative
    * 2 -- end of stream; offset is usually negative
    
    Return the new absolute position.

>>> help(f.tell)
Help on built-in function tell:

tell() method of _io.TextIOWrapper instance
    Return current stream position.

>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
51
Enter item: peanut butter
66
Enter item: potatos
75
Enter item: EXIT
>>> f = open('shopping_list.txt')
>>> f
<_io.TextIOWrapper name='shopping_list.txt' mode='r' encoding='cp1252'>
>>> f.tell()
0
>>> f.read()
'bread\nmilk\neggs\nbutter\njelly\nlettuce\ngrapes\npeanut butter\npotatos\n'
>>> print(f.read())

>>> f.tell()
75
>>> f.seek(0)
0
>>> print(f.read())
bread
milk
eggs
butter
jelly
lettuce
grapes
peanut butter
potatos

>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
75
Enter item: LIST
bread
milk
eggs
butter
jelly
lettuce
grapes
peanut butter
potatos

75
Enter item: EXIT
>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: LIST
bread
milk
eggs
butter
jelly
lettuce
grapes
peanut butter
potatos

Enter item: chicken
Enter item: EXIT
>>> 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: LIST
bread
milk
eggs
butter
jelly
lettuce
grapes
peanut butter
potatos
chicken

Enter item: 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: LIST
bread
milk
eggs
butter
jelly
lettuce
grapes
peanut butter
potatos
chicken
LIST

Enter item: 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
Enter item: 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
Enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
Enter number to delete or 0 to continue: 0
Enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
Enter number to delete or 0 to continue: 1
Enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
Enter number to delete or 0 to continue: 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
type anytime
Exit: to quit
List: To Read and Delete

Enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
Enter number to delete or 0 to continue: 
========= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python36-32\ideas.py ========
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) ham
  2) shrimp
  3) bread
  4) milk
  5) cereal
  6) soap
enter number to delete or 0 to continue: 
==== RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py ====
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
enter number to delete or 0 to continue: 
Traceback (most recent call last):
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 961, in <module>
    my_list()
  File "C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py", line 949, in my_list
    remove = int(input('enter number to delete or 0 to continue: '))
ValueError: invalid literal for int() with base 10: ''
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
enter number to delete or 0 to continue: 
If you don't want to delete please enter 0
enter number to delete or 0 to continue: 0
enter number to delete or 0 to continue: 0
enter number to delete or 0 to continue: 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: EXIT
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: EXIT
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python36-32\ideas.py
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) ham
  2) shrimp
  3) bread
  4) milk
  5) cereal
  6) soap
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) ham
  2) shrimp
  3) bread
  4) milk
  5) cereal
  6) soap
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: help
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LIST
 13) help
enter number to delete or 0 to continue: 12
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LSIT
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) help
 13) LSIT
enter number to delete or 0 to continue: 12
enter number to delete or 0 to continue: 12
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LSIT
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
 12) LSIT
enter number to delete or 0 to continue: 12
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
enter number to delete or 0 to continue: EXIT
If you don't want to delete please enter 0
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: EXIT
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python36-32\ideas.py
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) ham
  2) shrimp
  3) bread
  4) milk
  5) cereal
  6) soap
enter number to delete or 0 to continue: 6
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) ham
  2) shrimp
  3) bread
  4) milk
  5) cereal
  6) 0
  7) 0
enter number to delete or 0 to continue: 6
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: 6
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) ham
  2) shrimp
  3) bread
  4) milk
  5) cereal
  6) 0
  7) 6
enter number to delete or 0 to continue: 6
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) ham
  2) shrimp
  3) bread
  4) milk
  5) cereal
  6) 6
enter number to delete or 0 to continue: 6
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) ham
  2) shrimp
  3) bread
  4) milk
  5) cereal
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) ham
  2) shrimp
  3) bread
  4) milk
  5) cereal
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: EXIT
>>> 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python38-32\Free Code Camp.py
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) bread
  2) milk
  3) eggs
  4) butter
  5) jelly
  6) lettuce
  7) grapes
  8) peanut
  9) butter
 10) potatos
 11) chicken
enter number to delete or 0 to continue: 
= RESTART: C:\Users\samue\AppData\Local\Programs\Python\Python36-32\ideas.py
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: LIST
  1) ham
  2) shrimp
  3) bread
  4) milk
  5) cereal
enter number to delete or 0 to continue: 0
type anytime
EXIT: to quit
LIST: To Read and Delete

enter item: EXIT
>>> 
