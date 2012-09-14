from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation import Link

from .permissions import (PERMISSION_OCR_DOCUMENT,
    PERMISSION_OCR_DOCUMENT_DELETE, PERMISSION_OCR_QUEUE_ENABLE_DISABLE,
    PERMISSION_OCR_CLEAN_ALL_PAGES)
from .models import OCRProcessingSingleton
from .icons import icon_submit_document, icon_ocr_cleanup

def is_enabled(context):
    return OCRProcessingSingleton.get().is_enabled()

def is_disabled(context):
    return not OCRProcessingSingleton.get().is_enabled()
    
    
#ocr_log = Link(text=_(u'queue document list'), view='ocr_log', sprite='text', permissions=[PERMISSION_OCR_DOCUMENT])
#ocr_disable = Link(text=_(u'disable OCR processing'), view='ocr_disable', sprite='control_stop_blue', permissions=[PERMISSION_OCR_QUEUE_ENABLE_DISABLE], conditional_disable=is_disabled)
#ocr_enable = Link(text=_(u'enable OCR processing'), view='ocr_enable', sprite='control_play_blue', permissions=[PERMISSION_OCR_QUEUE_ENABLE_DISABLE], conditional_disable=is_enabled)
submit_document = Link(text=_('submit to OCR queue'), view='submit_document', args='object.id', icon=icon_submit_document, permissions=[PERMISSION_OCR_DOCUMENT])
submit_document_multiple = Link(text=_('submit to OCR queue'), view='submit_document_multiple', icon=icon_submit_document, permissions=[PERMISSION_OCR_DOCUMENT])

all_document_ocr_cleanup = Link(text=_(u'clean up pages content'), view='all_document_ocr_cleanup', icon=icon_ocr_cleanup, permissions=[PERMISSION_OCR_CLEAN_ALL_PAGES], description=_(u'Runs a language filter to remove common OCR mistakes from document pages content.'))

#ocr_tool_link = Link(text=_(u'OCR'), view='ocr_log', sprite='hourglass', icon='text.png', permissions=[PERMISSION_OCR_DOCUMENT])  # children_view_regex=[r'queue_', r'document_queue'])