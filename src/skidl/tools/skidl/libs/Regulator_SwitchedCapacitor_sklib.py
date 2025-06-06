from collections import defaultdict
from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

from skidl.pin import pin_types

SKIDL_lib_version = '0.0.1'

Regulator_SwitchedCapacitor = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'CAT3200', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'CAT3200'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-8_3x3mm_P0.65mm'], 'footprint':'Package_SO:MSOP-8_3x3mm_P0.65mm', 'keywords':'switched capacitor charge pump', 'description':'', 'datasheet':'https://www.onsemi.com/pdf/datasheet/cat3200-d.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nCAT3200\n\nswitched capacitor charge pump', 'pins':[
            Pin(num='1',name='CPOS',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='CNEG',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='PGND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='SGND',func=pin_types.PWRIN,unit=1),
            Pin(num='6',name='~{SHDN}',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='FB',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='VOUT',func=pin_types.PWROUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'CAT3200-5', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'CAT3200-5'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-23-6'], 'footprint':'Package_TO_SOT_SMD:SOT-23-6', 'keywords':'switched capacitor charge pump', 'description':'', 'datasheet':'https://www.onsemi.com/pdf/datasheet/cat3200-d.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nCAT3200-5\n\nswitched capacitor charge pump', 'pins':[
            Pin(num='1',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='~{SHDN}',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='CNEG',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='6',name='CPOS',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LM2665M6', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LM2665M6'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-23-6'], 'footprint':'Package_TO_SOT_SMD:SOT-23-6', 'keywords':'switched capacitor voltage converter doubler splitter', 'description':'', 'datasheet':'https://www.ti.com/lit/ds/symlink/lm2665.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLM2665M6\n\nswitched capacitor voltage converter doubler splitter', 'pins':[
            Pin(num='1',name='V+',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='CAP-',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='SD',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='OUT',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='CAP+',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LM2775DSG', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LM2775DSG'}), 'ref_prefix':'U', 'fplist':['Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias'], 'footprint':'Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias', 'keywords':'Charge pump inductorless', 'description':'', 'datasheet':'https://www.ti.com/lit/gpn/lm2775', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLM2775DSG\n\nCharge pump inductorless', 'pins':[
            Pin(num='1',name='PFM',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='C1-',func=pin_types.PASSIVE,unit=1),
            Pin(num='3',name='C1+',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='OUTDIS',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='EN',func=pin_types.INPUT,unit=1),
            Pin(num='6',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='7',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='8',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='9',name='GND',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LM2776', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LM2776'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-23-6'], 'footprint':'Package_TO_SOT_SMD:SOT-23-6', 'keywords':'Switched capacitor inverter', 'description':'', 'datasheet':'http://www.ti.com/lit/ds/symlink/lm2776.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLM2776\n\nSwitched capacitor inverter', 'pins':[
            Pin(num='1',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='EN',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='C1+',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='C1-',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LM27761', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LM27761'}), 'ref_prefix':'U', 'fplist':['Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm'], 'footprint':'Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm', 'keywords':'low-noise switched capacitor voltage converter invert', 'description':'', 'datasheet':'http://www.ti.com/lit/ds/symlink/lm27761.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLM27761\n\nlow-noise switched capacitor voltage converter invert', 'pins':[
            Pin(num='1',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='CPOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='4',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='5',name='VFB',func=pin_types.INPUT,unit=1),
            Pin(num='6',name='EN',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='C-',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='C+',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='PAD',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LM27762', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LM27762'}), 'ref_prefix':'U', 'fplist':['Package_SON:WSON-12-1EP_3x2mm_P0.5mm_EP1x2.65_ThermalVias'], 'footprint':'Package_SON:WSON-12-1EP_3x2mm_P0.5mm_EP1x2.65_ThermalVias', 'keywords':"Low-noise inverting charge pump with both positive and negative LDO's", 'description':'', 'datasheet':'http://www.ti.com/lit/ds/symlink/lm27762.pdf', 'search_text':"/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLM27762\n\nLow-noise inverting charge pump with both positive and negative LDO's", 'pins':[
            Pin(num='1',name='PGOOD',func=pin_types.OPENCOLL,unit=1),
            Pin(num='10',name='C+',func=pin_types.PASSIVE,unit=1),
            Pin(num='11',name='OUT+',func=pin_types.PWROUT,unit=1),
            Pin(num='12',name='EN+',func=pin_types.INPUT,unit=1),
            Pin(num='13',name='PAD',func=pin_types.PWRIN,unit=1),
            Pin(num='2',name='FB+',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='CP',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='OUT-',func=pin_types.PWROUT,unit=1),
            Pin(num='7',name='FB-',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='EN-',func=pin_types.INPUT,unit=1),
            Pin(num='9',name='C-',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LM7705', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LM7705'}), 'ref_prefix':'U', 'fplist':['Package_SO:VSSOP-8_3x3mm_P0.65mm'], 'footprint':'Package_SO:VSSOP-8_3x3mm_P0.65mm', 'keywords':'switched capacitor voltage converter inverter negative bias regulator', 'description':'', 'datasheet':'http://www.ti.com/lit/ds/symlink/lm7705.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLM7705\n\nswitched capacitor voltage converter inverter negative bias regulator', 'pins':[
            Pin(num='1',name='CF+',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='SD',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='7',name='CRES',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='CF-',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LMC7660', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LMC7660'}), 'ref_prefix':'U', 'fplist':[''], 'footprint':'', 'keywords':'Voltage converter', 'description':'', 'datasheet':'http://www.ti.com/lit/ds/symlink/lmc7660.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLMC7660\n\nVoltage converter', 'pins':[
            Pin(num='1',name='NC',func=pin_types.NOCONNECT,unit=1),
            Pin(num='2',name='CAP+',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='CAP-',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='6',name='LV',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='OSC',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='V+',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LT1054', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LT1054'}), 'ref_prefix':'U', 'fplist':[''], 'footprint':'', 'keywords':'monolithic bipolar switched capacitor voltage converter regulator inverter doubler shutdown', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/1054lfh.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLT1054\n\nmonolithic bipolar switched capacitor voltage converter regulator inverter doubler shutdown', 'pins':[
            Pin(num='1',name='FB/SHDN',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='CAP+',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='CAP-',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='-VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='6',name='VREF',func=pin_types.OUTPUT,unit=1),
            Pin(num='7',name='OSC',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='V+',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LT1054xSW', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LT1054xSW'}), 'ref_prefix':'U', 'fplist':['Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm'], 'footprint':'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'keywords':'monolithic bipolar switched capacitor voltage converter regulator inverter doubler shutdown', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/1054lfh.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLT1054xSW\n\nmonolithic bipolar switched capacitor voltage converter regulator inverter doubler shutdown', 'pins':[
            Pin(num='1',name='FB/SHDN',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='CAP+',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='CAP-',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='-VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='6',name='VREF',func=pin_types.OUTPUT,unit=1),
            Pin(num='7',name='OSC',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='V+',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LTC1044', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LTC1044'}), 'ref_prefix':'U', 'fplist':[''], 'footprint':'', 'keywords':'monolithic CMOS switched capacitor voltage converter invert double divide multiply boost', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/lt1044.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLTC1044\n\nmonolithic CMOS switched capacitor voltage converter invert double divide multiply boost', 'pins':[
            Pin(num='1',name='BOOST',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='CAP+',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='CAP-',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='6',name='LV',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='OSC',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='V+',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LTC1503CMS8-2', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LTC1503CMS8-2'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-8_3x3mm_P0.65mm'], 'footprint':'Package_SO:MSOP-8_3x3mm_P0.65mm', 'keywords':'regulator inductorless', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/1503f.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLTC1503CMS8-2\n\nregulator inductorless', 'pins':[
            Pin(num='1',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='C1-',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='C1+',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='~{SHDN}/SS',func=pin_types.INPUT,unit=1),
            Pin(num='6',name='C2+',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='8',name='C2-',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LTC1751', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LTC1751'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-8_3x3mm_P0.65mm'], 'footprint':'Package_SO:MSOP-8_3x3mm_P0.65mm', 'keywords':'charge pump', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/1751f.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLTC1751\n\ncharge pump', 'pins':[
            Pin(num='1',name='PGOOD/FB',func=pin_types.OUTPUT,unit=1),
            Pin(num='2',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='3',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='C-',func=pin_types.INPUT,unit=1),
            Pin(num='6',name='C+',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='~{SHDN}',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='SS',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LTC1754', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LTC1754'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-23-6'], 'footprint':'Package_TO_SOT_SMD:SOT-23-6', 'keywords':'charge pump', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/175435f.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLTC1754\n\ncharge pump', 'pins':[
            Pin(num='1',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='~{SHDN}',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='CP-',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='6',name='CP+',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LTC660', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LTC660'}), 'ref_prefix':'U', 'fplist':[''], 'footprint':'', 'keywords':'monolithic CMOS switched capacitor voltage converter invert double divide multiply boost', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/660fa.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLTC660\n\nmonolithic CMOS switched capacitor voltage converter invert double divide multiply boost', 'pins':[
            Pin(num='1',name='BOOST',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='CAP+',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='CAP-',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='6',name='LV',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='OSC',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='V+',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MAX1044', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MAX1044'}), 'ref_prefix':'U', 'fplist':[''], 'footprint':'', 'keywords':'monolithic CMOS switched capacitor voltage converter invert double divide multiply boost', 'description':'', 'datasheet':'http://datasheets.maximintegrated.com/en/ds/ICL7660-MAX1044.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nMAX1044\n\nmonolithic CMOS switched capacitor voltage converter invert double divide multiply boost', 'pins':[
            Pin(num='1',name='NC',func=pin_types.NOCONNECT,unit=1),
            Pin(num='2',name='CAP+',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='CAP-',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='6',name='LV',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='OSC',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='V+',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'RT9361AxE', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'RT9361AxE'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-23-6'], 'footprint':'Package_TO_SOT_SMD:SOT-23-6', 'keywords':'Switched capacitor boost', 'description':'', 'datasheet':'https://www.richtek.com/assets/product_file/RT9361A=RT9361B/DS9361AB-14.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nRT9361AxE\n\nSwitched capacitor boost', 'pins':[
            Pin(num='1',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='EN',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='CN',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='6',name='CP',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'TPS60151DRV', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'TPS60151DRV'}), 'ref_prefix':'U', 'fplist':['Package_SON:WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm_ThermalVias'], 'footprint':'Package_SON:WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm_ThermalVias', 'keywords':'charge pump', 'description':'', 'datasheet':'https://www.ti.com/lit/ds/symlink/tps60151.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nTPS60151DRV\n\ncharge pump', 'pins':[
            Pin(num='1',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='2',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='4',name='CP+',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='CP-',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='ENA',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='EP',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'TPS60400DBV', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'TPS60400DBV'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-23-5'], 'footprint':'Package_TO_SOT_SMD:SOT-23-5', 'keywords':'unregulated charge pump inverter variable switching frequency', 'description':'', 'datasheet':'https://www.ti.com/lit/ds/symlink/tps60400.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nTPS60400DBV\n\nunregulated charge pump inverter variable switching frequency', 'pins':[
            Pin(num='1',name='OUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='IN',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='C_{FLY-}',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='C_{FLY+}',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'TPS60500DGS', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'TPS60500DGS'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-10_3x3mm_P0.5mm'], 'footprint':'Package_SO:MSOP-10_3x3mm_P0.5mm', 'keywords':'Regulator Step-Down Charge Pump TPS Texas Instruments Ti', 'description':'', 'datasheet':'http://www.ti.com/lit/ds/symlink/tps60503.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nTPS60500DGS\n\nRegulator Step-Down Charge Pump TPS Texas Instruments Ti', 'pins':[
            Pin(num='1',name='~{EN}',func=pin_types.INPUT,unit=1),
            Pin(num='10',name='FB',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='PG',func=pin_types.OPENCOLL,unit=1),
            Pin(num='3',name='C2-',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='C2+',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='6',name='C1+',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='8',name='C1-',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='GND',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'ICL7660', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'ICL7660'}), 'ref_prefix':'U', 'fplist':['', ''], 'footprint':'', 'keywords':'monolithic CMOS switched capacitor voltage converter invert double divide multiply', 'description':'', 'datasheet':'http://datasheets.maximintegrated.com/en/ds/ICL7660-MAX1044.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nICL7660\n\nmonolithic CMOS switched capacitor voltage converter invert double divide multiply', 'pins':[
            Pin(num='1',name='NC',func=pin_types.NOCONNECT,unit=1),
            Pin(num='2',name='CAP+',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='CAP-',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='6',name='LV',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='OSC',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='V+',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LT1054L', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LT1054L'}), 'ref_prefix':'U', 'fplist':['', ''], 'footprint':'', 'keywords':'monolithic bipolar switched capacitor voltage converter regulator inverter doubler shutdown', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/1054lfh.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLT1054L\n\nmonolithic bipolar switched capacitor voltage converter regulator inverter doubler shutdown', 'pins':[
            Pin(num='1',name='FB/SHDN',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='CAP+',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='CAP-',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='-VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='6',name='VREF',func=pin_types.OUTPUT,unit=1),
            Pin(num='7',name='OSC',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='V+',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LTC1503CMS8-1.8', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LTC1503CMS8-1.8'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-8_3x3mm_P0.65mm', 'Package_SO:MSOP-8_3x3mm_P0.65mm'], 'footprint':'Package_SO:MSOP-8_3x3mm_P0.65mm', 'keywords':'regulator inductorless', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/1503f.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLTC1503CMS8-1.8\n\nregulator inductorless', 'pins':[
            Pin(num='1',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='C1-',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='C1+',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='~{SHDN}/SS',func=pin_types.INPUT,unit=1),
            Pin(num='6',name='C2+',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='8',name='C2-',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LTC1503xS8-1.8', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LTC1503xS8-1.8'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-8_3x3mm_P0.65mm', 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm'], 'footprint':'Package_SO:MSOP-8_3x3mm_P0.65mm', 'keywords':'regulator inductorless', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/1503f.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLTC1503xS8-1.8\n\nregulator inductorless', 'pins':[
            Pin(num='1',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='C1-',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='C1+',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='~{SHDN}/SS',func=pin_types.INPUT,unit=1),
            Pin(num='6',name='C2+',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='8',name='C2-',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LTC1503xS8-2', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LTC1503xS8-2'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-8_3x3mm_P0.65mm', 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm'], 'footprint':'Package_SO:MSOP-8_3x3mm_P0.65mm', 'keywords':'regulator inductorless', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/1503f.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nLTC1503xS8-2\n\nregulator inductorless', 'pins':[
            Pin(num='1',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='C1-',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='C1+',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='~{SHDN}/SS',func=pin_types.INPUT,unit=1),
            Pin(num='6',name='C2+',func=pin_types.INPUT,unit=1),
            Pin(num='7',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='8',name='C2-',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'RT9361BxE', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'RT9361BxE'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-23-6', 'Package_TO_SOT_SMD:SOT-23-6'], 'footprint':'Package_TO_SOT_SMD:SOT-23-6', 'keywords':'Switched capacitor boost', 'description':'', 'datasheet':'https://www.richtek.com/assets/product_file/RT9361A=RT9361B/DS9361AB-14.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nRT9361BxE\n\nSwitched capacitor boost', 'pins':[
            Pin(num='1',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='EN',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='CN',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='6',name='CP',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'TPS60401DBV', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'TPS60401DBV'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-23-5', 'Package_TO_SOT_SMD:SOT-23-5'], 'footprint':'Package_TO_SOT_SMD:SOT-23-5', 'keywords':'unregulated charge pump inverter fixed switching frequency', 'description':'', 'datasheet':'https://www.ti.com/lit/ds/symlink/tps60401.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nTPS60401DBV\n\nunregulated charge pump inverter fixed switching frequency', 'pins':[
            Pin(num='1',name='OUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='IN',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='C_{FLY-}',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='C_{FLY+}',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'TPS60402DBV', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'TPS60402DBV'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-23-5', 'Package_TO_SOT_SMD:SOT-23-5', 'Package_TO_SOT_SMD:SOT-23-5'], 'footprint':'Package_TO_SOT_SMD:SOT-23-5', 'keywords':'unregulated charge pump inverter fixed switching frequency', 'description':'', 'datasheet':'https://www.ti.com/lit/ds/symlink/tps60401.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nTPS60402DBV\n\nunregulated charge pump inverter fixed switching frequency', 'pins':[
            Pin(num='1',name='OUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='IN',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='C_{FLY-}',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='C_{FLY+}',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'TPS60403DBV', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'TPS60403DBV'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-23-5', 'Package_TO_SOT_SMD:SOT-23-5', 'Package_TO_SOT_SMD:SOT-23-5', 'Package_TO_SOT_SMD:SOT-23-5'], 'footprint':'Package_TO_SOT_SMD:SOT-23-5', 'keywords':'unregulated charge pump inverter fixed switching frequency', 'description':'', 'datasheet':'https://www.ti.com/lit/ds/symlink/tps60401.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nTPS60403DBV\n\nunregulated charge pump inverter fixed switching frequency', 'pins':[
            Pin(num='1',name='OUT',func=pin_types.PWROUT,unit=1),
            Pin(num='2',name='IN',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='C_{FLY-}',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='C_{FLY+}',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'TPS60501DGS', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'TPS60501DGS'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-10_3x3mm_P0.5mm', 'Package_SO:MSOP-10_3x3mm_P0.5mm'], 'footprint':'Package_SO:MSOP-10_3x3mm_P0.5mm', 'keywords':'Regulator Step-Down Charge Pump TPS Texas Instruments Ti', 'description':'', 'datasheet':'http://www.ti.com/lit/ds/symlink/tps60503.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nTPS60501DGS\n\nRegulator Step-Down Charge Pump TPS Texas Instruments Ti', 'pins':[
            Pin(num='1',name='~{EN}',func=pin_types.INPUT,unit=1),
            Pin(num='10',name='FB',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='PG',func=pin_types.OPENCOLL,unit=1),
            Pin(num='3',name='C2-',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='C2+',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='6',name='C1+',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='8',name='C1-',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='GND',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'TPS60502DGS', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'TPS60502DGS'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-10_3x3mm_P0.5mm', 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'Package_SO:MSOP-10_3x3mm_P0.5mm'], 'footprint':'Package_SO:MSOP-10_3x3mm_P0.5mm', 'keywords':'Regulator Step-Down Charge Pump TPS Texas Instruments Ti', 'description':'', 'datasheet':'http://www.ti.com/lit/ds/symlink/tps60503.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nTPS60502DGS\n\nRegulator Step-Down Charge Pump TPS Texas Instruments Ti', 'pins':[
            Pin(num='1',name='~{EN}',func=pin_types.INPUT,unit=1),
            Pin(num='10',name='FB',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='PG',func=pin_types.OPENCOLL,unit=1),
            Pin(num='3',name='C2-',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='C2+',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='6',name='C1+',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='8',name='C1-',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='GND',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'TPS60503DGS', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'TPS60503DGS'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-10_3x3mm_P0.5mm', 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'Package_SO:MSOP-10_3x3mm_P0.5mm'], 'footprint':'Package_SO:MSOP-10_3x3mm_P0.5mm', 'keywords':'Regulator Step-Down Charge Pump TPS Texas Instruments Ti', 'description':'', 'datasheet':'http://www.ti.com/lit/ds/symlink/tps60503.pdf', 'search_text':'/usr/share/kicad/symbols/Regulator_SwitchedCapacitor.kicad_sym\nTPS60503DGS\n\nRegulator Step-Down Charge Pump TPS Texas Instruments Ti', 'pins':[
            Pin(num='1',name='~{EN}',func=pin_types.INPUT,unit=1),
            Pin(num='10',name='FB',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='PG',func=pin_types.OPENCOLL,unit=1),
            Pin(num='3',name='C2-',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='C2+',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='6',name='C1+',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='VOUT',func=pin_types.PWROUT,unit=1),
            Pin(num='8',name='C1-',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='GND',func=pin_types.PWRIN,unit=1)], 'unit_defs':[] })])