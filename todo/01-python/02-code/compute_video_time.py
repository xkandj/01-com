import os
import time
from moviepy.editor import VideoFileClip


def compute_video_time(file_path):
    type = ('.flv', '.mp4', '.ts', '.avi', '.rm', '3gp',
            '.rmvb', '.asf', '.mpg', '.wmv', 'mkv', '.vob')

    file_list = []
    for root, _, files in os.walk(file_path):
        for name in files:
            file_name = os.file_path.join(root, name)
            file_name = file_name.lower()
            if file_name.endswith(type):
                file_list.append(file_name)

    # format, <^>左中右
    print_len = 50
    print(f'{"开始视频文件统计":-^{print_len}}')
    total_time = 0.0
    count = 0
    for item in file_list:
        try:
            clip = VideoFileClip(item)
            count = count + 1
            total_time += clip.duration
            print(f"已完成{(count / len(file_list)):.2%}")
        except Exception:
            print(item)
        finally:
            # 防止出现错误：句柄无效
            clip.reader.close()
            clip.audio.reader.close_proc()

    print(f'{"视频文件统计结束":-^{print_len}}')
    print(f"文件数量：{count}")
    print(
        f"视频总时长：{total_time}秒, {time.strftime('%H:%M:%S', time.gmtime(total_time))}(时:分:秒)")


if __name__ == "__main__":
    file_path = r"c:\users\xxx\desktop\1.txt"
    compute_video_time(file_path)
