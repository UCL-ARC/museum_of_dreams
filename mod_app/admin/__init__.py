from .film_admin import FilmAdmin, FilmAnalysisInline, TRInline
from .analysis_admin import (
    AnalysisAdmin,
    AnalysisAdminForm,
    TRAnalysisInline,
)
from .additional_resources_admin import (
    TRAdminForm,
    TeachingResourcesAdmin,
    ExhibitionResourcesAdmin,
    EditedCollectionAdmin,
)
from .bibliography_admin import BibliographyItemAdmin
from .link_admin import (
    SourceInline,
    SourceAdmin,
    OtherLinkInline,
    OtherLinkAdmin,
    TagAdmin,
)
from .note_admin import ProjectNoteAdmin, FeedbackAdmin, ArchiveAdmin

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
    "ExhibitionResourcesAdmin",
    "EditedCollectionAdmin",
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
    "FeedbackAdmin",
    "ArchiveAdmin",
]
