#!/usr/bin/env python

import os, shutil

script_path = os.path.realpath(os.path.dirname(__file__))
repo_root = os.path.dirname(script_path)
special_links = os.path.join(script_path, 'special-links.txt')

with open(special_links) as f:
    for line in f:
        line = line.strip()
        if line != '':
            target, link = line.split(' ')
            link = os.path.expanduser(link)
            link_location, link_name = os.path.split(link)
            os.system('mkdir -p ' + link_location)
            target, link_name = os.path.join(repo_root, target), link_name
            try:
                curr_dir = os.getcwd()
                print('ln -s %s %s' % (target, link))
                os.chdir(link_location)
                if os.path.exists(link_name): # back it up
                    print('found {}, backing it up.'.format(link_name))
                    os.rename(link_name, link_name + '-backup')
                os.symlink(target, link_name)
                os.chdir(curr_dir)
            except OSError as e:
                if e.errno==17: # file exists
                    pass
                else:
                    raise
