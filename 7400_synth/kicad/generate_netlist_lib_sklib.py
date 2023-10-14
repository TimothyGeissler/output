from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

generate_netlist_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'74LS32', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', '_name':'74LS32', '_match_pin_regex':False, '_aliases':Alias({'74LS32'}), 'datasheet':'http://www.ti.com/lit/gpn/sn74LS32', 'keywords':'TTL Or2', 'description':'Quad 2-input OR', 'value_str':'74LS32', 'ref_prefix':'U', 'num_units':5, 'fplist':['DIP?14*'], 'do_erc':True, 'aliases':Alias({'74LS32'}), 'pin':None, 'footprint':'Package_DIP:DIP-14_W7.62mm', 'pins':[
            Pin(num='14',name='VCC',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='7',name='GND',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='1',name='1A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='2',name='1B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='3',name='1Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='4',name='2A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='5',name='2B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='6',name='2Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='10',name='3B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='8',name='3Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='9',name='3A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='11',name='4Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='12',name='4A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='13',name='4B',func=Pin.types.INPUT,do_erc=True)] }),
        Part(**{ 'name':'74LS00', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', '_name':'74LS00', '_match_pin_regex':False, '_aliases':Alias({'74HC00', '74LS37', '7400', '74LS00', '74HCT00'}), 'datasheet':'http://www.ti.com/lit/gpn/sn74ls37', 'keywords':'TTL nand 2-input buffer', 'description':'quad 2-input NAND buffer', 'value_str':'74LS00', 'ref_prefix':'U', 'num_units':5, 'fplist':['DIP*W7.62mm*', 'SO14*'], 'do_erc':True, 'aliases':Alias({'74HC00', '74LS37', '7400', '74LS00', '74HCT00'}), 'pin':None, 'footprint':'Package_DIP:DIP-14_W7.62mm', 'pins':[
            Pin(num='14',name='VCC',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='7',name='GND',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='1',name='1A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='2',name='1B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='3',name='1Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='4',name='2A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='5',name='2B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='6',name='2Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='10',name='3A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='8',name='3Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='9',name='3B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='11',name='4Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='12',name='4B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='13',name='4A',func=Pin.types.INPUT,do_erc=True)] }),
        Part(**{ 'name':'74LS86', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', '_name':'74LS86', '_match_pin_regex':False, '_aliases':Alias({'74HC86', '74LS86'}), 'datasheet':'74xx/74ls86.pdf', 'keywords':'TTL XOR2', 'description':'Quad 2-input XOR', 'value_str':'74LS86', 'ref_prefix':'U', 'num_units':5, 'fplist':['DIP*W7.62mm*'], 'do_erc':True, 'aliases':Alias({'74HC86', '74LS86'}), 'pin':None, 'footprint':'Package_DIP:DIP-14_W7.62mm', 'pins':[
            Pin(num='1',name='1A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='2',name='1B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='3',name='1Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='4',name='2A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='5',name='2B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='6',name='2Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='10',name='3B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='8',name='3Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='9',name='3A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='11',name='4Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='12',name='4A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='13',name='4B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='14',name='VCC',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='7',name='GND',func=Pin.types.PWRIN,do_erc=True)] })])