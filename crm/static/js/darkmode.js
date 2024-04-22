const body = document.querySelector("body")
const modeToggle = body.querySelector(".mode-toggle")
const nameMode = body.querySelector(".name-mode")

let whatMode = false

modeToggle.addEventListener("click", () =>{
   body.classList.toggle("dark")
   if (whatMode === false){
      nameMode.innerHTML = "Light Mode"
      whatMode = true
   }
   else if(whatMode === true){
      nameMode.innerHTML = "Dark Mode"
      whatMode = false
   }


});