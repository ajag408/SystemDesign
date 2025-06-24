from redis import Redis
from rq import Queue
from image_downloader import download_image

q = Queue(connection=Redis())
q.enqueue(
    download_image,
    "http://www.lenna.org/lena_std.tif",
)