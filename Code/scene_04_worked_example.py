"""Scene 4: Worked Example (Target ~80-90 s, Beats 4.1 - 4.4).

Tracks sample point (1, 2) through step-by-step row-by-column matrix multiplication
without skipping intermediate arithmetic, then animates (1, 2) -> (4, 2) alongside
the transformed grid lines and head-to-tail basis combination 1*Ae1 + 2*Ae2 = (4, 2).
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
    GRID,
    MUTED,
    PANEL_BG,
    PANEL_STROKE,
    TEAL,
    TEXT_WHITE,
    BaseM3Scene,
    make_bottom_caption,
    make_card,
    make_scene_header,
    pill_label,
)


class Scene04WorkedExample(BaseM3Scene):
    def construct(self):
        self.setup_scene()

        header = make_scene_header(
            "Scene 4  •  Worked Example",
            "Tracking the Point (1, 2) Step by Step",
            self.sans_font,
        )

        # ------------------------------------------------------------------
        # Left Stage: Coordinate Plane covering x in [-1, 5], y in [-1, 3]
        # Holds both (1, 2) and (4, 2) with generous margins.
        # ------------------------------------------------------------------
        unit = 0.88
        plane = NumberPlane(
            x_range=[-1, 5, 1],
            y_range=[-1, 3, 1],
            x_length=6 * unit,
            y_length=4 * unit,
            axis_config={"stroke_color": AXIS, "stroke_width": 2.0},
            background_line_style={
                "stroke_color": GRID,
                "stroke_width": 1.25,
                "stroke_opacity": 0.62,
            },
        ).move_to(LEFT * 3.65 + DOWN * 0.20)

        origin = plane.c2p(0, 0)
        origin_dot = Dot(origin, radius=0.05, color=AXIS).set_z_index(4)
        x_lbl = MathTex("x", color=MUTED).scale(0.58).next_to(plane.c2p(5, 0), UP + LEFT * 0.1, buff=0.10)
        y_lbl = MathTex("y", color=MUTED).scale(0.58).next_to(plane.c2p(0, 3), UP, buff=0.08)

        # Subtle numeric tick labels on x and y axes for instant coordinate reading
        tick_labels = VGroup()
        for xv in (1, 2, 3, 4):
            tick_labels.add(
                MathTex(str(xv), color=MUTED).scale(0.46).next_to(plane.c2p(xv, 0), DOWN, buff=0.10)
            )
        for yv in (1, 2):
            tick_labels.add(
                MathTex(str(yv), color=MUTED).scale(0.46).next_to(plane.c2p(0, yv), LEFT, buff=0.10)
            )

        p_old = plane.c2p(1, 2)
        p_new = plane.c2p(4, 2)
        dot_old_ghost = Dot(p_old, radius=0.065, color=CORAL, fill_opacity=0.45).set_z_index(3)
        dot_active = Dot(p_old, radius=0.09, color=CORAL).set_z_index(5)
        lbl_old = pill_label(
            MathTex(r"(1,2)", color=CORAL).scale(0.60).next_to(p_old, UP, buff=0.14)
        ).set_z_index(5)
        lbl_new = pill_label(
            MathTex(r"(4,2)", color=CORAL).scale(0.62).next_to(p_new, UP, buff=0.14)
        ).set_z_index(5)

        # ------------------------------------------------------------------
        # Right Stage: Step-by-step Matrix Multiplication Card
        # ------------------------------------------------------------------
        right_center = RIGHT * 3.15 + DOWN * 0.16
        card_bg = RoundedRectangle(
            width=6.35,
            height=4.95,
            corner_radius=0.18,
            stroke_color=PANEL_STROKE,
            stroke_width=1.3,
            fill_color=PANEL_BG,
            fill_opacity=0.95,
        ).move_to(right_center)

        # Top row inside card: A * [1, 2]^T
        setup_eq = MathTex(
            r"T\begin{bmatrix} 1 \\ 2 \end{bmatrix}",
            r"=",
            r"\begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}",
            r"\begin{bmatrix} 1 \\ 2 \end{bmatrix}",
            color=TEXT_WHITE,
        ).scale(0.76)
        setup_eq[0].set_color(TEAL)
        setup_eq[3].set_color(CORAL)
        setup_eq.move_to(right_center + UP * 1.55)

        # Highlight boxes for Row 1 & Row 2 of A and the input column vector
        mat_a_part = setup_eq[2]
        row1_box = SurroundingRectangle(
            VGroup(mat_a_part[1], mat_a_part[2]), color=CYAN, buff=0.07, corner_radius=0.05, stroke_width=2.1
        )
        row2_box = SurroundingRectangle(
            VGroup(mat_a_part[3], mat_a_part[4]), color=AMBER, buff=0.07, corner_radius=0.05, stroke_width=2.1
        )
        col_box = SurroundingRectangle(
            setup_eq[3], color=CORAL, buff=0.07, corner_radius=0.05, stroke_width=2.0
        )

        # Intermediate row-by-row arithmetic (never skipped!)
        row1_tag = Text("Row 1:", font_size=15, weight=BOLD, color=CYAN, font=self.sans_font)
        row1_math = MathTex(r"2(1) + 1(2) = 2 + 2 = 4", color=TEXT_WHITE).scale(0.66)
        row1_math[0][-1].set_color(CYAN)
        row1_line = VGroup(row1_tag, row1_math).arrange(RIGHT, buff=0.22)
        row1_line.move_to(right_center + UP * 0.42)

        row2_tag = Text("Row 2:", font_size=15, weight=BOLD, color=AMBER, font=self.sans_font)
        row2_math = MathTex(r"0(1) + 1(2) = 0 + 2 = 2", color=TEXT_WHITE).scale(0.66)
        row2_math[0][-1].set_color(AMBER)
        row2_line = VGroup(row2_tag, row2_math).arrange(RIGHT, buff=0.22)
        row2_line.move_to(right_center + DOWN * 0.30)

        # Final assembled result column vector
        result_eq = MathTex(
            r"A\begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}",
            color=TEXT_WHITE,
        ).scale(0.76)
        result_eq[0][-4:].set_color(CORAL)
        result_card = make_card(result_eq, pad_x=0.42, pad_y=0.20, stroke_color=CORAL)
        result_card.move_to(right_center + DOWN * 1.48)

        # Linear combination verification badge (swapped in during Beat 4.4)
        lincomb_eq = MathTex(
            r"1\cdot Ae_1 + 2\cdot Ae_2 = (2,0) + (2,2) = (4,2)",
            color=TEAL,
        ).scale(0.54)
        lincomb_card = make_card(lincomb_eq, pad_x=0.34, pad_y=0.18, stroke_color=TEAL)
        lincomb_card.move_to(right_center + DOWN * 1.50)

        caption = make_bottom_caption("WORKED POINT: (1, 2) AS A COLUMN VECTOR", self.sans_font, MUTED)

        # ------------------------------------------------------------------
        # Beat 4.1 — Highlight point (1, 2) and write A * [1, 2]^T
        # ------------------------------------------------------------------
        self.play_beat(
            "4.1",
            [
                ([FadeIn(header, shift=DOWN * 0.1), Create(plane), FadeIn(origin_dot), FadeIn(x_lbl), FadeIn(y_lbl), FadeIn(tick_labels), FadeIn(card_bg), FadeIn(caption)], 1.6),
                ([FadeIn(dot_active, scale=1.4), FadeIn(lbl_old), Write(setup_eq)], 1.8),
            ],
            post_wait=0.8,
        )

        # ------------------------------------------------------------------
        # Beat 4.2 — Row 1 dot product: 2(1) + 1(2) = 2 + 2 = 4
        # ------------------------------------------------------------------
        caption_r1 = make_bottom_caption("ROW 1 DOT PRODUCT: 2(1) + 1(2) = 4", self.sans_font, CYAN)
        self.play_beat(
            "4.2",
            [
                ([Create(row1_box), Create(col_box), ReplacementTransform(caption, caption_r1)], 1.0),
                ([FadeIn(row1_tag), Write(row1_math)], 2.8),
                ([Indicate(row1_math[0][-1], color=CYAN, scale_factor=1.25)], 1.0),
            ],
            post_wait=1.0,
        )

        # ------------------------------------------------------------------
        # Beat 4.3 — Row 2 dot product: 0(1) + 1(2) = 0 + 2 = 2
        # ------------------------------------------------------------------
        caption_r2 = make_bottom_caption("ROW 2 DOT PRODUCT: 0(1) + 1(2) = 2", self.sans_font, AMBER)
        self.play_beat(
            "4.3",
            [
                ([ReplacementTransform(row1_box, row2_box), ReplacementTransform(caption_r1, caption_r2)], 0.9),
                ([FadeIn(row2_tag), Write(row2_math)], 2.2),
                ([FadeOut(row2_box), FadeOut(col_box), FadeIn(result_card, shift=UP * 0.1)], 1.1),
            ],
            post_wait=1.0,
        )

        # ------------------------------------------------------------------
        # Beat 4.4 — Glide (1, 2) -> (4, 2) & show 1*Ae1 + 2*Ae2 on transformed grid
        # ------------------------------------------------------------------
        # Exact transformed local grid for [0, 1] x [0, 2] under A:
        # Lines stay 100% inside x in [0, 4], y in [0, 2] on the left plane.
        t_grid = VGroup(
            Line(plane.c2p(0, 0), plane.c2p(2, 2), color=TEAL, stroke_width=1.6, stroke_opacity=0.65),
            Line(plane.c2p(2, 0), plane.c2p(4, 2), color=TEAL, stroke_width=1.6, stroke_opacity=0.65),
            Line(plane.c2p(0, 0), plane.c2p(2, 0), color=TEAL, stroke_width=1.6, stroke_opacity=0.65),
            Line(plane.c2p(1, 1), plane.c2p(3, 1), color=TEAL, stroke_width=1.6, stroke_opacity=0.65),
            Line(plane.c2p(2, 2), plane.c2p(4, 2), color=TEAL, stroke_width=1.6, stroke_opacity=0.65),
        ).set_z_index(2)

        trace = DashedLine(
            p_old, p_new, dash_length=0.09, color=CORAL, stroke_opacity=0.65, stroke_width=2.2
        ).set_z_index(2)

        # Head-to-tail basis walk: 1 * Ae1 = (2, 0) then + 2 * Ae2 = (2, 2) -> (4, 2)
        step_ae1 = Arrow(origin, plane.c2p(2, 0), buff=0, color=CYAN, stroke_width=5.0).set_z_index(4)
        step_ae1_lbl = pill_label(
            MathTex(r"1\cdot Ae_1", color=CYAN).scale(0.54).next_to(step_ae1, DOWN, buff=0.22)
        ).set_z_index(5)
        step_2ae2 = Arrow(plane.c2p(2, 0), p_new, buff=0, color=AMBER, stroke_width=5.0).set_z_index(4)
        step_2ae2_lbl = pill_label(
            MathTex(r"2\cdot Ae_2", color=AMBER).scale(0.54).next_to(step_2ae2.get_center(), RIGHT + DOWN * 0.2, buff=0.14)
        ).set_z_index(5)

        caption_geom = make_bottom_caption(
            "(1, 2) ↦ (4, 2)   •   1·Ae₁ + 2·Ae₂ = (4, 2)",
            self.sans_font,
            TEAL,
        )

        self.add(dot_old_ghost)
        self.play_beat(
            "4.4",
            [
                (
                    [
                        plane.animate.set_opacity(0.32),
                        Create(trace),
                        dot_active.animate.move_to(p_new),
                        FadeIn(lbl_new),
                        ReplacementTransform(caption_r2, caption_geom),
                    ],
                    2.2,
                ),
                ([Create(t_grid)], 1.0),
                ([GrowArrow(step_ae1), FadeIn(step_ae1_lbl)], 1.4),
                ([GrowArrow(step_2ae2), FadeIn(step_2ae2_lbl), ReplacementTransform(result_card, lincomb_card)], 1.8),
            ],
            post_wait=2.0,
        )

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)

