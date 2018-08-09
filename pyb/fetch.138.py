
import subprocess
import shlex
#import requests as req


sand_story = 'https://github.com/goodagood/story/blob/master/y10m/b.markdown'
git = 'https://github.com/goodagood/story.git'

tmp_folder = "/tmp/story"

src_file = "/tmp/story/y10m/b.markdown"
tgt_folder   = "/tmp/"

clone_cmd = "git clone -- %s %s"%(git, tmp_folder)

cp_cmd  = "cp %s %s"%(src_file, tgt_folder)

ls_cmd = "ls -l"


try:
    rm_cmd = "rm -rf /tmp/story"
    args = shlex.split(rm_cmd)
    print('remove possible cloned repo.', args)
    subprocess.call(args)
except:
    print('nothing to delete before clone')
    pass

print(clone_cmd)
args = shlex.split(clone_cmd)

# why the following fails?
#subprocess.call(args, shell=True)
#subprocess.call(['git', 'clone', git, tmp_folder], shell=True)
#co = subprocess.check_output(['git', 'clone', git, tmp_folder], shell=True)

co = subprocess.call(args)



try:
    subprocess.call(shlex.split(cp_cmd))
    print(cp_cmd)
except:
    print('cp failed ', cp_cmd)
