import os
import re

import yt_dlp


def download_audio(url, output_path='macro/file'):
    """
    YouTube 영상의 음원만 다운로드하는 함수

    Args:
        url: 다운로드할 영상 URL
        output_path: 저장할 경로 (기본값: 'macro/file')
    """
    # file 디렉토리가 없으면 생성
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 영상 정보 추출
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)

        # 가수 정보 추출
        artists = info.get('artists', [])
        if isinstance(artists, list) and len(artists) > 0:
            artist = artists[0]
        else:
            artist = info.get('artist', '') or info.get(
                'uploader', '') or info.get('channel', 'Unknown')

        # 제목은 원본 title 사용 (사이트 제목 그대로)
        title = info.get('title', 'Unknown')

        # 파일명에 사용 불가능한 문자 제거
        def clean_filename(name):
            return re.sub(r'[\\/*?:"<>|]', '', name)

        artist = clean_filename(artist)
        title = clean_filename(title)

        filename = f"{artist} - {title}"

        print(f"가수: {artist}")
        print(f"제목: {title}")
        print(f"파일명: {filename}.mp3")

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_path}/{filename}.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"다운로드 시작: {url}")
            ydl.download([url])
            print("다운로드 완료!")
    except Exception as e:
        print(f"오류 발생: {e}")


# 사용 예시
if __name__ == "__main__":
    video_url = "https://music.youtube.com/watch?v=VhEoCOWUtcU&si=Kbxiy7sNQKeVrD2X"
    download_audio(video_url)
