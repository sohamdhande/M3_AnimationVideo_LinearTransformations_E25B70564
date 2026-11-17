"""Scene 3: Visual Intuition (Target ~60 s, Beats 3.1 - 3.4).

Introduces standard basis vectors e1 = (1, 0) and e2 = (0, 1), shows explicitly why
multiplying A by e1 and e2 extracts Column 1 (2, 0) and Column 2 (1, 1), then
transforms the full coordinate grid progressively under A while preserving the
dimmed original grid underneath for clear visual comparison.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from manim import *

from common import (
    AMBER,
    AXIS,
    CYAN,
    MATRIX_A,
    MUTED,
    TEAL,
    TEXT_WHITE,
    BaseM3Scene,
    make_bottom_caption,
    make_card,
    make_plane_pair,
    make_scene_header,
    pill_label,
)


class Scene03Intuition(BaseM3Scene):
    def construct(self):
        self.setup_scene()

        header = make_scene_header(
            "Scene 3  •  Visual Intuition",
            "Where Do the Basis Vectors Land?",
            self.sans_font,
        )

        # Color-coded matrix A badge in upper right: Col 1 = cyan, Col 2 = amber
        mat_tex = MathTex(
            r"A = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}",
            color=TEXT_WHITE,
        ).scale(0.80)
        # In MathTex(r"A = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}"):
        # Submobjects inside mat_tex[0]: A(0), =(1), [(2), 2(3), 1(4), 0(5), 1(6), ](7)
        mat_tex[0][3].set_color(CYAN)
        mat_tex[0][5].set_color(CYAN)
        mat_tex[0][4].set_color(AMBER)
        mat_tex[0][6].set_color(AMBER)
        mat_card = make_card(mat_tex, pad_x=0.50, pad_y=0.30)
        mat_card.to_corner(UR, buff=0.34)

        original_plane, transformed_plane = make_plane_pair(
            x_range=(-2, 2, 1),
            y_range=(-2, 2, 1),
            unit_size=0.92,
            center=DOWN * 0.28,
        )
        origin = original_plane.c2p(0, 0)
        origin_dot = Dot(origin, radius=0.055, color=AXIS).set_z_index(4)
        x_label = MathTex("x", color=MUTED).scale(0.62).next_to(original_plane.c2p(2, 0), UP + RIGHT, buff=0.12)
        y_label = MathTex("y", color=MUTED).scale(0.62).next_to(original_plane.c2p(0, 2), UP, buff=0.10)

        # Original standard basis vectors
        e1 = Arrow(origin, original_plane.c2p(1, 0), buff=0, color=CYAN, stroke_width=5.2).set_z_index(3)
        e2 = Arrow(origin, original_plane.c2p(0, 1), buff=0, color=AMBER, stroke_width=5.2).set_z_index(3)
        e1_lbl = pill_label(
            MathTex(r"e_1=(1,0)", color=CYAN).scale(0.60).next_to(e1.get_end(), DOWN, buff=0.15)
        ).set_z_index(4)
        e2_lbl = pill_label(
            MathTex(r"e_2=(0,1)", color=AMBER).scale(0.60).next_to(e2.get_end(), LEFT, buff=0.15)
        ).set_z_index(4)

        caption = make_bottom_caption("STANDARD BASIS VECTORS: e₁ AND e₂", self.sans_font, MUTED)

        # ------------------------------------------------------------------
        # Beat 3.1 — Introduce e1 = (1, 0) and e2 = (0, 1)
        # ------------------------------------------------------------------
        self.play_beat(
            "3.1",
            [
                ([FadeIn(header, shift=DOWN * 0.1), FadeIn(mat_card, shift=DOWN * 0.1), Create(original_plane), FadeIn(origin_dot), FadeIn(x_label), FadeIn(y_label), FadeIn(caption)], 1.6),
                ([GrowArrow(e1), FadeIn(e1_lbl)], 1.4),
                ([GrowArrow(e2), FadeIn(e2_lbl)], 1.4),
            ],
            post_wait=0.5,
        )

        # ------------------------------------------------------------------
        # Beat 3.2 — Show why Ae1 extracts Col 1 = (2,0) & Ae2 extracts Col 2 = (1,1)
        # ------------------------------------------------------------------
        ae1_calc = MathTex(
            r"A e_1 = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}"
            r"\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix}",
            color=TEXT_WHITE,
        ).scale(0.62)
        ae1_calc[0][:3].set_color(CYAN)
        ae1_calc[0][-4:].set_color(CYAN)
        ae1_card = make_card(ae1_calc, pad_x=0.38, pad_y=0.26, stroke_color=CYAN)
        ae1_card.to_edge(LEFT, buff=0.34).shift(UP * 0.45)

        ae2_calc = MathTex(
            r"A e_2 = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}"
            r"\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}",
            color=TEXT_WHITE,
        ).scale(0.62)
        ae2_calc[0][:3].set_color(AMBER)
        ae2_calc[0][-4:].set_color(AMBER)
        ae2_card = make_card(ae2_calc, pad_x=0.38, pad_y=0.26, stroke_color=AMBER)
        ae2_card.to_edge(RIGHT, buff=0.34).shift(UP * 0.45)

        target_e1 = Arrow(origin, original_plane.c2p(2, 0), buff=0, color=CYAN, stroke_width=5.2).set_z_index(3)
        target_e2 = Arrow(origin, original_plane.c2p(1, 1), buff=0, color=AMBER, stroke_width=5.2).set_z_index(3)
        target_e1_lbl = pill_label(
            MathTex(r"Ae_1=(2,0)", color=CYAN).scale(0.62).next_to(target_e1.get_end(), DOWN, buff=0.16)
        ).set_z_index(4)
        target_e2_lbl = pill_label(
            MathTex(r"Ae_2=(1,1)", color=AMBER).scale(0.62).next_to(target_e2.get_end(), UP + LEFT * 0.35, buff=0.14)
        ).set_z_index(4)

        self.play_beat(
            "3.2",
            [
                ([FadeIn(ae1_card, shift=RIGHT * 0.15)], 1.2),
                ([Transform(e1, target_e1), ReplacementTransform(e1_lbl, target_e1_lbl)], 1.8),
                ([FadeIn(ae2_card, shift=LEFT * 0.15)], 1.2),
                ([Transform(e2, target_e2), ReplacementTransform(e2_lbl, target_e2_lbl)], 1.8),
            ],
            post_wait=0.6,
        )

        # ------------------------------------------------------------------
        # Beat 3.3 (cached from PoC!) — Columns of A = landing positions of e1, e2
        # ------------------------------------------------------------------
        col1_box = SurroundingRectangle(
            VGroup(mat_tex[0][3], mat_tex[0][5]), color=CYAN, buff=0.07, corner_radius=0.05, stroke_width=2.2
        )
        col2_box = SurroundingRectangle(
            VGroup(mat_tex[0][4], mat_tex[0][6]), color=AMBER, buff=0.07, corner_radius=0.05, stroke_width=2.2
        )
        caption_cols = make_bottom_caption("COLUMNS OF A = IMAGES OF STANDARD BASIS VECTORS", self.sans_font, TEAL)

        self.play_beat(
            "3.3",
            [
                ([ReplacementTransform(caption, caption_cols), Create(col1_box), Indicate(e1, color=CYAN, scale_factor=1.08)], 1.6),
                ([Create(col2_box), Indicate(e2, color=AMBER, scale_factor=1.08)], 1.6),
                ([FadeOut(ae1_card), FadeOut(ae2_card), FadeOut(col1_box), FadeOut(col2_box)], 1.0),
            ],
            post_wait=0.5,
        )

        # ------------------------------------------------------------------
        # Beat 3.4 — Transform full coordinate grid (stretch + shear-like shift)
        # ------------------------------------------------------------------
        transformed_plane.set_z_index(1)
        original_plane.set_z_index(0)
        origin_ring = Circle(radius=0.18, color=TEAL, stroke_width=2.5).move_to(origin).set_z_index(4)
        caption_grid = make_bottom_caption(
            "ORIGIN FIXED  •  HORIZONTAL STRETCH (×2) + SHEAR-LIKE SLANT",
            self.sans_font,
            TEAL,
        )

        self.play_beat(
            "3.4",
            [
                ([Create(origin_ring), FadeOut(origin_ring), ReplacementTransform(caption_cols, caption_grid)], 1.4),
                ([FadeIn(transformed_plane)], 0.5),
                (
                    [
                        original_plane.animate.set_opacity(0.24),
                        ApplyMatrix(MATRIX_A, transformed_plane, about_point=origin),
                        x_label.animate.next_to(original_plane.c2p(4, 0), RIGHT, buff=0.14),
                    ],
                    3.2,
                ),
            ],
            post_wait=1.5,
        )

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)

