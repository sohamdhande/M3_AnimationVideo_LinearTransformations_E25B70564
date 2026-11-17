"""Scene 6: Summary & Credits (Target ~25 s, Beats 6.1 - 6.2).

Returns softly to the transformed grid, presents the three concise mathematical
takeaways, and closes with the required references, audio/music credits, and
AI disclosure screen.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from manim import *

from common import (
    AMBER,
    CYAN,
    MATRIX_A,
    MUTED,
    PANEL_BG,
    PANEL_STROKE,
    PROJECT_SUBTITLE,
    PROJECT_TITLE,
    STUDENT_ID,
    STUDENT_NAME,
    TEAL,
    TEXT_WHITE,
    BaseM3Scene,
    make_plane_pair,
    make_scene_header,
)


class Scene06SummaryCredits(BaseM3Scene):
    def construct(self):
        self.setup_scene()

        header = make_scene_header(
            "Scene 6  •  Summary",
            "Three Core Takeaways",
            self.sans_font,
        )

        # Subtle dimmed transformed grid + area-2 parallelogram backdrop
        _, bg_plane = make_plane_pair(
            x_range=(-2, 2, 1),
            y_range=(-2, 2, 1),
            unit_size=0.92,
            center=DOWN * 0.20,
        )
        bg_origin = bg_plane.c2p(0, 0)
        bg_plane.apply_matrix(MATRIX_A, about_point=bg_origin)
        bg_plane.set_opacity(0.16)

        bg_para = Polygon(
            bg_origin,
            bg_origin + RIGHT * 2 * 0.92,
            bg_origin + RIGHT * 3 * 0.92 + UP * 1 * 0.92,
            bg_origin + RIGHT * 1 * 0.92 + UP * 1 * 0.92,
            color=TEAL,
            stroke_width=1.5,
            stroke_opacity=0.28,
            fill_color=TEAL,
            fill_opacity=0.10,
        )
        backdrop = VGroup(bg_plane, bg_para).set_z_index(0)

        def _takeaway_card(num: str, heading: str, math_latex: str, accent: str) -> VGroup:
            badge_num = Text(num, font_size=22, weight=BOLD, color=accent, font=self.sans_font)
            head_txt = Text(heading, font_size=19, weight=BOLD, color=TEXT_WHITE, font=self.sans_font)
            left_col = VGroup(badge_num, head_txt).arrange(RIGHT, buff=0.22)
            eq = MathTex(math_latex, color=accent).scale(0.62)

            box = RoundedRectangle(
                width=11.4,
                height=1.22,
                corner_radius=0.16,
                stroke_color=accent,
                stroke_width=1.4,
                fill_color=PANEL_BG,
                fill_opacity=0.94,
            )
            left_col.move_to(box.get_left() + RIGHT * (left_col.width / 2 + 0.42))
            eq.move_to(box.get_right() + LEFT * (eq.width / 2 + 0.46))
            return VGroup(box, left_col, eq).set_z_index(2)

        card_1 = _takeaway_card(
            "01",
            "Matrix maps column vectors linearly",
            r"A\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}2x+y\\y\end{bmatrix}",
            CYAN,
        )
        card_2 = _takeaway_card(
            "02",
            "Columns record transformed basis vectors",
            r"Ae_1=\begin{bmatrix}2\\0\end{bmatrix},\;\; Ae_2=\begin{bmatrix}1\\1\end{bmatrix}",
            AMBER,
        )
        card_3 = _takeaway_card(
            "03",
            "Determinant scales area & tracks orientation",
            r"|\det(A)|=2,\;\; \det(A)>0",
            TEAL,
        )

        cards = VGroup(card_1, card_2, card_3).arrange(DOWN, buff=0.30)
        cards.move_to(DOWN * 0.25)

        # ------------------------------------------------------------------
        # Beat 6.1 — Takeaways 1 & 2
        # ------------------------------------------------------------------
        self.play_beat(
            "6.1",
            [
                ([FadeIn(backdrop), FadeIn(header, shift=DOWN * 0.1)], 0.9),
                ([FadeIn(card_1, shift=UP * 0.15)], 1.6),
                ([FadeIn(card_2, shift=UP * 0.15)], 1.6),
            ],
            post_wait=0.4,
        )

        # ------------------------------------------------------------------
        # Beat 6.2 — Takeaway 3
        # ------------------------------------------------------------------
        self.play_beat(
            "6.2",
            [
                ([FadeIn(card_3, shift=UP * 0.15)], 1.6),
                ([Indicate(card_3[2], color=TEAL, scale_factor=1.08)], 1.0),
            ],
            post_wait=1.0,
        )

        # ------------------------------------------------------------------
        # Closing Credits, References, & AI Disclosure Frame (~5.5 s hold)
        # ------------------------------------------------------------------
        self.play(FadeOut(header), FadeOut(cards), run_time=0.6)

        credits_title = Text(
            f"{PROJECT_TITLE}  —  {PROJECT_SUBTITLE}",
            font_size=22,
            weight=BOLD,
            color=TEXT_WHITE,
            font=self.sans_font,
        )
        author_line = Text(
            f"Created by {STUDENT_NAME}   •   {STUDENT_ID}",
            font_size=15,
            color=CYAN,
            font=self.sans_font,
        )
        rule = Line(LEFT * 5.2, RIGHT * 5.2, color=PANEL_STROKE, stroke_width=1.2)

        refs_head = Text("REFERENCES & TOOLS", font_size=13, weight=BOLD, color=TEAL, font=self.sans_font)
        refs_body = Text(
            "• G. Strang, Introduction to Linear Algebra   • S. Axler, Linear Algebra Done Right\n"
            "• Animation: Python 3.11 + Manim Community v0.22.1 + BasicTeX (TeX Live 2026)\n"
            "• Voiceover: Manim Voiceover 0.4.0 + Gemini TTS (Kore, gemini-3.1-flash-tts-preview)\n"
            "• Audio / Music: No background music used; no third-party visual assets used.",
            font_size=13,
            color=MUTED,
            font=self.sans_font,
            line_spacing=1.28,
        )

        ai_head = Text("AI ASSISTANCE DISCLOSURE", font_size=13, weight=BOLD, color=AMBER, font=self.sans_font)
        ai_body = Text(
            "Google Antigravity assisted with planning and Python/Manim development, and Gemini TTS\n"
            "generated the narration audio. All mathematical statements, derivations, calculations,\n"
            "and rendered outputs were independently verified by the student.",
            font_size=13,
            color=TEXT_WHITE,
            font=self.sans_font,
            line_spacing=1.28,
        )

        credits_content = VGroup(
            credits_title,
            author_line,
            rule,
            refs_head,
            refs_body,
            ai_head,
            ai_body,
        ).arrange(DOWN, buff=0.22)
        for sec in (refs_head, refs_body, ai_head, ai_body):
            sec.align_to(rule, LEFT)

        credits_box = RoundedRectangle(
            width=11.6,
            height=5.75,
            corner_radius=0.18,
            stroke_color=PANEL_STROKE,
            stroke_width=1.4,
            fill_color=PANEL_BG,
            fill_opacity=0.96,
        )
        credits_content.move_to(credits_box.get_center())
        credits_card = VGroup(credits_box, credits_content).set_z_index(3)

        self.play(FadeIn(credits_card, shift=UP * 0.15), run_time=0.9)
        self.wait(4.6)
        self.play(FadeOut(credits_card), FadeOut(backdrop), run_time=0.7)

