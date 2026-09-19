const LESSON_METADATA = {
  lessonId: "9702_t11_cm01_l01",
  subjectCode: "9702",
  subjectName: "Physics",
  level: "AS Level",
  topic: "Topic 11: Particle Physics",
  module: "Module 1: Nuclear structure and nuclides",
  title: "The nuclear atom and alpha-particle scattering",
  total_pages: 8,
  outcomes: [
    { code: "9702_t11_m01_o01", text: "Infer the existence and small size of the nucleus from alpha-particle scattering." },
    { code: "9702_t11_m01_o02", text: "Describe a simple nuclear model of the atom." }
  ]
};

const LESSON_PAGES = [
  {
    pageNumber: 1, pageCode: "L01-P01", title: "The scattering puzzle",
    subtitle: "A particle that seems to turn around", badge: "Notice · Predict",
    imageSrc: "images/9702_t11_cm01_l01_P01.png", provenance: "Verified lesson page · PASS",
    teachingJob: "Notice the surprising result before explaining it.",
    notesHtml: `<div class="note-section compact-note">
      <div class="section-badge tag-hook">Teacher explanation</div>
      <h3 class="section-title">What should you notice?</h3>
      <p class="lead-text">Alpha particles are fired at a very thin metal foil. Most carry on almost straight, but a tiny number turn through a large angle.</p>
      <div class="callout callout-insight"><div class="callout-header"><strong>The surprising part</strong></div><div class="callout-body">A fast particle does not reverse direction for no reason. Something inside the atom must exert a strong force on it.</div></div>
      <h4 class="subsection-title">Keep these separate</h4>
      <table class="data-table"><tbody><tr><th>Observation</th><td>A very small number turn through a large angle.</td></tr><tr><th>Question</th><td>What inside the atom could cause such a strong change in direction?</td></tr></tbody></table>
      <div class="mini-check"><strong>Think first:</strong> should the cause be spread throughout the atom, or concentrated in one small region?</div>
    </div>`
  },
  {
    pageNumber: 2, pageCode: "L01-P02", title: "Use each observation",
    subtitle: "Straight paths and slight deflections", badge: "Explain · Infer",
    imageSrc: "images/9702_t11_cm01_l01_P02.png", provenance: "Verified lesson page · PASS",
    teachingJob: "Link the two common paths to two careful inferences.",
    notesHtml: `<div class="note-section compact-note">
      <div class="section-badge tag-explain">Teacher explanation</div>
      <h3 class="section-title">Let the path tell you what happened</h3>
      <p class="lead-text">If an alpha particle travels straight through, it did not experience a strong sideways force. This happens to most particles, so most of the atom must be empty space.</p>
      <div class="path-key"><div><span class="path-line straight"></span><strong>Straight path</strong><small>no strong encounter</small></div><div><span class="path-line curved"></span><strong>Slight bend</strong><small>weak repulsion from farther away</small></div></div>
      <div class="callout callout-setup"><div class="callout-header"><strong>Important wording</strong></div><div class="callout-body">“Most pass straight through” is the observation. “Most of the atom is empty space” is the inference.</div></div>
      <div class="mini-check"><strong>Cambridge habit:</strong> state what was seen before stating what it tells us.</div>
    </div>`
  },
  {
    pageNumber: 3, pageCode: "L01-P03", title: "Large deflections",
    subtitle: "A small, positive nucleus", badge: "Explain · Cause",
    imageSrc: "images/9702_t11_cm01_l01_P03.png", provenance: "Verified lesson page · PASS",
    teachingJob: "Explain why closer alpha particles turn more strongly.",
    notesHtml: `<div class="note-section compact-note">
      <div class="section-badge tag-explain">Teacher explanation</div>
      <h3 class="section-title">Why does the path curve?</h3>
      <p class="lead-text">An alpha particle is positively charged. The nucleus is also positive. Like charges repel, so the nucleus pushes the alpha particle away.</p>
      <div class="cause-chain"><span>closer approach</span><b>→</b><span>stronger repulsion</span><b>→</b><span>larger deflection</span></div>
      <h4 class="subsection-title">What the rare sharp turns reveal</h4>
      <ul class="teacher-list"><li>Only a tiny fraction get close enough to turn sharply, so the nucleus is very small.</li><li>The alpha particle can be sent backwards, so the nucleus contains nearly all the atom’s mass.</li><li>The repulsion shows that the nucleus is positively charged.</li></ul>
      <div class="callout callout-insight"><div class="callout-header"><strong>Definition</strong></div><div class="callout-body"><strong>Nucleus:</strong> the very small, positively charged central region of an atom where nearly all its mass is concentrated.</div></div>
    </div>`
  },
  {
    pageNumber: 4, pageCode: "L01-P04", title: "Count the evidence",
    subtitle: "Reason from 20 000 alpha particles", badge: "Calculate · Interpret",
    imageSrc: "images/9702_t11_cm01_l01_P04.png", provenance: "Verified lesson page · PASS",
    teachingJob: "Turn the counts into simple proportions and physical meaning.",
    notesHtml: `<div class="note-section compact-note">
      <div class="section-badge tag-demo">Teacher explanation</div>
      <h3 class="section-title">The numbers make the pattern clear</h3>
      <table class="data-table evidence-table"><thead><tr><th>Result</th><th>Out of 20 000</th><th>Meaning</th></tr></thead><tbody><tr><td>Straight or almost straight</td><td>19 900 = 99.5%</td><td>Most atomic volume is empty.</td></tr><tr><td>Modest deflection</td><td>98 = 0.49%</td><td>A few pass near the positive nucleus.</td></tr><tr><td>Very large deflection</td><td>2 = 0.01%</td><td>Very few approach it extremely closely.</td></tr></tbody></table>
      <div class="callout callout-setup"><div class="callout-header"><strong>Formula</strong></div><div class="callout-body"><span class="formula">percentage = (number in group ÷ total number) × 100%</span></div></div>
      <p>The rare result matters most. It reveals a tiny region capable of producing a very strong repulsive effect.</p>
    </div>`
  },
  {
    pageNumber: 5, pageCode: "L01-P05", title: "Test the model",
    subtitle: "One model must explain every result", badge: "Compare · Decide",
    imageSrc: "images/9702_t11_cm01_l01_P05.png", provenance: "Verified lesson page · PASS",
    teachingJob: "Choose the model that explains both common and rare paths.",
    notesHtml: `<div class="note-section compact-note">
      <div class="section-badge tag-correct">Teacher explanation</div>
      <h3 class="section-title">A good model explains all the evidence</h3>
      <p class="lead-text">A model with positive charge spread across a large region might cause gentle bending, but it cannot explain why a few alpha particles turn sharply.</p>
      <table class="data-table"><thead><tr><th>Model</th><th>Most go straight?</th><th>A few turn sharply?</th></tr></thead><tbody><tr><td>Mostly empty atom with a tiny positive nucleus</td><td>✓</td><td>✓</td></tr><tr><td>Positive charge spread throughout the atom</td><td>✗</td><td>✗</td></tr></tbody></table>
      <div class="callout callout-insight"><div class="callout-header"><strong>Teacher tip</strong></div><div class="callout-body">Do not choose a model because it explains one path. It must explain the frequent result and the rare result together.</div></div>
    </div>`
  },
  {
    pageNumber: 6, pageCode: "L01-P06", title: "Build the nuclear atom",
    subtitle: "Particles, charges and locations", badge: "Define · Organise",
    imageSrc: "images/9702_t11_cm01_l01_P06.png", provenance: "Verified lesson page · PASS",
    teachingJob: "Organise the simple nuclear model of the atom.",
    notesHtml: `<div class="note-section compact-note">
      <div class="section-badge tag-model">Teacher explanation</div>
      <h3 class="section-title">The simple model</h3>
      <p class="lead-text">The atom has a tiny central nucleus. Protons and neutrons are inside it. Electrons are outside the nucleus.</p>
      <table class="data-table particle-table"><thead><tr><th>Particle</th><th>Charge</th><th>Location</th></tr></thead><tbody><tr><td><span class="particle proton">+</span> Proton</td><td>+e</td><td>Nucleus</td></tr><tr><td><span class="particle neutron">0</span> Neutron</td><td>0</td><td>Nucleus</td></tr><tr><td><span class="particle electron">−</span> Electron</td><td>−e</td><td>Outside nucleus</td></tr></tbody></table>
      <ul class="teacher-list"><li>Nearly all atomic mass is concentrated in the nucleus.</li><li>The atom is much larger than its nucleus.</li><li>The drawing is enlarged and is not to scale.</li></ul>
      <div class="mini-check"><strong>Quick check:</strong> Which two particles are found inside the nucleus?</div>
    </div>`
  },
  {
    pageNumber: 7, pageCode: "L01-P07", title: "Mass is not size",
    subtitle: "Small nucleus, concentrated mass", badge: "Correct · Clarify",
    imageSrc: "images/9702_t11_cm01_l01_P07.png", provenance: "Verified lesson page · PASS",
    teachingJob: "Prevent confusion between mass and volume.",
    notesHtml: `<div class="note-section compact-note">
      <div class="section-badge tag-correct">Teacher explanation</div>
      <h3 class="section-title">Small things can contain most of the mass</h3>
      <p class="lead-text">Mass tells us how much matter is present. Volume tells us how much space something occupies. They are different quantities.</p>
      <div class="mass-volume-grid"><div><strong>Mass</strong><span class="bar mass-bar"></span><small>Nearly all in the nucleus</small></div><div><strong>Volume</strong><span class="bar volume-bar"></span><small>Mostly empty space</small></div></div>
      <div class="callout callout-insight"><div class="callout-header"><strong>Correct statement</strong></div><div class="callout-body">The nucleus is extremely small, but nearly all the atom’s mass is concentrated there.</div></div>
      <div class="mini-check"><strong>Avoid:</strong> “The nucleus is large because it contains most of the mass.”</div>
    </div>`
  },
  {
    pageNumber: 8, pageCode: "L01-P08", title: "Connect the reasoning",
    subtitle: "Observation → interaction → inference", badge: "Summarise · Check",
    imageSrc: "images/9702_t11_cm01_l01_P08.png", provenance: "Verified lesson page · PASS",
    teachingJob: "Practise the complete Cambridge reasoning chain.",
    notesHtml: `<div class="note-section compact-note">
      <div class="section-badge tag-synth">Teacher explanation</div>
      <h3 class="section-title">Use this three-step answer pattern</h3>
      <div class="reasoning-grid"><strong>1. Observation</strong><span>What path was seen?</span><strong>2. Interaction</strong><span>Was there no, weak or strong repulsion?</span><strong>3. Inference</strong><span>What does that reveal about the atom?</span></div>
      <table class="data-table"><tbody><tr><td>Most pass straight</td><td>→</td><td>Most of the atom is empty space.</td></tr><tr><td>A few bend slightly</td><td>→</td><td>Positive charge is concentrated.</td></tr><tr><td>Very few turn greatly</td><td>→</td><td>The nucleus is very small and contains nearly all the mass.</td></tr></tbody></table>
      <div class="callout callout-setup"><div class="callout-header"><strong>Say it aloud</strong></div><div class="callout-body">“I observed … This means the alpha particle experienced … Therefore …”</div></div>
      <div class="mini-check"><strong>Lesson boundary:</strong> nuclide notation and isotopes come next.</div>
    </div>`
  }
];
