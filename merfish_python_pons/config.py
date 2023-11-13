import os
from collections import defaultdict


def get_config(root, slice_id, region_id):
    out = {
        'cell_by_gene': os.path.join(root, slice_id, region_id, 'cell_by_gene.csv'),
        'cell_metadata': os.path.join(root, slice_id, region_id, 'cell_metadata.csv'),
        'detected_transcripts': os.path.join(root, slice_id, region_id, 'detected_transcripts.csv'),
        'micron_to_mosaic_pixel_transform': os.path.join(root, slice_id, region_id, 'images', 'micron_to_mosaic_pixel_transform.csv'),
        'manifest': os.path.join(root, slice_id, region_id, 'images', 'manifest.json'),
        'dapi_tif': os.path.join(root, slice_id, region_id, 'images', 'mosaic_DAPI_z3.tif'),
        'cell_boundaries_dir': os.path.join(root, slice_id, region_id, 'cell_boundaries'),
        'clip_poly': _clip_poly[slice_id][region_id],
        'rotation': _rotation[slice_id][region_id],
        'slice_id': slice_id,
        'region_id': region_id,
        'z_stacks': [0, 1, 2, 3, 4, 5, 6],
    }
    return out


# only spots within this poly will be plotted. Use empty array if you do not want any clipping to be applied
_clip_poly = defaultdict(dict)
_clip_poly['MsBrain_Eg1_VS6_JH_V6_05-02-2021']['region_0'] = [[25009,29875], [25594,32860], [27268,37773], [28476,42200], [28319,45239], [48535,40838], [72239,39897], [71366,38387], [68110,34895], [67266,32498], [63527,25493], [52594,26965], [45625,27624], [33621,28185]]
_clip_poly['MsBrain_Eg1_VS6_JH_V6_05-02-2021']['region_1'] = [[25106,29454], [26388,32536], [26659,38544], [28245,41168], [27516,44897], [48331,39522], [69056,36621], [65948,33412], [66650,32191], [65446,28944], [65549,22916], [45505,28184]]
_clip_poly['MsBrain_Eg2_VS6_V11_JH_05-02-2021']['region_0'] = [[28094,23896], [25746,25410], [24495,27027], [20162,29651], [17683,30951], [15614,31536], [33310,44154], [50425,59685], [51163,54493], [52558,47763], [55733,45640], [58030,44952], [47527,38343], [43377,38534], [40182,36575], [38295,34134], [38376,30361]]
_clip_poly['MsBrain_Eg2_VS6_V11_JH_05-02-2021']['region_1'] = [[22166,21044], [40780,31079], [43060,25614], [44783,20500], [48653,17247], [51944,17096], [39781,8273], [36062,8532], [33925,7331], [32613,6355]]
_clip_poly['MsBrain_Eg3_VS6_JH_V6_05-01-2021']['region_0'] = [[20536,46833], [21073,57587], [24378,57968], [28677,61407], [30993,64743], [32433,66376], [44250,45254], [42496,22093], [38324,23373], [32435,25375], [30592,26122], [29011,25406], [28182,24806], [24628,30324], [26056,32438], [27387,41162], [24383,46495], [22309,47044]]
_clip_poly['MsBrain_Eg3_VS6_JH_V6_05-01-2021']['region_1'] = [[20118,47441], [24203,54149], [26177,56640], [30439,61406], [40574,41546], [39264,20452], [37252,20928], [35823,20936], [27965,25666], [25275,25646], [27374,39593]]
_clip_poly['MsBrain_EG4_VS6library_V6_LH_04-14-21']['region_0'] = [[38795,34051], [48315,36706], [53254,35519], [57565,33713], [60644,28831], [63749,26289], [39603,18535], [16894,23371], [19447,28288], [21805,31870], [24055,34746], [27814,35267], [32734,34724]]
_clip_poly['MsBrain_EG4_VS6library_V6_LH_04-14-21']['region_1'] = [[39155,31287], [40553,31074], [42232,31653], [45079,32768], [48324,33984], [50624,34889], [53553,34110], [56277,32898], [58316,31663], [59659,30535], [64268,25448], [42512,16254], [19976,19858], [20980,21404], [23078,25355], [26402,29978], [28978,31853], [31479,31942], [34826,31488], [37966,31032]]
_clip_poly['MsBrain_Eg5_VS6_JH_V6_05-16-2021']['region_0'] = [[39035,30314], [45997,32143], [48813,33976], [51279,33900], [55589,33350], [59792,31342], [63320,25053], [40458,15638], [17272,20468], [17414,23563], [16671,25882], [16976,27139], [17830,28421], [20984,30671], [24045,31357], [27619,31120], [31897,31233], [36821,30905]]
_clip_poly['MsBrain_Eg5_VS6_JH_V6_05-16-2021']['region_1'] = [[39066,25611], [44108,26157], [46670,27575], [49424,30216], [54130,30767], [55809,30035], [59592,26619], [63940,22703], [64730,17694], [39666,14540], [14635,14820], [15696,18906], [18275,23866], [22570,26986], [26956,28571], [30533,25935], [34623,25328]]


