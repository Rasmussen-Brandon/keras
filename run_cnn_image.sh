#!/bin/bash
sudo nvidia-docker run -v $(pwd):/notebooks -it -p 8888:8888 --rm brandonrasmussen/cnn_gpu:latest
sudo pip install --upgrade keras

