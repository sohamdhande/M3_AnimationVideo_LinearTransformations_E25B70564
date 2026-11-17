"""Shared design tokens, approved 521-word narration beats, and reusable Manim helpers
for 'Matrices in Motion: How a 2x2 Matrix Transforms the Plane'.

Student: Soham Dhande (E25B70564)

Runtime Dependencies (Python 3.11+):
    - manim==0.22.1
    - manim-voiceover[gemini]==0.4.0
    - google-genai==2.34.0
    - python-dotenv==1.2.4
    - numpy==2.4.6
    - System tools: FFmpeg 8.1+, SoX 14.4+, Cairo, Pango, LaTeX (pdflatex + dvisvgm)
    - Environment: Set GEMINI_API_KEY locally (via shell or local .env; never commit keys)

Render Individual Scenes (1080p, 30fps):
    manim -r 1920,1080 --fps 30 Code/scene_01_hook.py Scene01Hook
    manim -r 1920,1080 --fps 30 Code/scene_02_concept.py Scene02Concept
    manim -r 1920,1080 --fps 30 Code/scene_03_intuition.py Scene03Intuition
    manim -r 1920,1080 --fps 30 Code/scene_04_worked_example.py Scene04WorkedExample
    manim -r 1920,1080 --fps 30 Code/scene_05_interpretation.py Scene05Interpretation
    manim -r 1920,1080 --fps 30 Code/scene_06_summary_credits.py Scene06SummaryCredits
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, Sequence

import manimpango
import numpy as np
from dotenv import load_dotenv
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gemini import GeminiService

# ---------------------------------------------------------------------------
# Project Metadata (editable prior to final 1080p render)
# ---------------------------------------------------------------------------
PROJECT_TITLE = "MATRICES IN MOTION"
PROJECT_SUBTITLE = "How a 2×2 Matrix Transforms the Plane"
COURSE_TAG = "M3 — First-Year Undergraduate Mathematics"
STUDENT_NAME = "Soham Dhande"
STUDENT_ID = "Student ID: E25B70564"

# ---------------------------------------------------------------------------
# Approved Hybrid Visual Design System
# ---------------------------------------------------------------------------
BG = "#0D1117"            # Deep charcoal/navy canvas
GRID = "#526477"          # Subdued cool blue/grey original grid
AXIS = "#9AAFC2"          # Original axes
CYAN = "#53D8FB"          # e1 / first column / horizontal contribution
AMBER = "#FFB84D"         # e2 / second column / slanted contribution
CORAL = "#FF718D"         # Tracked sample point (1,2) -> (4,2)
TEAL = "#55D6BE"          # Transformed grid & determinant accent
TEAL_AXIS = "#8AEAD8"     # Transformed axes
TEXT_WHITE = "#F4F7FB"    # Primary crisp white
MUTED = "#A8B6C6"         # Secondary labels & captions
PANEL_BG = "#111B27"      # Dark translucent card fill
PANEL_STROKE = "#34495E"  # Subtle card border

# ---------------------------------------------------------------------------
# Authoritative Matrix & Mathematical Constants (docs/MATH_CHECK.md)
# ---------------------------------------------------------------------------
MATRIX_A = np.array([[2.0, 1.0], [0.0, 1.0]])

# ---------------------------------------------------------------------------
# Approved 521-Word Narration Script (19 Semantic Beats — DO NOT ALTER)
# ---------------------------------------------------------------------------
BEATS: dict[str, str] = {
    # Scene 1: Hook / Context (46 words)
    "1.1": (
        "Can four numbers move every point in a two-dimensional plane in one predictable way?"
    ),
    "1.2": (
        "Look at this square coordinate grid. Instead of moving one isolated point at a time, "
        "a two-by-two matrix transforms the entire plane at once, reshaping every grid line "
        "and every vector together."
    ),
    # Scene 2: Concept Introduction (61 words)
    "2.1": (
        "Meet matrix A, with first row two, one, and second row zero, one."
    ),
    "2.2": (
        "Matrix A defines a linear transformation T. We represent any point as a column vector "
        "with entries x and y, and multiply matrix A on its left."
    ),
    "2.3": (
        "That matrix product gives our coordinate rule: the first coordinate becomes two x plus y, "
        "and the second coordinate stays y."
    ),
    # Scene 3: Visual Intuition (121 words)
    "3.1": (
        "To see how this rule reshapes space, begin with the standard basis vectors: e one, "
        "one unit right at one, zero, and e two, one unit up at zero, one."
    ),
    "3.2": (
        "When matrix A multiplies e one, the one and zero entries select the first column directly, "
        "sending e one to two, zero. Multiplying by e two selects the second column, sending e two "
        "to one, one."
    ),
    "3.3": (
        "That is our central geometric insight: the columns of matrix A are the exact landing "
        "positions of the standard basis vectors."
    ),
    "3.4": (
        "Because linear transformations preserve vector addition and scaling, they keep the origin "
        "fixed and map grid lines onto parallel, evenly spaced lines here. The plane stretches "
        "horizontally while slanting sideways in a shear-like shift."
    ),
    # Scene 4: Worked Example (116 words)
    "4.1": (
        "Now let us test this rule on a specific point: one, two, written as a column vector "
        "with x equal to one and y equal to two."
    ),
    "4.2": (
        "To compute T of one, two, we take the dot product of each row of matrix A with our "
        "column vector. Row one gives two times one plus one times two, which is two plus two, "
        "equaling four."
    ),
    "4.3": (
        "Row two gives zero times one plus one times two, which is zero plus two, equaling two."
    ),
    "4.4": (
        "So the point one, two moves cleanly to four, two. Geometrically, it lands at one step "
        "along transformed e one plus two steps along transformed e two, staying at the exact "
        "same grid intersection."
    ),
    # Scene 5: Interpretation (130 words)
    "5.1": (
        "Finally, look at the unit square spanned by e one and e two. Its four corners map from "
        "zero, zero to zero, zero; one, zero to two, zero; one, one to three, one; and zero, one "
        "to one, one."
    ),
    "5.2": (
        "The unit square becomes a parallelogram with base length two and perpendicular height one, "
        "giving an area of two times one, which equals two."
    ),
    "5.3": (
        "Algebraically, the determinant of matrix A is two times one minus one times zero, "
        "which also equals two."
    ),
    "5.4": (
        "In general, the absolute value of the determinant gives the area-scaling factor for every "
        "region, so here all areas double. Because this determinant is positive, orientation is "
        "preserved rather than reversed. And because it is nonzero, space does not collapse to a "
        "lower dimension, meaning matrix A is invertible."
    ),
    # Scene 6: Summary & Credits (47 words)
    "6.1": (
        "Three ideas tie everything together. First, a two-by-two matrix defines a linear "
        "transformation on column vectors. Second, its columns record where the standard basis "
        "vectors land, determining the entire grid."
    ),
    "6.2": (
        "Third, the determinant's magnitude gives the area-scaling factor, while its sign tells us "
        "whether orientation is preserved."
    ),
}


def select_sans_font() -> str:
    """Choose a crisp modern sans-serif installed on the current OS."""
    available = set(manimpango.list_fonts())
    for candidate in ("Avenir Next", "Helvetica Neue", "DejaVu Sans", "Arial"):
        if candidate in available:
            return candidate
    return "Sans"


def pill_label(mobj: Mobject, opacity: float = 0.86, buff: float = 0.06) -> Mobject:
    """Place a subtle canvas-matched backing behind a label so grid lines never cut text."""
    mobj.add_background_rectangle(color=BG, opacity=opacity, buff=buff)
    return mobj


def make_card(
    content: Mobject,
    pad_x: float = 0.44,
    pad_y: float = 0.30,
    stroke_color: str = PANEL_STROKE,
    fill_opacity: float = 0.96,
) -> VGroup:
    """Wrap any Mobject or VGroup inside a clean dark card."""
    box = RoundedRectangle(
        width=content.width + pad_x,
        height=content.height + pad_y,
        corner_radius=0.14,
        stroke_color=stroke_color,
        stroke_width=1.25,
        fill_color=PANEL_BG,
        fill_opacity=fill_opacity,
    )
    content.move_to(box.get_center())
    return VGroup(box, content)


def make_scene_header(scene_tag: str, scene_title: str, font_name: str) -> VGroup:
    """Consistent upper-left header shared across all scenes."""
    tag = Text(scene_tag.upper(), font_size=13, weight=BOLD, color=TEAL, font=font_name)
    title = Text(scene_title, font_size=24, weight=BOLD, color=TEXT_WHITE, font=font_name)
    header = VGroup(tag, title).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
    header.to_corner(UL, buff=0.34)
    return header


def make_matrix_badge(include_rule: bool = False) -> VGroup:
    """Upper-right matrix card (either A alone or A with column-vector rule)."""
    if include_rule:
        tex = MathTex(
            r"A=\begin{bmatrix}2&1\\0&1\end{bmatrix},\quad "
            r"A\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}2x+y\\y\end{bmatrix}",
            color=TEXT_WHITE,
        ).scale(0.64)
    else:
        tex = MathTex(
            r"A=\begin{bmatrix}2&1\\0&1\end{bmatrix}",
            color=TEXT_WHITE,
        ).scale(0.76)
    card = make_card(tex, pad_x=0.48, pad_y=0.30)
    card.to_corner(UR, buff=0.34)
    return card


def make_plane_pair(
    x_range: Sequence[float] = (-2, 2, 1),
    y_range: Sequence[float] = (-2, 2, 1),
    unit_size: float = 0.92,
    center: np.ndarray = DOWN * 0.28,
) -> tuple[NumberPlane, NumberPlane]:
    """Build matching original (cool blue/grey) and transformed (teal) coordinate planes."""
    x_len = (x_range[1] - x_range[0]) * unit_size
    y_len = (y_range[1] - y_range[0]) * unit_size
    kwargs = dict(x_range=x_range, y_range=y_range, x_length=x_len, y_length=y_len)

    original = NumberPlane(
        **kwargs,
        axis_config={"stroke_color": AXIS, "stroke_width": 2.0},
        background_line_style={
            "stroke_color": GRID,
            "stroke_width": 1.3,
            "stroke_opacity": 0.65,
        },
    ).move_to(center)

    transformed = NumberPlane(
        **kwargs,
        axis_config={"stroke_color": TEAL_AXIS, "stroke_width": 2.1},
        background_line_style={
            "stroke_color": TEAL,
            "stroke_width": 1.5,
            "stroke_opacity": 0.72,
        },
    ).move_to(center)

    return original, transformed


def make_bottom_caption(text: str, font_name: str, color: str = MUTED) -> Text:
    """Consistent bottom guide caption bar."""
    return Text(text.upper(), font_size=14, weight=MEDIUM, color=color, font=font_name).to_edge(
        DOWN, buff=0.28
    )


class BaseM3Scene(VoiceoverScene):
    """Shared base class wiring Gemini Kore TTS (cached) and paced animation beats."""

    sans_font: str

    def setup_scene(self) -> None:
        project_root = Path(__file__).resolve().parent.parent
        load_dotenv(project_root / ".env")
        load_dotenv()
        if not os.getenv("GEMINI_API_KEY") and not os.getenv("GOOGLE_API_KEY"):
            raise RuntimeError(
                "Gemini API key not found. Add GEMINI_API_KEY to local .env; "
                "never hardcode credentials in source code."
            )

        self.sans_font = select_sans_font()
        self.camera.background_color = BG
        self.set_speech_service(
            GeminiService(
                model="gemini-3.1-flash-tts-preview",
                voice="Kore",
                auth_mode="api_key",
            )
        )

    def play_beat(
        self,
        beat_id: str,
        steps: Sequence[tuple[Iterable[Animation] | None, float]],
        post_wait: float = 0.0,
    ) -> float:
        """Speak an approved beat and play natural-paced animation steps inside its duration.

        Each entry in `steps` is `(animations_or_None, desired_seconds)`.
        - If animations_or_None is None or empty, a quiet hold of `desired_seconds` is played.
        - Steps play at natural speeds (never stretched artificially) and are only gently
          compressed if their total exceeds 92% of `tracker.duration`.
        - After the steps complete, the scene waits out the remaining spoken audio cleanly,
          plus an optional `post_wait` cognitive hold after speech finishes.
        """
        spoken_text = BEATS[beat_id]
        with self.voiceover(text=spoken_text) as tracker:
            total_desired = sum(dur for _, dur in steps)
            budget = max(0.5, tracker.duration * 0.92)
            scale = min(1.0, budget / total_desired) if total_desired > 0 else 1.0

            elapsed = 0.0
            for anims, desired in steps:
                dur = max(0.15, desired * scale)
                if anims:
                    self.play(*anims, run_time=dur, rate_func=smooth)
                else:
                    self.wait(dur)
                elapsed += dur

            remaining = max(0.0, tracker.duration - elapsed)
            if remaining > 0.04:
                self.wait(remaining)

            duration = tracker.duration

        if post_wait > 0.0:
            self.wait(post_wait)

        return duration