_clip_poly["MsBrain_ZM0_VS6_JH_V6_05-15-2021"]["region_0"] = [[23054,63265], [25434,63245], [29185,63098], [31673,63185], [35503,64704], [37423,65301], [38362,44637], [39902,27565], [38247,27520], [37332,26910], [36019,27398], [34709,28753], [33415,29622], [31155,30776], [29117,31468], [27652,30278], [26370,28599], [24264,26311]]
_clip_poly["MsBrain_ZM1_VS6_JH_V11_05-16-2021"]["region_0"] = [[38946,26660], [35233,26282], [33875,26076], [30686,25406], [28411,23967], [26785,22761], [21890,45270], [13050,63421], [20827,62503], [23185,62547], [25723,62724], [32020,62076], [35147,64719]]
_clip_poly["MsBrain_ZM2_VS6_JH_V11_05-15-2021"]["region_0"] = [[23117,24654], [26929,26072], [27535,27338], [27759,29437], [27705,32140], [26990,35421], [27376,37175], [27282,39431], [47416,34657], [66303,29019], [64389,26207], [63291,25089], [63332,24336], [61994,22090], [60104,20922], [57677,15412]]
_clip_poly["MsBrain_ZM3_VS6_JH_V11_05-17-2021"]["region_0"] = [[18398,52894], [20475,53506], [23330,54538], [27024,56024], [29922,57610], [31696,58844], [44492,39381], [48267,22289], [46650,22397], [44282,22747], [40749,22930], [38472,23078], [31862,22270], [30330,21460], [26923,28744], [30024,30308], [30808,32573], [30593,34746], [29696,37133], [28048,38873], [25517,40459], [22741,39880]]
_clip_poly["MsBrain_ZM4_VS6_JH_V11_05-11-2021"]["region_0"] = [[18222,44334], [18495,55619], [19221,55285], [22219,55212], [23744,56249], [29759,60315], [33543,62473], [41175,37648], [39881,19957], [34642,22166], [30906,23554], [26622,24319], [23195,24638], [21752,24492], [20247,30515], [23517,28883], [25249,32036], [25700,38536], [21768,44714], [20152,45324]]
_clip_poly["MsBrain_ZM5.1_VS6_JH_V11_05-12-2021"]["region_0"] = [[35847,21888], [28894,20172], [28440,21781], [27098,23184], [24674,24510], [20166,26852], [16307,29838], [33684,40803], [55383,48893], [54446,44310], [53990,42577], [54173,39880], [52983,35549], [52251,33109], [51206,32774], [44284,31725], [40486,30385], [38239,27936], [34675,23646]]
_clip_poly["MsBrain_ZM5.2_VS6_JH_V6_05-13-2021"]["region_0"] = [[19426,44606], [19070,50883], [22521,51821], [24016,54446], [25648,57174], [29312,60546], [43435,41289], [44003,21226], [34218,24388], [31572,25292], [29210,26741], [28355,27565], [28886,30714], [28564,34850], [28014,38206], [25149,41801], [22831,43949], [21397,45048]]
_clip_poly["MsBrain_ZM6.1_VS6_V6_JH_05-11-2021"]["region_0"] = [[28207,37231], [23494,43335], [21871,45056], [21767,46972], [22220,49714], [23949,52425], [25790,54737], [27980,56960], [30147,59541], [43590,39121], [43358,18881], [39927,19695], [37464,20436], [35066,21685], [32393,22706], [31075,23664], [29855,24884], [29359,27034], [29604,29873], [29239,32825]]
_clip_poly["MsBrain_ZM7.1_VS6_V6_JH_05-12-2021"]["region_0"] = [[39251,31974], [42238,31669], [44833,31537], [46664,31842], [48538,32185], [50328,31623], [51609,29824], [54950,24687], [56538,21423], [57941,17500], [34737,16481], [15534,30763], [17174,31858], [19332,33296], [21063,36519], [23687,36915], [26771,37406], [30072,36924], [32588,35317], [35277,34463]]
_clip_poly["MsBrain_ZM7.2_VS6_JH_V11_05-13-2021"]["region_0"] = [[24123,20115], [22358,19888], [20666,20222], [18542,20581], [16637,21205], [11962,22760], [9557,24080], [26936,39796], [50039,48626], [49708,46513], [49554,45238], [49330,39553], [49041,36505], [47367,34100], [45353,31658], [43736,31231], [40757,31034], [37234,29666], [34504,28396], [32340,26120], [30562,23250], [29189,21449], [27633,19954], [25954,19343]]

