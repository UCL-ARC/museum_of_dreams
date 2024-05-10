from .film_admin import FilmAdmin, FilmAnalysisInline, TRInline
from .teaching_analysis_admin import (
    AnalysisAdmin,
    AnalysisAdminForm,
    TRAnalysisInline,
    TRAdminForm,
    TeachingResourcesAdmin,
)
from .bibliography_admin import BibliographyItemAdmin
from .link_admin import (
    SourceInline,
    SourceAdmin,
    ScriptAdmin,
    ScriptInline,
    PressBookInline,
    PressBookAdmin,
    ProgrammeInline,
    ProgrammeAdmin,
    PublicityInline,
    PublicityAdmin,
    StillInline,
    StillAdmin,
    DrawingInline,
    DrawingAdmin,
    VideoInline,
    OtherLinkInline,
    OtherLinkAdmin,
    VideoAdmin,
    PostcardInline,
    PostcardAdmin,
    TagAdmin,
)
from .note_admin import ProjectNoteAdmin

__all__ = [
    "BibliographyItemAdmin",
    "FilmAdmin",
    "FilmAnalysisInline",
    "TRInline",
    "AnalysisAdmin",
    "AnalysisAdminForm",
    "TRAnalysisInline",
    "TRAdminForm",
    "TeachingResourcesAdmin",
    "SourceInline",
    "SourceAdmin",
    "ScriptAdmin",
    "ScriptInline",
    "PressBookInline",
    "PressBookAdmin",
    "ProgrammeInline",
    "ProgrammeAdmin",
    "PublicityInline",
    "PublicityAdmin",
    "StillInline",
    "StillAdmin",
    "DrawingInline",
    "DrawingAdmin",
    "VideoInline",
    "VideoAdmin",
    "OtherLinkInline",
    "OtherLinkAdmin",
    "VideoAdmin",
    "PostcardInline",
    "PostcardAdmin",
    "TagAdmin",
    "CustomUserAdmin",
    "ProjectNoteAdmin",
]
