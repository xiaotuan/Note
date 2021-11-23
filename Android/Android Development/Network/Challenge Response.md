<center><b>挑战字请求流程</b></center>

```sequence
CLIENT->SERVER: ① Client requests a server resource
SERVER->CLIENT: ② Server sends a challenge string C
CLIENT->SERVER: ③ Client generates a random string R\n④ Client generates a hash  baseed or C,R\n⑤ nand the user password;Client sends R and the ahsh of the server
SERVER->CLIENT: ⑥ Server calculates hash based or stored user password and R\n⑦ Server sends back authorization status to client
```

