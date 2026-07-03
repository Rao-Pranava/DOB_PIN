# DOB_PIN
Generate upto 16 Digit Pin using combinations of multiple Date of Births


> Every PIN has a story. Sometimes, it starts with a birthday.

**DOB_PIN** is a lightweight Python utility that generates possible PIN combinations from the Date of Birth (DOB) of one or more individuals. It builds a pool of date fragments and can generate base combinations, cyclic rotations, or every unique permutation for a chosen PIN length.

Built for security research, password awareness, and demonstrating how predictable human-chosen PINs can be.

## Disclaimer

This project is intended **strictly for educational purposes, cybersecurity awareness, security research, and authorized penetration testing**.

The tool demonstrates how predictable information—such as dates of birth—can be used to generate potential PIN combinations. It is designed to help security professionals, students, and organizations understand the risks of weak or personally derived PINs.

The author assumes **no responsibility** for any misuse of this software. You are solely responsible for ensuring that your use of this tool complies with all applicable laws, regulations, and authorization requirements.

**Only use this tool on systems, accounts, or data that you own or have explicit permission to test.**

---

# Prerequisite

1. Clone the repository on to your system using `git`.
```
git clone https://github.com/Rao-Pranava/DOB_PIN.git
```


2. Go into the Directory and create a python virtual environment (optional, but recommended)
```
cd DOB_PIN && python3 -m venv .venv
```
*Make sure you have `python3-venv` installed for this step to work*

> To install python venv:
> ```
> sudo apt update && sudo apt install python3-venv
> ```

3. Activate the virtual environment
```
source .venv/bin/activate
```

4. Install `tqdm` library
```
pip install tqdm
```

# Run the Tool:

```
python3 DOBPINGEN.py
```
*On screen instructions will guide*

<img width="940" height="1442" alt="image" src="https://github.com/user-attachments/assets/2cf0fab0-468f-4b92-b076-a05b5fb1ec39" />

## Permutation Modes

The tool supports three different generation modes depending on how exhaustive you want the output to be.

### 1. Base Combinations Only
Generates the PIN exactly as it is formed from the extracted DOB fragments without any modifications.

**Example**
```
Input : 0207
Output:
0207
```

---

### 2. Cyclic Rotations
Generates every cyclic rotation of the generated PIN by shifting the digits while preserving their order.

**Example**
```
Input : 0207
Output:
0207
2070
0702
7020
```

---

### 3. All Unique Permutations *(Default)*
Generates every unique arrangement of the digits in the generated PIN. This mode produces the largest number of possible PINs and is useful for demonstrating the full search space of DOB-derived PINs.

**Example**
```
Input : 0207
Output:
0027
0072
0702
0720
0207
0270
...
```

> **Note:** Duplicate permutations caused by repeated digits (e.g., two `0`s) are automatically removed, so only unique PINs are saved.
---
