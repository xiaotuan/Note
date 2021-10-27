使用自定义签名文件编译软件后，生成的 otatools 目录中的签名文件与自定义签名文件不同造成的，因此在使用 otatools 生成差分包前需要将 `build/make/target/product/security/release` 目录下的 `releasekey.pk8` 和 `releasekey.x509.pem` 文件拷贝到 `otatools/build/make/target/product/security/release` 目录下覆盖对应的文件，再使用 otatools 制作差分包。

