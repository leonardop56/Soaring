import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            '100m_u_component_of_wind', '100m_v_component_of_wind', 
            '10m_u_component_of_wind', '10m_v_component_of_wind', 
            '2m_temperature', 'sea_surface_temperature', 
            'mean_sea_level_pressure', 'instantaneous_surface_sensible_heat_flux',
            'boundary_layer_height', 'convective_available_potential_energy',
        ],
       'year': [
            '2019', '2020',
        ],
        'month': [
            '05','06', '07',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': [
            54.25, 3.25, 51,
            7,
        ],
    },
    '/media/leo/Extreme SSD/ERA5/North_Sea_2019_2020.nc')
