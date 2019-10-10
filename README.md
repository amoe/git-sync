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

remember to deploy the sync key

rememebr to add the sudo entry

    amoe   ALL = (root) NOPASSWD: /usr/local/share/git-sync/privileged-part

It also needs the cron-notify-send utility.
