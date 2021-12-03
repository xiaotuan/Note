[toc]

### 1. Apk 写法

```bp
android_app {
	name: "SystemUI",	// 模块名称
	resource_dirs: ["res"], // 资源目录列表
	src: ["src/**/*.java"],	// 源代码列表
	platform_apis: true,	// 平台api
	certificate: "platform",	// 签名方式
	optimize: {
		proguard_flags_files: ["proguard.flags"],	// 混淆文件列表
	}
	static_libs: ["SystemUI-core"],	// 静态库列表
	jni_libs: ["libbluetooth_jni"],	// JNI 共享库列表
}
```

