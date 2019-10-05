#! /usr/bin/python3

import subprocess
import os
import sys

# sudo wrapper for privileged operations

command = sys.argv[1]
print(command)

NG_ANNEX_LOCATION = '/home/amoe/ng-annex'
PRECIOUS_KEY_LOCATION = '/home/amoe/PRECIOUS.pem'
my_env = os.environ.copy()
my_env['GIT_SSH_COMMAND'] = 'ssh -l amoe -o PasswordAuthentication=no -o IdentitiesOnly=yes -i {}'.format(PRECIOUS_KEY_LOCATION)

def reassign_ownership():
    subprocess.check_call(['chown', '-R', 'amoe:amoe', NG_ANNEX_LOCATION])

if command == 'fetch':
    subprocess.check_call(['git', '-C', NG_ANNEX_LOCATION, 'fetch'], env=my_env)
    reassign_ownership()
elif command == 'push':
    subprocess.check_call(['git', '-C', NG_ANNEX_LOCATION, 'push'], env=my_env)
    reassign_ownership()
else:
    raise Exception("bad request")
