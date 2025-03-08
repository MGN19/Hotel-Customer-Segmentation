import functions as f

# Dictionary defining outlier thresholds and bin settings for each numeric column
outliers_dict = {'Age': {"n_bins": 15, "left_out": None, "right_out": None},
                 'DaysSinceCreation': {"n_bins": 15, "left_out": None, "right_out": None},
                 'AverageLeadTime': {"n_bins": 15, "left_out": None, "right_out": 570},
                 'LodgingRevenue': {"n_bins": 15, "left_out": None, "right_out": 10500},
                 'OtherRevenue': {"n_bins": 15, "left_out": None, "right_out": 3500},
                 'BookingsCanceled': {"n_bins": 15, "left_out": None, "right_out": 4.5},
                 'BookingsNoShowed': {"n_bins": 15, "left_out": None, "right_out": 2.5},
                 'BookingsCheckedIn': {"n_bins": 15, "left_out": None, "right_out": 60},
                 'PersonsNights': {"n_bins": 15, "left_out": None, "right_out": 80},
                 'RoomNights': {"n_bins": 15, "left_out": None, "right_out": 80},
                 'TotalRevenue': {"n_bins": 15, "left_out": None, "right_out": 9250},
                 'RetentionRate': {"n_bins": 10, "left_out": 0.65, "right_out": None},
                 'RevenuePerNight': {"n_bins": 15, "left_out": None, "right_out": 2500},
                 'RevenuePerPersonNight': {"n_bins": 15, "left_out": None, "right_out": 1250},
}

# Dictionary defining outlier ellipses
plot_params_dict = {
    ('DaysSinceCreation', 'BookingsNoShowed'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (100, 1), 'width': 100, 'height': 0.5, 'angle':0}
        ]
    },
    ('AverageLeadTime', 'BookingsCheckedIn'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (200, 15), 'width': 20, 'height': 3, 'angle':0}
        ]
    },
    ('OtherRevenue', 'BookingsCheckedIn'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (2500, 20), 'width': 1000, 'height': 4, 'angle':0},
            {'center': (700, 37), 'width': 400, 'height': 8, 'angle':0}
        ]
    },
    ('Age', 'BookingsCheckedIn'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (33, 36), 'width': 15, 'height': 7, 'angle':0}
        ]
    },
    ('LodgingRevenue', 'BookingsCheckedIn'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (7000, 26), 'width': 700, 'height': 10, 'angle':0}
        ]
    },
    ('LodgingRevenue', 'RetentionRate'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (5700, 0.33), 'width': 200, 'height': 0.03, 'angle':0}
        ]
    },
    ('OtherRevenue', 'BookingsCanceled'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (3050, 1), 'width': 100, 'height': 0.3, 'angle':0}
        ]
    },
    ('OtherRevenue', 'RetentionRate'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (1500, 0.34), 'width': 300, 'height': 0.05, 'angle':0},
            {'center': (3050, 0.92), 'width': 100, 'height': 0.05, 'angle':0}
        ]
    },
    ('OtherRevenue', 'PreferenceScore'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (2550, 3), 'width': 150, 'height': 0.3, 'angle':0}
        ]
    },
    ('BookingsCanceled', 'BookingsCheckedIn'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (0, 32), 'width': 0.2, 'height': 3, 'angle':0}
        ]
    },
    ('BookingsCanceled', 'LTV'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (1, 36.8), 'width': 0.13, 'height': 5, 'angle':0}
        ]
    },
    ('BookingsCanceled', 'RevenuePerNight'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (1, 1050), 'width': 0.1, 'height': 80, 'angle':0}
        ]
    },
    ('BookingsCanceled', 'RevenuePerPersonNight'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (1, 550), 'width': 0.1, 'height': 80, 'angle':0}
        ]
    },
    ('BookingsNoShowed', 'BookingsCheckedIn'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (1, 38), 'width': 0.08, 'height': 1.5, 'angle':0},
            {'center': (0, 40), 'width': 0.08, 'height': 3, 'angle':0}
        ]
    },
    ('BookingsCheckedIn', 'TotalRevenue'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (40, 4420), 'width': 4, 'height': 500, 'angle':0},
            {'center': (32, 8097), 'width': 1, 'height': 300, 'angle':0}
        ]
    },
    ('BookingsCheckedIn', 'LTV'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (8, 34.5), 'width': 1, 'height': 5, 'angle':0}
        ]
    },
    ('PersonsNights', 'LTV'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (60, 62), 'width': 2, 'height': 3, 'angle':0}
        ]
    },
    ('RoomNights', 'TotalRevenue'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (57, 7000), 'width': 4, 'height': 1500, 'angle':0}
        ]
    },
    ('RoomNights', 'RetentionRate'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (59, 0.5), 'width': 1, 'height': 0.03, 'angle':0}
        ]
    },
    ('RoomNights', 'PreferenceScore'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (51, 2), 'width': 1.7, 'height': 0.2, 'angle':0}
        ]
    },
    ('TotalRevenue', 'PreferenceScore'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (5000, 3), 'width': 200, 'height': 0.1, 'angle':0}
        ]
    },
    ('RevenuePerPersonNight', 'PreferenceScore'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (890, 1), 'width': 30, 'height': 0.1, 'angle':0}
        ]
    },
    ('LTV', 'RevenuePerPersonNight'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (37.3, 889.6), 'width': 3, 'height': 40, 'angle':0}
        ]
    },
    ('RetentionRate', 'RevenuePerNight'): {
        'color': f.main_color,
        'ellipses': [
            {'center': (0.33, 1048), 'width':0.03, 'height': 70, 'angle':0}
        ]
    }
}

