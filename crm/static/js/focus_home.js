let timerInWeb = 20
let isFocused = true

window.addEventListener('blur', () => isFocused = false)
window.addEventListener('focus', () => isFocused = true)

const timerId = setInterval(() => {
    document.title = `Test will pass in ${timerInWeb}s `
    if (timerInWeb === 0){
        clearInterval(timerId)
        document.title = 'Test - Passed'
    }

    else if(isFocused){
        timerInWeb--
    }

}, 1000)
