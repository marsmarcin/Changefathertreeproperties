# by FYJ

import xml.dom.minidom
import os

path='F://changeftpro//Changefathertreeproperties//d//'
sv_path='F://changeftpro//Changefathertreeproperties//e//'
files=os.listdir(path)
for xmlFile in files:
    dom=xml.dom.minidom.parse(os.path.join(path,xmlFile))
    root=dom.documentElement
    item=root.getElementsByTagName('name')
    for i in item:
        if(i.firstChild.data=='Pin_1st_0x01'):
            i.firstChild.data='Pin'
        if(i.firstChild.data=='Pin_1st_0x02'):
            i.firstChild.data='Pin'
        if(i.firstChild.data=='Pin_1st_0x03'):
            i.firstChild.data='Pin'
        if(i.firstChild.data=='Pin_1st_0x0F'):
            i.firstChild.data='Pin'
        if(i.firstChild.data=='Pin_2nd_0x01'):
            i.firstChild.data='Pin'
        if(i.firstChild.data=='Pin_2nd_0x02'):
            i.firstChild.data='Pin'
        if(i.firstChild.data=='Pin_2nd_0x03'):
            i.firstChild.data='Pin'
        if(i.firstChild.data=='Pin_2nd_0x0F'):
            i.firstChild.data='Pin'
        if(i.firstChild.data=='Insulator_1st_0x01'):
            i.firstChild.data='Insulator'
        if(i.firstChild.data=='Insulator_1st_0x02'):
            i.firstChild.data='Insulator'
        if(i.firstChild.data=='Insulator_1st_0x03'):
            i.firstChild.data='Insulator'
        if(i.firstChild.data=='Insulator_1st_0x0F'):
            i.firstChild.data='Insulator'
        if(i.firstChild.data=='Insulator_2nd_0x01'):
            i.firstChild.data='Insulator'
        if(i.firstChild.data=='Insulator_2nd_0x02'):
            i.firstChild.data='Insulator'
        if(i.firstChild.data=='Insulator_2nd_0x0F'):
            i.firstChild.data='Insulator'
        if(i.firstChild.data=='StrandedWire_0x01'):
            i.firstChild.data='StrandedWire'
        if(i.firstChild.data=='StrandedWire_0x02'):
            i.firstChild.data='StrandedWire'
        if(i.firstChild.data=='StrandedWire_0x0F'):
            i.firstChild.data='StrandedWire'
    with open(os.path.join(sv_path,xmlFile),'w') as fh:
        dom.writexml(fh)
