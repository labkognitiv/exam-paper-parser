# Kognitiv app — student experience and navigation specification

Date: 12 September 2026  
Status: UI/UX visualization only. Revised after user clarification and agent review on 12 September 2026. Prototype code remains unchanged.  
Owner: Existing Kognitiv dashboard prototype in this Physics workspace; intended experience spans all seven subjects.

Quick navigation: [App structure](#4-information-architecture) · [Onboarding](#5-onboarding-and-account-entry) · [Study](#8-study-module-lesson-notes-and-questions) · [Progress rules](#9-completion-and-progress-rules--proposed-not-implemented) · [Revision](#10-revision-hub-and-topical-setup) · [Games](#12-games-and-reuse-of-the-existing-path) · [Shared player](#13-shared-question-player) · [Review](#14-review-a-queue-not-isolated-popups) · [Analytics](#16-analytics-and-the-progress-tracker) · [Screen register](#19-screen-register-and-return-behaviour) · [Open decisions](#22-open-decisions-and-recommended-defaults).

## 1. Purpose and decision status

Give students one understandable route from choosing a subject to learning, practising, reviewing mistakes and seeing progress. Keep the current visual theme. Reveal detail when useful, without putting every capability on every screen.

**Confirmed from the brief:** Google sign-in; one name field and compulsory phone number; global dashboard; subject selection with AS/A2; subject-scoped navigation; Study, Revision, Review, Exercises and Analytics; HTML lesson notes; explicit notes completion; lesson question sets targeting 20 questions; one shared question player; Topical, Yearly and Games; reuse the existing game path; minimal visible controls; detailed drill-downs; settings at the bottom.

**Proposed below:** Labels, screen arrangements, sample progress displays, question-player variants and return paths. Descriptions of scores/completion explain what a sample screen means; they do not ask for a scoring, tracking or persistence system. Future product policies remain undecided and are not acceptance conditions for this visualization.

**Unresolved wording:** “AILD progress” is not defined; this document uses the student-facing label “Progress” without inventing an acronym. “Ailey papers” is interpreted as “Yearly papers,” consistent with the existing Revision hub. “First name (full name)” is treated as one field labelled “Name,” accepting either. Multi-subject selection in one add flow was retracted; use one subject at a time.

**Stop condition for this task:** A reviewable Markdown specification grounded in the existing prototypes, covering routes, states, calculations, mobile behaviour and unresolved decisions. No code changes, live authentication, content moves, deployment or new backend.

### 1.1 Controlling scope: visualize, do not build the product

This section governs every later use of “save,” “complete,” “submit,” “resume,” “timer” or “progress.” They describe visible controls and example states, not required working services.

- **Build later only when asked:** screen layouts, navigation, opening/closing surfaces, tabs, selectors, hover/focus details and lightweight in-memory state needed to feel the journey.
- **Use fixed sample data:** example student, subjects, modules, questions, completion percentages, graph points, review items, exercises and result screens. Values need to be internally understandable, not calculated from what the visitor does.
- **No recording:** no database, account creation, real Google OAuth, SMS, server/API writes, analytics events, answer history, files written by clicks, browser-storage persistence or synchronization. No real personal information is required to try the preview.
- **No progress engine:** marking sample notes complete may toggle that lesson's visible check during the current visit. It need not recompute dashboard charts, a streak, review counts or a curriculum tracker. Use separately selectable sample scenarios to show those screens.
- **No full question engine:** a few representative MCQ/theory/game examples are enough. Show a 20-item sample grid and ten-item Review fixture where needed to judge navigation; do not author or wire complete course banks.
- **No enforced exams:** sample countdown, running timer, expiry and results states can be selected or briefly animated. They need not survive refresh, assess answers, submit anything or follow actual deadlines.
- **Reload/reset may restore the default preview.** Keep context while clicking around, not across devices or sessions. No recovery infrastructure is required.
- **Connect routes, not data systems.** “Everything in its place” means the intended destination is visible and reachable. It does not mean each action updates every other screen.

Keep a small persistent “Design preview · sample data” label in the preview frame, outside the student's main content. Put scenario controls in a separate Preview controls menu, not among student filters. No technical setup banners inside the lesson or question flow.

| Area | Enough for visualization | Specifically not required |
| --- | --- | --- |
| Google/profile | Sign-in appearance → sample Name/Phone form → Dashboard; demonstrate required-field error | Google connection, collecting/storing contact information, identity validation |
| Subjects | Seven choices, AS/A2 step, sample card appears for this visit | Enrolment records or syllabus integration |
| Notes | Existing local HTML example; complete/incomplete appearance | Reading telemetry, version tracking, completion records |
| Questions | Representative content, local answer selection, Previous/Next/grid/support, sample results | Real grading, exhaustive banks, attempt/event storage |
| Review | Fixed ten-question example; local resolve appearance and queue navigation | Automatic mistake collection or persisted resolution |
| Games | Existing path visual style, one representative node interaction, shared-player variant | Currency, leaderboard service, full game progression or importing saved game state |
| Analytics | Fixed charts, tooltips and linked detail screens | Aggregation, tracking, mastery model or live recalculation |
| Exercises | Sample list/detail/timer/submitted/late states | Publishing pipeline, deadline enforcement or submission service |
| Settings | Example form controls and confirmation appearance | Account updates, real logout, billing or deletion |

### 1.2 Preview scenarios

Provide a small design-review scenario menu: **Populated Dashboard** (default), **New learner**, **Lesson in progress**, **Lesson complete**, **Review queue**, **Exam running**, **Exam ended**, **Empty content**, and optional **Error example**. Selecting a scenario sets up a fixed visual story; Reset preview restores the default. A designer can inspect a completion screen without answering 20 questions or waiting for an exam to end.

Within one story, labels must agree: Biology · AS remains Biology · AS; a clicked Review item 4 opens 4 of 10; a clicked chart and its detail show the same sample period. Cross-feature counters do not have to update from clicks. If another scenario is needed, select it explicitly rather than suggesting data was recorded.

## 2. Existing work and what it can supply

Paths below are relative to this document unless explicitly rooted at another subject workspace; shortened `src/` and `components/` dashboard paths are inside `kognitiv-dashboard/`. These are inspected local sources, not claims that every interaction already works.

Source entry points: [Dashboard README](kognitiv-dashboard/README.md), [current theme](kognitiv-dashboard/src/index.css), [past-paper reviewer](past-paper-question-reviewer/README.md), [Games handoff](../../../mathematics/9709/prototypes/revision-path/handoff.md), [prototype session log](SESSION-LOG.md).

| Existing source | Verified behaviour or structure | Design implication |
| --- | --- | --- |
| `kognitiv-dashboard/src/App.tsx` and `components/Sidebar.tsx` | Local page state; only Mathematics opens a subject dashboard; changing sidebar tabs clears selected subject; Exercises absent | Subject and level must become persistent navigation context |
| `src/pages/DashboardPage.tsx` | Greeting, horizontal subject cards, add modal, resume banner, four charts; add currently shows toast | Reuse composition; make add flow real in the future prototype; remove unsupported catalogue options |
| `src/pages/MathsSubjectPage.tsx` | Greeting, exam calendar, resume strip, four diagnostic charts | Reuse arrangement for every subject; replace hardcoded subject content and internal design captions |
| `src/pages/StudyPage.tsx` | Module-style cards and sample completion | Extend to module, lesson, HTML notes and question-session navigation |
| `src/pages/RevisionPage.tsx` | Topical, Yearly, Games cards; Games currently shows unavailable toast | Preserve the hub; Games needs a connected route |
| `src/pages/PhysicsTopicalPage.tsx` | Topic/lesson selection and many session filters; synthetic counts; two sample player prompts | Keep selection capability, reduce visible setup; no production counts can be inferred |
| `src/pages/YearlyPage.tsx` | Year/session/component/variant selection; three modes; countdown; placeholder player and duration presets | Reuse browse structure; connect shared player and verified per-paper metadata later |
| `src/pages/ReviewPage.tsx` | Active/Resolved lists, reason filters, single-question inspection | Replace isolated inspection with a stable session containing the visible review queue |
| `src/pages/SettingsPage.tsx` | Account, exam, subscription and help sections with sample values | Retain basic account/exam concepts; no invented billing or password flow |
| `src/index.css` | Manrope; teal actions; violet text; light canvas/sidebar; mint, peach and lavender accents | This is the current palette reference, superseding older blue-theme descriptions |
| `past-paper-question-reviewer/app/page.tsx`, `components/player/MathText.tsx`, `AnswerEditor.tsx` | Text/math/figures, answer editor, split panels, scheme/hint/walkthrough presentation | Reuse presentation patterns; editorial Pass/Flag workflows are not student Review |
| `subjects/mathematics/9709/prototypes/revision-path/` from repository root | Existing Physics AS game path, themed topics, tiered original question games and linked case; player uses `practice-player.tsx` and `practice-model.ts` | Reuse path and interaction ideas without pretending it contains seven complete courses |

Games evidence: inspected `revision-path/handoff.md`, `README.md`, and player imports. Handoff describes an 11-topic path, one populated lesson, and a ten-step ball-flight case. README retains some earlier case descriptions; validate source bank contents during integration rather than relying on those counts. Current game storage saves summaries/tier completion but does not resume the active queue after refresh. Gems, stars and a fictional leaderboard are prototype features, not approved app requirements.

## 3. Navigation principles

1. **Scope is always visible.** Students can identify “All subjects” or “Biology · AS” without opening a menu.
2. **Selecting a section never changes the subject.** Biology → Revision stays Biology. Returning from Settings restores Biology.
3. **Back means a recognisable place.** Use “Back to lessons,” “Back to papers,” or “Back to review.” Preserve filters, expanded cards and scroll position.
4. **One main action per screen.** Secondary actions remain accessible, but do not compete with Start, Continue or Finish.
5. **A session owns its question list.** Source screens choose the list; the player navigates it. No return to the list between questions.
6. **Completion is not correctness.** Show coverage, performance and activity separately.
7. **No unexplained dead ends.** Disabled sections explain that a subject is required; unavailable content gives a useful return action.
8. **Minimal does not mean hidden navigation.** Back, current scope, question position, save status and the next action are visible. Rare controls can be disclosed.
9. **Consistent naming.** “Revision” is the section; “Revise” is read-through mode; “Review” is the saved-question queue. “Exam” is a single mode label, with “Exam conditions” in its description.
10. **Restore work before offering more work.** Continue a saved session in context; never replace it silently with a fresh attempt.

## 4. Information architecture

```text
Google sign-in
└── Complete profile: Name + Phone number
    └── Dashboard — All subjects
        ├── Add subject → Choose subject → Choose AS/A2 → Add
        ├── Overall chart → Overall Analytics detail → Back to Dashboard
        ├── Settings
        └── Subject dashboard — Subject + Level
            ├── Study → Modules → Module lessons → Lesson
            │   ├── Notes → Mark notes complete → Questions
            │   └── Questions → Shared player → Results → Lesson / Next lesson
            ├── Revision
            │   ├── Topical → Select topics → Configure → Shared player → Results
            │   ├── Yearly → Year → Session/paper → Mode → Shared player → Results
            │   └── Games → Topic path → Node preview → Shared player → Path
            ├── Review → Saved questions → Shared player with queue → Review
            ├── Exercises → Exercise detail → Shared player → Submission/result
            ├── Analytics → Overview / Study / Performance → Focused detail
            └── Settings → Return to previous subject screen
```

### 4.1 Global and subject sidebar

| Item | All-subject Dashboard | Inside a subject |
| --- | --- | --- |
| Dashboard | Active/available | Subject dashboard; all-subject Dashboard has a separate visible return link |
| Study | Greyed out | Enabled in selected subject/level |
| Revision | Greyed out | Enabled in selected subject/level |
| Review | Greyed out | Enabled; quiet count only if useful |
| Exercises | Greyed out | Enabled, even when no exercises are published |
| Analytics | Greyed out | Enabled with current subject scope |
| Settings | Enabled, pinned near bottom | Enabled, pinned near bottom |

In global context, one shared helper says “Choose a subject to start.” Disabled items do not navigate or resemble loading controls. Explain on focus/tap where needed; maintain readable muted labels rather than nearly invisible text.

Inside a subject, show a compact subject/level selector above the section list and “All subjects” above it. Dashboard means that selected subject’s dashboard. Brand/home action returns to All subjects consistently. Do not reuse a single ambiguous Back arrow for both meanings. The preview keeps this context only in memory while navigating.

Global graphs must still open overall Analytics despite the greyed-out global Analytics sidebar item. **Proposed resolution:** chart click opens a dedicated overall analytics detail route, reached from Dashboard. Header says “All subjects,” Back says “Dashboard,” and the sidebar remains in global state. It does not silently activate a subject or make the disabled sidebar clickable.

### 4.2 Subject switching

The scope selector lists enrolled subject/level combinations; “Add subject” opens the same add flow. On normal pages, selecting a new subject opens its dashboard. Do not land on an arbitrary equivalent lesson or carry Biology filters into Mathematics. Preserve each scope’s previous local browsing state for later return.

During a player preview, close the player before changing subject; return to its origin first. Do not switch the question list underneath an open question. Show an example exam-leave confirmation if reviewing that scenario; no actual save or continuing background timer is required.

### 4.3 Location and browser history

Give Dashboard, scope, section, module, lesson and player an identifiable location and parent. A lightweight in-memory navigation stack is enough; URL routing is optional. No real session identifiers, authenticated deep links or server routes are required.

Visible Back/Close returns to the prior design screen. If browser history is used, it must match that flow; question-to-question movement must not add 20 page-history entries. Remember position and list filters for the current preview visit. Reload may reset everything to the selected starting scenario. If a screen is opened directly through Preview controls, use the deterministic parent in the screen register.

## 5. Onboarding and account entry

### 5.1 Sign-in screen

Show Kognitiv branding, one sentence about learning, and “Continue with Google.” No password, school, exam board, subject preferences, subscription choices or goal questionnaire. Do not ask students to type an email already supplied by Google.

“Continue with Google” advances to the sample profile screen without contacting Google. New-learner and returning-learner paths are chosen through Preview controls. Optional cancelled/failed sign-in appearances are fixed examples, not real requests. Use a fictional name and phone number; do not ask the reviewer to supply real contact information.

### 5.2 Profile form

| Control | Behaviour |
| --- | --- |
| Name | One required field labelled “Name”; Google value may be prefilled and edited; accept a single name or full name |
| Phone number | Required; country calling-code selector plus telephone input; allow paste and familiar separators |
| Continue | Demonstrate required-field styling if blank; proceed to the sample Dashboard; store nothing |

Keep this a single short screen. The calling code is part of the phone input, not another onboarding step. “Only name” in the initial description is superseded by the explicit compulsory phone requirement.

Validation appearance: show required-field errors beside Name and Phone, preserving the sample input and focusing the first empty field. Name accepts a single name or full name. The country code and phone layout should look realistic; no phone-validation library, verification service or production validation rules are needed for this preview.

Phone verification by SMS is **not specified**. The proposed minimum collects the required phone but does not label it verified or invent an OTP screen. Purpose of collection and whether verification is necessary remain product decisions. Required phone collection does not itself imply consent to marketing messages.

Greeting uses a short display form of the entered name where reliable; fall back to the full entered name. No additional required “preferred name.” Let the student edit Name in Settings. Proposed local greeting periods: morning 05:00–11:59, afternoon 12:00–17:59, evening otherwise.

### 5.3 First visit versus populated demonstration

The requested Physics, Mathematics and Chemistry cards describe the populated Dashboard. **Proposed demo state:** these three are already enrolled, visibly labelled AS for the sample. **Proposed real new-account state:** no subjects are silently enrolled; show Add your first subject and empty charts. This avoids assuming everyone takes all three. Confirm if automatic enrolment was intended.

Do not add a subject-selection step to mandatory onboarding. A returning account goes to All subjects, with a clear Continue action where there is saved work.

## 6. Global Dashboard and adding subjects

### 6.1 Desktop composition

1. Greeting: “Good afternoon, Abdullah.” Small subtitle: “Your learning overview.”
2. “Your subjects” with Add subject aligned right; horizontal cards for Physics, Mathematics, Chemistry and any additions.
3. Optional compact Continue strip in the returning-learner sample scenario; identify subject, level, lesson/session and position.
4. Four overall analytics cards in a 2×2 grid. All combine enrolled subjects; no topic is selected.

Subject card: subject name, level badge and concise study progress. Entire card opens its subject dashboard; management actions are in a labelled overflow menu, not an extra competing button. Do not place a fake progress percentage on a new course. A new card says “Not started.”

Add subject stays visible independently of horizontal scrolling. At normal desktop sizes show the three requested cards in a row; additional cards wrap or use an explicit scroll control. Mobile uses a labelled horizontal list with partial next-card visibility and non-swipe access. Avoid compressing seven cards into unreadable tiles.

### 6.2 Add subject flow

Use one dialog on desktop, a sheet/full-screen step on mobile:

1. **Choose subject:** Physics, Chemistry, Mathematics, Biology, Accounting, Business, Economics. Seven choices need no search box. Do not retain Computer Science from the current sample modal.
2. **Choose level:** AS level or A2 level. Show the selected subject above. Neither level is selected silently for a fresh addition.
3. **Confirm:** Primary button “Add Biology · AS.” A separate review page is unnecessary.
4. **Success:** From Dashboard, close, append the sample card, focus/briefly highlight it and announce “Biology · AS added.” From Settings, return to its Subjects list; from the subject selector, return to the previous screen with the new scope in that selector. A quiet “Open Biology · AS” action permits deliberate navigation. Adding never switches the current subject unexpectedly.

Back from level returns to the seven subjects with the current selection preserved. Close/cancel returns to the exact caller, not always Dashboard. Double-clicking Add adds one sample card during this visit. An optional error scenario leaves the chosen subject/level visible with Retry, which simply switches to the success appearance.

Sample subject identity is subject + level. If already added, display “Added” and offer Open; do not create duplicate cards. Adding A2 when AS exists attaches a second visible level choice to the same subject card. The card displays its currently selected level; clicking the main card opens that level's dashboard. Separate AS/A2 pills change that choice without opening the card, with the last choice remembered only during the visit. Selector rows always say Subject · Level. Never open an implicit AS+A2 union or nest the level button inside the card's button.

A published subject can be selected even if portions of its course are unavailable, but the card must honestly describe availability. Do not treat the mere presence of a syllabus as a fully authored course. Preview-only fixtures are labelled as such.

### 6.3 Four overall graphs

| Card | Visible summary | On hover/focus/tap | On open |
| --- | --- | --- | --- |
| Consistency | Active-day heatmap and current streak | Date, active minutes, completed learning actions | Overall Analytics → Consistency, same period |
| Practice activity | Weekly bars; unique questions attempted | Day/week breakdown and attempt count | Overall Analytics → Activity |
| Performance | Trend of first scored attempts; evidence count | Score, date, coverage and supported/self-marked status | Overall Analytics → Performance |
| Study progress | Completed lessons across enrolled courses | Notes/practice breakdown and subject contribution | Overall Analytics → Study progress |

No topic-specific mastery card on this screen. A small common period selector defaults to Last 28 days; Current streak remains explicitly current, independent of chart period. Details expose alternative periods instead of four independent filter rows. Chart opening preserves period and scroll position on return.

## 7. Subject Dashboard

Header and selector identify “Mathematics · AS.” Repeat the friendly greeting without extra motivational banners. Display a compact calendar beside the greeting on wide screens; stack it below the Continue card on mobile if space is limited.

Primary content is Continue learning: specific module/lesson plus “Notes · section 3” or “Questions · 7 of 20.” If nothing has started, show “Start studying” leading to the first available module. A separate quiet “Recent activity” expansion can expose other saved sessions; the student should not see three competing Continue buttons.

Use the same four graphs as the global dashboard, filtered to this subject and level. This creates familiarity and replaces the current collection of specialist diagnostic chart labels. Deeper topic strengths, marks and pacing belong in Analytics.

Calendar default is sample study activity for this subject. Show one illustrative next exam or due exercise beneath it. Mark example dates as sample dates in preview context; do not claim they are an official timetable. With no configured exam, show Add exam date. Selecting a day opens its sample activity list, including a No activity state. Selecting a due exercise opens its detail. Selecting an exam opens a compact exam detail popover: subject/level, paper, date/time and sample confirmed/personal-target label. Edit date opens Settings → Exams & dates; Back returns to the same calendar month/day. No timetable connection is needed.

The global streak is across all subjects. A subject streak, if shown, must say “Biology streak”; do not mix it with the global streak. Prefer one streak badge in the header and a clearly scoped calendar to avoid competing numbers.

## 8. Study: module, lesson, notes and questions

### 8.1 Study overview

Show the subject’s published modules in authored order, with topic group headings if required by its curriculum. Do not impose an extra topic-selection screen just because the storage hierarchy contains topics. Mathematics component groupings and Biology topic/module groupings can differ while using the same card pattern.

Each module shows title, available lesson count, completed lesson count and one progress bar. Continue opens its most recent unfinished lesson; the card opens the lesson list. Expose one optional search field only when the list is long. Default order is curriculum order; advanced sorting is unnecessary.

No invented prerequisites or mandatory lesson locks. Show “Coming soon” only for genuinely planned unpublished material, visually separate from available lesson counts. Missing content is “Unavailable,” with a return path, not falsely 0% complete.

### 8.2 Module lesson list

Top: breadcrumb, module title, “3 of 8 lessons complete,” one progress bar. Rows show lesson number/title, Notes status and Questions status. Use a small status marker with text rather than multiple brightly coloured badges.

Click lesson title to open the lesson workspace at the most recent tab; first visit opens Notes. Direct Notes and Questions links may appear as two quiet row actions on desktop, but both lead to the same workspace. On mobile use one row action plus the two tabs inside. Preserve list scroll and expanded module state on return.

### 8.3 Lesson workspace

Persistent header: “Back to lessons,” lesson title and module context. Two tabs: **Notes** and **Questions · 20** when the published pack actually has 20 complete question items. Display actual counts otherwise, with internal content readiness flagged outside the student flow. Do not fabricate missing questions to make the label 20.

First Notes visit renders the released HTML notes. Questions tab shows concise progress and Start/Continue questions; a saved attempt reopens at its exact item. Switching tabs saves the current position and draft. Students may practise first and return to notes later; no artificial read-before-practice gate.

### 8.4 HTML notes reader

- Content is the primary surface: comfortable line length, readable headings, contextual diagrams, tables and equations. Preserve the lesson’s authored sequence.
- A collapsed Contents control jumps between sections without adding a permanent third column. On small screens it opens a sheet.
- Remember the section anchor/reading position while switching tabs in the current preview visit. No reading telemetry or refresh restoration is required.
- Images can expand; closing restores reading position. Wide tables scroll within their container. Broken media offers Retry while readable content remains accessible.
- At the end: **Mark notes complete**. After success: “Notes complete” with Undo and primary **Start questions** or **Continue questions**.
- Scroll-to-end alone never marks completion. No minimum dwell-time quiz or forced delay. For keyboard/screen-reader users, the end action is available in document order without pixel-dependent gating.
- Reopening notes during the visit can preserve its local check. “Mark incomplete” is in a quiet menu and toggles that sample state back.
- A Notes updated badge can be an optional visual example; no content-version tracking is required.
- An optional loading/error scenario demonstrates unavailable notes and Retry. Mark complete switches the visible example directly; no save request, durable acknowledgement or write is involved.

### 8.5 Lesson questions

Question previews open the shared player with a fixed lesson-labelled example list. Demonstrate Previous, Next, Skip, question grid, answer selection, support panels and source-aware exit. A selected result scenario returns to the lesson workspace's matching sample completion appearance. No real pack selection, answer storage or progress roll-up is needed.

Completing questions does not automatically mark notes complete. Reading notes does not mark questions attempted. A learner who finishes both sees “Lesson complete,” Next lesson as the main action, and Review mistakes as a secondary action if relevant. At the module end, the main action becomes Back to module or Next module, whichever is available.

In the finished-pack scenario, Review answers opens a read-only example response set; Practise again opens the editable example player. This demonstrates two different appearances without recording attempts. Read-only has a clear label, Previous/Next/grid and Back to results; it has no Check, Submit or Finish action.

## 9. Completion and progress rules — proposed, not implemented

**Design rationale only:** use these examples to choose understandable labels and consistent sample percentages. Do not build the calculations, events, denominators, storage or cross-feature updates described by an eventual product. The preview can show In progress and Complete by selecting fixtures; actions do not need to change global charts.

### 9.1 Three separate concepts

| Concept | Meaning | Must not mean |
| --- | --- | --- |
| Study completion | Required lesson activities have been completed | Student has mastered the subject |
| Performance | Scored evidence from attempted questions | Time spent or pages opened |
| Activity | Meaningful learning activity over time | A score or proof of understanding |

### 9.2 Notes, questions and lessons

For a standard lesson with required notes and a 20-question pack:

- Notes state: Not started → Reading → Complete by explicit action. Completion is a boolean for that content version, not a reading percentage.
- Question state per item: Unseen, Draft, Skipped, Submitted; scoring state is separate: Unmarked, Correct, Partially correct or Incorrect.
- A qualifying attempted item has a submitted answer or an explicit “I attempted this” acknowledgement for on-paper work. Empty draft, mere visit, Skip and opening the scheme do not qualify.
- Questions coverage = distinct qualifying attempted items / required published items. Repeated attempts do not inflate coverage.
- Structured questions remain whole items. Display part-level progress inside the item. An item is complete for coverage only when all required parts are answered or acknowledged as attempted; an explicit “Could not answer” can end the session but is still an unattempted part.
- Lesson complete = notes complete AND questions coverage 100%. Correctness is not a gate. An honest wrong attempt counts toward coverage but lowers performance if marked.
- A finished session with skipped questions is “Session finished · 17/20 attempted”; lesson practice remains incomplete. Offer Continue remaining 3.

For optional or legitimately absent lesson components, the published lesson manifest must define the required activities. Never infer “notes-only” from a missing question file. A pack missing required material is a content-readiness issue, not grounds to award completion.

### 9.3 Roll-up mathematics and display

Default Study progress = completed required lessons / available required lessons in the selected published course version. Module progress uses that module’s lesson counts; subject progress uses all its required lessons. Topic progress, when displayed, aggregates its lessons, not rounded module percentages.

Do not assign arbitrary 50% weight to notes and 50% to practice. A lesson with complete notes and 10/20 attempts is “In progress,” with those two facts visible. It is not “75% mastered.” The module percentage only advances when another whole lesson completes, while the row shows intermediate activity.

Overall progress pools completed and required lessons across enrolled subject/level scopes. Example: Biology 3/10 and Mathematics 1/2 gives 4/12 = 33%, not the average of 30% and 50%. Detail also shows per-subject bars so the larger course does not hide the smaller course.

Round for display once at the final aggregate. If incomplete progress rounds to 100%, show “<100%” or cap the displayed whole number at 99%; reserve the completion tick and 100% for exact completion. A zero denominator shows “No lessons available,” not 0% or 100%.

### 9.4 Concrete examples

| Student activity | Notes | Questions | Lesson result |
| --- | --- | --- | --- |
| Opens notes, scrolls to end, leaves | Reading | 0/20 | In progress |
| Explicitly marks notes complete | Complete | 0/20 | In progress |
| Attempts 16; skips 4; ends session | Complete | 16/20 | In progress; Continue remaining 4 |
| Attempts all 20; 11 correct | Complete | 20/20 | Complete; performance remains 55% if all are equally scored MCQs |
| Attempts all 20 before reading | Not started | 20/20 | In progress; Read notes |
| Repeats the same 5 questions twice | Complete | 5/20 unique | In progress |
| Submits theory answers, marks later | Complete | 20/20 | Complete; score pending |
| Reads all schemes in Revise mode | Unchanged | No new coverage | Revision reading recorded separately |

### 9.5 Scope, versions and consistency

Sample completion is independent across Study, Revision and Games. Do not build identity matching or cross-credit. A game star must not be labelled as a completed Study lesson. Any eventual product policy linking those concepts is deferred.

For add/remove-subject visualization, show and hide cards only in memory. Existing-progress and new-subject appearances can be separate fixtures. No historical activity, recalculation or enrolment restoration is needed.

Course updates, historical denominators and AS/A2 cross-credit are deferred product questions. An optional “2 new lessons added” badge may be visualized independently; do not implement those systems.

## 10. Revision hub and Topical setup

### 10.1 Hub

Three equal cards: **Topical**, **Yearly**, **Games**, each with one short description and whole-card navigation. Current subject/level remains visible. No mode dropdown on the hub and no fourth “Games” option buried inside Topical mode selection.

### 10.2 Topical: select scope first

Show topics as compact selectable cards, collapsed by default. Checkbox selects the whole topic; a separate disclosure opens lesson selection. Clicking disclosure never changes selection. Partial selection uses an indeterminate checkbox and “3 lessons selected.”

Select one topic for focused work, or several for a combined session. No “Combine topics?” toggle: selecting multiple topics already expresses that intent. Search appears as a single field when needed. “All topics” selects the full current scope; when search is active, label any bulk control explicitly as “Select visible topics” so its effect is not ambiguous.

Selection survives search, collapsing and Back from setup. A compact sticky summary shows “2 topics · 8 lessons” and Continue. Clear selection is secondary. Do not start a session when nothing is selected.

### 10.3 Topical: compact session configuration

Show only three decisions initially:

| Primary choice | Suggested default | Details |
| --- | --- | --- |
| Paper/question type | One available type appropriate to the scope | Descriptive label plus component, e.g. “MCQs · P1”; allow multiple supported components |
| Mode | Practice | Practice, Exam, Revise; one sentence explaining each |
| Length | 10 questions where available | Compact presets 10/20/All; custom count under More options |

“More options” contains difficulty, unattempted-only and ordering. Show a small “2 customised” indication if hidden choices differ from defaults. Reopening retains them; Reset restores sensible defaults for this scope. Do not introduce duplicate “Test,” “Test run,” “Exam simulation” and “Exam” modes with unclear distinctions. Timed practice can be an optional Practice setting only if later retained; it is not a required fourth mode.

No universal component assumptions: Mathematics P1 is not labelled MCQs because Physics P1 is. Read labels and supported types from the subject’s verified catalogue. If a requested practical component cannot be meaningfully attempted in this player, show why it is unavailable rather than presenting an empty runnable session.

### 10.4 Session assembly and edge cases

Summary before Start: subject/level, topics, components, mode, question count, and time limit if applicable. Difficulty/order details are collapsed unless customised. Counts use unique eligible question packages, not the sum of overlapping lesson counts.

Keep whole structured questions and required contextual dependencies intact. If several selected lessons map to one question, include it once. Mixed-topic order groups by topic by default; Shuffle under More options shuffles whole dependency groups, not disconnected subparts.

If only 7 eligible questions exist, show “7 available” and offer Start 7 instead of silently repeating questions or claiming 10. If zero exist, keep selection and explain which restriction can be relaxed. Missing difficulty metadata is “Unclassified”; do not randomly assign Easy/Medium/Hard. New-only excludes prior qualifying attempts, not read-through visits.

For mixed-topic Exam visualization, show a labelled example practice limit. It is not an official paper duration. A selector may switch its displayed value; no timer engine or metadata service is required.

Back from setup restores topics. Exiting the player returns to this setup with selections retained. Results offer Review this session and Practise again; changing topics returns to selection without silently replacing an unfinished run.

## 11. Yearly papers

Flow: Year → exam session → component/variant → mode → player. Use existing supported paper inventory; do not fabricate missing years or variants.

- Year cards are simple and ordered consistently. Retain the last selected year per scope.
- Show one session at a time, named in full: February/March, May/June, October/November where available.
- Paper rows show descriptive component, variant and paper code, with meaningful New / In progress / Attempted status. “Attempted” does not imply passed or fully scored.
- Component filter is one optional control. A paper list should not require students to decode P1/P2/P3 alone.
- A selected paper opens a concise detail/setup screen: paper identity, complete question count, verified duration if known, the three modes and the latest attempt summary.
- Keep previous attempts collapsed behind “Previous attempts.” Each attempt can reopen its answers; it cannot overwrite another attempt’s result.
- An unfinished Practice paper shows Continue prominently and Start new as secondary. An unfinished Exam shows its actual remaining/expired state.

Practice and Exam show the existing five-second cancellable countdown appearance; a short local animation is sufficient. Revise opens directly. Preserve the source ordering/context of the few example questions used. Display a clearly illustrative exam duration, or an Exam timing unavailable sample state. No full paper loading, verified-duration integration or deadline enforcement is required.

Results Back returns to the paper detail with its updated status. Back again returns to the same year/session/component and scroll position. Direct links to a missing paper show a scoped unavailable state, with Back to yearly papers.

## 12. Games and reuse of the existing path

Games opens the existing Duolingo-style topic path within the current subject shell. It must not open another app with an unrelated sidebar or silently switch every subject to the populated Physics lesson.

Reuse topic banners, compact topic shortcuts, path nodes, node preview, progress feedback, subtle topic atmosphere and matching/ordering/choice renderers. Bring them under the current Manrope/plum/teal theme and shared navigation. Preserve current prototype storage during later integration; do not overwrite it during exploration.

### 12.1 Path interaction

- Open at the last visited/current available node; offer a quiet “Back to current” control after exploring elsewhere.
- Nodes distinguish Available, In progress, Complete and Unavailable with shape/icon and text, not colour alone.
- A node preview shows topic/lesson title, actual available game type/tier, approximate length only if supported, and Start/Continue.
- Difficulty tiers can be available choices without invented prerequisite locks. Unpopulated nodes explain “Games for this lesson are not available yet.”
- Close during a game returns to the same path position with that node preview reopened. Close node preview returns to the path; Back from path returns to Revision. Finishing shows the sample result, then Continue path closes the result and highlights the same node. A separate next-node action is optional and explicitly labelled. No saved-run integration is required.
- No mandatory leaderboard, currency store, hearts or punitive streak mechanics. Existing fictional leaderboard and gems stay outside core student metrics unless separately approved.

### 12.2 One player, different question interaction

The brief requests both the existing Games experience and exactly the same question player everywhere. **Proposed reconciliation:** one player shell, queue/navigation/save/exit model and results pattern; game items use their matching, ordering or choice input renderer inside it. The game path remains distinct; it does not fork a second player with different Back/Review semantics.

Default game feedback may be faster and more animated, but Previous, position, accessibility settings and session exit stay recognisable. Automatic advance is a Games preference, never imposed on theory answers or read-through. Linked explanations wait for Next when needed. Provide a non-automatic option for readers and reduced motion.

Incorrect game items may enter a retry queue. Distinguish “12/20 covered” from “Retry 2 of 3”; the denominator of original unique items does not grow on every retry. Game completion, retries and stars do not become Study completion or exam marks. Game performance is shown separately from comparable first-attempt paper scores.

**Decision still required:** whether “exact same” also requires the same split-screen arrangement in Games at all times. Proposed answer: yes for the shell and available support panel, with the support panel collapsed during fast game interactions. Do not silently retain the current independent full-screen game player in the final design.

## 13. Shared question player

### 13.1 Session contract from a student's perspective

Every preview launch needs subject/level, a source label, a fixed ordered example list, current position, mode and a return destination held in memory. Distinguish **content source** (for example a Yearly paper) from **launch origin** (for example an Analytics chart). Close returns to launch origin with its scope/filter/scroll, not automatically to that paper's library. No attempt records, support-use logging or persistence are required.

| Entry | Queue | Initial position | Exit destination |
| --- | --- | --- | --- |
| Study lesson | That lesson's required pack | Saved item or first unseen | Same lesson Questions tab |
| Topical | Frozen unique matching packages | First item or saved item | Same session setup |
| Yearly | That full paper in original order | First item or saved item | Selected paper detail |
| Review | Frozen visible filtered review list | Clicked question | Same Review filter/tab/list position |
| Exercise | Published exercise version | Saved item or first | Exercise detail/result |
| Games | Selected node/tier queue and retry policy | Saved item or first | Same game node/path position |
| Results → Review answers | Read-only example responses for that result | Chosen item or first | Exact results screen |
| Analytics → sample attempt | Read-only example responses behind selected chart point | Chosen item or first | Same metric, scope, period and chart position |
| Tracker → Continue lesson | Lesson fixture shown by that tracker row | Sample notes anchor or question | Same tracker row, with lesson Back labelled Back to tracker |
| Calendar → sample activity | Lesson or read-only response fixture for selected day | Sample position | Same calendar month/day detail |

The example queue stays fixed while it is open. Withdrawn/corrected-item screens are optional standalone visual scenarios. No content-version records or live updates are needed. Source metadata is for the small example only.

### 13.2 Desktop composition

Use a large player window over the source page, effectively filling the available workspace. Avoid a narrow modal for 20 long questions. Preserve source behind it, but prevent background focus and accidental scrolling.

- **Top bar:** source label, subject/level, question position (“4 of 20”), small save status, timer only when relevant, and labelled Close/Back to source.
- **Left panel:** selectable question text, mathematical rendering, diagrams and full shared stem. Show question number, part labels and marks without burying the prompt in metadata.
- **Right panel:** Answer support with Mark scheme, Hints and Walkthrough tabs when allowed. For a selected part, show that part’s scheme; retain the shared stem and related figures on the left.
- **Answer area:** appropriate input alongside/below the question. MCQ choices, structured response, on-paper acknowledgement/self-marking or game-specific input. Do not present a text box for every question type by default.
- **Bottom bar:** Previous, question-grid control, Skip/Next and the main contextual action. Finish session remains available through a clear secondary control; the final item promotes it.

Scheme content is preserved faithfully, including marking points and criteria. Hide editorial repair controls, canonical issue counts and Pass/Flag review decisions. Student “Save to Review” is separate from reporting a content issue.

### 13.3 Modes and support disclosure

| Behaviour | Practice | Exam | Revise | Games |
| --- | --- | --- | --- | --- |
| Submit answers | Yes | Yes, final assessment at end | No; read-through | According to game input |
| Mark scheme | Reveal on request; mark attempt as supported after reveal | Unavailable until submission/expiry | Available immediately | Shared panel where applicable; feedback rules by item |
| Hints/walkthrough | Available if authored; collapsed initially | Unavailable during run | Available if authored | Brief support where authored |
| Marking | Check MCQ; self-mark theory where supported | After submission; theory may remain pending | No score | Separate game result |
| Timing | Optional elapsed time; pause allowed | Countdown against fixed deadline; no pause | None required | Active play time; pause allowed |
| Progress effect | Coverage for its source | Coverage and scored evidence where valid | Reading history only | Game progress/activity |

All modes use the same controls and structure, but unavailable support does not occupy a misleading clickable tab. In Exam, use the right area for neutral session information or expand the question panel; never leak a scheme through a hidden tab, tooltip or restored state. Changing mode requires a new session, not a way to reveal answers mid-exam and keep an exam score.

### 13.4 Answers, marking and movement

MCQ selection is reversible until Check/Submit in Practice. Show text/icon feedback, not colour alone. Once checked, preserve that attempt; Try again is a new response event rather than overwriting the first answer. In Exam, choices remain editable until final submission and reveal no correctness while navigating.

Theory answer entry is optional in the design. Show an Answer and working area, a Work on paper choice and a simple self-mark appearance where useful. The inspected editor offers Correct/Partial/Incorrect/Confused, not numerical mark allocation. Use those labels for this preview; a numeric scoring system is unnecessary. Sample numerical results can be separate fixtures labelled Self-marked or Example result. Do not equate Confused with a numeric mark or promise automatic grading.

Previous/Next saves drafts. Next moves without claiming completion. Skip moves forward and marks the item Skipped; it remains in the question grid. At the end, show unanswered/skipped count with a direct Return to unanswered action. The grid uses symbols/text for Unseen, Draft, Submitted and Skipped; correctness is shown only when mode permits.

Long shared stems remain attached to all relevant parts. Jumping to (c) shows the necessary context, including results from earlier parts where provided by the source. Selecting a question scrolls to its heading; switching support tabs does not reset question scroll.

Save to Review is available for the current question with a quiet bookmark control. Default reason is “Revisit”; optional reason selection follows without blocking answer flow. Additional reasons can include Difficult, Mistake and Unsure. Duplicate saves update the existing active item, not create duplicate cards.

### 13.5 Finish, leave and resume

Normal preview exit returns directly to the launch origin, remembering position only within this visit. Do not demand a save confirmation. A deliberately selected Leave example can show the intended dialog for review; it must not call any storage or service. Resume opens a fixed in-progress fixture or the current in-memory position.

Finish opens a compact summary if unanswered questions remain: “17 attempted · 3 unanswered,” Return to unanswered or Finish anyway. Finishing does not turn skipped items into Study completion. Repeated finish clicks create one submitted result.

Exam start, running, early-submit confirmation and Time is up are selectable visual states. A local timer may animate briefly to demonstrate appearance; Preview controls can jump directly to expiry/results. Nothing must continue after closing or reload. Do not submit answers, record deadlines or implement exam enforcement.

Pause can change the timer's visible state. Study time is fixed sample data, never instrumented activity. Authentication expiry, reconnect/recovery and background timer handling are outside this preview.

### 13.6 Results and next action

Show completion status, attempted/total, available score with marking coverage, and time when meaningful. Keep a single primary next step based on source. A question breakdown is collapsed initially, with “Review answers” always discoverable.

- Study: Continue remaining questions; otherwise complete notes or Next lesson.
- Topical: Review session; secondary Adjust session or Practise again.
- Yearly: Review answers; secondary Back to paper.
- Review: Continue remaining review items or Back to review.
- Exercise: Submission confirmation/result; Back to exercises.
- Games: Continue path; show retries/unique completion separately from exam-style score.

Never show confetti for a failed save, 0/20 attempts, or an unscored response as though it were a high score.

### 13.7 Past-paper question player: what to reuse visually

Inspected source: [player page](past-paper-question-reviewer/app/page.tsx) and [answer editor](past-paper-question-reviewer/components/player/AnswerEditor.tsx). This is a code/layout inspection, not a claim of a new live browser test. The existing tool is an editorial reviewer as well as a question display; copying the entire page would bring unwanted navigation and recording behaviour into the student mockup.

| Existing element | Decision for this visualization |
| --- | --- |
| Wide question left, support right; approximately 62/38 desktop split | Reuse the layout with current dashboard colours and consistent typography |
| Selectable question text, mathematical rendering, figures and part labels | Reuse representative display examples; keep shared stem and contextual figures visible |
| P1 question image with extracted-text toggle | Make text-first the student default where an existing usable text sample is available; preserve diagrams; do not rebuild/OCR the corpus |
| Mark Scheme / Hints / Walkthrough tabs | Reuse appearance with fixed examples; label selected part clearly; keep support hidden in the Exam-running appearance |
| Per-part scheme/hint/walkthrough shortcuts | Keep a quiet selected-part action; do not show three competing buttons under every part plus repeated full toolbars |
| Previous/Next and position | Reuse, add grid/Skip/Finish or read-only Close as appropriate; operate only on the current fixture queue |
| Paper selector, Papers breadcrumb, Browse papers button | Omit from shared player; they could replace a Study or ten-question Review list. Use Back to the actual launch origin |
| Pass question / Flag for correction / review-note box / pasted screenshot attachment | Omit completely; these are editorial repair controls, not student Review |
| Saved to review file, issue counts, raw question IDs, source paths | Omit from the student surface; a quiet human-readable paper/lesson source label is enough |
| `/api/reviews`, `/api/review-images`, answer/self-mark localStorage, file persistence | Do not copy or call. Use isolated fixed examples and temporary UI state only |
| Correct / Partial / Incorrect / Confused self-mark menu | Optional appearance only; selecting changes a chip, not a score/history record. Confused may suggest Revisit visually |
| Chemistry Symbols toolbar inside the inspected Physics editor | Do not carry over universally. Keep Tools collapsed; use a relevant subject example or omit it |
| Official Scan tab with question, compact-paper and mark-scheme PDFs | Outside the initial minimal student player; optional Source preview can be a separate sample surface later. Do not expose a scheme PDF in the Exam-running appearance |
| Focus mode and Open support | Keep as one clearly labelled collapse/reopen support action; on mobile use Question/Support tabs |

The visual demonstration needs an MCQ example, a multipart theory example with a diagram, a read-only answer example and a game-input example. Each should have a matching support/empty-support state. The same renderer appearance can be reused across the source fixtures; this does not require a shared backend, real paper loading or a complete scoring engine.

Question-only/focus view must always expose Show support, so it cannot become a dead end. Closing diagram zoom returns to the same part. When a part has no hints or scheme, show a short unavailable-support example rather than another part's content. The student Review bookmark uses Revisit/Resolved language; it never invokes editorial Pass/Flag.

## 14. Review: a queue, not isolated popups

Keep the current minimal card/list styling: topic first, short source/lesson context, optional reason tags, Open question. Active/Resolved at top; one Reasons dropdown. No question excerpt or thumbnail required in every row.

Review is scoped to subject and level. A top-level “Review all 10” starts at item 1; opening item 4 also launches the same 10-item queue at position 4. Students can move Previous/Next or use the grid without closing the window. At the last item, offer Go to remaining earlier items when some have not been visited; do not silently loop or call the queue complete.

Filters determine the queue at launch. Example: ten Active questions, Reasons = Difficult gives six; clicking a row opens “2 of 6,” not a hidden all-subject list. Text above the list says “6 matching questions.” Membership/order stay stable until exit, even when an item is resolved.

Resolve toggles a local sample state, leaving the item in the open queue with a Resolved indicator and Undo. It can disappear from the current in-memory Active list on return. Restoring reverses that local toggle. No writing, automatic grading or mistake collection is involved. Keep Resolve/Undo available in the player header or support area, so students need not exit to use it.

Specify two Review fixtures: a question with an example previous answer opens read-only, labelled Previous answer; a bookmarked but unanswered question opens the editable Practice appearance. Try again switches the current item to the editable appearance inside the same fixed queue. Other items keep their example states. At the end, show a sample “4 resolved · 6 still active,” not a mastery score. No previous answers are actually retrieved and no reattempt events are written.

No items: “Nothing saved for review yet,” with Go to Study/Revision. No filtered items: offer Clear reasons, not an unrelated empty-state tutorial. If a question becomes unavailable, preserve the saved reference and reason; explain unavailable, allow return/resolve, and do not substitute another question.

## 15. Exercises — minimum useful design

Exercises are published sets, not a second Study syllabus. Show simple module-like cards: title, subject/level, question count, due date when present, and state. Default list includes current/upcoming work; Completed is one secondary view.

States: Not started, In progress, Submitted, Awaiting marking, Completed, and Overdue as a due-date modifier. An overdue exercise can still be In progress; do not encode both concepts as mutually exclusive statuses.

Detail page shows short instructions, timer/due-date rules, and Start/Continue. A timer is attempt duration; a due date is a calendar deadline. Display both distinctly if both exist. A timed exercise with an approaching due date explains the effective end condition before Start.

Publisher metadata decides support access, repeat attempts and late submission. Proposed default for ordinary practice exercises: save/continue, mark scheme after submission, late work allowed and labelled late. A stricter setting must be stated explicitly before starting; do not invent punitive rules. With missing rules, do not silently lock students out.

Use the same question player and a fixed Submitted/result appearance. Submitted, Late and Awaiting marking are selectable sample states, not real submissions or evaluated deadlines. An empty Exercises screen says “No exercises published yet.” No publisher, marking or submission connection is needed.

Teacher/admin publishing UI, grading workflow, assignment distribution and notifications are outside this student navigation specification. Only their student-visible effects are described.

## 16. Analytics and the progress tracker

One Analytics workspace per scope, with three internal tabs: **Overview**, **Study**, **Performance**. The progress tracker sits in Study rather than becoming a sixth sidebar item. “AILD” remains an unresolved internal phrase; do not place it in UI copy.

### 16.1 Overview

Start with the same four dashboard cards, now expandable. One period selector; scope is inherited. Detail routes open the selected metric directly and provide Back to overview or Back to dashboard according to origin.

Show a modest evidence summary (“18 scored questions”) beside performance. Avoid predictive grades, opaque readiness scores and excessive decimal precision until a separate validated model exists. Sparse data says “Not enough scored work for a trend” and still shows available individual results.

### 16.2 Study tracker

Tree/list: subject level → topic where needed → module → lesson. Default shows modules collapsed, counts and completion bars. Expand to see Notes complete, Questions attempted/required, latest study date and a direct Continue link. Provide one optional “In progress” filter, with detailed filters collapsed.

The tracker shows unfinished work separately from areas with low scored performance. A not-started lesson is not a weak point. Where sufficient evidence exists, show “Needs practice” with a count and a direct Start topical session link prefilled to that topic. Do not diagnose a whole module from one wrong question.

### 16.3 Performance details

Allow inspection by topic and by paper, with Practice/Exam separation and scored coverage. Show first attempts and latest attempts as distinct views rather than blending repeats into improvement. Clicking a point opens the original session/attempt; returning preserves metric, period and scroll.

In this preview those points open fixed read-only answer examples. Global → Biology · AS detail visibly changes the subject/level selector and breadcrumb; Back restores the original global metric/period, then Dashboard. From a global tracker, Continue on a lesson first activates that row's subject/level and retains Back to tracker. Calendar activity uses the same launch-origin rule. Content source never overrides this return chain.

Use comparable scoring groups. MCQ accuracy, theory marks and game retry success are different measures. A minimal overall first-attempt performance card may combine scored marks only with a visible “Scored work” label and details disclosing the mix, support use and self-marking. Game gems, notes completion and time never enter that score.

### 16.4 Metric definitions

**Reference for sample labels only.** These formulas describe possible future meaning and keep example screens understandable. Do not implement collection, timestamps, counting, scoring, inactivity measurement, timezone bucketing or analytics calculations. Choose fixed values and chart points.

| Metric | Proposed calculation | Edge handling |
| --- | --- | --- |
| Unique questions attempted | Distinct stable question IDs with qualifying attempt in period and scope | Repeats visible in detail; read-through and skips excluded |
| Scored performance | Sum awarded marks / sum available marks for the scored eligible items | Unmarked excluded, with coverage displayed; no average of rounded percentages |
| First-attempt trend | First qualifying attempt per question within chosen comparison policy; timestamped by actual attempt | Later repeats do not become new first attempts because period changed; support status retained |
| Current streak | Consecutive local calendar days with qualifying activity, allowing today to remain unfinished while yesterday's streak is current | Login, refresh and idle timer do not qualify; never negative |
| Qualifying active day | At least one meaningful submitted attempt, explicit notes completion, or at least 2 minutes active notes engagement | Two-minute threshold is a proposal; scrolling alone is not notes completion |
| Active study time | Foreground, non-idle learning intervals; proposed idle cutoff 5 minutes | No double-counted overlapping tabs; exam deadline time is separate |
| Study completion | Completed required lessons / available required lessons for selected course version | Required activities and denominator policy in section 9 |
| Review remaining | Active unique saved review items in current scope | Resolved items excluded from count but retained in history |

Show a sample timezone control and explicit sample date range. No day bucketing, historical records, timezone migration or daylight-saving logic is needed. The greeting may use the current local time as a tiny display convenience.

For future metric meaning, repeated topic mappings should not inflate a global count, Games should stay separate from paper marks, and unscored theory should not mean wrong. For this preview, simply choose consistent sample values; build no deduplication or aggregation.

### 16.5 Drill-down discipline

One chart card contains one readable headline, one graph and one short descriptor. Hover/focus/tap provides the exact data point; a labelled View details action opens the full analysis. Tooltips never hide the only route to navigation. On touch, tapping a point reveals its value and tapping View details navigates, avoiding conflicting tap meanings.

Details may expose source, subject, period, mode and attempt basis. Keep those controls off the Dashboard. A selected weak topic can prefill Topical configuration but must show its proposed settings before launching questions.

## 17. Settings

Settings remains reachable at the bottom of both sidebar contexts. Open the last settings section or Account on first entry. Back restores the previous app location and scope, not always the global Dashboard.

| Section | Minimum controls |
| --- | --- |
| Account | Name, compulsory phone, Google account/email shown read-only, Sign out |
| Subjects | Enrolled subject/level pairs; Add; remove from active Dashboard while retaining progress |
| Exams & dates | Optional exam series/date configuration when supported; clearly distinguish confirmed dates from personal targets |
| Preferences | Timezone, motion/auto-advance preferences, optional game sound |
| Help | Support entry and relevant existing policy links |

No password-change UI for Google-only authentication. Do not expand sample billing, credits, AI grants or subscription controls without a product requirement. Keep account deletion separate from reversible subject removal; do not implement a deletion flow in this prototype task.

Settings controls change their appearance in memory. Save shows a sample confirmation; Remove/Undo toggles a sample subject card. Sign out navigates to the sign-in appearance. No account updates, logout calls, persistent preferences or draft-saving logic are required. A sample error state can be selected independently for visual inspection.

## 18. Visual system and interaction details

### 18.1 Preserve the current theme

| Role | Inspected current token/value | Use |
| --- | --- | --- |
| Font | Manrope, Inter/system fallback | Shared headings, controls and reading chrome |
| Main ink | `#1d1935` | Readable body text |
| Heading/deep violet | `#272043` | Titles and strong emphasis |
| Primary | `#2bb9b1` | Main action/selection accent |
| Primary dark | `#168f89` | Stronger teal emphasis, subject to contrast validation |
| Canvas/sidebar | `#f7f9fb` / `#f6f8fa` | Calm page background and navigation |
| Border | `#e8eaee` | Card separation |
| Lavender | `#e1e1fb` | Active navigation background |
| Peach/mint | `#f8ead9` / `#e6f5da` | Quiet supporting accents |
| Muted | `#888995` | Secondary metadata where contrast remains sufficient |

These are current palette references, not evidence of accessibility compliance. Preserve their identity but validate actual text/background pairs; use darker text or a deeper same-hue button treatment where needed. Do not keep low-contrast white-on-teal solely to match a screenshot. White cards, soft borders and restrained shadows remain consistent across all screens.

### 18.2 Status language

| State | Treatment |
| --- | --- |
| Not started | Neutral outline, explicit text |
| In progress/selected | Teal accent with subtle mint surface |
| Complete | Check icon and “Complete”; green/teal family |
| Needs review/incorrect | Muted warm/rose accent plus text; no whole-screen red wash |
| Unavailable | Readable muted text and explanation |
| Overdue | Small warm badge with date; no alarm-like full card |

Do not reuse completion green as the only cue for a correct answer. Show the word or icon. Never colour every subject, chart series and filter differently without a purpose. Topic themes are faint background details in Games, not competing interfaces.

### 18.3 Density and microinteractions

Use a stable spacing scale and consistent card padding. Prefer title, one summary line and one action to explanatory paragraphs on the product screen. Selected rows change subtly; avoid moving surrounding content. Save acknowledgements are quiet, errors persistent until handled, and brief success toasts do not steal focus.

Dropdowns close on outside click/Escape; retain selections unless cancelled explicitly. Dialogs have a visible title/close action, constrained scrolling and restored trigger focus. Do not nest dialogs inside dialogs: switch the same surface from question to scheme or from subject choice to level choice.

Tooltips supplement visible labels. Icon-only controls have accessible names. Filter badges describe active constraints when panels are collapsed. Loading preserves card geometry. No decorative animation delays a student's next action; honour reduced motion.

### 18.4 Mobile and accessibility

- Collapse sidebar into a drawer; keep current subject/level in the mobile top bar. Disabled global items retain their explanation.
- Use 44px touch targets as a design target, visible keyboard focus, labelled controls and logical heading order. Validate contrast and keyboard navigation during implementation.
- Stack dashboard graphs; keep Add subject visible without scrolling to the end of the subject strip.
- Notes use a single reading column. Sticky tabs and bottom completion controls must not obscure content at zoom or when the keyboard opens.
- Player becomes full-screen. Use Question / Support tabs rather than squeezing two columns; preserve scroll and current part separately. Timer/position/back stay visible.
- Question grid opens a sheet. Closing restores focus to its trigger; changing question focuses the new prompt. Do not announce the countdown every second to screen readers.
- Diagram zoom supports a visible Close and keyboard exit. Tables/math overflow locally, not across the whole page.
- Charts offer textual summaries and data-table detail. Hover information must also work on focus and touch.
- Games ordering/matching supports selection buttons and keyboard alternatives to dragging. Auto-advance can be disabled; feedback text remains accessible.

## 19. Screen register and return behaviour

| ID | Screen/surface | Main action | Parent/return and preserved state |
| --- | --- | --- | --- |
| O1 | Google sign-in | Continue with Google | Returns here on cancelled sign-in |
| O2 | Profile completion | Continue | Preserve entered Name/Phone on error |
| D1 | Global Dashboard | Open subject / Add subject | Stable global home |
| D2 | Add subject dialog | Choose subject | Exact invoking Dashboard, Settings or selector screen |
| D3 | Add level step | Add subject + level | D2 on Back; invoking screen on add/cancel; explicit Open new subject action |
| S1 | Subject Dashboard | Continue learning | D1 via All subjects |
| S2 | Subject/level switcher | Select scope | New S1; prior browsing remembered |
| ST1 | Study modules | Open module | S1/sidebar, scope retained |
| ST2 | Module lessons | Open lesson | ST1, expanded module/scroll retained |
| ST3 | Lesson Notes | Mark notes complete / Start questions | ST2; notes anchor retained |
| ST4 | Lesson Questions | Start/Continue questions | ST2; same lesson workspace |
| R1 | Revision hub | Topical / Yearly / Games | S1, scope retained |
| R2 | Topical scope | Continue | R1; topic selections retained |
| R3 | Topical setup | Start | R2; filters and scope retained |
| Y1 | Year list | Select year | R1 |
| Y2 | Session/paper list | Select paper | Y1; session/component/scroll retained |
| Y3 | Paper detail/mode | Start/Continue/Open Revise | Y2, selected paper retained |
| G1 | Game path | Open node | R1; path position retained |
| G2 | Game node preview | Start/Continue | G1 on close; player Close reopens G2 at same node |
| V1 | Review list | Review all / Open question | S1; tab/reasons/sort/scroll retained |
| E1 | Exercises list | Open exercise | S1; current/completed state retained |
| E2 | Exercise detail | Start/Continue | E1, list position retained |
| P0 | Countdown | Wait / Cancel | Exact setup; no attempt recorded on cancellation |
| P1 | Shared question player | Check/Next/Submit appearance | Exact launch origin in section 13; content source does not override it |
| P2 | Question grid/support/zoom | Select or inspect | P1; focus/scroll retained |
| P3 | Finish/leave confirmation when needed | Finish / Stay | P1; no silent draft loss |
| P4 | Sample results | Context-appropriate next step | Launch origin retained; Review answers opens P5 and returns here |
| P5 | Read-only answer/history example | Previous/Next/grid; Try again where appropriate | Exact originating result, Review list or Analytics point; no Submit/Finish |
| P6 | Player focus/support or empty-support state | Show support / switch part | Same question, part and scroll position |
| A1 | Analytics overview | Open metric / Study / Performance | Subject Dashboard or global chart origin |
| A2 | Study progress tracker | Expand / Continue lesson | A1; scope/period retained |
| A3 | Performance/metric detail | Open attempt / Practise topic | Originating chart/analytics state |
| C1 | Calendar day detail | Open activity/exercise | S1, calendar month/day retained |
| C2 | Calendar exam detail / empty day | Edit date / Close | Calendar month/day; Settings returns here |
| SE1 | Settings | Save changes | Exact previous screen and scope |
| X1 | Unavailable/error state | Retry / Back to parent | Deterministic scoped parent, never blank app |
| PV1 | Preview controls, outside student frame | Choose sample scenario | Establishes that scenario's known starting screen |
| PV2 | Reset preview | Restore default samples | Populated Dashboard; clears temporary UI selections only |

Normal section navigation is a page, not a modal. Short choices use dialogs/sheets. The player uses a large window/full-screen surface with a restorable route. Detailed analytics is a page. Do not hide whole learning journeys in nested popup stacks.

## 20. Optional empty and error appearances

These are visual examples selected from Preview controls, not failures the app must generate, detect or recover from. Prioritize normal navigation first. No network/offline/auth-expiry/multi-tab conflict machinery is required.

| Example | Appearance and click-through |
| --- | --- |
| No subjects | Add your first subject; global sidebar gating visible |
| No activity | Empty charts with short explanatory text; useful next action |
| Level/content unavailable | Scope stays visible; Back to subject or another available sample |
| Notes/figure loading or error | Skeleton/error card, Retry switches to the example content |
| No matching topical questions | Selection retained, Clear restrictions returns to populated fixture |
| Lesson partly complete | Notes complete plus 17/20 questions appearance; Continue remaining opens a sample remaining item |
| Review empty or filtered empty | Distinguish Nothing saved from No matching items; Clear reasons is available |
| Exam running/ended | Same player layout with timer/status changed; results accessible without waiting |
| Exercise submitted/late | Sample status badge, due-date text and Back to exercise |
| Saving/error confirmation | Optional visual sample only; Retry changes appearance, performs no write |
| Course complete | Completion card with Revision action and no nonexistent Next lesson |
| Calendar day empty | No activity on this day; Close returns to same month |

Do not add every exceptional state to the main student navigation. Keep a small scenario chooser outside the product frame so the reviewer can inspect them deliberately. Persistent sample-data labelling makes clear that an example Saved or Submitted message is not a real stored result.

## 21. Scripted walkthroughs for visual review

These are click-through stories using fixed fixtures and small in-memory UI changes. No story requires real answers, recorded progress, live authentication, exhaustive content or computed analytics.

### Journey A — onboarding and first subject

Preview controls → New learner → Continue with Google (mock) → sample Name/Phone form → demonstrate blank-phone error → sample Dashboard → Add Biology → AS → card appears → Biology Dashboard. Check readable hierarchy, short steps, sidebar gating and clear return paths. Reload may reset the story.

### Journey B — module, notes and question appearance

Biology · AS → Study → module → lesson → existing HTML notes example → Mark notes complete toggles its local check → Questions → sample player. Preview controls can jump to 17/20 attempted or Lesson complete. Show the matching module row in that selected scenario; do not recalculate charts from the click.

### Journey C — review all ten in one window

Review fixture has ten items → open row 4 → 4 of 10 → local Resolve → item remains with Undo → Next → 5 of 10 → grid → item 1 → Close returns to the same list/filter. The queue never unexpectedly shortens. A sample unanswered bookmark demonstrates editable mode; a sample previous answer demonstrates read-only mode.

### Journey D — read-only result and return

Open sample lesson result → Review answers → read-only player labelled Example previous answers → Next/grid work, answer input and Submit do not appear → Back to results → Back to lesson. Try again opens the editable appearance without creating an attempt record.

### Journey E — yearly visual states

Revision → Yearly → year → session → paper → Exam → countdown appearance → Cancel returns to setup. Start opens a running-timer fixture. Preview controls → Exam ended → sample results. No need to wait, score answers or enforce a deadline. Revise opens directly with support available and no submission action.

### Journey F — Games inside the shared navigation

Physics Games → path → representative available node → preview → shared player with game-style input. Close returns to the same node preview on the path; close preview → path; Back → Revision. Sample Finish → result → Continue path highlights the node. Another scenario shows unavailable nodes. No currency, saved game import or progression calculations.

### Journey G — analytics origin and scope

Global chart → overall detail with same sample period → Biology · AS detail visibly changes scope → sample attempt → read-only player → Close restores Biology metric → Back restores global chart detail → Back to Dashboard. Tracker Continue and calendar activity links likewise retain an explicit return origin instead of dropping the learner at a paper library.

### Journey H — contextual add, settings and calendar

Settings → Subjects → Add subject → cancel returns Settings. Repeat → add returns Settings with Open subject option. Scope selector → Add → success returns to prior subject screen, leaving it selected. On a dual-level card, A2 pill updates the displayed choice; the main card opens A2. Calendar exam → detail → Edit date → Settings → Back returns to the same calendar day. No account or date service is called.

### Journey I — mobile navigation

Open subject drawer → Study → lesson notes → Questions full-screen → Support tab → diagram zoom → Close restores Support/current item → grid → another item → Back to lesson → Back to module. Inspect tap targets, keyboard focus, scrolling and text legibility; never squeeze the desktop split into unreadable columns.

## 22. Open decisions and recommended defaults

These do not block visualization. Use sample choices to compare alternatives. Authentication, scoring, tracking, exam-policy and content-version decisions below are future-product questions, not requirements to resolve before showing the mockup.

| Decision | Recommended default | Why it matters |
| --- | --- | --- |
| Name means first or full? | One Name field accepts either; short greeting derived conservatively | Avoid unnecessary onboarding fields |
| Phone verification/purpose | Required collection only; verification and purpose to be confirmed | Do not add an unrequested OTP journey or claim verification |
| Three initial subjects | Demo seeded; real new accounts choose subjects on Dashboard | Avoid accidental enrolment assumptions |
| Both AS and A2 | One subject card, separate explicit levels/progress; no forced migration | Keep Dashboard compact without overwriting history |
| Meaning of AILD | Use Progress until defined | Avoid invented analytics taxonomy |
| “Ailey papers” | Treat as Yearly | Matches existing navigation |
| Games versus exact shared player | Same shell/state/navigation; specialised input renderers and optional faster feedback | Reconciles two explicit requirements |
| Lesson completion | Notes marked complete plus every required question attempted; correctness separate | Makes completion honest and understandable |
| Theory scoring | Explicitly labelled self-marking or pending; no assumed automatic grading | Prevents false performance claims |
| Automatic Review additions | Manual save by default; optional suggested mistakes at results | Avoid surprise queue growth |
| Streak/activity threshold | Meaningful attempt/completion or 2 minutes active reading; 5-minute idle cutoff for time | Needs agreement before metrics are treated as authoritative |
| Exercise policy | Ordinary practice defaults; publisher-defined timer/late/retry rules visible before start | Exercises are not fully specified yet |
| Exam accommodations | Use verified per-user/paper allowance when configured; no guessed adjustments | Prevent conflicting deadlines or durations |
| Course updates and cross-credit | Versioned completion; no inferred Study credit from Games/Revision | Preserve stable authored scope and credible totals |
| Overall chart access with disabled Analytics | Dedicated global detail route from cards | Satisfies both global sidebar gating and chart drill-down |

## 23. Later visual-prototype sequence and acceptance gates

For a future explicit request to edit the prototype. This document update does not begin those edits. The target is a believable navigable mockup, not a connected application.

1. **Shared shell:** subject/level label, global versus subject sidebar, Exercises entry and clear Back/Close behaviour using temporary UI state.
2. **Sample onboarding and subject choices:** visual Google step, example Name/Phone form, seven-subject AS/A2 picker and caller-aware returns.
3. **Study screens:** module list, lessons, existing HTML example, Notes/Questions tabs, incomplete/complete sample appearances.
4. **Common player layout:** representative MCQ and multipart theory question, support tabs, grid, editable/read-only variants, ten-item Review fixture and origin-aware Close.
5. **Revision screens:** minimal Topical selections, Yearly browse/mode/countdown examples, paths to that same player layout. Fixed example counts are enough.
6. **Games appearance:** reuse the existing path/style and a representative input interaction in the shared shell. Do not port its storage or full game engine.
7. **Dashboard/Analytics samples:** four charts, tooltips, matching detail fixtures, tracker and origin-aware return. No computation or event collection.
8. **Exercises/Settings and design review:** sample detail/submitted screens, account/preferences forms, calendar popovers, selected empty/error appearances, responsive navigation checks.

Acceptance is visual and navigational:

- All requested screen families have an inspectable sample; the seven subjects/levels have explicit scope selection, without building fourteen complete courses.
- Core clicks open the right surface; Back/Close returns to the exact caller, including Analytics, Settings, Games node and calendar origins.
- One recognisable player layout supports sample Study, Revision, Review, Exercises and Games contexts; controls respect editable, read-only and Exam appearances.
- No paper-library control replaces a lesson or Review queue; no editorial repair controls or exposed storage paths appear in the student design.
- Selected examples demonstrate partial/complete notes and question states without requiring full attempts or a global progress engine.
- Topical options remain discoverable without five permanent filter rows; graphs reveal details on hover/focus/tap with a visible detail link.
- Current theme is retained; desktop/mobile layouts, keyboard focus, text contrast and touch targets are reviewed at the design level.
- Preview controls make result, empty and error appearances reachable without doing the underlying real-world work.
- Only sample data and in-memory UI state are used. No real Google flow, database/API writes, file writes, browser-storage recording, learner tracking, scoring service, synchronization or authenticated recovery is added.
- Existing prototype data, editorial review decisions, source files and canonical subject material remain unchanged.

Stop when those screens and journeys can be judged for look, feel and clarity. A mockup does not fail because refresh resets it, a score is predetermined, a deadline is illustrative or changing one lesson does not recalculate every graph.

## 24. Design review outcome

The preview should answer: Where am I? What can I do here? What opens next? How do I return? What does an incomplete, complete, editable or read-only state look like?

The original draft over-specified persistence, timing and tracking. Those requirements are removed from the visual-prototype scope. Completion and metric explanations remain only as design rationale for example labels. The main deliverable is connected screen navigation with consistent sample context, not connected data or a fully functioning learning product.

## 25. Agent review and corrections

An independent agent reviewed the initial specification after the visual-only clarification. The parent separately inspected the past-paper reviewer source. Findings and document corrections:

| Finding | Correction |
| --- | --- |
| Product persistence/auth/timing requirements overwhelmed the UI brief | Controlling visual-only contract; sample scenarios; visual acceptance gates; no recording or service connections |
| Add subject always returned Dashboard even when opened elsewhere | Caller-aware close, cancel and success; explicit Open subject |
| AS+A2 card click was ambiguous | Visible selected level, separate level pills and unambiguous Subject · Level selector rows |
| Analytics/history player could return to the original paper instead of the chart | Content source separated from launch origin; explicit read-only return paths |
| Review did not define unanswered bookmarks or location of Resolve | Two Review sample variants; Resolve/Undo in player; fixed ten-item queue |
| Read-only answers absent from screen register | P5 read-only state with correct actions and origin-aware Close |
| Games exit alternated vaguely between node and path | Close → node preview → path → Revision; results → Continue path |
| Global analytics/tracker drill-down could lose scope | Explicit scope change and preserved global return chain |
| Calendar lacked exam and empty-day surfaces | C2 detail/empty example, Edit date and contextual Settings return |
| Whole reviewer reuse would import editorial controls, paper-library escape and recording | Section 13.7 specifies visual reuse, omissions, text-first examples and no write/storage calls |

Only this specification and its owning session-log handoff are revised. No prototype screen, database, source question or review record is changed by this review.

Focused agent reread found no further blockers; its remaining screen-register wording corrections are incorporated above. This is document-level review, not a browser interaction or implementation test.

## 26. Populated curriculum and analytics preview — user addition

Use the existing Physics, Biology and Chemistry AS/A2 curriculum titles to make the mockup feel populated. Copy topic, course-module and active lesson IDs/names into a small read-only-derived navigation fixture inside the prototype. Preserve current reviewed lesson order and relationships. Syllabus topic/module names come from local official-source-derived records; lesson titles are the repository's authored lesson plan, not a claim that Cambridge authored those lessons.

Normal Dashboard, Analytics, metric details and Study tracker show fictional values, trends, history and completion states. Explicit New learner/Empty content scenarios may still show intentional empty states. No normal analytics tab should be just an empty card or placeholder where a representative chart/table could demonstrate its intended appearance.

All imported lesson names open the same reusable example notes/questions experience with the selected subject, module and lesson identified in the header. One HTML note and a few repeated questions are enough. A quiet Preview example label distinguishes the reused body from the actual lesson named in the header. Do not populate or import the full notes/question corpus, connect databases, record answers or calculate real progress.

At inspection, active map arrays contain Physics AS/A2 82/65 lessons, Biology 66/66 and Chemistry 97/70. Derive counts from current arrays, not potentially stale declared totals or retired lesson directories. These counts are verification context, not a new curriculum registry or a requirement to author missing content.
