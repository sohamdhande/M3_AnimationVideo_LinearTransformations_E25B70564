"""Scene 2: Concept Introduction (Target ~30 s, Beats 2.1 - 2.3).

Reveals matrix A = [[2, 1], [0, 1]] beside the coordinate plane, highlights its rows,
establishes the column-vector left-multiplication convention T([x, y]^T) = A[x, y]^T,
and derives the coordinate rule (x, y) -> (2x + y, y).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from manim import *

from common import (
    AMBER,
    AXIS,
    CORAL,
    CYAN,
    MUTED,
    PANEL_BG,
    PANEL_STROKE,
    TEAL,
    TEXT_WHITE,
    BaseM3Scene,
    make_bottom_caption,
    make_card,
    make_plane_pair,
    make_scene_header,
    pill_label,
)


class Scene02Concept(BaseM3Scene):
    def construct(self):
        self.setup_scene()

        header = make_scene_header("Scene 2  •  Concept Introduction", "Matrix Multiplication as a Map", self.sans_font)

        # Left stage: clean coordinate plane with generic point (x, y)
        plane, _ = make_plane_pair(
            x_range=(-2, 2, 1),
            y_range=(-2, 2, 1),
            unit_size=0.86,
            center=LEFT * 3.35 + DOWN * 0.22,
        )
        origin = plane.c2p(0, 0)
        origin_dot = Dot(origin, radius=0.05, color=AXIS).set_z_index(4)
        x_label = MathTex("x", color=MUTED).scale(0.60).next_to(plane.c2p(2, 0), UP + RIGHT, buff=0.10)
        y_label = MathTex("y", color=MUTED).scale(0.60).next_to(plane.c2p(0, 2), UP, buff=0.10)

        # Generic vector illustration at (1.15, 1.35) labeled (x, y)
        pt = plane.c2p(1.15, 1.35)
        pt_x = plane.c2p(1.15, 0)
        pt_y = plane.c2p(0, 1.35)
        vec_v = Arrow(origin, pt, buff=0, color=CORAL, stroke_width=4.2).set_z_index(3)
        pt_dot = Dot(pt, radius=0.08, color=CORAL).set_z_index(4)
        pt_lbl = pill_label(MathTex(r"(x, y)", color=CORAL).scale(0.66).next_to(pt_dot, UP + RIGHT * 0.25, buff=0.12)).set_z_index(4)
        dash_x = DashedLine(pt, pt_x, dash_length=0.08, color=CYAN, stroke_opacity=0.65, stroke_width=1.8)
        dash_y = DashedLine(pt, pt_y, dash_length=0.08, color=AMBER, stroke_opacity=0.65, stroke_width=1.8)
        x_coord_lbl = pill_label(MathTex("x", color=CYAN).scale(0.58).next_to(pt_x, DOWN, buff=0.12)).set_z_index(4)
        y_coord_lbl = pill_label(MathTex("y", color=AMBER).scale(0.58).next_to(pt_y, LEFT, buff=0.12)).set_z_index(4)

        # Right stage: clean algebraic card
        right_center = RIGHT * 2.85 + DOWN * 0.15
        panel_bg = RoundedRectangle(
            width=6.35,
            height=4.75,
            corner_radius=0.18,
            stroke_color=PANEL_STROKE,
            stroke_width=1.3,
            fill_color=PANEL_BG,
            fill_opacity=0.95,
        ).move_to(right_center)

        # Beat 2.1: Matrix A with individually highlightable rows
        mat_a_eq = MathTex(
            r"A = ",
            r"\begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}",
            color=TEXT_WHITE,
        ).scale(0.95)
        mat_a_eq.move_to(right_center + UP * 1.40)

        # Subtle highlight boxes around Row 1 and Row 2 of matrix A
        mat_body = mat_a_eq[1]
        row1_box = SurroundingRectangle(
            VGroup(mat_body[1], mat_body[2]),
            color=CYAN,
            buff=0.09,
            corner_radius=0.06,
            stroke_width=2.2,
        )
        row2_box = SurroundingRectangle(
            VGroup(mat_body[3], mat_body[4]),
            color=AMBER,
            buff=0.09,
            corner_radius=0.06,
            stroke_width=2.2,
        )
        row1_tag = Text("Row 1:  2, 1", font_size=14, weight=MEDIUM, color=CYAN, font=self.sans_font)
        row1_tag.next_to(mat_a_eq, RIGHT, buff=0.35).shift(UP * 0.24)
        row2_tag = Text("Row 2:  0, 1", font_size=14, weight=MEDIUM, color=AMBER, font=self.sans_font)
        row2_tag.next_to(mat_a_eq, RIGHT, buff=0.35).shift(DOWN * 0.24)

        # Beat 2.2: Left-multiplication equation
        map_eq_lhs = MathTex(
            r"T\begin{bmatrix} x \\ y \end{bmatrix}",
            r"=",
            r"\begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}",
            r"\begin{bmatrix} x \\ y \end{bmatrix}",
            color=TEXT_WHITE,
        ).scale(0.76)
        map_eq_lhs[0].set_color(TEAL)
        map_eq_lhs[3].set_color(CORAL)
        map_eq_lhs.move_to(right_center + LEFT * 0.90 + DOWN * 0.05)

        col_note = Text("Column vector", font_size=13, color=CORAL, font=self.sans_font)
        col_note.next_to(map_eq_lhs[3], DOWN, buff=0.14)

        # Beat 2.3: Resulting output column vector + coordinate rule pill
        map_eq_rhs = MathTex(
            r"=",
            r"\begin{bmatrix} 2x + y \\ y \end{bmatrix}",
            color=TEXT_WHITE,
        ).scale(0.76)
        map_eq_rhs[1].set_color(TEAL)
        map_eq_rhs.next_to(map_eq_lhs, RIGHT, buff=0.16)

        rule_tex = MathTex(
            r"(x,\, y) \;\longmapsto\; (2x + y,\; y)",
            color=TEAL,
        ).scale(0.76)
        rule_card = make_card(rule_tex, pad_x=0.46, pad_y=0.24, stroke_color=TEAL)
        rule_card.move_to(right_center + DOWN * 1.55)

        caption = make_bottom_caption("COLUMN-VECTOR CONVENTION: A MULTIPLIES ON THE LEFT", self.sans_font, MUTED)

        # ------------------------------------------------------------------
        # Beat 2.1
        # ------------------------------------------------------------------
        self.play_beat(
            "2.1",
            [
                ([FadeIn(header, shift=DOWN * 0.1), Create(plane), FadeIn(origin_dot), FadeIn(x_label), FadeIn(y_label), FadeIn(panel_bg)], 1.2),
                ([Write(mat_a_eq)], 1.0),
                ([Create(row1_box), FadeIn(row1_tag, shift=RIGHT * 0.1)], 0.9),
                ([FadeOut(row1_box), Create(row2_box), FadeIn(row2_tag, shift=RIGHT * 0.1)], 0.9),
            ],
            post_wait=1.4,
        )

        # ------------------------------------------------------------------
        # Beat 2.2
        # ------------------------------------------------------------------
        self.play_beat(
            "2.2",
            [
                ([FadeOut(row2_box), FadeOut(row1_tag), FadeOut(row2_tag), mat_a_eq.animate.move_to(right_center + UP * 1.48)], 0.7),
                ([GrowArrow(vec_v), FadeIn(pt_dot), FadeIn(pt_lbl), Create(dash_x), Create(dash_y), FadeIn(x_coord_lbl), FadeIn(y_coord_lbl)], 1.6),
                ([Write(map_eq_lhs), FadeIn(col_note, shift=UP * 0.08), FadeIn(caption)], 1.8),
            ],
            post_wait=1.7,
        )

        # ------------------------------------------------------------------
        # Beat 2.3
        # ------------------------------------------------------------------
        self.play_beat(
            "2.3",
            [
                ([FadeOut(col_note), Write(map_eq_rhs)], 1.4),
                ([FadeIn(rule_card, shift=UP * 0.12)], 1.2),
                ([Indicate(rule_tex, color=CYAN, scale_factor=1.06)], 1.1),
            ],
            post_wait=0.8,
        )

        # Reinforce derived coordinate rule visually before transitioning to Scene 3
        self.play(Indicate(map_eq_rhs[1], color=CYAN, scale_factor=1.08), run_time=1.0)
        self.wait(1.2)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)

