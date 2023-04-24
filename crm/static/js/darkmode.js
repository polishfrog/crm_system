const body = document.querySelector("body")
const modeToggle = body.querySelector(".mode-toggle")

modeToggle.addEventListener("click", () =>{
   body.classList.toggle("dark");
});