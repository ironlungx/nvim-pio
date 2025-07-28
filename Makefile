all:
	pio run -t upload -t monitor

build:
	pio run

upload:
	pio run -t upload

uploadfs:
	pio run -t uploadfs

monitor:
	pio run -t monitor

compiledb:
	pio project init --ide vim
	pio run -t compiledb

home:
	pio home --shutdown-timeout 1

clean:
	pio run -t clean
