# DarkForce

DarkForce is a Python-based brute-force password cracking tool designed to break password-protected PDF, ZIP, RAR, and Microsoft Office files. It also supports hash cracking and dictionary-based attacks.

## Features
- **Brute Force Attack**: Generates and tests passwords systematically.
- **Dictionary Attack**: Uses a predefined list of passwords.
- **Random Password Generation**: Generates passwords based on given character sets and lengths.
- **Hash Cracking**: Supports MD5, SHA1, SHA224, SHA256, SHA384, SHA512, BLAKE2b, and BLAKE2s hash types.
- **File Decryption**: Cracks password-protected PDF, ZIP, RAR, and MS Office files.

## Installation
### Prerequisites
Ensure you have Python 3 installed along with the following dependencies:
```sh
pip install pdfplumber colorama chardet rarfile msoffcrypto-tool
```

## Usage
Run the script:
```sh
python3 DarkForce.py
```

### Options
Upon execution, select the attack method:
1. **Brute Force Attack**
   - Select the file type: PDF, RAR, ZIP, MS Office, or Hash.
   - Enter the character set, minimum and maximum password length.
   - The script will attempt to brute-force the password.
2. **Dictionary Attack**
   - Provide a dictionary file.
   - The script will test passwords from the file.
3. **Random Password Generation**
   - Generate and test random passwords.

## Example Commands
- **Brute-force a ZIP file:**
  ```
  Enter ZIP file path: secret.zip
  Enter character set: abc123
  Enter min password length: 4
  Enter max password length: 6
  ```
- **Dictionary attack on a PDF file:**
  ```
  Enter PDF file path: document.pdf
  Enter dictionary file path: passwords.txt
  ```

## Disclaimer
This tool is for educational and ethical use only. Use it only on files and systems you have explicit permission to test. Misuse may lead to legal consequences.

## Author
**Riya Mishra**

## License
This project is licensed under the GNU General Public License 3.0

