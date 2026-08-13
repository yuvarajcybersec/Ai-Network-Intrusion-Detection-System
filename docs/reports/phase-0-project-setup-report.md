# Phase 0 Report — Project Initialization & GitHub Setup

## Project Title

**AI-Based Network Intrusion Detection System**

## Objective of Phase 0

The objective of this phase was to establish a professional development environment, initialize version control, create a modular project structure, and connect the local Kali Linux workspace with GitHub using secure authentication.

---

## Tasks Completed

### 1. GitHub Repository Creation

A public GitHub repository was created with the name:

`Ai-Network-Intrusion-Detection-System`

Initial repository settings included:

* README.md
* Python `.gitignore`
* MIT License

### 2. Local Repository Setup in Kali Linux

The repository was cloned into the Kali Linux home directory using Git.

```bash
git clone https://github.com/yuvarajcybersec/Ai-Network-Intrusion-Detection-System.git
```

### 3. Git Identity Configuration

Git global username and email were configured for proper commit attribution.

```bash
git config --global user.name "Yuvaraj S"
git config --global user.email "your_email@example.com"
```

### 4. Professional Project Structure Creation

A modular folder structure was designed for scalability and maintainability.

```text
src/
 ├── capture/
 ├── features/
 ├── model/
 ├── detection/
 ├── alerts/
 └── utils/
data/
models/
logs/
tests/
docs/
```

Placeholder Python modules were created for each component.

### 5. Documentation Setup

A professional `README.md` was written containing:

* Project overview
* Features
* Technology stack
* Folder structure
* Development status
* Author information

### 6. Initial Git Commit

The initial project structure was committed locally.

```bash
git add .
git commit -m "Initial project structure and documentation"
```

### 7. GitHub Authentication Troubleshooting

Password-based Git authentication failed because GitHub no longer supports passwords for Git operations. SSH authentication was configured by:

* Generating an ED25519 SSH key
* Starting the SSH agent
* Adding the key to GitHub
* Testing the connection successfully

### 8. Remote Synchronization

The local and remote repositories had divergent histories because both contained initial commits. The histories were merged and synchronized using:

```bash
git pull origin main --allow-unrelated-histories --no-rebase
git push origin main
```

### 9. Verification

Repository synchronization was verified using:

```bash
git status
git log --oneline --graph --all -5
```

The working tree was clean and the local branch was fully synchronized with GitHub.

---

# Technical Skills Learned

## Git & GitHub

* Repository creation
* Cloning repositories
* Staging and committing changes
* Pushing to remote repositories
* Pulling and merging divergent branches
* Reading commit history graphs

## Secure Authentication

* SSH key generation (`ssh-keygen`)
* SSH agent management
* GitHub SSH key configuration
* Remote URL management

## Linux Command-Line Skills

* Directory navigation
* File and folder creation
* Tree visualization
* Git command-line workflow

## Software Engineering Practices

* Modular project organization
* Documentation-first development
* Version-controlled incremental development
* Professional repository structuring

---

# Problems Encountered and Solutions

| Problem                                     | Solution                                  |
| ------------------------------------------- | ----------------------------------------- |
| GitHub password authentication failed       | Configured SSH authentication             |
| Remote repository already contained commits | Pulled with `--allow-unrelated-histories` |
| Push rejected due to non-fast-forward       | Merged histories and pushed again         |

---

# Outcome of Phase 0

At the end of Phase 0, a fully functional and professionally organized GitHub project was established. The repository is securely connected to the Kali Linux development environment, version control is operational, and the project is ready for implementation phases.

---

# Key Takeaways

* Modern GitHub workflows use SSH or personal access tokens instead of passwords.
* A clean project structure is essential before writing code.
* Frequent commits improve traceability and professionalism.
* Understanding Git merge workflows is an important developer skill.
* Documentation should be treated as a core project artifact, not an afterthought.

---

# Next Phase

**Phase 1 — Kali Environment Setup and Packet Capture Preparation**

This phase will include:

* Python virtual environment creation
* Dependency installation
* Wireshark and tcpdump configuration
* Network interface identification
* First live packet capture using Kali Linux.
