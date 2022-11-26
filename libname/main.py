import click
import xerox
import hashlib
import getpass


@click.command()
@click.option('--site', '-s', required=False, help='E.g. google.com')
@click.option('--username', '-u', required=False, help='E.g. sam')
@click.option('--length', '-l', default=8, show_default=True)
@click.option('--digest', '-d', default='SHA1', show_default=True,
              type=click.Choice(['SHA1', 'SHA224', 'SHA256', 'SHA384', 'SHA512'], case_sensitive=False))
def run(length=8, site=str(), username=str(), digest='SHA1'):
    """Stateless password manager that can generated passwords on the go 🍺
    Both site and username are optional, but has to be remembered in order to reproduce the hash digest if used."""
    password = getpass.getpass('Password: ')
    if password:
        if length or site or username:
            password_string = ''.join(filter(None, [site, username, password]))
            return magic(length, digest, password_string)
    click.secho("Something went wrong 🥴", fg='red', bold=True)


def magic(length, digest, string):
    encoded = string.encode('ascii')
    match digest:
        case 'SHA1':
            xerox.copy(hashlib.sha1(encoded).hexdigest()[:length])
        case 'SHA224':
            xerox.copy(hashlib.sha224(encoded).hexdigest()[:length])
        case 'SHA256':
            xerox.copy(hashlib.sha256(encoded).hexdigest()[:length])
        case 'SHA384':
            xerox.copy(hashlib.sha384(encoded).hexdigest()[:length])
        case 'SHA512':
            xerox.copy(hashlib.sha512(encoded).hexdigest()[:length])
    click.secho('Hash digest is copied to clipboard ✨', fg='bright_green', bold=True)


if __name__ == '__main__':
    run()
