
1. **What happens step by step when you type a command in bash (e.g., `ls`) until you see the output?**

- **Read:** The shell (bash) reads your command line.
- **Parse:** Bash parses the command, expands variables, wildcards, etc.
- **Search:** Bash searches `$PATH` for the binary `ls`.
- **Fork:** Bash creates a child process (using the `fork()` syscall).
- **Exec:** The child process replaces itself with the `ls` program (via `execve()` syscall).
- **Kernel:** Kernel gives CPU time, manages memory, and handles I/O.
- **Output:** `ls` writes to stdout (terminal).
- **Wait:** Bash waits for the process to finish, then shows a new prompt.

---

2. **Explain the types of processes in Linux: daemon, zombie, orphan. How can you detect them?**
- **Daemon:**
    - Background service, usually started at boot.
    - often managed by systemd, names often end with d, PPID=1
    - Detect: `ps aux | grep daemon`

- **Zombie:**
    - A process finished execution but its parent has not read its exit status.
    - Shows as `Z` in `ps`.
    - Detect: `ps aux | grep Z`

- **Orphan:**
    - A process whose parent terminated before it did.
    - Orphans get adopted by `init` (`systemd`).
    - Detect: `ps -o ppid= -p <PID>` (PPID=1 means orphan).


---

3. **Why do we need Inter-Process Communication (IPC)? List some IPC mechanisms and real-life examples.**

- Processes often need to share data, coordinate tasks, or send signals. IPC provides a structured way for them to communicate.

- **IPC mechanisms:**
    
    - **Pipes:** Unidirectional channel (`ls | grep txt`).
    - **Signals:** Notifications (`kill -TERM PID`).
    - **Message Queues:** Structured message passing.
    - **Shared Memory:** Fast data sharing in RAM.
    - **Sockets:** Communication across networks.

- **Real-life examples:**    
    - Web server and browser → sockets.
    - Shell pipelines → Pipes ( | ) → connect output of one process to input of another.
    - Logging daemons → message queues.
    - Multimedia apps → shared memory for video frames.
