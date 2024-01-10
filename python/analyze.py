import pandas as pd
import matplotlib.pyplot as plt
import re

# 로그 파일 읽기
with open('logs/main.log', 'r') as file:
    log_data = file.readlines()

# 데이터 파싱
data = {'timestamp': [], 'type': [], 'method': [], 'duration': [], 'cpu_clock': [], 'cpu_core': []}
for line in log_data:
    match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}):INFO:(\w+) (\w+): (\d+\.\d+) seconds \[CPU Clock: (\d+\.\d+)Hz, CPU Core: (\d+)\]', line)
    if match:
        data['timestamp'].append(match.group(1))
        data['type'].append(match.group(2))
        data['method'].append(match.group(3))
        data['duration'].append(float(match.group(4)))
        data['cpu_clock'].append(float(match.group(5)))
        data['cpu_core'].append(int(match.group(6)))

# 데이터프레임 생성
df = pd.DataFrame(data)

# 데이터 시각화
df.groupby(['type', 'method'])['duration'].mean().unstack().plot(kind='bar')
plt.ylabel('Average Duration (seconds)')
plt.xticks(rotation=0)
plt.show()