include $(TOPDIR)/rules.mk

PKG_NAME:=basicstation
PKG_VERSION:=2.0.6
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=https://github.com/lorabasics/basicstation.git
PKG_SOURCE_VERSION:=v$(PKG_VERSION)
PKG_MIRROR_HASH:=skip

PKG_BUILD_PARALLEL:=1
PKG_BUILD_FLAGS:=no-mips16

include $(INCLUDE_DIR)/package.mk

define Package/basicstation
  SECTION:=net
  CATEGORY:=Network
  TITLE:=LoRa Basics Station (SX1302 corecell)
  URL:=https://github.com/lorabasics/basicstation
  DEPENDS:=+libpthread +librt
endef

define Package/basicstation/description
  LoRa Basics Station - LoRaWAN gateway software supporting LNS and CUPS.
  Built for SX1302-based USB gateways (corecell platform).
endef

define Build/Configure
	# musl libc fixes:
	# 1. fd_set/select() requires explicit sys/select.h (not transitive in musl)
	# 2. argp.h is GNU-only; CFG_argp activates basicstation's built-in argp.c
	echo 'CFLAGS.corecell = -include sys/select.h -DCFG_argp' > $(PKG_BUILD_DIR)/setup-corecell.gmk
endef

define Build/Compile
	export STAGING_DIR=$(STAGING_DIR); \
	$(MAKE) -C $(PKG_BUILD_DIR) \
		platform=corecell \
		variant=std \
		TOOLPREFIX="$(TARGET_CROSS)" \
		$(if $(MAKE_JOBSERVER),$(MAKE_JOBSERVER),-j$(shell nproc))
endef

define Package/basicstation/install
	$(INSTALL_DIR) $(1)/usr/sbin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/build-corecell-std/bin/station $(1)/usr/sbin/station
	$(INSTALL_DIR) $(1)/etc/basicstation
	$(INSTALL_DIR) $(1)/etc/init.d
	$(INSTALL_BIN) ./files/basicstation.init $(1)/etc/init.d/basicstation
endef

$(eval $(call BuildPackage,basicstation))
