# GPG 

# Key Usage

Generate:
> gpg --full-gen-key

Export:
> gpg --export --a <email> > public.key

Import someone else's key:
> gpg --import public.key


Encrypt a file for a specific recipient

> gpg --recipient <user-id> --encrypt <file>


Encrypt a file with a password

> gpg --symetric file

Decrypt a file 

> gpg --output <file> --decrypt <file.gpg>

Site that hosts gpg keys: keys.openpgp.org 

https://users.ece.cmu.edu/~adrian/630-f04/PGP-intro_files/fig1-6.gif
