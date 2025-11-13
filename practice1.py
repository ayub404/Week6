readings = [
	('SensorB', 25.4),
	('SensorA', 22.1),
	('SensorB', 26.1), # New max for SensorB
	('SensorC', 30.5),
	('SensorA', 21.9), # Lower than previous SensorA reading
	('SensorB', 25.9)
]

def summarize_sensor_data(reading):
    if not reading:
        return []
    reading.sort()
    sorted_list = []
    current_id = reading[0][0]
    
    for i in range( 1,len(reading)):
        if reading[i][0] != current_id:
            sorted_list.append(reading[i-1])
            current_id = reading[i][0]
    sorted_list.append(reading[-1])
    return sorted_list


    
    

print(summarize_sensor_data(readings))
print(summarize_sensor_data([]))




