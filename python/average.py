import re

# 로그 파일 경로
log_file_path = "logs/main.log"

# CPU 바운드 작업과 I/O 바운드 작업의 실행 시간을 저장할 변수
cpu_bound_times = []
io_bound_times = []

# 로그 파일 읽기
with open(log_file_path, "r") as file:
    # 각 줄마다 로그 정보 추출
    for line in file:
        # 로그 정보에서 실행 시간 추출
        match = re.search(r"\d+\.\d+ seconds", line)
        if match:
            time = float(match.group().split()[0])
            
            # CPU 바운드 작업인지 I/O 바운드 작업인지 확인하여 해당 리스트에 추가
            if "cpu_bound" in line:
                cpu_bound_times.append(time)
            elif "io_bound" in line:
                io_bound_times.append(time)

# CPU 바운드 작업과 I/O 바운드 작업의 평균 실행 시간 계산
avg_cpu_bound_time = sum(cpu_bound_times) / len(cpu_bound_times)
avg_io_bound_time = sum(io_bound_times) / len(io_bound_times)

# 결과 출력
print(f"CPU 바운드 작업의 평균 실행 시간: {avg_cpu_bound_time:.3f} seconds")
print(f"I/O 바운드 작업의 평균 실행 시간: {avg_io_bound_time:.3f} seconds")