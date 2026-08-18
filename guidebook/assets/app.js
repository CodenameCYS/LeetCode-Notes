document.addEventListener("DOMContentLoaded", () => {
  if (window.renderMathInElement) {
    window.renderMathInElement(document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false }
      ],
      throwOnError: false
    });
  }

  const searchInput = document.querySelector("[data-search-input]");
  if (searchInput) {
    const algorithms = [...document.querySelectorAll(".algorithm")];
    const chapters = [...document.querySelectorAll(".chapter")];
    const empty = document.querySelector("[data-no-results]");
    searchInput.addEventListener("input", () => {
      const query = searchInput.value.trim().toLowerCase();
      let visible = 0;
      algorithms.forEach((algorithm) => {
        const match = !query || algorithm.textContent.toLowerCase().includes(query);
        algorithm.classList.toggle("filtered-out", !match);
        if (match) visible += 1;
      });
      chapters.forEach((chapter) => {
        const hasMatch = !query || [...chapter.querySelectorAll(".algorithm")].some((item) => !item.classList.contains("filtered-out"));
        chapter.classList.toggle("filtered-out", !hasMatch);
      });
      if (empty) empty.hidden = visible > 0;
    });
  }

  const sidebar = document.querySelector(".sidebar");
  if (sidebar) {
    const revealCurrentNavigation = () => {
      const currentHash = decodeURIComponent(window.location.hash);
      if (!currentHash) return;
      const currentLink = [...sidebar.querySelectorAll('a[href^="#"]')].find(
        (link) => decodeURIComponent(link.getAttribute("href")) === currentHash
      );
      if (!currentLink) return;

      sidebar.querySelectorAll("a.is-active").forEach((link) => link.classList.remove("is-active"));
      currentLink.classList.add("is-active");
      let parentDetails = currentLink.closest("details");
      while (parentDetails) {
        parentDetails.open = true;
        parentDetails = parentDetails.parentElement.closest("details");
      }
      window.requestAnimationFrame(() => currentLink.scrollIntoView({ block: "nearest" }));
    };

    revealCurrentNavigation();
    window.addEventListener("hashchange", revealCurrentNavigation);
  }

  const mapSearch = document.querySelector("[data-map-search]");
  if (mapSearch) {
    const chapters = [...document.querySelectorAll(".map-chapter")];
    const branches = [...document.querySelectorAll(".map-branch")];
    const empty = document.querySelector("[data-map-empty]");
    mapSearch.addEventListener("input", () => {
      const query = mapSearch.value.trim().toLowerCase();
      let visible = 0;
      chapters.forEach((chapter) => {
        const match = !query || chapter.dataset.search.includes(query);
        chapter.classList.toggle("filtered-out", !match);
        if (match) visible += 1;
      });
      branches.forEach((branch) => {
        const hasMatch = !query || [...branch.querySelectorAll(".map-chapter")].some((item) => !item.classList.contains("filtered-out"));
        branch.classList.toggle("filtered-out", !hasMatch);
      });
      if (empty) empty.hidden = visible > 0;
    });
  }
});