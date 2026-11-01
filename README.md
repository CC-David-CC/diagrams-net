# diagrams.net

A local diagrams.net editor embedded per window. Use **File → Open from My files…**
to open a diagram. To upload a `.drawio` document from the computer, use Files
first. **File → Save** writes the current diagram to My files; **File → Save as…**
chooses another path. Files are saved in the browser and then synchronized with
the account. Existing files require confirmation and the file service checks
versions; conflicts are reported without silently replacing another copy. The
two added menu commands integrate with the pinned upstream editor menu; review
the integration when updating diagrams.net. If the editor menu cannot be
connected, recovery controls appear above it for opening and saving work.

Opening checks the XML document before replacing the current diagram and keeps
unsaved work if reading or validation fails. The editor remains the upstream
interface and has not yet received a full touch usability review. Browser
viewport emulation is not physical-phone evidence. Large and unusual diagrams,
all upstream export formats, and third-party integrations have not been broadly
qualified. The embedded editor uses local assets, with plugin and optional
network features disabled in its launch configuration.

Run `python3 apps/system/diagrams-net/prepare.py` before building. It retrieves
and checks the pinned upstream commit listed there; generated `node_modules`
and application bundles are not source files. The upstream license is in
`LICENSE.drawio.txt`.

Save as records the chosen destination and edit revision before asking the embedded editor for XML. Changes made while it prepares the diagram remain marked unsaved; the actual saved path is shown. A separate notice reports mirror-detected changes, conflicts or unavailability of the saved file while keeping the current diagram open. Resolve conflicts in Files or save a copy. Detection depends on mirror synchronization. Local desktop, emulated-phone and 4K and live emulated-phone account tests cover delayed export, newer edits, changes/conflicts, fresh-session reopen and listener cleanup.

The local File-menu candidate handles the upstream menu’s pointer events for mouse and touch, while retaining keyboard activation. Local account workflows pass with real mouse clicks, emulated taps, keyboard activation and a 4K-sized viewport; the save snapshot and conflict test passes locally. Initial direct-click tests missed an upstream event interception; pointer-based tests exposed it and the candidate was corrected. Touch movement beyond the tap threshold does not intentionally activate a command, but physical phone gestures remain unverified. This candidate is not live.
