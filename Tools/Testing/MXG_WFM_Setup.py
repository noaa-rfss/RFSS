import pyvisa
import time

PXA_RESOURCE_STRING = 'TCPIP::192.168.2.101::hislip0::INSTR' 
MXG_RESOURCE_STRING = 'TCPIP::192.168.130.66::5025::SOCKET' 
RM = pyvisa.ResourceManager()
INSTR_DIR = 'D:\\Users\\Instrument\\Documents\\BASIC\\data\\WAV\\results\\RFSS\\'

# pyvisa.log_to_screen()

waveforms_15MHz = [
"2-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1698_QPSK.ARB",
"2-1-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1698_QPSK_1PRB_GUARDBAND.ARB",
"2-2-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1698_QPSK_2PRB_GUARDBAND.ARB",
"2-3-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1698_QPSK_3PRB_GUARDBAND.ARB",
"4-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLDFT_ALLPUSCH_1698_QPSK.ARB",
"6-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1702_QPSK.ARB",
"16-1-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1702_QPSK_1PRB_GUARDBAND.ARB",
"6-2-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1702_QPSK_2PRB_GUARDBAND.ARB",
"6-3-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1702_QPSK_3PRB_GUARDBAND.ARB",
"7-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLDFT_ALLPUSCH_1702_QPSK.ARB",
"8-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1707_QPSK.ARB",
"8-1-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1707_QPSK_1PRB_GUARDBAND.ARB",
"8-2-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1707_QPSK_2PRB_GUARDBAND.ARB",
"8-3-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1707_QPSK_3PRB_GUARDBAND.ARB",
"9-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLDFT_ALLPUSCH_1707_QPSK.ARB",
"16-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1701_QPSK_METOP.ARB",
"16-1-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1701_METOP_QPSK_1PRB_GUARDBAND.ARB",
"16-2-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1701_METOP_QPSK_2PRB_GUARDBAND.ARB",
"16-3-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1701_METOP_QPSK_3PRB_GUARDBAND.ARB",
"17-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLDFT_ALLPUSCH_1701_QPSK_METOP.ARB",
"18-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1698_QPSK_PUCCH.ARB",
"19-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_1701_QPSK_METOP_PUCCH.ARB",
"22-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLCP_ALLPUSCH_NONBLANKED.ARB",
"23-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLDFT_ALLPUSCH_NONBLANKED.ARB"
]

# waveforms_5MHz = [
# "1-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLCP_ALLPUSCH_1698_QPSK.ARB"
# "1-1-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLCP_ALLPUSCH_1698_QPSK_1PRB_GUARDBAND.ARB"
# "1-2-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLCP_ALLPUSCH_1698_QPSK_2PRB_GUARDBAND.ARB"
# "1-3-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLCP_ALLPUSCH_1698_QPSK_3PRB_GUARDBAND.ARB"
# "3-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLDFT_ALLPUSCH_1698_QPSK.ARB"
# "5-PUCCH_FORMAT3_STARTSYMBOL0_SYMBOLLENGTH1_PRBSET11TO24_5MHZ_VAR_1698.ARB"
# "10-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLCP_ALLPUSCH_1701_QPSK_METOP.ARB"
# "10-1-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLCP_ALLPUSCH_1701_METOP_QPSK_1PRB_GUARDBAND.ARB"
# "10-2-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLCP_ALLPUSCH_1701_METOP_QPSK_2PRB_GUARDBAND.ARB"
# "10-3-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLCP_ALLPUSCH_1701_METOP_QPSK_3PRB_GUARDBAND.ARB"
# "11-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLDFT_ALLPUSCH_1701_QPSK_METOP.ARB"
# "12-PUCCH_FORMAT3_STARTSYMBOL0_SYMBOLLENGTH14_PRBSET24_5MHZ_VAR_1701_METOP.ARB"
# "13-PUCCH_FORMAT3_STARTSYMBOL0_SYMBOLLENGTH14_PRBSET23TO24_5MHZ_VAR_1701_METOP.ARB"
# "14-PUCCH_FORMAT3_STARTSYMBOL0_SYMBOLLENGTH14_PRBSET24_INTERASLOTHOPPING_5MHZ_VAR_1701_METOP.ARB"
# "15-PUCCH_FORMAT3_STARTSYMBOL0_SYMBOLLENGTH1_PRBSET11TO24_5MHZ_VAR_1701_METOP.ARB"
# "20-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLCP_ALLPUSCH_QPSK_NONBLANKED.ARB"
# "21-5MHZ_SCS15KHZ_3UES_ALLTTI_ALLDFT_ALLPUSCH_QPSK_NONBLANKED.ARB"
# ]

# with RM.open_resource(PXA_RESOURCE_STRING, timeout = 2000) as PXA:
#     # PXA reset/setup
#     pxa_idn = PXA.query('*IDN?')
#     print(f'PXA: {pxa_idn}')

with RM.open_resource(MXG_RESOURCE_STRING, timeout=15000) as MXG:
    MXG.read_termination = '\n'
    MXG.write_termination = '\n'
    
    # MXG reset/setup
    MXG.write('*IDN?')
    mxg_idn = MXG.read()
    print(f'MXG: {mxg_idn}')

    #RMXG Config
    MXG.write('*RST')
    MXG.write('*CLS')

    MXG.write(':FREQ 1702.5 MHZ')
    freq = MXG.query_ascii_values(':FREQ?')
    # print(f'CF: {freq}')

    MXG.write(':POW -60 DBM')
    power = MXG.query_ascii_values(':POW?')
    # print(f'Power: {power}')

    MXG.write(':RAD:ARB 1')
    MXG.write(':OUTP 1')

    # Extract waveform names from the response
    for entry in waveforms_15MHz:
        # print(f'setting up now and sending "{entry}"')

        MXG.write(f':RAD:ARB:WAV "{entry}"')
    # MXG.write(':RAD:ARB:WAV "%s"' % ('17-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLDFT_ALLPUSCH_1701_QPSK_METOP.ARB'))
    # MXG.write('RAD:ARB:WAV "17-15MHZ_SCS15KHZ_9UES_ALLTTI_ALLDFT_ALLPUSCH_1701_QPSK_METOP.ARB"')
        waveform = MXG.query(':RAD:ARB:WAV?')
        print(f'WFM Configured: {waveform}')

        MXG.write(':RAD:ARB:SCL:RATE 23.04 MHZ')
        sampleClock = MXG.query_ascii_values(':RAD:ARB:SCL:RATE?')
        # print(f'Sample Clock: {sampleClock}')

        if MXG.query('*OPC?') == '1':
            MXG.write(':RAD:ARB 1')
            MXG.write(':OUTP 1')
            time.sleep(1)
            continue
        else:
            print("Operation issue")
            break        

    # for entry in waveforms_5MHz:
    #     MXG.write(':FREQ 1702.5 MHZ')
    #     MXG.write(':FREQ?')
    #     MXG.write(':POW -60 DBM')
    #     MXG.write(':POW?')
    #     MXG.write(':RAD:ARB:SCL:RATE 23.04 MHZ')
    #     MXG.write(':RAD:ARB:SCL:RATE?')
    #     MXG.write(f':RAD:ARB:WAV "{entry}"')
    #     MXG.write(':RAD:ARB 1')
    #     MXG.write(':OUTP 1')
    #     pass

