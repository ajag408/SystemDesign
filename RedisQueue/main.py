from redis import Redis
from rq import Queue
from image_downloader import download_image

f = Queue(connection=Redis())
f.enqueue(
    download_image,
    "http://www.lenna.org/lena_std.tif",
)