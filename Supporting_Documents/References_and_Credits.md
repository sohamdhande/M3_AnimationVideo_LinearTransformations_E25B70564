# References, Licenses, and Credits

**Project:** *Matrices in Motion: How a 2×2 Matrix Transforms the Plane*  
**Author:** Soham Dhande (`E25B70564`)

---

## 1. Mathematical References

1. **Gilbert Strang**, *Introduction to Linear Algebra* (5th/6th Edition, Wellesley-Cambridge Press) — Linear transformations, column picture of matrix-vector multiplication, and geometric interpretation of determinants.
2. **Sheldon Axler**, *Linear Algebra Done Right* (Springer) — Linear maps on finite-dimensional vector spaces, standard bases, and invertibility criteria.
3. **David C. Lay, Steven R. Lay, & Judi J. McDonald**, *Linear Algebra and Its Applications* (Pearson) — Matrix transformations of $\mathbb{R}^2$, unit-square area scaling, and orientation preservation.

---

## 2. Software & Production Stack

| Tool / Library | Version | License / Attribution | Role in Project |
|---|---|---|---|
| **Python** | `3.11.14` | PSF License | Core programming runtime |
| **Manim Community Edition** | `0.22.1` | MIT License | Programmatic 2D mathematical animation & scene rendering |
| **Manim Voiceover** | `0.4.0` | MIT License | Beat-level voiceover caching, synchronization trackers, and `.srt` subtitles |
| **Google GenAI SDK / Gemini TTS** | `2.34.0` (`gemini-3.1-flash-tts-preview`, voice `Kore`) | Google Generative AI Terms | Educational English narration synthesis |
| **BasicTeX / TeX Live** | `2026` (`pdflatex`, `dvisvgm 3.6`) | TeX Live / LPPL | LaTeX mathematical typesetting for `MathTex` and storyboard PDF |
| **FFmpeg / FFprobe** | `8.1.2` | LGPL / GPL | Scene assembly (`libx264` / `aac`), stream auditing, and loudness verification |
| **SoX** | `14.4.2_6` | GPL / LGPL | Audio processing backend required by Manim Voiceover |

---

## 3. Music & Third-Party Media Credits

- **Background Music:** **No background music used.** The audio track consists solely of clear educational narration to maximize mathematical intelligibility.
- **Third-Party Video, Footage, or Image Assets:** **None used.** Every visual frame—coordinate planes, basis vectors, matrix panels, polygons, dashed traces, and title/credit cards—is original Python/Manim code written for this project.
- **Typography:** System sans-serif (`Avenir Next` on macOS, with `Helvetica Neue` / `DejaVu Sans` / `Arial` fallback) and Computer Modern mathematical glyphs via TeX Live 2026.

---

## 4. AI Assistance Credit

See [AI_Disclosure.md](AI_Disclosure.md) for the complete AI tools and verification disclosure.

