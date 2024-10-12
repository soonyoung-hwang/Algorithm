def solution(play_time, adv_time, logs):
    def to_seconds(time_format):
        h, m, s = map(int, time_format.split(":"))
        return h * 3600 + m * 60 + s
    
    def to_times(seconds):
        h = seconds // 3600
        m = (seconds - 3600 * h) // 60
        s = seconds % 60
        return f'{h:02d}:{m:02d}:{s:02d}'
    
    # step 1 : find num of watchers accumulated sum
    watchers = [0 for _ in range(to_seconds(play_time))]
    N, M, A = len(watchers), len(logs), to_seconds(adv_time)
    
    for log in logs:
        fr, to = log.split("-")
        fr_sec = to_seconds(fr)
        to_sec = to_seconds(to)
        watchers[fr_sec] += 1
        if(to_sec < N):
            watchers[to_sec] -= 1
            
    for i in range(1, N):
        watchers[i] += watchers[i-1]
        
    # step 2 : shifted-window
    temp_time = 0
    for i in range(A):
        temp_time += watchers[i]
    
    max_time = temp_time
    answer = 0

    for i in range(1, N - A + 1):
        temp_time -= watchers[i-1]
        temp_time += watchers[A+i-1]
        if (max_time < temp_time):
            max_time = temp_time
            answer = i
            
    return to_times(answer)