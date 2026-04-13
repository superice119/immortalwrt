#
# Copyright (C) 2025 superice119
#
# This is free software, licensed under the GNU General Public License v2.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=sx1302-hal
PKG_VERSION:=2.1.0
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=https://github.com/Lora-net/sx1302_hal.git
PKG_SOURCE_VERSION:=V2.1.0
PKG_MIRROR_HASH:=skip

PKG_MAINTAINER:=superice119
PKG_LICENSE:=BSD-3-Clause
PKG_LICENSE_FILES:=LICENSE.TXT

include $(INCLUDE_DIR)/package.mk

define Package/sx1302-hal
  SECTION:=net
  CATEGORY:=Network
  SUBMENU:=LoRa
  TITLE:=SX1302/SX1303 HAL + packet forwarder
  DEPENDS:=+kmod-usb-acm
  URL:=https://github.com/Lora-net/sx1302_hal
endef

define Package/sx1302-hal/description
  Hardware Abstraction Layer for Semtech SX1302/SX1303 LoRa concentrators.
  Includes lora_pkt_fwd, chip_id, spectral_scan utilities.
  Supports USB interface (WM1303 / USB Corecell).
endef

define Build/Compile
	$(MAKE) -C $(PKG_BUILD_DIR)/libtools \
		CROSS_COMPILE="$(TARGET_CROSS)" \
		ARCH="$(ARCH)"
	$(MAKE) -C $(PKG_BUILD_DIR)/libloragw \
		CROSS_COMPILE="$(TARGET_CROSS)" \
		ARCH="$(ARCH)"
	$(MAKE) -C $(PKG_BUILD_DIR)/util_chip_id \
		CROSS_COMPILE="$(TARGET_CROSS)" \
		ARCH="$(ARCH)"
	$(MAKE) -C $(PKG_BUILD_DIR)/util_spectral_scan \
		CROSS_COMPILE="$(TARGET_CROSS)" \
		ARCH="$(ARCH)"
	$(MAKE) -C $(PKG_BUILD_DIR)/packet_forwarder \
		CROSS_COMPILE="$(TARGET_CROSS)" \
		ARCH="$(ARCH)"
endef

define Package/sx1302-hal/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/util_chip_id/chip_id $(1)/usr/bin/
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/util_spectral_scan/spectral_scan $(1)/usr/bin/

	$(INSTALL_DIR) $(1)/usr/sbin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/packet_forwarder/lora_pkt_fwd $(1)/usr/sbin/

	$(INSTALL_DIR) $(1)/etc/lora
	$(CP) $(PKG_BUILD_DIR)/packet_forwarder/global_conf.json.sx1250.* \
		$(1)/etc/lora/

	$(INSTALL_DIR) $(1)/etc/init.d
	$(INSTALL_BIN) ./files/lora_pkt_fwd.init $(1)/etc/init.d/lora_pkt_fwd
endef

$(eval $(call BuildPackage,sx1302-hal))
