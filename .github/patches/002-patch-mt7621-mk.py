#!/usr/bin/env python3
import pathlib, sys

mk = pathlib.Path("target/linux/ramips/image/mt7621.mk")
text = mk.read_text()

entry = (
    "define Device/gainstrong_oolite-v8\n"
    "  $(Device/dsa-migration)\n"
    "  DEVICE_VENDOR := GainStrong\n"
    "  DEVICE_MODEL := Oolite V8.X\n"
    "  DEVICE_PACKAGES := kmod-usb3 kmod-mmc-mtk -wpad-openssl -uboot-envtools\n"
    "  IMAGE_SIZE := 32448k\n"
    "endef\n"
    "TARGET_DEVICES += gainstrong_oolite-v8\n\n"
)

# Insert alphabetically before gehua_ghl-r-001
anchor = "define Device/gehua_ghl-r-001"
if anchor not in text:
    print(f"ERROR: anchor '{anchor}' not found in mt7621.mk", file=sys.stderr)
    sys.exit(1)

if "gainstrong_oolite-v8" in text:
    print("Entry already present, skipping.")
else:
    mk.write_text(text.replace(anchor, entry + anchor))
    print("Device entry inserted successfully.")
