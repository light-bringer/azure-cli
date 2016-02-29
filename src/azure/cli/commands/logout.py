﻿from .._profile import Profile
from ..commands import command, description, option

@command('logout')
@description(_('Log out from Azure subscription using Active Directory.'))
@option('--username -u <username>', _('User name used to log out from Azure Active Directory.'))
def logout(args, unexpected):
    username = args.get('username')
    if not username:
        raise ValueError(_('Please provide a valid username to logout.'))

    profile = Profile()
    profile.logout(username)