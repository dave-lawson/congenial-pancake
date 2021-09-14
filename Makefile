lint:
	python3 -m flake8 .

test:
	pytest-3 -W ignore::DeprecationWarning

REV = $(shell git rev-parse --short HEAD)

docker-build:
	sudo docker build -t do-$(REV) .

docker-run:
	sudo docker run do-$(REV)
