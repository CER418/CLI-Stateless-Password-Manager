# CLI Stateless Password Manager

## Why passwords matter

Once in a while data leaks occur. It can happen as companies or systems does not follow best practises, nor
manage to follow up on the latest vulnerabilities. Password has been used since the earliest days of
computing. Although the development of security standards is constantly changing and improving, the
principles and use of passwords remain mostly the same. To minimise the attack surface of the various
services one use, a good practise is using unique passwords.</p>

### Documentation
`python main.py --help`

Available options:

`-s, --site TEXT`

`-u, --username TEXT`

`-l, --length INTEGER`

`-d, --digest [SHA1|SHA224|SHA256|SHA384|SHA512]`

There are several options for creating passwords. One can specify the url or site name of the web page
the password is intended to be used on. It is also possible to specify a desired password length given that
the hash itself is long enough.

### Examples
`python main.py -s google -l 16`

`python main.py -s github -u gh -l 8 -d SHA512`

### Contribute
We are open to suggestions and want to improve the project! Whether you want to submit a PR or help
translating the application, all help is appreciated.

### Contact
Feel free to contact me with cheers or jeers!

www.cspm.martinfidjeland.com

### References

- [Lesspass](https://www.lesspass.com/)
- [Hashlib library](https://docs.python.org/3/library/hashlib.html)