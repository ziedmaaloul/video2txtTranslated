FROM python:3.7

COPY . /input/

RUN pip install --upgrade pip && \
    pip install google_trans_new && \
    pip install requests && \
    python -m pip install requests && \
    pip install six && \
    pip install moviepy && \
    pip install speechrecognition pydub && \
    mkdir /output
RUN chmod +x /input/script.sh
CMD /bin/bash
RUN apt update && apt install -yq ffmpeg