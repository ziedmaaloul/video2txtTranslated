## Extract and Translate Speech from Video

To Run Using Docker

Build Docker Image 
```sh
docker build -t maaloulmz/video2txttranslated -f Dockerfile .
```

RUN Container and extract speech


```sh
docker run -it --rm -v /path/to/video2txttranslated/neuralink.mp4:/input/neuralink.mp4 -v /path/to/video2txttranslated/neuralink/:/output/ maaloulmz/video2txttranslated sh /input/script.sh /input/neuralink.mp4 french /output/
```
