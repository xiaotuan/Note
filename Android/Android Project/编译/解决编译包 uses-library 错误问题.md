**问题详情**
        有同事在SDK环境上将AndroidQ的Email应用搬到AndroidS上使用，使用mm命令进行编译毫无问题，可以正常生产apk，然后就自信满满提交了补丁。但是其他同事更新代码后整体编译，就报了以下的错误：

```
[ 91% 1133/1239] Verifying uses-libraries: out/target/common/obj/APPS/Email_intermediates/manifest/AndroidManifest.xml
FAILED: out/target/common/obj/APPS/Email_intermediates/enforce_uses_libraries.status
/bin/bash -c "(rm -f out/target/common/obj/APPS/Email_intermediates/enforce_uses_libraries.status ) && (build/soong/scripts/manifest_check.py     --enforce-uses-libraries        --enforce-uses-libraries-status out/target/common/obj/APPS/Email_intermediates/enforce_uses_libraries.status       --aapt out/host/linux-x86/bin/aapt                                 out/target/common/obj/APPS/Email_intermediates/manifest/AndroidManifest.xml )"
error: mismatch in the <uses-library> tags between the build system and the manifest:
        - required libraries in build system: []
                         vs. in the manifest: [org.apache.http.legacy]
        - optional libraries in build system: []
                         vs. in the manifest: []
        - tags in the manifest (out/target/common/obj/APPS/Email_intermediates/manifest/AndroidManifest.xml):
                <uses-library android:name="org.apache.http.legacy" android:required="true"/>
 
note: the following options are available:
        - to temporarily disable the check on command line, rebuild with RELAX_USES_LIBRARY_CHECK=true (this will set compiler filter "verify" and disable AOT-compilation in dexpreopt)
        - to temporarily disable the check for the whole product, set PRODUCT_BROKEN_VERIFY_USES_LIBRARIES := true in the product makefiles
        - to fix the check, make build system properties coherent with the manifest
        - see build/make/Changes.md for details
```


报错信息是执行manifest_check.py发现，声明请求使用的libraries跟AndroidManifest.xml中声明的不一致，导致的报错。

这种报错规则一般是在build系统中进行的，因此到Android的build目录下进行搜索：

    $ mgrep manifest_check.py
    ./make/core/dex_preopt_odex_install.mk:240:  my_verify_script := build/soong/scripts/manifest_check.py
    ./soong/scripts/Android.bp:80:    main: "manifest_check.py",
    ./soong/scripts/Android.bp:82:        "manifest_check.py",
    ./soong/scripts/Android.bp:102:        "manifest_check.py",

可以确定检测机制的规则是在build/./make/core/dex_preopt_odex_install.mk中定义的：

```
# Verify LOCAL_USES_LIBRARIES/LOCAL_OPTIONAL_USES_LIBRARIES against the manifest.
ifndef LOCAL_ENFORCE_USES_LIBRARIES
  LOCAL_ENFORCE_USES_LIBRARIES := true
endif
 
my_enforced_uses_libraries :=
ifeq (true,$(LOCAL_ENFORCE_USES_LIBRARIES))
  my_verify_script := build/soong/scripts/manifest_check.py
  my_uses_libs_args := $(patsubst %,--uses-library %,$(LOCAL_USES_LIBRARIES))
  my_optional_uses_libs_args := $(patsubst %,--optional-uses-library %, \
    $(LOCAL_OPTIONAL_USES_LIBRARIES))
  my_relax_check_arg := $(if $(filter true,$(RELAX_USES_LIBRARY_CHECK)), \
    --enforce-uses-libraries-relax,)
  my_dexpreopt_config_args := $(patsubst %,--dexpreopt-config %,$(my_dexpreopt_dep_configs))
 
  my_enforced_uses_libraries := $(intermediates.COMMON)/enforce_uses_libraries.status
  $(my_enforced_uses_libraries): PRIVATE_USES_LIBRARIES := $(my_uses_libs_args)
  $(my_enforced_uses_libraries): PRIVATE_OPTIONAL_USES_LIBRARIES := $(my_optional_uses_libs_args)
  $(my_enforced_uses_libraries): PRIVATE_DEXPREOPT_CONFIGS := $(my_dexpreopt_config_args)
  $(my_enforced_uses_libraries): PRIVATE_RELAX_CHECK := $(my_relax_check_arg)
  $(my_enforced_uses_libraries): $(AAPT)
  $(my_enforced_uses_libraries): $(my_verify_script)
  $(my_enforced_uses_libraries): $(my_dexpreopt_dep_configs)
  $(my_enforced_uses_libraries): $(my_manifest_or_apk)
	@echo Verifying uses-libraries: $<
	rm -f $@
	$(my_verify_script) \
	  --enforce-uses-libraries \
	  --enforce-uses-libraries-status $@ \
	  --aapt $(AAPT) \
	  $(PRIVATE_USES_LIBRARIES) \
	  $(PRIVATE_OPTIONAL_USES_LIBRARIES) \
	  $(PRIVATE_DEXPREOPT_CONFIGS) \
	  $(PRIVATE_RELAX_CHECK) \
	  $<
  $(LOCAL_BUILT_MODULE) : $(my_enforced_uses_libraries)
endif
```

