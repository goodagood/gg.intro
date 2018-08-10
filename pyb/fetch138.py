
#
# Copy from fetch.138.py, which is testing and file name not regular.
# 2018 August 10
#


import subprocess
import shlex
#import requests as req


def hard_coded_story_clone(target_file_name):

    sand_story = 'https://github.com/goodagood/story/blob/master/y10m/b.markdown'
    git = 'https://github.com/goodagood/story.git'

    tmp_folder = "/tmp/story"

    src_file = "/tmp/story/y10m/b.markdown"
    tgt_folder   = "/tmp/"

    clone_cmd = "git clone -- %s %s"%(git, tmp_folder)

    #cp_cmd  = "cp %s %s"%(src_file, tgt_folder)
    cp_cmd  = "cp %s %s"%(src_file, target_file_name)

    ls_cmd = "ls -l"


    try: # remove old clone
        rm_cmd = "rm -rf /tmp/story"
        args = shlex.split(rm_cmd)
        print('remove possible cloned repo.', args)
        subprocess.call(args)
    except:
        print('nothing to delete before clone')
        pass


    try: # clone
        print(clone_cmd)
        args = shlex.split(clone_cmd)

        subprocess.call(args)

        # why the following fails?
        #subprocess.call(args, shell=True)
        #subprocess.call(['git', 'clone', git, tmp_folder], shell=True)
        #co = subprocess.check_output(['git', 'clone', git, tmp_folder], shell=True)

    except:
        print('clone failed, ', clone_cmd) 
        pass



    try:
        subprocess.call(shlex.split(cp_cmd))
        print(cp_cmd)
    except:
        print('cp failed ', cp_cmd)



if __name__ == "__main__":
    hard_coded_story_clone('/tmp/mdhtml/b.md')

