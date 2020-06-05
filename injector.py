__author__ = 'Imam Omar Mochtar (iomarmochtar@gmail.com)'

import hivex
import sys
import tempfile
from string import Template

REG_TEMPLATE = """Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\primary_ide_channel]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="atapi"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\secondary_ide_channel]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="atapi"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\*pnp0600]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="atapi"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\*azt0502]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="atapi"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\gendisk]
"ClassGUID"="{4D36E967-E325-11CE-BFC1-08002BE10318}"
"Service"="disk"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#cc_0101]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_0e11&dev_ae33]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_1039&dev_0601]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_1039&dev_5513]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_1042&dev_1000]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_105a&dev_4d33]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_1095&dev_0640]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_1095&dev_0646]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_1095&dev_0646&REV_05]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_1095&dev_0646&REV_07]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_1095&dev_0648]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_1095&dev_0649]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_1097&dev_0038]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_10ad&dev_0001]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_10ad&dev_0150]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_10b9&dev_5215]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_10b9&dev_5219]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_10b9&dev_5229]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="pciide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_1106&dev_0571]
"Service"="pciide"
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_8086&dev_1222]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="intelide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_8086&dev_1230]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="intelide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_8086&dev_2411]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="intelide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_8086&dev_2421]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="intelide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_8086&dev_7010]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="intelide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_8086&dev_7111]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="intelide"

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CriticalDeviceDatabase\pci#ven_8086&dev_7199]
"ClassGUID"="{4D36E96A-E325-11CE-BFC1-08002BE10318}"
"Service"="intelide"

;Add driver for Atapi (requires Atapi.sys in Drivers directory)

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Services\atapi]
"ErrorControl"=dword:00000001
"Group"="SCSI miniport"
"Start"=dword:00000000
"Tag"=dword:00000019
"Type"=dword:00000001
"DisplayName"="Standard IDE/ESDI Hard Disk Controller"
"ImagePath"=hex(2):53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,44,00,\ 
  52,00,49,00,56,00,45,00,52,00,53,00,5c,00,61,00,74,00,61,00,70,00,69,00,2e,\ 
  00,73,00,79,00,73,00,00,00

;Add driver for intelide (requires intelide.sys in drivers directory)

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Services\IntelIde]
"ErrorControl"=dword:00000001
"Group"="System Bus Extender"
"Start"=dword:00000000
"Tag"=dword:00000004
"Type"=dword:00000001
"ImagePath"=hex(2):53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,44,00,\ 
  52,00,49,00,56,00,45,00,52,00,53,00,5c,00,69,00,6e,00,74,00,65,00,6c,00,69,\ 
  00,64,00,65,00,2e,00,73,00,79,00,73,00,00,00


;Add driver for Pciide (requires Pciide.sys and Pciidex.sys in Drivers directory)

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Services\PCIIde]
"ErrorControl"=dword:00000001
"Group"="System Bus Extender"
"Start"=dword:00000000
"Tag"=dword:00000003
"Type"=dword:00000001
"ImagePath"=hex(2):53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,44,00,\ 
  52,00,49,00,56,00,45,00,52,00,53,00,5c,00,70,00,63,00,69,00,69,00,64,00,65,\ 
  00,2e,00,73,00,79,00,73,00,00,00

;Enable minidump

[HKEY_LOCAL_MACHINE\SYSTEM\$cset\Control\CrashControl]
"AutoReboot"=dword:00000000
"CrashDumpEnabled"=dword:00000003
"DumpFile"=str(2):"%SystemRoot%\MEMORY.DMP"
"LogEvent"=dword:00000001
"MinidumpDir"=str(2):"%SystemRoot%\Minidump"
"MinidumpsCount"=dword:00000032
"Overwrite"=dword:00000001
"""

class HivexManager(object):
    
    def __init__(self, path, write=False, debug=False):
        self.path = path
        self.cntx = hivex.Hivex(path, write=write, debug=debug)
        self.root_id = self.cntx.root()

    @property
    def current_control(self):
        node = self.cntx.node_get_child(self.root_id, "Select")
        val = self.cntx.node_get_value(node, "Current")
        return "ControlSet%03d" % self.cntx.value_dword(val)

    def get_children(self, key):
        children = self.cntx.node_children(key)
        result = []
        for child in children:
            name = self.cntx.node_name(child)
            sub_chld = self.cntx.node_children(child) 
            result.append({
                'name': name,
                'has_child': True if len(sub_chld) > 0 else False,
                'node_id': child
            })

        return result

    def save(self, path=None):
        self.cntx.commit(path if path else self.path)

    def close(self):
        self.cntx.close()

    def add_child(self, parent_id, node):
        self.cntx.node_add_child(parent_id, node)

    def get_nodeid_by_path(self, location):
        # search from root node
        paths = [ x.lower() for x in location.split('\\') ]
        childrens = self.get_children(self.root_id)
        path_count = 0
        for path in paths:
            path_count += 1
            next_chld_id = None

            for chld in childrens:
                if path_count == len(paths) and path == chld['name'].lower():
                    return chld['node_id']

                if path_count < len(paths) and path == chld['name'].lower():
                    next_chld_id = chld['node_id']

            if next_chld_id:
                childrens = self.get_children(next_chld_id)
            else:
                break
        return None

class Injector():

    def __init__(self, hive_path):
        self.path = hive_path
        self.mgr = HivexManager(hive_path, write=True)
        self.temp_registry = tempfile.mktemp('mergeide')
        self.current_control = self.mgr.current_control

    @property
    def hivexregedit(self):
        return "hivexregedit  --merge {} --prefix 'HKEY_LOCAL_MACHINE\SYSTEM' {}".format(self.path, self.temp_registry)

    def write_registry(self):
        with open(self.temp_registry, 'w') as fh:
            registry = Template(REG_TEMPLATE)
            #fh.write(REG_TEMPLATE % {'cset': self.current_control})
            fh.write(registry.substitute(cset=self.current_control))

    def log(self, txt):
        b = '=' * 3
        print('{} {} {}'.format(b, txt.upper(), b))

    def ensure_node(self, parent, node_name):
        parent_node = '{}\{}'.format(self.current_control, parent)
        child_node = '{}\{}'.format(parent_node, node_name)

        self.cntr = self.mgr.current_control
        control = 'ControlSet001\Control'
        crit = 'CriticalDeviceDatabase'
        critical_device = '{}\{}'.format(control, crit)
        
        #test = 'ControlSet001\Control\CriticalDeviceDatabase'
        control_id = self.mgr.get_nodeid_by_path(control)

        parent_id = self.mgr.get_nodeid_by_path(parent_node)
        if parent_id:
            child_nodeid = self.mgr.get_nodeid_by_path(child_node)
            if not child_nodeid:
                self.log('{} not exists, create it'.format(child_node))
                self.mgr.add_child(parent_id, node_name)
                self.mgr.save()


    def main(self):

        self.log('writing to temporary registry')
        self.write_registry()

        self.log('Ensuring node CriticalDeviceDatabase')
        self.ensure_node('Control', 'CriticalDeviceDatabase')

        self.log('Ensuring node Services\PCIIde')
        self.ensure_node('Services', 'PCIIde')

        self.log('Run following command')
        print(self.hivexregedit)
   
if __name__ == '__main__':
    import sys

    obj = Injector(sys.argv[1])
    obj.main()