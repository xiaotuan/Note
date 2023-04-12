`FFmpeg` 不仅仅支持本地的多媒体处理，而且还支持网络流媒体的处理，支持的网络流媒体协议相对来说也很全面，可以通过命令 `./configure --list-protocols` 查看：

```shell
$ ./configure --list-protocols 
async                   ffrtmphttp              icecast                 librtmpte               prompeg                 srtp
bluray                  file                    ipfs_gateway            libsmbclient            rtmp                    subfile
cache                   ftp                     ipns_gateway            libsrt                  rtmpe                   tcp
concat                  gopher                  libamqp                 libssh                  rtmps                   tee
concatf                 gophers                 librist                 libzmq                  rtmpt                   tls
crypto                  hls                     librtmp                 md5                     rtmpte                  udp
data                    http                    librtmpe                mmsh                    rtmpts                  udplite
fd                      httpproxy               librtmps                mmst                    rtp                     unix
ffrtmpcrypt             https                   librtmpt                pipe                    sctp
```

