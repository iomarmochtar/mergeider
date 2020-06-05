Merge IDE(r)
============

Inspirated by [Jackobadam's script](https://github.com/jakobadam/kvm-mergeide/) except this script can be used outside kvm (libvirt) systems.

How to use
----------

*Note: Assumming you are using debian/ubuntu based distro for live CD/DVD*

- Install required package.
```bash
apt install libguestfs-tools python3-hivex
```

- Do mount disk where targeted windows inside it, assuming /dev/sda2.
```bash
mkdir /tmp/fixing
mount /dev/sda2 /tmp/fixing
```

- (Additional) if you have error or warning message that indicating the disk are in read-only mode because of unclean shutdown (may happen in windows 10). then use `ntfsfix` to repair it and remount the disk 
```bash
apt install ntfs-3g
ntfsfix /dev/sda2
mount /dev/sda2 /tmp/fixing
```

- Make a backup before injecting registry.
```bash
cp -r /mnt/fixing/Windows/System32/config /mnt/fixing/Windows/System32/config_BAK
```

- Run the injector script
```bash
python reg_generate.py /mnt/fixing/Windows/System32/config/SYSTEM
```

- Execute command that instructed in output of script above to injecting the modified registry file, example:
```bash
hivexregedit  --merge SYSTEM --prefix 'HKEY_LOCAL_MACHINE\SYSTEM' /tmp/regist.reg
```

- Done, the system registry has been patched to use IDE storage.


**Additional:**

You can run following command for debugging purpose to extract the content of hive file:
```
hivexregedit --export /tmp/fixiing/Windows/System32/config/SYSTEM '\'
```