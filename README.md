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

Before opening an `mxfile`, the host uses the bundled editor's decoder to
check every compressed or uncompressed page for a readable graph model. A
corrupt page is rejected before the current drawing and its save target change.
This check is not a guarantee that every valid-looking diagram will render.
Decoding very large pages
can consume substantial browser memory. Local desktop and emulated-phone tests
cover an uploaded corrupt page, a corrupt later page, a valid two-page compressed
file, and preservation, editing, synchronization and reopening of the previous
drawing. Physical touch and every diagram variant remain unverified.

An initial restore clears its file association when the file is missing or
invalid. A conflict or transient read failure retains the association for a
later retry. Local desktop and emulated-phone tests inject both kinds of
temporary failure; they do not simulate every network or storage failure.

The host waits for a matching load response and observes the pinned editor's
actual load and error methods before associating a selected file. The canvas is
inert and close asks for confirmation while loading. If the editor reports an
error or does not confirm within 15 seconds, the prior file association remains
and the window is locked against editing and saving: close it and reopen the
last saved drawing. An uncertain load may have changed the visible canvas, so
unsaved work may be lost. Local desktop and emulated-phone tests inject an
editor exception, delayed and missing responses, a late response after timeout,
and closing while a load is pending. This adapter depends on the pinned upstream
protocol and methods and must be requalified on upgrade; it is not proof that
every possible draw.io rendering defect is detected. Physical touch is unverified.

Run `python3 apps/system/diagrams-net/prepare.py` before building. It retrieves
and checks the pinned upstream commit listed there; generated `node_modules`
and application bundles are not source files. The upstream license is in
`LICENSE.drawio.txt`.

Save as records the chosen destination and edit revision before asking the embedded editor for XML. Changes made while it prepares the diagram remain marked unsaved; the actual saved path is shown. A separate notice reports mirror-detected changes, conflicts or unavailability of the saved file while keeping the current diagram open. Resolve conflicts in Files or save a copy. Detection depends on mirror synchronization. Local desktop, emulated-phone and 4K and live emulated-phone account tests cover delayed export, newer edits, changes/conflicts, fresh-session reopen and listener cleanup.

Closing asks for confirmation while the editor is preparing a save or the
account write is in progress, even when the diagram was previously clean. A
write already sent to storage may still finish after the window closes.

The current File-menu integration handles the upstream menu’s pointer events for mouse and touch, while retaining keyboard activation. Local account workflows pass with real mouse clicks, emulated taps, keyboard activation and a 4K-sized viewport; the save snapshot and conflict test passes locally. Initial direct-click tests missed an upstream event interception; pointer-based tests exposed it and the candidate was corrected. Touch movement beyond the tap threshold does not intentionally activate a command, but physical phone gestures remain unverified. The integration is live in static release `86f7fbc0e7c9610d641b96f0e0afa9f5f3ccb9f39599f4a42b065d3065058bb2`; public desktop mouse and emulated-phone tap account workflows passed, including upload, sync, reopen and fallback.

If the diagram changes during the discard confirmation, Open is cancelled so
the newer edit stays available. Local desktop and emulated-phone checks cover
a delayed embedded-editor autosave, plus the account save/reopen workflow.
Physical touch and overlapping Open invocations remain unverified.

The editor's Export as workflow sends supported local exports to My files.
SVG and PNG exports were checked with the actual export dialog, overwrite
cancellation and a changed-target conflict. Files are saved on the device and
sync to the account server. The bridge intercepts the pinned editor's local
save API; other upstream export types, large files and physical-phone touch
remain unverified. If an export supplies an unsupported data type, the app
reports that it cannot save it rather than offering a device download.

Opening or saving a diagram updates the desktop restore reference. If the
initial file is missing or invalid, the failed reference is cleared without
modifying the original file. Local desktop and emulated-phone account tests
cover switching diagrams, Save As, server sync and refresh; phone-sized checks
cover invalid and missing file fallback. Physical touch remains unverified.

If the restored diagram cannot be read temporarily, **Retry saved diagram**
reopens it without leaving the window. Scratch work uses a separate save
path, including `/Untitled-recovery.drawio` if the original was named
`/Untitled.drawio`. Retry asks before discarding unsaved scratch edits;
saving or opening a different file clears the retry target. Local account
tests covered injected read failure, separate blank scratch save and sync,
confirmation cancellation and Retry on desktop and an emulated phone. They
injected the scratch edit notification; actual drawing interaction in this
particular recovery path, physical touch and other failure modes remain
unverified.

Exports now suggest a destination beside the saved drawing, while preserving
the upstream export filename and letting the user edit both folder and name.
Local registered-account desktop and emulated-phone checks opened a labeled
diagram, saved it in a folder, exported SVG beside it, verified the label and
server sync, and exercised PNG, cancellation and overwrite conflict. Physical
touch and all export formats remain unverified.

Save As accepts one name choice at a time and rejects it if the diagram changed
while the prompt was open; choose the name again to save the current work. Local
registered-account desktop and phone-sized tests injected a delayed autosave,
then saved an actual edited label, synced it and reopened it in a fresh browser.

In the inspected offline **File → Import from** menu, only the computer Device
option appeared; Google Drive, Dropbox, OneDrive, GitHub and GitLab options did
not. The computer import remains available alongside account-backed Open. Local
desktop and emulated-phone menu checks observed no external HTTP requests in
that flow. This is a limited menu check, not a complete provider or network
security audit; no new provider features were disabled by this change.

Image/PDF export produces a snapshot. If the editor reports changes while the
result is waiting for its destination or account write, the status says that
newer changes are not included; the open diagram stays unsaved. Conflicting
copies are still reported. Local registered-account desktop and emulated-phone
tests hold an actual SVG write, edit a diagram label, compare the exported
snapshot, save the newer diagram, sync and reopen it. Changes before the
upstream editor delivers its export to the host are not necessarily detected,
and physical touch remains unverified.
