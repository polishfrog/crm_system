let timerInWeb = 30
let isFocused = true

window.addEventListener('blur', () => isFocused = false)
window.addEventListener('focus', () => isFocused = true)

const timerId = setInterval(() => {
    if (timerInWeb === 0){
        clearInterval(timerId)
        document.title = 'Test - Passed'
    }

    else if(isFocused){
        timerInWeb--
    }
    document.title = `Test will pass in ${timerInWeb}s `
}, 1000)
