def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    def to_minutes(input_time):
        a, b = map(int,input_time.split(":"))
        return a*60 + b
    
    video_len = to_minutes(video_len)
    pos = to_minutes(pos)
    op_start = to_minutes(op_start)
    op_end = to_minutes(op_end)
    
    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if command == "prev":
            pos = max(0, pos-10)
        elif command == "next":
            pos = min(video_len, pos+10)
        if op_start < pos < op_end:
            pos = op_end
    
    answer = f"{pos//60:02d}" + ":" + f"{pos%60:02d}"
    
    return answer