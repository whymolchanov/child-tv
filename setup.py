import os
import subprocess

with open("/etc/fstab", "a") as fstab:
    fstab.write("/dev/sda1 /mnt/child-tv auto defaults 0 1")

os.mkdir("/mnt/child-tv")

subprocess.call(["mount", "-a"])
