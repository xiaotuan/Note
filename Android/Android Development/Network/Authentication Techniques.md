<center><b>Auth 请求流程</b></center>

```sequence
Web Browser->Web Server: Browser requests Secure Socket.
Web Server->Web Browser: Server responds with SSL Certificate.
Web Browser->Web Server: Session key seed is encrypted with SSL Public key and sent to server.
Web Server->Web Browser: Server indicates all future transmissions are encrypted.
Web Server->Web Browser: Server and Browser can send encrypted messages.
```

