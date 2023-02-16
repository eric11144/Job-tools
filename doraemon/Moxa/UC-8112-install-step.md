# UC-8112

## Run docker image of debian problem

1. 將 `FB_UC8100_V2.0_Build_17042015.img` image 燒錄進 sd card 中
2. 開機後 `ssh` 進入 `UC-8100`，並安裝 `docker-ce`

	```
	$ sudo apt-get update
    $ sudo apt-get install \
     	apt-transport-https \
     	ca-certificates \
     	curl \
     	gnupg2 \
     	software-properties-common
    $ curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
    $ echo "deb [arch=armhf] https://download.docker.com/linux/debian \
     	$(lsb_release -cs) stable" | \
    	sudo tee /etc/apt/sources.list.d/docker.list
    $ sudo apt-get update
    $ sudo apt-get install docker-ce
	```

3. Run without `-it` behaves good.

    ```
    $ sudo docker run arm32v6/bash echo hello world
    hello world
    ```

4. Run with `-it` causes `"open /dev/ptmx"` error.

    ```
    $ sudo docker run -it arm32v6/bash
    docker: Error response from daemon: oci runtime error: container_linux.go:262: starting container process caused "process_linux.go:339: container init caused \"open /dev/ptmx: no such file or directory\"".
    ERRO[0001] error waiting for container: context canceled
    ```
s