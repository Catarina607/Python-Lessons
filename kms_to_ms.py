
k = float(input('write distance: '))

delta_time = float(input('write total hour: '))

velocity_km = k/delta_time
m = velocity_km/3.6
km_h = m * 3.6

print(velocity_km,  'km/h')
print(m,  'm/s')
print(km_h,  'km/h')
