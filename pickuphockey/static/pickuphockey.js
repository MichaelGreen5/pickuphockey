// function Alerts(button_id, display_message){ 

// const alertPlaceholder = document.getElementById('liveAlertPlaceholder')

// const alert = (message, type) => {
//   const wrapper = document.createElement('div')
//   wrapper.innerHTML = [
//     `<div class="alert alert-${type} alert-dismissible" role="alert">`,
//     `   <div>${message}</div>`,
//     '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
//     '</div>'
//   ].join('')

//   alertPlaceholder.append(wrapper)
// }

// const alertTrigger = document.getElementById(button_id)
// if (alertTrigger) {
//   alertTrigger.addEventListener('click', () => {
//     alert(display_message)
//   })
// }
// }



function DisplayMessage(target_div){
    const alertPlaceholder = document.getElementById(target_div)
      
    const alert = (message, type) => {
    const wrapper = document.createElement('div')
    wrapper.innerHTML = [
    `<div class="alert alert-success alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
    ].join('')
    
    alertPlaceholder.append(wrapper)
    }
    $(document).ready(function() {
    alert('{{message}}')
    });
};