#!/bin/bash
sudo nvidia-docker run -v $(pwd):/notebooks -it -p 8080:8888 --rm cspinc/big_docker:latest

