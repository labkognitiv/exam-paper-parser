/**
 * Application Controller for Particle Physics Lesson 1 Reviewer
 * Subject: Cambridge Physics 9702
 */

(function () {
  "use strict";

  let currentPageIndex = 0;
  const totalPages = LESSON_PAGES.length;

  // DOM Elements
  const pageNav = document.getElementById("page-nav");
  const btnPrev = document.getElementById("btn-prev");
  const btnNext = document.getElementById("btn-next");
  const pageCounter = document.getElementById("page-counter");

  // Left Panel Elements
  const notesTitle = document.getElementById("notes-page-title");
  const notesSubtitle = document.getElementById("notes-page-subtitle");
  const notesTeachingJob = document.getElementById("notes-teaching-job");
  const notesBody = document.getElementById("notes-body");

  // Right Panel Elements
  const visualStatus = document.getElementById("visual-status");
  const visualFilename = document.getElementById("visual-filename");
  const visualProvenance = document.getElementById("visual-provenance");
  const lessonImage = document.getElementById("lesson-image");
  const btnFitHeight = document.getElementById("btn-fit-height");
  const btnZoomModal = document.getElementById("btn-zoom-modal");

  // Dialog Elements
  const zoomDialog = document.getElementById("zoom-dialog");
  const dialogTitle = document.getElementById("dialog-title");
  const dialogImg = document.getElementById("dialog-img");
  const dialogClose = document.getElementById("dialog-close");

  /**
   * Safe KaTeX render for element
   */
  function renderMath(element) {
    if (typeof renderMathInElement === "function") {
      renderMathInElement(element, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false },
          { left: "\\(", right: "\\)", display: false },
          { left: "\\[", right: "\\]", display: true }
        ],
        throwOnError: false
      });
    } else if (typeof katex !== "undefined") {
      // Inline text replacement if auto-render extension is not loaded
      const textNodes = [];
      const walk = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, false);
      let n;
      while ((n = walk.nextNode())) textNodes.push(n);

      for (const node of textNodes) {
        const text = node.nodeValue;
        if (text && (text.includes("$") || text.includes("\\[") || text.includes("\\("))) {
          const parent = node.parentNode;
          if (parent && parent.tagName !== "SCRIPT" && parent.tagName !== "STYLE") {
            const span = document.createElement("span");
            span.innerHTML = text
              .replace(/\$\$([\s\S]+?)\$\$/g, (_, eq) => {
                try {
                  return katex.renderToString(eq.trim(), { displayMode: true });
                } catch {
                  return `$$${eq}$$`;
                }
              })
              .replace(/\$([^\$\n]+?)\$/g, (_, eq) => {
                try {
                  return katex.renderToString(eq.trim(), { displayMode: false });
                } catch {
                  return `$${eq}$`;
                }
              });
            parent.replaceChild(span, node);
          }
        }
      }
    }
  }

  /**
   * Build Top Navigation Pills
   */
  function buildNavTabs() {
    pageNav.innerHTML = "";
    LESSON_PAGES.forEach((page, idx) => {
      const tab = document.createElement("button");
      tab.className = `nav-tab ${idx === currentPageIndex ? "active" : ""}`;
      tab.innerHTML = `<span class="tab-num">P0${page.pageNumber}</span> ${page.badge.split("·")[0].trim()}`;
      tab.title = `${page.title}: ${page.subtitle}`;
      tab.addEventListener("click", () => goToPage(idx));
      pageNav.appendChild(tab);
    });
  }

  /**
   * Render Page by Index
   */
  function renderPage(index) {
    if (index < 0 || index >= totalPages) return;
    currentPageIndex = index;

    const page = LESSON_PAGES[index];

    // Update Header Navigation Tabs
    const tabs = pageNav.querySelectorAll(".nav-tab");
    tabs.forEach((tab, idx) => {
      tab.classList.toggle("active", idx === currentPageIndex);
    });

    // Update Counter & Controls
    pageCounter.textContent = `${index + 1} / ${totalPages}`;
    btnPrev.disabled = index === 0;
    btnNext.disabled = index === totalPages - 1;

    // Update Left Panel
    notesTitle.textContent = `${page.pageCode}: ${page.title}`;
    notesSubtitle.textContent = page.subtitle;
    notesTeachingJob.textContent = page.badge;
    notesBody.innerHTML = page.notesHtml;

    // Render Math in Notes
    renderMath(notesBody);

    // Scroll Left Panel to Top
    notesBody.scrollTop = 0;

    // Update Right Panel (Visual Image)
    lessonImage.src = page.imageSrc;
    lessonImage.alt = `${page.title} (${page.pageCode})`;
    dialogImg.src = page.imageSrc;

    const filename = page.imageSrc.split("/").pop();
    visualFilename.textContent = filename;
    visualProvenance.textContent = `Source provenance: ${page.provenance}`;
    dialogTitle.textContent = `${page.pageCode} — ${page.title} (High-Resolution Inspection)`;

    // Save to LocalStorage
    try {
      localStorage.setItem("9702_l01_current_page", index.toString());
    } catch {
      // Ignore storage errors
    }
  }

  function goToPage(index) {
    renderPage(index);
  }

  function prevPage() {
    if (currentPageIndex > 0) goToPage(currentPageIndex - 1);
  }

  function nextPage() {
    if (currentPageIndex < totalPages - 1) goToPage(currentPageIndex + 1);
  }

  function openZoomModal() {
    zoomDialog.showModal();
  }

  function closeZoomModal() {
    zoomDialog.close();
  }

  // Event Listeners
  btnPrev.addEventListener("click", prevPage);
  btnNext.addEventListener("click", nextPage);

  lessonImage.addEventListener("click", openZoomModal);
  btnZoomModal.addEventListener("click", openZoomModal);
  dialogClose.addEventListener("click", closeZoomModal);

  zoomDialog.addEventListener("click", (e) => {
    if (e.target === zoomDialog) closeZoomModal();
  });

  btnFitHeight.addEventListener("click", () => {
    lessonImage.style.width = "100%";
    lessonImage.style.height = "100%";
    lessonImage.style.objectFit = "contain";
  });

  // Global Keyboard Navigation
  window.addEventListener("keydown", (e) => {
    // If modal is open, let Escape close it
    if (zoomDialog.open) {
      if (e.key === "Escape") closeZoomModal();
      return;
    }

    if (e.key === "ArrowLeft" || e.key.toLowerCase() === "p") {
      prevPage();
    } else if (e.key === "ArrowRight" || e.key.toLowerCase() === "n") {
      nextPage();
    } else if (e.key.toLowerCase() === "z") {
      openZoomModal();
    } else if (e.key >= "1" && e.key <= "8") {
      const pageNum = parseInt(e.key, 10) - 1;
      if (pageNum >= 0 && pageNum < totalPages) {
        goToPage(pageNum);
      }
    }
  });

  // Initial Boot
  buildNavTabs();

  // Restore previous page if saved
  let initialIndex = 0;
  try {
    const saved = localStorage.getItem("9702_l01_current_page");
    if (saved !== null) {
      const parsed = parseInt(saved, 10);
      if (!isNaN(parsed) && parsed >= 0 && parsed < totalPages) {
        initialIndex = parsed;
      }
    }
  } catch {
    // Default to 0
  }

  renderPage(initialIndex);
})();
