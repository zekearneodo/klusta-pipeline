import numpy as np


# applies the transformation of sites to headstage introduced by an adapter
def apply_adapter(a_port_site, adapter):
    '''
    a_port_site: a dictionary with port: site (mapping channels in a headstage to ports in a recording system)
    adapter: n_site x 2 numpy array
            col 0: site in headstage end
            col 1: site in porbe end
    retunrs: new dictionary with port: mapped_site, where mapped_site is the probe site that connects to that channel instead of site
    '''
    new_port_site = {port: adapter[adapter[:, 1] == site][0, 0] for port, site in a_port_site.iteritems()}
    return new_port_site


# n_site x 2 numpy array
# col 0: site in headstage end
# col 1: site in porbe end
site_headstage = {
    'A32-HST32V': np.transpose(np.array([[11, 9, 7, 5, 3, 2, 6, 8, 10, 12,
                                          1, 4, 13, 14, 15, 16,
                                          26, 24, 20, 19, 18, 17,
                                          32, 30, 31, 28, 29, 27, 25, 22, 23, 21],
                                         [1, 2, 3, 4, 6, 8, 10, 12, 14, 16,
                                          5, 7, 9, 11, 13, 15,
                                          21, 23, 25, 27, 29, 31,
                                          17, 18, 19, 20, 22, 24, 26, 28, 30, 32]], dtype=np.int)
                               )}

# dictionary yields port:site
port_site = {
    'paukstis32': {
        'Port_1': 15,
        'Port_2': 6,
        'Port_3': 5,
        'Port_4': 4,
        'Port_5': 16,
        'Port_6': 3,
        'Port_7': 2,
        'Port_8': 1,
        'Port_9': 32,
        'Port_10': 31,
        'Port_11': 30,
        'Port_12': 17,
        'Port_13': 29,
        'Port_14': 28,
        'Port_15': 27,
        'Port_16': 18,
        'Port_17': 13,
        'Port_18': 12,
        'Port_19': 11,
        'Port_20': 10,
        'Port_21': 14,
        'Port_22': 9,
        'Port_23': 8,
        'Port_24': 7,
        'Port_25': 26,
        'Port_26': 25,
        'Port_27': 24,
        'Port_28': 19,
        'Port_29': 23,
        'Port_30': 22,
        'Port_31': 21,
        'Port_32': 20,
    },
    'paukstis16-ec': {
        'Port_1': 14,
        'Port_2': 15,
        'Port_3': 9,
        'Port_4': 16,
        'Port_5': 1,
        'Port_6': 8,
        'Port_7': 2,
        'Port_8': 3,
        'Port_9': 12,
        'Port_10': 11,
        'Port_11': 10,
        'Port_12': 13,
        'Port_13': 4,
        'Port_14': 7,
        'Port_15': 6,
        'Port_16': 5,
    },
    'passaro32-nn': {
        'Port_1': 26,
        'Port_2': 25,
        'Port_3': 24,
        'Port_4': 19,
        'Port_5': 23,
        'Port_6': 22,
        'Port_7': 21,
        'Port_8': 20,
        'Port_9': 18,
        'Port_10': 27,
        'Port_11': 28,
        'Port_12': 29,
        'Port_13': 17,
        'Port_14': 30,
        'Port_15': 31,
        'Port_16': 32,
        'Port_17': 1,
        'Port_18': 2,
        'Port_19': 3,
        'Port_20': 16,
        'Port_21': 4,
        'Port_22': 5,
        'Port_23': 6,
        'Port_24': 15,
        'Port_25': 13,
        'Port_26': 12,
        'Port_27': 11,
        'Port_28': 10,
        'Port_29': 14,
        'Port_30': 9,
        'Port_31': 8,
        'Port_32': 7,
    },
    'passaro16-nn': {
        'Port_1': 13,
        'Port_2': 10,
        'Port_3': 11,
        'Port_4': 12,
        'Port_5': 14,
        'Port_6': 15,
        'Port_7': 9,
        'Port_8': 16,
        'Port_9': 1,
        'Port_10': 8,
        'Port_11': 2,
        'Port_12': 3,
        'Port_13': 5,
        'Port_14': 6,
        'Port_15': 7,
        'Port_16': 4,
    },
    # Port 2 in John Hermiz's Flex-Intan Adapter v2 to rhd164 (upper connector)
    'passaro64-fi2': {
        'Port_16': 2,
        'Port_17': 1,
        'Port_18': 4,
        'Port_19': 3,
        'Port_20': 6,
        'Port_21': 5,
        'Port_22': 8,
        'Port_23': 7,
        'Port_24': 10,
        'Port_25': 9,
        'Port_26': 12,
        'Port_27': 11,
        'Port_28': 14,
        'Port_29': 13,
        'Port_30': 16,
        'Port_31': 15,
        'Port_32': 18,
        'Port_33': 17,
        'Port_34': 20,
        'Port_35': 19,
        'Port_36': 22,
        'Port_37': 21,
        'Port_38': 24,
        'Port_39': 23,
        'Port_40': 26,
        'Port_41': 25,
        'Port_42': 28,
        'Port_43': 27,
        'Port_44': 30,
        'Port_45': 29,
        'Port_46': 32,
        'Port_47': 31,
    }
}
port_site['ibon32'] = port_site['paukstis32']
port_site['bodegh16'] = {'Port_%d' % (i + 1): i + 1 for i in range(16)}
port_site['burung16'] = port_site['bodegh16']

# Burung system with 32 channels trhough amps 2, 3, with no adapter
burung32_No_Adapter = {'Port_%d' % (i + 1 + 16): i + 1 for i in range(32)}

# Buring system with the A32 adapter for neuronexus probes
port_site['burung32-A32-HST32V'] = apply_adapter(burung32_No_Adapter, site_headstage['A32-HST32V'])
port_site['burung32'] = port_site['burung32-A32-HST32V']
