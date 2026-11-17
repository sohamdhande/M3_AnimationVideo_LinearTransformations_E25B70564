"""Scene 1: Hook / Context (Target ~25 s, Beats 1.1 - 1.2).

Establishes the opening title card (title, concept, student name/ID),
introduces the 2D coordinate grid with standard basis arrows and a tracked point,
and previews a partial plane-wide transformation before freezing prior to Scene 2.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
from manim import *

from common import (
    AMBER,
    AXIS,
    CORAL,
    COURSE_TAG,
    CYAN,
    MUTED,
    PROJECT_SUBTITLE,
    PROJECT_TITLE,
    STUDENT_ID,
    STUDENT_NAME,
    TEAL,
    TEXT_WHITE,
    BaseM3Scene,
    make_bottom_caption,
    make_card,
    make_plane_pair,
    make_scene_header,
    pill_label,
)

# Exact 40% linear interpolation M(0.4) = 0.6*I + 0.4*A for the teaser freeze.
PREVIEW_MATRIX = np.array([[1.4, 0.4], [0.0, 1.0]])


class Scene01Hook(BaseM3Scene):
    def construct(self):
        self.setup_scene()

        # ------------------------------------------------------------------
        # Opening Title Frame (required by college brief / QA checklist)
        # ------------------------------------------------------------------
        course_label = Text(COURSE_TAG, font_size=16, weight=MEDIUM, color=TEAL, font=self.sans_font)
        main_title = Text(PROJECT_TITLE, font_size=48, weight=BOLD, color=TEXT_WHITE, font=self.sans_font)
        subtitle = Text(PROJECT_SUBTITLE, font_size=24, color=MUTED, font=self.sans_font)
        concept_line = Text(
            "Concept: 2D Linear Transformations & Determinant Area Scaling",
            font_size=17,
            color=CYAN,
            font=self.sans_font,
        )
        accent_bar = Line(LEFT * 2.4, RIGHT * 2.4, color=TEAL, stroke_width=2.5)
        student_line = Text(
            f"{STUDENT_NAME}   •   {STUDENT_ID}",
            font_size=16,
            color=MUTED,
            font=self.sans_font,
        )

        title_block = VGroup(
            course_label,
            main_title,
            subtitle,
            accent_bar,
            concept_line,
            student_line,
        ).arrange(DOWN, buff=0.26)
        title_block.move_to(ORIGIN)

        self.play(FadeIn(title_block, shift=UP * 0.2), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title_block, shift=UP * 0.15), run_time=0.6)

        # ------------------------------------------------------------------
        # Persistent Stage Header + Mysterious Four-Number Teaser Matrix
        # ------------------------------------------------------------------
        header = make_scene_header("Scene 1  •  Hook", "Can Four Numbers Move the Plane?", self.sans_font)

        mystery_tex = MathTex(
            r"\begin{bmatrix} ? & ? \\ ? & ? \end{bmatrix}",
            color=CYAN,
        ).scale(0.84)
        mystery_card = make_card(mystery_tex, pad_x=0.52, pad_y=0.34, stroke_color=CYAN)
        mystery_card.to_corner(UR, buff=0.34)

        original_plane, preview_plane = make_plane_pair(
            x_range=(-2, 2, 1),
            y_range=(-2, 2, 1),
            unit_size=0.92,
            center=DOWN * 0.28,
        )
        origin = original_plane.c2p(0, 0)
        origin_dot = Dot(origin, radius=0.05, color=AXIS).set_z_index(4)
        x_label = MathTex("x", color=MUTED).scale(0.62).next_to(original_plane.c2p(2, 0), UP + RIGHT, buff=0.12)
        y_label = MathTex("y", color=MUTED).scale(0.62).next_to(original_plane.c2p(0, 2), UP, buff=0.10)

        e1 = Arrow(origin, original_plane.c2p(1, 0), buff=0, color=CYAN, stroke_width=5).set_z_index(3)
        e2 = Arrow(origin, original_plane.c2p(0, 1), buff=0, color=AMBER, stroke_width=5).set_z_index(3)
        e1_lbl = pill_label(MathTex(r"e_1", color=CYAN).scale(0.70).next_to(e1.get_end(), DOWN, buff=0.14)).set_z_index(4)
        e2_lbl = pill_label(MathTex(r"e_2", color=AMBER).scale(0.70).next_to(e2.get_end(), LEFT, buff=0.14)).set_z_index(4)

        p_start = original_plane.c2p(1, 2)
        p_preview = original_plane.c2p(2.2, 2.0)  # M(0.4) * [1, 2]^T = [2.2, 2.0]^T
        sample_dot = Dot(p_start, radius=0.085, color=CORAL).set_z_index(4)
        sample_lbl = pill_label(
            MathTex(r"P", color=CORAL).scale(0.68).next_to(sample_dot, RIGHT, buff=0.14)
        ).set_z_index(4)

        caption = make_bottom_caption("A 2×2 MATRIX ACTS ON EVERY POINT AT ONCE", self.sans_font, MUTED)

        # ------------------------------------------------------------------
        # Beat 1.1 (cached from Visual PoC!)
        # ------------------------------------------------------------------
        self.play_beat(
            "1.1",
            [
                ([FadeIn(header, shift=DOWN * 0.1), FadeIn(mystery_card, shift=DOWN * 0.1)], 1.0),
                ([Create(original_plane), FadeIn(origin_dot), FadeIn(x_label), FadeIn(y_label)], 1.8),
                ([Indicate(mystery_tex, color=TEAL, scale_factor=1.10)], 1.2),
            ],
            post_wait=0.5,
        )

        # ------------------------------------------------------------------
        # Beat 1.2 — Show basis arrows & sample point, then begin partial tilt & freeze
        # ------------------------------------------------------------------
        preview_plane.set_z_index(1)
        original_plane.set_z_index(0)

        e1_preview = Arrow(origin, original_plane.c2p(1.4, 0.0), buff=0, color=CYAN, stroke_width=5).set_z_index(3)
        e2_preview = Arrow(origin, original_plane.c2p(0.4, 1.0), buff=0, color=AMBER, stroke_width=5).set_z_index(3)
        pulse_ring = Circle(radius=0.22, color=CORAL, stroke_width=2.5).move_to(p_start).set_z_index(4)
        trace_line = DashedLine(
            p_start, p_preview, dash_length=0.09, color=CORAL, stroke_opacity=0.55, stroke_width=2.0
        ).set_z_index(2)

        def _prep_preview():
            self.add(preview_plane)

        self.play_beat(
            "1.2",
            [
                (
                    [
                        GrowArrow(e1),
                        GrowArrow(e2),
                        FadeIn(e1_lbl),
                        FadeIn(e2_lbl),
                        FadeIn(sample_dot),
                        FadeIn(sample_lbl),
                        FadeIn(caption),
                    ],
                    1.8,
                ),
                ([Create(pulse_ring), FadeOut(pulse_ring)], 1.4),
                ([FadeIn(preview_plane, run_time=0.4)], 0.4),
                (
                    [
                        original_plane.animate.set_opacity(0.28),
                        ApplyMatrix(PREVIEW_MATRIX, preview_plane, about_point=origin),
                        Transform(e1, e1_preview),
                        Transform(e2, e2_preview),
                        e1_lbl.animate.next_to(e1_preview.get_end(), DOWN, buff=0.14),
                        e2_lbl.animate.next_to(e2_preview.get_end(), UP + LEFT * 0.25, buff=0.14),
                        Create(trace_line),
                        sample_dot.animate.move_to(p_preview),
                        sample_lbl.animate.next_to(p_preview, RIGHT, buff=0.14),
                    ],
                    2.8,
                ),
                (None, 1.2),  # Freeze frame before matrix reveal in Scene 2
            ],
            post_wait=1.0,
        )

        # Clean fade out into Scene 2
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
