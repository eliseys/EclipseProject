from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
#import signal, os, subprocess
#import schedule

print(gp("--auto-detect"))

print("*******************")
print("Canon EOS 7D MarkII")
print("*******************")


gp("--camera", "Canon EOS 7D MarkII", "--set-config", "capturetarget=1") # Capture Target Memory card
print(gp("--get-config", "capturetarget"))

# imgsettings

gp("--camera", "Canon EOS 7D MarkII", "--set-config", "imageformat=RAW") # Image Format 
print(gp("--camera", "Canon EOS 7D MarkII", "--get-config", "imageformat"))
gp("--camera", "Canon EOS 7D MarkII", "--set-config", "imageformatcf=RAW") # Image Format CF
print(gp("--camera", "Canon EOS 7D MarkII", "--get-config", "imageformatcf"))

gp("--camera", "Canon EOS 7D MarkII", "--set-config", "iso=100") # ISO
print(gp("--camera", "Canon EOS 7D MarkII", "--get-config", "iso"))

gp("--camera", "Canon EOS 7D MarkII", "--set-config", "whitebalance=Daylight") # WhiteBalance
print(gp("--camera", "Canon EOS 7D MarkII", "--get-config", "whitebalance"))

# capturesettings

print(gp("--camera", "Canon EOS 7D MarkII", "--get-config", "exposurecompensation"))

gp("--camera", "Canon EOS 7D MarkII", "--set-config", "highisonr=2") # High ISO Noise Reduction (2=off)
print(gp("--camera", "Canon EOS 7D MarkII", "--get-config", "highisonr"))

gp("--camera", "Canon EOS 7D MarkII", "--set-config", "drivemode=1") # Drive Mode Continuous high speed
print(gp("--camera", "Canon EOS 7D MarkII", "--get-config", "drivemode"))

gp("--camera", "Canon EOS 7D MarkII", "--set-config", "drivemode=2") # Drive Mode Continuous low speed
print(gp("--camera", "Canon EOS 7D MarkII", "--get-config", "drivemode"))

gp("--camera", "Canon EOS 7D MarkII", "--set-config", "picturestyle=Neutral") # Picture Style
print(gp("--camera", "Canon EOS 7D MarkII", "--get-config", "picturestyle"))


gp("--camera", "Canon EOS 7D MarkII", "--set-config", "shutterspeed=0.5") # Shutter Speed
print(gp("--camera", "Canon EOS 7D MarkII", "--get-config", "shutterspeed"))

gp("--camera", "Canon EOS 7D MarkII", "--set-config", "aeb=2") # Auto Exposure Bracketing
print(gp("--camera", "Canon EOS 7D MarkII", "--get-config", "aeb"))

print("*******************")
print("Canon EOS RP")
print("*******************")

gp("--camera", "USB PTP Class Camera", "--set-config", "capturetarget=1") # Capture Target Memory card
print(gp("--get-config", "capturetarget"))

# imgsettings

gp("--camera", "USB PTP Class Camera", "--set-config", "imageformat=RAW") # Image Format 
print(gp("--camera", "USB PTP Class Camera", "--get-config", "imageformat"))

gp("--camera", "USB PTP Class Camera", "--set-config", "iso=100") # ISO
print(gp("--camera", "USB PTP Class Camera", "--get-config", "iso"))

gp("--camera", "USB PTP Class Camera", "--set-config", "whitebalance=Daylight") # WhiteBalance
print(gp("--camera", "USB PTP Class Camera", "--get-config", "whitebalance"))

# capturesettings

print(gp("--camera", "USB PTP Class Camera", "--get-config", "exposurecompensation"))

gp("--camera", "USB PTP Class Camera", "--set-config", "highisonr=2") # High ISO Noise Reduction (2=off)
print(gp("--camera", "USB PTP Class Camera", "--get-config", "highisonr"))

gp("--camera", "USB PTP Class Camera", "--set-config", "drivemode=1") # Drive Mode Continuous high speed
print(gp("--camera", "USB PTP Class Camera", "--get-config", "drivemode"))

#gp("--camera", "USB PTP Class Camera", "--set-config", "drivemode=2") # Drive Mode Continuous low speed
#print(gp("--camera", "USB PTP Class Camera", "--get-config", "drivemode"))

gp("--camera", "USB PTP Class Camera", "--set-config", "picturestyle=Neutral") # Picture Style
print(gp("--camera", "USB PTP Class Camera", "--get-config", "picturestyle"))

gp("--camera", "USB PTP Class Camera", "--set-config", "shutterspeed=0.5") # Shutter Speed
print(gp("--camera", "USB PTP Class Camera", "--get-config", "shutterspeed"))

gp("--camera", "USB PTP Class Camera", "--set-config", "aeb=3") # Auto Exposure Bracketing
print(gp("--camera", "USB PTP Class Camera", "--get-config", "aeb"))