当我们的Android.mk/Android.bp没有定义LOCAL_ENFORCE_USES_LIBRARIES/enforce_uses_libs，则默认开始检测机制。获取好参数后就会去执行manifest_check.py。

manifest_check.py会从参数中获取到uses_libraries的值，也就是LOCAL_USES_LIBRARIES变量的值：

    required = translate_libnames(args.uses_libraries, mod_to_lib)
    optional = translate_libnames(args.optional_uses_libraries, mod_to_lib)

然后调用enforce_uses_libraries方法去检测：

```python
       errmsg = enforce_uses_libraries(manifest, required, optional,
         args.enforce_uses_libraries_relax, is_apk, args.input)
 
 
 
def enforce_uses_libraries(manifest, required, optional, relax, is_apk, path):
  """Verify that the <uses-library> tags in the manifest match those provided
  by the build system.
  Args:
    manifest: manifest (either parsed XML or aapt dump of APK)
    required: required libs known to the build system
    optional: optional libs known to the build system
    relax:    if true, suppress error on mismatch and just write it to file
    is_apk:   if the manifest comes from an APK or an XML file
  """
  if is_apk:
    manifest_required, manifest_optional, tags = extract_uses_libs_apk(manifest)
  else:
    manifest_required, manifest_optional, tags = extract_uses_libs_xml(manifest)
 
  if manifest_required == required and manifest_optional == optional:
    return None
 
  errmsg = ''.join([
    'mismatch in the <uses-library> tags between the build system and the '
      'manifest:\n',
    '\t- required libraries in build system: [%s]\n' % ', '.join(required),
    '\t                 vs. in the manifest: [%s]\n' % ', '.join(manifest_required),
    '\t- optional libraries in build system: [%s]\n' % ', '.join(optional),
    '\t                 vs. in the manifest: [%s]\n' % ', '.join(manifest_optional),
    '\t- tags in the manifest (%s):\n' % path,
    '\t\t%s\n' % '\t\t'.join(tags),
      'note: the following options are available:\n',
    '\t- to temporarily disable the check on command line, rebuild with ',
      'RELAX_USES_LIBRARY_CHECK=true (this will set compiler filter "verify" ',
      'and disable AOT-compilation in dexpreopt)\n',
    '\t- to temporarily disable the check for the whole product, set ',
      'PRODUCT_BROKEN_VERIFY_USES_LIBRARIES := true in the product makefiles\n',
    '\t- to fix the check, make build system properties coherent with the '
      'manifest\n',
    '\t- see build/make/Changes.md for details\n'])
 
  if not relax:
    raise ManifestMismatchError(errmsg)
 
  return errmsg
```

enforce_uses_libraries 方法会从 apk 中解析出 AndroidManifest 的内容，并提取出 uses-libraries 的配置，然后跟 LOCAL_USES_LIBRARIES 中的内容进行配对，检测是否一致。如果不一致，就会报出文章开头的错误。

**解决方法**
        1.如 manifest_check.py 中报错信息的提示，方案中配置 RELAX_USES_LIBRARY_CHECK=true 或者 PRODUCT_BROKEN_VERIFY_USES_LIBRARIES := true

2. 令 LOCAL_ENFORCE_USES_LIBRARIES 的值为 false，如在`Android.mk/Android.bp` 中设置：

   ```
   mk:     LOCAL_ENFORCE_USES_LIBRARIES := false
   bp:     enforce_uses_libs: false
   ```

   或者 LOCAL_MODULE_TAGS 设置为 tests，LOCAL_COMPATIBILITY_SUITE 设置为非空。方案中设置 WITH_DEXPREOPT 为 true 等等，具体参考 `build/make/core/dex_preopt_odex_install.mk`

3. 正确设置LOCAL_USES_LIBRARIES的值。