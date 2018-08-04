
import subprocess
import os
import shutil


SUrl = "https://github.com/goodagood/story.git"

SLoc = "/tmp/story"
TargetFile = "/tmp/some"

SFile= os.path.join(SLoc, "y10m/b.markdown")

print("SUrl, SLoc, Sfile ", SUrl, SLoc, SFile)


cmd_clone = "git clone %s %s"%(SUrl, SLoc)


if os.path.isdir(SLoc):
	print("rm ", SLoc)
	shutil.rmtree(SLoc)

print("clone ", SUrl)
cmd_clone = subprocess.check_output(["git", "clone", SUrl, SLoc])


print('got the file: ', SFile, TargetFile)

#shutil.copyfile(SFile, TargetFile)