_clip_poly["VS6_MsBrain_B3_VS6library_V10_LH_02-07-21"]["region_0"] = [[32917,26008], [24361,28957], [25839,31564], [24211,35064], [22120,39609], [20635,44214], [41629,42298], [62474,37733], [61877,33751], [60880,32249], [59415,29992], [56871,26896], [57010,23526], [46939,24344], [47313,25683], [45787,26689], [41245,28607], [34796,28123], [33284,27413]]
_clip_poly["VS6_MsBrain_B3_VS6library_V10_LH_02-07-21"]["region_1"] = [[37117,25176], [25995,27374], [26766,29228], [26734,31083], [24659,32425], [23728,35161], [21960,36985], [22339,39712], [21468,42744], [42886,42142], [63175,40255], [62489,37473], [62550,35874], [64638,35494], [62426,31822], [60506,27453], [59409,25031], [48957,25346], [43083,27945]]


 # MERFISH MC
_clip_poly['VS6MsBrain_C1_VS6libary_V3_LH_03-14-21']['region_0'] = [[27033,21446], [24608,24479], [23258,27752], [21640,30681], [20575,32354], [39926,37918], [53521,55600], [53932,52285], [55350,48775], [57634,44849], [59112,42340], [42631,32129]]
_clip_poly['VS6MsBrain_C1_VS6libary_V3_LH_03-14-21']['region_1'] = [[25801,24688], [25812,27114], [25935,30636], [24436,33060], [22564,34973], [20174,37591], [41554,42363], [60349,53037], [60058,50319], [59957,47698], [60185,42960], [63904,37780], [65288,35420], [45651,30243]]
_clip_poly['VS6MsBrain_C2_VS6libary_V1_LH_03-14-21']['region_0'] = [[61747,48106], [62113,46381], [63554,43902], [64976,41029], [67794,39011], [70122,37956], [73466,36415], [51870,24743], [30178,17253], [30829,19043], [31360,21868], [32233,24877], [32355,28106], [31566,30166], [29206,32385], [45353,39859]]
_clip_poly['VS6MsBrain_C2_VS6libary_V1_LH_03-14-21']['region_1'] = [[60409,45099], [60884,43133], [61702,40841], [62960,37992], [64285,35911], [65760,33891], [68214,32718], [47907,23017], [27414,14774], [28096,16520], [28469,18746], [28707,21215], [29051,24911], [28687,26308], [26902,27846], [24799,29658], [23639,30239], [42559,37692]]
_clip_poly['VS6MsBrain_C3_VS6libary_V10_LH_03-15-21']['region_0'] = [[40054,49642], [47114,54985], [48021,53925], [50480,53420], [54976,52337], [57710,51748], [60574,51911], [63601,52358], [49777,31331], [28576,17374], [29029,19863], [28989,22628], [28582,26410], [27972,30046], [27199,32324], [25305,33973], [31487,41324], [37124,43592]]
_clip_poly['VS6MsBrain_C3_VS6libary_V10_LH_03-15-21']['region_1'] = [[45837,59466], [47044,54992], [49198,53471], [54479,52072], [58258,51947], [61003,52294], [63200,52131], [51000,31035], [32307,13645], [32351,15810], [32106,18307], [31262,21581], [30429,25828], [28847,29327], [27219,30059], [23945,30463], [22186,30463], [36566,43172]]
_clip_poly['VS6MsBrain_C4_VS6libary_V1_LH_03-17-21']['region_0'] = [[39739,26197], [36038,25744], [35603,27283], [32857,29144], [30019,30670], [27810,31813], [21647,35138], [44761,44517], [68229,44735], [65556,40207], [59661,30749], [57167,29086], [47767,30400]]
_clip_poly['VS6MsBrain_C4_VS6libary_V1_LH_03-17-21']['region_1'] = [[41849,27853], [32164,23633], [30942,24498], [28470,26481], [26640,28555], [24046,30416], [21976,32320], [20651,35152], [20011,37531], [19835,38702], [41862,41512], [64106,37548], [61459,32865], [58744,30302], [55532,27788], [52163,24967]]
_clip_poly['VS6MsBrain_C5_VS6libary_V3_LH_03-17-21']['region_0'] = [[32554,26825], [30681,27816], [27132,29459], [24897,31331], [22374,33466], [20361,35236], [41840,43307], [63839,39969], [63503,38553], [61402,35941], [58678,32644], [55951,30450], [52703,28557], [42692,29459]]
_clip_poly['VS6MsBrain_C5_VS6libary_V3_LH_03-17-21']['region_1'] = [[34557,26970], [30037,27510], [25701,28606], [23344,29870], [20111,31922], [38923,43702], [61968,44376], [61488,41740], [59808,37811], [57722,35395], [54596,33175], [52838,31516], [42920,30562]]

