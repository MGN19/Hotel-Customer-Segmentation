import functions as f

# Dictionary defining outlier thresholds and bin settings for each numeric column
outliers_dict = {'Age': {"n_bins": 15, "left_out": None, "right_out": None},
                 'DaysSinceCreation': {"n_bins": 15, "left_out": None, "right_out": None},
                 'AverageLeadTime': {"n_bins": 15, "left_out": None, "right_out": 570},
                 'LodgingRevenue': {"n_bins": 15, "left_out": None, "right_out": 10500},
                 'OtherRevenue': {"n_bins": 15, "left_out": None, "right_out": 3500},
                 'BookingsCanceled': {"n_bins": 15, "left_out": None, "right_out": 4.5},
                 'BookingsNoShowed': {"n_bins": 15, "left_out": None, "right_out": 2.5},
                 'BookingsCheckedIn': {"n_bins": 15, "left_out": None, "right_out": 45},
                 'PersonsNights': {"n_bins": 15, "left_out": None, "right_out": 80},
                 'RoomNights': {"n_bins": 15, "left_out": None, "right_out": 75},
                 'TotalRevenue': {"n_bins": 15, "left_out": None, "right_out": 9250},
                 'LTV': {"n_bins": 15, "left_out": None, "right_out": 85},
                 'RetentionRate': {"n_bins": 10, "left_out": 0.3, "right_out": None},
                 'RevenuePerNight': {"n_bins": 15, "left_out": None, "right_out": 1200},
                 'RevenuePerPersonNight': {"n_bins": 15, "left_out": None, "right_out": 1000},
                 'PreferenceScore': {"n_bins": 15, "left_out": None, "right_out": 3.5}}

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
