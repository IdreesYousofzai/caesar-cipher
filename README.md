<img width="800"  alt="image" src="https://github.com/user-attachments/assets/00ff40dc-c64c-49a2-bcc7-69355072e122" />


```markdown
# Caesar Cipher Tool

A lightweight, interactive Python command-line application that encrypts and decrypts text using the classic Caesar Cipher algorithm. 

## Features

* **Dual Modes:** Easily switch between encrypting (encoding) and decrypting (decoding) text.
* **Case Preservation:** Maintains uppercase and lowercase formatting from the original message.
* **Character Safety:** Spaces, punctuation, and numeric characters are left untouched during processing.
* **Input Validation:** Built-in error handling ensures valid operation modes and numeric keys are entered.

---

## How It Works

The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet. For instance, with a shift of 3, `A` becomes `D`, `B` becomes `E`, and so on. 

This script handles wrapping around the alphabet automatically using mathematical modulo operations.

---

## Prerequisites

* Python 3.x installed on your local machine.

## How to Run

1. Clone or download this repository to your local computer.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the program using the following command:

```bash
python caesar_cipher.py

```

---

## Usage Example

```text
--- Caesar Cipher Program ---
Would you like to (E)ncode or (D)ecode? E
Enter your message: Hello, World!
Enter the shift key (number): 3

Result: Khoor, Zruog!

