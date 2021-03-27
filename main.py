import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')

import logging
logger = logging.getLogger(__name__)

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

from providers.googletrans import Translator
from tools import bool_parser, pack_languages
'''
import threading
import queue
q = queue.Queue()
'''
import time
# Imports >
translator = Translator()
LANGUAGES = {}
FROM = "auto"

class TranslatorExtension(Extension):
    def __init__(self):
        super(TranslatorExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
        self.subscribe(SystemExitEvent, SystemExitEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent, PreferencesUpdateListener())
        
class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument()
        results = []
        items=[]
        if query!="" or len(query)>0:
            results.append(translator.translate(text=query,src=FROM,dest=LANGUAGES["lang1"]))
            results.append(translator.translate(text=query,src=FROM,dest=LANGUAGES["lang2"]))
            results.append(translator.translate(text=query,src=FROM,dest=LANGUAGES["lang3"]))
            results.append(translator.translate(text=query,src=FROM,dest=LANGUAGES["lang4"]))
            results.append(translator.translate(text=query,src=FROM,dest=LANGUAGES["lang5"]))
            for i in range(5):
                items.append(ExtensionResultItem(icon='images/icon.png',
                                                name=results[i].text,
                                                description=results[i].pronunciation,
                                                on_enter=ExtensionCustomAction(i,keep_app_open=True)))

        return RenderResultListAction(items)
class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        data = event.get_data()

class PreferencesUpdateListener(EventListener):
    def on_event(self, event, extension):
        pass
        
        #event.old_value

class PreferencesEventListener(EventListener):
    def on_event(self, event,extension):
        global FROM
        preferences_updater(event.preferences)

class SystemExitEventListener(EventListener):    
    pass #TODO

def thread_manager():
    pass #TODO

def preferences_updater(preferences):
    global LANGUAGES
    LANGUAGES = pack_languages(preferences["lang2trans1"],preferences["lang2trans2"],preferences["lang2trans3"],preferences["lang2trans4"],preferences["lang2trans5"])
    
    FROM = preferences["lang4trans"]
    
if __name__ == '__main__':
    TranslatorExtension().run()