# MERFISH FF
_clip_poly['VS6MsBrain_F1_VS6libary_V10_LH_03-19-21']['region_0'] = [[59940,49349], [61699,44670], [63130,42204], [66310,38221], [45878,28022], [38642,8555], [36176,9499], [34314,10444], [32364,12542], [28181,14668], [25348,15764], [41947,39196]]
_clip_poly['VS6MsBrain_F1_VS6libary_V10_LH_03-19-21']['region_1'] = [[63661,52199], [63601,50663], [64149,47544], [65552,44012], [67258,40601], [70484,36908], [74049,34083], [52177,25540], [30262,22119], [29855,24831], [28717,28563], [27282,32313], [25435,34438], [45698,40172]]
_clip_poly['VS6MsBrain_F2_VS6libary_V3_LH_03-21-21']['region_0'] = [[12912,60440], [16653,60546], [18911,61468], [21136,62421], [23864,64019], [25329,65051], [27688,67562], [28745,69065], [36784,46445], [41165,27653], [38984,27874], [36495,27913], [33744,27006], [31008,25998], [29115,24955], [23232,43357]]
_clip_poly['VS6MsBrain_F2_VS6libary_V3_LH_03-21-21']['region_1'] = [[24858,61321], [27114,60901], [29593,60323], [31423,61503], [34397,63163], [38263,66786], [42029,67820], [42905,43247], [39148,21801], [37237,23266], [35103,24326], [32169,25481], [29469,25752], [25717,23763], [24759,37846], [26478,38804], [28064,42304], [26789,45967], [23983,47757]]
_clip_poly['VS6MsBrain_F3_VS6libary_V10_LH_03-21-21']['region_0'] = [[21233,55516], [20908,57062], [21965,59380], [26236,62648], [33704,68694], [42067,47175], [40370,24004], [37237,25866], [33613,27457], [30831,29713], [28325,32342], [26391,35006], [27067,45224]]
_clip_poly['VS6MsBrain_F3_VS6libary_V10_LH_03-21-21']['region_1'] = [[23235,51006], [26770,61428], [29095,62115], [31898,64619], [34097,67150], [37126,68848], [39287,69370], [46829,45535], [41077,22994], [37673,24224], [35019,25964], [31084,28375], [29162,28009], [27362,26880], [24637,36069], [26967,37738], [28760,45125], [26362,51415]]
_clip_poly['VS6MsBrain_F4_VS6libary_V3_LH_03-19-21']['region_0'] = [[18283,48492], [19746,51625], [21982,54350], [24340,56547], [27226,59029], [30205,60402], [33797,62450], [35299,38794], [33442,16701], [31204,17335], [27544,18247], [26487,18857], [24726,21886], [22531,24612], [21515,26849], [23409,38304]]
_clip_poly['VS6MsBrain_F4_VS6libary_V3_LH_03-19-21']['region_1'] = [[28783,49375], [30530,51442], [32785,53658], [35618,55627], [39132,57566], [42860,59124], [46121,60338], [47266,38394], [40312,12792], [38194,15054], [36323,16438], [33682,18097], [31811,20538], [30631,23182], [29410,25785], [28800,28633], [31987,38220]]
_clip_poly['VS6MsBrain_F5_VS6libary_V10_LH_03-17-21']['region_0'] = [[37857,44342], [38300,47542], [39642,48559], [45445,49247], [52730,48783], [57819,48905], [43795,28961], [28643,13734], [24623,16309], [22816,17630], [22529,23001], [23462,26763], [26071,32145], [33429,38220]]
_clip_poly['VS6MsBrain_F5_VS6libary_V10_LH_03-17-21']['region_1'] = [[37998,42784], [37550,44533], [39233,47868], [42014,51256], [45810,53751], [50467,54468], [55886,53804], [46892,28499], [30868,12999], [28356,14292], [24406,15826], [24252,17842], [23666,21286], [24417,25287], [25598,27686], [28835,29323], [30666,29771], [36137,35412]]


