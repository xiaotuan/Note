[toc]

> 摘自：<https://docs.oracle.com/javase/10/docs/specs/security/standard-names.html#cipher-algorithm-names>

## `Cipher` Algorithm Names

The following names can be specified as the *algorithm* component in a [transformation](https://docs.oracle.com/javase/10/docs/api/javax/crypto/Cipher.html) when requesting an instance of `Cipher`.

| Algorithm Name                                               | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| AES                                                          | Advanced Encryption Standard as specified by NIST in [FIPS 197](http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf). Also known as the Rijndael algorithm by Joan Daemen and Vincent Rijmen, AES is a 128-bit block cipher supporting keys of 128, 192, and 256 bits.  To use the AES cipher with only one valid key size, use the format AES_\<n>, where \<n> can be 128, 192 or 256. |
| AESWrap                                                      | The AES key wrapping algorithm as described in [RFC 3394](http://tools.ietf.org/html/rfc3394).  To use the AESWrap cipher with only one valid key size, use the format AESWrap_\<n>, where \<n> can be 128, 192, or 256. |
| ARCFOUR                                                      | A stream cipher believed to be fully interoperable with the RC4 cipher developed by Ron Rivest. For more information, see K. Kaukonen and R. Thayer, ["A Stream Cipher Encryption Algorithm 'Arcfour'"](https://tools.ietf.org/id/draft-kaukonen-cipher-arcfour-03.txt), Internet Draft (expired). |
| Blowfish                                                     | The [Blowfish block cipher](http://www.schneier.com/blowfish.html) designed by Bruce Schneier. |
| DES                                                          | The Digital Encryption Standard as described in [FIPS PUB 46-3](http://csrc.nist.gov/publications/fips/fips46-3/fips46-3.pdf). |
| DESede                                                       | Triple DES Encryption (also known as DES-EDE, 3DES, or Triple-DES). Data is encrypted using the DES algorithm three separate times. It is first encrypted using the first subkey, then decrypted with the second subkey, and encrypted with the third subkey. |
| DESedeWrap                                                   | The DESede key wrapping algorithm as described in [RFC 3217](http://tools.ietf.org/html/rfc3217). |
| ECIES                                                        | Elliptic Curve Integrated Encryption Scheme                  |
| PBEWith\<digest>And\<encryption> PBEWith\<prf>And\<encryption> | The password-based encryption algorithm defined in PKCS #5, using the specified message digest (\<digest>) or pseudo-random function (\<prf>) and encryption algorithm (\<encryption>). Examples:  <br/>**PBEWithMD5AndDES**: The password-based encryption algorithm as defined in RSA Laboratories, ["PKCS #5: Password-Based Encryption Standard," version 1.5, Nov 1993](http://www.emc.com/emc-plus/rsa-labs/standards-initiatives/pkcs-5-password-based-cryptography-standard.htm). Note that this algorithm implies [CBC](https://docs.oracle.com/javase/10/docs/specs/security/standard-names.html#cbc) as the cipher mode and [PKCS5Padding](https://docs.oracle.com/javase/10/docs/specs/security/standard-names.html#pkcs5padding) as the padding scheme and cannot be used with any other cipher modes or padding schemes.  <br/>**PBEWithHmacSHA256AndAES_128**: The password-based encryption algorithm as defined in RSA Laboratories, ["PKCS #5: Password-Based Cryptography Standard," version 2.0, September 2000](http://www.emc.com/emc-plus/rsa-labs/standards-initiatives/pkcs-5-password-based-cryptography-standard.htm). |
| RC2                                                          | Variable-key-size encryption algorithms developed by Ron Rivest for RSA Data Security, Inc. |
| RC4                                                          | Variable-key-size encryption algorithms developed by Ron Rivest for RSA Data Security, Inc. (See note prior for ARCFOUR.) |
| RC5                                                          | Variable-key-size encryption algorithms developed by Ron Rivest for RSA Data Security, Inc. |
| RSA                                                          | The RSA encryption algorithm as defined in [PKCS #1](http://tools.ietf.org/html/rfc2437) |

## `Cipher` Algorithm Modes

The following names can be specified as the *mode* component in a [transformation](https://docs.oracle.com/javase/10/docs/api/javax/crypto/Cipher.html) when requesting an instance of `Cipher`.

| Algorithm Name | Description                                                  |
| :------------- | :----------------------------------------------------------- |
| NONE           | No mode.                                                     |
| CBC            | Cipher Block Chaining Mode, as defined in [FIPS PUB 81](http://csrc.nist.gov/publications/fips/fips81/fips81.htm). |
| CCM            | Counter/CBC Mode, as defined in [NIST Special Publication SP 800-38C](http://csrc.nist.gov/publications/nistpubs/800-38C/SP800-38C_updated-July20_2007.pdf). |
| CFB, CFBx      | Cipher Feedback Mode, as defined in [FIPS PUB 81](http://csrc.nist.gov/publications/fips/fips81/fips81.htm).  Using modes such as CFB and OFB, block ciphers can encrypt data in units smaller than the cipher's actual block size. When requesting such a mode, you may optionally specify the number of bits to be processed at a time by appending this number to the mode name as shown in the "*DES/CFB8/NoPadding*" and "*DES/OFB32/PKCS5Padding*" transformations. If no such number is specified, a provider-specific default is used. (For example, the SunJCE provider uses a default of 64 bits for DES.) Thus, block ciphers can be turned into byte-oriented stream ciphers by using an 8-bit mode such as CFB8 or OFB8. |
| CTR            | A simplification of OFB, Counter mode updates the input block as a counter. |
| CTS            | Cipher Text Stealing, as described in Bruce Schneier's book *Applied Cryptography-Second Edition*, John Wiley and Sons, 1996. |
| ECB            | Electronic Codebook Mode, as defined in [FIPS PUB 81](http://csrc.nist.gov/publications/fips/fips81/fips81.htm) (generally this mode should not be used for multiple blocks of data). |
| GCM            | Galois/Counter Mode, as defined in [NIST Special Publication SP 800-38D](http://csrc.nist.gov/publications/nistpubs/800-38D/SP-800-38D.pdf). |
| OFB, OFBx      | Output Feedback Mode, as defined in [FIPS PUB 81](http://csrc.nist.gov/publications/fips/fips81/fips81.htm).  Using modes such as CFB and OFB, block ciphers can encrypt data in units smaller than the cipher's actual block size. When requesting such a mode, you may optionally specify the number of bits to be processed at a time by appending this number to the mode name as shown in the "*DES/CFB8/NoPadding*" and "*DES/OFB32/PKCS5Padding*" transformations. If no such number is specified, a provider-specific default is used. (For example, the SunJCE provider uses a default of 64 bits for DES.) Thus, block ciphers can be turned into byte-oriented stream ciphers by using an 8-bit mode such as CFB8 or OFB8. |
| PCBC           | Propagating Cipher Block Chaining, as defined by [Kerberos V4](http://web.mit.edu/kerberos/). |

## `Cipher` Algorithm Paddings

The following names can be specified as the *padding* component in a [transformation](https://docs.oracle.com/javase/10/docs/api/javax/crypto/Cipher.html) when requesting an instance of `Cipher`.

| Algorithm Name                                 | Description                                                  |
| :--------------------------------------------- | :----------------------------------------------------------- |
| NoPadding                                      | No padding.                                                  |
| ISO10126Padding                                | This padding for block ciphers is described in [5.2 Block Encryption Algorithms](http://www.w3.org/TR/xmlenc-core/#sec-Alg-Block) in the W3C "XML Encryption Syntax and Processing" document. |
| OAEPPadding, OAEPWith\<digest>And\<mgf>Padding | Optimal Asymmetric Encryption. Padding scheme defined in PKCS1, where \<digest> should be replaced by the message digest and \<mgf> by the mask generation function. Examples: **OAEPWithMD5AndMGF1Padding** and **OAEPWithSHA-512AndMGF1Padding**.  If `OAEPPadding` is used, `Cipher` objects are initialized with a `javax.crypto.spec.OAEPParameterSpec` object to supply values needed for OAEPPadding. |
| PKCS1Padding                                   | The padding scheme described in [PKCS#1](https://tools.ietf.org/html/rfc2437), used with the RSA algorithm. |
| PKCS5Padding                                   | The padding scheme described in RSA Laboratories, ["PKCS #5: Password-Based Encryption Standard, version 1.5, November 1993"](http://www.emc.com/emc-plus/rsa-labs/standards-initiatives/pkcs-5-password-based-cryptography-standard.htm). |
| SSL3Padding                                    | The padding scheme defined in the SSL Protocol Version 3.0, November 18, 1996, section 5.2.3.2 (CBC block cipher):  `block-ciphered struct {`   `opaque content[SSLCompressed.length];`   `opaque MAC[CipherSpec.hash_size];`   `uint8 padding[GenericBlockCipher.padding_length];`   `uint8 padding_length;` `} GenericBlockCipher;`  The size of an instance of a `GenericBlockCipher` must be a multiple of the block cipher's block length. The padding length, which is always present, contributes to the padding, which implies that if:  `sizeof(content) + sizeof(MAC) % block_length = 0,`  padding has to be `(block_length - 1)` bytes long, because of the existence of `padding_length`.  This makes the padding scheme similar (but not quite) to PKCS5Padding, where the padding length is encoded in the padding (and ranges from 1 to `block_length`). With the SSL scheme, the `sizeof(padding)` is encoded in the always present `padding_length` and therefore ranges from 0 to `block_length-1`. |

