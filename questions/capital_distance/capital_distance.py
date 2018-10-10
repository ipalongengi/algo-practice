T = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]

def solution(arr):
    # find the distance of each city from the capital
    city_distances = [0] * len(arr)
    
    for i in range(len(arr)):
        counter = 0
        current_idx = i

        while arr[current_idx] != current_idx:
            counter += 1
            current_idx = arr[current_idx]
        
        city_distances[i] = counter

    # create a frequency list 
    frequency = [0] * (len(arr) - 1)
    
    for distance in city_distances:
        if distance == 0:
            continue
        else:
            frequency[distance - 1] += 1

    return frequency
            
print(solution(T))