_rotation = defaultdict(dict)
_rotation["MsBrain_Eg1_VS6_JH_V6_05-02-2021"]["region_0"] = 9,
_rotation["MsBrain_Eg1_VS6_JH_V6_05-02-2021"]["region_1"] = 11,
_rotation["MsBrain_Eg2_VS6_V11_JH_05-02-2021"]["region_0"] = -39,
_rotation["MsBrain_Eg2_VS6_V11_JH_05-02-2021"]["region_1"] = -42,
_rotation["MsBrain_Eg3_VS6_JH_V6_05-01-2021"]["region_0"] = 75,
_rotation["MsBrain_Eg3_VS6_JH_V6_05-01-2021"]["region_1"] = 79,
_rotation['MsBrain_EG4_VS6library_V6_LH_04-14-21']['region_0'] = 180,
_rotation['MsBrain_EG4_VS6library_V6_LH_04-14-21']['region_1'] = 180,
_rotation['MsBrain_Eg5_VS6_JH_V6_05-16-2021']['region_0'] = 180,
_rotation['MsBrain_Eg5_VS6_JH_V6_05-16-2021']['region_1'] = 180,
_rotation['VS6_MsBrain_B3_VS6library_V10_LH_02-07-21']['region_0'] = 7,
_rotation['VS6_MsBrain_B3_VS6library_V10_LH_02-07-21']['region_1'] = 2, # this could easily be 0 or even 1.0
_rotation['VS6MsBrain_F5_VS6libary_V10_LH_03-17-21']["region_0"] = 130,
_rotation['VS6MsBrain_F5_VS6libary_V10_LH_03-17-21']["region_1"] = 120,

_rotation["MsBrain_ZM0_VS6_JH_V6_05-15-2021"]["region_0"] = 85,
_rotation["MsBrain_ZM1_VS6_JH_V11_05-16-2021"]["region_0"] = -117,
_rotation["MsBrain_ZM2_VS6_JH_V11_05-15-2021"]["region_0"] = -3,
_rotation["MsBrain_ZM3_VS6_JH_V11_05-17-2021"]["region_0"] = 60,
_rotation["MsBrain_ZM4_VS6_JH_V11_05-11-2021"]["region_0"] = 78,
_rotation["MsBrain_ZM5.1_VS6_JH_V11_05-12-2021"]["region_0"] = -32,
_rotation["MsBrain_ZM5.2_VS6_JH_V6_05-13-2021"]["region_0"] = 63,
_rotation["MsBrain_ZM6.1_VS6_V6_JH_05-11-2021"]["region_0"] = 63,
_rotation["MsBrain_ZM7.1_VS6_V6_JH_05-12-2021"]["region_0"] = -167,
_rotation["MsBrain_ZM7.2_VS6_JH_V11_05-13-2021"]["region_0"] = -37,


