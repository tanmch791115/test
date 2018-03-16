# _*_ coding:utf-8_*_
# coding=utf-8

import os
import shutil
import time
import bz2

HTB_Home = 'D:' + os.sep + 'htb'
Cast_Home = 'D:' + os.sep + 'castdata'
CCTV_Home = 'D:' + os.sep + 'cctvdata'
Dest_Home = 'D:' + os.sep + 'weatherdata'
TaskList = ['NWP_KWBC_GLB_CASTDATA',
            'NWP_KWBC_GLB_CCTVDATA',
            'NWP_CLDAS',
            'NWP_ECMF_DAM',
            'NWP_ECMF_GLB_CASTDATA',
            'NWP_ECMF_GLB_CCTVDATA',
            'NWP_EDZW_GLB_CASTDATA',
            'NWP_EDZW_GLB_CCTVDATA',
            'NWP_JMA_GSM',
            'NWP_NCC_CLFC',
            'NWP_NWP_KJ_QuanQiu',
            'NWP_NWP_KJ_QuYu',
            'NWP_NWP_ZC_T799',
            'NWP_NWP_NMC_GEPS',
            'NWP_NWP_NMC_GRAPES0048',
            'NWP_NWP_NMC_GRAPES54',
            'NWP_NWP_NMC_GRAPES60',
            'NWP_NWP_NMC_REPS',
            'NWP_NWP_NMC_T639G0072',
            'NWP_NWP_NMC_T639G7296',
            'NWP_NWP_NMC_T639G96120',
            'NWP_NWP_NMC_T639G120',
            'NWP_NWP_NMC_T639R0072',
            'NWP_NWP_NMC_T639R7296',
            'NWP_NWP_NMC_T639R96120',
            'NWP_NWP_NMC_T639R120',
            'NWP_RJTD_GLB_CASTDATA',
            'NWP_RJTD_GLB_CCTVDATA',
            'OBS_OBS_DOM_ARMY',
            'OBS_OBS_DOM_AWS_BCGZ',
            'OBS_OBS_DOM_AWS_BECS',
            'OBS_OBS_DOM_AWS_BEFZ',
            'OBS_OBS_DOM_AWS_BEGY',
            'OBS_OBS_DOM_AWS_BEHK',
            'OBS_OBS_DOM_AWS_BEKM',
            'OBS_OBS_DOM_AWS_CMA',
            'OBS_OBS_DOM_HANGWEI_KongSi',
            'OBS_OBS_DOM_HANGWEI_ZhongCan',
            'OBS_OBS_DOM_HTB_fromCAST',
            'OBS_OBS_DOM_HTB_fromCCTV',
            'OBS_OBS_DOM_MINHANG_GuanCe',
            'OBS_OBS_DOM_MINHANG_YuBao',
            'OBS_OBS_DOM_OCEN_CHUANBO',
            'OBS_OBS_DOM_OCEN_FUBIAO',
            'OBS_OBS_DOM_OCEN_HAIYANGZHAN',
            'OBS_OBS_DOM_OCEN_OCEN',
            'OBS_OBS_DOM_RIVER_GATE',
            'OBS_OBS_DOM_RIVER_PPTN',
            'OBS_OBS_DOM_RIVER_RIVER',
            'OBS_OBS_DOM_RIVER_RSVR',
            'OBS_OBS_DOM_RIVER_TIDE',
            'OBS_OBS_DOM_RIVER_WAS',

            'OBS_OBS_DOM_UPAR_CMA',
            'OBS_OBS_DOM_UPAR_META',
            'OBS_OBS_DOM_WRPD',
            'OBS_OBS_DOM_CAWN',
            'OBS_OBS_DOM_LPD',

            'RADA_RADA_NOR_fromCCTV',
            'RADA_RADA_NOR_fromCAST',
            'RADA_RADA_BCGZ_Z9200',
            'RADA_RADA_BCGZ_Z9660',
            'RADA_RADA_BCGZ_Z9662',
            'RADA_RADA_BCGZ_Z9751',
            'RADA_RADA_BCGZ_Z9753',
            'RADA_RADA_BCGZ_Z9754',
            'RADA_RADA_BCGZ_Z9755',
            'RADA_RADA_BCGZ_Z9758',
            'RADA_RADA_BCGZ_Z9759',
            'RADA_RADA_BCGZ_Z9762',
            'RADA_RADA_BCGZ_Z9763',
            'RADA_RADA_BECS_Z9730',
            'RADA_RADA_BECS_Z9734',
            'RADA_RADA_BECS_Z9735',
            'RADA_RADA_BECS_Z9736',
            'RADA_RADA_BECS_Z9739',
            'RADA_RADA_BECS_Z9745',
            'RADA_RADA_BECS_Z9746',
            'RADA_RADA_BEGY_Z9070',
            'RADA_RADA_BEGY_Z9851',
            'RADA_RADA_BEGY_Z9852',
            'RADA_RADA_BEGY_Z9854',
            'RADA_RADA_BEGY_Z9855',
            'RADA_RADA_BEGY_Z9856',
            'RADA_RADA_BEGY_Z9857',
            'RADA_RADA_BEGY_Z9859',
            'RADA_RADA_BEHK_Z9070',
            'RADA_RADA_BEHK_Z9071',
            'RADA_RADA_BEHK_Z9072',
            'RADA_RADA_BEHK_Z9898',
            'RADA_RADA_BEKM_Z9692',
            'RADA_RADA_BEKM_Z9870',
            'RADA_RADA_BEKM_Z9871',
            'RADA_RADA_BEKM_Z9872',
            'RADA_RADA_BEKM_Z9874',
            'RADA_RADA_BEKM_Z9876',
            'RADA_RADA_BEKM_Z9879',
            'RADA_RADA_BEKM_Z9883',
            'RADA_RADA_BEKM_Z9888',
            'RADA_RADA_BENN_Z9770',
            'RADA_RADA_BENN_Z9771',
            'RADA_RADA_BENN_Z9772',
            'RADA_RADA_BENN_Z9773',
            'RADA_RADA_BENN_Z9774',
            'RADA_RADA_BENN_Z9775',
            'RADA_RADA_BENN_Z9776',
            'RADA_RADA_BENN_Z9777',
            'RADA_RADA_BENN_Z9778',
            'RADA_RADA_BENN_Z9779',
            'SATE_FY2D_ZC',
            'SATE_FY2E_AMV',
            'SATE_FY2E_CLC',
            'SATE_FY2E_CTA',
            'SATE_FY2E_HPF',
            'SATE_FY2E_NOM',
            'SATE_FY2E_OLR',
            'SATE_FY2E_PRE',
            'SATE_FY2E_SEC_LCN',
            'SATE_FY2E_SEC_MLS',
            'SATE_FY2E_SEC_R01',
            'SATE_FY2E_SEC_R02',
            'SATE_FY2E_SEC_R03',
            'SATE_FY2E_SEC_R04',
            'SATE_FY2E_SNW',
            'SATE_FY2E_SSI',
            'SATE_FY2E_TBB',
            'SATE_FY2E_TPW',
            'SATE_FY2E_UTH',
            'SATE_FY2E_ZC1',
            'SATE_FY2E_ZC3',
            'SATE_FY2E_ZC4',
            'SATE_FY2F_CTA',
            'SATE_FY2F_NOM',
            'SATE_FY2F_OLR',
            'SATE_FY2F_PRE',
            'SATE_FY2F_SEC',
            'SATE_FY2F_TBB',
            'SATE_FY2G_ALL',
            'SATE_FY2G_NOM',
            'SATE_FY3A_MERSI',
            'SATE_FY3A_NOM',
            'SATE_FY3A_TOU',
            'SATE_FY3A_VIRR',
            'SATE_FY3A_VIRR1',
            'SATE_FY3B_VIRR',
            'SATE_FY3C_AMP',
            'SATE_FY3C_ARP',
            'SATE_FY3C_ASO',
            'SATE_FY3C_ATP',
            'SATE_FY3C_CLA',
            'SATE_FY3C_CLM',
            'SATE_FY3C_CLW',
            'SATE_FY3C_COT',
            'SATE_FY3C_CPP',
            'SATE_FY3C_DFI',
            'SATE_FY3C_EDP',
            'SATE_FY3C_GFR',
            'SATE_FY3C_IWP',
            'SATE_FY3C_MRR',
            'SATE_FY3C_NOM',
            'SATE_FY3C_OLR',
            'SATE_FY3C_SIC',
            'SATE_FY3C_SST',
            'SATE_FY3C_SWE',
            'SATE_FY3C_VSM',
            'SATE_MULTI_CPP',
            'SATE_MULTI_H08',
            'SATE_GOES15',
            'SATE_JASON2',
            'SATE_MET8_MSG1_MPEF',
            'SATE_MET8_MSG1_MSG1',
            'SATE_MET10_MSG3_MPEF',
            'SATE_MET10_MSG3_MSG3',
            'SATE_METOPA_L1',
            'SATE_METOPA_L1_PUB',
            'SATE_METOPA_L2',
            'SATE_METOPB_L1',
            'SATE_METOPB_L1_PUB',
            'SATE_METOPB_L2',
            'SATE_NA19_L1',
            'SATE_NA19_L2',
            'SEVP_SEVP_FAX_BABJ',
            'SEVP_SEVP_FAX_EDZW',
            'SEVP_SEVP_FAX_RJTD',
            'SEVP_SEVP_OCEAN_OCEN',
            'SEVP_SEVP_OCEAN_YIDE',
            'SEVP_SEVP_WE_PROG',
            'SEVP_SEVP_WE_RFFC',
            'WARN_PROD',
            'WARN_WS'

            ]

