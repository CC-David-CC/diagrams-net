# diagrams.net

A local diagrams.net editor embedded per window. Open diagrams from My files;
use Files to upload a `.drawio` document from the computer. Save diagram writes
to My files, first on the browser and then through account sync. Expand Save
location to choose a folder or change the `.drawio` filename. Existing files
require confirmation and the file service checks versions; conflicts are
reported without silently replacing another copy.

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

Save diagram records the chosen destination and edit revision before asking the embedded editor for XML. Changes made while it prepares the diagram remain marked unsaved; the actual saved path is shown. A separate notice reports mirror-detected changes, conflicts or unavailability of the saved file while keeping the current diagram open. Resolve conflicts in Files or save a copy. Detection depends on mirror synchronization. Local desktop, emulated-phone and 4K and live emulated-phone account tests cover delayed export, newer edits, changes/conflicts, fresh-session reopen and listener cleanup.
