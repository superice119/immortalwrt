#
# Copyright (C) 2025 superice119
#
# This is free software, licensed under the GNU General Public License v2.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=lora-gateway
PKG_VERSION:=5.0.1
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=https://github.com/Lora-net/lora_gateway.git
PKG_SOURCE_VERSION:=v5.0.1
PKG_MIRROR_HASH:=skip

PKG_MAINTAINER:=superice119
PKG_LICENSE:=BSD-3-Clause
PKG_LICENSE_FILES:=LICENSE

include $(INCLUDE_DIR)/package.mk

define Package/lora-gateway
  SECTION:=libs
  CATEGORY:=Libraries
  SUBMENU:=LoRa
  TITLE:=Semtech SX1301 LoRa Gateway HAL (libloragw)
  URL:=https://github.com/Lora-net/lora_gateway
endef

define Package/lora-gateway/description
  Hardware Abstraction Layer for Semtech SX1301-based LoRa concentrators.
  Provides libloragw static library and headers for packet_forwarder.
endef

define Build/Compile
	$(MAKE) -C $(PKG_BUILD_DIR)/libloragw \
		CROSS_COMPILE="$(TARGET_CROSS)" \
		ARCH="$(ARCH)"
endef

# Install headers + static lib + library.cfg to staging_dir
# so that packet-forwarder can use LGW_PATH=$(STAGING_DIR)/usr/lib/loragw
define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/lib/loragw/inc
	$(CP) $(PKG_BUILD_DIR)/libloragw/libloragw.a \
		$(1)/usr/lib/loragw/
	$(CP) $(PKG_BUILD_DIR)/libloragw/library.cfg \
		$(1)/usr/lib/loragw/
	$(CP) $(PKG_BUILD_DIR)/libloragw/inc/*.h \
		$(1)/usr/lib/loragw/inc/
endef

define Package/lora-gateway/install
	# Runtime: no shared lib needed (static); install reset script
	$(INSTALL_DIR) $(1)/usr/sbin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/reset_lgw.sh $(1)/usr/sbin/reset_lgw.sh
endef

$(eval $(call BuildPackage,lora-gateway))