Src2DstDir = {'NWP_KWBC_GLB_CASTDATA': ('NWP_MCTR_001\\KWBC_GLB\\PUB', 'NWP\\KWBC_GLB\\CASTDATA', 'CAST'),
              'NWP_KWBC_GLB_CCTVDATA': ('ShuZhi\\MeiGuo', 'NWP\\KWBC_GLB\\CCTVDATA', 'CCTV'),
              'NWP_CLDAS': ('NWP_MCTR_001\\CLDAS\\PUB', 'NWP\\CLDAS', 'CAST'),
              'NWP_ECMF_DAM': ('NWP_MCTR_002\\ECMF_DAM\\PUB', 'NWP\\ECMF_DAM', 'CAST'),
              'NWP_ECMF_GLB_CASTDATA': ('NWP_MCTR_001\\ECMF_GLB\\PUB', 'NWP\\ECMF_GLB\\CASTDATA', 'CAST'),
              'NWP_ECMF_GLB_CCTVDATA': ('ShuZhi\\OuZhou', 'NWP\\ECMF_GLB\\CCTVDATA', 'CCTV'),
              'NWP_EDZW_GLB_CASTDATA': ('NWP_MCTR_001\\EDZW_GLB\\PUB', 'NWP\\EDZW_GLB\\CASTDATA', 'CAST'),
              'NWP_EDZW_GLB_CCTVDATA': ('ShuZhi\\DeGuo', 'NWP\\EDZW_GLB\\CCTVDATA', 'CCTV'),
              'NWP_JMA_GSM': ('NWP_MCTR_003\\JMA_GSM\\PUB', 'NWP\\JMA_GSM', 'CAST'),
              'NWP_NCC_CLFC': ('NWP_MCTR_001\\NCC_CLFC\\PUB', 'NWP\\NCC_CLFC', 'CAST'),
              'NWP_NWP_KJ_QuanQiu': ('ShuZhi\\KongJun\\QuanQiu', 'NWP\\NWP_KJ', 'CCTV'),
              'NWP_NWP_KJ_QuYu': ('ShuZhi\\KongJun\\QuYu', 'NWP\\NWP_KJ', 'CCTV'),
              'NWP_NWP_ZC_T799': ('ShuZhi\\ZongCan\\T799', 'NWP\NWP_ZC', 'CCTV'),
              'NWP_NWP_NMC_GEPS': ('NWP_NMC_GEPS\\PUB\\PUB', 'NWP\\NWP_NMC_GEPS', 'CAST'),
              'NWP_NWP_NMC_GRAPES0048': ('NWP_NMC_GRAPES\\H00H48\\PUB', 'NWP\\NWP_NMC_GRAPES', 'CAST'),
              'NWP_NWP_NMC_GRAPES54': ('NWP_NMC_GRAPES\\H54\\PUB', 'NWP\\NWP_NMC_GRAPES', 'CAST'),
              'NWP_NWP_NMC_GRAPES60': ('NWP_NMC_GRAPES\\H60\\PUB', 'NWP\\NWP_NMC_GRAPES', 'CAST'),
              'NWP_NWP_NMC_REPS': ('NWP_NMC_REPS\\PUB\\PUB', 'NWP\\NWP_NMC_REPS', 'CAST'),
              'NWP_NWP_NMC_T639G0072': ('NWP_NMC_T639G\\H00H72\\PUB', 'NWP\\NWP_NMC_T639G', 'CAST'),
              'NWP_NWP_NMC_T639G7296': ('NWP_NMC_T639G\\H72H96\\PUB', 'NWP\\NWP_NMC_T639G', 'CAST'),
              'NWP_NWP_NMC_T639G96120': ('NWP_NMC_T639G\\H96H120\\PUB', 'NWP\\NWP_NMC_T639G', 'CAST'),
              'NWP_NWP_NMC_T639G120': ('NWP_NMC_T639G\\H120\\PUB', 'NWP\\NWP_NMC_T639G', 'CAST'),
              'NWP_NWP_NMC_T639R0072': ('NWP_NMC_T639R\\H00H72\\PUB', 'NWP\\NWP_NMC_T639R', 'CAST'),
              'NWP_NWP_NMC_T639R7296': ('NWP_NMC_T639R\\H72H96\\PUB', 'NWP\\NWP_NMC_T639R', 'CAST'),
              'NWP_NWP_NMC_T639R96120': ('NWP_NMC_T639R\\H96H120\\PUB', 'NWP\\NWP_NMC_T639R', 'CAST'),
              'NWP_NWP_NMC_T639R120': ('NWP_NMC_T639R\\H120\\PUB', 'NWP\\NWP_NMC_T639R', 'CAST'),
              'NWP_RJTD_GLB_CASTDATA': ('NWP_MCTR_001\\RJTD_GLB\\PUB', 'NWP\\RJTD_GLB\\CASTDATA', 'CAST'),
              'NWP_RJTD_GLB_CCTVDATA': ('ShuZhi\\RiBen', 'NWP\\RJTD_GLB\\CCTVDATA', 'CCTV'),
              'OBS_OBS_DOM_ARMY': ('QiXiang\\shikuang', 'OBS\\OBS_DOM_ARMY', 'CCTV'),
              'OBS_OBS_DOM_AWS_BCGZ': ('OBS_DOM_AWS\\CMA\\BCGZ', 'OBS\\OBS_DOM_AWS\\BCGZ', 'CAST'),
              'OBS_OBS_DOM_AWS_BECS': ('OBS_DOM_AWS\\CMA\\BECS', 'OBS\\OBS_DOM_AWS\\BECS', 'CAST'),
              'OBS_OBS_DOM_AWS_BEFZ': ('OBS_DOM_AWS\\CMA\\BEFZ', 'OBS\\OBS_DOM_AWS\\BEFZ', 'CAST'),
              'OBS_OBS_DOM_AWS_BEGY': ('OBS_DOM_AWS\\CMA\\BEGY', 'OBS\\OBS_DOM_AWS\\BEGY', 'CAST'),
              'OBS_OBS_DOM_AWS_BEHK': ('OBS_DOM_AWS\\CMA\\BEHK', 'OBS\\OBS_DOM_AWS\\BEHK', 'CAST'),
              'OBS_OBS_DOM_AWS_BEKM': ('OBS_DOM_AWS\\CMA\\BEKM', 'OBS\\OBS_DOM_AWS\\BEKM', 'CAST'),
              'OBS_OBS_DOM_AWS_CMA': ('OBS_DOM_AWS\\DOM\\CMA', 'OBS\\OBS_DOM_AWS\\CMA', 'CAST'),
              'OBS_OBS_DOM_HANGWEI_KongSi': ('QiXiang\\HangWei\\KongSi', 'OBS\\OBS_DOM_HANGWEI\\KS', 'CCTV'),
              'OBS_OBS_DOM_HANGWEI_ZhongCan': ('QiXiang\\HangWei\\ZhongCan', 'OBS\\OBS_DOM_HANGWEI\\ZC', 'CCTV'),
              'OBS_OBS_DOM_HTB_fromCCTV': ('QiXiang\\huitubao', 'OBS\\OBS_DOM_HTB', 'CCTV'),
              'OBS_OBS_DOM_HTB_fromCAST': ('MSG_001\\CMA\\PUB', 'OBS\\OBS_DOM_HTB', 'CAST'),
              'OBS_OBS_DOM_MINHANG_GuanCe': ('QiXiang\\MinHang\\GuanCe', 'OBS\\OBS_DOM_MINHANG\\GUANCE', 'CCTV'),
              'OBS_OBS_DOM_MINHANG_YuBao': ('QiXiang\\MinHang\\YuBao', 'OBS\\OBS_DOM_MINHANG\\YUBAO', 'CCTV'),
              'OBS_OBS_DOM_OCEN_CHUANBO': ('HaiYang\\ChuanBo', 'OBS\\OBS_DOM_OCEN\\CHUANBO', 'CCTV'),
              'OBS_OBS_DOM_OCEN_FUBIAO': ('HaiYang\\FuBiao\\ChangGui', 'OBS\\OBS_DOM_OCEN\\FUBIAO', 'CCTV'),
              'OBS_OBS_DOM_OCEN_HAIYANGZHAN': ('HaiYang\\HaiYangZhan', 'OBS\\OBS_DOM_OCEN\\HAIYANGZHAN', 'CCTV'),
              'OBS_OBS_DOM_OCEN_OCEN': ('OBS_DOM_PUB\\OCEN\\PUB', 'OBS\\OBS_DOM_OCEN\\OCEN', 'CAST'),
              'OBS_OBS_DOM_RIVER_GATE': ('ShuiLi\\ShuiYuQing\\GATE', 'OBS\\OBS_DOM_RIVER\\GATE', 'CCTV'),
              'OBS_OBS_DOM_RIVER_PPTN': ('ShuiLi\\ShuiYuQing\\PPTN', 'OBS\\OBS_DOM_RIVER\\PPTN', 'CCTV'),
              'OBS_OBS_DOM_RIVER_RIVER': ('ShuiLi\\ShuiYuQing\\RIVER', 'OBS\\OBS_DOM_RIVER\\RIVER', 'CCTV'),
              'OBS_OBS_DOM_RIVER_RSVR': ('ShuiLi\\ShuiYuQing\\RSVR', 'OBS\\OBS_DOM_RIVER\\RSVR', 'CCTV'),
              'OBS_OBS_DOM_RIVER_TIDE': ('ShuiLi\\ShuiYuQing\\TIDE', 'OBS\\OBS_DOM_RIVER\\TIDE', 'CCTV'),
              'OBS_OBS_DOM_RIVER_WAS': ('ShuiLi\\ShuiYuQing\\WAS', 'OBS\\OBS_DOM_RIVER\\WAS', 'CCTV'),

              'OBS_OBS_DOM_UPAR_CMA': ('OBS_DOM_PUB\\UPAR\\CMA', 'OBS\\OBS_DOM_UPAR\\CMA', 'CAST'),
              'OBS_OBS_DOM_UPAR_META': ('OBS_DOM_PUB\\UPAR\\META', 'OBS\\OBS_DOM_UPAR\\META', 'CAST'),
              'OBS_OBS_DOM_WRPD': ('OBS_DOM_PUB\\WRPD\\PUB', 'OBS\\OBS_DOM_WRPD', 'CAST'),
              'OBS_OBS_DOM_CAWN': ('OBS_DOM_PUB\\CAWN\\PUB', 'OBS\\OBS_DOM_CAWN', 'CAST'),
              'OBS_OBS_DOM_LPD': ('OBS_DOM_PUB\\LPD\\PUB', 'OBS\\OBS_DOM_LPD', 'CAST'),

              'RADA_RADA_NOR_fromCCTV': ('LeiDa\\ChangGui', 'RADA\\RADA_NOR', 'CCTV'),
              'RADA_RADA_NOR_fromCAST': ('RADA_PUB\\NOR\\IMG', 'RADA\\RADA_NOR', 'CAST'),
              'RADA_RADA_BCGZ_Z9200': ('RADA_BCGZ\\DOR\\Z9200', 'RADA\\RADA_BCGZ\\Z9200', 'CAST'),
              'RADA_RADA_BCGZ_Z9660': ('RADA_BCGZ\\DOR\\Z9660', 'RADA\\RADA_BCGZ\\Z9660', 'CAST'),
              'RADA_RADA_BCGZ_Z9662': ('RADA_BCGZ\\DOR\\Z9662', 'RADA\\RADA_BCGZ\\Z9662', 'CAST'),
              'RADA_RADA_BCGZ_Z9751': ('RADA_BCGZ\\DOR\\Z9751', 'RADA\\RADA_BCGZ\\Z9751', 'CAST'),
              'RADA_RADA_BCGZ_Z9753': ('RADA_BCGZ\\DOR\\Z9753', 'RADA\\RADA_BCGZ\\Z9753', 'CAST'),
              'RADA_RADA_BCGZ_Z9754': ('RADA_BCGZ\\DOR\\Z9754', 'RADA\\RADA_BCGZ\\Z9754', 'CAST'),
              'RADA_RADA_BCGZ_Z9755': ('RADA_BCGZ\\DOR\\Z9755', 'RADA\\RADA_BCGZ\\Z9755', 'CAST'),
              'RADA_RADA_BCGZ_Z9758': ('RADA_BCGZ\\DOR\\Z9758', 'RADA\\RADA_BCGZ\\Z9758', 'CAST'),
              'RADA_RADA_BCGZ_Z9759': ('RADA_BCGZ\\DOR\\Z9759', 'RADA\\RADA_BCGZ\\Z9759', 'CAST'),
              'RADA_RADA_BCGZ_Z9762': ('RADA_BCGZ\\DOR\\Z9762', 'RADA\\RADA_BCGZ\\Z9762', 'CAST'),
              'RADA_RADA_BCGZ_Z9763': ('RADA_BCGZ\\DOR\\Z9763', 'RADA\\RADA_BCGZ\\Z9763', 'CAST'),
              'RADA_RADA_BECS_Z9730': ('RADA_BECS\\DOR\\Z9730', 'RADA\\RADA_BECS\\Z9730', 'CAST'),
              'RADA_RADA_BECS_Z9734': ('RADA_BECS\\DOR\\Z9734', 'RADA\\RADA_BECS\\Z9734', 'CAST'),
              'RADA_RADA_BECS_Z9735': ('RADA_BECS\\DOR\\Z9735', 'RADA\\RADA_BECS\\Z9735', 'CAST'),
              'RADA_RADA_BECS_Z9736': ('RADA_BECS\\DOR\\Z9736', 'RADA\\RADA_BECS\\Z9736', 'CAST'),
              'RADA_RADA_BECS_Z9739': ('RADA_BECS\\DOR\\Z9739', 'RADA\\RADA_BECS\\Z9739', 'CAST'),
              'RADA_RADA_BECS_Z9745': ('RADA_BECS\\DOR\\Z9745', 'RADA\\RADA_BECS\\Z9745', 'CAST'),
              'RADA_RADA_BECS_Z9746': ('RADA_BECS\\DOR\\Z9746', 'RADA\\RADA_BECS\\Z9746', 'CAST'),
              'RADA_RADA_BEGY_Z9070': ('RADA_BEGY\\DOR\\Z9070', 'RADA\\RADA_BEGY\\Z9070', 'CAST'),
              'RADA_RADA_BEGY_Z9851': ('RADA_BEGY\\DOR\\Z9851', 'RADA\\RADA_BEGY\\Z9851', 'CAST'),
              'RADA_RADA_BEGY_Z9852': ('RADA_BEGY\\DOR\\Z9852', 'RADA\\RADA_BEGY\\Z9852', 'CAST'),
              'RADA_RADA_BEGY_Z9854': ('RADA_BEGY\\DOR\\Z9854', 'RADA\\RADA_BEGY\\Z9854', 'CAST'),
              'RADA_RADA_BEGY_Z9855': ('RADA_BEGY\\DOR\\Z9855', 'RADA\\RADA_BEGY\\Z9855', 'CAST'),
              'RADA_RADA_BEGY_Z9856': ('RADA_BEGY\\DOR\\Z9856', 'RADA\\RADA_BEGY\\Z9856', 'CAST'),
              'RADA_RADA_BEGY_Z9857': ('RADA_BEGY\\DOR\\Z9857', 'RADA\\RADA_BEGY\\Z9857', 'CAST'),
              'RADA_RADA_BEGY_Z9859': ('RADA_BEGY\\DOR\\Z9859', 'RADA\\RADA_BEGY\\Z9859', 'CAST'),
              'RADA_RADA_BEHK_Z9070': ('RADA_BEHK\\DOR\\Z9070', 'RADA\\RADA_BEHK\\Z9070', 'CAST'),
              'RADA_RADA_BEHK_Z9071': ('RADA_BEHK\\DOR\\Z9071', 'RADA\\RADA_BEHK\\Z9071', 'CAST'),
              'RADA_RADA_BEHK_Z9072': ('RADA_BEHK\\DOR\\Z9072', 'RADA\\RADA_BEHK\\Z9072', 'CAST'),
              'RADA_RADA_BEHK_Z9898': ('RADA_BEHK\\DOR\\Z9898', 'RADA\\RADA_BEHK\\Z9898', 'CAST'),
              'RADA_RADA_BEKM_Z9692': ('RADA_BEKM\\DOR\\Z9692', 'RADA\\RADA_BEHK\\Z9692', 'CAST'),
              'RADA_RADA_BEKM_Z9870': ('RADA_BEKM\\DOR\\Z9870', 'RADA\\RADA_BEHK\\Z9870', 'CAST'),
              'RADA_RADA_BEKM_Z9871': ('RADA_BEKM\\DOR\\Z9871', 'RADA\\RADA_BEHK\\Z9871', 'CAST'),
              'RADA_RADA_BEKM_Z9872': ('RADA_BEKM\\DOR\\Z9872', 'RADA\\RADA_BEHK\\Z9872', 'CAST'),
              'RADA_RADA_BEKM_Z9874': ('RADA_BEKM\\DOR\\Z9874', 'RADA\\RADA_BEHK\\Z9874', 'CAST'),
              'RADA_RADA_BEKM_Z9876': ('RADA_BEKM\\DOR\\Z9876', 'RADA\\RADA_BEHK\\Z9876', 'CAST'),
              'RADA_RADA_BEKM_Z9879': ('RADA_BEKM\\DOR\\Z9879', 'RADA\\RADA_BEHK\\Z9879', 'CAST'),
              'RADA_RADA_BEKM_Z9883': ('RADA_BEKM\\DOR\\Z9883', 'RADA\\RADA_BEHK\\Z9883', 'CAST'),
              'RADA_RADA_BEKM_Z9888': ('RADA_BEKM\\DOR\\Z9888', 'RADA\\RADA_BEHK\\Z9888', 'CAST'),
              'RADA_RADA_BENN_Z9770': ('RADA_BENN\\DOR\\Z9770', 'RADA\\RADA_BENN\\Z9770', 'CAST'),
              'RADA_RADA_BENN_Z9771': ('RADA_BENN\\DOR\\Z9771', 'RADA\\RADA_BENN\\Z9771', 'CAST'),
              'RADA_RADA_BENN_Z9772': ('RADA_BENN\\DOR\\Z9772', 'RADA\\RADA_BENN\\Z9772', 'CAST'),
              'RADA_RADA_BENN_Z9773': ('RADA_BENN\\DOR\\Z9773', 'RADA\\RADA_BENN\\Z9773', 'CAST'),
              'RADA_RADA_BENN_Z9774': ('RADA_BENN\\DOR\\Z9774', 'RADA\\RADA_BENN\\Z9774', 'CAST'),
              'RADA_RADA_BENN_Z9775': ('RADA_BENN\\DOR\\Z9775', 'RADA\\RADA_BENN\\Z9775', 'CAST'),
              'RADA_RADA_BENN_Z9776': ('RADA_BENN\\DOR\\Z9776', 'RADA\\RADA_BENN\\Z9776', 'CAST'),
              'RADA_RADA_BENN_Z9777': ('RADA_BENN\\DOR\\Z9777', 'RADA\\RADA_BENN\\Z9777', 'CAST'),
              'RADA_RADA_BENN_Z9778': ('RADA_BENN\\DOR\\Z9778', 'RADA\\RADA_BENN\\Z9778', 'CAST'),
              'RADA_RADA_BENN_Z9779': ('RADA_BENN\\DOR\\Z9779', 'RADA\\RADA_BENN\\Z9779', 'CAST'),
              'SATE_FY2D_ZC': ('WeiXing\\FY2D\\ZongCan\\data1', 'SATE\\FY2D\\ZC', 'CCTV'),
              'SATE_FY2E_AMV': ('SATE_FY2E_L2L3\\AMV\\PUB', 'SATE\\FY2E\\AMV', 'CAST'),
              'SATE_FY2E_CLC': ('SATE_FY2E_L2L3\\CLC\\PUB', 'SATE\\FY2E\\CLC', 'CAST'),
              'SATE_FY2E_CTA': ('SATE_FY2E_L2L3\\CTA\\PUB', 'SATE\\FY2E\\CTA', 'CAST'),
              'SATE_FY2E_HPF': ('SATE_FY2E_L2L3\\HPF\\PUB', 'SATE\\FY2E\\HPF', 'CAST'),
              'SATE_FY2E_NOM': ('SATE_FY2E_NOM', 'SATE\\FY2E\\NOM', 'CAST'),
              'SATE_FY2E_OLR': ('SATE_FY2E_L2L3\\OLR\\PUB', 'SATE\\FY2E\\OLR', 'CAST'),
              'SATE_FY2E_PRE': ('SATE_FY2E_L2L3\\PRE\\PUB', 'SATE\\FY2E\\PRE', 'CAST'),
              'SATE_FY2E_SEC_LCN': ('SATE_FY2E_L2L3\\SEC\\LCN', 'SATE\\FY2E\\SEC\\LCN', 'CAST'),
              'SATE_FY2E_SEC_MLS': ('SATE_FY2E_L2L3\\SEC\\MLS', 'SATE\\FY2E\\SEC\\MLS', 'CAST'),
              'SATE_FY2E_SEC_R01': ('SATE_FY2E_L2L3\\SEC\\R01', 'SATE\\FY2E\\SEC\\R01', 'CAST'),
              'SATE_FY2E_SEC_R02': ('SATE_FY2E_L2L3\\SEC\\R02', 'SATE\\FY2E\\SEC\\R02', 'CAST'),
              'SATE_FY2E_SEC_R03': ('SATE_FY2E_L2L3\\SEC\\R03', 'SATE\\FY2E\\SEC\\R03', 'CAST'),
              'SATE_FY2E_SEC_R04': ('SATE_FY2E_L2L3\\SEC\\R04', 'SATE\\FY2E\\SEC\\R04', 'CAST'),
              'SATE_FY2E_SNW': ('SATE_FY2E_L2L3\\SNW\\PUB', 'SATE\\FY2E\\SNW', 'CAST'),
              'SATE_FY2E_SSI': ('SATE_FY2E_L2L3\\SSI\\PUB', 'SATE\\FY2E\\SSI', 'CAST'),
              'SATE_FY2E_TBB': ('SATE_FY2E_L2L3\\TBB\\PUB', 'SATE\\FY2E\\TBB', 'CAST'),
              'SATE_FY2E_TPW': ('SATE_FY2E_L2L3\\TPW\\PUB', 'SATE\\FY2E\\TPW', 'CAST'),
              'SATE_FY2E_UTH': ('SATE_FY2E_L2L3\\UTH\\PUB', 'SATE\\FY2E\\UTH', 'CAST'),
              'SATE_FY2E_ZC1': ('WeiXing\\FY2E\\ZongCan\\data1', 'SATE\\FY2E\\ZC1', 'CCTV'),
              'SATE_FY2E_ZC3': ('WeiXing\\FY2E\\ZongCan\\data2', 'SATE\\FY2E\\ZC3', 'CCTV'),
              'SATE_FY2E_ZC4': ('WeiXing\\FY2E\\ZongCan\\data4', 'SATE\\FY2E\\ZC4', 'CCTV'),
              'SATE_FY2F_CTA': ('SATE_FY2F_L2L3\\CTA\\PUB', 'SATE\\FY2F\\CTA', 'CAST'),
              'SATE_FY2F_NOM': ('SATE_FY2F_NOM', 'SATE\\FY2F\\NOM', 'CAST'),
              'SATE_FY2F_OLR': ('SATE_FY2F_L2L3\\OLR\\PUB', 'SATE\\FY2F\\CTA', 'CAST'),
              'SATE_FY2F_PRE': ('SATE_FY2F_L2L3\\PRE\\PUB', 'SATE\\FY2F\\CTA', 'CAST'),
              'SATE_FY2F_SEC': ('SATE_FY2F_L2L3\\SEC\\PUB', 'SATE\\FY2F\\CTA', 'CAST'),
              'SATE_FY2F_TBB': ('SATE_FY2F_L2L3\\TBB\\PUB', 'SATE\\FY2F\\CTA', 'CAST'),
              'SATE_FY2G_ALL': ('SATE_FY2G_L2L3\\pub\\pub', 'SATE\\FY2G\\ALL', 'CAST'),
              'SATE_FY2G_NOM': ('SATE_FY2G_NOM', 'SATE\\FY2G\\NOM', 'CAST'),
              'SATE_FY3A_MERSI': ('SATE_FY3A_L2L3\\MERSI\\PUB', 'SATE\\FY3A\\MERSI', 'CAST'),
              'SATE_FY3A_NOM': ('SATE_FY3A_L1\PUB\PUB', 'SATE\\FY3A\\NOM', 'CAST'),
              'SATE_FY3A_TOU': ('SATE_FY3A_L2L3\\TOU\\TOZ', 'SATE\\FY3A\\TOU', 'CAST'),
              'SATE_FY3A_VIRR': ('SATE_FY3A_L2L3\\VIRR\\PUB', 'SATE\\FY3A\\VIRR', 'CAST'),
              'SATE_FY3A_VIRR1': ('SATE_FY3A_VIRR1\\PUB\\PUB', 'SATE\\FY3A\\VIRR1', 'CAST'),
              'SATE_FY3B_VIRR': ('SATE_FY3B_L2L3\\VIRR\\PUB', 'SATE\\FY3B\\VIRR', 'CAST'),
              'SATE_FY3C_AMP': ('SATE_FY3C_L2L3\\GNOS\\AMP', 'SATE\\FY3C\\AMP', 'CAST'),
              'SATE_FY3C_ARP': ('SATE_FY3C_L2L3\\GNOS\\ARP', 'SATE\\FY3C\\ARP', 'CAST'),
              'SATE_FY3C_ASO': ('SATE_FY3C_L2L3\\VIRR\\ASO', 'SATE\\FY3C\\ASO', 'CAST'),
              'SATE_FY3C_ATP': ('SATE_FY3C_L2L3\\GNOS\\ATP', 'SATE\\FY3C\\ATP', 'CAST'),
              'SATE_FY3C_AHP': ('SATE_FY3C_L2L3\\MWHS\\AHP', 'SATE\\FY3C\\AHP', 'CAST'),
              'SATE_FY3C_CLA': ('SATE_FY3C_L2L3\\VIRR\\CLA', 'SATE\\FY3C\\CLA', 'CAST'),
              'SATE_FY3C_CLM': ('SATE_FY3C_L2L3\\VIRR\\CLM', 'SATE\\FY3C\\CLM', 'CAST'),
              'SATE_FY3C_CLW': ('SATE_FY3C_L2L3\\MWRI\\CLW', 'SATE\\FY3C\\CLW', 'CAST'),
              'SATE_FY3C_COT': ('SATE_FY3C_L2L3\\VIRR\\COT', 'SATE\\FY3C\\COT', 'CAST'),
              'SATE_FY3C_CPP': ('SATE_FY3C_L2L3\\VIRR\\CPP', 'SATE\\FY3C\\CPP', 'CAST'),
              'SATE_FY3C_DFI': ('SATE_FY3C_L2L3\\MWRI\\DFI', 'SATE\\FY3C\\DFI', 'CAST'),
              'SATE_FY3C_EDP': ('SATE_FY3C_L2L3\\GNOS\\EDP', 'SATE\\FY3C\\EDP', 'CAST'),
              'SATE_FY3C_GFR': ('SATE_FY3C_L2L3\\VIRR\\GFR', 'SATE\\FY3C\\ASO', 'GFR'),
              'SATE_FY3C_IWP': ('SATE_FY3C_L2L3\\MWHS\\IWP', 'SATE\\FY3C\\IWP', 'CAST'),
              'SATE_FY3C_MRR': ('SATE_FY3C_L2L3\\MWRI\\MRR', 'SATE\\FY3C\\MRR', 'CAST'),
              'SATE_FY3C_NOM': ('SATE_FY3C_L1\\PUB\\PUB', 'SATE\\FY3C\\NOM', 'CAST'),
              'SATE_FY3C_OLR': ('SATE_FY3C_L2L3\\IRAS\\OLR', 'SATE\\FY3C\\OLR', 'CAST'),
              'SATE_FY3C_SIC': ('SATE_FY3C_L2L3\\VIRR\\SIC', 'SATE\\FY3C\\SIC', 'CAST'),
              'SATE_FY3C_SST': ('SATE_FY3C_L2L3\\MWRI\\SST', 'SATE\\FY3C\\SST', 'CAST'),
              'SATE_FY3C_SWE': ('SATE_FY3C_L2L3\\MWRI\\SWE', 'SATE\\FY3C\\SWE', 'CAST'),
              'SATE_FY3C_VSM': ('SATE_FY3C_L2L3\\MWRI\\VSM', 'SATE\\FY3C\\VSM', 'CAST'),
              'SATE_MULTI_CPP': ('SATE_MLT_PROD\\CPP\\PUB', 'SATE\\MULTI\\CPP', 'CAST'),
              'SATE_MULTI_H08': ('SATE_MULTI_001\\H08\\PUB', 'SATE\\MULTI\\H08', 'CAST'),
              'SATE_GOES15': ('SATE_MULTI_003\\GOES15\\MSG3_GOES15', 'SATE\\GOES15', 'CAST'),
              'SATE_JASON2': ('SATE_MULTI_003\\JASON2\\PUB', 'SATE\\JASON2', 'CAST'),
              'SATE_MET8_MSG1_MPEF': ('SATE_MULTI_003\\MET8\\MSG1_MPEF', 'SATE\\MET8\\MSG1_MPEF', 'CAST'),
              'SATE_MET8_MSG1_MSG1': ('SATE_MULTI_003\\MET8\\MSG1_MSG1', 'SATE\\MET8\\MSG1_MSG1', 'CAST'),
              'SATE_MET10_MSG3_MPEF': ('SATE_MULTI_003\\MET10\\MSG3_MPEF', 'SATE\\MET10\\MSG3_MPEF', 'CAST'),
              'SATE_MET10_MSG3_MSG3': ('SATE_MULTI_003\\MET10\\MSG3_MSG3', 'SATE\\MET10\\MSG3_MSG3', 'CAST'),
              'SATE_METOPA_L1': ('SATE_MULTI_003\\METOPA\\L1', 'SATE\\METOPA\\L1', 'CAST'),
              'SATE_METOPA_L1_PUB': ('SATE_MULTI_003\\METOPA\\L1_PUB', 'SATE\\METOPA\\L1_PUB', 'CAST'),
              'SATE_METOPA_L2': ('SATE_MULTI_003\\METOPA\\L2', 'SATE\\METOPA\\L2', 'CAST'),
              'SATE_METOPB_L1': ('SATE_MULTI_003\\METOPB\\L1', 'SATE\\METOPB\\L1', 'CAST'),
              'SATE_METOPB_L1_PUB': ('SATE_MULTI_003\\METOPB\\L1_PUB', 'SATE\\METOPB\\L1_PUB', 'CAST'),
              'SATE_METOPB_L2': ('SATE_MULTI_003\\METOPB\\L2', 'SATE\\METOPB\\L2', 'CAST'),
              'SATE_NA19_L1': ('SATE_MULTI_003\\NA19\\L1', 'SATE\\NA19\\L1', 'CAST'),
              'SATE_NA19_L2': ('SATE_MULTI_003\\NA19\\L2', 'SATE\\NA19\\L2', 'CAST'),
              'SEVP_SEVP_FAX_BABJ': ('SEVP_FAX_001\\BABJ\\PUB', 'SEVP\\SEVP_FAX\\BABJ', 'CAST'),
              'SEVP_SEVP_FAX_EDZW': ('SEVP_FAX_001\\EDZW\\PUB', 'SEVP\\SEVP_FAX\\EDZW', 'CAST'),
              'SEVP_SEVP_FAX_RJTD': ('SEVP_FAX_001\\RJTD\\PUB', 'SEVP\\SEVP_FAX\\RJTD', 'CAST'),
              'SEVP_SEVP_OCEAN_OCEN': ('SEVP_OC_001\\OCEN\\PUB', 'SEVP\\SEVP_OCEAN\\OCEN', 'CAST'),
              'SEVP_SEVP_OCEAN_YIDE': ('SEVP_OC_001\\OCEN\\TIDE', 'SEVP\\SEVP_OCEAN\\TIDE', 'CAST'),
              'SEVP_SEVP_WE_PROG': ('SEVP_WE_001\\PROG\\PUB', 'SEVP\\SEVP_WE\\PROG', 'CAST'),
              'SEVP_SEVP_WE_RFFC': ('SEVP_WE_001\\RFFC\\PUB', 'SEVP\\SEVP_WE\\RFFC', 'CAST'),
              'WARN_PROD': ('WARNING_001\\PUB\\PROD', 'WARN\\PROD', 'CAST'),
              'WARN_WS': ('WARNING_001\\PUB\\WS', 'WARN\\WS', 'CAST')

              }
