* **1. Types of Files in Linux**

- **Regular file (`-`)** → text, images, programs.
- **Directory (`d`)** → contains files/folders.
- **Symbolic link (`l`)** → shortcut pointing to another file.
- **Character device (`c`)** → data in streams (e.g., `/dev/tty`).
- **Block device (`b`)** → data in blocks (e.g., `/dev/sda`).
- **Socket (`s`)** → interprocess communication (e.g., Docker).
- **FIFO/Pipe (`p`)** → ordered data channel between processes.

Check type: Using `ls -l` (first letter shows type).
EX :
![](ScreenShot/7.png)
All First Letter is == d  --> All File is Directory

---
* **2. Hard Link vs Symbolic Link**

- **Hard link**
    
    - Points to the same inode (real data).
    - Still works if original file is deleted.
    - Same filesystem only.
    - `ln file1 file2`

- **Symbolic link **
    - Points to a file path (like a shortcut).
    - Breaks if original is deleted.
    - Can link across filesystems or to dirs.
    - `ln -s file1 file2`

 Use **hard links** for data redundancy, **symbolic links** for shortcuts/flexibility.

---

* **3. `rmdir` vs `rm -r`**
- **`rmdir`** → removes **empty directories only**.
- **`rm -r`** → removes directories **and all contents** (dangerous).

