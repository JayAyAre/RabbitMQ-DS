import random

import grpc, redis, time, pickle

time =123
while True:
    r = redis.Redis(host='localhost', port=6379)

    p111 = []
    w111 = []

    pollution = dict()
    data1 = {"id": 111, "timer_seconds": time, "value": random.uniform(0.0,2.0)}
    p111.append(data1)
    pollution[111] = p111

    wellness = dict()
    data2 = {"id": 111, "timer_seconds": time, "value": random.uniform(0.0,2.0)}
    w111.append(data2)
    wellness[111] = w111

    #pollution = {str(key): value for key, value in pollution.items()}
    #wellness = {str(key): value for key, value in wellness.items()}

    # Guardar los bytes en Redis
    pollution_bytes = pickle.dumps(pollution)
    wellness_bytes = pickle.dumps(wellness)

    r.execute_command('SET', 'pollution', pollution_bytes)
    r.execute_command('SET', 'wellness', wellness_bytes)
    #r.set('pollution',pollution)

    data3 = {"id": 111, "timer_seconds": time, "value": 23.5}
    data3_bytes = pickle.dumps(data3)
    r.append("pollution",data3_bytes)

    time +=1