# Index of multivariate outliers
multivariate_outliers = [94231, 2133, 64309, 65589, 3038, 97232, 17576, 36848, 92877, 97232, 64309,
                          3038, 65589, 17576, 60055, 92061, 92877, 92877, 72942, 92061, 24069, 17576,
                            72942, 92061, 3038, 64309, 65589, 17576, 3038, 65589, 64309, 50584, 27886]


continent_dict = {
    'FRA': 'EU', 'DEU': 'EU', 'PRT': 'EU', 'GBR': 'EU', 'ESP': 'EU',
    'ITA': 'EU', 'BEL': 'EU', 'NLD': 'EU', 'IRL': 'EU', 'CHE': 'EU',
    'AUT': 'EU', 'SWE': 'EU', 'NOR': 'EU', 'POL': 'EU', 'FIN': 'EU',
    'DNK': 'EU', 'RUS': 'EU', 'ROU': 'EU', 'HUN': 'EU', 'CZE': 'EU',
    'LUX': 'EU', 'GRC': 'EU', 'BGR': 'EU', 'HRV': 'EU', 'SRB': 'EU',
    'UKR': 'EU', 'EST': 'EU', 'SVK': 'EU', 'LVA': 'EU', 'LTU': 'EU',
    'SVN': 'EU', 'ISL': 'EU', 'CYP': 'EU', 'MLT': 'EU', 'ALB': 'EU',
    'MKD': 'EU', 'BIH': 'EU', 'BLR': 'EU', 'SMR': 'EU', 'LIE': 'EU',
    'AND': 'EU', 'GIB': 'EU', 'MCO': 'EU', 'SLV': 'EU', 'SJM': 'EU','MNE': 'EU',
    'USA': 'NA', 'CAN': 'NA', 'MEX': 'NA','JAM': 'NA',
    'GTM': 'NA','GRD': 'NA','PRI': 'NA','AIA': 'NA','KNA': 'NA',
    'CRI': 'NA', 'PAN': 'NA', 'CUB': 'NA', 'BRB': 'NA','ABW': 'NA','DMA': 'NA',
    'BRA': 'SA', 'ARG': 'SA', 'CHL': 'SA', 'COL': 'SA','DOM': 'NA','HTI': 'NA',
    'PER': 'SA', 'VEN': 'SA', 'ECU': 'SA', 'BOL': 'SA','LCA': 'NA','BMU': 'NA',
    'PER': 'SA', 'VEN': 'SA', 'ECU': 'SA', 'BOL': 'SA','LCA': 'NA','BMU': 'NA',
    'PRY': 'SA', 'URY': 'SA', 'GUY': 'SA', 'SUR': 'SA',
    'ISR': 'AS', 'CHN': 'AS', 'IND': 'AS', 'KOR': 'AS', 'JPN': 'AS', 'TUR': 'AS','THA': 'AS','SGP': 'AS','HKG': 'AS',
    'IRN': 'AS', 'PHL': 'AS', 'ARE': 'AS', 'QAT': 'AS', 'KAZ': 'AS', 'VNM': 'AS','BGD': 'AS','LBN': 'AS','KGZ': 'AS',
    'IDN': 'AS', 'MYS': 'AS', 'PAK': 'AS', 'ARM': 'AS', 'GEO': 'AS', 'KWT': 'AS','AZE': 'AS','MDV': 'AS',
    'OMN': 'AS', 'BHR': 'AS', 'IRQ': 'AS', 'JOR': 'AS', 'LKA': 'AS', 'SYR': 'AS','SAU': 'AS','LAO': 'AS',
    'AFG': 'AS', 'UZB': 'AS', 'TJK': 'AS', 'YEM': 'AS', 'SDN': 'AS', 'IOT': 'AS','TWN': 'AS','TMP': 'AS',
    'AUS': 'OC', 'NZL': 'OC', 'FJI': 'OC', 'PNG': 'OC', 'WSM': 'OC',
    'TON': 'OC', 'KIR': 'OC', 'NRU': 'OC', 'VUT': 'OC', 'SLB': 'OC',
    'MHL': 'OC', 'PLW': 'OC', 'FSM': 'OC', 'COK': 'OC', 'NCL': 'OC',
    'PYF': 'OC', 'PCN': 'OC', 'NIU': 'OC', 'TKL': 'OC', 'GUM': 'OC',
    'MNP': 'OC', 'ASM': 'OC', 'WLF': 'OC', 'TUV': 'OC', 'NF': 'OC',
    'ZAF': 'AF', 'MAR': 'AF', 'DZA': 'AF', 'EGY': 'AF', 'NGA': 'AF', 'MOZ': 'AF', 'AGO': 'AF','CPV': 'AF','TUN': 'AF','MUS': 'AF','MDG': 'AF',
    'SEN': 'AF', 'ETH': 'AF', 'UGA': 'AF', 'KEN': 'AF', 'TZA': 'AF', 'SOM': 'AF', 'CMR': 'AF', 'GHA': 'AF', 'CIV': 'AF', 'NGA': 'AF',
    'ZAF': 'AF', 'DZA': 'AF', 'EGY': 'AF', 'MAR': 'AF', 'SDN': 'AF', 'ETH': 'AF', 'MLI': 'AF', 'BFA': 'AF', 'NER': 'AF','MRT': 'AF',
    'TGO': 'AF', 'BEN': 'AF', 'MR': 'AF', 'SEN': 'AF', 'GMB': 'AF', 'GNB': 'AF', 'SLE': 'AF', 'LBR': 'AF', 'CIV': 'AF','STP': 'AF',
    'GH': 'AF', 'TOG': 'AF', 'BJ': 'AF', 'NG': 'AF', 'CM': 'AF', 'CF': 'AF', 'TD': 'AF', 'ER': 'AF', 'DJ': 'AF','MWI': 'AF',
    'SO': 'AF', 'ET': 'AF', 'UG': 'AF', 'RW': 'AF', 'BI': 'AF', 'MZ': 'AF', 'ZM': 'AF', 'ZW': 'AF', 'MW': 'AF','COM': 'AF',
    'LS': 'AF', 'BW': 'AF', 'NA': 'AF', 'ZA': 'AF', 'SZ': 'AF', 'KM': 'AF', 'MG': 'AF', 'MU': 'AF', 'SC': 'AF','GAB': 'AF',
    'ST': 'AF', 'KE': 'AF', 'TZ': 'AF', 'UG': 'AF', 'RW': 'AF', 'BI': 'AF', 'DJ': 'AF', 'ER': 'AF', 'ET': 'AF','BDI': 'AF',
    'SO': 'AF', 'SD': 'AF', 'SS': 'AF','COD': 'AF','LBY': 'AF','NAM': 'AF','RWA': 'AF','NAM': 'AF','SYC': 'AF','GIN': 'AF',
    'ATA': 'AN','ATF': 'AN',
    'CAF': 'AF','FRO': 'EU', 'ZWE': 'AF','BWA': 'AF','ERI': 'AF','SPM': 'NA','JEY': 'EU','GNQ': 'AF','NIC': 'NA', 'SWZ': 'AF',
    'CYM': 'NA','ATG': 'NA','FLK': 'SA','BHS': 'NA', 'UMI': 'OC','TKM': 'AS', 'MMR': 'AS', 'VIR': 'NA', 
    'VCT': 'NA', 'GUF': 'SA','TCD': 'AF','NPL': 'AS','TTO': 'NA','HND': 'NA',
}