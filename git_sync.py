#! /usr/bin/env python3

import subprocess
import logging
import sys
from logging import info, debug

# SSH based key unlock needs some sort of handling, but it's not clear how.

LOG_PATH = "/home/amoe/ng_annex_sync_log.log"
GIT_DIR = "/home/amoe/ng-annex"
AUTO_COMMIT_MESSAGE = 'automatic commit'
PRIVILEGED_SEGMENT_BINARY_NAME = '/usr/local/share/git-sync/privileged-part'

def git(rest_of_command):
    prefix = ['git', '-C', GIT_DIR]
    prefix.extend(rest_of_command)
    return prefix


class GitSync(object):
    def run(self):
        log_stream = open(LOG_PATH, 'a')

        logging.basicConfig(
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.StreamHandler(log_stream)
            ],
            level=logging.DEBUG,            
            format="%(asctime)s - %(levelname)8s - %(name)s - %(message)s"
        )

        status_output = subprocess.check_output(git(['status', '--porcelain=v1']))

        # If status output is blank, then nothing has changed.
        if status_output:
            subprocess.check_call(git(['add', '-A']), stdout=log_stream, stderr=log_stream)
            subprocess.check_call(git(['commit', '-m', AUTO_COMMIT_MESSAGE]), stdout=log_stream, stderr=log_stream)
        else:
            info("No changes, not committing.")


        subprocess.check_call(['sudo', PRIVILEGED_SEGMENT_BINARY_NAME, 'fetch'], stdout=log_stream, stderr=log_stream)
        subprocess.check_call(git(['merge', '--ff', '--ff-only']), stdout=log_stream, stderr=log_stream)
        subprocess.check_call(['sudo', PRIVILEGED_SEGMENT_BINARY_NAME, 'push'], stdout=log_stream, stderr=log_stream)

        log_stream.close()

try:
    obj = GitSync()
    obj.run()
except Exception as e:
    message = str(e).encode('utf-8')
    subprocess.run(['cron-notify-send', 'git-sync'], input=message)    
