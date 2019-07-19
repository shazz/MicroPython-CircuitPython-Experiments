# GDB commands

## Program Manipulation

### Most useful

````
append -- Append target code/data to a local file
append binary -- Append target code/data to a raw binary file
append binary memory -- Append contents of memory to a raw binary file
append binary value -- Append the value of an expression to a raw binary file
append memory -- Append contents of memory to a raw binary file
append value -- Append the value of an expression to a raw binary file

init-if-undefined -- Initialize a convenience variable if necessary
call -- Call a function in the program

display -- Print value of expression EXP each time the program stops
undisplay -- Cancel some expressions to be displayed when program stops

whatis -- Print data type of expression EXP

explore -- Explore a value or a type valid in the current context
explore type -- Explore a type or the type of an expression
explore value -- Explore value of an expression valid in the current context

find -- Search memory for a sequence of bytes
mem -- Define attributes for memory region or reset memory region handling to
x -- Examine memory: x/FMT ADDRESS

agent-printf -- Agent-printf "printf format string"
print -- Print value of expression EXP
print-object -- Ask an Objective-C object to print itself
printf -- Formatted printing
output -- Like "print" but don't put in value history and don't print newline
ptype -- Print definition of type TYPE

disassemble -- Disassemble a specified section of memory
````

### Others

````
dump -- Dump target code/data to a local file
dump binary -- Write target code/data to a raw binary file
dump binary memory -- Write contents of memory to a raw binary file
dump binary value -- Write the value of an expression to a raw binary file
dump ihex -- Write target code/data to an intel hex file
dump ihex memory -- Write contents of memory to an ihex file
dump ihex value -- Write the value of an expression to an ihex file
dump memory -- Write contents of memory to a raw binary file
dump srec -- Write target code/data to an srec file
dump srec memory -- Write contents of memory to an srec file
dump srec value -- Write the value of an expression to an srec file
dump tekhex -- Write target code/data to a tekhex file
dump tekhex memory -- Write contents of memory to a tekhex file
dump tekhex value -- Write the value of an expression to a tekhex file
dump value -- Write the value of an expression to a raw binary file
dump verilog -- Write target code/data to a verilog hex file
dump verilog memory -- Write contents of memory to a verilog hex file
dump verilog value -- Write the value of an expression to a verilog hex file
restore -- Restore the contents of FILE to target memory

