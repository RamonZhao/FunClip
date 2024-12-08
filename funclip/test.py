import os

if __name__ == '__main__':
    # IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')
    IMAGEMAGICK_BINARY = 'E:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe'
    print("1"+IMAGEMAGICK_BINARY)

    FFMPEG_BINARY = os.getenv('FFMPEG_BINARY', 'ffmpeg-imageio')

    print("2"+FFMPEG_BINARY)