from enigma import eDVBResourceManager
from Tools.Directories import fileExists, resolveFilename, SCOPE_SKIN
from Tools.HardwareInfo import HardwareInfo
from os import path
from boxbranding import getBoxType

SystemInfo = { }

#FIXMEE...
def getNumVideoDecoders():
	idx = 0
	while fileExists("/dev/dvb/adapter0/video%d"% idx, 'f'):
		idx += 1
	return idx

SystemInfo["NumVideoDecoders"] = getNumVideoDecoders()
SystemInfo["CanMeasureFrontendInputPower"] = eDVBResourceManager.getInstance().canMeasureFrontendInputPower()


def countFrontpanelLEDs():
	leds = 0
	if fileExists("/proc/stb/fp/led_set_pattern"):
		leds += 1

	while fileExists("/proc/stb/fp/led%d_pattern" % leds):
		leds += 1

	return leds

SystemInfo["NumFrontpanelLEDs"] = countFrontpanelLEDs()
SystemInfo["FrontpanelDisplay"] = fileExists("/dev/dbox/oled0") or fileExists("/dev/dbox/lcd0")
SystemInfo["FrontpanelDisplayGrayscale"] = fileExists("/dev/dbox/oled0")
SystemInfo["OledDisplay"] = fileExists(resolveFilename(SCOPE_SKIN, 'display/skin_display_picon.xml')) or fileExists(resolveFilename(SCOPE_SKIN, 'vfd_skin/skin_display_no_picon.xml'))
SystemInfo["TextDisplay"] = fileExists(resolveFilename(SCOPE_SKIN, 'display/skin_text_clock.xml'))
SystemInfo["DeepstandbySupport"] = HardwareInfo().has_deepstandby()
SystemInfo["WOL"] = fileExists("/proc/stb/fp/wol")
SystemInfo["HDMICEC"] = (path.exists("/dev/hdmi_cec") or path.exists("/dev/misc/hdmi_cec0")) and fileExists("/usr/lib/enigma2/python/Plugins/SystemPlugins/HdmiCEC/plugin.pyo")
SystemInfo["SABSetup"] = fileExists("/usr/lib/enigma2/python/Plugins/SystemPlugins/SABnzbd/plugin.pyo")
SystemInfo["SeekStatePlay"] = False
SystemInfo["GraphicLCD"] = getBoxType() == "vuultimo"
SystemInfo["Blindscan"] = fileExists("/usr/lib/enigma2/python/Plugins/SystemPlugins/Blindscan/plugin.pyo")
SystemInfo["Satfinder"] = fileExists("/usr/lib/enigma2/python/Plugins/SystemPlugins/Satfinder/plugin.pyo")
SystemInfo["GBWOL"] = fileExists("/usr/bin/gigablue_wol")
SystemInfo["Fan"] = fileExists("/proc/stb/fp/fan")
SystemInfo["FanPWM"] = SystemInfo["Fan"] and fileExists("/proc/stb/fp/fan_pwm")