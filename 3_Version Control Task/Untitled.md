# **1. Open-Ended Questions – Model Answers**

**Q1. Which type of Git object is used to store the contents of a file and how does it fit into Git’s object model?**

- Git stores file contents in **blob objects**.
    
- Blobs contain the raw data of a file but no filename.
    
- Filenames are stored in **tree objects**, which map names to blob IDs.
    
- Commits then reference trees, creating a hierarchy.
---

**Q2. Git allows configuration at system, global, and local levels. Which level takes priority and why is this design useful?**

- **Priority:** Local > Global > System.
    
- This design is useful because it allows project-specific overrides (local), while still maintaining user-wide defaults (global) and machine-wide defaults (system).
    

---

**Q3. Compare `.gitignore` and `.git/info/exclude`.**

- Both tell Git which files to ignore.
    
- `.gitignore` is tracked and shared with collaborators.
    
- `.git/info/exclude` is local-only and not shared (useful for machine-specific ignores like IDE files).
    

---

**Q4. Difference between `git diff` and `git diff --staged`.**

- `git diff`: shows changes between the working directory and the staging area.
    
- `git diff --staged`: shows changes between the staging area and the last commit.
    
- Example: Before staging → use `git diff`. After staging → use `git diff --staged`.
    

---

**Q5. If you accidentally staged a file, how to remove it from staging but keep changes? Why might this be necessary?**

- Use: `git restore --staged <file>` (or `git reset HEAD <file>`).
    
- This is necessary if you added a file to staging by mistake but still want to keep editing it without committing yet.
    

---

**Q6. Can you alias `git commit` as `git ci`?**

- You **cannot** directly rename built-in commands like `commit`.
    
- But you can create an alias: `git config --global alias.ci commit`.
    
- Then `git ci` will work as a shorthand.
    

---

**Q7. What does `init.defaultBranch` control? Why might teams set it differently?**

- It sets the default branch name when initializing a repo (`main` by default in new Git versions).
    
- Teams may set it to `master`, `develop`, or another standard depending on workflow or legacy practices.
    

---

**Q8. Every commit in Git points to at least one tree object. Explain.**

- A commit object contains metadata (author, message) and a pointer to a **tree object**.
    
- That tree represents the project’s directory snapshot at that point in time.
    
- This is crucial for Git’s snapshot-based versioning.
    

---

**Q9. If you have staged changes in `main` and then switch to a feature branch, what happens? Why?**

- Staged changes **move with you** to the new branch.
    
- Git behaves this way because staging is tied to your working directory, not the branch itself.
    

---

**Q10. Difference between `git switch -c feature` and `git checkout -b feature`. Why was `switch` introduced?**

- Both create and switch to a new branch.
    
- `git switch` is newer and clearer, introduced to reduce confusion (`checkout` is overloaded with many functions).
    
- `switch` is meant just for branch operations.
    

---

# **2. MCQs – Answers**

1. **c) Automatic bug fixing**
    
2. **b) On a single central server**
    
3. **b) Linus Torvalds, 2005**
    
4. **c) git --version**
    
5. **c) Clone**
    
6. **b) Staging area (index)**
    
7. **b) git branch -M main**
    
8. **a) git clone**
    
9. **b) To suggest merging changes from one branch into another**
    
10. **b) Add Peter as a collaborator**
    

---

# **3. Practice Project – Step by Step**

### **1. Setup**

```bash
git init
git config core.editor "nano"        # or vim / code --wait
git config --global alias.st status
```

### **2. First Commit**

```bash
git add .
git commit -m "Initial project structure"

# Explore objects
ls .git/objects
git cat-file -p <hash>    # read blob/tree
```

### **3. Ignore Files**

`.gitignore`

```
*.log
```

Test:

```bash
echo "debug info" > debug.log
git status    # should not show debug.log
```

### **4. New Feature (Branching)**

```bash
git branch feature-math
git switch feature-math
```

Edit `utils/math_utils.py`:

```python
def add(a, b):
    return a + b
```

```bash
git add utils/math_utils.py
git commit -m "Add add() function"
```

### **5. Merging**

```bash
git switch main
git merge feature-math
git log --oneline --graph --all
```

- If `main` has no new commits → fast-forward merge.
    
- If both diverged → 3-way merge.
    

---

### **6. Undo / Unstage**

```bash
# Edit README.md and stage
git add README.md

# Unstage but keep changes
git restore --staged README.md

# Discard changes completely
git restore README.md
```

👉 **Difference**:

- `git restore --staged` → removes from staging only.
    
- `git restore --worktree` → discards working directory changes.
    
- `git rm --cached` → stops tracking file but leaves it in the working directory.
    

---

### **7. Bonus Challenge**

Ignore locally:

```bash
echo "local.txt" >> .git/info/exclude
```

Visualize history:

```bash
git log --oneline --graph --all --decorate
```

---

✅ That covers both the **theory + MCQs + practical project**.

Do you want me to also create a **sample diagram (ASCII log graph)** to show the difference between **fast-forward** and **3-way merge** for Task 5?