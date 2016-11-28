# TinyPwdMan
A *Tiny Password Manager* for everyone to *Read*, *Understand* and *Trust* 

Created as a Proof of Concept Open-Source project that could be read and understood by its users.
Single File, few line, straightforward features.
The coding style is really golfy as the project has to be as small as possible to fit in a page without scrolling. 

## Usage
``` python
Usage:
	./TinyPwdMan.py key_db_file A|C|E|L [service] [username]
```

## Help
TinyPwdMan is a CLI stateless tool. 
In each run it will decrypt the Key Database file and do 1 of the following:

* `A`: Add new Key.
    You will be prompted for the Service of the logins, the Username and the Password.
* `E`: Edit existing Key specified by `service` argument.
* `L`: List all Keys in a JSON format. Ideal for a quick inspection of your Password Database
* `C`: Copies to clipboard the key pairing with given `service`.


## Contribution
I 'd more than happily check and accept pull requests! If a usable Password Manager needs 40 lines of Python, a great deal of features can be added in 10 more lines!
