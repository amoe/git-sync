Think about this.

If it runs as my user, then we can't have the un-passphrased key around
anywhere.
Because, the attacker would not have to authenticate as me.
So anything I can access, he can access too.

Cron can't access the ssh-agent by default.
What we should really do is send a notification if the key is unlocked.
But that would probably get annoying.
It would be much better to just never ask.

If we store the 

dotfiles default_identity parameter handles the various things

Maybe we should make it root-accessible.

You can do this using something as such.

amoe@steenvlieg $ sudo ssh -F /dev/null -o IdentitiesOnly=yes -i PRECIOUS.pem -o PasswordAuthentication=no -vv amoe@visarend.solasistim.net                                                    3.03s 

foo;;

GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" git clone user@host

If we do the ssh checkout as root, we'd have to chown it afterward
