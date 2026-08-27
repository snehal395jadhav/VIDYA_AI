"""
Navneet TopTech Learning Hub — main entry point.
Run with:  streamlit run app.py
"""
from datetime import datetime, timedelta

import streamlit as st

from config import settings

st.set_page_config(
    page_title=settings.APP_NAME,
    page_icon=":material/school:",
    layout="wide",
    initial_sidebar_state="expanded",
)

from components import cards
from components.sidebar import render_sidebar
from database import crud
from database.db import get_db, init_db
from pages import (admin_panel, dashboard, flashcards, landing, login,
                   notes_library, quiz_center, settings as settings_page,
                   video_notes)

# Extra CSS layered on top when the user enables dark mode
DARK_CSS = """
<style>
.stApp { background: #101418 !important; }
:root { --plane:#101418; --surface:#1a2027; --ink:#eef1f5; --ink-2:#c0c6cf;
        --muted:#8b929c; --hairline:#2b323b; --soft:#161c23; --ice:#1d2430; --mint:#16241f; }
html, body, [class*="css"], p, li, label, h1,h2,h3,h4 { color:#eef1f5; }
section[data-testid="stSidebar"], .vm-stat, .vm-feature, .vm-note-card,
[data-testid="stMetric"], [data-testid="stExpander"], [data-testid="stChatMessage"] {
    background:#1a2027 !important; border-color:#2b323b !important; }
.vm-glass { background: rgba(26,32,39,.8) !important; border-color:#2b323b !important; }
.vm-stat-value, .vm-note-title, .vm-feature h4,
.vm-step-label, .vm-flashcard-front, .vm-section h3 { color:#eef1f5 !important; }
.vm-feature p, .vm-flashcard-back { color:#c0c6cf !important; }
.vm-flashcard { background: linear-gradient(135deg,#1a2027,#151b22) !important;
                border-color:#2b323b !important; }
.stTabs [data-baseweb="tab-list"] { background:#1a2027; border-color:#2b323b; }
.stTextInput input, .stTextArea textarea, .stNumberInput input,
.stSelectbox [data-baseweb="select"] > div {
    background:#12171d !important; color:#eef1f5 !important; border-color:#2b323b !important; }
</style>
"""


SIGNED_IN_CSS = """
<style>
section[data-testid="stSidebar"][aria-expanded="true"] {
    box-sizing: border-box !important;
    width: 280px !important;
    min-width: 280px !important;
    max-width: 280px !important;
    overflow-x: hidden !important;
    overflow-y: auto !important;
}
section[data-testid="stSidebar"][aria-expanded="true"] > div,
section[data-testid="stSidebar"][aria-expanded="true"] [data-testid="stSidebarContent"],
section[data-testid="stSidebar"][aria-expanded="true"] [data-testid="stSidebarUserContent"],
section[data-testid="stSidebar"][aria-expanded="true"] .block-container {
    width: 100% !important;
    min-width: 0 !important;
    max-width: 100% !important;
}
section[data-testid="stSidebar"][aria-expanded="true"] [data-testid="stSidebarUserContent"] {
    padding: .8rem 1rem 1rem !important;
}
section[data-testid="stSidebar"][aria-expanded="true"] [data-testid="stSidebarUserContent"]
> [data-testid="stVerticalBlock"] {
    gap: .3rem !important;
}
section[data-testid="stSidebar"] .block-container {
    padding: 0 !important;
}
section[data-testid="stSidebar"] .element-container,
section[data-testid="stSidebar"] [data-testid="stElementContainer"],
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
section[data-testid="stSidebar"] .vm-logo,
section[data-testid="stSidebar"] .vm-logo > div,
section[data-testid="stSidebar"] .vm-user-card,
section[data-testid="stSidebar"] .nav,
section[data-testid="stSidebar"] .nav-item,
section[data-testid="stSidebar"] .nav-link {
    width: 100% !important;
    max-width: 100% !important;
}
section[data-testid="stSidebar"] .nav-link {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    white-space: nowrap !important;
}
section[data-testid="stSidebar"] .vm-logo-sub {
    display: none !important;
}
section[data-testid="stSidebar"] .vm-user-card .name,
section[data-testid="stSidebar"] .vm-user-card .mail {
    white-space: normal !important;
    overflow-wrap: break-word !important;
}
section[data-testid="stSidebar"] .stButton {
    margin: 0 !important;
}
section[data-testid="stSidebar"] .stButton > button {
    min-height: 40px !important;
    padding: 8px 12px !important;
}
@media (max-width: 700px) {
    section[data-testid="stSidebar"][aria-expanded="true"] {
        width: min(280px, 84vw) !important;
        min-width: min(280px, 84vw) !important;
        max-width: min(280px, 84vw) !important;
    }
}
@media (min-width: 901px) {
    .block-container {
        width: 100% !important;
        max-width: none !important;
        padding: 1rem clamp(1rem, 2vw, 2rem) 2rem !important;
    }
}
</style>
"""

@st.cache_resource
def _bootstrap():
    """Create tables + seed admin exactly once per server process."""
    init_db()
    return True


def _session_guard() -> dict | None:
    """Return the signed-in user dict, enforcing the inactivity timeout."""
    user = st.session_state.get("user")
    if not user:
        return None
    last = st.session_state.get("last_active")
    if last and datetime.utcnow() - last > timedelta(minutes=settings.SESSION_TIMEOUT_MINUTES):
        st.session_state.pop("user", None)
        st.warning("Your session expired due to inactivity. Please sign in again.",
                   icon=":material/schedule:")
        return None
    st.session_state.last_active = datetime.utcnow()
    return user


def _logout(user):
    with get_db() as db:
        crud.log_activity(db, user["id"], "logout", f"{user['email']} signed out")
    for key in ("user", "last_active", "current_video_id", "current_note_id",
                "rag_stores", "fc_index", "fc_show_back", "nav_choice",
                "sidebar_open", "sidebar_compact"):
        st.session_state.pop(key, None)
    st.session_state.nav_target = "Dashboard"
    st.session_state.nav_epoch = st.session_state.get("nav_epoch", 0) + 1
    st.query_params.clear()
    st.rerun()


def main():
    _bootstrap()
    cards.load_css()
    if st.session_state.get("dark_mode"):
        st.markdown(DARK_CSS, unsafe_allow_html=True)

    user = _session_guard()

    # ── Public website (landing + login via ?page=login) ─────────────────
    if user is None:
        if st.query_params.get("page") == "login":
            login.render()
        else:
            landing.render()
        return

    # ── Signed-in dashboard shell (sidebar navigation) ───────────────────
    st.markdown(SIGNED_IN_CSS, unsafe_allow_html=True)
    choice = render_sidebar(user)

    routes = {
        "Dashboard": dashboard,
        "Generate Notes": video_notes,
        "Generated Library": notes_library,
        "Notes Library": notes_library,
        "Quiz Center": quiz_center,
        "Flashcards": flashcards,
        "Admin": admin_panel,
        "Website": landing,
        "Settings": settings_page,
    }
    if choice == "Logout":
        _logout(user)
    else:
        routes.get(choice, dashboard).render(user)


if __name__ == "__main__":
    main()
