"""Scene 5: Interpretation (Target ~70 s, Beats 5.1 - 5.4).

Transforms the unit square into its image parallelogram with all four mapped corners
labeled (0,0), (2,0), (3,1), (1,1), demonstrates Area = base * height = 2 * 1 = 2,
computes det(A) = 2*1 - 1*0 = 2, and explains |det(A)| (area scaling), det(A) > 0
(orientation preservation), and det(A) != 0 (invertibility).
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
    GRID,
    MUTED,
    PANEL_BG,
    PANEL_STROKE,
    TEAL,
    TEXT_WHITE,
    BaseM3Scene,
    make_bottom_caption,
    make_scene_header,
    pill_label,
)


class Scene05Interpretation(BaseM3Scene):
    def construct(self):
        self.setup_scene()

        header = make_scene_header(
            "Scene 5  •  Geometric Interpretation",
            "Determinant, Area Scaling & Orientation",
            self.sans_font,
        )

        # ------------------------------------------------------------------
        # Left Stage: Coordinate Plane covering x in [-1, 4], y in [-1, 3]
        # ------------------------------------------------------------------
        unit = 1.02
        plane = NumberPlane(
            x_range=[-1, 4, 1],
            y_range=[-1, 3, 1],
            x_length=5 * unit,
            y_length=4 * unit,
            axis_config={"stroke_color": AXIS, "stroke_width": 2.0},
            background_line_style={
                "stroke_color": GRID,
                "stroke_width": 1.25,
                "stroke_opacity": 0.58,
            },
        ).move_to(LEFT * 3.55 + DOWN * 0.22)

        origin = plane.c2p(0, 0)
        x_lbl = MathTex("x", color=MUTED).scale(0.58).next_to(plane.c2p(4, 0), UP + LEFT * 0.1, buff=0.10)
        y_lbl = MathTex("y", color=MUTED).scale(0.58).next_to(plane.c2p(0, 3), UP, buff=0.08)

        # Original unit square (ghost outline kept for visual contrast)
        sq_pts = [plane.c2p(0, 0), plane.c2p(1, 0), plane.c2p(1, 1), plane.c2p(0, 1)]
        para_pts = [plane.c2p(0, 0), plane.c2p(2, 0), plane.c2p(3, 1), plane.c2p(1, 1)]

        unit_square_ghost = DashedVMobject(
            Polygon(*sq_pts, color=AXIS, stroke_width=1.6, stroke_opacity=0.55),
            num_dashes=24,
        ).set_z_index(1)

        active_poly = Polygon(
            *sq_pts,
            color=TEAL,
            stroke_width=2.4,
            fill_color=TEAL,
            fill_opacity=0.24,
        ).set_z_index(2)

        target_poly = Polygon(
            *para_pts,
            color=TEAL,
            stroke_width=2.6,
            fill_color=TEAL,
            fill_opacity=0.30,
        ).set_z_index(2)

        area1_lbl = pill_label(
            MathTex(r"\text{Area}=1", color=TEXT_WHITE).scale(0.46).move_to(plane.c2p(0.5, 0.5))
        ).set_z_index(4)
        area2_lbl = pill_label(
            MathTex(r"\text{Area}=2", color=TEAL).scale(0.54).move_to(plane.c2p(1.62, 0.52))
        ).set_z_index(4)

        e1 = Arrow(origin, plane.c2p(1, 0), buff=0, color=CYAN, stroke_width=4.8).set_z_index(3)
        e2 = Arrow(origin, plane.c2p(0, 1), buff=0, color=AMBER, stroke_width=4.8).set_z_index(3)
        ae1 = Arrow(origin, plane.c2p(2, 0), buff=0, color=CYAN, stroke_width=4.8).set_z_index(3)
        ae2 = Arrow(origin, plane.c2p(1, 1), buff=0, color=AMBER, stroke_width=4.8).set_z_index(3)

        # Mapped corner dots and labels
        corner_dots = VGroup(*[Dot(pt, radius=0.065, color=TEXT_WHITE).set_z_index(5) for pt in para_pts])
        c00_lbl = pill_label(MathTex(r"(0,0)", color=MUTED).scale(0.50).next_to(para_pts[0], DOWN + LEFT, buff=0.10)).set_z_index(5)
        c20_lbl = pill_label(MathTex(r"(2,0)", color=CYAN).scale(0.52).next_to(para_pts[1], DOWN + RIGHT * 0.25, buff=0.10)).set_z_index(5)
        c31_lbl = pill_label(MathTex(r"(3,1)", color=TEAL).scale(0.52).next_to(para_pts[2], UP + RIGHT * 0.25, buff=0.10)).set_z_index(5)
        c11_lbl = pill_label(MathTex(r"(1,1)", color=AMBER).scale(0.52).next_to(para_pts[3], UP + LEFT * 0.25, buff=0.10)).set_z_index(5)
        corner_labels = VGroup(c00_lbl, c20_lbl, c31_lbl, c11_lbl)

        # Base & height geometric annotations
        base_brace = Brace(Line(plane.c2p(0, 0), plane.c2p(2, 0)), direction=DOWN, color=CYAN, buff=0.42).set_z_index(4)
        base_lbl = pill_label(
            MathTex(r"\text{base} = 2", color=CYAN).scale(0.54).next_to(base_brace, DOWN, buff=0.08)
        ).set_z_index(5)

        alt_top = plane.c2p(3, 1)
        alt_bot = plane.c2p(3, 0)
        alt_line = DashedLine(alt_top, alt_bot, dash_length=0.08, color=AMBER, stroke_width=2.4).set_z_index(4)
        base_ext = DashedLine(plane.c2p(2, 0), alt_bot, dash_length=0.08, color=AXIS, stroke_opacity=0.65, stroke_width=1.8).set_z_index(3)
        right_angle = RightAngle(
            Line(alt_bot, alt_top),
            Line(alt_bot, plane.c2p(2, 0)),
            length=0.18,
            color=AMBER,
            stroke_width=1.8,
        ).set_z_index(4)
        height_lbl = pill_label(
            MathTex(r"h = 1", color=AMBER).scale(0.54).next_to(alt_line, RIGHT, buff=0.12)
        ).set_z_index(5)

        # Subtle counter-clockwise orientation arc between Ae1 and Ae2
        orient_arc = CurvedArrow(
            plane.c2p(0.72, 0.08),
            plane.c2p(0.54, 0.48),
            angle=PI / 4,
            color=TEAL,
            stroke_width=2.6,
            tip_length=0.14,
        ).set_z_index(5)

        # ------------------------------------------------------------------
        # Right Stage: Area, Determinant & 3 Interpretation Badges Card
        # ------------------------------------------------------------------
        right_center = RIGHT * 3.15 + DOWN * 0.16
        card_bg = RoundedRectangle(
            width=6.35,
            height=5.05,
            corner_radius=0.18,
            stroke_color=PANEL_STROKE,
            stroke_width=1.3,
            fill_color=PANEL_BG,
            fill_opacity=0.95,
        ).move_to(right_center)

        area_eq = MathTex(
            r"\text{Area} = \text{base} \times \text{height} = 2 \times 1 = 2",
            color=TEXT_WHITE,
        ).scale(0.64)
        area_eq[0][-1].set_color(TEAL)
        area_eq.move_to(right_center + UP * 1.85)

        det_eq = MathTex(
            r"\det(A) = \begin{vmatrix} 2 & 1 \\ 0 & 1 \end{vmatrix} = 2\cdot 1 - 1\cdot 0 = 2",
            color=TEXT_WHITE,
        ).scale(0.62)
        det_eq[0][-1].set_color(TEAL)
        det_eq.move_to(right_center + UP * 0.85)

        divider = Line(
            right_center + LEFT * 2.75 + UP * 0.22,
            right_center + RIGHT * 2.75 + UP * 0.22,
            color=PANEL_STROKE,
            stroke_width=1.2,
        )

        def _make_badge(math_str: str, desc_str: str, accent: str) -> VGroup:
            m = MathTex(math_str, color=accent).scale(0.56)
            d = Text(desc_str, font_size=15, color=TEXT_WHITE, font=self.sans_font)
            row = VGroup(m, d).arrange(RIGHT, buff=0.22)
            box = RoundedRectangle(
                width=5.65,
                height=0.64,
                corner_radius=0.10,
                stroke_color=accent,
                stroke_width=1.2,
                fill_color="#0E1722",
                fill_opacity=0.96,
            )
            row.move_to(box.get_center())
            return VGroup(box, row)

        badge_area = _make_badge(r"|\det(A)| = 2", "Areas scale by factor 2", CYAN)
        badge_orient = _make_badge(r"\det(A) > 0", "Orientation preserved", TEAL)
        badge_inv = _make_badge(r"\det(A) \neq 0", "Invertible (no collapse)", AMBER)
        badges = VGroup(badge_area, badge_orient, badge_inv).arrange(DOWN, buff=0.20)
        badges.move_to(right_center + DOWN * 1.08)

        caption = make_bottom_caption("UNIT SQUARE → PARALLELOGRAM WITH AREA 2", self.sans_font, MUTED)

        # ------------------------------------------------------------------
        # Beat 5.1 — Transform unit square -> parallelogram & label 4 corners
        # ------------------------------------------------------------------
        self.play_beat(
            "5.1",
            [
                ([FadeIn(header, shift=DOWN * 0.1), Create(plane), FadeIn(x_lbl), FadeIn(y_lbl), FadeIn(card_bg), FadeIn(caption)], 1.4),
                ([FadeIn(active_poly), GrowArrow(e1), GrowArrow(e2), FadeIn(area1_lbl)], 1.5),
                (
                    [
                        FadeIn(unit_square_ghost),
                        FadeOut(area1_lbl),
                        Transform(active_poly, target_poly),
                        Transform(e1, ae1),
                        Transform(e2, ae2),
                    ],
                    2.6,
                ),
                ([FadeIn(corner_dots), FadeIn(corner_labels)], 1.6),
            ],
            post_wait=0.8,
        )

        # ------------------------------------------------------------------
        # Beat 5.2 — Base 2, height 1 -> Area = 2 * 1 = 2
        # ------------------------------------------------------------------
        self.play_beat(
            "5.2",
            [
                ([GrowFromCenter(base_brace), FadeIn(base_lbl)], 1.5),
                ([Create(base_ext), Create(alt_line), Create(right_angle), FadeIn(height_lbl)], 1.5),
                ([Write(area_eq), FadeIn(area2_lbl)], 1.8),
            ],
            post_wait=0.8,
        )

        # ------------------------------------------------------------------
        # Beat 5.3 — Algebraic determinant det(A) = 2(1) - 1(0) = 2
        # ------------------------------------------------------------------
        caption_det = make_bottom_caption("DETERMINANT EQUALS SIGNED AREA SCALE: det(A) = 2", self.sans_font, TEAL)
        self.play_beat(
            "5.3",
            [
                ([Write(det_eq), ReplacementTransform(caption, caption_det)], 2.2),
                ([Indicate(det_eq[0][-1], color=TEAL, scale_factor=1.3), Indicate(area_eq[0][-1], color=TEAL, scale_factor=1.3)], 1.2),
            ],
            post_wait=0.8,
        )

        # ------------------------------------------------------------------
        # Beat 5.4 — |det(A)|, det(A) > 0, det(A) != 0
        # ------------------------------------------------------------------
        self.play_beat(
            "5.4",
            [
                ([Create(divider), FadeIn(badge_area, shift=UP * 0.1)], 1.6),
                ([FadeIn(badge_orient, shift=UP * 0.1), Create(orient_arc)], 2.0),
                ([FadeIn(badge_inv, shift=UP * 0.1)], 1.6),
                ([Indicate(badge_area[1][0], color=CYAN, scale_factor=1.10), Indicate(badge_orient[1][0], color=TEAL, scale_factor=1.10), Indicate(badge_inv[1][0], color=AMBER, scale_factor=1.10)], 1.2),
            ],
            post_wait=1.8,
        )

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)

