import xbmc
import xbmcaddon
import xbmcvfs
import os

addon = xbmcaddon.Addon()
addon_path = xbmcvfs.translatePath(addon.getAddonInfo('path'))
addon_data_path = xbmcvfs.translatePath(addon.getAddonInfo('profile'))

# Check if this is the first run
if not addon.getSetting('first_run') == 'true':
    # Copy settings.xml to addon_data directory
    source = os.path.join(addon_path, 'settings.xml')
    destination = os.path.join(addon_data_path, 'settings.xml')
    xbmcvfs.copy(source, destination)
    
    # Set first_run to true
    addon.setSetting('first_run', 'true')

    # Reload the addon to apply new settings
    xbmc.executebuiltin('LoadProfile(Master)')