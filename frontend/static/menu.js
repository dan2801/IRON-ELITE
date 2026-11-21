const toggle = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#nav");

function closeMenu() {
  toggle.setAttribute("aria-expanded", "false");
}

toggle.classList.add("is-ready");
toggle.addEventListener("click", () => {
  const isOpen = toggle.getAttribute("aria-expanded") === "true";
  toggle.setAttribute("aria-expanded", String(!isOpen));
});

navigation.addEventListener("click", (event) => {
  if (event.target.closest("a")) closeMenu();
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
    closeMenu();
    toggle.focus();
  }
});