for task in TaskList:
    try:
        # 命名格式类似A_HVXQ20ECMG090000_C_BABJ_20180109062857_73939.bin
        #             ?_????????????????_?_????_YYYYMMDD??????_?????.???
        if task in {'NWP_KWBC_GLB_CASTDATA',
                    'NWP_CLDAS',
                    'NWP_ECMF_DAM',
                    'NWP_ECMF_GLB_CASTDATA',
                    'NWP_EDZW_GLB_CASTDATA',
                    'NWP_JMA_GSM',
                    'NWP_NCC_CLFC',
                    'NWP_NWP_NMC_GEPS',
                    'NWP_NWP_NMC_GRAPES0048',
                    'NWP_NWP_NMC_GRAPES54',
                    'NWP_NWP_NMC_GRAPES60',
                    'NWP_NWP_NMC_REPS',
                    'NWP_NWP_NMC_T639G0072',
                    'NWP_NWP_NMC_T639G7296',
                    'NWP_NWP_NMC_T639G96120',
                    'NWP_NWP_NMC_T639G120',
                    'NWP_NWP_NMC_T639R0072',
                    'NWP_NWP_NMC_T639R7296',
                    'NWP_NWP_NMC_T639R96120',
                    'NWP_NWP_NMC_T639R120',
                    'NWP_RJTD_GLB_CASTDATA',
                    'OBS_OBS_DOM_AWS_BCGZ',
                    'OBS_OBS_DOM_AWS_BECS',
                    'OBS_OBS_DOM_AWS_BEFZ',
                    'OBS_OBS_DOM_AWS_BEGY',
                    'OBS_OBS_DOM_AWS_BEHK',
                    'OBS_OBS_DOM_AWS_BEKM',
                    'OBS_OBS_DOM_AWS_BENN',
                    'OBS_OBS_DOM_AWS_CMA',

                    'OBS_OBS_DOM_UPAR_CMA',
                    'OBS_OBS_DOM_UPAR_META',
                    'OBS_OBS_DOM_WRPD',
                    'OBS_OBS_DOM_CAWN',

                    'RADA_RADA_NOR_fromCCTV',
                    'RADA_RADA_NOR_fromCAST',
                    'RADA_RADA_BCGZ_Z9200',
                    'RADA_RADA_BCGZ_Z9660',
                    'RADA_RADA_BCGZ_Z9662',
                    'RADA_RADA_BCGZ_Z9751',
                    'RADA_RADA_BCGZ_Z9753',
                    'RADA_RADA_BCGZ_Z9754',
                    'RADA_RADA_BCGZ_Z9755',
                    'RADA_RADA_BCGZ_Z9758',
                    'RADA_RADA_BCGZ_Z9759',
                    'RADA_RADA_BCGZ_Z9762',
                    'RADA_RADA_BCGZ_Z9763',
                    'RADA_RADA_BECS_Z9730',
                    'RADA_RADA_BECS_Z9734',
                    'RADA_RADA_BECS_Z9735',
                    'RADA_RADA_BECS_Z9736',
                    'RADA_RADA_BECS_Z9739',
                    'RADA_RADA_BECS_Z9745',
                    'RADA_RADA_BECS_Z9746',
                    'RADA_RADA_BEGY_Z9070',
                    'RADA_RADA_BEGY_Z9851',
                    'RADA_RADA_BEGY_Z9852',
                    'RADA_RADA_BEGY_Z9854',
                    'RADA_RADA_BEGY_Z9855',
                    'RADA_RADA_BEGY_Z9856',
                    'RADA_RADA_BEGY_Z9857',
                    'RADA_RADA_BEGY_Z9859',
                    'RADA_RADA_BEHK_Z9070',
                    'RADA_RADA_BEHK_Z9071',
                    'RADA_RADA_BEHK_Z9072',
                    'RADA_RADA_BEHK_Z9898',
                    'RADA_RADA_BEKM_Z9692',
                    'RADA_RADA_BEKM_Z9870',
                    'RADA_RADA_BEKM_Z9871',
                    'RADA_RADA_BEKM_Z9872',
                    'RADA_RADA_BEKM_Z9874',
                    'RADA_RADA_BEKM_Z9876',
                    'RADA_RADA_BEKM_Z9879',
                    'RADA_RADA_BEKM_Z9883',
                    'RADA_RADA_BEKM_Z9888',
                    'RADA_RADA_BENN_Z9770',
                    'RADA_RADA_BENN_Z9771',
                    'RADA_RADA_BENN_Z9772',
                    'RADA_RADA_BENN_Z9773',
                    'RADA_RADA_BENN_Z9774',
                    'RADA_RADA_BENN_Z9775',
                    'RADA_RADA_BENN_Z9776',
                    'RADA_RADA_BENN_Z9777',
                    'RADA_RADA_BENN_Z9778',
                    'RADA_RADA_BENN_Z9779',
                    'SATE_FY2E_AMV',
                    'SATE_FY2E_CLC',
                    'SATE_FY2E_CTA',
                    'SATE_FY2E_HPF',
                    'SATE_FY2E_NOM',
                    'SATE_FY2E_OLR',
                    'SATE_FY2E_PRE',
                    'SATE_FY2E_SEC_LCN',
                    'SATE_FY2E_SEC_MLS',
                    'SATE_FY2E_SEC_R01',
                    'SATE_FY2E_SEC_R02',
                    'SATE_FY2E_SEC_R03',
                    'SATE_FY2E_SEC_R04',
                    'SATE_FY2E_SNW',
                    'SATE_FY2E_SSI',
                    'SATE_FY2E_TBB',
                    'SATE_FY2E_TPW',
                    'SATE_FY2E_UTH',
                    'SATE_FY2F_CTA',
                    'SATE_FY2F_NOM',
                    'SATE_FY2F_OLR',
                    'SATE_FY2F_PRE',
                    'SATE_FY2F_SEC',
                    'SATE_FY2F_TBB',
                    'SATE_FY2G_ALL',
                    'SATE_FY2G_NOM',
                    'SATE_FY3A_MERSI',
                    'SATE_FY3A_NOM',
                    'SATE_FY3A_TOU',
                    'SATE_FY3A_VIRR',
                    'SATE_FY3A_VIRR1',
                    'SATE_FY3B_VIRR',
                    'SATE_FY3C_AMP',
                    'SATE_FY3C_ARP',
                    'SATE_FY3C_ASO',
                    'SATE_FY3C_ATP',
                    'SATE_FY3C_CLA',
                    'SATE_FY3C_CLM',
                    'SATE_FY3C_CLW',
                    'SATE_FY3C_COT',
                    'SATE_FY3C_CPP',
                    'SATE_FY3C_DFI',
                    'SATE_FY3C_EDP',
                    'SATE_FY3C_GFR',
                    'SATE_FY3C_IWP',
                    'SATE_FY3C_MRR',
                    'SATE_FY3C_NOM',
                    'SATE_FY3C_OLR',
                    'SATE_FY3C_SIC',
                    'SATE_FY3C_SST',
                    'SATE_FY3C_SWE',
                    'SATE_FY3C_VSM',
                    'SATE_MULTI_CPP',
                    'SATE_MULTI_H08',
                    'SATE_JASON2',
                    'SATE_METOPA_L1',
                    'SATE_METOPA_L1_PUB',
                    'SATE_METOPA_L2',
                    'SATE_METOPB_L1',
                    'SATE_METOPB_L1_PUB',
                    'SATE_METOPB_L2',
                    'SATE_NA19_L1',
                    'SATE_NA19_L2',
                    'SEVP_SEVP_OCEAN_OCEN',
                    'SEVP_SEVP_OCEAN_YIDE',
                    'SEVP_SEVP_WE_RFFC',
                    'WARN_PROD'

                    }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('_').__len__() >= 5:
                        dt = file.split('.')[0].split('_')[4]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)

                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        # if (file.split('.')[-1]=='bz2'):#如果是压缩文件解压bz2文件
                        #     src=open(fileSourcePath,'rb')
                        #     dst=open(os.path.join(DstPath,file.split('.')[0]),'wb')
                        #     dst.write(bz2.decompress(src.read()))
                        #     print(task + '====' + 'Decompress file from:' + fileSourcePath + '    To:    ' + DstPath)
                        #     dst.close()
                        #     src.close()
                        #     continue

                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        # if (file.split('.')[-1]=='bz2'):#如果是压缩文件解压bz2文件
                        #     src=open(fileSourcePath,'rb')
                        #     dst=open(os.path.join(DstPath,file.split('.')[0]),'wb')
                        #     dst.write(bz2.decompress(src.read()))
                        #     print(task + '====' + 'Decompress file from:' + fileSourcePath + '    To:    ' + DstPath)
                        #     dst.close()
                        #     src.close()
                        #     continue
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似Z_P_LPD__C_BABJ_20180117171201_2018_01_18.txt
        #             ?_?_???__?_????_YYYYMMDD??????_????_??_??.???
        elif task in {'OBS_OBS_DOM_LPD'

                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('_').__len__() >= 7:
                        dt = file.split('.')[0].split('_')[6]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似kwheic98.070
        #             ????????.DD?
        elif task in {'NWP_KWBC_GLB_CCTVDATA',
                      'NWP_EDZW_GLB_CCTVDATA',
                      'NWP_RJTD_GLB_CCTVDATA',
                      'SEVP_SEVP_FAX_BABJ',
                      'SEVP_SEVP_FAX_EDZW',
                      'SEVP_SEVP_FAX_RJTD'

                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if (file.split('.').__len__() != 1) | (file.split('.')[0].split('_').__len__() == 1):
                        day = file.split('.')[-1][:2]
                        ctime = time.localtime(os.path.getctime(fileSourcePath))
                        cyear = time.strftime('%Y', ctime)
                        cmonth = time.strftime('%Y', ctime) + time.strftime('%m', ctime)
                        yearDir = os.path.join(Dest_Home, cyear)
                        dayDir = os.path.join(yearDir, cmonth + day)
                        try:
                            time.strptime(cmonth + day, '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似kwheic98.070
        #             ????????.DD?
        # 命名格式类似echirs_pv_850_201801110800.120
        # ??????_??_???_YYYYMMDD????.???
        # 命名格式类似zc_mwf_dh24-p_200_201801090800.096
        #             ??_???_??????_??_?????????????.???
        elif task in {'NWP_ECMF_GLB_CCTVDATA',
                      'NWP_NWP_ZC_T799',

                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('_').__len__() == 1:
                        day = file.split('.')[-1][:2]
                        ctime = time.localtime(os.path.getctime(fileSourcePath))
                        cyear = time.strftime('%Y', ctime)
                        cmonth = time.strftime('%Y', ctime) + time.strftime('%m', ctime)
                        yearDir = os.path.join(Dest_Home, cyear)
                        dayDir = os.path.join(yearDir, cmonth + day)
                        try:
                            time.strptime(cmonth + day, '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    elif file.split('.')[0].split('_').__len__() == 4:
                        dt = file.split('.')[0].split('_')[3]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    elif file.split('.')[0].split('_').__len__() == 5:
                        dt = file.split('.')[0].split('_')[4]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似KTDIA2018010612000000.grb
        #             ?????YYYYMMDD????????.???
        # 命名格式类似t2018010612-TH500_HH500_TT500_UU500-000.gif
        #            ?YYYYMMDD??-???????????????????????-???.???
        #            t2018010612-TD999_PP999-120.gif
        #            ?YYYYMMDD??-???????????-???.???
        elif task in {'NWP_NWP_KJ_QuanQiu',
                      'NWP_NWP_KJ_QuYu'
                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('-').__len__() == 1:
                        dt = file.split('.')[0][5:13]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    elif file.split('.')[0].split('-').__len__() == 3:
                        dt = file.split('.')[0].split('-')[0][1:9]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似ds20180107.dat
        #             ??YYYYMMDD.???
        elif task in {'OBS_OBS_DOM_HANGWEI_KongSi',
                      'OBS_OBS_DOM_MINHANG_GuanCe',
                      'OBS_OBS_DOM_MINHANG_YuBao'
                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('_').__len__() == 1:
                        dt = file.split('.')[0][2:10]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似kj090150.abj
        #             ??DD????.???
        elif task in {'OBS_OBS_DOM_ARMY',
                      'OBS_OBS_DOM_HANGWEI_ZhongCan',
                      'OBS_OBS_DOM_HTB_fromCCTV',
                      'OBS_OBS_DOM_HTB_fromCAST',
                      'WARN_WS'

                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if '_' in file:  # 用于任务OBS_OBS_DOM_HTB_fromCAST
                        continue
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('_').__len__() == 1:
                        day = file.split('.')[0][2:4]
                        ctime = time.localtime(os.path.getctime(fileSourcePath))
                        cyear = time.strftime('%Y', ctime)
                        cmonth = time.strftime('%Y', ctime) + time.strftime('%m', ctime)
                        yearDir = os.path.join(Dest_Home, cyear)
                        dayDir = os.path.join(yearDir, cmonth + day)
                        try:
                            time.strptime(cmonth + day, '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            if (task == 'OBS_OBS_DOM_HTB_fromCCTV') or (task == 'OBS_OBS_DOM_HTB_fromCAST'):
                                shutil.copy(fileSourcePath, os.path.join(HTB_Home, file))  # 复制绘图报到htb目录
                                print(task + '====' + 'Copy file from:' + fileSourcePath + '    To:    ' + HTB_Home)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            if (task == 'OBS_OBS_DOM_HTB_fromCCTV') or (task == 'OBS_OBS_DOM_HTB_fromCAST'):
                                shutil.copy(fileSourcePath, os.path.join(HTB_Home, file))  # 复制绘图报到htb目录
                                print(task + '====' + 'Copy file from:' + fileSourcePath + '    To:    ' + HTB_Home)
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            if (task == 'OBS_OBS_DOM_HTB_fromCCTV') or (task == 'OBS_OBS_DOM_HTB_fromCAST'):
                                shutil.copy(fileSourcePath, os.path.join(HTB_Home, file))  # 复制绘图报到htb目录
                                print(task + '====' + 'Copy file from:' + fileSourcePath + '    To:    ' + HTB_Home)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            if (task == 'OBS_OBS_DOM_HTB_fromCCTV') or (task == 'OBS_OBS_DOM_HTB_fromCAST'):
                                shutil.copy(fileSourcePath, os.path.join(HTB_Home, file))  # 复制绘图报到htb目录
                                print(task + '====' + 'Copy file from:' + fileSourcePath + '    To:    ' + HTB_Home)
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似SH120702.BBX
        #             ??MMDD??.???
        elif task in {'OBS_OBS_DOM_OCEN_CHUANBO',
                      'OBS_OBS_DOM_OCEN_FUBIAO'

                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('_').__len__() == 1:
                        month = file.split('.')[0][2:4]
                        day = file.split('.')[0][4:6]
                        ctime = time.localtime(os.path.getctime(fileSourcePath))
                        cyear = time.strftime('%Y', ctime)
                        cmonth = time.strftime('%m', ctime)
                        if int(month) > int(cmonth):
                            cyear = str(int(cyear) - 1)
                            pass
                        yearDir = os.path.join(Dest_Home, cyear)
                        dayDir = os.path.join(yearDir, cyear + month + day)
                        try:
                            time.strptime(cyear + month + day, '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似010612.DGG
        #             MMDD??.???
        elif task in {'OBS_OBS_DOM_OCEN_HAIYANGZHAN'

                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('_').__len__() == 1:
                        month = file.split('.')[0][0:2]
                        day = file.split('.')[0][2:4]
                        ctime = time.localtime(os.path.getctime(fileSourcePath))
                        cyear = time.strftime('%Y', ctime)
                        cmonth = time.strftime('%m', ctime)
                        if int(month) > int(cmonth):
                            cyear = str(int(cyear) - 1)
                            pass
                        yearDir = os.path.join(Dest_Home, cyear)
                        dayDir = os.path.join(yearDir, cyear + month + day)
                        try:
                            time.strptime(cyear + month + day, '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似H2A_RA1_IDR_2PT_0004_4156_20180107_220624_20180107_220624.nc
        #             ???_???_???_???_????_????_YYYYMMDD_??????_????????_??????.???
        # 命名格式类似H2A_RM2A20180106000004_4115.h5
        #            ???_????YYYYMMDD??????_????.???
        # 命名格式类似W_cn-SOA-beijing,OCEN_C_BABJ_20180107150000.txt
        #            ?_???????????????????_?_????_YYYYMMDD??????.???
        elif task in {'OBS_OBS_DOM_OCEN_OCEN'

                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if (file.split('.')[-1] == 'nc') & (file.split('.')[0].split('_').__len__() == 10):
                        dt = file.split('.')[0].split('_')[6]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    elif (file.split('.')[-1] == 'h5') & (file.split('.')[0].split('_').__len__() == 3):
                        dt = file.split('.')[0].split('_')[1][4:12]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    elif (file.split('.')[-1] == 'txt') & (file.split('.')[0].split('_').__len__() == 5):
                        dt = file.split('.')[0].split('_')[4]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似ST_GATE_R18010909.TXT
        #             ??_????_?????????.???
        elif task in {'OBS_OBS_DOM_RIVER_GATE',
                      'OBS_OBS_DOM_RIVER_PPTN',
                      'OBS_OBS_DOM_RIVER_RIVER',
                      'OBS_OBS_DOM_RIVER_RSVR',
                      'OBS_OBS_DOM_RIVER_TIDE',
                      'OBS_OBS_DOM_RIVER_WAS'
                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('_').__len__() == 3:
                        ctime = time.localtime(os.path.getctime(fileSourcePath))
                        cyear = time.strftime('%Y', ctime)
                        dt = cyear[0:2] + file.split('.')[0].split('_')[2][1:7]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似20180109-0203_ch1_org.fy2
        #             YYYYMMDD?????_???_???.???
        # 命名格式类似20180112-0901.fy0
        #             ????????-????.???
        # 命名格式类似18011211.i1m
        #             YYMMDD??.??
        elif task in {'SATE_FY2D_ZC',
                      'SATE_FY2E_ZC1',
                      'SATE_FY2E_ZC3',
                      'SATE_FY2E_ZC4'
                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp') | (file.split('.')[-1] == 'idx') | (
                                file.split('.')[-1] == 'log'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('-').__len__() == 2:
                        dt = file.split('.')[0].split('-')[0][:8]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    elif file.split('.')[0].split('-').__len__() == 1:
                        ctime = time.localtime(os.path.getctime(fileSourcePath))
                        cyear = time.strftime('%Y', ctime)
                        dt = cyear[0:2] + file.split('.')[0][:6]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似L-000-MSG3__-GOES15______-00_7_135W-000001___-201801061600-C_
        #             ?-???-??????-????????????-?????????-?????????-YYYYMMDD????-?
        elif task in {'SATE_GOES15',
                      'SATE_MET8_MSG1_MPEF',
                      'SATE_MET8_MSG1_MSG1',
                      'SATE_MET10_MSG3_MPEF',
                      'SATE_MET10_MSG3_MSG3'

                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('-').__len__() == 8:
                        dt = file.split('.')[0].split('-')[-2]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
        # 命名格式类似A_HVXQ20ECMG090000_C_BABJ_20180109062857_73939.bin
        #             ?_????????????????_?_????_YYYYMMDD??????_?????.???
        # 命名格式类似FO0910TJ.YTY
        #             ??DD????.???
        elif task in {'SEVP_SEVP_WE_PROG'
                      }:
            SrcDir, DstDir, Home = Src2DstDir[task]
            if Home == 'CCTV':
                SrcPath = os.path.join(CCTV_Home, SrcDir)
            elif Home == 'CAST':
                SrcPath = os.path.join(Cast_Home, SrcDir)
            print('Traverse the source directory:  ' + SrcPath)
            for root, dirs, files in os.walk(SrcPath):
                for file in files:
                    if (file == 'Thumbs.db') | (file.split('.')[-1] == 'tmp'):
                        continue
                    fileSourcePath = os.path.join(SrcPath, file)
                    if file.split('.')[0].split('_').__len__() == 6:
                        dt = file.split('.')[0].split('_')[4]
                        yearDir = os.path.join(Dest_Home, dt[:4])
                        dayDir = os.path.join(yearDir, dt[:8])
                        try:
                            time.strptime(dt[:8], '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    elif file.split('.')[0].split('_').__len__() == 1:
                        day = file.split('.')[0][2:4]
                        ctime = time.localtime(os.path.getctime(fileSourcePath))
                        cyear = time.strftime('%Y', ctime)
                        cmonth = time.strftime('%Y', ctime) + time.strftime('%m', ctime)
                        yearDir = os.path.join(Dest_Home, cyear)
                        dayDir = os.path.join(yearDir, cmonth + day)
                        try:
                            time.strptime(cmonth + day, '%Y%m%d')
                        except Exception, e:
                            continue
                        DstPath = os.path.join(dayDir, DstDir)
                        fileDstPath = os.path.join(DstPath, file)
                    else:
                        continue
                    if (os.path.exists(DstPath) == False):
                        os.makedirs(DstPath)
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)

                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                    else:
                        if os.path.exists(fileDstPath) == False:
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
                        else:
                            os.remove(fileDstPath)
                            shutil.move(fileSourcePath, DstPath)
                            print(task + '====' + 'Move file from:' + fileSourcePath + '    To:    ' + DstPath)
    except Exception, e:
        print e

print('All tasks have been done!')
