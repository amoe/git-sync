> This is my sync script.  There are many like it, but this one is mine.

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