set -- Evaluate expression EXP and assign result to variable VAR
set ada -- Prefix command for changing Ada-specific settings
set ada print-signatures -- Enable or disable the output of formal and return types for functions in the overloads selection menu
set ada trust-PAD-over-XVS -- Enable or disable an optimization trusting PAD types over XVS types
set agent -- Set debugger's willingness to use agent as a helper
set annotate -- Set annotation_level
set architecture -- Set architecture of target
set args -- Set argument list to give program being debugged when it is started
set auto-connect-native-target -- Set whether GDB may automatically connect to the native target
set auto-load -- Auto-loading specific settings
set auto-load gdb-scripts -- Enable or disable auto-loading of canned sequences of commands scripts
set auto-load libthread-db -- Enable or disable auto-loading of inferior specific libthread_db
set auto-load local-gdbinit -- Enable or disable auto-loading of .gdbinit script in current directory
set auto-load python-scripts -- Set the debugger's behaviour regarding auto-loaded Python scripts
set auto-load safe-path -- Set the list of files and directories that are safe for auto-loading
set auto-load scripts-directory -- Set the list of directories from which to load auto-loaded scripts
set auto-solib-add -- Set autoloading of shared library symbols
set backtrace -- Set backtrace specific variables
set backtrace limit -- Set an upper bound on the number of backtrace levels
set backtrace past-entry -- Set whether backtraces should continue past the entry point of a program
set backtrace past-main -- Set whether backtraces should continue past "main"
set basenames-may-differ -- Set whether a source file may have multiple base names
set breakpoint -- Breakpoint specific settings
set breakpoint always-inserted -- Set mode for inserting breakpoints
set breakpoint auto-hw -- Set automatic usage of hardware breakpoints
set breakpoint condition-evaluation -- Set mode of breakpoint condition evaluation
set breakpoint pending -- Set debugger's behavior regarding pending breakpoints
set can-use-hw-watchpoints -- Set debugger's willingness to use watchpoint hardware
set case-sensitive -- Set case sensitivity in name search
set charset -- Set the host and target character sets
set check -- Set the status of the type/range checker
set check range -- Set range checking
set check type -- Set strict type checking
set circular-trace-buffer -- Set target's use of circular trace buffer
set code-cache -- Set cache use for code segment access
set coerce-float-to-double -- Set coercion of floats to doubles when calling functions
set compile-args -- Set compile command GCC command-line arguments
set compile-gcc -- Set compile command GCC driver filename
set complaints -- Set max number of complaints about incorrect symbols
set confirm -- Set whether to confirm potentially dangerous operations
set cp-abi -- Set the ABI used for inspecting C++ objects
set cwd -- Set the current working directory to be used when the inferior is started
set data-directory -- Set GDB's data directory
set dcache -- Use this command to set number of lines in dcache and line-size
set dcache line-size -- Set dcache line size in bytes (must be power of 2)
set dcache size -- Set number of dcache lines
set debug -- Generic command for setting gdb debugging flags
set debug arch -- Set architecture debugging
set debug auto-load -- Set auto-load verifications debugging
set debug bfd-cache -- Set bfd cache debugging
set debug check-physname -- Set cross-checking of "physname" code against demangler
set debug coff-pe-read -- Set coff PE read debugging
set debug compile -- Set compile command debugging
set debug compile-cplus-scopes -- Set debugging of C++ compile scopes
set debug compile-cplus-types -- Set debugging of C++ compile type conversion
set debug displaced -- Set displaced stepping debugging
set debug dwarf-die -- Set debugging of the DWARF DIE reader
set debug dwarf-line -- Set debugging of the dwarf line reader
set debug dwarf-read -- Set debugging of the DWARF reader
set debug entry-values -- Set entry values and tail call frames debugging
set debug expression -- Set expression debugging
set debug frame -- Set frame debugging
set debug index-cache -- Set display of index-cache debug messages
set debug infrun -- Set inferior debugging
set debug jit -- Set JIT debugging
set debug libthread-db -- Set libthread-db debugging
set debug lin-lwp -- Set debugging of GNU/Linux lwp module
set debug linux-namespaces -- Set debugging of GNU/Linux namespaces module
set debug notification -- Set debugging of async remote notification
set debug observer -- Set observer debugging
set debug overload -- Set debugging of C++ overloading
set debug parser -- Set parser debugging
set debug py-unwind -- Set Python unwinder debugging
set debug record -- Set debugging of record/replay feature
set debug remote -- Set debugging of remote protocol
set debug separate-debug-file -- Set printing of separate debug info file search debug
set debug serial -- Set serial debugging
set debug skip -- Set whether to print the debug output about skipping files and functions
set debug stap-expression -- Set SystemTap expression debugging
set debug symbol-lookup -- Set debugging of symbol lookup
set debug symfile -- Set debugging of the symfile functions
set debug symtab-create -- Set debugging of symbol table creation
set debug target -- Set target debugging
set debug timestamp -- Set timestamping of debugging messages
set debug varobj -- Set varobj debugging
set debug xml -- Set XML parser debugging
set debug-file-directory -- Set the directories where separate debug symbols are searched for
set default-collect -- Set the list of expressions to collect by default
set demangle-style -- Set the current C++ demangling style
set detach-on-fork -- Set whether gdb will detach the child of a fork
set directories -- Set the search path for finding source files
set disable-randomization -- Set disabling of debuggee's virtual address space randomization
set disassemble-next-line -- Set whether to disassemble next source line or insn when execution stops
set disassembler-options -- Set the disassembler options
set disassembly-flavor -- Set the disassembly flavor
set disconnected-dprintf -- Set whether dprintf continues after GDB disconnects
set disconnected-tracing -- Set whether tracing continues after GDB disconnects
set displaced-stepping -- Set debugger's willingness to use displaced stepping
set dprintf-channel -- Set the channel to use for dynamic printf
set dprintf-function -- Set the function to use for dynamic printf
set dprintf-style -- Set the style of usage for dynamic printf
set dump-excluded-mappings -- Set whether gcore should dump mappings marked with the VM_DONTDUMP flag
set editing -- Set editing of command lines as they are typed
set endian -- Set endianness of target
set environment -- Set environment variable value to give the program
set exec-direction -- Set direction of execution
set exec-done-display -- Set notification of completion for asynchronous execution commands
set exec-wrapper -- Set a wrapper for running programs
set extended-prompt -- Set the extended prompt
set extension-language -- Set mapping between filename extension and source language
set filename-display -- Set how to display filenames
set follow-exec-mode -- Set debugger response to a program call of exec
set follow-fork-mode -- Set debugger response to a program call of fork or vfork
set frame-filter -- Prefix command for 'set' frame-filter related operations
set frame-filter priority -- GDB command to set the priority of the specified frame-filter
set gnutarget -- Set the current BFD target
set guile -- Prefix command for Guile preference settings
set guile print-stack -- Set mode for Guile exception printing on error
set height -- Set number of lines in a page for GDB output pagination
set history -- Generic command for setting command history parameters
set history expansion -- Set history expansion on command input
set history filename -- Set the filename in which to record the command history
set history remove-duplicates -- Set how far back in history to look for and remove duplicate entries
set history save -- Set saving of the history record on exit
set history size -- Set the size of the command history
set host-charset -- Set the host character set
set index-cache -- Set index-cache options
set index-cache directory -- Set the directory of the index cache
set index-cache off -- Disable the index cache
set index-cache on -- Enable the index cache
set inferior-tty -- Set terminal for future runs of program being debugged
set input-radix -- Set default input radix for entering numbers
set interactive-mode -- Set whether GDB's standard input is a terminal
set language -- Set the current source language
set libthread-db-search-path -- Set search path for libthread_db
set listsize -- Set number of source lines gdb will list by default
set logging -- Set logging options
set logging file -- Set the current logfile
set logging off -- Disable logging
set logging on -- Enable logging
set logging overwrite -- Set whether logging overwrites or appends to the log file
set logging redirect -- Set the logging output mode
set max-completions -- Set maximum number of completion candidates
set max-user-call-depth -- Set the max call depth for non-python/scheme user-defined commands
set max-value-size -- Set maximum sized value gdb will load from the inferior
set may-insert-breakpoints -- Set permission to insert breakpoints in the target
set may-insert-fast-tracepoints -- Set permission to insert fast tracepoints in the target
set may-insert-tracepoints -- Set permission to insert tracepoints in the target
set may-interrupt -- Set permission to interrupt or signal the target
set may-write-memory -- Set permission to write into target memory
set may-write-registers -- Set permission to write into registers
set mem -- Memory regions settings
set mem inaccessible-by-default -- Set handling of unknown memory regions
set mi-async -- Set whether MI asynchronous mode is enabled
set mpx -- Set Intel Memory Protection Extensions specific variables
set mpx bound -- Set the memory bounds for a given array/pointer storage in the bound table
set multiple-symbols -- Set the debugger behavior when more than one symbol are possible matches
set non-stop -- Set whether gdb controls the inferior in non-stop mode
set observer -- Set whether gdb controls the inferior in observer mode
set opaque-type-resolution -- Set resolution of opaque struct/class/union types (if set before loading symbols)
set osabi -- Set OS ABI of target
set output-radix -- Set default output radix for printing of values
set overload-resolution -- Set overload resolution in evaluating C++ functions
set pagination -- Set state of GDB output pagination
set print -- Generic command for setting how things print
set print address -- Set printing of addresses
set print array -- Set pretty formatting of arrays
set print array-indexes -- Set printing of array indexes
set print asm-demangle -- Set demangling of C++/ObjC names in disassembly listings
set print demangle -- Set demangling of encoded C++/ObjC names when displaying symbols
set print elements -- Set limit on string chars or array elements to print
set print entry-values -- Set printing of function arguments at function entry
set print frame-arguments -- Set printing of non-scalar frame arguments
set print inferior-events -- Set printing of inferior events (e.g.
set print max-symbolic-offset -- Set the largest offset that will be printed in <symbol+1234> form
set print null-stop -- Set printing of char arrays to stop at first null char
set print object -- Set printing of object's derived type based on vtable info
set print pascal_static-members -- Set printing of pascal static members
set print pretty -- Set pretty formatting of structures
set print raw -- Generic command for setting what things to print in "raw" mode
set print raw frame-arguments -- Set whether to print frame arguments in raw form
set print repeats -- Set threshold for repeated print elements
set print sevenbit-strings -- Set printing of 8-bit characters in strings as \nnn
set print static-members -- Set printing of C++ static members
set print symbol -- Set printing of symbol names when printing pointers
set print symbol-filename -- Set printing of source filename and line number with <symbol>
set print symbol-loading -- Set printing of symbol loading messages
set print thread-events -- Set printing of thread events (such as thread start and exit)
set print type -- Generic command for setting how types print
set print type methods -- Set printing of methods defined in classes
--Type <RET> for more, q to quit, c to continue without paging--
set print type nested-type-limit -- Set the number of recursive nested type definitions to print ("unlimited" or -1 to show all)
set print type typedefs -- Set printing of typedefs defined in classes
set print union -- Set printing of unions interior to structures
set print vtbl -- Set printing of C++ virtual function tables
set prompt -- Set gdb's prompt
set python -- Prefix command for python preference settings
set python print-stack -- Set mode for Python stack dump on error
set radix -- Set default input and output number radices
set range-stepping -- Enable or disable range stepping
set record -- Set record options
set record btrace -- Set record options
set record btrace bts -- Set record btrace bts options
set record btrace bts buffer-size -- Set the record/replay bts buffer size
set record btrace cpu -- Set the cpu to be used for trace decode
set record btrace cpu auto -- Automatically determine the cpu to be used for trace decode
set record btrace cpu none -- Do not enable errata workarounds for trace decode
set record btrace pt -- Set record btrace pt options
set record btrace pt buffer-size -- Set the record/replay pt buffer size
set record btrace replay-memory-access -- Set what memory accesses are allowed during replay
set record full -- Set record options
set record full insn-number-max -- Set record/replay buffer limit
set record full memory-query -- Set whether query if PREC cannot record memory change of next instruction
set record full stop-at-limit -- Set whether record/replay stops when record/replay buffer becomes full
set record function-call-history-size -- Set number of function to print in "record function-call-history"
set record instruction-history-size -- Set number of instructions to print in "record instruction-history"
set remote -- Remote protocol specific variables
set remote P-packet -- Set use of remote protocol `P' (set-register) packet
set remote TracepointSource-packet -- Set use of remote protocol `TracepointSource' (TracepointSource) packet
set remote X-packet -- Set use of remote protocol `X' (binary-download) packet
set remote Z-packet -- Set use of remote protocol `Z' packets
set remote access-watchpoint-packet -- Set use of remote protocol `Z4' (access-watchpoint) packet
set remote agent-packet -- Set use of remote protocol `QAgent' (agent) packet
set remote allow-packet -- Set use of remote protocol `QAllow' (allow) packet
set remote attach-packet -- Set use of remote protocol `vAttach' (attach) packet
set remote binary-download-packet -- Set use of remote protocol `X' (binary-download) packet
set remote breakpoint-commands-packet -- Set use of remote protocol `BreakpointCommands' (breakpoint-commands) packet
set remote btrace-conf-bts-size-packet -- Set use of remote protocol `Qbtrace-conf:bts:size' (btrace-conf-bts-size) packet
set remote btrace-conf-pt-size-packet -- Set use of remote protocol `Qbtrace-conf:pt:size' (btrace-conf-pt-size) packet
set remote catch-syscalls-packet -- Set use of remote protocol `QCatchSyscalls' (catch-syscalls) packet
set remote conditional-breakpoints-packet -- Set use of remote protocol `ConditionalBreakpoints' (conditional-breakpoints) packet
set remote conditional-tracepoints-packet -- Set use of remote protocol `ConditionalTracepoints' (conditional-tracepoints) packet
set remote ctrl-c-packet -- Set use of remote protocol `vCtrlC' (ctrl-c) packet
set remote disable-btrace-packet -- Set use of remote protocol `Qbtrace:off' (disable-btrace) packet
set remote disable-randomization-packet -- Set use of remote protocol `QDisableRandomization' (disable-randomization) packet
set remote enable-btrace-bts-packet -- Set use of remote protocol `Qbtrace:bts' (enable-btrace-bts) packet
set remote enable-btrace-pt-packet -- Set use of remote protocol `Qbtrace:pt' (enable-btrace-pt) packet
set remote environment-hex-encoded-packet -- Set use of remote protocol `QEnvironmentHexEncoded' (environment-hex-encoded) packet
set remote environment-reset-packet -- Set use of remote protocol `QEnvironmentReset' (environment-reset) packet
set remote environment-unset-packet -- Set use of remote protocol `QEnvironmentUnset' (environment-unset) packet
set remote exec-event-feature-packet -- Set use of remote protocol `exec-event-feature' (exec-event-feature) packet
set remote exec-file -- Set the remote pathname for "run"
set remote fast-tracepoints-packet -- Set use of remote protocol `FastTracepoints' (fast-tracepoints) packet
set remote fetch-register-packet -- Set use of remote protocol `p' (fetch-register) packet
set remote fork-event-feature-packet -- Set use of remote protocol `fork-event-feature' (fork-event-feature) packet
set remote get-thread-information-block-address-packet -- Set use of remote protocol `qGetTIBAddr' (get-thread-information-block-address) packet
set remote get-thread-local-storage-address-packet -- Set use of remote protocol `qGetTLSAddr' (get-thread-local-storage-address) packet
set remote hardware-breakpoint-limit -- Set the maximum number of target hardware breakpoints
set remote hardware-breakpoint-packet -- Set use of remote protocol `Z1' (hardware-breakpoint) packet
set remote hardware-watchpoint-length-limit -- Set the maximum length (in bytes) of a target hardware watchpoint
set remote hardware-watchpoint-limit -- Set the maximum number of target hardware watchpoints
set remote hostio-close-packet -- Set use of remote protocol `vFile:close' (hostio-close) packet
set remote hostio-fstat-packet -- Set use of remote protocol `vFile:fstat' (hostio-fstat) packet
set remote hostio-open-packet -- Set use of remote protocol `vFile:open' (hostio-open) packet
set remote hostio-pread-packet -- Set use of remote protocol `vFile:pread' (hostio-pread) packet
set remote hostio-pwrite-packet -- Set use of remote protocol `vFile:pwrite' (hostio-pwrite) packet
set remote hostio-readlink-packet -- Set use of remote protocol `vFile:readlink' (hostio-readlink) packet
set remote hostio-setfs-packet -- Set use of remote protocol `vFile:setfs' (hostio-setfs) packet
set remote hostio-unlink-packet -- Set use of remote protocol `vFile:unlink' (hostio-unlink) packet
set remote hwbreak-feature-packet -- Set use of remote protocol `hwbreak-feature' (hwbreak-feature) packet
set remote install-in-trace-packet -- Set use of remote protocol `InstallInTrace' (install-in-trace) packet
set remote interrupt-on-connect -- Set whether interrupt-sequence is sent to remote target when gdb connects to
set remote interrupt-sequence -- Set interrupt sequence to remote target
set remote kill-packet -- Set use of remote protocol `vKill' (kill) packet
set remote library-info-packet -- Set use of remote protocol `qXfer:libraries:read' (library-info) packet
set remote library-info-svr4-packet -- Set use of remote protocol `qXfer:libraries-svr4:read' (library-info-svr4) packet
set remote memory-map-packet -- Set use of remote protocol `qXfer:memory-map:read' (memory-map) packet
set remote memory-read-packet-size -- Set the maximum number of bytes per memory-read packet
set remote memory-write-packet-size -- Set the maximum number of bytes per memory-write packet
--Type <RET> for more, q to quit, c to continue without paging--
set remote multiprocess-feature-packet -- Set use of remote protocol `multiprocess-feature' (multiprocess-feature) packet
set remote no-resumed-stop-reply-packet -- Set use of remote protocol `N stop reply' (no-resumed-stop-reply) packet
set remote noack-packet -- Set use of remote protocol `QStartNoAckMode' (noack) packet
set remote osdata-packet -- Set use of remote protocol `qXfer:osdata:read' (osdata) packet
set remote p-packet -- Set use of remote protocol `p' (fetch-register) packet
set remote pass-signals-packet -- Set use of remote protocol `QPassSignals' (pass-signals) packet
set remote pid-to-exec-file-packet -- Set use of remote protocol `qXfer:exec-file:read' (pid-to-exec-file) packet
set remote program-signals-packet -- Set use of remote protocol `QProgramSignals' (program-signals) packet
set remote query-attached-packet -- Set use of remote protocol `qAttached' (query-attached) packet
set remote read-aux-vector-packet -- Set use of remote protocol `qXfer:auxv:read' (read-aux-vector) packet
set remote read-btrace-conf-packet -- Set use of remote protocol `qXfer:btrace-conf' (read-btrace-conf) packet
set remote read-btrace-packet -- Set use of remote protocol `qXfer:btrace' (read-btrace) packet
set remote read-fdpic-loadmap-packet -- Set use of remote protocol `qXfer:fdpic:read' (read-fdpic-loadmap) packet
set remote read-sdata-object-packet -- Set use of remote protocol `qXfer:statictrace:read' (read-sdata-object) packet
set remote read-siginfo-object-packet -- Set use of remote protocol `qXfer:siginfo:read' (read-siginfo-object) packet
set remote read-spu-object-packet -- Set use of remote protocol `qXfer:spu:read' (read-spu-object) packet
set remote read-watchpoint-packet -- Set use of remote protocol `Z3' (read-watchpoint) packet
set remote reverse-continue-packet -- Set use of remote protocol `bc' (reverse-continue) packet
set remote reverse-step-packet -- Set use of remote protocol `bs' (reverse-step) packet
set remote run-packet -- Set use of remote protocol `vRun' (run) packet
set remote search-memory-packet -- Set use of remote protocol `qSearch:memory' (search-memory) packet
set remote set-register-packet -- Set use of remote protocol `P' (set-register) packet
set remote set-working-dir-packet -- Set use of remote protocol `QSetWorkingDir' (set-working-dir) packet
set remote software-breakpoint-packet -- Set use of remote protocol `Z0' (software-breakpoint) packet
set remote startup-with-shell-packet -- Set use of remote protocol `QStartupWithShell' (startup-with-shell) packet
set remote static-tracepoints-packet -- Set use of remote protocol `StaticTracepoints' (static-tracepoints) packet
set remote supported-packets-packet -- Set use of remote protocol `qSupported' (supported-packets) packet
set remote swbreak-feature-packet -- Set use of remote protocol `swbreak-feature' (swbreak-feature) packet
set remote symbol-lookup-packet -- Set use of remote protocol `qSymbol' (symbol-lookup) packet
set remote system-call-allowed -- Set if the host system(3) call is allowed for the target
set remote target-features-packet -- Set use of remote protocol `qXfer:features:read' (target-features) packet
set remote thread-events-packet -- Set use of remote protocol `QThreadEvents' (thread-events) packet
set remote threads-packet -- Set use of remote protocol `qXfer:threads:read' (threads) packet
set remote trace-buffer-size-packet -- Set use of remote protocol `QTBuffer:size' (trace-buffer-size) packet
set remote trace-status-packet -- Set use of remote protocol `qTStatus' (trace-status) packet
set remote traceframe-info-packet -- Set use of remote protocol `qXfer:traceframe-info:read' (traceframe-info) packet
set remote unwind-info-block-packet -- Set use of remote protocol `qXfer:uib:read' (unwind-info-block) packet
set remote verbose-resume-packet -- Set use of remote protocol `vCont' (verbose-resume) packet
set remote verbose-resume-supported-packet -- Set use of remote protocol `vContSupported' (verbose-resume-supported) packet
--Type <RET> for more, q to quit, c to continue without paging--
set remote vfork-event-feature-packet -- Set use of remote protocol `vfork-event-feature' (vfork-event-feature) packet
set remote write-siginfo-object-packet -- Set use of remote protocol `qXfer:siginfo:write' (write-siginfo-object) packet
set remote write-spu-object-packet -- Set use of remote protocol `qXfer:spu:write' (write-spu-object) packet
set remote write-watchpoint-packet -- Set use of remote protocol `Z2' (write-watchpoint) packet
set remoteaddresssize -- Set the maximum size of the address (in bits) in a memory packet
set remotecache -- Set cache use for remote targets
set remoteflow -- Set use of hardware flow control for remote serial I/O
set remotelogbase -- Set numerical base for remote session logging
set remotelogfile -- Set filename for remote session recording
set remotetimeout -- Set timeout limit to wait for target to respond
set remotewritesize -- Set the maximum number of bytes per memory write packet (deprecated)
set schedule-multiple -- Set mode for resuming threads of all processes
set scheduler-locking -- Set mode for locking scheduler during execution
set script-extension -- Set mode for script filename extension recognition
set serial -- Set default serial/parallel port configuration
set serial baud -- Set baud rate for remote serial I/O
set serial parity -- Set parity for remote serial I/O
set solib-absolute-prefix -- Set an alternate system root
set solib-search-path -- Set the search path for loading non-absolute shared library symbol files
set stack-cache -- Set cache use for stack access
set startup-with-shell -- Set use of shell to start subprocesses
set step-mode -- Set mode of the step operation
set stop-on-solib-events -- Set stopping for shared library events
set struct-convention -- Set the convention for returning small structs
set style -- Style-specific settings
set style address -- Address display styling
set style address background -- Set the background color for this property
set style address foreground -- Set the foreground color for this property
set style address intensity -- Set the display intensity for this property
set style enabled -- Set whether CLI styling is enabled
set style filename -- Filename display styling
set style filename background -- Set the background color for this property
set style filename foreground -- Set the foreground color for this property
set style filename intensity -- Set the display intensity for this property
set style function -- Function name display styling
set style function background -- Set the background color for this property
set style function foreground -- Set the foreground color for this property
set style function intensity -- Set the display intensity for this property
set style sources -- Set whether source code styling is enabled
set style variable -- Variable name display styling
set style variable background -- Set the background color for this property
set style variable foreground -- Set the foreground color for this property
set style variable intensity -- Set the display intensity for this property
set substitute-path -- Usage: set substitute-path FROM TO
set sysroot -- Set an alternate system root
set target-charset -- Set the target character set
set target-file-system-kind -- Set assumed file system kind for target reported file names
set target-wide-charset -- Set the target wide character set
set tcp -- TCP protocol specific variables
set tcp auto-retry -- Set auto-retry on socket connect
set tcp connect-timeout -- Set timeout limit in seconds for socket connection
set tdesc -- Set target description specific variables
set tdesc filename -- Set the file to read for an XML target description
set trace-buffer-size -- Set requested size of trace buffer
set trace-commands -- Set tracing of GDB CLI commands
set trace-notes -- Set notes string to use for current and future trace runs
set trace-stop-notes -- Set notes string to use for future tstop commands
set trace-user -- Set the user name to use for current and future trace runs
set trust-readonly-sections -- Set mode for reading from readonly sections
set tui -- TUI configuration variables
set tui active-border-mode -- Set the attribute mode to use for the active TUI window border
set tui border-kind -- Set the kind of border for TUI windows
set tui border-mode -- Set the attribute mode to use for the TUI window borders
set tui tab-width -- Set the tab width
set unwind-on-terminating-exception -- Set unwinding of stack if std::terminate is called while in call dummy
set unwindonsignal -- Set unwinding of stack if a signal is received while in a call dummy
set use-coredump-filter -- Set whether gcore should consider /proc/PID/coredump_filter
set use-deprecated-index-sections -- Set whether to use deprecated gdb_index sections
set var -- Evaluate expression EXP and assign result to variable VAR
set variable -- Evaluate expression EXP and assign result to variable VAR
set varsize-limit -- Set the maximum number of bytes allowed in a variable-size object
set verbose -- Set verbosity
set watchdog -- Set watchdog timer
set width -- Set number of characters where GDB should wrap lines of its output
set write -- Set writing into executable and core files
````

## control

````
start -- Start the debugged program stopping at the beginning of the main procedure
advance -- Continue the program up to the given location (same form as args for break command)
continue -- Continue program being debugged
jump -- Continue program being debugged at specified line or address
next -- Step program
nexti -- Step one instruction
step -- Step program until it reaches a different source line
stepi -- Step one instruction exactly
run -- Start debugged program
until -- Execute until the program reaches a source line greater than the current
interrupt -- Interrupt the execution of the debugged program
Aliases:
ni -- Step one instruction
rc -- Continue program being debugged but run it in reverse
rni -- Step backward one instruction
rsi -- Step backward exactly one instruction
si -- Step one instruction exactly
stepping -- Specify single-stepping behavior at a tracepoint
tp -- Set a tracepoint at specified location
tty -- Set terminal for future runs of program being debugged
where -- Print backtrace of all stack frames
ws -- Specify single-stepping behavior at a tracepoint

reverse-continue -- Continue program being debugged but run it in reverse
reverse-finish -- Execute backward until just before selected stack frame is called
reverse-next -- Step program backward
reverse-nexti -- Step backward one instruction
reverse-step -- Step program backward until it reaches the beginning of another source line
reverse-stepi -- Step backward exactly one instruction

attach -- Attach to a process or file outside of GDB
detach -- Detach a process or file previously attached
detach checkpoint -- Detach from a checkpoint (experimental)
detach inferiors -- Detach from inferior ID (or list of IDS)
disconnect -- Disconnect from a target
finish -- Execute until selected stack frame returns
handle -- Specify how to handle signals
inferior -- Use this command to switch between inferiors
kill -- Kill execution of program being debugged
kill inferiors -- Kill inferior ID (or list of IDs)
queue-signal -- Queue a signal to be delivered to the current thread when it is resumed
signal -- Continue program with the specified signal
starti -- Start the debugged program stopping at the first instruction
taas -- Apply a command to all threads (ignoring errors and empty output)
target -- Connect to a target machine or process
target core -- Use a core file as a target
target ctf -- (Use a CTF directory as a target
target exec -- Use an executable file as a target
target extended-remote -- Use a remote computer via a serial line
target native -- Native process (started by the "run" command)
target record-btrace -- Collect control-flow trace and provide the execution history
target record-core -- Log program while executing and replay execution from log
target record-full -- Log program while executing and replay execution from log
target remote -- Use a remote computer via a serial line
target tfile -- Use a trace file as a target
task -- Use this command to switch between Ada tasks
tfaas -- Apply a command to all frames of all threads (ignoring errors and empty output)
thread -- Use this command to switch between threads
thread apply -- Apply a command to a list of threads
thread apply all -- Apply a command to all threads
thread find -- Find threads that match a regular expression
thread name -- Set the current thread's name
````

## Status

````
info -- Generic command for showing things about the program being debugged
info address -- Describe where symbol SYM is stored
info all-registers -- List of all registers and their contents
info args -- All argument variables of current stack frame or those matching REGEXPs
info auto-load -- Print current status of auto-loaded files
info auto-load gdb-scripts -- Print the list of automatically loaded sequences of commands
info auto-load libthread-db -- Print the list of loaded inferior specific libthread_db
info auto-load local-gdbinit -- Print whether current directory .gdbinit file has been loaded
info auto-load python-scripts -- Print the list of automatically loaded Python scripts
info auxv -- Display the inferior's auxiliary vector
info bookmarks -- Status of user-settable bookmarks
info breakpoints -- Status of specified breakpoints (all user-settable breakpoints if no argument)
info checkpoints -- IDs of currently known checkpoints
info classes -- All Objective-C classes
info common -- Print out the values contained in a Fortran COMMON block
info copying -- Conditions for redistributing copies of GDB
info dcache -- Print information on the dcache performance
info display -- Expressions to display when program stops
info exceptions -- List all Ada exception names
info extensions -- All filename extensions associated with a source language
info files -- Names of targets and files being debugged
info float -- Print the status of the floating point unit
info frame -- All about the selected stack frame
info frame address -- Print information about a stack frame selected by stack address
info frame function -- Print information about a stack frame selected by function name
info frame level -- Print information about a stack frame selected by level
info frame view -- Print information about a stack frame outside the current backtrace
info frame-filter -- List all registered Python frame-filters
info functions -- All function names or those matching REGEXPs
info guile -- Prefix command for Guile info displays
info handle -- What debugger does when program gets various signals
info inferiors -- Print a list of inferiors being managed
info line -- Core addresses of the code for a source line
info locals -- All local variables of current stack frame or those matching REGEXPs
info macro -- Show the definition of MACRO
info macros -- Show the definitions of all macros at LINESPEC
info mem -- Memory region attributes
info os -- Show OS data ARG
info pretty-printer -- GDB command to list all registered pretty-printers
info probes -- Show available static probes
info probes all -- Show information about all type of probes
info probes dtrace -- Show information about DTrace static probes
info probes stap -- Show information about SystemTap static probes
info proc -- Show additional information about a process
info proc all -- List all available info about the specified process
info proc cmdline -- List command line arguments of the specified process
info proc cwd -- List current working directory of the specified process
info proc exe -- List absolute filename for executable of the specified process
info proc files -- List files opened by the specified process
info proc mappings -- List memory regions mapped by the specified process
info proc stat -- List process info from /proc/PID/stat
info proc status -- List process info from /proc/PID/status
info program -- Execution status of the program
info record -- Info record options
info registers -- List of integer registers and their contents
info scope -- List the variables local to a scope
info selectors -- All Objective-C selectors
info set -- Show all GDB settings
info sharedlibrary -- Status of loaded shared object libraries
info signals -- What debugger does when program gets various signals
info skip -- Display the status of skips
info source -- Information about the current source file
info sources -- Source files in the program
info stack -- Backtrace of the stack
info static-tracepoint-markers -- List target static tracepoints markers
info symbol -- Describe what symbol is at location ADDR
info target -- Names of targets and files being debugged
info tasks -- Provide information about all known Ada tasks
info terminal -- Print inferior's saved terminal status
info threads -- Display currently known threads
info tracepoints -- Status of specified tracepoints (all tracepoints if no argument)
info tvariables -- Status of trace state variables and their values
info type-printers -- GDB command to list all registered type-printers
info types -- All type names
info unwinder -- GDB command to list unwinders
info variables -- All global and static variable names or those matching REGEXPs
info vector -- Print the status of the vector unit
info vtbl -- Show the virtual function table for a C++ object
info warranty -- Various kinds of warranty you do not have
info watchpoints -- Status of specified watchpoints (all watchpoints if no argument)
info win -- List of all displayed windows
info xmethod -- GDB command to list registered xmethod matchers
macro -- Prefix for commands dealing with C preprocessor macros
macro define -- Define a new C/C++ preprocessor macro
macro expand -- Fully expand any C/C++ preprocessor macro invocations in EXPRESSION
macro expand-once -- Expand C/C++ preprocessor macro invocations appearing directly in EXPRESSION
macro list -- List all the macros defined using the `macro define' command
macro undef -- Remove the definition of the C/C++ preprocessor macro with the given name
show -- Generic command for showing things about the debugger
show ada -- Generic command for showing Ada-specific settings
show ada print-signatures -- Show whether the output of formal and return types for functions in the overloads selection menu is activated
show ada trust-PAD-over-XVS -- Show whether an optimization trusting PAD types over XVS types is activated
show agent -- Show debugger's willingness to use agent as a helper
show annotate -- Show annotation_level
show architecture -- Show architecture of target
show args -- Show argument list to give program being debugged when it is started
show auto-connect-native-target -- Show whether GDB may automatically connect to the native target
show auto-load -- Show auto-loading specific settings
show auto-load gdb-scripts -- Show whether auto-loading of canned sequences of commands scripts is enabled
show auto-load libthread-db -- Show whether auto-loading inferior specific libthread_db is enabled
show auto-load local-gdbinit -- Show whether auto-loading .gdbinit script in current directory is enabled
show auto-load python-scripts -- Show the debugger's behaviour regarding auto-loaded Python scripts
show auto-load safe-path -- Show the list of files and directories that are safe for auto-loading
show auto-load scripts-directory -- Show the list of directories from which to load auto-loaded scripts
show auto-solib-add -- Show autoloading of shared library symbols
show backtrace -- Show backtrace specific variables
show backtrace limit -- Show the upper bound on the number of backtrace levels
show backtrace past-entry -- Show whether backtraces should continue past the entry point of a program
show backtrace past-main -- Show whether backtraces should continue past "main"
show basenames-may-differ -- Show whether a source file may have multiple base names
show breakpoint -- Breakpoint specific settings
show breakpoint always-inserted -- Show mode for inserting breakpoints
show breakpoint auto-hw -- Show automatic usage of hardware breakpoints
show breakpoint condition-evaluation -- Show mode of breakpoint condition evaluation
show breakpoint pending -- Show debugger's behavior regarding pending breakpoints
show can-use-hw-watchpoints -- Show debugger's willingness to use watchpoint hardware
show case-sensitive -- Show case sensitivity in name search
show charset -- Show the host and target character sets
show check -- Show the status of the type/range checker
show check range -- Show range checking
show check type -- Show strict type checking
show circular-trace-buffer -- Show target's use of circular trace buffer
show code-cache -- Show cache use for code segment access
show coerce-float-to-double -- Show coercion of floats to doubles when calling functions
show commands -- Show the history of commands you typed
show compile-args -- Show compile command GCC command-line arguments
show compile-gcc -- Show compile command GCC driver filename
show complaints -- Show max number of complaints about incorrect symbols
show configuration -- Show how GDB was configured at build time
show confirm -- Show whether to confirm potentially dangerous operations
show convenience -- Debugger convenience ("$foo") variables and functions
show copying -- Conditions for redistributing copies of GDB
show cp-abi -- Show the ABI used for inspecting C++ objects
show cwd -- Show the current working directory that is used when the inferior is started
show data-directory -- Show GDB's data directory
show dcache -- Show dcachesettings
show dcache line-size -- Show dcache line size
show dcache size -- Show number of dcache lines
show debug -- Generic command for showing gdb debugging flags
show debug arch -- Show architecture debugging
show debug auto-load -- Show auto-load verifications debugging
show debug bfd-cache -- Show bfd cache debugging
show debug check-physname -- Show cross-checking of "physname" code against demangler
show debug coff-pe-read -- Show coff PE read debugging
show debug compile -- Show compile command debugging
show debug compile-cplus-scopes -- Show debugging of C++ compile scopes
show debug compile-cplus-types -- Show debugging of C++ compile type conversion
show debug displaced -- Show displaced stepping debugging
show debug dwarf-die -- Show debugging of the DWARF DIE reader
show debug dwarf-line -- Show debugging of the dwarf line reader
show debug dwarf-read -- Show debugging of the DWARF reader
show debug entry-values -- Show entry values and tail call frames debugging
show debug expression -- Show expression debugging
show debug frame -- Show frame debugging
show debug index-cache -- Show display of index-cache debug messages
show debug infrun -- Show inferior debugging
show debug jit -- Show JIT debugging
show debug libthread-db -- Show libthread-db debugging
show debug lin-lwp -- Show debugging of GNU/Linux lwp module
show debug linux-namespaces -- Show debugging of GNU/Linux namespaces module
show debug notification -- Show debugging of async remote notification
show debug observer -- Show observer debugging
show debug overload -- Show debugging of C++ overloading
show debug parser -- Show parser debugging
show debug py-unwind -- Show Python unwinder debugging
show debug record -- Show debugging of record/replay feature
show debug remote -- Show debugging of remote protocol
show debug separate-debug-file -- Show printing of separate debug info file search debug
show debug serial -- Show serial debugging
show debug skip -- Show whether the debug output about skipping files and functions is printed
show debug stap-expression -- Show SystemTap expression debugging
show debug symbol-lookup -- Show debugging of symbol lookup
show debug symfile -- Show debugging of the symfile functions
show debug symtab-create -- Show debugging of symbol table creation
show debug target -- Show target debugging
show debug timestamp -- Show timestamping of debugging messages
show debug varobj -- Show varobj debugging
show debug xml -- Show XML parser debugging
show debug-file-directory -- Show the directories where separate debug symbols are searched for
show default-collect -- Show the list of expressions to collect by default
show demangle-style -- Show the current C++ demangling style
show detach-on-fork -- Show whether gdb will detach the child of a fork
show directories -- Show the search path for finding source files
show disable-randomization -- Show disabling of debuggee's virtual address space randomization
show disassemble-next-line -- Show whether to disassemble next source line or insn when execution stops
show disassembler-options -- Show the disassembler options
show disassembly-flavor -- Show the disassembly flavor
show disconnected-dprintf -- Show whether dprintf continues after GDB disconnects
show disconnected-tracing -- Show whether tracing continues after GDB disconnects
show displaced-stepping -- Show debugger's willingness to use displaced stepping
show dprintf-channel -- Show the channel to use for dynamic printf
show dprintf-function -- Show the function to use for dynamic printf
show dprintf-style -- Show the style of usage for dynamic printf
show dump-excluded-mappings -- Show whether gcore should dump mappings marked with the VM_DONTDUMP flag
show editing -- Show editing of command lines as they are typed
show endian -- Show endianness of target
show environment -- The environment to give the program
show exec-direction -- Show direction of execution (forward/reverse)
show exec-done-display -- Show notification of completion for asynchronous execution commands
show exec-wrapper -- Show the wrapper for running programs
show extended-prompt -- Show the extended prompt
show extension-language -- Show mapping between filename extension and source language
show filename-display -- Show how to display filenames
show follow-exec-mode -- Show debugger response to a program call of exec
show follow-fork-mode -- Show debugger response to a program call of fork or vfork
show frame-filter -- Prefix command for 'show' frame-filter related operations
show frame-filter priority -- GDB command to show the priority of the specified frame-filter
show gnutarget -- Show the current BFD target
show guile -- Prefix command for Guile preference settings
show guile print-stack -- Show the mode of Guile exception printing on error
show height -- Show number of lines in a page for GDB output pagination
show history -- Generic command for showing command history parameters
show history expansion -- Show history expansion on command input
show history filename -- Show the filename in which to record the command history
show history remove-duplicates -- Show how far back in history to look for and remove duplicate entries
show history save -- Show saving of the history record on exit
show history size -- Show the size of the command history
show host-charset -- Show the host character set
show index-cache -- Show index-cache options
show index-cache directory -- Show the directory of the index cache
show index-cache stats -- Show some stats about the index cache
show inferior-tty -- Show terminal for future runs of program being debugged
show input-radix -- Show default input radix for entering numbers
show interactive-mode -- Show whether GDB's standard input is a terminal
show language -- Show the current source language
show libthread-db-search-path -- Show the current search path or libthread_db
show listsize -- Show number of source lines gdb will list by default
show logging -- Show logging options
show logging file -- Show the current logfile
show logging overwrite -- Show whether logging overwrites or appends to the log file
show logging redirect -- Show the logging output mode
show max-completions -- Show maximum number of completion candidates
show max-user-call-depth -- Show the max call depth for non-python/scheme user-defined commands
show max-value-size -- Show maximum sized value gdb will load from the inferior
show may-insert-breakpoints -- Show permission to insert breakpoints in the target
show may-insert-fast-tracepoints -- Show permission to insert fast tracepoints in the target
show may-insert-tracepoints -- Show permission to insert tracepoints in the target
show may-interrupt -- Show permission to interrupt or signal the target
show may-write-memory -- Show permission to write into target memory
show may-write-registers -- Show permission to write into registers
show mem -- Memory regions settings
show mem  inaccessible-by-default -- Show handling of unknown memory regions
show mi-async -- Show whether MI asynchronous mode is enabled
show mpx -- Show Intel Memory Protection Extensions specific variables
show mpx bound -- Show the memory bounds for a given array/pointer storage in the bound table
show multiple-symbols -- Show how the debugger handles ambiguities in expressions
show non-stop -- Show whether gdb controls the inferior in non-stop mode
show observer -- Show whether gdb controls the inferior in observer mode
show opaque-type-resolution -- Show resolution of opaque struct/class/union types (if set before loading symbols)
show osabi -- Show OS ABI of target
show output-radix -- Show default output radix for printing of values
show overload-resolution -- Show overload resolution in evaluating C++ functions
show pagination -- Show state of GDB output pagination
show paths -- Current search path for finding object files
show print -- Generic command for showing print settings
show print address -- Show printing of addresses
show print array -- Show pretty formatting of arrays
show print array-indexes -- Show printing of array indexes
show print asm-demangle -- Show demangling of C++/ObjC names in disassembly listings
show print demangle -- Show demangling of encoded C++/ObjC names when displaying symbols
show print elements -- Show limit on string chars or array elements to print
show print entry-values -- Show printing of function arguments at function entry
show print frame-arguments -- Show printing of non-scalar frame arguments
show print inferior-events -- Show printing of inferior events (e.g.
show print max-symbolic-offset -- Show the largest offset that will be printed in <symbol+1234> form
show print null-stop -- Show printing of char arrays to stop at first null char
show print object -- Show printing of object's derived type based on vtable info
show print pascal_static-members -- Show printing of pascal static members
show print pretty -- Show pretty formatting of structures
show print raw -- Generic command for showing "print raw" settings
show print raw frame-arguments -- Show whether to print frame arguments in raw form
show print repeats -- Show threshold for repeated print elements
show print sevenbit-strings -- Show printing of 8-bit characters in strings as \nnn
show print static-members -- Show printing of C++ static members
show print symbol -- Show printing of symbol names when printing pointers
show print symbol-filename -- Show printing of source filename and line number with <symbol>
show print symbol-loading -- Show printing of symbol loading messages
show print thread-events -- Show printing of thread events (such as thread start and exit)
show print type -- Generic command for showing type-printing settings
show print type methods -- Show printing of methods defined in classes
show print type nested-type-limit -- Show the number of recursive nested type definitions to print
show print type typedefs -- Show printing of typedefs defined in classes
show print union -- Show printing of unions interior to structures
show print vtbl -- Show printing of C++ virtual function tables
show prompt -- Show gdb's prompt
show python -- Prefix command for python preference settings
show python print-stack -- Show the mode of Python stack printing on error
show radix -- Show the default input and output number radices
show range-stepping -- Show whether target-assisted range stepping is enabled
show record -- Show record options
show record btrace -- Show record options
show record btrace bts -- Show record btrace bts options
show record btrace bts buffer-size -- Show the record/replay bts buffer size
show record btrace cpu -- Show the cpu to be used for trace decode
show record btrace pt -- Show record btrace pt options
show record btrace pt buffer-size -- Show the record/replay pt buffer size
show record btrace replay-memory-access -- Show what memory accesses are allowed during replay
show record full -- Show record options
show record full insn-number-max -- Show record/replay buffer limit
show record full memory-query -- Show whether query if PREC cannot record memory change of next instruction
show record full stop-at-limit -- Show whether record/replay stops when record/replay buffer becomes full
show record function-call-history-size -- Show number of functions to print in "record function-call-history"
show record instruction-history-size -- Show number of instructions to print in "record instruction-history"
show remote -- Remote protocol specific variables
show remote P-packet -- Show current use of remote protocol `P' (set-register) packet
show remote TracepointSource-packet -- Show current use of remote protocol `TracepointSource' (TracepointSource) packet
show remote X-packet -- Show current use of remote protocol `X' (binary-download) packet
show remote Z-packet -- Show use of remote protocol `Z' packets 
show remote access-watchpoint-packet -- Show current use of remote protocol `Z4' (access-watchpoint) packet
show remote agent-packet -- Show current use of remote protocol `QAgent' (agent) packet
show remote allow-packet -- Show current use of remote protocol `QAllow' (allow) packet
show remote attach-packet -- Show current use of remote protocol `vAttach' (attach) packet
show remote binary-download-packet -- Show current use of remote protocol `X' (binary-download) packet
show remote breakpoint-commands-packet -- Show current use of remote protocol `BreakpointCommands' (breakpoint-commands) packet
show remote btrace-conf-bts-size-packet -- Show current use of remote protocol `Qbtrace-conf:bts:size' (btrace-conf-bts-size) packet
show remote btrace-conf-pt-size-packet -- Show current use of remote protocol `Qbtrace-conf:pt:size' (btrace-conf-pt-size) packet
show remote catch-syscalls-packet -- Show current use of remote protocol `QCatchSyscalls' (catch-syscalls) packet
show remote conditional-breakpoints-packet -- Show current use of remote protocol `ConditionalBreakpoints' (conditional-breakpoints) packet
show remote conditional-tracepoints-packet -- Show current use of remote protocol `ConditionalTracepoints' (conditional-tracepoints) packet
show remote ctrl-c-packet -- Show current use of remote protocol `vCtrlC' (ctrl-c) packet
show remote disable-btrace-packet -- Show current use of remote protocol `Qbtrace:off' (disable-btrace) packet
show remote disable-randomization-packet -- Show current use of remote protocol `QDisableRandomization' (disable-randomization) packet
show remote enable-btrace-bts-packet -- Show current use of remote protocol `Qbtrace:bts' (enable-btrace-bts) packet
show remote enable-btrace-pt-packet -- Show current use of remote protocol `Qbtrace:pt' (enable-btrace-pt) packet
show remote environment-hex-encoded-packet -- Show current use of remote protocol `QEnvironmentHexEncoded' (environment-hex-encoded) packet
show remote environment-reset-packet -- Show current use of remote protocol `QEnvironmentReset' (environment-reset) packet
show remote environment-unset-packet -- Show current use of remote protocol `QEnvironmentUnset' (environment-unset) packet
show remote exec-event-feature-packet -- Show current use of remote protocol `exec-event-feature' (exec-event-feature) packet
show remote exec-file -- Show the remote pathname for "run"
show remote fast-tracepoints-packet -- Show current use of remote protocol `FastTracepoints' (fast-tracepoints) packet
show remote fetch-register-packet -- Show current use of remote protocol `p' (fetch-register) packet
show remote fork-event-feature-packet -- Show current use of remote protocol `fork-event-feature' (fork-event-feature) packet
show remote get-thread-information-block-address-packet -- Show current use of remote protocol `qGetTIBAddr' (get-thread-information-block-address) packet
show remote get-thread-local-storage-address-packet -- Show current use of remote protocol `qGetTLSAddr' (get-thread-local-storage-address) packet
show remote hardware-breakpoint-limit -- Show the maximum number of target hardware breakpoints
show remote hardware-breakpoint-packet -- Show current use of remote protocol `Z1' (hardware-breakpoint) packet
show remote hardware-watchpoint-length-limit -- Show the maximum length (in bytes) of a target hardware watchpoint
show remote hardware-watchpoint-limit -- Show the maximum number of target hardware watchpoints
show remote hostio-close-packet -- Show current use of remote protocol `vFile:close' (hostio-close) packet
show remote hostio-fstat-packet -- Show current use of remote protocol `vFile:fstat' (hostio-fstat) packet
show remote hostio-open-packet -- Show current use of remote protocol `vFile:open' (hostio-open) packet
show remote hostio-pread-packet -- Show current use of remote protocol `vFile:pread' (hostio-pread) packet
show remote hostio-pwrite-packet -- Show current use of remote protocol `vFile:pwrite' (hostio-pwrite) packet
show remote hostio-readlink-packet -- Show current use of remote protocol `vFile:readlink' (hostio-readlink) packet
show remote hostio-setfs-packet -- Show current use of remote protocol `vFile:setfs' (hostio-setfs) packet
show remote hostio-unlink-packet -- Show current use of remote protocol `vFile:unlink' (hostio-unlink) packet
show remote hwbreak-feature-packet -- Show current use of remote protocol `hwbreak-feature' (hwbreak-feature) packet
show remote install-in-trace-packet -- Show current use of remote protocol `InstallInTrace' (install-in-trace) packet
show remote interrupt-on-connect -- 		Show whether interrupt-sequence is sent to remote target when gdb connects to
show remote interrupt-sequence -- Show interrupt sequence to remote target
show remote kill-packet -- Show current use of remote protocol `vKill' (kill) packet
show remote library-info-packet -- Show current use of remote protocol `qXfer:libraries:read' (library-info) packet
show remote library-info-svr4-packet -- Show current use of remote protocol `qXfer:libraries-svr4:read' (library-info-svr4) packet
show remote memory-map-packet -- Show current use of remote protocol `qXfer:memory-map:read' (memory-map) packet
show remote memory-read-packet-size -- Show the maximum number of bytes per memory-read packet
show remote memory-write-packet-size -- Show the maximum number of bytes per memory-write packet
show remote multiprocess-feature-packet -- Show current use of remote protocol `multiprocess-feature' (multiprocess-feature) packet
show remote no-resumed-stop-reply-packet -- Show current use of remote protocol `N stop reply' (no-resumed-stop-reply) packet
show remote noack-packet -- Show current use of remote protocol `QStartNoAckMode' (noack) packet
show remote osdata-packet -- Show current use of remote protocol `qXfer:osdata:read' (osdata) packet
show remote p-packet -- Show current use of remote protocol `p' (fetch-register) packet
show remote pass-signals-packet -- Show current use of remote protocol `QPassSignals' (pass-signals) packet
show remote pid-to-exec-file-packet -- Show current use of remote protocol `qXfer:exec-file:read' (pid-to-exec-file) packet
show remote program-signals-packet -- Show current use of remote protocol `QProgramSignals' (program-signals) packet
show remote query-attached-packet -- Show current use of remote protocol `qAttached' (query-attached) packet
show remote read-aux-vector-packet -- Show current use of remote protocol `qXfer:auxv:read' (read-aux-vector) packet
show remote read-btrace-conf-packet -- Show current use of remote protocol `qXfer:btrace-conf' (read-btrace-conf) packet
show remote read-btrace-packet -- Show current use of remote protocol `qXfer:btrace' (read-btrace) packet
show remote read-fdpic-loadmap-packet -- Show current use of remote protocol `qXfer:fdpic:read' (read-fdpic-loadmap) packet
show remote read-sdata-object-packet -- Show current use of remote protocol `qXfer:statictrace:read' (read-sdata-object) packet
show remote read-siginfo-object-packet -- Show current use of remote protocol `qXfer:siginfo:read' (read-siginfo-object) packet
show remote read-spu-object-packet -- Show current use of remote protocol `qXfer:spu:read' (read-spu-object) packet
show remote read-watchpoint-packet -- Show current use of remote protocol `Z3' (read-watchpoint) packet
show remote reverse-continue-packet -- Show current use of remote protocol `bc' (reverse-continue) packet
show remote reverse-step-packet -- Show current use of remote protocol `bs' (reverse-step) packet
show remote run-packet -- Show current use of remote protocol `vRun' (run) packet
show remote search-memory-packet -- Show current use of remote protocol `qSearch:memory' (search-memory) packet
show remote set-register-packet -- Show current use of remote protocol `P' (set-register) packet
show remote set-working-dir-packet -- Show current use of remote protocol `QSetWorkingDir' (set-working-dir) packet
show remote software-breakpoint-packet -- Show current use of remote protocol `Z0' (software-breakpoint) packet
show remote startup-with-shell-packet -- Show current use of remote protocol `QStartupWithShell' (startup-with-shell) packet
show remote static-tracepoints-packet -- Show current use of remote protocol `StaticTracepoints' (static-tracepoints) packet
show remote supported-packets-packet -- Show current use of remote protocol `qSupported' (supported-packets) packet
show remote swbreak-feature-packet -- Show current use of remote protocol `swbreak-feature' (swbreak-feature) packet
show remote symbol-lookup-packet -- Show current use of remote protocol `qSymbol' (symbol-lookup) packet
show remote system-call-allowed -- Show if the host system(3) call is allowed for the target
show remote target-features-packet -- Show current use of remote protocol `qXfer:features:read' (target-features) packet
show remote thread-events-packet -- Show current use of remote protocol `QThreadEvents' (thread-events) packet
show remote threads-packet -- Show current use of remote protocol `qXfer:threads:read' (threads) packet
show remote trace-buffer-size-packet -- Show current use of remote protocol `QTBuffer:size' (trace-buffer-size) packet
show remote trace-status-packet -- Show current use of remote protocol `qTStatus' (trace-status) packet
show remote traceframe-info-packet -- Show current use of remote protocol `qXfer:traceframe-info:read' (traceframe-info) packet
show remote unwind-info-block-packet -- Show current use of remote protocol `qXfer:uib:read' (unwind-info-block) packet
show remote verbose-resume-packet -- Show current use of remote protocol `vCont' (verbose-resume) packet
show remote verbose-resume-supported-packet -- Show current use of remote protocol `vContSupported' (verbose-resume-supported) packet
show remote vfork-event-feature-packet -- Show current use of remote protocol `vfork-event-feature' (vfork-event-feature) packet
show remote write-siginfo-object-packet -- Show current use of remote protocol `qXfer:siginfo:write' (write-siginfo-object) packet
show remote write-spu-object-packet -- Show current use of remote protocol `qXfer:spu:write' (write-spu-object) packet
show remote write-watchpoint-packet -- Show current use of remote protocol `Z2' (write-watchpoint) packet
show remoteaddresssize -- Show the maximum size of the address (in bits) in a memory packet
show remotecache -- Show cache use for remote targets
show remoteflow -- Show use of hardware flow control for remote serial I/O
show remotelogbase -- Show numerical base for remote session logging
show remotelogfile -- Show filename for remote session recording
show remotetimeout -- Show timeout limit to wait for target to respond
show remotewritesize -- Show the maximum number of bytes per memory write packet (deprecated)
show schedule-multiple -- Show mode for resuming threads of all processes
show scheduler-locking -- Show mode for locking scheduler during execution
show script-extension -- Show mode for script filename extension recognition
show serial -- Show default serial/parallel port configuration
show serial baud -- Show baud rate for remote serial I/O
show serial parity -- Show parity for remote serial I/O
show solib-absolute-prefix -- Show the current system root
show solib-search-path -- Show the search path for loading non-absolute shared library symbol files
show stack-cache -- Show cache use for stack access
show startup-with-shell -- Show use of shell to start subprocesses
show step-mode -- Show mode of the step operation
show stop-on-solib-events -- Show stopping for shared library events
show struct-convention -- Show the convention for returning small structs
show style -- Style-specific settings
show style address -- Address display styling
show style address background -- Show the background color for this property
show style address foreground -- Show the foreground color for this property
show style address intensity -- Show the display intensity for this property
show style enabled -- Show whether CLI is enabled
show style filename -- Filename display styling
show style filename background -- Show the background color for this property
show style filename foreground -- Show the foreground color for this property
show style filename intensity -- Show the display intensity for this property
show style function -- Function name display styling
show style function background -- Show the background color for this property
show style function foreground -- Show the foreground color for this property
show style function intensity -- Show the display intensity for this property
show style sources -- Show whether source code styling is enabled
show style variable -- Variable name display styling
show style variable background -- Show the background color for this property
show style variable foreground -- Show the foreground color for this property
show style variable intensity -- Show the display intensity for this property
show substitute-path -- Usage: show substitute-path [FROM]
show sysroot -- Show the current system root
show target-charset -- Show the target character set
show target-file-system-kind -- Show assumed file system kind for target reported file names
show target-wide-charset -- Show the target wide character set
show tcp -- TCP protocol specific variables
show tcp auto-retry -- Show auto-retry on socket connect
show tcp connect-timeout -- Show timeout limit in seconds for socket connection
show tdesc -- Show target description specific variables
show tdesc filename -- Show the file to read for an XML target description
show trace-buffer-size -- Show requested size of trace buffer
show trace-commands -- Show state of GDB CLI command tracing
show trace-notes -- Show the notes string to use for current and future trace runs
show trace-stop-notes -- Show the notes string to use for future tstop commands
show trace-user -- Show the user name to use for current and future trace runs
show trust-readonly-sections -- Show mode for reading from readonly sections
show tui -- TUI configuration variables
show tui active-border-mode -- Show the attribute mode to use for the active TUI window border
show tui border-kind -- Show the kind of border for TUI windows
show tui border-mode -- Show the attribute mode to use for the TUI window borders
show tui tab-width -- Show the tab witdh
show unwind-on-terminating-exception -- Show unwinding of stack if std::terminate() is called while in a call dummy
show unwindonsignal -- Show unwinding of stack if a signal is received while in a call dummy
show use-coredump-filter -- Show whether gcore should consider /proc/PID/coredump_filter
show use-deprecated-index-sections -- Show whether to use deprecated gdb_index sections
show user -- Show definitions of non-python/scheme user defined commands
show values -- Elements of value history around item number IDX (or last ten)
show varsize-limit -- Show the maximum number of bytes allowed in a variable-size object
show verbose -- Show verbosity
show version -- Show what version of GDB this is
show warranty -- Various kinds of warranty you do not have
show watchdog -- Show watchdog timer
show width -- Show number of characters where GDB should wrap lines of its output
show write -- Show writing into executable and core files
````

## GDB internals

### Most useful

````
source -- Read commands from a file named FILE
quit -- Exit gdb
alias -- Define a new command that is an alias of an existing command
````

### Others

````
! -- Execute the rest of the line as a shell command
add-auto-load-safe-path -- Add entries to the list of directories from which it is safe to auto-load files
add-auto-load-scripts-directory -- Add entries to the list of directories from which to load auto-loaded scripts
apropos -- Search for commands matching a REGEXP
define -- Define a new command name
demangle -- Demangle a mangled name
document -- Document a user-defined command
dont-repeat -- Don't repeat this command
down-silently -- Same as the `down' command
echo -- Print a constant string
help -- Print list of commands
if -- Execute nested commands once IF the conditional expression is non zero
interpreter-exec -- Execute a command in an interpreter
make -- Run the ``make'' program using the rest of the line as arguments
new-ui -- Create a new UI
overlay -- Commands for debugging overlays
overlay auto -- Enable automatic overlay debugging
overlay list-overlays -- List mappings of overlay sections
overlay load-target -- Read the overlay mapping state from the target
overlay manual -- Enable overlay debugging
overlay map-overlay -- Assert that an overlay section is mapped
overlay off -- Disable overlay debugging
overlay unmap-overlay -- Assert that an overlay section is unmapped
shell -- Execute the rest of the line as a shell command
up-silently -- Same as the `up' command
while -- Execute nested commands WHILE the conditional expression is non zero
````

## breakpoints

### Most useful

````
awatch -- Set a watchpoint for an expression
break -- Set breakpoint at specified location
clear -- Clear breakpoint at specified location

delete -- Delete some breakpoints or auto-display expressions
delete bookmark -- Delete a bookmark from the bookmark list
delete breakpoints -- Delete some breakpoints or auto-display expressions
delete display -- Cancel some expressions to be displayed when program stops
save breakpoints -- Save current breakpoint definitions as a script
watch -- Set a watchpoint for an expression
````

### Others

````
break-range -- Set a breakpoint for an address range
catch -- Set catchpoints to catch events
catch assert -- Catch failed Ada assertions
catch catch -- Catch an exception
catch exception -- Catch Ada exceptions
catch exec -- Catch calls to exec
catch fork -- Catch calls to fork
catch handlers -- Catch Ada exceptions
catch load -- Catch loads of shared libraries
catch rethrow -- Catch an exception
catch signal -- Catch signals by their names and/or numbers
catch syscall -- Catch system calls by their names
catch throw -- Catch an exception
catch unload -- Catch unloads of shared libraries
catch vfork -- Catch calls to vfork
commands -- Set commands to be executed when the given breakpoints are hit
condition -- Specify breakpoint number N to break only if COND is true
delete checkpoint -- Delete a checkpoint (experimental)
delete mem -- Delete memory region
delete tracepoints -- Delete specified tracepoints
delete tvariable -- Delete one or more trace state variables
disable -- Disable some breakpoints
disable breakpoints -- Disable some breakpoints
disable display -- Disable some expressions to be displayed when program stops
disable frame-filter -- GDB command to disable the specified frame-filter
disable mem -- Disable memory region
disable pretty-printer -- GDB command to disable the specified pretty-printer
disable probes -- Disable probes
disable type-printer -- GDB command to disable the specified type-printer
disable unwinder -- GDB command to disable the specified unwinder
disable xmethod -- GDB command to disable a specified (group of) xmethod(s)
dprintf -- Set a dynamic printf at specified location
enable -- Enable some breakpoints
enable breakpoints -- Enable some breakpoints
enable breakpoints count -- Enable breakpoints for COUNT hits
enable breakpoints delete -- Enable breakpoints and delete when hit
enable breakpoints once -- Enable breakpoints for one hit
enable count -- Enable breakpoints for COUNT hits
enable delete -- Enable breakpoints and delete when hit
enable display -- Enable some expressions to be displayed when program stops
enable frame-filter -- GDB command to enable the specified frame-filter
enable mem -- Enable memory region
enable once -- Enable breakpoints for one hit
enable pretty-printer -- GDB command to enable the specified pretty-printer
enable probes -- Enable probes
enable type-printer -- GDB command to enable the specified type printer
enable unwinder -- GDB command to enable unwinders
enable xmethod -- GDB command to enable a specified (group of) xmethod(s)
ftrace -- Set a fast tracepoint at specified location
hbreak -- Set a hardware assisted breakpoint
ignore -- Set ignore-count of breakpoint number N to COUNT
rbreak -- Set a breakpoint for all functions matching REGEXP
rwatch -- Set a read watchpoint for an expression
save -- Save breakpoint definitions as a script
save gdb-index -- Save a gdb-index file
save tracepoints -- Save current tracepoint definitions as a script
skip -- Ignore a function while stepping
skip delete -- Delete skip entries
skip disable -- Disable skip entries
skip enable -- Enable skip entries
skip file -- Ignore a file while stepping
skip function -- Ignore a function while stepping
strace -- Set a static tracepoint at location or marker
tbreak -- Set a temporary breakpoint
tcatch -- Set temporary catchpoints to catch events
tcatch assert -- Catch failed Ada assertions
tcatch catch -- Catch an exception
tcatch exception -- Catch Ada exceptions
tcatch exec -- Catch calls to exec
tcatch fork -- Catch calls to fork
tcatch handlers -- Catch Ada exceptions
tcatch load -- Catch loads of shared libraries
tcatch rethrow -- Catch an exception
tcatch signal -- Catch signals by their names and/or numbers
tcatch syscall -- Catch system calls by their names
tcatch throw -- Catch an exception
tcatch unload -- Catch unloads of shared libraries
tcatch vfork -- Catch calls to vfork
thbreak -- Set a temporary hardware assisted breakpoint
trace -- Set a tracepoint at specified location
````
