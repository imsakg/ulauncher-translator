import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')

import logging

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction 
from ulauncher.search.Query import Query
from ulauncher.api.shared.action.ExtensionCustomAction import (
    ExtensionCustomAction,
    ItemEnterEvent
)
from ulauncher.api.shared.event import (
    ItemEnterEvent,
    KeywordQueryEvent,
    SystemExitEvent,
    PreferencesUpdateEvent,
    PreferencesEvent,
    BaseEvent
)
def pack_languages(lang1,lang2,lang3,lang4,lang5):
    return {"lang1":lang1,"lang2":lang2,"lang3":lang3,"lang4":lang4,"lang5":lang5}
    
def bool_parser(text):
    if text == "true":
        return True
    elif text == "false":
        return False
    else:
        return None