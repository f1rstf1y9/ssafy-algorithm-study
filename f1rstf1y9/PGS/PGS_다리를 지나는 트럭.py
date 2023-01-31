def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge = [0]*(bridge_length-1) + truck_weights
    sum_bridge = truck_weights[0]
    while bridge:
        answer += 1
        sum_bridge -= bridge[0]
        bridge.pop(0)
        if len(bridge) >= bridge_length:
            if sum_bridge + bridge[bridge_length-1] > weight:
                bridge.insert(bridge_length-1, 0)
            else:
                sum_bridge += bridge[bridge_length-1]
    return answer