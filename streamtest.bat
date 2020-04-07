cd\
cd gstreamer
cd 1.0
cd x86_64
cd bin
gst-launch-1.0 udpsrc port=5000 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! autovideosink