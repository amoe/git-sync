> This is my sync script.  There are many like it, but this one is mine.

The concept of this script is that a user's regular SSH key may be protected
with a passphrase, which prevents automated use of the key for `git fetch`
operations.  However, if the user also has an key that does not use a
passphrase, they can set up that key in a secure location (with mode `0400` or
similar), and the script will use `sudo` to get the necessary permissions to use
the key.

to set up an hourly sync

    class main::git_sync {
        # Sync every hour.
        cron { 'git_sync':
            ensure => present,
            command => '/usr/local/share/git-sync/git-sync',
            user => amoe,
            minute => 00,
        }
    }

remember to deploy the sync key; it should be deployed with ownership root:root
and permissions `0400`.

rememebr to add the sudo entry

    amoe   ALL = (root) NOPASSWD: /usr/local/share/git-sync/privileged-part

It also needs the cron-notify-send utility.
It relies on cron-notify-send script which needs its own scaffolding.

With inspiration from [simonthum](https://github.com/simonthum/git-sync), sorry
for the name clash.
