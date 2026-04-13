#
# Copyright (C) 2025 superice119
#
# This is free software, licensed under the GNU General Public License v2.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=packet-forwarder
PKG_VERSION:=4.0.1
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=https://github.com/Lora-net/packet_forwarder.git
PKG_SOURCE_VERSION:=v4.0.1
PKG_MIRROR_HASH:=skip

PKG_MAINTAINER:=superice119
PKG_LICENSE:=BSD-3-Clause
PKG_LICENSE_FILES:=LICENSE

include $(INCLUDE_DIR)/package.mk

# LGW_PATH points to the staging area populated by lora-gateway's InstallDev
LGW_PATH:=$(STAGING_DIR)/usr/lib/loragw

define Package/packet-forwarder
  SECTION:=net
  CATEGORY:=Network
  SUBMENU:=LoRa
  TITLE:=LoRa packet forwarder (SX1301)
  DEPENDS:=+lora-gateway
  URL:=https://github.com/Lora-net/packet_forwarder
endef

define Package/packet-forwarder/description
  Legacy LoRa packet forwarder for SX1301-based gateways.
  Forwards LoRa packets to a network server via UDP.
  Depends on lora-gateway (libloragw / SX1301 HAL).
endef

define Build/Compile
	$(MAKE) -C $(PKG_BUILD_DIR)/lora_pkt_fwd \
		CROSS_COMPILE="$(TARGET_CROSS)" \
		ARCH="$(ARCH)" \
		LGW_PATH="$(LGW_PATH)"

	$(MAKE) -C $(PKG_BUILD_DIR)/util_ack \
		CROSS_COMPILE="$(TARGET_CROSS)" \
		ARCH="$(ARCH)" \
		LGW_PATH="$(LGW_PATH)"
endef

define Package/packet-forwarder/install
	$(INSTALL_DIR) $(1)/usr/sbin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/lora_pkt_fwd/lora_pkt_fwd $(1)/usr/sbin/

	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/util_ack/util_ack $(1)/usr/bin/

	$(INSTALL_DIR) $(1)/etc/lora
	$(CP) $(PKG_BUILD_DIR)/lora_pkt_fwd/global_conf.json* \
		$(1)/etc/lora/ 2>/dev/null || true

	$(INSTALL_DIR) $(1)/etc/init.d
	$(INSTALL_BIN) ./files/lora_pkt_fwd.init $(1)/etc/init.d/lora_pkt_fwd
endef

$(eval $(call BuildPackage,packet-forwarder))
