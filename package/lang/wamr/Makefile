include $(TOPDIR)/rules.mk

PKG_NAME:=wamr
PKG_VERSION:=2.4.4
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=https://github.com/bytecodealliance/wasm-micro-runtime.git
PKG_SOURCE_VERSION:=WAMR-$(PKG_VERSION)
PKG_MIRROR_HASH:=skip

PKG_BUILD_PARALLEL:=1
PKG_BUILD_FLAGS:=no-mips16

include $(INCLUDE_DIR)/package.mk

define Package/wamr
  SECTION:=lang
  CATEGORY:=Languages
  TITLE:=WebAssembly Micro Runtime (iwasm)
  URL:=https://github.com/bytecodealliance/wasm-micro-runtime
  DEPENDS:=+libpthread +libdl +librt
endef

define Package/wamr/description
  WebAssembly Micro Runtime (WAMR) - lightweight WASI-capable interpreter
  for MIPS targets. Runs .wasm and pre-compiled AOT (.aot) modules.
  No JIT; interpreter + AOT loader only. Built for mipsel_24kc (MT7621).
endef

WAMR_SRC_DIR:=$(PKG_BUILD_DIR)/product-mini/platforms/linux
WAMR_BUILD_DIR:=$(PKG_BUILD_DIR)/cmake-build

define Build/Configure
	mkdir -p $(WAMR_BUILD_DIR)
	cd $(WAMR_BUILD_DIR) && \
	cmake $(WAMR_SRC_DIR) \
		-DCMAKE_SYSTEM_NAME=Linux \
		-DCMAKE_SYSTEM_PROCESSOR=mips \
		-DCMAKE_C_COMPILER="$(TARGET_CC)" \
		-DCMAKE_CXX_COMPILER="$(TARGET_CXX)" \
		-DCMAKE_AR="$(TARGET_CROSS)ar" \
		-DCMAKE_NM="$(TARGET_CROSS)nm" \
		-DCMAKE_RANLIB="$(TARGET_CROSS)ranlib" \
		-DCMAKE_FIND_ROOT_PATH="$(STAGING_DIR)" \
		-DCMAKE_FIND_ROOT_PATH_MODE_PROGRAM=NEVER \
		-DCMAKE_FIND_ROOT_PATH_MODE_LIBRARY=ONLY \
		-DCMAKE_FIND_ROOT_PATH_MODE_INCLUDE=ONLY \
		-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DCMAKE_BUILD_TYPE=Release \
		-DWAMR_BUILD_PLATFORM=linux \
		-DWAMR_BUILD_TARGET=MIPS \
		-DWAMR_BUILD_INTERP=1 \
		-DWAMR_BUILD_FAST_INTERP=1 \
		-DWAMR_BUILD_AOT=1 \
		-DWAMR_BUILD_JIT=0 \
		-DWAMR_BUILD_FAST_JIT=0 \
		-DWAMR_BUILD_LIBC_BUILTIN=1 \
		-DWAMR_BUILD_LIBC_WASI=1 \
		-DWAMR_BUILD_MULTI_MODULE=0 \
		-DWAMR_BUILD_LIB_PTHREAD=0 \
		-DWAMR_BUILD_LIB_WASI_THREADS=0 \
		-DWAMR_BUILD_SIMD=0 \
		-DWAMR_BUILD_MINI_LOADER=0 \
		-DWAMR_BUILD_REF_TYPES=1
endef

define Build/Compile
	$(MAKE) -C $(WAMR_BUILD_DIR) \
		$(if $(MAKE_JOBSERVER),$(MAKE_JOBSERVER),-j$(shell nproc))
endef

define Build/Install
	$(MAKE) -C $(WAMR_BUILD_DIR) install \
		DESTDIR=$(PKG_INSTALL_DIR)
endef

define Package/wamr/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/iwasm $(1)/usr/bin/iwasm
endef

$(eval $(call BuildPackage,wamr))
